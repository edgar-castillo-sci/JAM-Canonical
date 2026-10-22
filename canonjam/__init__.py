"""Canonicalization of JAM strings for duplicate detection."""

from .canonical import (
    generate_group,
    canonical_key,
    canonical_key_fast,
    filter_duplicates,
    rot, transp, flip, sign,
    sort_cols,
    elements_S3,
    array_to_chain,
    chain_to_array,
)

__all__ = [
    "generate_group",
    "canonical_key",
    "canonical_key_fast",
    "filter_duplicates",
    "rot", "transp", "flip", "sign",
    "sort_cols",
    "elements_S3",
    "array_to_chain",
    "chain_to_array",
]

__version__ = "1.1.0"
