# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RaceCarUpgradeSubCategory(str, Enum):
    """
    RaceCarUpgradeSubCategory
    """

    """
    allowed enum values
    """
    ENGINE_COOLING = 'Engine Cooling'
    FRONT_DIFFUSER = 'Front Diffuser'
    REAR_DIFFUSER = 'Rear Diffuser'
    SPOILER = 'Spoiler'
    BRAKE_ACCESSORY = 'Brake Accessory'
    BRAKE_CONTROL = 'Brake Control'
    CALLIPERS = 'Callipers'
    DISCS = 'Discs'
    BRAKE_COOLING = 'Brake Cooling'
    FLUID = 'Fluid'
    REAR_CONTROL_ARMS = 'Rear Control Arms'
    SPRINGS = 'Springs'
    UPPER_FRONT_BRACE = 'Upper Front Brace'
    CLUTCH = 'Clutch'
    DIFFERENTIAL = 'Differential'
    FLYWHEEL = 'Flywheel'
    GEARBOX = 'Gearbox'
    SHIFTING = 'Shifting'
    BOOT = 'Boot'
    HOOD = 'Hood'
    INTERIOR = 'Interior'
    ROOF = 'Roof'
    STEERING_WHEEL = 'Steering wheel'
    STRIP_OUT = 'Strip out'
    WINDOWS = 'Windows'
    TYRES = 'Tyres'
    WHEELS = 'Wheels'
    REAR_BUSHES = 'Rear Bushes'
    REAR_BRACE = 'Rear Brace'
    LOWER_FRONT_BRACE = 'Lower Front Brace'
    FRONT_TIE_RODS = 'Front Tie Rods'
    FRONT_BUSHES = 'Front Bushes'
    SEAT = 'Seat'
    SAFETY_ACCESSORY = 'Safety Accessory'
    ROLL_CAGE = 'Roll cage'
    OVERALLS = 'Overalls'
    HELMET = 'Helmet'
    FIRE_EXTINGUISHER = 'Fire Extinguisher'
    CUT_MINUS_OFF = 'Cut-off'
    FUEL = 'Fuel'
    MANIFOLD = 'Manifold'
    EXHAUST = 'Exhaust'
    AIR_FILTER = 'Air Filter'
    TURBO = 'Turbo'
    PISTONS = 'Pistons'
    INTERCOOLER = 'Intercooler'
    GASKET = 'Gasket'
    FUEL_PUMP = 'Fuel Pump'
    ENGINE_PORTING = 'Engine Porting'
    ENGINE_CLEANING = 'Engine Cleaning'
    COMPUTER = 'Computer'
    CAMSHAFT = 'Camshaft'
    PADS = 'Pads'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RaceCarUpgradeSubCategory from a JSON string"""
        return cls(json.loads(json_str))


