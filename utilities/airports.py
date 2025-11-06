# -*- coding: utf-8 -*-
"""
Airport code to city name mapping utility.
Provides fast lookup for common airports with optional API fallback.
"""

from functools import lru_cache
from typing import Optional

# Static mapping of IATA codes to city names (common European airports)
# This provides fast lookups without API calls
AIRPORT_CITY_MAP = {
    # Poland
    "WAW": "Warsaw",
    "KRK": "Krakow",
    "GDN": "Gdansk",
    "WRO": "Wroclaw",
    "POZ": "Poznan",
    "KTW": "Katowice",
    "RZE": "Rzeszow",
    "SZZ": "Szczecin",
    "LCJ": "Lodz",
    "BZG": "Bydgoszcz",
    "IEG": "Zielona Gora",

    # Germany
    "FRA": "Frankfurt",
    "MUC": "Munich",
    "BER": "Berlin",
    "DUS": "Dusseldorf",
    "HAM": "Hamburg",
    "CGN": "Cologne",
    "STR": "Stuttgart",
    "DTM": "Dortmund",
    "NUE": "Nuremberg",
    "HAJ": "Hannover",
    "LEJ": "Leipzig",
    "BRE": "Bremen",
    "DRS": "Dresden",

    # UK & Ireland
    "LHR": "London",
    "LGW": "London",
    "STN": "London",
    "LTN": "London",
    "LCY": "London",
    "MAN": "Manchester",
    "BHX": "Birmingham",
    "EDI": "Edinburgh",
    "GLA": "Glasgow",
    "BRS": "Bristol",
    "NCL": "Newcastle",
    "LBA": "Leeds",
    "DUB": "Dublin",
    "ORK": "Cork",
    "SNN": "Shannon",
    "BFS": "Belfast",

    # France
    "CDG": "Paris",
    "ORY": "Paris",
    "BVA": "Paris Beauvais",
    "NCE": "Nice",
    "LYS": "Lyon",
    "MRS": "Marseille",
    "TLS": "Toulouse",
    "BOD": "Bordeaux",
    "NTE": "Nantes",

    # Spain (Mainland + Islands)
    "MAD": "Madrid",
    "BCN": "Barcelona",
    "AGP": "Malaga",
    "PMI": "Palma de Mallorca",
    "IBZ": "Ibiza",
    "SVQ": "Seville",
    "VLC": "Valencia",
    "ALC": "Alicante",
    "BIO": "Bilbao",
    "TFS": "Tenerife South",
    "TFN": "Tenerife North",
    "LPA": "Gran Canaria",
    "ACE": "Lanzarote",
    "FUE": "Fuerteventura",

    # Italy
    "FCO": "Rome",
    "CIA": "Rome",
    "MXP": "Milan",
    "LIN": "Milan",
    "BGY": "Milan Bergamo",
    "VCE": "Venice",
    "NAP": "Naples",
    "BLQ": "Bologna",
    "CTA": "Catania",
    "PMO": "Palermo",
    "PSA": "Pisa",
    "BRI": "Bari",
    "TRN": "Turin",
    "VRN": "Verona",
    "OLB": "Olbia",
    "CAG": "Cagliari",

    # Netherlands & Belgium
    "AMS": "Amsterdam",
    "RTM": "Rotterdam",
    "EIN": "Eindhoven",
    "BRU": "Brussels",
    "CRL": "Brussels Charleroi",
    "ANR": "Antwerp",

    # Switzerland & Austria
    "ZRH": "Zurich",
    "GVA": "Geneva",
    "BSL": "Basel",
    "VIE": "Vienna",
    "SZG": "Salzburg",
    "INN": "Innsbruck",
    "GRZ": "Graz",

    # Czech Republic & Slovakia
    "PRG": "Prague",
    "BRQ": "Brno",
    "BTS": "Bratislava",
    "KSC": "Kosice",

    # Scandinavia & Baltics
    "CPH": "Copenhagen",
    "ARN": "Stockholm",
    "NYO": "Stockholm Skavsta",
    "OSL": "Oslo",
    "TRF": "Oslo Torp",
    "HEL": "Helsinki",
    "BGO": "Bergen",
    "GOT": "Gothenburg",
    "RIX": "Riga",
    "TLL": "Tallinn",
    "VNO": "Vilnius",

    # Greece
    "ATH": "Athens",
    "SKG": "Thessaloniki",
    "HER": "Heraklion",
    "RHO": "Rhodes",
    "CFU": "Corfu",
    "CHQ": "Chania",
    "ZTH": "Zakynthos",
    "JMK": "Mykonos",
    "JTR": "Santorini",
    "KGS": "Kos",

    # Portugal
    "LIS": "Lisbon",
    "OPO": "Porto",
    "FAO": "Faro",
    "FNC": "Madeira",
    "PDL": "Ponta Delgada",

    # Balkans
    "SPU": "Split",
    "DBV": "Dubrovnik",
    "ZAD": "Zadar",
    "TIA": "Tirana",
    "LJU": "Ljubljana",
    "TGD": "Podgorica",
    "TIV": "Tivat",
    "SKP": "Skopje",
    "BEG": "Belgrade",
    "ZAG": "Zagreb",
    "SOF": "Sofia",
    "VAR": "Varna",
    "BOJ": "Burgas",
    "CLJ": "Cluj-Napoca",
    "IAS": "Iasi",

    # Eastern Europe
    "BUD": "Budapest",
    "OTP": "Bucharest",
    "KIV": "Chisinau",
    "LWO": "Lviv",
    "IEV": "Kyiv",
    "KBP": "Kyiv",
    "MSQ": "Minsk",

    # Egypt & Middle East
    "HRG": "Hurghada",
    "SSH": "Sharm El Sheikh",
    "RMF": "Marsa Alam",
    "CAI": "Cairo",
    "TLV": "Tel Aviv",
    "AMM": "Amman",
    "DXB": "Dubai",
    "DWC": "Dubai",
    "AUH": "Abu Dhabi",
    "DOH": "Doha",
    "IST": "Istanbul",
    "SAW": "Istanbul Sabiha Gokcen",
    "ADB": "Izmir",
    "AYT": "Antalya",
    "BJV": "Bodrum",
    "DLM": "Dalaman",
    "KWI": "Kuwait City",
    "BAH": "Bahrain",
    "MCT": "Muscat",

    # Cyprus & Malta
    "LCA": "Larnaca",
    "PFO": "Paphos",
    "MLA": "Malta",

    # Indian Ocean
    "MRU": "Mauritius",
    "RUN": "Reunion",
    "SEZ": "Seychelles",
    "TNR": "Antananarivo",
    "NOS": "Nosy Be",
    "DIE": "Antsiranana",
    "ZSE": "Saint-Pierre (Reunion)",
    "CMB": "Colombo",
    "MLE": "Malé",
    "MRV": "Marrakech",  # (for tourism from Poland often via charter)

    # Africa
    "RAK": "Marrakech",
    "CMN": "Casablanca",
    "AGA": "Agadir",
    "TUN": "Tunis",
    "DJE": "Djerba",
    "NBE": "Enfidha",
    "NBO": "Nairobi",
    "ZNZ": "Zanzibar",
    "MBA": "Mombasa",
    "DAR": "Dar es Salaam",
    "CPT": "Cape Town",
    "JNB": "Johannesburg",
    "ADD": "Addis Ababa",

    # Asia
    "BKK": "Bangkok",
    "HKT": "Phuket",
    "USM": "Koh Samui",
    "KUL": "Kuala Lumpur",
    "SIN": "Singapore",
    "DPS": "Bali",
    "CGK": "Jakarta",
    "HAN": "Hanoi",
    "SGN": "Ho Chi Minh City",
    "PNH": "Phnom Penh",
    "REP": "Siem Reap",
    "MLE": "Male",
    "HKG": "Hong Kong",
    "TPE": "Taipei",
    "ICN": "Seoul",
    "NRT": "Tokyo Narita",
    "HND": "Tokyo Haneda",
    "KIX": "Osaka",
    "BOM": "Mumbai",
    "DEL": "Delhi",
    "GOI": "Goa",
    "MLE": "Malé",
    "DXB": "Dubai",
    "DOH": "Doha",

    # Caribbean & Americas
    "PUJ": "Punta Cana",
    "SDQ": "Santo Domingo",
    "MBJ": "Montego Bay",
    "KIN": "Kingston",
    "HAV": "Havana",
    "VRA": "Varadero",
    "CUN": "Cancun",
    "SJO": "San Jose (Costa Rica)",
    "LIR": "Liberia (Costa Rica)",
    "PTP": "Pointe-à-Pitre (Guadeloupe)",
    "FDF": "Fort-de-France (Martinique)",
    "AUA": "Aruba",
    "CUR": "Curaçao",
    "BON": "Bonaire",
    "BGI": "Barbados",
    "UVF": "Saint Lucia",
    "GND": "Grenada",
    "TAB": "Tobago",
    "NAS": "Nassau",
    "EIS": "Tortola (BVI)",

    # USA & Canada (Major Hubs)
    "JFK": "New York",
    "EWR": "New York",
    "LGA": "New York",
    "LAX": "Los Angeles",
    "ORD": "Chicago",
    "ATL": "Atlanta",
    "DFW": "Dallas",
    "DEN": "Denver",
    "SFO": "San Francisco",
    "SEA": "Seattle",
    "MIA": "Miami",
    "LAS": "Las Vegas",
    "BOS": "Boston",
    "IAH": "Houston",
    "PHX": "Phoenix",
    "MCO": "Orlando",
    "YYZ": "Toronto",
    "YUL": "Montreal",
    "YVR": "Vancouver",
}

@lru_cache(maxsize=256)
def get_city_name(iata_code: str, use_api_fallback: bool = False) -> Optional[str]:
    """
    Get city name for an airport IATA code.
    
    Args:
        iata_code: 3-letter IATA airport code (e.g., "FRA", "POZ")
        use_api_fallback: If True and code not in static map, try API lookup
    
    Returns:
        City name string, or None if not found
    
    Examples:
        >>> get_city_name("FRA")
        "Frankfurt"
        >>> get_city_name("POZ")
        "Poznan"
    """
    if not iata_code or len(iata_code) != 3:
        return None
    
    iata_code = iata_code.upper()
    
    # Try static mapping first (fast)
    city = AIRPORT_CITY_MAP.get(iata_code)
    if city:
        return city
    
    # Optional: Try API fallback
    if use_api_fallback:
        try:
            from FlightRadar24.api import FlightRadar24API
            api = FlightRadar24API()
            airport = api.get_airport(iata_code, details=False)
            if hasattr(airport, 'city') and airport.city:
                # Cache the result in our static map for next time
                AIRPORT_CITY_MAP[iata_code] = airport.city
                return airport.city
        except Exception:
            # If API fails, just return None
            pass
    
    return None


def format_route(origin: str, destination: str, use_cities: bool = True, max_length: int = None) -> tuple:
    """
    Format a flight route for display.
    
    Args:
        origin: Origin IATA code
        destination: Destination IATA code
        use_cities: If True, use city names; if False, use IATA codes
        max_length: Maximum length for city names (truncate if longer)
    
    Returns:
        Tuple of (origin_display, destination_display)
    
    Examples:
        >>> format_route("FRA", "POZ", use_cities=True)
        ("Frankfurt", "Poznan")
        >>> format_route("FRA", "POZ", use_cities=False)
        ("FRA", "POZ")
        >>> format_route("FRA", "POZ", use_cities=True, max_length=4)
        ("Fran", "Pozn")
    """
    if not use_cities:
        return (origin, destination)
    
    origin_city = get_city_name(origin) or origin
    dest_city = get_city_name(destination) or destination
    
    if max_length:
        origin_city = origin_city[:max_length]
        dest_city = dest_city[:max_length]
    
    return (origin_city, dest_city)


if __name__ == "__main__":
    # Test the mapping
    test_codes = ["FRA", "POZ", "WAW", "LHR", "JFK", "XXX"]
    
    print("Testing airport code to city name mapping:")
    for code in test_codes:
        city = get_city_name(code)
        print(f"  {code} -> {city if city else 'Not found'}")
    
    print("\nTesting route formatting:")
    origin, dest = format_route("FRA", "POZ", use_cities=True)
    print(f"  FRA -> POZ: {origin} -> {dest}")
    
    origin, dest = format_route("FRA", "POZ", use_cities=True, max_length=4)
    print(f"  FRA -> POZ (max 4 chars): {origin} -> {dest}")

