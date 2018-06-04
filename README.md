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
is a naive application of this approach to cancer data. Things one could do next include: 

* Sanity-check the model by training the model using only mutations that are known to be correlated with certain genomic features, e.g., C->T mutation rate 
is known to be influenced by CpG density  
* Extend to other features known to affect mutation rate 
* Train the model using only mutations **not** subject to natural selection, e.g. synonymous mutations in the cancer genome, before searching for genomic regions under natural selection
* Extend the neural network to include hidden nodes thereby making it possible to model mutation rates that are non-monotonic functions of feature variables
