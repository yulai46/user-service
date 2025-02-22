from dataclasses import dataclass
import sys
from typing import Tuple
from pydantic import BaseModel, root_validator

SECRET_KEY_LENGTH = 16


class Settings(BaseModel):
    """
    Store settings values
    """
    MONGODB_URL: str
    SECRET_KEY: str
    TOKEN_EXPIRED: int # token expired time in minutes

    @root_validator
    def validate(cls, values):
        if values.get('TOKEN_EXPIRED') <= 0:
            raise ValueError('TOKEN_EXPIRED(in minutes) must be greater than 0')
        if len(values.get('SECRET_KEY')) < SECRET_KEY_LENGTH:
            raise ValueError(f'SECRET_KEY len must be greater than {SECRET_KEY_LENGTH}')
        return values