CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_agents_account_relu_default 
    ON agents(account_id) 
    WHERE metadata->>'is_relu_default' = 'true';