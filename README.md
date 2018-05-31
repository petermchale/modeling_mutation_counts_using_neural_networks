# Goal 

We would like to build models that accurately predict the average number of mutations in a given genomic interval, i.e., given the genomic sequence and, possibly, epigenetic information, 
e.g. DNase hypersensitivity profiles. We are particularly interested in the following applications of such models: 

* Learning new genomic "features" responsible for variation in *de novo* mutation rate with genomic coordinate. 

* Infer genomic regions under natural selection by identifying regions in which the mutation count deviates 
from expectation under the trained model. In other words, infer variants that give rise to inherited Mendelian diseases and driver mutations in cancer.

# Feature-engineered models 

Traditionally, researchers use prior knowledge of what affects mutation rate to build models. In machine learning parlance, features are "engineered" into such models. 
[Here](http://nbviewer.jupyter.org/github/petermchale/modeling_mutation_counts_using_neural_networks/blob/master/engineer_features/model/model.ipynb) is an introduction 
to this approach
and [here](http://nbviewer.jupyter.org/github/petermchale/modeling_mutation_counts_using_neural_networks/blob/master/engineer_features/data/analysis.ipynb) 
is a naive application of this approach to cancer data. Things one could do next include: 

