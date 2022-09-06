#!/usr/bin/env python3

from subprocess import run
from sys import argv

themes = {
    "Latte": {
        "openbox": "Latte-Openbox",
        "qtile": "frappe",
        "nvim": "catppuccin",
        "Gtk": "WhiteSur-Light-nord",
        "kitty": "latte",
        "polybar": "latte",
        "alacritty": "catppuccin",
        "emacs": "latte",
        "zathura": "latte"
    },
    "Macchiato": {
        "openbox": "Macchiato-Openbox",
        "qtile": "macchiato",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-dark",
        "kitty": "macchiato",
        "polybar": "macchiato",
        "alacritty": "catppuccin",
        "emacs": "macchiato",
        "zathura": "macchiato"
    },
    "Frappe": {
        "openbox": "Frappe-Openbox",
        "qtile": "frappe",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-dark",
        "kitty": "frappe",
        "polybar": "frappe",
        "alacritty": "catppuccin",
        "emacs": "frappe",
        "zathura": "frappe"
    },
    "Mocha": {
        "openbox": "Mocha-Openbox",
        "qtile": "mocha",
        "nvim": "catppuccin",
        "Gtk": "Catppuccin-dark",
        "kitty": "mocha",
        "polybar": "mocha",
        "alacritty": "catppuccin",
        "emacs": "mocha",
        "zathura": "mocha"
    },
    "Purple": {
        "openbox": "Purple-Openbox",
        "qtile": "purple",
        "nvim": "palenight",
        "Gtk": "WhiteSur-dark-nord",
        "kitty": "purple",
        "polybar": "purple",
        "alacritty": "dracula",
        "emacs": "purple",
        "zathura": "dracula"
    },
    "Dracula": {
        "openbox": "Dracula-withoutBorder",
        "qtile": "dracula",
        "nvim": "dracula",
        "Gtk": "dracula",
        "kitty": "dracula",
        "polybar": "dracula",
        "alacritty": "dracula",
        "emacs": "doom-dracula",
        "zathura": "dracula"
    },
    "Palenight": {
        "openbox": "Palenight-Openbox",
        "qtile": "palenight",
        "nvim": "palenight",
        "Gtk": "palenight",
        "kitty": "palenight",
        "polybar": "palenight",
        "alacritty": "palenight",
        "emacs": "doom-palenight",
        "zathura": "palenight"
    },
    "One": {
        "openbox": "Doom-One",
        "qtile": "one",
        "nvim": "doom-one",
        "Gtk": "AtomOneDarkTheme",
        "kitty": "one",
        "polybar": "one",
        "alacritty": "one",
        "emacs": "doom-one",
        "zathura": "macchiato"
    },
    "Nord": {
        "openbox": "Nord-Openbox",
        "qtile": "nord",
        "nvim": "nord",
        "Gtk": "Nordic-darker-v40",
        "kitty": "nord",
        "polybar": "one",
        "alacritty": "one",
        "emacs": "doom-nord",
        "zathura": "macchiato"
    }
}


thing = {
    'openbox': ((42, (10, -8)), '.config/openbox/rc.xml'),
    'qtile': ((7, (9, -2)), '.config/qtile/screens.py'),
    'kitty': ((-1, (15, -6)), '.config/kitty/kitty.conf'),
    'alacritty': ((-1, (33, -5)), '.config/alacritty/alacritty.yml'),
    'Gtk': ((14, (15, -1)), '.config/gtk-3.0/settings.ini'),
    'polybar': ((0, (40, -5)), '.config/polybar/config.ini'),
    'nvim': ((-2, (12, -1)), '.config/nvim/init.vim'),
    'emacs': ((34, (18, -2)), '.doom.d/config.el'),
    'zathura': ((-1, (8,-1)), '.config/zathura/zathurarc'),
}


def switch_theme(obj, theme):
    with open(f'{home}{thing[obj][1]}', 'r') as f:
        x = f.readlines()
    line = thing[obj][0][0]
    ind = thing[obj][0][1]

    old = x[line][ind[0]:ind[1]]
    new = x[line].replace(old, themes[theme][obj])

    x[line] = new
    with open(f'{home}{thing[obj][1]}', 'w') as w:
        for i in x:
            w.write(i)


theme = argv[-1]

theme = theme.capitalize()

a = run(
    'echo $HOME',
    shell=True,
    text=True,
    capture_output=True
)

home = a.stdout.strip()+'/'

if theme not in themes:
    print("Error: Theme not found")
    exit()

obj = list(thing)

for i in obj:
    switch_theme(i, theme)

if theme in ['Mocha', 'Macchiato', 'Frappe', 'Latte']:
    with open(f'{home}{thing["nvim"][1]}', 'r') as f:
        x = f.readlines()
    old = x[-3][28:-2]
    new = x[-3].replace(old, theme.lower())
    x[-3] = new

    with open(f'{home}{thing["nvim"][1]}', 'w') as w:
        for i in x:
            w.write(i)


run(
    'qtile cmd-obj -o cmd -f reload_config',
    shell=True
)
run(
    'openbox --reconfigure',
    shell=True
)
