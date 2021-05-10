#!/usr/bin/env python3
import os
from typing import Union

from rofication import RoficationGui, RoficationClient, resources, Resource

if __name__ == '__main__':
    # defaults
    label_icon: Resource = resources.notify_none
    label_color: Resource = resources.label_color
    value_color: Resource = resources.value_color
    value_font: Resource = resources.value_font

    num: Union[int, str]
    try:
        client = RoficationClient()

        if os.getenv('button'):
            RoficationGui(client).run()

        num, crit = client.count()
        if num > 0:
            label_icon = resources.notify_some
            value_color = resources.warning_color
        if crit > 0:
            value_color = resources.critical_color
    except (FileNotFoundError, ConnectionRefusedError):
        label_icon = resources.notify_error
        label_color = resources.critical_color
        num = '?'

    # only fetch resources if needed
    label = f'<span foreground="{label_color.fetch()}">{label_icon.fetch()}</span>'
    value = f'<span font_desc="{value_font.fetch()}" foreground="{value_color.fetch()}"> {num}</span>'
    print(label + value)
