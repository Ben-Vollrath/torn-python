# coding: utf-8

"""
    Torn API

      * The development of Torn's API v2 is still ongoing.  * If selections remain unaltered, they will default to the API v1 version.  * Unlike API v1, API v2 accepts both selections and IDs as path and query parameters.  * If any discrepancies or errors are found, please submit a [bug report](https://www.torn.com/forums.php#/p=forums&f=19&b=0&a=0) on the Torn Forums.  * In case you're using bots to check for changes on openapi.json file, make sure to specificy a custom user-agent header - CloudFlare sometimes prevents requests from default user-agents.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.hof_value import HofValue
from openapi_client.models.hof_value_float import HofValueFloat
from typing import Optional, Set
from typing_extensions import Self

class UserHofStats(BaseModel):
    """
    UserHofStats
    """ # noqa: E501
    attacks: HofValue
    busts: HofValue
    defends: HofValue
    networth: HofValue
    offences: HofValue
    revives: HofValue
    level: HofValue
    rank: HofValue
    awards: HofValue
    racing_skill: HofValueFloat
    racing_points: HofValue
    racing_wins: HofValue
    travel_time: HofValue
    working_stats: HofValue
    battle_stats: Optional[HofValue] = Field(description="This field is null when requesting data for other players.")
    __properties: ClassVar[List[str]] = ["attacks", "busts", "defends", "networth", "offences", "revives", "level", "rank", "awards", "racing_skill", "racing_points", "racing_wins", "travel_time", "working_stats", "battle_stats"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserHofStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of attacks
        if self.attacks:
            _dict['attacks'] = self.attacks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of busts
        if self.busts:
            _dict['busts'] = self.busts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of defends
        if self.defends:
            _dict['defends'] = self.defends.to_dict()
        # override the default output from pydantic by calling `to_dict()` of networth
        if self.networth:
            _dict['networth'] = self.networth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offences
        if self.offences:
            _dict['offences'] = self.offences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revives
        if self.revives:
            _dict['revives'] = self.revives.to_dict()
        # override the default output from pydantic by calling `to_dict()` of level
        if self.level:
            _dict['level'] = self.level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rank
        if self.rank:
            _dict['rank'] = self.rank.to_dict()
        # override the default output from pydantic by calling `to_dict()` of awards
        if self.awards:
            _dict['awards'] = self.awards.to_dict()
        # override the default output from pydantic by calling `to_dict()` of racing_skill
        if self.racing_skill:
            _dict['racing_skill'] = self.racing_skill.to_dict()
        # override the default output from pydantic by calling `to_dict()` of racing_points
        if self.racing_points:
            _dict['racing_points'] = self.racing_points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of racing_wins
        if self.racing_wins:
            _dict['racing_wins'] = self.racing_wins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of travel_time
        if self.travel_time:
            _dict['travel_time'] = self.travel_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of working_stats
        if self.working_stats:
            _dict['working_stats'] = self.working_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of battle_stats
        if self.battle_stats:
            _dict['battle_stats'] = self.battle_stats.to_dict()
        # set to None if battle_stats (nullable) is None
        # and model_fields_set contains the field
        if self.battle_stats is None and "battle_stats" in self.model_fields_set:
            _dict['battle_stats'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserHofStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attacks": HofValue.from_dict(obj["attacks"]) if obj.get("attacks") is not None else None,
            "busts": HofValue.from_dict(obj["busts"]) if obj.get("busts") is not None else None,
            "defends": HofValue.from_dict(obj["defends"]) if obj.get("defends") is not None else None,
            "networth": HofValue.from_dict(obj["networth"]) if obj.get("networth") is not None else None,
            "offences": HofValue.from_dict(obj["offences"]) if obj.get("offences") is not None else None,
            "revives": HofValue.from_dict(obj["revives"]) if obj.get("revives") is not None else None,
            "level": HofValue.from_dict(obj["level"]) if obj.get("level") is not None else None,
            "rank": HofValue.from_dict(obj["rank"]) if obj.get("rank") is not None else None,
            "awards": HofValue.from_dict(obj["awards"]) if obj.get("awards") is not None else None,
            "racing_skill": HofValueFloat.from_dict(obj["racing_skill"]) if obj.get("racing_skill") is not None else None,
            "racing_points": HofValue.from_dict(obj["racing_points"]) if obj.get("racing_points") is not None else None,
            "racing_wins": HofValue.from_dict(obj["racing_wins"]) if obj.get("racing_wins") is not None else None,
            "travel_time": HofValue.from_dict(obj["travel_time"]) if obj.get("travel_time") is not None else None,
            "working_stats": HofValue.from_dict(obj["working_stats"]) if obj.get("working_stats") is not None else None,
            "battle_stats": HofValue.from_dict(obj["battle_stats"]) if obj.get("battle_stats") is not None else None
        })
        return _obj


