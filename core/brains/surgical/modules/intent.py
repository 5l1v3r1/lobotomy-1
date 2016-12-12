
class IntentModel:
    values = {
        "android.content.Intent": [
            "parseUri",
            "getAction",
            "getBundleExtra",
            "getClipData",
            "getComponent",
            "getData",
            "getDataString",
            "getExtras",
            "getIntent",
            "getPackage",
            "getScheme",
            "getSelector",
        ]
    }


class IntentModule(object):
    def __init__(self, vm, vmx, package):
        self.name = "intent"
        self.model = IntentModel()
