# Admin Flow — Invoice Upload Spec

## 1. Overview
Admin uploads a platform invoice PDF (Amazon / Myntra / Flipkart / Pepperfry). A backend microservice detects the platform, splits the PDF into per-order page groups, extracts order data, maps each line item against the Master Catalog, expands combos, resolves the dispatch date, and writes each order to Supabase — where it becomes visible to staff in real time. Admin also has a read-only "Staff View" to see exactly what packing staff see.

## 2. Flow (Flowchart)

```mermaid
flowchart TD
    START(["Start"]) --> A1["Admin logs in\n(Supabase Auth)"]
    A1 --> A2["Opens Upload section"]
    A2 --> A3["Selects & uploads PDF\n1 PDF = multiple orders, one platform"]
    A3 --> S1["PDF stored in Supabase Storage"]
    S1 --> S2["Next.js calls Render microservice\n(passes storage file path)"]
    S2 --> S3["pymupdf detects platform from PDF\n(Amazon / Myntra / Flipkart / Pepperfry)"]
    S3 --> S4["PDF split into per-order page groups\nAmazon/Myntra: 2 pg/order · Flipkart/Pepperfry: 1 pg/order"]
    S4 --> LOOP(["↻ repeat per order group"])
    LOOP --> S5["Extract order data:\nOrder ID, Platform SKU, Qty, AWB, Dispatch date"]
    S5 --> S6["Lookup Platform SKU in Master Catalog\n→ Internal SKU + name + dimensions"]
    S6 --> D1{"SKU found in\nMaster Catalog?"}
    D1 -->|No| E1["Flagged: unknown SKU\norder held · admin alerted"]
    D1 -->|Yes| D2{"Combo SKU?"}
    D2 -->|Yes| S7["Expand into component SKUs\n(each its own line item)"]
    D2 -->|No| S8["Single product — continue"]
    S7 --> D3
    S8 --> D3{"Dispatch date ≠\ntoday?"}
    D3 -->|Yes, future| S9["Store under actual dispatch date\n→ correct future date pill in staff view"]
    D3 -->|No, today| S10["Store under today's date"]
    S9 --> S11["Write order row to Supabase\nstatus: pending · dispatch date · timestamp"]
    S10 --> S11
    S11 --> D4{"More order groups\nin this PDF?"}
    D4 -->|Yes| LOOP
    D4 -->|No| S12["All orders in PDF parsed"]
    S12 --> S13["Admin sees parsed orders in real time\n(Supabase Realtime, no refresh)"]
    S13 --> S14["Orders appear in staff pick list automatically"]
    S14 --> A4["Admin can open read-only Staff View\npick list · pack queue · packing screen · order details"]
    A4 --> END(["End"])
```

## 3. Nested Outline

- **Upload**
  - Admin logs in (Supabase Auth)
  - Opens Upload section
  - Selects & uploads a PDF — one PDF = multiple orders, all from **one platform**
- **Ingestion** (automatic, Render microservice)
  - PDF → Supabase Storage → file path passed to Next.js → Render
  - Platform auto-detected from PDF content (pymupdf)
  - PDF split into per-order page groups
    - Amazon / Myntra → 2 pages per order
    - Flipkart / Pepperfry → 1 page per order
- **Per order group** (loop)
  - Extract: Order ID, Platform SKU, Qty, AWB number, Dispatch date
  - Lookup Platform SKU → Master Catalog → Internal SKU + name + dimensions
    - **Not found** → flagged, order held, admin alerted (does not proceed to DB write)
    - **Found** → continue
  - Combo check
    - **Combo** → expand into component SKUs, each written as its own line item
    - **Not combo** → single line item
  - Dispatch date check
    - **Different from today** → stored under its actual dispatch date (Myntra: upload date used as proxy when no explicit date)
    - **Same as today** → stored under today's date
  - Write order row to Supabase — `status: pending`, dispatch date, timestamp
- **Completion**
  - Admin dashboard updates live (Supabase Realtime)
  - Orders appear in staff pick list automatically, no refresh needed
  - Admin can open a **read-only Staff View** — same pick list / pack queue / packing screen / order details staff see

## 4. Suggested Data Model (TypeScript)

```ts
type PlatformName = "Amazon" | "Myntra" | "Flipkart" | "Pepperfry";

interface UploadJob {
  id: string;
  platform: PlatformName;     // auto-detected
  filePath: string;           // Supabase Storage path
  uploadedAt: string;         // ISO timestamp
  orderGroupCount: number;
  status: "processing" | "done";
}

interface ParsedOrder {
  orderId: string;
  platform: PlatformName;
  awb: string;
  dispatchDate: string;       // ISO date — actual ship date, may differ from upload date
  status: "pending" | "flagged";
  lineItems: LineItem[];
  createdAt: string;          // ISO timestamp
}

interface LineItem {
  platformSku: string;
  internalSku: string | null;   // null when unmatched → order flagged
  productName: string | null;
  quantity: number;
  isComboComponent: boolean;
  comboParentSku?: string;      // present when this line is a component of a combo
}

interface MasterCatalogEntry {
  platformSku: string;
  internalSku: string;
  productName: string;
  dimensions: string;
  isCombo: boolean;
  comboComponents?: { internalSku: string; name: string; quantity: number }[];
}
```

## 5. Tech notes (as drawn)

- Auth: Supabase Auth (same as staff)
- File storage: Supabase Storage → file path handed to Next.js
- Parsing: Next.js → Render microservice → pymupdf (platform detection + page-group extraction)
- Persistence: Supabase DB, `status: pending` on write
- Live updates: Supabase Realtime — both admin dashboard and staff pick list update without refresh
- Staff View inside admin dashboard is explicitly **read-only**

## 6. Open questions

1. When a SKU is unmatched and the order is flagged/held, does parsing still continue to the next order group in the same PDF, or does the whole PDF pause? (Diagram shows no return arrow from the flagged node back into the loop.)
2. Is there a resolution path — e.g. admin adds the missing SKU to the Master Catalog and the held order gets reprocessed automatically, or is that a fully manual re-upload?
3. For Myntra's "upload date as proxy" — is that the *only* platform without an explicit dispatch date field, or should the same fallback apply to any platform where the field is missing/unparseable?
