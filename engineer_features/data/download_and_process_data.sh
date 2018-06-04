if [[ $# -lt 2 ]]; then
    echo "usage: $0 <cosmic username> <cosmic password>"
    exit 1
fi

# auxilary file to help download COSMIC data: https://gist.github.com/petermchale/f382537e680f59c169cd24c3a88c344e 
if [[ ! -e download_basicAccessAuthentication.py ]]; then 
    wget  https://gist.githubusercontent.com/petermchale/f382537e680f59c169cd24c3a88c344e/raw/5dd85b2223bbe8b3c42c71ff9501c2f30ff8c5ad/download_basicAccessAuthentication.py
fi

# download COSMIC data
if [[ ! -e CosmicCodingMuts.vcf.gz ]]; then
    echo "downloading, zipping, and indexing the COSMIC data file ..."
    python download_basicAccessAuthentication.py --url https://cancer.sanger.ac.uk/cosmic/file_download/GRCh37/cosmic/v85/VCF/CosmicCodingMuts.vcf.gz --username $1 --password $2 
    gunzip CosmicCodingMuts.vcf.gz
    bgzip CosmicCodingMuts.vcf
    tabix CosmicCodingMuts.vcf.gz
fi

base_file_name=ccrs.v2.20180420

echo "the file $base_file_name.bed.gz was obtained from the authors of https://www.biorxiv.org/content/early/2017/11/16/220814"

column_headings=`zless ccrs.v2.20180420.bed.gz | head -1`
column_headings=${column_headings:1} 
column_headings="$column_headings number_of_mutations"

gzcat $base_file_name.bed.gz | sort -k1,1n -k2,2n | gzip > $base_file_name.sorted.bed.gz

echo "intersecting the CCR file and the COSMIC variant file to compute number of somatic mutations in each CCR, along with their lengths, where a CCR can span multiple exons"
bedtools intersect -nonamecheck -a $base_file_name.sorted.bed.gz -b CosmicCodingMuts.vcf.gz -sorted -c | gzip > $base_file_name.sorted.mutationCounts.bed.gz
gzcat $base_file_name.sorted.mutationCounts.bed.gz | python compute_lengths_numberMutations.py --file $base_file_name.lengths_numberMutations.pkl --columns $column_headings 
