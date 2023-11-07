

class Color:
    def __init__(self):
        self._white = "#fff;"
        self._white_milky = "#E3DEE2"
        self._gray_shade_magenta = "#B0AEB1;"
        self._gray = "#36393f;"
        self._light_gray = "#a5a6a5;"
        self._dark_gray = "rgb(39, 44, 54)"
        self._aluminium = "#8e9297;"
        self._gradient_gray = "#66676f;"

    def __str__(self):
        return (f"Colors({self._white}, {self._white_milky}, {self._gray_shade_magenta} {self._gray}, {self._light_gray},"
                f" {self._dark_gray}, {self._aluminium}, {self._gradient_gray})")

    def __repr__(self):
        return (f"white: {self._white}, white milky: {self._white_milky}, gray shade of magenta: {self._gray_shade_magenta}."
                f"gray: {self._gray}, light gray: {self._light_gray}, dark gray: {self._dark_gray}, aluminium: {self._aluminium},"
                f"gray gradient: {self._gradient_gray}")

    @property
    def gray_shade_magenta(self) -> str:
        return self._gray_shade_magenta

    @gray_shade_magenta.getter
    def gray_shade_magenta(self) -> str:
        return self._gray_shade_magenta

    @gray_shade_magenta.setter
    def gray_shade_magenta(self, newValueColor: str):
        self._gray_shade_magenta = newValueColor

    @gray_shade_magenta.deleter
    def gray_shade_magenta(self):
        del self._gray_shade_magenta

    @property
    def white_milky(self) -> str:
        return self._white_milky

    @white_milky.getter
    def white_milky(self) -> str:
        return self._white_milky

    @white_milky.setter
    def white_milky(self, newValueColor: str):
        self._white_milky = newValueColor

    @white_milky.deleter
    def white_milky(self):
        del self._white_milky

    @property
    def white(self) -> str:
        return self._white

    @white.getter
    def white(self) -> str:
        return self._white

    @white.setter
    def white(self, newValueColor: str):
        self._white = newValueColor

    @white.deleter
    def white(self):
        del self._white

    @property
    def light_gray(self) -> str:
        return self._light_gray

    @light_gray.getter
    def light_gray(self) -> str:
        return self._light_gray

    @light_gray.setter
    def light_gray(self, newValueColor: str):
        self._light_gray = newValueColor

    @light_gray.deleter
    def light_gray(self):
        del self._light_gray

    @property
    def dark_gray(self) -> str:
        return self._dark_gray

    @dark_gray.getter
    def dark_gray(self) -> str:
        return self._dark_gray

    @dark_gray.setter
    def dark_gray(self, newValueColor: str):
        self._dark_gray = newValueColor

    @dark_gray.deleter
    def dark_gray(self):
        del self._dark_gray

    @property
    def gray(self) -> str:
        return self._gray

    @gray.getter
    def gray(self) -> str:
        return self._gray

    @gray.setter
    def gray(self, newValueColor: str):
        self._gray = newValueColor

    @gray.deleter
    def gray(self):
        del self._gray

    @property
    def aluminium(self) -> str:
        return self._aluminium

    @aluminium.getter
    def aluminium(self) -> str:
        return self._aluminium

    @aluminium.setter
    def aluminium(self, newValueColor: str):
        self._aluminium = newValueColor

    @aluminium.deleter
    def aluminium(self):
        del self._aluminium

    @property
    def gradient_gray(self) -> str:
        return self._gradient_gray

    @gradient_gray.getter
    def gradient_gray(self) -> str:
        return self._gradient_gray

    @gradient_gray.setter
    def gradient_gray(self, newValueColor: str):
        self._gradient_gray = newValueColor

    @gradient_gray.deleter
    def gradient_gray(self):
        del self._gradient_gray
