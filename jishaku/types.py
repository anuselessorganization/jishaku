# -*- coding: utf-8 -*-

"""
jishaku.types
~~~~~~~~~~~~~

Declarations for type checking

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import typing

from discord.ext import commands

BotT = commands.Bot
ContextT = typing.TypeVar('ContextT', commands.Context[commands.Bot], commands.Context[BotT])
ContextA = commands.Context[BotT]
