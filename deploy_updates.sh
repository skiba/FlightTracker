#!/bin/bash
# Deploy FlightTracker updates to Raspberry Pi
# Usage: ./deploy_updates.sh

PI_HOST="skibinskig@flightradarpi.local"
PI_PATH="~/FlightTracker"

echo "🚀 Deploying FlightTracker updates to Raspberry Pi..."
echo ""

# Copy updated weather scene (temperature display fix)
echo "📝 Copying weather.py (temperature display fix)..."
scp scenes/weather.py $PI_HOST:$PI_PATH/scenes/

# Copy utilities
echo "📝 Copying airports.py (new airport city names feature)..."
scp utilities/airports.py $PI_HOST:$PI_PATH/utilities/

echo "📝 Copying overhead.py (increased flight limit to 10)..."
scp utilities/overhead.py $PI_HOST:$PI_PATH/utilities/

# Copy updated journey scene
echo "📝 Copying journey.py (city names support)..."
scp scenes/journey.py $PI_HOST:$PI_PATH/scenes/

# Copy updated plane details scene
echo "📝 Copying planedetails.py (route display in scrolling text)..."
scp scenes/planedetails.py $PI_HOST:$PI_PATH/scenes/

# Copy updated config
echo "📝 Copying config.py (your settings and API key)..."
scp config.py $PI_HOST:$PI_PATH/

echo ""
echo "✅ Files copied successfully!"
echo ""
echo "To apply changes, restart the FlightTracker service:"
echo "  ssh $PI_HOST 'sudo systemctl restart FlightTracker.service'"
echo ""
echo "To check status:"
echo "  ssh $PI_HOST 'sudo systemctl status FlightTracker.service'"
echo ""
echo "To view logs:"
echo "  ssh $PI_HOST 'journalctl -u FlightTracker.service -f'"

