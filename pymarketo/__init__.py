from marketorestpython.client import MarketoClient
import os

class Marketo(MarketoClient):
    def __init__(self, client_server, client_id, client_secret):
        super().__init__(client_server, client_id, client_secret)

def main():
    mkto = Marketo(os.getenv('MKTO_CLIENT_SERVER'), os.getenv('MKTO_CLIENT_ID'), os.getenv('MKTO_CLIENT_SECRET'))
    pass


if __name__ == '__main__':
    main()