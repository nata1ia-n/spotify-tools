"""Spotify utils functions"""

import os
from typing import Any

import spotipy
from spotipy.oauth2 import SpotifyOAuth


def create_spotify_client():
    """Create a spotify client"""
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=["playlist-read-private", "playlist-modify-private"],
        )
    )
    return sp


def get_playlist_tracks(sp: spotipy.Spotify, playlist_id: str):
    """Fetch all tracks from a given playlist."""
    tracks = []
    results: Any = sp.playlist_tracks(playlist_id)
    tracks.extend(results["items"])
    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    return tracks


def create_playlist(sp: spotipy.Spotify, user_id: str, name: str, description: str):
    """Create a new playlist"""
    return sp.user_playlist_create(
        user=user_id, name=name, public=False, description=description
    )


def add_tracks_in_chunks(
    sp: spotipy.Spotify, playlist_id: str, track_uris: list, replace: bool = False
):
    """Add tracks in chunks of 100 (because of Spotify's limits)"""
    if replace:
        sp.playlist_replace_items(playlist_id, [])
    for i in range(0, len(track_uris), 100):
        chunk = track_uris[i : i + 100]
        sp.playlist_add_items(playlist_id, chunk)
