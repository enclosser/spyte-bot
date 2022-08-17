from .config import URL_TORRENT_SERV
from qbittorrent import Client
import requests

torrents = {}


def torrent_status():
    try:
        response = requests.head(URL_TORRENT_SERV)
    except Exception as e:
        print(f"NOT OK: {str(e)}")
        return False
    else:
        if response.status_code == 200:
            return True
        else:
            print(f"NOT OK: HTTP response code {response.status_code}")
            return False


def torrent_connect():
    if torrent_status():
        qb = Client(URL_TORRENT_SERV)
        return qb


def get_torrents():
    for elem in torrent_connect().torrents():
        torrents[elem['name']] = {
            'state': elem['state'],
            'progress': f'{round(elem["progress"] * 100)}%',
            'path': elem['save_path'][:-1],
            'hash': elem['hash']
        }
    return torrents