from typing import Optional

from common.event_queue import IAgentEventPublisher
from common.types import AgentID, PercentLimited


class CPUUtilizer:
    def __init__(
        self,
        cpu_utilization: PercentLimited,
        agent_id: AgentID,
        agent_event_publisher: IAgentEventPublisher,
    ):
        self._cpu_utilization = cpu_utilization
        self._agent_id = agent_id
        self._agent_event_publisher = agent_event_publisher

    def start(self):
        pass

    def stop(self, timeout: Optional[float] = None):
        pass