"""ICAO aircraft type-code -> human-readable name lookup.

Replaces the FR24 get_flight_details() aircraft model field, which returns 403
since FR24 locked down the clickhandler endpoint. Data comes from a static CSV
(rikgale/ICAOList) bundled in assets/icao_types.csv.
"""

import csv
import os

_TYPES = {}

_CSV_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "icao_types.csv")
)


def _format(manufacturer_model):
    # CSV stores e.g. 'BOEING, 737-800'. Title-case the manufacturer, keep model verbatim.
    if "," in manufacturer_model:
        mfr, _, model = manufacturer_model.partition(",")
        return f"{mfr.strip().title()} {model.strip()}".strip()
    return manufacturer_model.strip()


def _load():
    try:
        with open(_CSV_PATH, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # header
            for row in reader:
                if len(row) < 4:
                    continue
                code = row[0].strip().upper()
                if code:
                    _TYPES[code] = _format(row[3])
    except (FileNotFoundError, OSError):
        pass


_load()


def lookup(code):
    if not code:
        return ""
    return _TYPES.get(code.strip().upper(), "")
