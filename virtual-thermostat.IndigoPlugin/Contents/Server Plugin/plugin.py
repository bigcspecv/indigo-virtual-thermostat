class Plugin(indigo.PluginBase):
    def __init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs):
        indigo.PluginBase.__init__(self,pluginId,pluginDisplayName,pluginVersion,pluginPrefs)

    def __del__(self):
        indigo.PluginBase.__del__(self)

    def startup(self):
        self.logger.info(u"Startup called")

    def shutdown(self):
        self.logger.info(u"Shutdown called")

    def closedPrefsConfigUi(self, valuesDict, userCanceled):
        self.logger.info(u"userCanceled: {}".format(userCanceled))