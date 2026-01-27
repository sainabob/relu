"""
Step 9: Relu Admin API Key
"""

from setup.steps.base import BaseStep, StepResult
from setup.utils.secrets import generate_admin_api_key


class ReluStep(BaseStep):
    """Auto-generate Relu admin API key."""

    name = "relu"
    display_name = "Relu Admin API Key"
    order = 9
    required = True
    depends_on = ["requirements"]

    def run(self) -> StepResult:
        # Always generate a new key (overwrite existing if any)
        self.info("Generating a secure admin API key for Relu administrative functions...")

        self.config.relu.RELU_ADMIN_API_KEY = generate_admin_api_key()

        self.success("Relu admin API key generated.")
        self.success("Relu admin configuration saved.")

        return StepResult.ok(
            "Relu admin key generated",
            {"relu": self.config.relu.model_dump()},
        )

    def get_config_keys(self):
        return ["RELU_ADMIN_API_KEY"]

    def is_complete(self) -> bool:
        return bool(self.config.relu.RELU_ADMIN_API_KEY)
