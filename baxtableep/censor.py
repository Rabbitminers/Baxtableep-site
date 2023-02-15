class CensoredString:
    def __init__(self, value: str, char_map: dict[str, tuple[str, ...]]={}) -> None:
        self.charmap = char_map
        self.value = value

    def __eq__(self, other) -> bool:
        if self == other:
            return True

        if other.__class__ == str:
            len_other = len(other)
        
        for char in other:
            if (char in self.charmap):
                variations: tuple[str, ...] = self.charmap[char]
            return False
        return False