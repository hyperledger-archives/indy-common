import glob
import os
import shutil
from shutil import copyfile

from sovrin_common.constants import Environment


class Setup:

    def __init__(self, basedir):
        self.base_dir = basedir

    def setupAll(self):
        self.setupNode()
        self.setupClient()

    def setupCommon(self):
        self.setupTxns("poolLedger")

    def setupNode(self):
        self.setupCommon()
        self.setupTxns("domainLedger")

    def setupClient(self):
        self.setupCommon()
        self.setupSampleInvites()

    def setupTxns(self, key):
        import data
        dataDir = os.path.dirname(data.__file__)

        # TODO: Need to get "test" and "live" from ENVS property in config.py
        # but that gives error due to some dependency issue
        allEnvs = {
            "local": Environment("pool_transactions_local",
                                 "transactions_local"),
            "test": Environment("pool_transactions_sandbox",
                                "transactions_sandbox"),
            "live": Environment("pool_transactions_live",
                                "transactions_live")
        }
        for envName, env in allEnvs.items():
            for keyName, fileName in env._asdict().items():
                if keyName == key:
                    sourceFilePath = os.path.join(dataDir, fileName)
                    if os.path.exists(sourceFilePath):
                        destFilePath = os.path.join(self.base_dir, fileName)
                        copyfile(sourceFilePath, destFilePath)

        return self

    def setupSampleInvites(self):
        import sample
        sdir = os.path.dirname(sample.__file__)
        sidir = os.path.join(self.base_dir, "sample")
        os.makedirs(sidir, exist_ok=True)
        files = glob.iglob(os.path.join(sdir, "*.sovrin"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, sidir)
        return self
