#!/bin/bash
#
# run.sh
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Monday May 11, 2020
#
# Distributed under terms of the MIT license.
#

pushd $HOME/.config/polybar
python generate.py > config

# Start polybar on every monitor
if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload xmonad &
  done
else
  polybar --reload xmonad &
fi

popd
