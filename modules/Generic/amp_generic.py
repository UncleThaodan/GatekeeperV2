#
import AMP as AMP
import os

DisplayImageSources = ['Generic']
class AMPGeneric(AMP.AMPInstance):
    def __init__(self, instanceID = 0, serverdata = {},Index = 0,Handler=None):
        self.APIModule = 'Generic'
        
        super().__init__(instanceID,serverdata,Index,Handler=Handler)
        self.Console = AMPGenericConsole(AMPInstance = self)


class AMPGenericConsole(AMP.AMPConsole):
    def __init__(self, AMPInstance = AMPGeneric):
        super().__init__(AMPInstance)