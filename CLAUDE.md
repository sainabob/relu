# CLAUDE.md - AI Assistant Guide for Kortix/Suna

**Last Updated**: 2025-11-28
**Repository**: kortix-ai/suna
**Purpose**: Comprehensive guide for AI assistants working with the Kortix platform codebase

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Technology Stack](#technology-stack)
4. [Development Setup](#development-setup)
5. [Architecture Patterns](#architecture-patterns)
6. [Coding Conventions](#coding-conventions)
7. [Key Workflows](#key-workflows)
8. [Common Development Tasks](#common-development-tasks)
9. [Testing Guidelines](#testing-guidelines)
10. [Database Schema](#database-schema)
11. [API Patterns](#api-patterns)
12. [Troubleshooting](#troubleshooting)
13. [Important Files Reference](#important-files-reference)

---

## Project Overview

### What is Kortix?

Kortix is an **open-source platform for building, managing, and training autonomous AI agents**. The repository contains:

- **Suna**: The flagship generalist AI worker demonstrating platform capabilities
- **Agent Builder**: Tools to create custom specialized agents
- **Platform Infrastructure**: Backend API, frontend dashboard, mobile app, and SDK

### Core Capabilities

- **Browser Automation**: Web scraping, form filling, workflow automation
- **File Management**: Document creation/editing (docs, spreadsheets, presentations, code)
- **Web Intelligence**: Search, crawling, data extraction and synthesis
- **System Operations**: Command-line execution, DevOps tasks
- **API Integrations**: 200+ tools via Composio, MCP server support
- **Multi-LLM Support**: Anthropic, OpenAI, Groq, Gemini, AWS Bedrock, etc.

### Business Model

- **Open Source**: Apache 2.0 license
- **SaaS Platform**: Multi-tenant architecture with Stripe billing
- **Self-Hosting**: Docker-based deployment with setup wizard

---

## Repository Structure

### Monorepo Layout

```
/home/user/suna/
├── backend/              # Python FastAPI backend
│   ├── api.py           # Main FastAPI application entry point
│   ├── run_agent_background.py  # Dramatiq worker for async agent runs
│   ├── pyproject.toml   # UV-managed Python dependencies
│   ├── pytest.ini       # Test configuration
│   ├── Dockerfile       # Backend container
│   ├── supabase/        # Database migrations and config
│   │   ├── migrations/  # SQL schema migrations
│   │   └── config.toml  # Supabase CLI configuration
│   └── core/            # Core application logic
│       ├── agentpress/  # Custom agent execution framework
│       ├── tools/       # Agent tools (browser, files, shell, etc.)
│       ├── sandbox/     # Daytona sandbox integration
│       ├── ai_models/   # LLM model management
│       ├── api_models/  # Pydantic request/response schemas
│       ├── billing/     # Stripe integration
│       ├── mcp_module/  # Model Context Protocol integration
│       ├── composio_integration/  # Composio tools
│       ├── services/    # Shared services (Supabase, Redis, LLM)
│       └── utils/       # Utilities and helpers
│
├── frontend/            # Next.js 15 frontend
│   ├── src/
│   │   ├── app/         # Next.js App Router
│   │   │   ├── (dashboard)/  # Dashboard routes (route group)
│   │   │   │   ├── agents/[threadId]/  # Chat interface
│   │   │   │   ├── settings/           # User settings
│   │   │   │   ├── triggers/           # Workflow triggers
│   │   │   │   └── knowledge/          # Knowledge base
│   │   │   ├── (home)/  # Marketing pages
│   │   │   ├── auth/    # Authentication
│   │   │   └── api/     # API routes
│   │   ├── components/  # React components
│   │   │   ├── ui/      # shadcn/ui base components
│   │   │   ├── thread/  # Chat interface components
│   │   │   ├── agents/  # Agent builder UI
│   │   │   └── shared/  # Reusable components
│   │   ├── lib/         # Libraries and utilities
│   │   │   ├── api/     # API client functions
│   │   │   ├── supabase/  # Supabase client setup
│   │   │   └── utils/   # Helper functions
│   │   ├── hooks/       # React hooks
│   │   └── stores/      # Zustand state management
│   ├── public/          # Static assets
│   ├── translations/    # i18n files
│   ├── package.json     # npm dependencies
│   ├── next.config.ts   # Next.js configuration
│   ├── tsconfig.json    # TypeScript configuration
│   └── Dockerfile       # Frontend container
│
├── apps/
│   └── mobile/          # React Native Expo mobile app
│       ├── app/         # Expo Router screens
│       ├── components/  # React Native components
│       ├── lib/         # Utilities
│       ├── stores/      # Zustand stores
│       ├── api/         # API client
│       ├── ios/         # iOS native config
│       └── android/     # Android native config
│
├── sdk/                 # Python SDK for programmatic agent management
│   └── kortix/
│       ├── kortix.py    # Main SDK class
│       ├── agent.py     # Agent operations
│       ├── thread.py    # Thread operations
│       └── example/     # Usage examples
│
├── docs/                # Documentation and images
├── .github/             # CI/CD workflows
│   └── workflows/
│       ├── docker-build.yml  # Build and deploy
│       ├── mobile-eas-update.yml  # Mobile OTA updates
│       └── update-PROD.yml  # Production deployments
│
├── docker-compose.yaml  # Multi-container orchestration
├── setup.py             # Interactive installation wizard (17 steps)
└── start.py             # Service management script
```

### Key Directories

| Directory | Purpose | Primary Language |
|-----------|---------|------------------|
| `backend/core/agentpress/` | Custom agent execution framework | Python |
| `backend/core/tools/` | Agent tools (browser, files, shell) | Python |
| `backend/supabase/migrations/` | Database schema migrations | SQL |
| `frontend/src/app/` | Next.js App Router pages | TypeScript/React |
| `frontend/src/components/` | React components | TypeScript/React |
| `apps/mobile/` | React Native mobile app | TypeScript/React Native |
| `sdk/` | Python SDK for agent management | Python |

---

## Technology Stack

### Backend (Python/FastAPI)

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Framework** | FastAPI | 0.115.12 | REST API framework |
| **Runtime** | Python | 3.11+ | Core language |
| **Package Manager** | UV | Latest | Fast Python package manager |
| **ASGI Server** | Uvicorn + Gunicorn | Latest | Production server (7 workers, 2 threads) |
| **Database** | Supabase (PostgreSQL) | Latest | Primary database with RLS |
| **Caching** | Redis | 7-alpine | Cache + message broker |
| **Background Jobs** | Dramatiq | 1.18.0 | Async agent execution |
| **LLM Integration** | LiteLLM | Latest | Multi-provider LLM support |
| **Code Execution** | Daytona SDK + E2B | Latest | Sandboxed code execution |
| **Observability** | Langfuse | 2.60.5 | LLM tracing and monitoring |
| **Error Tracking** | Sentry | Latest | Error monitoring |
| **Billing** | Stripe | 11.6.0 | Subscription management |
| **Testing** | pytest + pytest-asyncio | Latest | Unit and integration testing |

**Key Dependencies**:
- **Search/Web**: Tavily, Firecrawl, Exa, Serper
- **Tools**: Composio (200+ integrations), MCP (Model Context Protocol)
- **Documents**: PyPDF2, python-docx, openpyxl, python-pptx
- **Web Scraping**: BeautifulSoup4, httpx

### Frontend (Next.js/React)

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Framework** | Next.js | 15.3.1 | React framework with App Router |
| **Runtime** | React | 18 | UI library |
| **Language** | TypeScript | 5 | Type-safe JavaScript |
| **Build Tool** | Turbopack | Latest | Fast bundler (Next.js integrated) |
| **Styling** | Tailwind CSS | 4 | Utility-first CSS |
| **UI Components** | Radix UI + shadcn/ui | Latest | Accessible component primitives |
| **Icons** | Lucide React | Latest | Icon library |
| **Animations** | Framer Motion | Latest | Animation library |
| **State (Global)** | Zustand | 5.0.3 | Lightweight state management |
| **State (Server)** | TanStack Query | 5.75.2 | Server state caching |
| **Rich Text** | TipTap | 3.3.0 | Collaborative text editor |
| **Code Editor** | CodeMirror | Latest | Code editing with syntax highlighting |
| **Charts** | Recharts | 3.2.1 | Data visualization |
| **Auth** | Supabase SSR | Latest | Authentication with SSR support |
| **i18n** | next-intl | 4.5.3 | Internationalization |
| **Analytics** | PostHog, Vercel Analytics | Latest | Product analytics |

**Key Features**:
- Server Components by default for better performance
- Streaming SSR with React Suspense
- API routes for backend integration
- Real-time updates via Supabase subscriptions

### Mobile (React Native/Expo)

| Category | Technology | Version | Purpose |
|----------|-----------|---------|---------|
| **Framework** | Expo | ~54.0.20 | React Native framework |
| **React Native** | React Native | 0.81.5 | Mobile framework |
| **React** | React | 19.1.0 | UI library |
| **Navigation** | Expo Router | 6.0.13 | File-based navigation |
| **UI Library** | RN Primitives | Latest | Radix-style components for mobile |
| **Styling** | NativeWind | 4.2.1 | Tailwind CSS for React Native |
| **State** | Zustand + TanStack Query | Latest | State management |
| **Auth** | Supabase JS + Expo Auth Session | Latest | Authentication |
| **Purchases** | react-native-purchases | 9.6.5 | In-app purchases (RevenueCat) |

### Infrastructure

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Containers** | Docker + Docker Compose | Service orchestration |
| **CI/CD** | GitHub Actions | Build and deployment |
| **Hosting (Backend)** | AWS ECS | Container orchestration |
| **Hosting (Frontend)** | Vercel (implied) | Frontend hosting |
| **Database** | Supabase Cloud or Self-hosted | PostgreSQL with real-time |
| **Sandbox** | Daytona Cloud | Isolated code execution environments |

---

## Development Setup

### Prerequisites

- **Git**: Version control
- **Docker**: For containerized services (Redis, optional Supabase)
- **UV**: Python package manager (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- **Node.js**: 18+ (for frontend and mobile)
- **npm**: Package manager
- **Python**: 3.11+ (for backend)

### Quick Start (Recommended)

```bash
# Clone repository
git clone https://github.com/kortix-ai/suna.git
cd suna

# Run interactive setup wizard
python setup.py

# Start all services
python start.py
```

The setup wizard will guide you through 17 steps including:
1. Choosing deployment method (Docker vs Manual)
2. Installing dependencies
3. Configuring Supabase (local or cloud)
4. Setting up Daytona API
5. Configuring LLM providers (Anthropic, OpenAI, etc.)
6. Configuring search APIs (Tavily, Firecrawl, etc.)
7. Generating encryption keys
8. Running database migrations
9. Starting services

### Manual Setup (Full Control)

**1. Infrastructure (Redis)**
```bash
docker compose up redis -d
```

**2. Database (Supabase)**

Option A: Cloud Supabase (recommended for Docker setup)
```bash
# Use Supabase dashboard to create project
# Update backend/.env with credentials
```

Option B: Local Supabase (recommended for manual setup)
```bash
cd backend
npx supabase start  # Starts local Supabase stack
npx supabase db reset  # Apply migrations
```

**Important**: After migrations, expose `basejump` schema in Supabase:
- Settings → API → Exposed schemas → Add `basejump`

**3. Backend**
```bash
cd backend

# Install dependencies
uv sync

# Run migrations (if using cloud Supabase)
npx supabase link --project-ref <your-project-ref>
npx supabase db push

# Start API server (Terminal 1)
uv run api.py

# Start background worker (Terminal 2)
uv run dramatiq run_agent_background --processes 4 --threads 4
```

**4. Frontend**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev  # Runs on http://localhost:3000
```

**5. Mobile (Optional)**
```bash
cd apps/mobile

# Install dependencies
npm install

# Start Expo dev server
npm run dev

# Platform-specific
npm run ios      # iOS simulator
npm run android  # Android emulator
npm run web      # Web browser
```

### Environment Configuration

**Backend** (`backend/.env`)
```bash
# Environment
ENV_MODE=local  # local | staging | production

# Supabase
SUPABASE_URL=http://127.0.0.1:54321  # or cloud URL
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
SUPABASE_JWT_SECRET=your_jwt_secret

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# LLM Providers (at least one required)
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk_...

# Search/Web APIs
TAVILY_API_KEY=tvly-...
FIRECRAWL_API_KEY=fc-...

# Sandbox
DAYTONA_API_KEY=your_daytona_key
E2B_API_KEY=your_e2b_key

# Billing
STRIPE_SECRET_KEY=sk_test_...

# Observability
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
SENTRY_DSN=https://...

# Admin
KORTIX_ADMIN_API_KEY=generated_key  # Generate with: openssl rand -hex 32
MCP_ENCRYPTION_KEY=generated_key    # Generate with setup.py
```

**Frontend** (`frontend/.env.local`)
```bash
# Environment
NEXT_PUBLIC_ENV_MODE=local

# Supabase (public)
NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:54321
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key

# Backend API
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000/api

# Frontend URL
NEXT_PUBLIC_URL=http://localhost:3000

# Admin API (for server-side operations)
KORTIX_ADMIN_API_KEY=same_as_backend_admin_key
```

---

## Architecture Patterns

### 1. AgentPress Framework (Core Agent System)

**Location**: `backend/core/agentpress/`

AgentPress is a custom agent execution framework built on tool-calling patterns.

**Key Components**:

- **ThreadManager** (`thread_manager.py`): Manages conversation threads
  - Creates and manages threads
  - Adds messages to threads
  - Orchestrates LLM calls with tool execution
  - Handles streaming responses

- **ToolRegistry** (`tool_registry.py`): Central tool registration
  - Registers tools with metadata
  - Provides tool schemas to LLM
  - Routes tool calls to implementations

- **Tool** (`tool.py`): Base class for all tools
  - Decorator-based schema definition
  - OpenAPI schema generation
  - Metadata for UI display

- **ResponseProcessor** (`response_processor.py`): Processes LLM responses
  - Handles tool calls
  - Manages streaming
  - Processes artifacts (code blocks, documents)

**Tool Definition Pattern**:

```python
from core.agentpress.tool import Tool, tool_metadata, method_metadata, openapi_schema

@tool_metadata(
    display_name="File Operations",
    weight=20,  # Ordering in UI
    visible=True  # Show in agent builder
)
class FilesTool(Tool):
    def __init__(self, sandbox_id: str):
        super().__init__()
        self.sandbox_id = sandbox_id

    @method_metadata(
        display_name="Read File",
        visible=True,
        description="Read contents of a file"
    )
    @openapi_schema({
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "File path to read"
            }
        },
        "required": ["path"]
    })
    async def read_file(self, path: str) -> str:
        """Read file from sandbox."""
        # Implementation
        return content
```

### 2. Background Job Processing (Dramatiq)

**Location**: `backend/run_agent_background.py`

Agents run in background workers to handle long-running tasks.

**Architecture**:
```
User Request → FastAPI → Create AgentRun → Enqueue Dramatiq Task
                                                    ↓
                                            Background Worker
                                                    ↓
                                            Thread Manager
                                                    ↓
                                            LLM + Tool Execution
                                                    ↓
                                            Update AgentRun Status
                                                    ↓
                                            Realtime Update (Supabase)
```

**Key Features**:
- Distributed task queue via Redis
- Multiple workers (4 processes × 4 threads)
- Idempotent task execution
- Graceful shutdown handling
- Real-time control via Redis Pub/Sub (start/stop runs)

**Worker Management**:
```bash
# Start worker
uv run dramatiq run_agent_background --processes 4 --threads 4

# Worker will process tasks from queue:
# - run_agent_actor: Main agent execution
# - Health checks and monitoring
```

### 3. Sandbox Isolation (Daytona)

**Location**: `backend/core/sandbox/`

Each user gets an isolated cloud sandbox for code execution.

**Features**:
- Docker-based isolation
- Persistent storage
- Snapshot-based initialization
- Pre-installed tools (Python, Node.js, browsers)
- Session-based command execution

**Sandbox Lifecycle**:
```python
# Create sandbox
sandbox = await Sandbox.create(
    user_id=user_id,
    snapshot="kortix/suna:0.1.3.25"
)

# Execute command
result = await sandbox.execute_command("python script.py")

# File operations
await sandbox.write_file("/path/to/file", content)
content = await sandbox.read_file("/path/to/file")

# Cleanup (automatic or manual)
await sandbox.destroy()
```

### 4. Frontend Architecture (Next.js App Router)

**Location**: `frontend/src/app/`

**Patterns**:

1. **Route Groups**: Organize routes without affecting URL structure
   - `(dashboard)` - Authenticated pages with shared layout
   - `(home)` - Marketing pages

2. **Server Components**: Default for better performance
   ```typescript
   // Server Component (default)
   async function ThreadPage({ params }) {
     const thread = await fetchThread(params.threadId);
     return <ThreadView thread={thread} />;
   }
   ```

3. **Client Components**: Interactive UI
   ```typescript
   'use client';

   import { useState } from 'react';

   export function ChatInput() {
     const [message, setMessage] = useState('');
     // Interactive logic
   }
   ```

4. **API Routes**: Backend integration
   ```typescript
   // app/api/threads/route.ts
   export async function GET(request: Request) {
     const threads = await fetchThreads();
     return Response.json(threads);
   }
   ```

### 5. State Management Strategy

**Global State** (Zustand): `frontend/src/stores/`
```typescript
// stores/auth-store.ts
import { create } from 'zustand';

interface AuthStore {
  user: User | null;
  setUser: (user: User | null) => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  setUser: (user) => set({ user }),
}));
```

**Server State** (TanStack Query): `frontend/src/hooks/`
```typescript
import { useQuery } from '@tanstack/react-query';

export function useThreads() {
  return useQuery({
    queryKey: ['threads'],
    queryFn: fetchThreads,
    staleTime: 5000,
  });
}
```

**URL State**: Next.js router params and searchParams

### 6. Real-time Updates

**Backend → Frontend**:
1. Server-Sent Events (SSE) for agent streaming
2. Supabase Realtime for database changes

**SSE Streaming**:
```python
# Backend
async def stream_agent_response():
    async for chunk in agent.run_stream():
        yield f"data: {json.dumps(chunk)}\n\n"

# Frontend
const eventSource = new EventSource('/api/agent-runs/123/stream');
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateUI(data);
};
```

**Supabase Realtime**:
```typescript
// Subscribe to thread updates
const channel = supabase
  .channel('thread-updates')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'messages',
      filter: `thread_id=eq.${threadId}`,
    },
    (payload) => {
      addMessage(payload.new);
    }
  )
  .subscribe();
```

---

## Coding Conventions

### Python (Backend)

**File Naming**:
- Snake case: `thread_manager.py`, `tool_registry.py`
- Test files: `test_*.py`

**Code Style**:
- **Classes**: `PascalCase` (e.g., `ThreadManager`, `SandboxFilesTool`)
- **Functions/Variables**: `snake_case` (e.g., `create_thread`, `user_id`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
- **Private**: Leading underscore (e.g., `_internal_method`, `_cache`)

**Type Hints**: Required for all function signatures
```python
async def create_thread(
    self,
    account_id: Optional[str] = None,
    project_id: Optional[str] = None,
    is_public: bool = False,
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """Create a new thread in the database."""
    # Implementation
```

**Async Patterns**:
- Use `async/await` for all I/O operations
- Avoid blocking calls
- Use `asyncio.gather()` for concurrent operations

```python
# Good
async def fetch_multiple_threads(thread_ids: List[str]) -> List[Thread]:
    tasks = [fetch_thread(tid) for tid in thread_ids]
    return await asyncio.gather(*tasks)

# Bad (sequential)
async def fetch_multiple_threads(thread_ids: List[str]) -> List[Thread]:
    threads = []
    for tid in thread_ids:
        threads.append(await fetch_thread(tid))
    return threads
```

**Error Handling**:
```python
try:
    result = await operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}", exc_info=True)
    raise HTTPException(status_code=400, detail=str(e))
```

**Logging**:
```python
from core.utils.logger import logger

# Structured logging
logger.info("Creating thread", extra={
    "account_id": account_id,
    "project_id": project_id
})

logger.error("Thread creation failed", exc_info=True, extra={
    "account_id": account_id,
    "error": str(e)
})
```

**Docstrings**: Module-level and class-level
```python
"""
Module-level docstring explaining purpose.
"""

class ThreadManager:
    """Manages conversation threads with LLM models and tool execution."""

    async def create_thread(self, account_id: str) -> str:
        """
        Create a new thread in the database.

        Args:
            account_id: User's account identifier

        Returns:
            Created thread ID

        Raises:
            HTTPException: If thread creation fails
        """
```

### TypeScript/React (Frontend)

**File Naming**:
- Components: `PascalCase.tsx` or `kebab-case.tsx`
- Utilities: `kebab-case.ts`
- Pages (App Router): `page.tsx`, `layout.tsx`

**Code Style**:
- **Components**: `PascalCase` (e.g., `ThreadView`, `ChatInput`)
- **Functions/Variables**: `camelCase` (e.g., `fetchThreads`, `userId`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_MESSAGE_LENGTH`)
- **Types/Interfaces**: `PascalCase` (e.g., `Thread`, `MessageContent`)

**Component Patterns**:

Server Component (default):
```typescript
// No 'use client' directive
import { fetchThread } from '@/lib/api/threads';

interface ThreadPageProps {
  params: Promise<{ threadId: string }>;
}

export default async function ThreadPage({ params }: ThreadPageProps) {
  const { threadId } = await params;
  const thread = await fetchThread(threadId);

  return <ThreadView thread={thread} />;
}
```

Client Component:
```typescript
'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';

interface ChatInputProps {
  onSubmit: (message: string) => void;
}

export function ChatInput({ onSubmit }: ChatInputProps) {
  const [message, setMessage] = useState('');

  return (
    <div>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <Button onClick={() => onSubmit(message)}>Send</Button>
    </div>
  );
}
```

**Type Definitions**:
```typescript
// Explicit interface for component props
interface ThreadViewProps {
  thread: Thread;
  onUpdate?: (thread: Thread) => void;
}

// Type for API responses
type ApiResponse<T> = {
  data: T | null;
  error: string | null;
  status: 'success' | 'error';
};
```

**Hooks Usage**:
```typescript
// Custom hook
export function useThread(threadId: string) {
  return useQuery({
    queryKey: ['thread', threadId],
    queryFn: () => fetchThread(threadId),
  });
}

// Usage in component
function ThreadComponent({ threadId }: { threadId: string }) {
  const { data: thread, isLoading } = useThread(threadId);

  if (isLoading) return <Skeleton />;
  return <ThreadView thread={thread} />;
}
```

**Error Boundaries**: Wrap components that might throw
```typescript
<ErrorBoundary fallback={<ErrorView />}>
  <ThreadView threadId={threadId} />
</ErrorBoundary>
```

### CSS/Styling (Tailwind)

**Utility-First Approach**:
```typescript
<div className="flex items-center gap-4 p-6 bg-background rounded-lg border">
  <Avatar />
  <div className="flex-1">
    <h3 className="text-lg font-semibold">Title</h3>
    <p className="text-sm text-muted-foreground">Description</p>
  </div>
</div>
```

**Custom Components** (shadcn/ui pattern):
```typescript
import { cn } from '@/lib/utils';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'outline' | 'ghost';
}

export function Button({ className, variant = 'default', ...props }: ButtonProps) {
  return (
    <button
      className={cn(
        'px-4 py-2 rounded-md font-medium transition-colors',
        variant === 'default' && 'bg-primary text-primary-foreground hover:bg-primary/90',
        variant === 'outline' && 'border border-input hover:bg-accent',
        className
      )}
      {...props}
    />
  );
}
```

### Database (SQL)

**Naming Conventions**:
- Tables: `snake_case` (e.g., `threads`, `agent_runs`, `secure_mcp_credentials`)
- Columns: `snake_case` (e.g., `thread_id`, `created_at`, `is_public`)
- Primary Keys: `{table}_id` (e.g., `thread_id`, `message_id`)
- Foreign Keys: `{referenced_table}_id` (e.g., `account_id` in `threads`)
- Junction Tables: `{table1}_{table2}` (e.g., `agent_tools`)

**Migration Files**:
- Timestamp prefix: `YYYYMMDDHHMMSS_description.sql`
- Descriptive names: `20250417000000_workflow_system.sql`

### Git Workflow

**Branches**:
- `main` - Staging environment
- `PRODUCTION` - Production environment
- Feature branches: `feature/description` or `claude/description`

**Commit Messages** (Conventional Commits style):
```bash
feat(agents): add multi-agent conversation support
fix(sandbox): prevent memory leak in long-running sessions
docs(readme): update installation instructions
refactor(tools): simplify tool registration API
```

**Pull Requests**:
- Must pass CI checks
- Descriptive title and description
- Link related issues

---

## Key Workflows

### 1. Agent Execution Flow

```
User sends message
    ↓
Frontend → POST /api/threads/{id}/messages
    ↓
Backend creates message in DB
    ↓
Backend → POST /api/agent-runs (creates AgentRun)
    ↓
Dramatiq task enqueued
    ↓
Background worker picks up task
    ↓
ThreadManager.run() orchestrates execution
    ↓
Loop:
  1. Get thread history from DB
  2. Call LLM with thread + tool schemas
  3. Process LLM response:
     - Text content → Save to DB
     - Tool calls → Execute via ToolRegistry
  4. Add tool results to thread
  5. Continue if more tool calls needed
    ↓
Final response saved to DB
    ↓
AgentRun marked complete
    ↓
Frontend receives updates via:
  - SSE stream (real-time)
  - Supabase Realtime (DB changes)
```

### 2. Tool Execution Flow

```
LLM returns tool call
    ↓
ResponseProcessor identifies tool call
    ↓
ToolRegistry looks up tool by name
    ↓
Tool instance executes method
    ↓
Tool returns result (success or error)
    ↓
Result added to thread as tool_result message
    ↓
Thread continues with updated context
```

### 3. Authentication Flow

**Frontend (Next.js + Supabase)**:
```
User clicks "Sign In"
    ↓
Redirect to /auth/signin
    ↓
Supabase Auth (email/password or OAuth)
    ↓
Supabase returns JWT token
    ↓
Token stored in cookie (httpOnly)
    ↓
Middleware validates token on each request
    ↓
User object available in components
```

**Backend (FastAPI + Supabase)**:
```
Request with Authorization header
    ↓
Middleware extracts JWT token
    ↓
Verify token with Supabase JWT secret
    ↓
Extract user_id from token
    ↓
Attach user context to request
    ↓
Handler has access to current_user
```

### 4. Sandbox Management

**Lifecycle**:
```
User starts conversation
    ↓
Check if sandbox exists for account
    ↓
If not:
  - Create sandbox via Daytona API
  - Initialize with snapshot (kortix/suna:0.1.3.25)
  - Store sandbox_id in DB
    ↓
Tools use sandbox for operations:
  - File operations
  - Shell commands
  - Code execution
    ↓
Sandbox persists across conversations
    ↓
Auto-cleanup after inactivity (configurable)
```

### 5. Billing/Subscription Flow

**Powered by Basejump SaaS Framework**:
```
User creates account
    ↓
Basejump creates account record
    ↓
User views pricing page
    ↓
Selects plan → Redirect to Stripe Checkout
    ↓
Stripe processes payment
    ↓
Webhook → Backend receives subscription event
    ↓
Basejump updates billing status
    ↓
User gets access to paid features
    ↓
Row-Level Security enforces feature access
```

---

## Common Development Tasks

### Adding a New Tool

1. **Create Tool Class** (`backend/core/tools/new_tool.py`):
```python
from core.agentpress.tool import Tool, tool_metadata, method_metadata, openapi_schema
from typing import Dict, Any

@tool_metadata(
    display_name="New Tool",
    weight=30,
    visible=True,
    description="Description of what this tool does"
)
class NewTool(Tool):
    def __init__(self, **kwargs):
        super().__init__()
        # Initialization

    @method_metadata(
        display_name="Do Something",
        visible=True,
        description="What this method does"
    )
    @openapi_schema({
        "type": "object",
        "properties": {
            "param": {
                "type": "string",
                "description": "Parameter description"
            }
        },
        "required": ["param"]
    })
    async def do_something(self, param: str) -> Dict[str, Any]:
        """Implementation."""
        result = await self._process(param)
        return {"success": True, "result": result}
```

2. **Register Tool** (in thread manager or agent config):
```python
thread_manager.add_tool(NewTool, function_names=['do_something'])
```

3. **Test Tool**:
```python
# backend/tests/unit/tools/test_new_tool.py
import pytest
from core.tools.new_tool import NewTool

@pytest.mark.asyncio
async def test_new_tool():
    tool = NewTool()
    result = await tool.do_something(param="test")
    assert result["success"] is True
```

### Adding a New API Endpoint

1. **Define Pydantic Models** (`backend/core/api_models/`):
```python
from pydantic import BaseModel

class CreateItemRequest(BaseModel):
    name: str
    description: str | None = None

class ItemResponse(BaseModel):
    item_id: str
    name: str
    created_at: str
```

2. **Create Router** (`backend/core/api/items.py`):
```python
from fastapi import APIRouter, Depends, HTTPException
from core.api_models.items import CreateItemRequest, ItemResponse
from core.services.supabase import DBConnection

router = APIRouter(prefix="/items", tags=["items"])

@router.post("", response_model=ItemResponse)
async def create_item(
    request: CreateItemRequest,
    db: DBConnection = Depends()
):
    client = await db.client
    result = await client.table('items').insert({
        'name': request.name,
        'description': request.description
    }).execute()

    if not result.data:
        raise HTTPException(status_code=500, detail="Failed to create item")

    return result.data[0]
```

3. **Register Router** (`backend/api.py`):
```python
from core.api.items import router as items_router

app.include_router(items_router, prefix="/api")
```

4. **Create Frontend API Client** (`frontend/src/lib/api/items.ts`):
```typescript
import { apiClient } from './client';

export interface CreateItemRequest {
  name: string;
  description?: string;
}

export interface Item {
  item_id: string;
  name: string;
  created_at: string;
}

export async function createItem(data: CreateItemRequest): Promise<Item> {
  const response = await apiClient.post<Item>('/items', data);
  return response.data;
}
```

### Adding a New Page (Frontend)

1. **Create Page** (`frontend/src/app/(dashboard)/items/page.tsx`):
```typescript
import { Suspense } from 'react';
import { ItemList } from '@/components/items/item-list';
import { Skeleton } from '@/components/ui/skeleton';

export default function ItemsPage() {
  return (
    <div className="container py-8">
      <h1 className="text-3xl font-bold mb-6">Items</h1>
      <Suspense fallback={<Skeleton className="h-96" />}>
        <ItemList />
      </Suspense>
    </div>
  );
}
```

2. **Create Component** (`frontend/src/components/items/item-list.tsx`):
```typescript
'use client';

import { useQuery } from '@tanstack/react-query';
import { fetchItems } from '@/lib/api/items';

export function ItemList() {
  const { data: items, isLoading } = useQuery({
    queryKey: ['items'],
    queryFn: fetchItems,
  });

  if (isLoading) return <div>Loading...</div>;

  return (
    <div className="space-y-4">
      {items?.map(item => (
        <div key={item.item_id} className="p-4 border rounded-lg">
          <h3 className="font-semibold">{item.name}</h3>
        </div>
      ))}
    </div>
  );
}
```

### Running Database Migrations

**Local Supabase**:
```bash
cd backend

# Create new migration
npx supabase migration new add_new_table

# Edit migration file in supabase/migrations/

# Apply migrations
npx supabase db reset
```

**Cloud Supabase**:
```bash
cd backend

# Link to project
npx supabase link --project-ref <your-project-ref>

# Create migration
npx supabase migration new add_new_table

# Edit migration file

# Push to cloud
npx supabase db push
```

**Important**: After schema changes, expose new schemas/functions in Supabase dashboard if needed (Settings → API → Exposed schemas).

### Debugging Agent Issues

1. **Check Langfuse**: https://cloud.langfuse.com
   - View agent traces
   - See LLM calls, tool executions, errors
   - Check token usage and latency

2. **Check Backend Logs**:
```bash
# API server logs
tail -f backend/logs/api.log

# Worker logs
tail -f backend/logs/worker.log
```

3. **Check Database**:
```bash
# Connect to local Supabase
npx supabase db connect

# Query agent runs
SELECT * FROM agent_runs WHERE thread_id = 'xxx' ORDER BY created_at DESC;

# Query messages
SELECT * FROM messages WHERE thread_id = 'xxx' ORDER BY created_at;
```

4. **Check Redis**:
```bash
# Connect to Redis
docker exec -it suna-redis-1 redis-cli

# Check queues
LLEN dramatiq:default
KEYS dramatiq:*

# Check pub/sub channels
PUBSUB CHANNELS
```

---

## Testing Guidelines

### Backend Testing

**Framework**: pytest with asyncio support

**Running Tests**:
```bash
cd backend

# All tests
uv run pytest

# Unit tests only (fast)
uv run pytest -m unit

# Integration tests
uv run pytest -m integration

# Specific test file
uv run pytest tests/unit/tools/test_browser_tool.py

# With coverage
uv run pytest --cov=core --cov-report=html
```

**Test Structure**:
```
backend/tests/
├── unit/              # Fast, isolated tests
│   ├── tools/
│   ├── agentpress/
│   └── services/
├── integration/       # DB/API/LLM tests
│   ├── test_agent_workflow.py
│   └── test_api_endpoints.py
└── conftest.py        # Shared fixtures
```

**Test Markers** (defined in `pytest.ini`):
- `@pytest.mark.unit` - Fast unit tests
- `@pytest.mark.integration` - Integration tests (DB, API, external services)
- `@pytest.mark.slow` - Slow tests (skip in quick runs)
- `@pytest.mark.api` - API endpoint tests
- `@pytest.mark.llm` - Tests that call LLM APIs
- `@pytest.mark.asyncio` - Async tests

**Writing Tests**:
```python
import pytest
from core.agentpress.thread_manager import ThreadManager

@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_thread():
    """Test thread creation."""
    thread_manager = ThreadManager()
    thread_id = await thread_manager.create_thread(
        account_id="test_account"
    )
    assert thread_id is not None
    assert isinstance(thread_id, str)

@pytest.mark.integration
@pytest.mark.asyncio
async def test_agent_run_with_tools():
    """Test full agent execution with tool calls."""
    # Setup
    thread_manager = ThreadManager()
    thread_manager.add_tool(TestTool)

    # Execute
    response = await thread_manager.run(
        thread_id="test_thread",
        user_message="Use the test tool"
    )

    # Assert
    assert response.status == "completed"
    assert "tool_result" in str(response.messages)
```

**Fixtures** (`conftest.py`):
```python
import pytest
from core.services.supabase import DBConnection

@pytest.fixture
async def db_connection():
    """Provide database connection for tests."""
    db = DBConnection()
    yield db
    await db.close()

@pytest.fixture
async def test_thread(db_connection):
    """Create test thread."""
    client = await db_connection.client
    result = await client.table('threads').insert({
        'account_id': 'test_account'
    }).execute()
    thread_id = result.data[0]['thread_id']

    yield thread_id

    # Cleanup
    await client.table('threads').delete().eq('thread_id', thread_id).execute()
```

**Coverage Requirements**:
- Minimum: 60% (enforced in CI)
- Target: 80%+ for core modules

### Frontend Testing

**Current State**: No formal test framework configured yet.

**Recommended Setup** (to be implemented):
```bash
cd frontend

# Install testing dependencies
npm install --save-dev @testing-library/react @testing-library/jest-dom jest

# Run tests
npm test
```

**Example Test** (pattern to follow):
```typescript
import { render, screen } from '@testing-library/react';
import { ChatInput } from '@/components/thread/chat-input';

describe('ChatInput', () => {
  it('renders input field', () => {
    render(<ChatInput onSubmit={jest.fn()} />);
    expect(screen.getByRole('textbox')).toBeInTheDocument();
  });

  it('calls onSubmit with message', async () => {
    const onSubmit = jest.fn();
    render(<ChatInput onSubmit={onSubmit} />);

    const input = screen.getByRole('textbox');
    await userEvent.type(input, 'Hello');
    await userEvent.click(screen.getByRole('button', { name: /send/i }));

    expect(onSubmit).toHaveBeenCalledWith('Hello');
  });
});
```

---

## Database Schema

### Key Tables

**threads**
- `thread_id` (PK, UUID)
- `account_id` (FK to basejump.accounts)
- `project_id` (FK to projects)
- `is_public` (boolean)
- `metadata` (JSONB)
- `created_at`, `updated_at`

**messages**
- `message_id` (PK, UUID)
- `thread_id` (FK to threads)
- `type` (text: 'user', 'assistant', 'tool_call', 'tool_result')
- `content` (JSONB)
- `is_llm_message` (boolean)
- `metadata` (JSONB)
- `agent_id`, `agent_version_id` (FKs)
- `created_at`

**agent_runs**
- `run_id` (PK, UUID)
- `thread_id` (FK to threads)
- `agent_id` (FK to agents)
- `status` (text: 'pending', 'running', 'completed', 'failed', 'stopped')
- `error` (text)
- `metadata` (JSONB)
- `created_at`, `updated_at`, `completed_at`

**agents**
- `agent_id` (PK, UUID)
- `account_id` (FK to basejump.accounts)
- `name`, `description`
- `model` (text: LLM model identifier)
- `system_prompt` (text)
- `is_public` (boolean)
- `created_at`, `updated_at`

**agent_tools**
- Junction table for agents and tools
- `agent_id` (FK to agents)
- `tool_name` (text)
- `config` (JSONB)

**secure_mcp_credentials**
- `credential_id` (PK, UUID)
- `account_id` (FK to basejump.accounts)
- `server_name` (text)
- `encrypted_env` (text)
- `encryption_key_hash` (text)
- `created_at`, `updated_at`

**Basejump Tables** (Multi-tenancy framework):
- `basejump.accounts` - Account/team management
- `basejump.account_users` - User-account relationships
- `basejump.billing_subscriptions` - Stripe subscriptions
- `basejump.billing_customers` - Stripe customer mapping

### Row-Level Security (RLS)

All tables have RLS policies enforcing:
- Users can only access their own account's data
- Public threads are readable by anyone
- Service role bypasses RLS for system operations

**Example Policy**:
```sql
-- Users can view threads they own or public threads
CREATE POLICY "Users can view own threads"
ON threads FOR SELECT
USING (
  auth.uid() IN (
    SELECT user_id FROM basejump.account_users
    WHERE account_id = threads.account_id
  )
  OR is_public = true
);
```

---

## API Patterns

### RESTful Endpoints

**Standard CRUD**:
```
GET    /api/threads           - List threads
POST   /api/threads           - Create thread
GET    /api/threads/:id       - Get thread
PATCH  /api/threads/:id       - Update thread
DELETE /api/threads/:id       - Delete thread

POST   /api/threads/:id/messages  - Add message to thread
```

**Nested Resources**:
```
GET    /api/agents/:id/versions   - List agent versions
POST   /api/agents/:id/publish    - Publish agent version
```

**Actions**:
```
POST   /api/agent-runs/:id/stop    - Stop running agent
POST   /api/sandbox/:id/execute    - Execute command in sandbox
```

### Request/Response Format

**Success Response**:
```json
{
  "data": {
    "thread_id": "123",
    "messages": [...]
  },
  "error": null,
  "status": "success"
}
```

**Error Response**:
```json
{
  "data": null,
  "error": {
    "message": "Thread not found",
    "code": "THREAD_NOT_FOUND",
    "details": {}
  },
  "status": "error"
}
```

### Authentication

**Header**:
```
Authorization: Bearer <supabase_jwt_token>
```

**Admin API**:
```
x-admin-api-key: <KORTIX_ADMIN_API_KEY>
```

### Streaming Endpoints

**Server-Sent Events (SSE)**:
```
POST /api/agent-runs/:id/stream
Content-Type: text/event-stream

data: {"type":"message","content":"Hello"}

data: {"type":"tool_call","name":"browser","args":{...}}

data: {"type":"done"}
```

**Client (Frontend)**:
```typescript
const eventSource = new EventSource('/api/agent-runs/123/stream');

eventSource.addEventListener('message', (event) => {
  const data = JSON.parse(event.data);
  handleUpdate(data);
});

eventSource.addEventListener('error', () => {
  eventSource.close();
});
```

---

## Troubleshooting

### Common Issues

**1. "Module not found" errors (Backend)**
```bash
# Sync dependencies
cd backend
uv sync

# Check Python version
python --version  # Should be 3.11+
```

**2. "Connection refused" to database**
```bash
# Check Supabase is running (local)
cd backend
npx supabase status

# Restart if needed
npx supabase stop
npx supabase start
```

**3. Frontend build errors**
```bash
# Clear Next.js cache
cd frontend
rm -rf .next
npm run build
```

**4. Docker Compose issues**
```bash
# Check service status
docker compose ps

# View logs
docker compose logs backend
docker compose logs worker

# Restart services
docker compose restart
```

**5. Agent runs stuck in "pending" or "running"**
```bash
# Check worker is running
ps aux | grep dramatiq

# Check Redis connection
docker exec -it suna-redis-1 redis-cli ping

# Check worker logs
tail -f backend/logs/worker.log

# Restart worker
pkill -f dramatiq
cd backend && uv run dramatiq run_agent_background
```

**6. "Sandbox not found" errors**
```bash
# Check Daytona API key
echo $DAYTONA_API_KEY

# Check sandbox in database
psql <supabase_connection_string>
SELECT * FROM sandboxes WHERE account_id = 'xxx';

# Force recreate sandbox (delete old record in DB)
```

**7. Missing API keys**
```bash
# Check environment variables
cd backend
cat .env | grep API_KEY

# Regenerate with setup.py
python setup.py
```

**8. Database schema out of sync**
```bash
# Local Supabase
cd backend
npx supabase db reset  # Warning: deletes all data

# Cloud Supabase
npx supabase db push  # Apply pending migrations
```

**9. "basejump schema not exposed" error**

After running migrations, expose the `basejump` schema in Supabase:
1. Go to Supabase Dashboard
2. Settings → API → Exposed schemas
3. Add `basejump` to the list
4. Restart backend

### Debug Mode

**Backend**:
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
uv run api.py
```

**Frontend**:
```bash
# Next.js debug mode
DEBUG=* npm run dev
```

### Health Checks

**Backend**:
```
GET /health          # Basic health check
GET /health-docker   # Docker health check (includes DB, Redis)
```

**Check all services**:
```bash
# Backend
curl http://localhost:8000/health

# Frontend
curl http://localhost:3000

# Redis
docker exec -it suna-redis-1 redis-cli ping

# Supabase (local)
curl http://localhost:54321/rest/v1/
```

---

## Important Files Reference

### Configuration Files

| File | Purpose | Location |
|------|---------|----------|
| `setup.py` | Interactive installation wizard | Root |
| `start.py` | Service management script | Root |
| `docker-compose.yaml` | Multi-container orchestration | Root |
| `backend/pyproject.toml` | Python dependencies (UV) | Backend |
| `backend/pytest.ini` | Test configuration | Backend |
| `backend/.env` | Backend environment variables | Backend (generated) |
| `backend/supabase/config.toml` | Supabase CLI config | Backend |
| `frontend/package.json` | npm dependencies | Frontend |
| `frontend/next.config.ts` | Next.js configuration | Frontend |
| `frontend/tsconfig.json` | TypeScript configuration | Frontend |
| `frontend/.env.local` | Frontend environment variables | Frontend (generated) |
| `apps/mobile/app.json` | Expo configuration | Mobile |

### Entry Points

| File | Purpose | How to Run |
|------|---------|------------|
| `backend/api.py` | FastAPI application | `uv run api.py` |
| `backend/run_agent_background.py` | Dramatiq worker | `uv run dramatiq run_agent_background` |
| `frontend/src/app/layout.tsx` | Root layout | Auto (Next.js) |
| `apps/mobile/app/_layout.tsx` | Mobile root layout | Auto (Expo) |

### Core Logic

| File | Purpose |
|------|---------|
| `backend/core/agentpress/thread_manager.py` | Conversation orchestration |
| `backend/core/agentpress/tool_registry.py` | Tool management |
| `backend/core/agentpress/tool.py` | Base tool class |
| `backend/core/agentpress/response_processor.py` | LLM response handling |
| `backend/core/services/llm.py` | LLM API calls (LiteLLM) |
| `backend/core/services/supabase.py` | Database connection |
| `backend/core/services/redis.py` | Redis connection |
| `backend/core/sandbox/sandbox.py` | Daytona sandbox wrapper |
| `frontend/src/lib/api/client.ts` | API client setup |
| `frontend/src/components/thread/` | Chat interface components |

### Database

| File | Purpose |
|------|---------|
| `backend/supabase/migrations/` | SQL migrations (timestamped) |
| `backend/supabase/migrations/20240414161707_basejump-setup.sql` | Basejump SaaS foundation |
| `backend/supabase/migrations/20250416133920_agentpress_schema.sql` | Core agent tables |

### Tools

| File | Purpose |
|------|---------|
| `backend/core/tools/browser_tool.py` | Browser automation (Playwright) |
| `backend/core/tools/sb_files_tool.py` | Sandbox file operations |
| `backend/core/tools/sb_shell_tool.py` | Sandbox shell commands |
| `backend/core/tools/mcp_tool_wrapper.py` | MCP server integration |

---

## Quick Reference Commands

### Development

```bash
# Backend
cd backend
uv sync                           # Install dependencies
uv run api.py                     # Start API server
uv run dramatiq run_agent_background  # Start worker
uv run pytest                     # Run tests

# Frontend
cd frontend
npm install                       # Install dependencies
npm run dev                       # Start dev server
npm run build                     # Production build
npm run lint                      # Lint code

# Mobile
cd apps/mobile
npm install                       # Install dependencies
npm run dev                       # Start Expo
npm run ios                       # iOS simulator
npm run android                   # Android emulator

# Database
cd backend
npx supabase start                # Start local Supabase
npx supabase stop                 # Stop local Supabase
npx supabase db reset             # Reset and migrate
npx supabase migration new <name> # Create migration
```

### Docker

```bash
# Start services
docker compose up -d

# View logs
docker compose logs -f backend
docker compose logs -f worker

# Restart services
docker compose restart backend

# Stop services
docker compose down

# Rebuild images
docker compose build --no-cache
```

### Git

```bash
# Create feature branch
git checkout -b feature/my-feature

# Commit changes
git add .
git commit -m "feat(component): add new feature"

# Push to remote
git push -u origin feature/my-feature

# Switch to main and update
git checkout main
git pull origin main
```

---

## Additional Resources

### Documentation

- **Kortix Docs**: (Check `docs/` directory)
- **Supabase Docs**: https://supabase.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Next.js Docs**: https://nextjs.org/docs
- **Expo Docs**: https://docs.expo.dev

### Community

- **Discord**: https://discord.gg/RvFhXUdZ9H
- **Twitter**: https://x.com/kortixai
- **GitHub Issues**: https://github.com/kortix-ai/suna/issues

### Code References

When referencing code locations for the user, use the pattern:
```
backend/core/agentpress/thread_manager.py:28
frontend/src/app/(dashboard)/agents/[threadId]/page.tsx:14
```

---

**Note**: This document is maintained for AI assistants working with the Kortix codebase. Keep it updated as the architecture evolves.
