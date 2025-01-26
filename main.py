"""Create a new playlist"""

from dotenv import load_dotenv

from spotify import (
    add_tracks_in_chunks,
    create_playlist,
    create_spotify_client,
    get_playlist_tracks,
)

load_dotenv()


def main():
    """Main function to execute the script."""
    source_playlist_id = input("Enter the playlist ID: ").strip()
    target_artist_name = input("Enter the artist name: ").strip()

    sp = create_spotify_client()
    user = sp.current_user()
    if not user:
        print("😖 Could not get user information.")
        return

    user_id = user["id"]

    print("🎶 Fetching tracks from given playlist...")
    tracks = get_playlist_tracks(sp, source_playlist_id)

    print("🎶 Filtering tracks...")
    filtered_tracks = [
        track["track"]["uri"]
        for track in tracks
        if track.get("track")
        and track["track"].get("artists")
        and any(
            artist["name"].lower() == target_artist_name.lower()
            for artist in track["track"]["artists"]
        )
    ]

    new_playlist_name = f"Filtered by {target_artist_name}"
    print(f"🎼 Creating a new playlist: {new_playlist_name}...")
    new_playlist = create_playlist(
        sp,
        user_id,
        new_playlist_name,
        f"Songs by {target_artist_name}",
    )
    if not new_playlist:
        print("😖 Could not create a new playlist.")
        return

    new_playlist_id = new_playlist["id"]

    if filtered_tracks:
        add_tracks_in_chunks(sp, new_playlist_id, filtered_tracks)
        print(
            f"✅ Success! Created new playlist '{new_playlist_name}' with {len(filtered_tracks)} tracks."
        )
    else:
        print("❌ No tracks found by the specified artist.")


if __name__ == "__main__":
    main()
