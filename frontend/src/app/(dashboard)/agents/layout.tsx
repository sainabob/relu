import { Metadata } from 'next';
import { redirect } from 'next/navigation';

export const metadata: Metadata = {
  title: 'Worker Conversation | Relu',
  description: 'Interactive Worker conversation powered by Relu',
  openGraph: {
    title: 'Worker Conversation | Relu',
    description: 'Interactive Worker conversation powered by Relu',
    type: 'website',
  },
};

export default async function AgentsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <>{children}</>;
}
