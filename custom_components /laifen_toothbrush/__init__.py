"""Laifen Toothbrush integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Laifen Toothbrush from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    return True
