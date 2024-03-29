import plexapi.exceptions
from .config import PLEX_SERVER, PLEX_USERNAME, PLEX_PASSWORD
from plexapi.myplex import MyPlexAccount

account = MyPlexAccount(PLEX_USERNAME, PLEX_PASSWORD)


def plex_status():
    try:
        plex = account.resource(PLEX_SERVER).connect()
        return True
    except plexapi.exceptions.NotFound:
        return False


def plex_library():
    if plex_status():
        plex = account.resource(PLEX_SERVER).connect()
        all_libraries = {}
        for elem in plex.library.sections():
            all_libraries[elem.title] = ''.join(elem.locations)
        return all_libraries


def plex_update(library):
    if plex_status():
        plex = account.resource(PLEX_SERVER).connect()
        plex.library.section(library).update()