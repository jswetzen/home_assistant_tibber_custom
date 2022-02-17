"""Tibber lowest price at night"""
import logging

from homeassistant.const import EVENT_HOMEASSISTANT_START
from homeassistant.helpers import discovery


DOMAIN = "tibber_night_price"

DEPENDENCIES = ["tibber"]

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    """Setup component."""

    def ha_started(_):
        discovery.load_platform(hass, "camera", DOMAIN, {}, config)

    hass.bus.listen_once(EVENT_HOMEASSISTANT_START, ha_started)

    return True
