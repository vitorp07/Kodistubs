## @package xbmcaddon
#  A class to access addon properties.
#


class Addon(object):
    def __init__(self, id='koditests.test.addon'):
        """Creates a new Addon class.

        id: string - id of the addon (autodetected in XBMC Eden)

        Example:
            self.Addon = xbmcaddon.Addon(id='script.recentlyadded')
        """
        self._id = id
        self._settings = {}

    def getLocalizedString(self, id):
        """Returns an addon's localized 'unicode string'.

        id: integer - id# for string you want to localize.

        Example:
            locstr = self.Addon.getLocalizedString(id=6)
        """
        return 'Fake UI string'

    def getSetting(self, id):
        """Returns the value of a setting as a unicode string.

        id: string - id of the setting that the module needs to access.

        Example:
        apikey = self.Addon.getSetting('apikey')
        """
        try:
            setting = self._settings[id]
        except KeyError:
            setting = ''
        return setting

    def setSetting(self, id, value):
        """Sets a script setting.

        id: string - id of the setting that the module needs to access.
        value: string or unicode - value of the setting.

        Example:
            self.Settings.setSetting(id='username', value='teamxbmc')
        """
        self._settings[id] = value

    def openSettings(self):
        """Opens this scripts settings dialog."""
        pass

    def getAddonInfo(self, id):
        """Returns the value of an addon property as a string.

        id: string - id of the property that the module needs to access.

        Note:
            Choices are (author, changelog, description, disclaimer, fanart, icon, id, name, path
            profile, stars, summary, type, version)

        Example:
            version = self.Addon.getAddonInfo('version')
        """
        if id == 'id':
            return self._id
        elif id == 'path':
            return '/some/fake/path'
        return 'Fake addon info'
