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


class FactionPositionAbilityEnum(str, Enum):
    """
    FactionPositionAbilityEnum
    """

    """
    allowed enum values
    """
    MEDICAL_ITEM_USAGE = 'Medical Item Usage'
    BOOSTER_ITEM_USAGE = 'Booster Item Usage'
    DRUG_ITEM_USAGE = 'Drug Item Usage'
    ENERGY_REFILL_USAGE = 'Energy Refill Usage'
    NERVE_REFILL_USAGE = 'Nerve Refill Usage'
    TEMPORARY_ITEM_LOANING = 'Temporary Item Loaning'
    WEAPON_AMPERSAND__ARMOR_LOANING = 'Weapon & Armor Loaning'
    ITEM_RETRIEVING = 'Item Retrieving'
    ORGANISED_CRIMES = 'Organised Crimes'
    FACTION_API_ACCESS = 'Faction API Access'
    ITEM_GIVING = 'Item Giving'
    MONEY_GIVING = 'Money Giving'
    POINTS_GIVING = 'Points Giving'
    FORUM_MANAGEMENT = 'Forum Management'
    APPLICATION_MANAGEMENT = 'Application Management'
    KICK_MEMBERS = 'Kick Members'
    BALANCE_ADJUSTMENT = 'Balance Adjustment'
    WAR_MANAGEMENT = 'War Management'
    UPGRADE_MANAGEMENT = 'Upgrade Management'
    NEWSLETTER_SENDING = 'Newsletter Sending'
    ANNOUNCEMENT_CHANGES = 'Announcement Changes'
    DESCRIPTION_CHANGES = 'Description Changes'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FactionPositionAbilityEnum from a JSON string"""
        return cls(json.loads(json_str))


