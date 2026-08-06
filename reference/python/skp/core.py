from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

_TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
_REQUIRED = {"skp","id","profile","semantic_address","action","subject","reach","provenance","extensions"}

@dataclass
class SkpError(ValueError):
    code: str
    message: str

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"

def _is_uri(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    p = urlparse(value)
    return bool(p.scheme)

def _entity(value: Any, name: str) -> None:
    if not isinstance(value, dict):
        raise SkpError("SKP_INVALID_ENTITY", f"{name} must be an object")
    if not _is_uri(value.get("id")) or not isinstance(value.get("type"), str) or not value["type"]:
        raise SkpError("SKP_INVALID_ENTITY", f"{name} requires URI id and non-empty type")

def validate_packet(packet: Any) -> None:
    if not isinstance(packet, dict):
        raise SkpError("SKP_REQUIRED_FIELD", "packet must be an object")
    missing = sorted(_REQUIRED - packet.keys())
    if missing:
        raise SkpError("SKP_REQUIRED_FIELD", f"missing: {', '.join(missing)}")
    if packet["skp"] != "1.0-draft":
        raise SkpError("SKP_UNSUPPORTED_VERSION", str(packet["skp"]))
    for field in ("id","profile"):
        if not _is_uri(packet[field]):
            raise SkpError("SKP_INVALID_URI", field)

    address = packet["semantic_address"]
    if not isinstance(address, dict) or not isinstance(address.get("space"), str) or not address["space"]:
        raise SkpError("SKP_INVALID_ADDRESS", "space")
    coordinates = address.get("coordinates")
    if not isinstance(coordinates, list) or not coordinates or not all(isinstance(x, str) for x in coordinates):
        raise SkpError("SKP_INVALID_ADDRESS", "coordinates")

    if not isinstance(packet["action"], str) or not packet["action"]:
        raise SkpError("SKP_PROFILE_VIOLATION", "action")
    _entity(packet["subject"], "subject")
    if "object" in packet:
        _entity(packet["object"], "object")

    if "transition" in packet:
        t = packet["transition"]
        if not isinstance(t, dict) or ("from" not in t and "to" not in t):
            raise SkpError("SKP_INVALID_TRANSITION", "transition requires from or to")

    if "payload" in packet:
        p = packet["payload"]
        if not isinstance(p, dict) or not isinstance(p.get("media_type"), str):
            raise SkpError("SKP_INVALID_PAYLOAD", "payload")
        if ("value" in p) == ("ref" in p):
            raise SkpError("SKP_INVALID_PAYLOAD", "exactly one of value or ref is required")
        if "ref" in p and not _is_uri(p["ref"]):
            raise SkpError("SKP_INVALID_URI", "payload.ref")

    prov = packet["provenance"]
    if not isinstance(prov, dict) or not _is_uri(prov.get("producer")) or not _TIMESTAMP.match(str(prov.get("created_at",""))):
        raise SkpError("SKP_INVALID_PROVENANCE", "provenance")

    if not isinstance(packet["extensions"], dict):
        raise SkpError("SKP_INVALID_EXTENSIONS", "extensions")

def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
