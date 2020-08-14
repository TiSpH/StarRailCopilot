import numpy as np

from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from module.exception import ScriptEnd, CampaignEnd
from .campaign_1_1 import MAP
from .campaign_1_1 import Config as ConfigBase

A1, B1, C1, D1, E1, F1, G1, \
    = MAP.flatten()


class Config(ConfigBase):
    ENABLE_FAST_FORWARD = False
    AMBUSH_EVADE = False


class Campaign(CampaignBase):
    MAP = MAP
    affinity_battle = 0

    def battle_default(self):
        logger.attr('Affinity_battle', f'{self.affinity_battle}/{self.config.C11_AFFINITY_BATTLE_COUNT}')
        self.goto(C1)
        self.affinity_battle += 1

        # End
        if self.affinity_battle >= self.config.C11_AFFINITY_BATTLE_COUNT:
            try:
                self.withdraw()
            except CampaignEnd:
                raise ScriptEnd('Reach condition: Affinity farming battle count')

        # Continue
        if np.random.uniform() < 0.7:
            self.goto(D1)
        else:
            self.goto(B1)
        return True
