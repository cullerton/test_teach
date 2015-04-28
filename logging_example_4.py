import logging

# create our logger with level DEBUG
logger = logging.getLogger('logging_example')
logger.setLevel(logging.DEBUG)

# create a console handler with level Info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# add the console handler to our logger
logger.addHandler(ch)


# create a file handler with level Debug
fh = logging.FileHandler('logging_example.log')
fh.setLevel(logging.DEBUG)
# create a formatter to use with our file handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# tell our file handler to use the formatter
fh.setFormatter(formatter)
# add the file handler to our logger
logger.addHandler(fh)

# some simple log statements
logger.debug('Simple debug log statement.')
logger.info('Simple info log statement.')
logger.warning('Simple warning log statement.')
logger.error('Simple error log statement.')
logger.critical('Simple critical log statement.')
