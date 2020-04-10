#!/usr/bin/env python3
# This file is automatically generated!
# Timestamp:          04/10/2020 @ 19:07:32.939661 (UTC)

from enum import IntEnum
from sphero_sdk.common import commands
from sphero_sdk.common.helpers import text_to_pascal_case


class DevicesEnum(IntEnum): 
    api_and_shell = 0x10
    system_info = 0x11
    power = 0x13
    drive = 0x16
    sensor = 0x18
    connection = 0x19
    io = 0x1A


def get_device_path_by_did(did): 
    device_name = DevicesEnum(did).name
    return text_to_pascal_case(device_name)


def get_command_path_by_cid(did, cid): 
    device_name = DevicesEnum(did).name

    command_name = eval( 
        'commands.{}.CommandsEnum({}).name'.format( 
            device_name,
            cid
        )
    )

    return text_to_pascal_case(command_name)
