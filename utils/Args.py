import sys

class Args:
    @staticmethod
    def isValidPort(arg):
        try:
            return isinstance(arg, int) and 1024 < arg < 65535
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def getFirst():
        args = sys.argv
        if(len(args) <= 1):
            raise Exception("No port provided")
        try:    
            firstArg = int(args[1])
            if(Args.isValidPort(firstArg)):
                return firstArg
        except Exception as e:
            raise Exception(e)            