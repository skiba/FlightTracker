from utilities.animator import Animator
from utilities.airports import get_city_name
from setup import colours, fonts

from rgbmatrix import graphics

# Attempt to load config data
try:
    from config import JOURNEY_CODE_SELECTED

except (ModuleNotFoundError, NameError, ImportError):
    # If there's no config data
    JOURNEY_CODE_SELECTED = "GLA"

try:
    from config import JOURNEY_BLANK_FILLER

except (ModuleNotFoundError, NameError, ImportError):
    # If there's no config data
    JOURNEY_BLANK_FILLER = " ? "

try:
    from config import JOURNEY_USE_CITY_NAMES

except (ModuleNotFoundError, NameError, ImportError):
    # If there's no config data
    JOURNEY_USE_CITY_NAMES = False

try:
    from config import JOURNEY_CITY_MAX_LENGTH

except (ModuleNotFoundError, NameError, ImportError):
    # Default max length for city names (to fit on display)
    JOURNEY_CITY_MAX_LENGTH = 8

# Setup
JOURNEY_POSITION = (0, 0)
JOURNEY_HEIGHT = 12
JOURNEY_WIDTH = 64
JOURNEY_SPACING = 16
JOURNEY_FONT = fonts.large
JOURNEY_FONT_SELECTED = fonts.large_bold
JOURNEY_COLOUR = colours.YELLOW

ARROW_COLOUR = colours.ORANGE

# Element Positions
ARROW_POINT_POSITION = (34, 7)
ARROW_WIDTH = 4
ARROW_HEIGHT = 8


class JourneyScene(object):
    def __init__(self):
        super().__init__()

    @Animator.KeyFrame.add(0)
    def journey(self):
        # Guard against no data
        if len(self._data) == 0:
            return

        origin = self._data[self._data_index]["origin"]
        destination = self._data[self._data_index]["destination"]

        # Convert to city names if enabled
        if JOURNEY_USE_CITY_NAMES:
            origin_display = get_city_name(origin) or origin
            dest_display = get_city_name(destination) or destination
            
            # Truncate if too long
            if JOURNEY_CITY_MAX_LENGTH:
                origin_display = origin_display[:JOURNEY_CITY_MAX_LENGTH]
                dest_display = dest_display[:JOURNEY_CITY_MAX_LENGTH]
        else:
            origin_display = origin
            dest_display = destination

        # Draw background
        self.draw_square(
            JOURNEY_POSITION[0],
            JOURNEY_POSITION[1],
            JOURNEY_POSITION[0] + JOURNEY_WIDTH - 1,
            JOURNEY_POSITION[1] + JOURNEY_HEIGHT - 1,
            colours.BLACK,
        )

        # Draw origin
        text_length = graphics.DrawText(
            self.canvas,
            JOURNEY_FONT_SELECTED if origin == JOURNEY_CODE_SELECTED else JOURNEY_FONT,
            1,
            JOURNEY_HEIGHT,
            JOURNEY_COLOUR,
            origin_display if origin_display else JOURNEY_BLANK_FILLER,
        )

        # Draw destination
        _ = graphics.DrawText(
            self.canvas,
            JOURNEY_FONT_SELECTED
            if destination == JOURNEY_CODE_SELECTED
            else JOURNEY_FONT,
            text_length + JOURNEY_SPACING,
            JOURNEY_HEIGHT,
            JOURNEY_COLOUR,
            dest_display if dest_display else JOURNEY_BLANK_FILLER,
        )

    @Animator.KeyFrame.add(0)
    def journey_arrow(self):
        # Guard against no data
        if len(self._data) == 0:
            return

        # Black area before arrow
        self.draw_square(
            ARROW_POINT_POSITION[0] - ARROW_WIDTH,
            ARROW_POINT_POSITION[1] - (ARROW_HEIGHT // 2),
            ARROW_POINT_POSITION[0],
            ARROW_POINT_POSITION[1] + (ARROW_HEIGHT // 2),
            colours.BLACK,
        )

        # Starting positions for filled in arrow
        x = ARROW_POINT_POSITION[0] - ARROW_WIDTH
        y1 = ARROW_POINT_POSITION[1] - (ARROW_HEIGHT // 2)
        y2 = ARROW_POINT_POSITION[1] + (ARROW_HEIGHT // 2)

        # Tip of arrow
        self.canvas.SetPixel(
            ARROW_POINT_POSITION[0],
            ARROW_POINT_POSITION[1],
            ARROW_COLOUR.red,
            ARROW_COLOUR.green,
            ARROW_COLOUR.blue,
        )

        # Draw using columns
        for col in range(0, ARROW_WIDTH):
            graphics.DrawLine(
                self.canvas,
                x,
                y1,
                x,
                y2,
                ARROW_COLOUR,
            )

            # Calculate next column's data
            x += 1
            y1 += 1
            y2 -= 1
