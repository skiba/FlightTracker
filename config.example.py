# FlightTracker Configuration Template
# Copy this to config.py and customize for your location

ZONE_HOME = {
    "tl_y": 52.51,   # Top-Left Latitude (deg)
    "tl_x": 16.75,   # Top-Left Longitude (deg)
    "br_y": 52.33,   # Bottom-Right Latitude (deg)
    "br_x": 17.03    # Bottom-Right Longitude (deg)
}

LOCATION_HOME = [
    52.419888,  # Latitude (deg)
    16.888337,  # Longitude (deg)
    0.08        # Altitude (km)
]

WEATHER_LOCATION = "Poznan,PL"  # City,Country format

# Get your free API key at https://openweathermap.org/price
OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"

TEMPERATURE_UNITS = "metric"  # or "imperial"
MIN_ALTITUDE = 100  # feet (filter out planes on ground)
BRIGHTNESS = 50  # 0-100
GPIO_SLOWDOWN = 2  # 0-4, higher for faster Pi models
JOURNEY_CODE_SELECTED = "POZ"  # Your nearest airport (displays in bold)
JOURNEY_BLANK_FILLER = " ? "
HAT_PWM_ENABLED = True  # Requires solder bridge on HAT

# Airport Display Options
JOURNEY_USE_CITY_NAMES = False   # Keep airport codes at top (e.g., "POZ → WAW")
JOURNEY_CITY_MAX_LENGTH = 8      # Maximum characters for city names
PLANE_DETAILS_SHOW_ROUTE = True  # Show full city names in scrolling plane details
PLANE_DETAILS_ROUTE_SEPARATOR = " -> "  # Direction separator between cities

