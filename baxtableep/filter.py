class Filter:
    def __init__(self, words=None) -> None:
        self.char_swaps: dict[str, tuple[str, ...]] = {
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

        self.default_wordlist_filename: str = "data/wordlist.txt"
        self.wordlist: list[str] = []

    def censor_text(self, text: str, char: str ='#') -> str:
        return ""

    def is_offensive(self, text: str) -> bool:
        return self.censor_text(text) != text

    def _populate_wordlist(self):
        pass
        
    def _generate_variations(self, text: str) -> list[str]:
        return ['']