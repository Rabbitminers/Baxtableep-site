
from censor import CensoredString

def find_swapped_match(test: str, other: str, char_swaps: dict) -> bool:
    swap_chars = set(c for c in other if c in char_swaps)
    for c in swap_chars:
        for swap in char_swaps[c]:
            s2_swap = other.replace(c, swap)
            if s2_swap == test:
                return True
    return False

if __name__ == '__main__':
    char_swaps: dict[str, tuple[str, ...]] = {
        "a": ("a", "@", "*", "4"),
        "i": ("i", "*", "l", "1"),
        "o": ("o", "*", "0", "@"),
        "u": ("u", "*", "v"),
        "v": ("v", "*", "u"),
        "l": ("l", "1", "|"),
        "e": ("e", "*", "3"),
        "s": ("s", "$", "5"),
        "t": ("t", "7", "+"),
    }

    test = "H3llo world"
    other = "Hello world"

    for c in other:
        if c in char_swaps:
            for swap in char_swaps[c]:
                s2_swap = other.replace(c, swap)
                if s2_swap == test:
                    print("Found!")

    print(find_swapped_match("He11o world", "Hello world", char_swaps))

    value: CensoredString = CensoredString("Hello world!", char_map=char_swaps)