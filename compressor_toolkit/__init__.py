# PEP 440 - version number format
VERSION = (0, 5, 1, 'dev0')

# PEP 396 - module version variable
__version__ = '.'.join(map(str, VERSION))

default_app_config = 'compressor_toolkit.apps.CompressorToolkitConfig'
