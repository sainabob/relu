from .api import agents, threads
from .agent import ReluAgent
from .thread import ReluThread
from .tools import AgentPressTools, MCPTools


class Relu:
    def __init__(self, api_key: str, api_url="https://api.relu.work/v1"):
        self._agents_client = agents.create_agents_client(api_url, api_key)
        self._threads_client = threads.create_threads_client(api_url, api_key)

        self.Agent = ReluAgent(self._agents_client)
        self.Thread = ReluThread(self._threads_client)
