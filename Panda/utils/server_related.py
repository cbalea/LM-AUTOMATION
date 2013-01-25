'''
Created on 24.09.2012

@author: cbalea
'''
import os
import sys

class ServerRelated(object):


    def serverToBeTested(self):
        try:
            return os.environ["ENVIRONMENT"]
        except KeyError: 
#            return "http://api-staging.pbslm.org/"
            return "http://api-qa.pbslm.org/"
#            return "http://ec2-54-243-130-153.compute-1.amazonaws.com/"

    def getFilePathInProjectFolder(self, filePath):
        path = os.path.abspath(filePath)
        if("Panda/" in path):
                return path
        else: # hack to work on local Windows machine
            localMachinePath = "%sPanda\%s" % (path.split("Panda")[0], filePath)
            if(localMachinePath.startswith("/")==False):
                localMachinePath = localMachinePath.replace("/", "\\")
            return localMachinePath

    def download_directory(self):
            o_s = sys.platform
            if ("win" in o_s):
                directory = ServerRelated().getFilePathInProjectFolder("downloads")
            elif ("linux" in o_s):
                directory = "/tmp"
            return directory
    
    def admin_password(self):
        try:
            return os.environ["ADMIN_PASSWORD"]
        except KeyError: 
            return "admin"
    
    def admin_username(self):
        try:
            return os.environ["ADMIN_USERNAME"]
        except KeyError: 
            return "admin1"