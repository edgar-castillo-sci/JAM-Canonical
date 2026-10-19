"""Canonicalization of JAM strings for duplicate detection."""

from .canonical import (
    generate_group,
    canonical_key,
    filter_duplicates,
    rot, transp, flip, sign,
    elements_S3,
    array_to_chain,
    chain_to_array,
)

__all__ = [
    "generate_group",
    "canonical_key",
    "filter_duplicates",
    "rot", "transp", "flip", "sign",
    "elements_S3",
    "array_to_chain",
    "chain_to_array",
]

__version__ = "1.0.0"
