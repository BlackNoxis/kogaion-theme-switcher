# -*- coding: utf-8 -*-

import os 
import subprocess

desktop_environments = ['cinnamon', 'generic', 'gnome', 'kde', 'mate', 'xfce'] 

def desktop_env_detect():
    desktop_environment = 'generic'
    if os.environ.get('KDE_FULL_SESSION') == 'true':
	desktop_environment = 'kde'
    elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
        desktop_environment = 'gnome'
    else:
       
        proc = subprocess.Popen(['xprop', '-root', '_DT_SAVE_MODE'], 
		   stdout = subprocess.PIPE).communicate()
	if ' = "xfce4"' in proc[0]:
	    desktop_environment = 'xfce'

    return desktop_environment

