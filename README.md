# Create a playlist with Spotify API

This Python script interacts with the Spotify API to create customized playlists. Given an existing playlist and artist name, it automatically generates a new playlist containing only songs by that specified artist.

## Prerequisites

- A Spotify account with the Spotify API enabled in your developer settings
- uv package manager (handles all other dependencies)
  - can be installed with 'brew install uv' (macOS) or 'pip install uv' (Windows)

## Usage

1. Create a new file named `.env` in the root directory with your Spotify API credentials:
   ```shell
   # Example contents of .env file
   SPOTIPY_CLIENT_ID="YOUR_SPOTIPY_CLIENT_ID"
   SPOTIPY_CLIENT_SECRET="YOUR_SPOTIPY_CLIENT_SECRET"
   SPOTIPY_REDIRECT_URI="YOUR_SPOTIPY_REDIRECT_URI"
   ```
2. Run the script with `make run`
3. Follow the prompts to create a new playlist.
