import ipfsApi


# Testing by Nebula AI
def add(client, filename):
    file_upload = client.add(filename)
    print("File is uploaded: ", file_upload)
    return file_upload['Hash']


def download(client, hash):
    client.get(hash)
    with open(hash, 'r') as fin:
        print(fin.read())


if __name__ == "__main__":
    client = ipfsApi.Client(host='127.0.0.1', port=5001)
    hash = add(client, "btfs.txt")
    download(client, hash)
