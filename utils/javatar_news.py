import sublime
from .javatar_actions import *


VERSION = "13.10.28.0.59b"
UPDATEFOR = "dev"
NEWSID = 4
NEWS = " - Organize Imports: Now improved and prepared to release on stable channel!\n - Refactor code to use tab instead of spaces\n - Dynamic method call auto-complete: In experimenting (available on debug_mode only)\n\nTry it out in Development Section"


def getVersion():
	return VERSION

def checkNews():
	getAction().addAction("javatar.util.news", "Check news")
	from .javatar_utils import getSettings, setSettings, isStable
	if getSettings("message_id") != NEWSID and getSettings("message_id") != -1:
		if isStable() and (UPDATEFOR == "stable" or UPDATEFOR == "all"):
			sublime.message_dialog("Javatar: Package has been updated!\n" + NEWS)
			setSettings("message_id", NEWSID)
		elif not isStable() and (UPDATEFOR == "dev" or UPDATEFOR == "all"):
			sublime.message_dialog("Javatar [Dev]: Package has been updated!\n" + NEWS)
			setSettings("message_id", NEWSID)
