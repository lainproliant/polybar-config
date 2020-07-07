#!/usr/bin/env python
# --------------------------------------------------------------------
# generate.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Thursday January 2, 2020
#
# Distributed under terms of the MIT license.
# --------------------------------------------------------------------
import json
import os
from jinja2 import Template


# -------------------------------------------------------------------
def load_template():
    with open("config.jinja", "r") as infile:
        return Template(infile.read())


# -------------------------------------------------------------------
def load_font_config():
    with open(os.path.expanduser("~/.font/config.json"), "r") as infile:
        return json.load(infile)


# -------------------------------------------------------------------
def main():
    template = load_template()
    font_config = load_font_config()
    print(template.render(**font_config))


# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
