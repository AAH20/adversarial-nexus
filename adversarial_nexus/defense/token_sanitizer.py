"""
Adversarial Token Sanitizer & Zero-Width Stripper.
Neutralizes steganographic payloads and instruction tags before LLM tokenization.
"""
import re

class InputSanitizer:
    ZERO_WIDTH_PATTERN = re.compile(r"[\u200B-\u200D\uFEFF]")
    INDIRECT_TAG_PATTERN = re.compile(r"\[SYSTEM NOTE:.*?\]", re.IGNORECASE)

    @classmethod
    def sanitize(cls, raw_input: str) -> str:
        # Strip zero-width hidden characters
        cleaned = cls.ZERO_WIDTH_PATTERN.sub("", raw_input)
        # Neutralize spoofed system notes
        cleaned = cls.INDIRECT_TAG_PATTERN.sub("[SANITIZED_USER_INPUT]", cleaned)
        return cleaned
