#!/bin/bash
# Setup script to commit your customizations and push to your fork
# Replace YOUR_USERNAME with your actual GitHub username

set -e  # Exit on error

echo "🚀 FlightTracker - Setting up your custom fork"
echo ""

# Step 1: Verify we're in the right directory
if [ ! -f "flight-tracker.py" ]; then
    echo "❌ Error: Not in FlightTracker directory"
    exit 1
fi

# Step 2: Create a custom branch for your changes
echo "📝 Creating custom branch 'poznan-customizations'..."
git checkout -b poznan-customizations

# Step 3: Stage all your changes
echo "📦 Staging all changes..."
git add .gitignore
git add config.example.py
git add scenes/weather.py
git add scenes/journey.py
git add scenes/planedetails.py
git add utilities/airports.py
git add utilities/overhead.py
git add deploy_updates.sh
git add CITY_NAMES_FEATURE.md
git add DISPLAY_EXAMPLE.md
git add GIT_WORKFLOW.md
git add setup_my_fork.sh

# Also stage any other modified files
git add display/__init__.py
git add scenes/date.py
git add scenes/day.py

# Note: config.py is ignored (contains your API key)

echo ""
echo "📋 Files to be committed:"
git status --short

echo ""
read -p "Continue with commit? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 1
fi

# Step 4: Commit with a descriptive message
echo ""
echo "💾 Creating commit..."
git commit -m "Custom Poznan FlightTracker Setup

Features added:
- Fixed temperature display (right-aligned, correct colors)
- Added airport city name mapping (150+ airports)
- Full city names in scrolling plane details
- Configurable route separator (->)
- Increased flight display from 5 to 10
- Updated config for Poznan location
- Added deployment script

Files modified:
- scenes/weather.py: Temperature display fixes
- scenes/journey.py: City name support (optional)
- scenes/planedetails.py: Route display in scrolling text
- utilities/airports.py: Airport code to city mapping
- utilities/overhead.py: Increased MAX_FLIGHT_LOOKUP to 10
- config.py: Poznan location and display options
- deploy_updates.sh: Deployment automation

Files added:
- CITY_NAMES_FEATURE.md: Feature documentation
- DISPLAY_EXAMPLE.md: Visual examples
"

echo ""
echo "✅ Commit created successfully!"
echo ""
echo "📤 Next steps:"
echo ""
echo "1. Go to GitHub and fork the original repository:"
echo "   https://github.com/ColinWaddell/FlightTracker"
echo ""
echo "2. Add your fork as a remote (replace YOUR_USERNAME):"
echo "   git remote add myfork https://github.com/YOUR_USERNAME/FlightTracker.git"
echo ""
echo "3. Push your custom branch:"
echo "   git push myfork poznan-customizations"
echo ""
echo "4. (Optional) Set as default branch on your fork via GitHub settings"
echo ""
echo "🎉 Done! Your changes are ready to push."

