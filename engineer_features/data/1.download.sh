# usage: <file>.sh <cosmic username> <cosmic password>
if [[ $# -lt 2 ]]; then
    echo "usage: $0 <cosmic username> <cosmic password>"
    exit 1
fi

# https://gist.github.com/petermchale/f382537e680f59c169cd24c3a88c344e 
test -e download_basicAccessAuthentication.py || wget  https://gist.githubusercontent.com/petermchale/f382537e680f59c169cd24c3a88c344e/raw/5dd85b2223bbe8b3c42c71ff9501c2f30ff8c5ad/download_basicAccessAuthentication.py

# COSMIC
echo "downloading, zipping, and indexing the COSMIC data file ..."
python download_basicAccessAuthentication.py --url https://cancer.sanger.ac.uk/cosmic/file_download/GRCh37/cosmic/v85/VCF/CosmicCodingMuts.vcf.gz --username $1 --password $2 
gunzip CosmicCodingMuts.vcf.gz
bgzip CosmicCodingMuts.vcf
tabix CosmicCodingMuts.vcf.gz

echo "The CCR file was obtained from the authors of https://www.biorxiv.org/content/early/2017/11/16/220814"
