# Goal 

We would like to build models that accurately predict the average number of mutations in a given genomic interval, i.e., given the genomic sequence and, possibly, epigenetic information, 
e.g. DNase hypersensitivity profiles. We are particularly interested in the following applications of such models: 

* Learning new genomic "features" responsible for variation in *de novo* mutation rate with genomic coordinate. 

* Infer genomic regions under natural selection by identifying regions in which the mutation count deviates 
from the expectations of the trained model. In other words, infer variants that give rise to inherited Mendelian diseases and driver mutations in cancer.

# Tensorflow 

The code in this repo uses TensorFlow. Best is to set up a `conda` environment and install TensorFlow there: 

```
conda create -n tensorflow python=2 ipython-notebook --yes
source activate tensorflow 
pip install tensorflow
```

As an alternative to `pip`, one should be able to install TensorFlow using `conda install -c conda-forge tensorflow`.

# Feature-engineered models 

Traditionally, researchers use prior knowledge of what affects mutation rate to build models. In machine learning parlance, features are "engineered" into such models. 
[Here](http://nbviewer.jupyter.org/github/petermchale/modeling_mutation_counts_using_neural_networks/blob/master/engineer_features/model/model.ipynb) is an introduction 
to this approach
and [here](http://nbviewer.jupyter.org/github/petermchale/modeling_mutation_counts_using_neural_networks/blob/master/engineer_features/data/analysis.ipynb) 
is a naive application of this approach to cancer data. 

# Possible next steps 

1. Find all somatic variants that are in highly constrained CCRs. 
Are those variants enriched in cancer driver mutations or known cancer genes? [Credit: Brent Pedersen]
1. Sanity-check by training the model using only mutations that are known to be correlated with certain genomic features, e.g., C->T mutation rate 
is known to be influenced by CpG density  
1. Train the model using only mutations **not** subject to natural selection, e.g. synonymous mutations in the cancer genome, before searching for genomic regions under natural selection
1. Compute a QQ plot to better compare data and model. Specifically, rank-order the total mutation counts per CCR, both for the data, 
and for a synthetic data set of equal size produced by the model, 
and plot one set of *order statistics* against the other. 
By first rank-ordering, we expect to reduce the noise in plots of expected versus actual mutation counts, 
increasing the power to discern deviations from expectations.
1. Extend the neural network to include hidden nodes thereby making it possible to model mutation rates that are non-monotonic functions of feature variables
1. Develop models that learn, rather than being fed, features that are predictive of mutation rate, e.g. feeding models genomic sequence rather than CpG density

