'''
Created on 20.09.2012

@author: cbalea
'''
import random
import string

class RandomGenerators(object):
    
    def generateRandomString(self, length):
        return ''.join(random.sample(string.ascii_uppercase + string.digits, length))
    
    
    def generateRandomDigits(self, lengthOfDigits):
        return ''.join(random.sample(string.digits, lengthOfDigits))