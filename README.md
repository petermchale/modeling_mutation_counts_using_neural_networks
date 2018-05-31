# Goal 

We would like to build models that accurately predict the average number of mutations in a given genomic interval, i.e., given the genomic sequence and, possibly, epigenetic information, 
e.g. DNase hypersensitivity profiles. We are particularly interested in the following applications of such models: 

* Learning new genomic "features" responsible for variation in *de novo* mutation rate with genomic coordinate. 

* By fitting the model to germline and somatic variation data, infer genomic regions under natural selection by identifying regions in which the mutation count is lower or higher than expected. 

# Model 

Traditionally, researchers use prior knowledge of what affects mutation rate to build models. In machine learning parlance, features are "engineered" into such models. 
[Here](http://nbviewer.jupyter.org/github/petermchale/modeling_mutation_counts_using_neural_networks/blob/master/engineer_features/model/model.ipynb) is an introductory example of 
this approach to modeling mutation count data. 


