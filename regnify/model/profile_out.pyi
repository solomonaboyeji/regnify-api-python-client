# coding: utf-8

"""
    REGNIFY HTTP API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: admin@regnify.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from regnify import schemas  # noqa: F401


class ProfileOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "avatar_url",
            "last_name",
            "first_name",
        }
        
        class properties:
            
            
            class last_name(
                schemas.StrSchema
            ):
                pass
            
            
            class first_name(
                schemas.StrSchema
            ):
                pass
            avatar_url = schemas.StrSchema
            __annotations__ = {
                "last_name": last_name,
                "first_name": first_name,
                "avatar_url": avatar_url,
            }
    
    avatar_url: MetaOapg.properties.avatar_url
    last_name: MetaOapg.properties.last_name
    first_name: MetaOapg.properties.first_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["last_name", "first_name", "avatar_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["last_name", "first_name", "avatar_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        avatar_url: typing.Union[MetaOapg.properties.avatar_url, str, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileOut':
        return super().__new__(
            cls,
            *_args,
            avatar_url=avatar_url,
            last_name=last_name,
            first_name=first_name,
            _configuration=_configuration,
            **kwargs,
        )
