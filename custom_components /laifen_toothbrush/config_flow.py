"""Config flow for Laifen Toothbrush integration."""
from __future__ import annotations

import logging
import voluptuous as vol
from typing import Any

from homeassistant import config_entries
from homeassistant.components import bluetooth
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("mac"): str,  # User must enter MAC address
    }
)

class LaifenToothbrushConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Laifen Toothbrush."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step for user configuration."""
        _LOGGER.debug("Starting Laifen Toothbrush config flow")

        # Check if Bluetooth is available in HA
        if not bluetooth.async_scanner_count(self.hass, connectable=False):
            _LOGGER.error("Bluetooth is not available on this system")
            return self.async_abort(reason="bluetooth_not_available")

        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=STEP_USER_DATA_SCHEMA
            )

        _LOGGER.info(f"User provided MAC address: {user_input['mac']}")

        return self.async_create_entry(title="Laifen Toothbrush", data=user_input)
