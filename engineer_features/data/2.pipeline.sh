base_file_name=ccrs.v2.20180420

column_headings=`zless ccrs.v2.20180420.bed.gz | head -1`
column_headings=${column_headings:1}
#column_headings=chrom\ start\ end\ ccr_pct\ gene\ ranges\ varflag\ syn_density\ cpg\ cov_score\ resid\ resid_pctile\ unique_key\ number_of_mutations

gzcat $base_file_name.bed.gz | sort -k1,1n -k2,2n | gzip > $base_file_name.sorted.bed.gz
bedtools intersect -nonamecheck -a $base_file_name.sorted.bed.gz -b ../CosmicCodingMuts.vcf.gz -sorted -c | gzip > $base_file_name.sorted.mutationCounts.bed.gz
gzcat $base_file_name.sorted.mutationCounts.bed.gz | python compute_lengths_numberMutations.py --file $base_file_name.lengths_numberMutations.pkl --columns $column_headings 
