from rgbmatrix import graphics

from utilities.animator import Animator
from utilities.airports import get_city_name
from setup import colours, fonts, screen

# Setup
PLANE_DETAILS_COLOUR = colours.PINK
PLANE_DISTANCE_FROM_TOP = 30
PLANE_TEXT_HEIGHT = 9
PLANE_FONT = fonts.regular

# Configuration for route display
try:
    from config import PLANE_DETAILS_SHOW_ROUTE
except (ModuleNotFoundError, NameError, ImportError):
    PLANE_DETAILS_SHOW_ROUTE = True  # Show city route by default

try:
    from config import PLANE_DETAILS_ROUTE_SEPARATOR
except (ModuleNotFoundError, NameError, ImportError):
    PLANE_DETAILS_ROUTE_SEPARATOR = " > "  # Separator between cities (e.g., "Frankfurt > Poznan")


class PlaneDetailsScene(object):
    def __init__(self):
        super().__init__()
        self.plane_position = screen.WIDTH
        self._data_all_looped = False

    @Animator.KeyFrame.add(1)
    def plane_details(self, count):

        # Guard against no data
        if len(self._data) == 0:
            return

        # Build display text
        plane = f'{self._data[self._data_index]["plane"]}'
        
        # Add route information if enabled
        if PLANE_DETAILS_SHOW_ROUTE:
            origin = self._data[self._data_index]["origin"]
            destination = self._data[self._data_index]["destination"]
            
            # Get city names
            origin_city = get_city_name(origin) or origin
            dest_city = get_city_name(destination) or destination
            
            # Build route string with configurable separator
            if origin_city and dest_city:
                route = f" - {origin_city}{PLANE_DETAILS_ROUTE_SEPARATOR}{dest_city}"
            elif origin_city or dest_city:
                route = f" - {origin_city or dest_city}"
            else:
                route = ""
            
            # Combine plane and route
            display_text = plane + route
        else:
            display_text = plane

        # Draw background
        self.draw_square(
            0,
            PLANE_DISTANCE_FROM_TOP - PLANE_TEXT_HEIGHT,
            screen.WIDTH,
            screen.HEIGHT,
            colours.BLACK,
        )

        # Draw text
        text_length = graphics.DrawText(
            self.canvas,
            PLANE_FONT,
            self.plane_position,
            PLANE_DISTANCE_FROM_TOP,
            PLANE_DETAILS_COLOUR,
            display_text,
        )

        # Handle scrolling
        self.plane_position -= 1
        if self.plane_position + text_length < 0:
            self.plane_position = screen.WIDTH
            if len(self._data) > 1:
                self._data_index = (self._data_index + 1) % len(self._data)
                self._data_all_looped = (not self._data_index) or self._data_all_looped
                self.reset_scene()

    @Animator.KeyFrame.add(0)
    def reset_scrolling(self):
        self.plane_position = screen.WIDTH
