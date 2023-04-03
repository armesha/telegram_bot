#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2023
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the classes that represent Telegram InlineQueryResultAudio."""
from typing import TYPE_CHECKING, Optional, Sequence, Tuple

from telegram._inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram._inline.inlinequeryresult import InlineQueryResult
from telegram._messageentity import MessageEntity
from telegram._utils.argumentparsing import parse_sequence_arg
from telegram._utils.defaultvalue import DEFAULT_NONE
from telegram._utils.types import JSONDict, ODVInput
from telegram.constants import InlineQueryResultType

if TYPE_CHECKING:
    from telegram import InputMessageContent


class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user.
    Alternatively, you can use :attr:`input_message_content` to send a message with the specified
    content instead of the audio.

    .. seealso:: :wiki:`Working with Files and Media <Working-with-Files-and-Media>`

    Args:
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`telegram.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`telegram.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        audio_url (:obj:`str`): A valid URL for the audio file.
        title (:obj:`str`): Title.
        performer (:obj:`str`, optional): Performer.
        audio_duration (:obj:`str`, optional): Audio duration in seconds.
        caption (:obj:`str`, optional): Caption,
            0-:tg-const:`telegram.constants.MessageLimit.CAPTION_LENGTH` characters after entities
            parsing.
        parse_mode (:obj:`str`, optional): |parse_mode|
        caption_entities (Sequence[:class:`telegram.MessageEntity`], optional): |caption_entities|

            .. versionchanged:: 20.0
                |sequenceclassargs|
        reply_markup (:class:`telegram.InlineKeyboardMarkup`, optional): Inline keyboard attached
            to the message.
        input_message_content (:class:`telegram.InputMessageContent`, optional): Content of the
            message to be sent instead of the audio.

    Attributes:
        type (:obj:`str`): :tg-const:`telegram.constants.InlineQueryResultType.AUDIO`.
        id (:obj:`str`): Unique identifier for this result,
            :tg-const:`telegram.InlineQueryResult.MIN_ID_LENGTH`-
            :tg-const:`telegram.InlineQueryResult.MAX_ID_LENGTH` Bytes.
        audio_url (:obj:`str`): A valid URL for the audio file.
        title (:obj:`str`): Title.
        performer (:obj:`str`): Optional. Performer.
        audio_duration (:obj:`str`): Optional. Audio duration in seconds.
        caption (:obj:`str`): Optional. Caption,
            0-:tg-const:`telegram.constants.MessageLimit.CAPTION_LENGTH` characters after entities
            parsing.
        parse_mode (:obj:`str`): Optional. |parse_mode|
        caption_entities (Tuple[:class:`telegram.MessageEntity`]): Optional. |captionentitiesattr|

            .. versionchanged:: 20.0

                * |tupleclassattrs|
                * |alwaystuple|
        reply_markup (:class:`telegram.InlineKeyboardMarkup`): Optional. Inline keyboard attached
            to the message.
        input_message_content (:class:`telegram.InputMessageContent`): Optional. Content of the
            message to be sent instead of the audio.

    """

    __slots__ = (
        "reply_markup",
        "caption_entities",
        "caption",
        "title",
        "parse_mode",
        "audio_url",
        "performer",
        "input_message_content",
        "audio_duration",
    )

    def __init__(
        self,
        id: str,  # pylint: disable=redefined-builtin
        audio_url: str,
        title: str,
        performer: str = None,
        audio_duration: int = None,
        caption: str = None,
        reply_markup: InlineKeyboardMarkup = None,
        input_message_content: "InputMessageContent" = None,
        parse_mode: ODVInput[str] = DEFAULT_NONE,
        caption_entities: Sequence[MessageEntity] = None,
        *,
        api_kwargs: JSONDict = None,
    ):
        # Required
        super().__init__(InlineQueryResultType.AUDIO, id, api_kwargs=api_kwargs)
        with self._unfrozen():
            self.audio_url: str = audio_url
            self.title: str = title

            # Optionals
            self.performer: Optional[str] = performer
            self.audio_duration: Optional[int] = audio_duration
            self.caption: Optional[str] = caption
            self.parse_mode: ODVInput[str] = parse_mode
            self.caption_entities: Tuple[MessageEntity, ...] = parse_sequence_arg(caption_entities)
            self.reply_markup: Optional[InlineKeyboardMarkup] = reply_markup
            self.input_message_content: Optional[InputMessageContent] = input_message_content
