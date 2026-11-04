"""SEAMK-brändivärit Pythonille (matplotlib, python-pptx, python-docx, openpyxl).

Lähde: SEAMKin brändikäsikirja 2025/03. Vaalennetut sävyt on laskettu.
Tunnusvärejä ei ole mukana: ne kuuluvat vain logoon.

Käyttö:
    from seamk_colors import HEX, RGB, CMYK, SERIES, apply_matplotlib_style
"""

RGB = {
    "lila": (84, 37, 131),
    "keltainen": (255, 240, 35),
    "vihrea": (172, 209, 149),
    "pinkki": (232, 167, 198),
    "vaaleansininen": (199, 230, 247),
    "musta": (0, 0, 0),
    "valkoinen": (255, 255, 255),
}

CMYK = {
    "lila": (84, 100, 3, 1),
    "keltainen": (5, 0, 84, 0),
    "vihrea": (39, 0, 52, 0),
    "pinkki": (7, 44, 4, 0),
    "vaaleansininen": (26, 1, 2, 0),
}

PANTONE = {
    "lila": "PMS 267 C",
    "keltainen": "Pantone Process Yellow C",
    "vihrea": "PMS 359",
    "pinkki": "PMS 210",
    "vaaleansininen": "PMS P 115",
}


def _hex(c):
    return "#%02X%02X%02X" % c


def tint(name, fraction):
    """Vaalennettu sävy: fraction=1.0 täysi väri, 0.25 = 25 % väriä + 75 % valkoista."""
    return tuple(round(v * fraction + 255 * (1 - fraction)) for v in RGB[name])


HEX = {k: _hex(v) for k, v in RGB.items()}
for _base in ("lila", "keltainen"):
    for _f in (75, 50, 25, 15):
        HEX[f"{_base}_{_f}"] = _hex(tint(_base, _f / 100))

# Kaaviosarjojen järjestys. Keltainen ja vaaleat lisävärit tarvitsevat
# valkoisella taustalla tumman ääriviivan (kontrasti alle 3:1).
SERIES = [HEX["lila"], HEX["keltainen"], HEX["vihrea"], HEX["pinkki"],
          HEX["vaaleansininen"], HEX["lila_50"]]

FONT_HEADING = ["Alte DIN 1451 Mittelschrift", "Barlow Condensed", "Arial Narrow", "DejaVu Sans"]
FONT_BODY = ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"]


def contrast(a, b):
    """WCAG-kontrastisuhde kahden RGB-tuplen välillä."""
    def lum(c):
        out = []
        for v in c:
            v /= 255
            out.append(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4)
        return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def apply_matplotlib_style():
    """Asettaa matplotlibiin SEAMK-värisyklin ja fontit."""
    import matplotlib as mpl
    from cycler import cycler
    mpl.rcParams.update({
        "axes.prop_cycle": cycler(color=SERIES),
        "font.family": "sans-serif",
        "font.sans-serif": FONT_BODY,
        "axes.titleweight": "bold",
        "axes.titlecolor": HEX["lila"],
        "axes.edgecolor": "#444444",
        "patch.edgecolor": HEX["lila"],
        "patch.linewidth": 0.8,
    })


if __name__ == "__main__":
    for k, v in HEX.items():
        print(f"{k:16s} {v}")
    print("valkoinen/lila  %.1f" % contrast(RGB["valkoinen"], RGB["lila"]))
    print("musta/keltainen %.1f" % contrast(RGB["musta"], RGB["keltainen"]))
