# Suna Infrastructure

Unified Pulumi Infrastructure-as-Code 

## Architecture

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                    CLOUDFLARE                            │
                    │                                                          │
                    │   api.relu.work ──► Worker (api-relu-router)          │
                    │                          │                               │
                    │         ┌────────────────┴────────────────┐              │
                    │         ▼                                 ▼              │
                    │   ACTIVE_BACKEND=lightsail          (future: ecs)        │
                    │         │                                 │              │
                    │         ▼                                 ▼              │
                    │   api-lightsail.relu.work         api-ecs.relu.work    │
                    │   (Tunnel f4125d84)                (Direct to ALB)       │
                    └─────────┬─────────────────────────────────┬──────────────┘
                              │                                 │
                              ▼                                 ▼
┌─────────────────────────────────────────┐    ┌───────────────────────────────────┐
│         LIGHTSAIL (Prod)                │    │           ECS (Prod)              │
│   suna-prod: 54.148.221.72              │    │   Cluster: suna-ecs               │
│   128GB RAM, 32 vCPU                    │    │   4 tasks on 3 instances          │
│   Cloudflared → localhost:8000          │    │   ALB → Target Group → Tasks      │
└─────────────────────────────────────────┘    └───────────────────────────────────┘

┌─────────────────────────────────────────┐    ┌───────────────────────────────────┐
│         LIGHTSAIL (Dev)                 │    │         LIGHTSAIL (Staging)       │
│   suna-dev: 35.87.190.182               │    │   suna-staging: 54.184.54.33      │
│   8GB RAM, 2 vCPU                       │    │   8GB RAM, 2 vCPU                 │
│   Tunnel → dev-api.relu.work           │    │   Tunnel → staging-api.relu.work │
└─────────────────────────────────────────┘    └───────────────────────────────────┘
```
