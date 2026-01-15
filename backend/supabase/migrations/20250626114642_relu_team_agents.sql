-- Migration: Add is_relu_team field to agent_templates
-- This migration adds support for marking templates as Relu team templates

BEGIN;

-- Add is_relu_team column to agent_templates table
ALTER TABLE agent_templates ADD COLUMN IF NOT EXISTS is_relu_team BOOLEAN DEFAULT false;

-- Create index for better performance
CREATE INDEX IF NOT EXISTS idx_agent_templates_is_relu_team ON agent_templates(is_relu_team);

-- Add comment
COMMENT ON COLUMN agent_templates.is_relu_team IS 'Indicates if this template is created by the Relu team (official templates)';

COMMIT; 