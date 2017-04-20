from plenum.common.init_util import initialize_node_environment as \
    p_initialize_node_environment, cleanup_environment
from sovrin_common.config_util import getConfig


def initialize_node_environment(name, base_dir, sigseed=None,
                                override_keep=False,
                                config=None):
    config = config or getConfig()
    cleanup_environment(name, config)
    vk = p_initialize_node_environment(name, base_dir, sigseed, override_keep)

    return vk
