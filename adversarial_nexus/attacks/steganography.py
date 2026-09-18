"""
Adversarial Token Steganography & Zero-Width Obfuscation Tester.
Tests whether tokenizers and input guardrails detect instruction payloads hidden via Unicode zero-width characters.
"""
class ZeroWidthSteganography:
    ZERO_WIDTH_SPACE = "\u200B"
    ZERO_WIDTH_NON_JOINER = "\u200C"

    @classmethod
    def encode(cls, secret_text: str) -> str:
        """Encodes ASCII text into binary zero-width sequence."""
        binary = "".join(f"{ord(c):08b}" for c in secret_text)
        return "".join(cls.ZERO_WIDTH_SPACE if b == '0' else cls.ZERO_WIDTH_NON_JOINER for b in binary)

    @classmethod
    def decode(cls, encoded_text: str) -> str:
        """Decodes zero-width binary sequence back into text."""
        bits = []
        for ch in encoded_text:
            if ch == cls.ZERO_WIDTH_SPACE:
                bits.append('0')
            elif ch == cls.ZERO_WIDTH_NON_JOINER:
                bits.append('1')
        
        bit_str = "".join(bits)
        chars = []
        for i in range(0, len(bit_str), 8):
            byte = bit_str[i:i+8]
            if len(byte) == 8:
                chars.append(chr(int(byte, 2)))
        return "".join(chars)
