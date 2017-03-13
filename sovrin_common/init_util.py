from plenum.common.init_util import initialize_node_environment as \
    p_initialize_node_environment


def cleanup_environment(name, base_dir):
    # TODO:
    pass


def initialize_node_environment(name, base_dir, sigseed=None, override=False):
    # Question: Does this comment belong here? I dont think so.
    """
    transport-agnostic method; in the future when the transport protocol is
    abstracted a bit more, this function and the one below will be the same
    and likely a method of an interface
    """
    vk = p_initialize_node_environment(name, base_dir, sigseed, override)
    return vk

