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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.faction_chain_warfare import FactionChainWarfare
from openapi_client.models.faction_raid_warfare import FactionRaidWarfare
from openapi_client.models.faction_ranked_war_details import FactionRankedWarDetails
from openapi_client.models.faction_territory_warfare import FactionTerritoryWarfare
from openapi_client.models.faction_warfare_dirty_bomb import FactionWarfareDirtyBomb
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

FACTIONWARFARERESPONSEWARFARE_ONE_OF_SCHEMAS = ["List[FactionChainWarfare]", "List[FactionRaidWarfare]", "List[FactionRankedWarDetails]", "List[FactionTerritoryWarfare]", "List[FactionWarfareDirtyBomb]"]

class FactionWarfareResponseWarfare(BaseModel):
    """
    FactionWarfareResponseWarfare
    """
    # data type: List[FactionRankedWarDetails]
    oneof_schema_1_validator: Optional[List[FactionRankedWarDetails]] = None
    # data type: List[FactionTerritoryWarfare]
    oneof_schema_2_validator: Optional[List[FactionTerritoryWarfare]] = None
    # data type: List[FactionChainWarfare]
    oneof_schema_3_validator: Optional[List[FactionChainWarfare]] = None
    # data type: List[FactionRaidWarfare]
    oneof_schema_4_validator: Optional[List[FactionRaidWarfare]] = None
    # data type: List[FactionWarfareDirtyBomb]
    oneof_schema_5_validator: Optional[List[FactionWarfareDirtyBomb]] = None
    actual_instance: Optional[Union[List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]]] = None
    one_of_schemas: Set[str] = { "List[FactionChainWarfare]", "List[FactionRaidWarfare]", "List[FactionRankedWarDetails]", "List[FactionTerritoryWarfare]", "List[FactionWarfareDirtyBomb]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = FactionWarfareResponseWarfare.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[FactionRankedWarDetails]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[FactionTerritoryWarfare]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[FactionChainWarfare]
        try:
            instance.oneof_schema_3_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[FactionRaidWarfare]
        try:
            instance.oneof_schema_4_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[FactionWarfareDirtyBomb]
        try:
            instance.oneof_schema_5_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FactionWarfareResponseWarfare with oneOf schemas: List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FactionWarfareResponseWarfare with oneOf schemas: List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into List[FactionRankedWarDetails]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[FactionTerritoryWarfare]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[FactionChainWarfare]
        try:
            # validation
            instance.oneof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_3_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[FactionRaidWarfare]
        try:
            # validation
            instance.oneof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_4_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[FactionWarfareDirtyBomb]
        try:
            # validation
            instance.oneof_schema_5_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_5_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FactionWarfareResponseWarfare with oneOf schemas: List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FactionWarfareResponseWarfare with oneOf schemas: List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[FactionChainWarfare], List[FactionRaidWarfare], List[FactionRankedWarDetails], List[FactionTerritoryWarfare], List[FactionWarfareDirtyBomb]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


