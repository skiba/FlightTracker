# FlightTracker Display Examples

## Recommended Setup (Codes Top + Full Names Bottom)

### Configuration
```python
JOURNEY_USE_CITY_NAMES = False  # Keep codes at top (compact, clear)
PLANE_DETAILS_SHOW_ROUTE = True  # Full city names in scrolling
```

### Display Output
```
┌─────────────────────────────────────────────────┐
│ FRA → POZ                            12.5°C     │  Row 1-12
│                                                 │
│ LH1234                                    1/2   │  Row 13-21
│─────────────────────────────────────────────────│  Row 22
│← Airbus A320 - Frankfurt → Poznan              │  Row 23-32
└─────────────────────────────────────────────────┘
    ↑                                              ↑
    Scrolling from right to left continuously
```

**What you see:**
1. **Top (Static)**: Airport codes (3 letters, compact, easy to read)
2. **Middle**: Flight number and temperature  
3. **Bottom (Scrolling)**: Full plane type and complete city names

**Why this is best:**
- ✅ Top stays clean and compact (like original)
- ✅ You know exactly which airports (codes are standard)
- ✅ Full city names scroll at bottom (no space constraints)
- ✅ Best of both worlds!

---

## Mixed: Codes + Full Names

### Configuration
```python
JOURNEY_USE_CITY_NAMES = False     # Keep codes at top
PLANE_DETAILS_SHOW_ROUTE = True    # Full names in scrolling
```

### Display Output
```
┌─────────────────────────────────────────────────┐
│ FRA → POZ                            12.5°C     │
│                                                 │
│ LH1234                                    1/2   │
│─────────────────────────────────────────────────│
│← Airbus A320 - Frankfurt → Poznan              │
└─────────────────────────────────────────────────┘
```

**What you see:**
1. **Top**: Airport codes (compact, fits easily)
2. **Bottom**: Full city names (scrolling, no space limit)

**This is the recommended setup!** ✨

---

## Classic: Original Display

### Configuration
```python
JOURNEY_USE_CITY_NAMES = False
PLANE_DETAILS_SHOW_ROUTE = False
```

### Display Output
```
┌─────────────────────────────────────────────────┐
│ FRA → POZ                            12.5°C     │
│                                                 │
│ LH1234                                    1/2   │
│─────────────────────────────────────────────────│
│← Airbus A320                                   │
└─────────────────────────────────────────────────┘
```

**What you see:**
- Original behavior
- No city names, only codes
- Shorter scrolling text

---

## Real-World Examples

### Example 1: Short Route
```
Flight: LH1234 from MUC to BER
Plane: Boeing 737

Top:    Munich → Berlin            12.5°C
Bottom: Boeing 737 - Munich → Berlin
```

### Example 2: Long City Names (Truncated)
```
Flight: BA456 from LHR to ATH
Plane: Airbus A321

Top:    London → Athens            15.2°C
Bottom: Airbus A321 - London → Athens
```

### Example 3: Intercontinental
```
Flight: DL123 from JFK to FRA
Plane: Boeing 777

Top:    New York → Frankfur        8.3°C
Bottom: Boeing 777 - New York → Frankfurt
```

---

## Scrolling Animation

The bottom text scrolls continuously from right to left:

```
Frame 1:  │                              Airbus A320 - Frankfurt → Poznan
Frame 2:  │                             Airbus A320 - Frankfurt → Poznan 
Frame 3:  │                            Airbus A320 - Frankfurt → Poznan  
...
Frame N:  │Airbus A320 - Frankfurt → Poznan                              
Frame N+1:│irbus A320 - Frankfurt → Poznan                               
...
```

**Speed**: 1 pixel per frame = 10 pixels per second (smooth and readable)

---

## Display Dimensions

```
Total: 64×32 pixels

Sections:
┌────────────────────────┐
│ Journey (Row 0-11)     │  12 pixels height
│ Flight Info (Row 12-21)│  10 pixels height
│ Divider (Row 22)       │   1 pixel
│ Plane Details (Row 23+)│   9 pixels height
└────────────────────────┘
```

---

## Tips for Best Display

1. **Use mixed mode** (codes top, names bottom) for best readability
2. **Keep `JOURNEY_CITY_MAX_LENGTH = 8`** for optimal fit on 64px width
3. **Enable `PLANE_DETAILS_SHOW_ROUTE = True`** for full information
4. **Add your local airports** to `utilities/airports.py` if missing

---

## Color Coding

- **Journey route**: Yellow (`JOURNEY_COLOUR`)
- **Plane details**: Pink (`PLANE_DETAILS_COLOUR`)
- **Temperature**: Color-coded by value (blue=cold, red=hot)
- **Flight number**: Blue/Light blue (letters/numbers)

