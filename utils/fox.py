import requests

def fox():
    url = 'https://randomfox.ca/floof'


    responce = requests.get(url)


    return responce.json().get('image')
if __name__ == '__main__':
    print(fox())