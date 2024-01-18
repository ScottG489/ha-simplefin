"""Platform for sensor integration."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from simplefin4py import Account

from homeassistant.components.sensor import SensorEntity, SensorStateClass, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SimpleFinDataUpdateCoordinator
from homeassistant.helpers.entity import EntityDescription


# Usually they ask for soemthing like this
#
# SIMPLEFIN_SENSORS: tuple[SensorEntityDescription, ...] = (
#     SensorEntityDescription(
#         key="balance",
#         translation_key="balance",
#         icon="mid:LOTS_OF_MONEY",
#         state_class=SensorStateClass.MEASUREMENT,
#         value_fn = labmda x: x
#     ),
#     SensorEntityDescription(
#         key="last_update",
#         translation_key="last_update",        
#         value_fn = labmda x: x
#     ),
#     )









class SimpleFinBalanceSensor(
    CoordinatorEntity[SimpleFinDataUpdateCoordinator], SensorEntity
):
    """Representation of a SimpleFinBalanceSensor."""

    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_has_entity_name = True

    def __init__(
        self,
        account,
        coordinator: SimpleFinDataUpdateCoordinator,
    ) -> None:
        """Initialize sensor."""
        super().__init__(coordinator)
        self.account_id = account.id
        self._attr_unique_id = f"account_{account.id}".lower()
        self._attr_name = account.name

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, account.org.domain)},
            name=account.org.name,
            entry_type=DeviceEntryType.SERVICE,
            manufacturer="SimpleFIN",
            model="Account",
        )

    @property
    def available(self) -> bool:
        """Determine if sensor is available."""
        return True

    @property
    def native_value(self) -> int | None:
        """Return the account balance."""
        return next(
            account.balance
            for account in self.coordinator.data.accounts
            if account.id == self.account_id
        )

    @property
    def icon(self) -> str | None:
        return next(
            account.inferred_account_type.value
            for account in self.coordinator.data.accounts
            if account.id == self.account_id
        )

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SimpleFIN sensors for config entries."""
    simplefin_coordinator: SimpleFinDataUpdateCoordinator = hass.data[DOMAIN][
        config_entry.entry_id
    ]
    accounts = simplefin_coordinator.data.accounts

    async_add_entities(
        [
            SimpleFinBalanceSensor(account, simplefin_coordinator)
            for account in accounts
        ],
        True,
    )
