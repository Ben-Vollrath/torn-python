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
from openapi_client.models.personal_stats_category_enum import PersonalStatsCategoryEnum
from openapi_client.models.racing_race_type_enum import RacingRaceTypeEnum
from openapi_client.models.report_type_enum import ReportTypeEnum
from openapi_client.models.user_list_enum import UserListEnum
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SELECTIONCATEGORYENUM_ONE_OF_SCHEMAS = ["PersonalStatsCategoryEnum", "RacingRaceTypeEnum", "ReportTypeEnum", "UserListEnum"]

class SelectionCategoryEnum(BaseModel):
    """
    SelectionCategoryEnum
    """
    # data type: ReportTypeEnum
    oneof_schema_1_validator: Optional[ReportTypeEnum] = None
    # data type: UserListEnum
    oneof_schema_2_validator: Optional[UserListEnum] = None
    # data type: PersonalStatsCategoryEnum
    oneof_schema_3_validator: Optional[PersonalStatsCategoryEnum] = None
    # data type: RacingRaceTypeEnum
    oneof_schema_4_validator: Optional[RacingRaceTypeEnum] = None
    actual_instance: Optional[Union[PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum]] = None
    one_of_schemas: Set[str] = { "PersonalStatsCategoryEnum", "RacingRaceTypeEnum", "ReportTypeEnum", "UserListEnum" }

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
        instance = SelectionCategoryEnum.model_construct()
        error_messages = []
        match = 0
        # validate data type: ReportTypeEnum
        if not isinstance(v, ReportTypeEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReportTypeEnum`")
        else:
            match += 1
        # validate data type: UserListEnum
        if not isinstance(v, UserListEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserListEnum`")
        else:
            match += 1
        # validate data type: PersonalStatsCategoryEnum
        if not isinstance(v, PersonalStatsCategoryEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PersonalStatsCategoryEnum`")
        else:
            match += 1
        # validate data type: RacingRaceTypeEnum
        if not isinstance(v, RacingRaceTypeEnum):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RacingRaceTypeEnum`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SelectionCategoryEnum with oneOf schemas: PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SelectionCategoryEnum with oneOf schemas: PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum. Details: " + ", ".join(error_messages))
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

        # deserialize data into ReportTypeEnum
        try:
            instance.actual_instance = ReportTypeEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserListEnum
        try:
            instance.actual_instance = UserListEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PersonalStatsCategoryEnum
        try:
            instance.actual_instance = PersonalStatsCategoryEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RacingRaceTypeEnum
        try:
            instance.actual_instance = RacingRaceTypeEnum.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SelectionCategoryEnum with oneOf schemas: PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SelectionCategoryEnum with oneOf schemas: PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], PersonalStatsCategoryEnum, RacingRaceTypeEnum, ReportTypeEnum, UserListEnum]]:
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


