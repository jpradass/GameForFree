from ..version import version
#from version import version

def health():
    return {'Status': 'OK'}

def server_version():
    return {'Version': f'v{version}'}

def refresh():
    pass