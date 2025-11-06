# Airport City Names Feature

## Overview
This feature enriches flight display by showing full city names in the scrolling plane details.

**Recommended Setup (Default):**
- **Journey display (top)**: Airport codes `FRA → POZ` (compact, standard)
- **Plane details (scrolling bottom)**: Full city names `Airbus A320 - Frankfurt → Poznan`

**Example on your display:**
- **Top**: `POZ → WAW` (3-letter codes like before)
- **Bottom scrolling**: `Airbus A320 - Poznan → Warsaw` (full city names)

This gives you the **best of both worlds** - clean compact codes at the top, and full descriptive city names in the scrolling text!

## What Changed

### New Files
- **`utilities/airports.py`**: Airport code → city name mapping utility
  - Contains 150+ major airport mappings
  - Fast static lookup (no API calls needed)
  - Supports European, US, and major international airports

### Modified Files
- **`scenes/journey.py`**: Now supports displaying city names in the top route display
- **`scenes/planedetails.py`**: Now shows full route in scrolling plane details
- **`scenes/weather.py`**: Fixed temperature display positioning and color gradient
- **`config.py`**: Added configuration options

## Configuration

The recommended configuration (already set in your `config.py`):

```python
# Airport Display Options
JOURNEY_USE_CITY_NAMES = False   # Keep airport codes at top (e.g., "POZ → WAW")
JOURNEY_CITY_MAX_LENGTH = 8      # Maximum characters for city names (only used if enabled)
PLANE_DETAILS_SHOW_ROUTE = True  # Show full city names in scrolling plane details (bottom)
```

**This gives you:**
- Top: `FRA → POZ` (clean, compact airport codes)
- Bottom: `Airbus A320 - Frankfurt → Poznan` (full city names)

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `JOURNEY_USE_CITY_NAMES` | bool | `False` | Enable/disable city name display in top route |
| `JOURNEY_CITY_MAX_LENGTH` | int | `8` | Maximum characters to display in top route (truncates longer names) |
| `PLANE_DETAILS_SHOW_ROUTE` | bool | `True` | Show full city route in scrolling plane details at bottom |

## Supported Airports

The mapping includes **150+ airports** covering:

### Europe
- 🇵🇱 Poland: WAW, KRK, GDN, WRO, POZ, KTW, etc.
- 🇩🇪 Germany: FRA, MUC, BER, DUS, HAM, CGN, etc.
- 🇬🇧 UK: LHR, LGW, MAN, EDI, GLA, etc.
- 🇫🇷 France: CDG, ORY, NCE, LYS, MRS, etc.
- 🇪🇸 Spain: MAD, BCN, AGP, PMI, etc.
- 🇮🇹 Italy: FCO, MXP, VCE, etc.
- 🇳🇱 Netherlands: AMS, RTM, EIN
- 🇨🇭 Switzerland: ZRH, GVA, BSL
- 🇦🇹 Austria: VIE, SZG, INN
- 🇨🇿 Czech Republic: PRG, BRQ
- 🇸🇪 Scandinavia: CPH, ARN, OSL, HEL, etc.
- And many more...

### USA
Major hubs: JFK, LAX, ORD, ATL, DFW, SFO, etc.

## Adding More Airports

To add airports not in the mapping, edit `utilities/airports.py`:

```python
AIRPORT_CITY_MAP = {
    # ... existing mappings ...
    "YOUR_CODE": "Your City",  # Add your airport here
}
```

## Display Layout

With the new feature, your LED matrix will show:

```
┌────────────────────────────────────────┐
│  Frankfurt → Poznan        12.5°C      │  ← Top: Journey (truncated city names)
│                                        │
│  LH1234                                │  ← Middle: Flight details
│ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ │
│ Airbus A320 - Frankfurt → Poznan  ←─ │  ← Bottom: Scrolling (full city names)
└────────────────────────────────────────┘
```

**Benefits:**
- **Top display**: Quick glance with truncated names (fits in space)
- **Bottom scrolling**: Full city names for clarity (scrolls indefinitely)
- **Best of both worlds**: Compact view + complete information

## Examples

### Display Settings

**Compact (fits more on screen):**
```python
JOURNEY_USE_CITY_NAMES = True
JOURNEY_CITY_MAX_LENGTH = 6
```
Result: `Frankf → Poznan`

**Full names (may overflow on small display):**
```python
JOURNEY_USE_CITY_NAMES = True
JOURNEY_CITY_MAX_LENGTH = 12
```
Result: `Frankfurt → Poznan`

**Airport codes only (original behavior):**
```python
JOURNEY_USE_CITY_NAMES = False
PLANE_DETAILS_SHOW_ROUTE = False
```
Result:
- Top: `FRA → POZ`
- Bottom scrolling: `Airbus A320` (no route)

**Show route only in scrolling text:**
```python
JOURNEY_USE_CITY_NAMES = False
PLANE_DETAILS_SHOW_ROUTE = True
```
Result:
- Top: `FRA → POZ`
- Bottom scrolling: `Airbus A320 - Frankfurt → Poznan`

## Performance

- **Zero API calls**: Uses fast static dictionary lookup
- **Cached results**: First lookup is cached via `@lru_cache`
- **No network required**: Works completely offline
- **Instant lookups**: Sub-millisecond performance

## Fallback Behavior

If an airport code is **not** in the mapping:
- Falls back to displaying the 3-letter IATA code
- No errors or crashes
- You can optionally enable API fallback (see code comments)

## Testing

Test the mapping from command line:

```bash
cd /home/pi/FlightTracker
python3 utilities/airports.py
```

Expected output:
```
Testing airport code to city name mapping:
  FRA -> Frankfurt
  POZ -> Poznan
  WAW -> Warsaw
  LHR -> London
  JFK -> New York
  XXX -> Not found

Testing route formatting:
  FRA -> POZ: Frankfurt -> Poznan
```

## Deployment

To deploy to your Raspberry Pi:

**Option 1: Use deployment script (recommended)**
```bash
cd /Users/grzegorzskibinski/workspace/FlightTracker
./deploy_updates.sh
```

**Option 2: Manual deployment**
```bash
# Copy updated files
scp utilities/airports.py skibinskig@flightradarpi.local:~/FlightTracker/utilities/
scp scenes/journey.py skibinskig@flightradarpi.local:~/FlightTracker/scenes/
scp scenes/planedetails.py skibinskig@flightradarpi.local:~/FlightTracker/scenes/
scp scenes/weather.py skibinskig@flightradarpi.local:~/FlightTracker/scenes/
scp config.py skibinskig@flightradarpi.local:~/FlightTracker/

# Restart the service
ssh skibinskig@flightradarpi.local "sudo systemctl restart FlightTracker.service"
```

## Troubleshooting

**Q: City names are cut off**
- Increase `JOURNEY_CITY_MAX_LENGTH` or use smaller font

**Q: Airport code not recognized**
- Add it to `AIRPORT_CITY_MAP` in `utilities/airports.py`

**Q: Want to see both code and city?**
- Use `JOURNEY_USE_CITY_NAMES = False` and `PLANE_DETAILS_SHOW_ROUTE = True`
- This shows codes at top, full city names in scrolling text

**Q: Scrolling text is too long**
- Disable route in scrolling by setting `PLANE_DETAILS_SHOW_ROUTE = False`

## Future Enhancements

Potential improvements:
- [ ] Add scrolling for long city names
- [ ] Option to show "Code (City)" format
- [ ] Dynamic font sizing based on name length
- [ ] API fallback for unknown airports
- [ ] Country flags next to city names

