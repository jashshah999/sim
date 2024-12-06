"""Registers the tasks in the task registry.

For other people who might be looking at this in the future - my preferred way
of doing config management is to use dataclasses (see the `mlfab` or `xax`
packages for examples of what I mean). This plays a lot better with type
checkers and VSCode. I am just doing it this way to get something working
quickly.
"""

# mypy: ignore-errors
from sim.envs.humanoids.dora_config import DoraCfg, DoraCfgPPO
from sim.envs.humanoids.dora_env import DoraFreeEnv
from sim.envs.humanoids.g1_config import G1Cfg, G1CfgPPO
from sim.envs.humanoids.g1_env import G1FreeEnv
from sim.envs.humanoids.gpr_env import GprFreeEnv
from sim.envs.humanoids.grp_config import GprCfg, GprCfgPPO, GprStandingCfg
from sim.envs.humanoids.h1_config import H1Cfg, H1CfgPPO
from sim.envs.humanoids.h1_env import H1FreeEnv
from sim.envs.humanoids.xbot_config import XBotCfg, XBotCfgPPO
from sim.envs.humanoids.xbot_env import XBotLFreeEnv
from sim.envs.humanoids.zeroth_config import ZerothCfg, ZerothCfgPPO
from sim.envs.humanoids.zeroth_env import ZerothEnv
from sim.utils.task_registry import TaskRegistry  # noqa: E402

task_registry = TaskRegistry()
task_registry.register("gpr", GprFreeEnv, GprCfg(), GprCfgPPO())
task_registry.register("gpr_standing", GprFreeEnv, GprStandingCfg(), GprCfgPPO())
task_registry.register("dora", DoraFreeEnv, DoraCfg(), DoraCfgPPO())
task_registry.register("h1", H1FreeEnv, H1Cfg(), H1CfgPPO())
task_registry.register("g1", G1FreeEnv, G1Cfg(), G1CfgPPO())
task_registry.register("XBotL_free", XBotLFreeEnv, XBotCfg(), XBotCfgPPO())
task_registry.register("zeroth", ZerothEnv, ZerothCfg(), ZerothCfgPPO())
