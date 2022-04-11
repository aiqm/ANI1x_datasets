# ANI1x_datasets
The ANI-1ccx and ANI-1x data sets, coupled-cluster and density functional theory properties for organic molecules. **Please downlod actual datafiles from FigShare first**: https://springernature.figshare.com/collections/The_ANI-1ccx_and_ANI-1x_data_sets_coupled-cluster_and_density_functional_theory_properties_for_molecules/4712477

This repository contains the scripts needed to access the ANI-1x data sets.

#### Required software

 - python>=3.5
 - numpy
 - h5py
 

#### Repository content

 - Python reader for HDF5 dataset file
 - Interactive plots comparing data distribution in QM9, ANI-1, ANI-1x and ANI-1ccx datasets in form of parametric t-SNE projection of the first later activation of ANI-1x model. 
   - [Carbon](https://htmlpreview.github.io/?https://github.com/aiqm/ANI1x_datasets/blob/master/data_embedding/ani1x_embed_C_neighborType.html)
   - [Hydrogen](https://htmlpreview.github.io/?https://github.com/aiqm/ANI1x_datasets/blob/master/data_embedding/ani1x_embed_H_neighborType.html)
   - [Nitrogen](https://htmlpreview.github.io/?https://github.com/aiqm/ANI1x_datasets/blob/master/data_embedding/ani1x_embed_N_neighborType.html)
   - [Oxygen](https://htmlpreview.github.io/?https://github.com/aiqm/ANI1x_datasets/blob/master/data_embedding/ani1x_embed_O_neighborType.html)
 
 ... 


#### If you use ANI-1x dataset please cite the following papers

- ANI-1x dataset
  
  Smith, J. S.; Nebgen, B.; Lubbers, N.; Isayev, O.; Roitberg, A. E. Less Is More: Sampling Chemical Space with Active Learning. J. Chem. Phys. 2018, 148 (24), 241733. <br>https://doi.org/10.1063/1.5023802</br>
  
- ANI-1ccx dataset

  Smith, J. S.; Nebgen, B. T.; Zubatyuk, R.; Lubbers, N.; Devereux, C.; Barros, K.; Tretiak, S.; Isayev, O.; Roitberg, A. E. Approaching Coupled Cluster Accuracy with a General-Purpose Neural Network Potential through Transfer Learning. Nat. Commun. 2019, 10 (1), 2903. <br>https://doi.org/10.1038/s41467-019-10827-4</br>

- wB97x/def2-TZVPP data

  Zubatyuk, R.; Smith, J. S.; Leszczynski, J.; Isayev, O. Accurate and Transferable Multitask Prediction of Chemical Properties with an Atoms-in-Molecules Neural Network. Sci. Adv. 2019, 5 (8), eaav6490. <br>https://doi.org/10.1126/sciadv.aav6490</br>
