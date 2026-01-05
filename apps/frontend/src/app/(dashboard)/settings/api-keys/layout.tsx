import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'API Keys | Relu',
  description: 'Manage your API keys for programmatic access to Relu',
  openGraph: {
    title: 'API Keys | Relu',
    description: 'Manage your API keys for programmatic access to Relu',
    type: 'website',
  },
};

export default async function APIKeysLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
