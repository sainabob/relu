# Environments

## Overview

| Environment | Git Branch | Frontend | Backend API |
|-------------|------------|----------|-------------|
| **DEV** | `main` | dev.relu.work | dev-api.relu.work |
| **STAGING** | `staging` | staging.relu.work | staging-api.relu.work |
| **PRODUCTION** | `PRODUCTION` | relu.work | api.relu.work |

## Databases (Supabase)

| Environment | Project |
|-------------|---------|
| DEV | heprlhlltebrxydgtsjs |
| STAGING | ujzsbwvurfyeuerxxeaz |
| PRODUCTION | jbriwassebxdwoieikga |

## Promotion Flow

```
main (DEV) → staging (STAGING) → PRODUCTION
```

Use GitHub Actions "Promote Branch" workflow to promote between environments.
