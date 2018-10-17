import argparse
import os
import zipfile

import requests


def download(url):
    filename = url.split('/')[-1]

    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        i = 1
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                print(f'{i} chunk')
                f.write(chunk)
                i += 1

    return filename


def unzip(file, destination):
    with zipfile.ZipFile(file, 'r') as f:
        f.extractall(destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Download archive from the given url'
                                     'and then extract csv')
    parser.add_argument('-u', '--url', required=True,
                        help='Url of archive to retrieve')
    parser.add_argument('-d', '--destination', required=False,
                        default=os.getcwd(),
                        help='Destination')
    parser.add_argument('-s', '--skip-extraction', action='store_true',
                        help='Whether to skip archive uncompression')
    args = vars(parser.parse_args())

    arch = download(args['url'])
    print('Download complete')

    if not args['skip_extraction']:
        unzip(arch, args['destination'])
        print('Archive extracted')

    print('Done')
