# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"
home = os.path.expanduser('~')
terminal = guess_terminal()
rofi = "rofi -show drun run"
firefox = "firefox"
voldwn = "pactl set-sink-volume @DEFAULT_SINK@ -2%"
volup = "pactl set-sink-volume @DEFAULT_SINK@ +2%"
mute = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
picon = "picom --config ~/.config/picom/picom.conf"
picoff = "killall picom"
fsgui = "flameshot gui"

#All colors from nordtheme.com. Use them as needed

def init_colors():
    return [["#2e3440", "#2e3440"], # Color 0, darkest of the "Polar Night" Selection
            ["#3b4252", "#3b4252"], # Color 1
            ["#434c5e", "#434c5e"], # Color 2
            ["#4c566a", "#4c566a"], # Color 3, lightest of the "Ploar Night" Selection
            ["#d8dee9", "#d8dee9"], # Color 4, Darkest of the "Snow Storm" Selection
            ["#e5e9f0", "#e5e9f0"], # Color 5
            ["#eceff4", "#eceff4"], # Color 6, Lightest of the "Snow Storm Selection 
            ["#8fbcbb", "#8fbcbb"], # Color 7, A slight sage-green-blue color, 1st in the "Frost" Selection
            ["#88c0d0", "#88c0d0"], # Color 8, The most brightest blue in the Nordic color scheme. Save for bright borders, etc.
            ["#81a1c1", "#81a1c1"], # Color 9, A slightly pale blue
            ["#5e81ac", "#5e81ac"], # Color 10, A bold blue, but it's no color 8
            ["#bf616a", "#bf616a"], # Color 11, red from the "Aurora" Selection
            ["#d08770", "#d08770"], # Color 12, orange 
            ["#ebcb8b", "#ebcb8b"], # Color 13, yellow
            ["#a3be8c", "#a3be8c"], # Color 14, green
            ["#b48ead", "#b48ead"]] # Color 15, purple

colors = init_colors()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn(rofi), desc="Launch Rofi"),
    Key([mod, "shift"], "b", lazy.spawn(firefox), desc="Launch Firefox"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(voldwn), desc = "Turn device volume down"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volup), desc = "Turn device volume up"),
    Key([], "XF86AudioMute", lazy.spawn(mute), desc = "Mutes device"),
    Key([mod, "shift"], "d", lazy.spawn("flatpak run com.discordapp.Discord"), desc = "Launch Discord"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle visibility of Bar"),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f11", lazy.spawn(picon), desc = "Start Picom with config, located at ~/.config/picom/picom.conf"),
    Key([mod, "shift"], "f12", lazy.spawn(picoff), desc = "Turn off Picom, useful for games or just when it needs a restart"),
    Key([mod, "shift"], "s", lazy.spawn(fsgui), desc = "Start Flameshot to take quick screenshot"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
    border_focus_stack=colors[10],
        border_focus = colors[11],
    border_width=2
    
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



            
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    #background = ["#2e3440", "#3b4252", "#434c5e", "#4c566a"]
    #background = [colors[1], colors[2]] #I'm trying to get this working, I just can't seem to get the formatting to work right. Python doesn't seem to bring up an error, but the bar doesn't show at all. 
    background = ["#2e3440", "#2e3440", "#3b4252", "#3b4252", "#434c5e", "#434c5e", "#4c566a", "#434c5e", "#434c5e", "#3b4252", "#3b4252", "#2e3440", "#2e3440"] # I should really just make an init_colors table. But I'm just gonna slap this on github and never have to do it again. I don't even use the bar, why am I so concerned about the gradient of this bar???
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(
                foreground = "#ebcb8b"
                ),
                widget.GroupBox(
                foreground = colors[13],
                    hide_unused = True,
                    active = colors[6],
                    inactive = "#9297a1",
                    highlight_color = colors[8],
                ),
                widget.Prompt(),
                widget.WindowTabs(
                    foreground = colors[8],
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#2e3440", "#eceff4"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("Mambert", name="default"),
                widget.TextBox("Press &lt;M-d&gt; to start rofi", foreground=colors[10]),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
                #widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = colors[10],
    border_normal = colors[4],
    border_width = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Mambert's Custom Qtile"
