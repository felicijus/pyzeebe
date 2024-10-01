from typing import Optional

import grpc

from pyzeebe.channel.channel_options import get_channel_options
from pyzeebe.channel.utils import create_address
from pyzeebe.types import ChannelArgumentType


def create_secure_channel(
    grpc_address: Optional[str] = None,
    channel_options: Optional[ChannelArgumentType] = None,
    channel_credentials: Optional[grpc.ChannelCredentials] = None,
) -> grpc.aio.Channel:
    """
    Create a secure channel

    Args:
        hostname (Optional[str], optional): Zeebe gateway hostname
        port (Optional[int], optional): Zeebe gateway port
        channel_options (Optional[Dict], optional): GRPC channel options.
            See https://grpc.github.io/grpc/python/glossary.html#term-channel_arguments
        channel_credentials (Optional[grpc.ChannelCredentials]): Channel credentials to use.
            Will use grpc.ssl_channel_credentials() if not provided.

    Returns:
        grpc.aio.Channel: A GRPC Channel connected to the Zeebe gateway.
    """
    grpc_address = create_address(grpc_address=grpc_address)
    credentials = channel_credentials or grpc.ssl_channel_credentials()
    return grpc.aio.secure_channel(
        target=grpc_address, credentials=credentials, options=get_channel_options(channel_options)
    )
