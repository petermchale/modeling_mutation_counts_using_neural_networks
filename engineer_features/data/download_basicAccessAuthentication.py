# purpose: use Basic Access Authentication to download data from a web server
# example usage: python <this file>.py --url https://cancer.sanger.ac.uk/cosmic/file_download/GRCh37/cosmic/v85/VCF/CosmicCodingMuts.vcf.gz --username email@example.com --password mycosmicpassword
# for more on Basic access authentication see: https://en.wikipedia.org/wiki/Basic_access_authentication

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--username')
parser.add_argument('--password')
args = parser.parse_args()

first_response = requests.get(args.url, auth=(args.username, args.password))

if first_response.status_code != 200:
    print first_response.headers['content-type']
    print first_response.encoding
else:
    second_response = requests.get(first_response.json()['url'])
    with open(args.url.split('/')[-1], 'wb') as f:  # give the downloaded file the same name as that on the server
        f.write(second_response.content)
