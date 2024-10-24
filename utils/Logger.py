import logging

class Logger:
    @staticmethod
    def info(args):
        FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
        logging.basicConfig(format=FORMAT)
        d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
        logger = logging.getLogger('tcpserver')
        logger.warning('Protocol problem: %s', 'connection reset', extra=args)

    @staticmethod
    def log(message: str):
        FORMAT = "%(asctime)s - %(message)s"
        logging.basicConfig(format=FORMAT)
        logger = logging.getLogger('event')
        logger.info(message)