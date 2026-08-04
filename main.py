from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Audio Engine",
    description="Sleek Music Streaming & Playlist Layout API",
    version="1.5.0"
)

# Enable seamless mobile testing without running into network blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_music_experience():
    return {
        "status": "success",
        
        # 👤 1. USER PROFILE IDENTITY
        "user_profile": {
            "listener_name": "Pavithra Pramod",
            "roll_number": "24MIC0022",
            "account_tier": "Premium Curator Verified Account 🎧"
        },
        
        # 🎨 2. MUSIC APP SKIN & DESIGN CONFIGURATION (Over-the-Air Style)
        "app_skin": {
            "player_name": "Studio Music",
            "dark_mode": True,
            "primary_color": "#1DB954",       # Spotify Green Accent
            "secondary_color": "#BB86FC",     # Deep Neon Purple
            "background_canvas": "#121212",   # Dark Onyx Studio Black
            "card_background": "#1E1E1E",     # Charcoal Grey Panel
            "ui_border_radius": 16,           # Smooth rounded modern album sheets
            "font_style": "Circular_Std_Bold"
        },
        
        # 📱 3. LIVE AUDIO PLAYER & PLAYLIST OBJECT MATRICES
        "audio_widgets": [
            {
                "id": "widget_player_01",
                "component_type": "now_playing_dock",
                "properties": {
                    "track_title": "Starboy",
                    "artist": "The Weeknd",
                    "album_name": "Starboy (Deluxe)",
                    "album_cover_url": "https://placehold.co",
                    "is_playing": True,
                    "duration_seconds": 230,
                    "current_progress_seconds": 88
                }
            },
            {
                "id": "widget_playlist_02",
                "component_type": "heavy_rotation_row",
                "section_title": "Your Top Daily Heavy Rotation",
                "tracks_list": [
                    {"id": 101, "title": "Blinding Lights", "artist": "The Weeknd", "plays": "248"},
                    {"id": 102, "title": "Levitating", "artist": "Dua Lipa", "plays": "184"},
                    {"id": 103, "title": "Sweater Weather", "artist": "The Neighbourhood", "plays": "142"},
                    {"id": 104, "title": "Nightcall", "artist": "Kavinsky", "plays": "96"}
                ]
            },
            {
                "id": "widget_shortcuts_03",
                "component_type": "quick_genre_grid",
                "genres": [
                    {"label": "Lo-Fi Beats", "emoji": "☕", "accent_tint": "#FFB7B2"},
                    {"label": "Synthwave", "emoji": "🌌", "accent_tint": "#BB86FC"},
                    {"label": "Pop Essentials", "emoji": "🔥", "accent_tint": "#1DB954"}
                ]
            }
        ],
        
        # 🧭 4. STREAMING UI BOTTOM NAVIGATION ARCHITECTURE
        "navigation_bar": {
            "current_tab_index": 0,
            "tabs": [
                {"label": "Home", "icon": "music_home"},
                {"label": "Search", "icon": "magnifying_glass"},
                {"label": "Your Library", "icon": "audio_library"}
            ]
        }
    }
