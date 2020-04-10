#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x1A-user_io.json
# Device ID:          0x1A
# Device Name:        io
# Timestamp:          04/10/2020 @ 19:07:32.828820 (UTC)

from sphero_sdk.common.enums.io_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def set_all_leds(led_group, led_brightness_values, target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.set_all_leds,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='ledGroup',
                data_type='uint32_t',
                index=0,
                value=led_group,
                size=1
            ),
            Parameter( 
                name='ledBrightnessValues',
                data_type='uint8_t',
                index=1,
                value=led_brightness_values,
                size=32
            ),
        ],
    }


def get_active_color_palette(target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.get_active_color_palette,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='rgbIndexBytes',
                data_type='uint8_t',
                index=0,
                size=48,
            ),
        ]
    }


def set_active_color_palette(rgb_index_bytes, target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.set_active_color_palette,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='rgbIndexBytes',
                data_type='uint8_t',
                index=0,
                value=rgb_index_bytes,
                size=48
            ),
        ],
    }


def get_color_identification_report(red, green, blue, confidence_threshold, target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.get_color_identification_report,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='red',
                data_type='uint8_t',
                index=0,
                value=red,
                size=1
            ),
            Parameter( 
                name='green',
                data_type='uint8_t',
                index=1,
                value=green,
                size=1
            ),
            Parameter( 
                name='blue',
                data_type='uint8_t',
                index=2,
                value=blue,
                size=1
            ),
            Parameter( 
                name='confidenceThreshold',
                data_type='uint8_t',
                index=3,
                value=confidence_threshold,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='indexConfidenceByte',
                data_type='uint8_t',
                index=0,
                size=24,
            ),
        ]
    }


def load_color_palette(palette_index, target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.load_color_palette,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='paletteIndex',
                data_type='uint8_t',
                index=0,
                value=palette_index,
                size=1
            ),
        ],
    }


def save_color_palette(palette_index, target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.save_color_palette,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='paletteIndex',
                data_type='uint8_t',
                index=0,
                value=palette_index,
                size=1
            ),
        ],
    }


def release_led_requests(target, timeout): 
    return { 
        'did': DevicesEnum.io,
        'cid': CommandsEnum.release_led_requests,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }
