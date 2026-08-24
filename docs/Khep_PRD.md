# Khep — Product Requirements Document

**Version:** 1.0  
**Author:** Suyash (Chitra Goenka Crafts & Creations)  
**Status:** Ready for Development  
**Scope:** Packing & Shipping Automation (Phase 1)

---

## Problem Statement

Chitra Goenka Crafts & Creations is a D2C home decor brand selling on multiple Indian e-commerce platforms — Amazon, Myntra, Flipkart, and Pepperfry. Each platform generates daily shipping invoices as PDFs, which must be manually read and reconciled before warehouse staff can begin packing orders.

The current process is entirely manual:

- An admin downloads PDFs from each platform seller portal and reads them to understand what needs to be packed.
- Staff receive verbal or written instructions on which orders to pack and which products to pick from shelves.
- There is no centralised system, so information is fragmented across WhatsApp messages, printed sheets, and personal memory.
- Two staff members can inadvertently pack the same order, causing wasted effort and potential shipping errors.
- There is no accountability mechanism — no audit trail of who packed what, or when.
- Product verification is purely visual and informal; staff cannot reliably confirm they have the right SKU for multi-SKU or combo orders.
- Platform SKUs differ from the internal product catalog SKUs, requiring manual cross-referencing every time.

This creates errors, delays, and operational chaos that will only worsen as order volume grows.

---

## Solution

Khep is a lightweight internal SaaS application that automates the flow from PDF invoice upload to packing confirmation. It has two actors: the **Admin** and **Staff**.

The Admin uploads a platform PDF once. Khep automatically parses it, maps platform SKUs to internal catalog SKUs, resolves combo products into their component items, routes orders to the correct dispatch date, and makes the structured data available to all staff instantly via real-time updates.

Staff log in on their personal mobile devices and see a date-organised interface: a summary card showing all items needed for the day (for bulk shelf picking), followed by platform-wise accordions containing individual orders. Each order shows full product details including watermarked images. Staff pack each order, scan the barcode on the shipping label to confirm the correct AWB, and the system marks the order complete — automatically disappearing it from all other staff screens. A points and leaderboard system incentivises speed and accuracy.

The Admin receives real-time notifications as each order is packed and can view a read-only Staff View to monitor packing progress at any time.

---

## User Stories

### Admin — Authentication & Setup

1. As an admin, I want to log in with an email and password, so that only authorised users can access the admin dashboard.
2. As an admin, I want my session to persist across browser refreshes, so that I do not have to log in every time I open the dashboard.
3. As an admin, I want to upload a Master Catalog Excel file with all product data, so that the system can resolve platform SKUs to internal SKUs during PDF parsing.
4. As an admin, I want the Master Catalog to support multiple Platform SKUs per product (Amazon, Myntra, Flipkart, Pepperfry), so that a single internal product is correctly recognised regardless of which platform's PDF is being parsed.
5. As an admin, I want to define combo SKUs in the Master Catalog with an open-ended list of component products, so that combo orders are automatically expanded into individual line items.
6. As an admin, I want to upload product images that are linked to internal SKUs, so that staff can see watermarked product visuals during packing.

### Admin — Invoice Upload

7. As an admin, I want to upload a PDF invoice from any supported platform (Amazon, Myntra, Flipkart, Pepperfry) through the dashboard, so that orders are parsed and available to staff without any manual data entry.
8. As an admin, I want the system to automatically identify which platform a PDF belongs to, so that I do not have to specify this manually.
9. As an admin, I want the uploaded PDF to be stored securely in cloud storage, so that I have a permanent audit record of each invoice.
10. As an admin, I want the system to extract every order from the uploaded PDF, including multi-order PDFs, so that no order is missed.
11. As an admin, I want each order's Platform Order ID to be extracted and stored, so that every packed order can be traced back to its platform reference.
12. As an admin, I want each order's AWB (Airway Bill) number to be extracted and stored, so that it can be validated against the physical shipping label barcode during packing.
13. As an admin, I want each order's dispatch date to be read from the PDF and used to file the order under the correct date, so that orders scheduled for future dates are not mixed with today's orders.
14. As an admin, I want Myntra orders (which have no explicit ship date in the PDF) to be filed under the upload date as a proxy dispatch date, so that no Myntra order is lost due to missing date metadata.
15. As an admin, I want a single PDF that contains orders spanning multiple dispatch dates to correctly separate those orders by date, so that an Aug 25 order inside an Aug 23 invoice is visible to staff on Aug 25, not Aug 23.
16. As an admin, I want each extracted platform SKU to be looked up in the Master Catalog, so that it is resolved to the correct Internal SKU and product name.
17. As an admin, I want orders containing unrecognised platform SKUs to be flagged and held, so that I can resolve mapping issues before staff attempt to pack them.
18. As an admin, I want combo SKUs to be automatically expanded into their component line items during parsing, so that staff see individual products rather than an opaque bundle label.
19. As an admin, I want parsed orders to appear in my dashboard in real-time as they are processed, so that I can see parsing progress without refreshing the page.

### Admin — Dashboard & Monitoring

20. As an admin, I want to see all orders organised by dispatch date in the dashboard, so that I have a clear picture of today's and upcoming workload.
21. As an admin, I want to see the real-time status of each order (pending / packed), so that I know packing progress without asking staff.
22. As an admin, I want to receive a real-time notification each time an order is marked packed, showing the Order ID, AWB, platform, staff member who packed it, and timestamp, so that I can perform spot-check human-in-the-loop verification.
23. As an admin, I want to open a Staff View from the admin dashboard, so that I can see exactly what any staff member sees — including the summary card, platform accordions, and order details.
24. As an admin, I want the Staff View to be read-only and clearly labelled "Staff View" in the admin panel, so that I cannot accidentally take actions that corrupt staff data.
25. As an admin, I want to be notified when a staff member scans the wrong AWB barcode for an order, so that I can investigate packing errors in real time.
26. As an admin, I want to see the full security log of AWB mismatch events including which staff member triggered them, so that I have a complete audit trail for every packing error.

### Staff — Authentication

27. As a staff member, I want to log in on my personal mobile device with an email and password, so that my packing activity is attributed to my account.
28. As a staff member, I want my session to persist across browser sessions and phone restarts, so that I do not have to log in at the start of every shift.
29. As a staff member, I want my access to be limited to the packing interface only, so that I cannot view the admin dashboard, other staff's accounts, or any data I should not see.

### Staff — Home Screen & Date Navigation

30. As a staff member, I want to see a horizontal scrollable row of date pills on the home screen, so that I can see at a glance which dates have orders waiting.
31. As a staff member, I want completed date pills to display a ✓ badge, so that I know which days have been fully packed without opening them.
32. As a staff member, I want future date pills to be visible but visually distinct, so that I am aware of upcoming workload while remaining focused on today.
33. As a staff member, I want to tap a date pill to load all orders for that date, so that I can begin working on that day's packing.

### Staff — Summary Card

34. As a staff member, I want to see a summary card after tapping a date pill, so that I can understand the total items I need to collect from the shelves in one bulk run.
35. As a staff member, I want the summary card to show consolidated product totals across all platforms for that date (product image, product name, internal SKU, size, total qty), so that I do not have to add up quantities manually across platforms.
36. As a staff member, I want the summary card to be read-only and clearly informational, so that there is no ambiguity that it is not a packing checklist.
37. As a staff member, I want the summary card to use real product images pulled from the catalog, so that I can visually identify items on the shelf quickly.

### Staff — Platform Accordions & Order Details

38. As a staff member, I want to see platform accordions (Amazon, Myntra, Flipkart, Pepperfry) below the summary card, so that orders are grouped by the platform they came from.
39. As a staff member, I want each accordion to show the count of pending orders for that platform as a badge, so that I can prioritise which platform to work on first.
40. As a staff member, I want orders inside each platform accordion to be sorted by dispatch deadline in ascending order (earliest deadline first), so that I always pack the most urgent order first.
41. As a staff member, I want to expand an order row to see its full details, so that I know exactly what to pack before I begin.
42. As a staff member, I want the expanded order to display the following fields without ambiguity:
    - **Order header:** Platform Order ID · AWB number · Dispatch deadline · Platform name
    - **Per line item:** Product thumbnail · Product name · Internal SKU · Platform SKU · Size · Quantity
    - **For combos:** Combo SKU shown as a parent label with each component expanded as its own line (Internal SKU · name · size · qty)
    - **Packing note** (if any added by admin)
    so that no data is missing and I can pack with full confidence.
43. As a staff member, I want to tap a product thumbnail to open a full-screen watermarked product view, so that I can visually verify I have picked the correct product from the shelf.
44. As a staff member, I want the full-screen product view to display a watermark showing my staff ID and session code overlaid on the image, so that screenshots of product images are traceable to me.
45. As a staff member, I want screenshot prevention to be active on the full-screen product view, so that product images cannot be casually captured and shared outside the system.
46. As a staff member, I want to close the full-screen product view by swiping or tapping the ✕ button and repeat for each product in the order, so that I can verify every item systematically.

### Staff — Scanning & Packing Confirmation

47. As a staff member, I want a "Scan Label" button at the order level, so that I can confirm packing by scanning the physical shipping label on the box.
48. As a staff member, I want the barcode scan to happen in-browser via my phone camera without installing any native app, so that setup is frictionless.
49. As a staff member, I want the system to decode the barcode using ZXing.js and compare the scanned AWB against the order's stored AWB, so that the correct package is confirmed before the order is marked packed.
50. As a staff member, I want an immediate success confirmation when the scanned AWB matches the order, so that I know the order has been recorded as packed.
51. As a staff member, I want a clear warning message when the scanned AWB does not match the order, so that I know immediately that I have the wrong package.
52. As a staff member, I want AWB mismatches to deduct 10 points from my account, so that there is an accountability mechanism for scanning errors.
53. As a staff member, I want the order to remain open and unconfirmed after an AWB mismatch, so that I must resolve the correct package before packing proceeds.

### Staff — Real-time Coordination (Anti Double-Packing)

54. As a staff member, I want a successfully packed order to immediately disappear from my screen and all other staff screens, so that no two staff members ever pack the same order.
55. As a staff member, I want to see a message "Order #XXX already packed — pick up pace 😤" when an order I was viewing has been packed by someone else, so that I am immediately redirected without confusion.
56. As a staff member, I want the screen updates to happen in real-time without any page refresh, so that the coordination mechanism is seamless during busy packing sessions.

### Staff — Auto-Complete Chain

57. As a staff member, I want a platform accordion to automatically show a ✓ badge and collapse when all its orders for the day are packed, so that I have a clear visual cue that a platform is done.
58. As a staff member, I want the date pill to automatically show a ✓ badge when all platform accordions for that date are complete, so that I know the full day's packing is done without counting manually.

### Staff — Points, Leaderboard & Session Summary

59. As a staff member, I want to earn 10 points for every order I successfully pack, so that my packing activity is quantified and rewarded.
60. As a staff member, I want to earn an additional 5 speed bonus points when I pack an order within the target time, so that working efficiently is incentivised.
61. As a staff member, I want to see a session summary screen when all orders for a date are packed, showing: total orders packed, points earned in this session, and my current leaderboard rank, so that I feel a sense of accomplishment at the end of a shift.
62. As a staff member, I want to see a leaderboard showing point rankings across all staff, so that there is healthy competitive motivation to pack faster and more accurately.

---

## Implementation Decisions

### Architecture

**Khep is a three-tier architecture:**

1. **Frontend** — Next.js 14 (App Router), deployed on Vercel. Handles all UI for both admin and staff. Communicates with Supabase directly for auth, DB reads, and Realtime; and with the Parse Service for PDF parsing.

2. **Parse Service** — Python/FastAPI microservice deployed on Render.com free tier. Accepts a PDF storage URL, downloads the file, parses it with `pymupdf` (coordinate-based extraction), and returns structured order JSON. Stateless — no DB access; all writes happen in the Next.js layer after receiving the parsed response.

3. **Supabase** — Managed PostgreSQL as the primary database, Auth for both admin and staff identity, Realtime for live subscriptions, and Storage for uploaded PDF files.

**Cloudflare R2** stores all product images. The R2 object URL per SKU is stored as a column in the Supabase `products` table. Zero egress cost and 10 GB free tier make it suitable for catalog-scale image hosting.

---

### PDF Parsing Module (Parse Service)

- `pymupdf` (fitz) is used over `pdf.js` or `unpdf` because it extracts word-level bounding boxes `(x0, y0, x1, y1)` per word, allowing text to be reconstructed by spatial position rather than stream order. This is immune to multi-column layout scrambling common in platform invoices.
- The Parse Service receives a Supabase Storage signed URL, downloads the PDF, and performs extraction entirely in memory — no disk writes on Render.
- Platform is identified from PDF structural patterns and/or filename conventions. Detection logic is encapsulated in a `PlatformDetector` class so new platforms can be added without changing the extraction pipeline.
- Each platform has its own `Extractor` class implementing a common `extract(pages) -> List[RawOrder]` interface. Extractors use coordinate-based region heuristics (header zone, line-item zone, footer zone) to locate fields reliably.
- **Dispatch date routing:** Each `RawOrder` carries its own `dispatch_date` field extracted from the PDF. For Myntra (no explicit ship date), the service receives the upload timestamp and writes it as `dispatch_date`. The Next.js layer stores each order under its `dispatch_date`, not the upload date.
- Combo detection happens in Next.js after receiving parsed data, by looking up `platform_sku` in the `combo_skus` table and expanding components. The Parse Service is unaware of the catalog.
- The Parse Service returns a JSON array of `RawOrder` objects. The interface is stable:

```
RawOrder {
  platform_order_id: string
  awb: string
  dispatch_date: string        # ISO date YYYY-MM-DD
  line_items: [
    {
      platform_sku: string
      quantity: int
    }
  ]
}
```

---

### Database Schema (Supabase / PostgreSQL)

**`products`** — Master Catalog (one row per internal product)
- `id` (uuid, PK)
- `internal_sku` (text, unique)
- `name` (text)
- `size` (text)
- `image_url` (text — Cloudflare R2 URL)
- `amazon_sku`, `myntra_sku`, `flipkart_sku`, `pepperfry_sku` (text, nullable)
- `created_at`, `updated_at` (timestamptz)

**`combo_skus`** — Combo definitions (one row per component)
- `id` (uuid, PK)
- `combo_internal_sku` (text — references `products.internal_sku`)
- `component_internal_sku` (text — references `products.internal_sku`)
- `component_qty` (int)

**`orders`** — One row per order
- `id` (uuid, PK)
- `platform` (enum: amazon | myntra | flipkart | pepperfry)
- `platform_order_id` (text)
- `awb` (text)
- `dispatch_date` (date)
- `status` (enum: pending | packed)
- `packed_by` (uuid, FK → `auth.users`, nullable)
- `packed_at` (timestamptz, nullable)
- `invoice_id` (uuid, FK → `invoices`)
- `packing_note` (text, nullable)
- `created_at` (timestamptz)

**`order_line_items`** — One row per line item (after combo expansion)
- `id` (uuid, PK)
- `order_id` (uuid, FK → `orders`)
- `internal_sku` (text, FK → `products.internal_sku`)
- `platform_sku` (text)
- `quantity` (int)
- `is_combo_component` (bool)
- `parent_combo_sku` (text, nullable — the combo SKU this component belongs to)

**`invoices`** — One row per uploaded PDF
- `id` (uuid, PK)
- `platform` (enum)
- `storage_path` (text — Supabase Storage path)
- `upload_date` (date)
- `uploaded_by` (uuid, FK → `auth.users`)
- `parse_status` (enum: pending | processing | done | error)
- `created_at` (timestamptz)

**`staff_points`** — Points ledger (one row per event)
- `id` (uuid, PK)
- `user_id` (uuid, FK → `auth.users`)
- `order_id` (uuid, FK → `orders`, nullable)
- `delta` (int — positive or negative)
- `reason` (enum: packed | speed_bonus | awb_mismatch)
- `created_at` (timestamptz)

**`security_events`** — Audit log for packing errors
- `id` (uuid, PK)
- `user_id` (uuid, FK → `auth.users`)
- `order_id` (uuid, FK → `orders`)
- `event_type` (enum: awb_mismatch)
- `scanned_awb` (text)
- `expected_awb` (text)
- `created_at` (timestamptz)

---

### Authentication & Access Control (Supabase Auth + RLS)

- Two roles: `admin` and `staff`. Role stored as a `role` claim in the Supabase `auth.users` metadata.
- **Admin RLS:** Full read/write access to all tables.
- **Staff RLS:**
  - `orders`: SELECT only on orders where `dispatch_date = today OR dispatch_date > today`. UPDATE only on own `packed_by` and `packed_at` fields (via the Next.js API route, not direct DB write).
  - `order_line_items`: SELECT only.
  - `products`: SELECT only.
  - `staff_points`: SELECT only own rows.
  - No access to `invoices`, `security_events`.
- All DB writes that change order status go through Next.js API routes (not direct client mutations) to enforce business logic (AWB validation, points award, Realtime broadcast) as a single transaction.

---

### Master Catalog Upload Module

- Admin uploads the Master Catalog Excel (`.xlsx`) through the admin dashboard.
- The Next.js API route parses the Excel using `xlsx` (SheetJS) in-process — no separate service needed.
- **Sheet 1 — Products:** Each row is upserted into the `products` table keyed on `internal_sku`. Existing products are updated, new ones are inserted.
- **Sheet 2 — Combos:** All existing combo rows for the affected `combo_internal_sku` values are deleted, then new rows are inserted. This handles component list edits cleanly.
- Product image upload is a separate action: admin uploads an image per SKU; it is stored in Cloudflare R2 and the URL is written to `products.image_url`.

---

### Admin Invoice Upload Module

1. Admin selects a PDF → uploaded to Supabase Storage under `/invoices/{uuid}.pdf` → `invoices` row created with `parse_status: pending`.
2. Next.js API route calls the Render Parse Service with a signed Supabase Storage URL + upload timestamp.
3. Parse Service returns `List[RawOrder]`.
4. For each `RawOrder`:
   - Look up each `platform_sku` in `products` using the platform-specific SKU column.
   - If not found: flag order, do not insert, add to admin error list.
   - If found: resolve to `internal_sku`. Check `combo_skus` table; if combo, expand into component line items.
   - Insert `orders` row (with correct `dispatch_date`) and associated `order_line_items` rows.
5. Supabase Realtime broadcasts the new orders to all connected admin and staff clients.
6. Update `invoices.parse_status` to `done` (or `error` on failure).

---

### Staff Packing Module

**Order completion flow (server-side, Next.js API route):**

1. Staff submits scanned AWB + `order_id`.
2. API route fetches `orders.awb` from DB.
3. If AWB does not match: insert `security_events` row; deduct 10 pts via `staff_points` insert; return mismatch error to client.
4. If AWB matches:
   - Update `orders` row: `status = packed`, `packed_by = user_id`, `packed_at = now()`.
   - Insert `staff_points` rows: +10 packed, +5 speed bonus if `packed_at - order.created_at < target_time`.
   - Broadcast Realtime event `order_packed` with `{ order_id, packed_by_name, platform, awb }`.
   - All other clients subscribed to this order's `dispatch_date` remove it from their UI on receiving the event.

**Realtime subscription:**
- Staff clients subscribe to the `orders` table filtered by `dispatch_date`.
- On `order_packed` event: remove order from local state; show taunt toast if the order was visible to another staff member.
- On new order INSERT (from admin parsing): add order to local state if it matches the active date pill.

---

### Image Security Module

- Product images are served from Cloudflare R2 via short-lived signed URLs generated server-side and passed to the client. URLs expire after a short window (e.g. 15 minutes) and are not directly downloadable.
- Full-screen image view renders a CSS watermark overlay: `staff_id + session_code` rendered as semi-transparent diagonal text across the image.
- `user-select: none` is applied globally on the image view. Keydown listeners block common screenshot keyboard shortcuts on desktop.
- These are deterrents, not cryptographic guarantees — this is documented as an intentional design decision.

---

### Points & Leaderboard Module

- Points are stored as an immutable ledger in `staff_points` (append-only inserts, no updates).
- Total points per user are computed as `SUM(delta)` grouped by `user_id`.
- Leaderboard is a ranked query over this aggregate.
- Points events:
  - `+10` — order packed successfully
  - `+5` — speed bonus (within target time threshold, configurable)
  - `−10` — AWB mismatch
- Session summary is computed client-side from the Realtime events received during the session (orders packed count, points delta).

---

### Admin Notification Module

- On each successful `order_packed` DB write, the API route publishes a Supabase Realtime broadcast on an `admin_notifications` channel.
- Payload: `{ order_id, platform_order_id, awb, platform, packed_by_name, packed_at }`.
- Admin dashboard maintains a live notification feed panel showing this stream. No third-party push service required.

---

## Testing Decisions

### What makes a good test

Tests should verify **external behaviour** — what the module does given specific inputs — not internal implementation details such as function names, intermediate variables, or the specific algorithm used. A good test remains valid even if the internals are refactored.

### Modules to test

**Parse Service (Python — pytest)**
- Unit test each platform `Extractor` class in isolation using fixture PDF pages (coordinate word lists, not real files).
- Tests cover: correct field extraction (order ID, AWB, dispatch date, line items), multi-order PDFs, date routing (future vs. today), Myntra proxy date, malformed/missing fields.
- `PlatformDetector` tested against sample structural signatures.
- Integration test: full `POST /parse` endpoint with real minimal PDFs for each platform. Asserts the returned `RawOrder` JSON schema.

**Next.js API Routes (Jest / Vitest)**
- Order completion route: mock Supabase client; test AWB match → points awarded, Realtime broadcast called. Test AWB mismatch → security event inserted, −10 pts, correct error response.
- Invoice upload route: mock Parse Service response; test SKU found → rows inserted correctly. Test unknown SKU → order flagged, no row inserted. Test combo SKU → correct number of component line items.
- Master Catalog upload route: test upsert behaviour for new vs. existing SKUs; test combo sheet diff (components removed, components added).

**Realtime behaviour (Playwright / end-to-end)**
- Two browser contexts (staff A, staff B) both viewing the same date. Staff A scans successfully → assert order disappears from Staff B's view and taunt message appears. This is the core anti-double-pack guarantee and must be covered by an E2E test.

**Points ledger (unit)**
- Test that `SUM(delta)` aggregate is correct after a sequence of packed/mismatch events.
- Test that speed bonus is awarded only when `packed_at - order_visible_at < threshold`.

**RLS policies (Supabase SQL tests or pgTAP)**
- Assert staff cannot read `invoices` or `security_events`.
- Assert staff cannot UPDATE another staff member's packed order.
- Assert admin has full access.

---

## Out of Scope

The following are explicitly deferred to future phases and must not be built or partially implemented in Phase 1:

- **Inventory management** — Tracking stock levels, deducting inventory on pack, low-stock alerts. Deferred pending a decision on whether inventory is seeded from the Master Catalog or managed separately.
- **Web Push / native push notifications** — Supabase Realtime covers all live update requirements. No service worker or push notification infrastructure is needed in Phase 1.
- **Automated order handoff to courier APIs** — No integration with Shiprocket, Delhivery, or any courier platform in Phase 1.
- **Returns / RTO management** — Return-to-origin order flows are not in scope.
- **Multi-warehouse / multi-location** — Khep assumes a single packing location.
- **Customer-facing features** — No customer portal, tracking pages, or communications.
- **Platform seller portal automation** — PDF download from seller portals is manual; the admin downloads and uploads. No web scraping or seller API integration.
- **Analytics & reporting dashboards** — Phase 1 includes only the live packing feed. Historical analytics, order volume trends, and staff performance reports are deferred.
- **Mobile native app** — The staff interface is a mobile-optimised Progressive Web App (PWA). No native iOS/Android app is planned.
- **Bulk order editing** — Admin cannot edit parsed orders in Phase 1. Incorrect data must be corrected via a re-upload.

---

## Further Notes

### Platform PDF Characteristics

Each platform invoice PDF has a distinct structure. The Parse Service must handle:

| Platform   | Dispatch Date Source          | Known Structural Challenges                          |
|------------|-------------------------------|------------------------------------------------------|
| Amazon     | Explicit in PDF per order     | Multi-order PDFs; line items can span pages          |
| Myntra     | None — use upload date        | Bundled shipment manifests; barcode-only AWB         |
| Flipkart   | Explicit per order            | Dense tabular format; combo SKUs common              |
| Pepperfry  | Explicit per order            | Low volume; simpler single-order PDFs                |

### Combo SKU Philosophy

Combo SKUs have no hard component limit. The Master Catalog Combos sheet defines as many component rows per combo as needed. Staff always see individual components — the combo label is shown as a parent grouping header only, never as a single opaque line item.

### Points Target Time Threshold

The speed bonus threshold (time within which an order must be packed to earn +5 pts) is a configurable value stored in the database or environment config. The initial value should be agreed upon after observing real packing times in the first few weeks of operation. It is not hardcoded.

### Supabase Realtime — Broadcast vs. DB events

The `order_packed` event must be broadcast immediately via the Realtime Broadcast API (not via DB Change Data Capture) to ensure sub-second delivery across all staff clients. DB CDC has higher latency and is not suitable for the anti-double-pack UX requirement.

### Render.com Parse Service — Cold Start

Render.com free tier spins down inactive services after 15 minutes of inactivity. The first PDF upload after inactivity will experience a cold start delay (typically 30–60 seconds). This is acceptable for Phase 1 given the low upload frequency (once per platform per day). A keep-alive ping can be added later if this proves disruptive.

### Watermark — Design Spec

The watermark overlay on full-screen product images must:
- Display: `Staff: {first_name} {last_initial} · Session: {short_session_code}`
- Appear as semi-transparent diagonal text (opacity ~0.25) repeated across the image
- Be rendered entirely in CSS (no server-side image manipulation) for performance
- Not obscure the product enough to make visual identification impossible

### Security Model — Honest Assessment

The image protection mechanisms (watermark, `user-select: none`, key listeners) are social deterrents, not technical guarantees. A determined person can always photograph the screen with another device. This is an accepted tradeoff for a Phase 1 internal tool. More robust DRM can be evaluated if the threat model requires it.

### Leaderboard Scope

The leaderboard covers all staff across all time (cumulative points). A time-scoped leaderboard (weekly / monthly reset) is a natural future enhancement but is out of scope for Phase 1.
