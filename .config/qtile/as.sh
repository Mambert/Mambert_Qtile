#!/bin/sh
xrandr --output DisplayPort-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --refresh 144.0 --output DisplayPort-1 --off --output DisplayPort-2 --off --output HDMI-A-0 --off &

nitrogen --restore &
picom --config ~/.config/picom/picom.conf &
/usr/bin/emacs --daemon
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xset s off &
xset -dpms &
exec /usr/lib/polkit-kde-authentication-agent-1 &
