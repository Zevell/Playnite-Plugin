from __future__ import annotations

from typing import TYPE_CHECKING

from library_server import LibraryServerUnavailable, fetch_games

if TYPE_CHECKING:
    from playnite import Game, PlayniteLibrary


def games(server_port: int, include_hidden: bool, fallback: "PlayniteLibrary") -> "list[Game]":
    try:
        return fetch_games(port=server_port, include_hidden=include_hidden)
    except LibraryServerUnavailable:
        return fallback.games(include_hidden=include_hidden)
