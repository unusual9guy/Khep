import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Khep',
  description:
    'Packing and shipping automation for Chitra Goenka Crafts & Creations.',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
