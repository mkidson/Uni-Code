# LHC Machine Learning Challenge: The Hunt for Boosted Top Quarks

Machine Learning techniques have revolutionized the identification of top quark decay signatures in experiments at the Large Hadron Collider. This repository describes how to use a public data set for the development of machine learning based top tagging methods, and contribute to the project of discovering new fundamental physics.

Link to data set: http://opendata.cern.ch/record/15013

<p align="center">
<img src="https://user-images.githubusercontent.com/27929701/183285418-b041833f-2249-495a-b3d0-37ae38a1d3a7.png" width=800 class="centerImage" alt="Hits in a particle detector can be represented as images. Here we show such images for single background and signal jets, as well as the averaged background and signal jets. Even for a human, telling signal from background is not easy!">
</p>

*This figure shows individual (top row) and averaged (bottom row) jet images built from the background (left column) and signal (right column) classes.*

## One Minute Introduction

Boosted top tagging is an essential binary classification task for experiments at the Large Hadron Collider (LHC) to measure the properties of the top quark. The ATLAS Top Tagging Open Data Set (*link to public set*) is a publicly available data set for the development of Machine Learning (ML) based boosted top tagging algorithms. The data is split into two orthogonal sets, named *train* and *test* and stored in the HDF5 file format, containing 42 million and 2.5 million jets respectively. Both sets are composed of equal parts signal (jets initiated by a boosted top quark) and background (jets initiated by light quarks or gluons). For each jet, the data set contains:

- The four vectors of constituent particles
- 15 high level summary quantities evaluated on the jet 
- The four vector of the whole jet
- A training weight
- A signal (1) vs background (0) label

There is one rule in using this data set: the contribution to a loss function from any jet should **always** be [weighted by the training weight](https://gitlab.cern.ch/atlas/ATLAS-top-tagging-open-data/-/blob/master/train.py#L272-293). Apart from this a model should separate the signal jets from background by whatever means necessary. Happy tagging!

## Introduction to Boosted Top Tagging at the LHC

The top quark is the heaviest known fundamental particle. Its large mass and strong interactions with the Higgs Boson make it an essential piece of the search for new fundamental physics. These quarks are produced in about one in every billion proton-proton collisions at the LHC. Given the rate of collisions, this means a top quark (along with its anti-particle the anti-top quark) is produced every few seconds when the LHC runs at peak luminosity. However its extremely short lifetime makes it a difficult particle to study. A top quark decays well before it could interact with any matter in a particle detector, so the only way to study this particle is to infer its properties from its decay products. When top quarks decay, they most often produce three lighter quarks in the process. These lighter quarks further *hadronize* into many final state particles which can be measured in a detector. Taken together these particles form a *jet*. A common signature of a top quark is then three of these jets. If the top has a large momentum in a direction perpindicular to the beam axis (transverse momentum or p<sub>T</sub>), or has a large *Lorentz boost*, the three jets can overlap and merge into a single large radius jet. 

Light quarks and gluons are produced in copious numbers in LHC collisions. When these particles hadronize they can produce jets that look very similar to jets initiated by boosted top quarks. This means it is difficult to separate the interesting boosted top quark events from the much more numerous light quark and gluon events. To study high momentum top quarks, LHC experiments need to isolate pure samples of boosted top quark jets from the background, requiring dedicated *top tagging* algorithms. These algorithms classify jets as signal or background based on the measured properties of each constituent in the jet. Typically both signal and background jets have around 50 constituent particles, with some jets having as many as 200. Given the high dimensionality of this feature space and the availability of large data sets of jets labeled as signal or background, boosted top tagging is an ideal application of machine learning techniques.

The existing top tagging models can be divided into two categories:

1. High level quantity based: These taggers are trained on a set of *high level quantities* which are observables that can be calculated from the measured properties of the jet constituents. These quantities are hand designed to draw out differences between signal jets and background jets. High level quantity based taggers have already been put to effective use in LHC experiments.
2. Constituent based: Instead of training on a set of high level quantities, these taggers are trained directly on the measured properties of the jet constituents. They have access to a superset of the information contained in any set of high level quantities, so in principle they can achieve higher performance. However these models need to learn to classify jets essentially from scratch, which necessitates more powerful ML models. This data set is designed for the development of constituent based taggers.

Many existing constituent based taggers showed impressive performance in [previous studies](https://arxiv.org/abs/1902.09914). However these studies trained the taggers on data sets generated with simplified methods for reconstructing jets from constituent particles and simulating the detector response. LHC experiments like CMS and ATLAS have developed highly detailed simulations of their detector based on software framework known as Geant 4. These simulations are the gold standard in modeling the response of a real particle detector, and are used to generate the simulated proton-proton collisions necessary for essentially all analyses of LHC data. A study of existing constituent based top taggers on the ATLAS Top Tagging Open Data Set that accompanys this data's release found that several constituent-based taggers easily surpassed the performance of a high level quantity based tagger, but some taggers which showed promise in previous studies failed to perform in this more realistic setting. Clearly future top tagger development and evaluation should happen in a highly realistic setting. This data set is meant to provide such a setting.

## Data Set Generation

The ATLAS Top Tagging Open Data Set consists of jets taken from simulated collisions of protons at a center of mass energy of 13 TeV. The signal and background jets come from simulations of two different processes:

- Signal: A heavy Z boson (termed Z') with mass of 2 tera-electron-volts decaying to a top anti-top quark pair.
- Background: Jets initiated by light quarks and gluons. These particles are copious by-products of proton-proton collisions at the LHC.

To be included in the data set, all jets are required to satisfy several conditions which produce sharp cut-offs in the distributions of some of the quantities contained in the data set (the jet pseudo-rapidity for example). For details of these requirements see the public note released in tandem with this data set.

Efficient simulation of background events requires introducing unphysical bumps in the distribution of the background jet's p<sub>T</sub>. To get rid of these bumps, the background jet p<sub>T</sub> spectrum could be reweighted to what is actually observed in LHC collisions, but these weights would cover many orders of magnitude and make the training of a top tagger difficult. Luckily there is no reason the background jet p<sub>T</sub> spectrum needs to be physical in a data set only used for training a top tagger. Searches for new physics at the LHC often bin events by quantities like jet p<sub>T</sub>, and if the tagger learns to associate a particular jet p<sub>T</sub> with signal jets, it can assign background jets as signal because they happen to have the correct p<sub>T</sub>. This effect is known as *background scultping*, and can produce false positive results in a search for new physics if not controlled properly. A first order method for eliminating this effect is to reweight the signal and background jet p<sub>T</sub> spectrum to be identical. The solution to both of these problems is to reweight the background jet p<sub>T</sub> spectrum to match the signal spectrum. This is the purpose of the training weights included in the data set.

## Data Set Contents

### Constituent Four-vectors

Each jet can have anywhere between 3 and 200 constituent particles. Each of these particles is described by four quantities, which collectively make up the particle's *four-vector*:

- Transverse momentum (p<sub>T</sub>): The component of the particle's momentum perpindicular to the beam axis
- Pseudo-rapidity (&eta;): One of two spatial coordinates in the widely used collider physics coordinate system
- Azimuthal angle (&phi;): The other spatial coordinate
- Energy

The constituent four-vectors are contained in branches named `['fjet_clus_pt', 'fjet_clus_eta', 'fjet_clus_phi', 'fjet_clus_E']`. Since jets contain a variable number of constituent particles, these branches have many zero padded entries. Handling the variable length quality of this data is an important challenge in building effective constituent based top taggers. For convenience the constituents are listed in order of decreasing p<sub>T</sub>, but this choice is arbitrary. There is no inherent ordering to the constituents in a jet!

Lastly the angular coordinates (&eta; and &phi;) are unitless, while the p<sub>T</sub> and energy are given in units of mega-electron-volts. This choice of units means these quantities can have large magnitudes (some constituents have energies upwards of 300,000 MeV). This large scale should be dealt with in pre-processing to stabilize training (see below).

### High Level Quantities

15 high level quantities are included in this data set. These variables were chosen in two separate studies of high level quantity based top taggers carried out by the ATLAS collaboration: https://cds.cern.ch/record/2259646, https://cds.cern.ch/record/2776782. It suffices to say they "summarize" the information contained in the data describing the jet constituents. They are contained in the following branches:

```
['fjet_C2', 'fjet_D2', 'fjet_ECF1', 'fjet_ECF2', 'fjet_ECF3', 'fjet_L2', 'fjet_L3', 'fjet_Qw', 'fjet_Split12', 'fjet_Split23', 'fjet_Tau1_wta', 'fjet_Tau2_wta', 'fjet_Tau3_wta', 'fjet_Tau4_wta', 'fjet_ThrustMaj']
```

### Jet Four-vector

In addition to the four-vectors of the jet constituents, the data set also includes the four vector of the jet as a whole. The four quantities are stored in branches named `['fjet_pt', 'fjet_eta', 'fjet_phi', fjet_m']`. Notice the four vector of the jet contains the jet mass, as opposed to the energy given for the jet constituents. For the interested user, the jet energy can be calculated from these quantities fairly easily.

### Training Weight

The training weights are contained in the branch `'weights'`. These should always be used to weight the loss function in tagger training. Both tensorflow and pytorch's loss functions support applying such a weighting through a simple key-word argument.

### Labels

Labels are stored in the branch `'labels'` and take the value of 1 for a signal jet and 0 for a background jet.

### Data Set Attributes

For convenience, each data file also contains a set of attributes which can be used to retrieve branch names and other meta data. These attributes are:

* `constit`: The names of the branches storing constituent kinematic quantities
* `hl`: The names of the branches storing high level quantities
* `jet`: The names of the branches storing jet level kinematic quantities
* `num_cons`: The number of constituent level kinematic quantities stored (4)
* `num_hl`: The number of high level quantities stored (15)
* `num_jet_features`: The number of jet level kinematic quantities stored (4)
* `num_jets`: The number of jets in the data set

## Best Practices for Training Top Taggers

### Pre-processing

The data set is stored "as simulated" with no pre-processing steps applied other than sorting the jet constituents by decreasing p<sub>T</sub>. However machine learning algorithm training often benefits from applying wise pre-processing. For example:

- In top tagging the &eta; and &phi; coordinates of the jet have no bearing on whether the jet is signal or background, so tagger performance can often be improved by shifting all of the jets such that they sit at the origin of the &eta;-&phi; plane.
- Since the p<sub>T</sub> and energy values are given in MeV, they have quite large magnitudes with some constituents having energies above 300,000 MeV. ML training proceeds best with approximately normally distributed (zero mean and unit standard deviation) inputs, so it is advisable to apply some pre-processing to reduce the scale of these inputs.

These are both standard pre-processing tricks, but there are many other ways of pre-processing tagger inputs. The data set is presented with no pre-processing to encourage experimentation in pre-processing schemes, as they can have considerable impact on tagger performance. For the user's reference the pre-processing scheme used in the ATLAS public note accompanying this data release is implemented in `preprocessing.py`.

### Training and Evaluation

An example tagger training script can be found in `train.py`. This script can run training for a high level quantity based tagger, a simple deep neural network constituent based tagger, and [two purpose built constituent top taggers](https://arxiv.org/abs/1810.05165): the energy flow network and the particle flow network. The user can select between these taggers by setting the `model_type` keyword. The hyper-parameters for these models are hardcoded to match those used in the accompanying ATLAS public note. The user should feel free to experiment with model hyper-parameters and all other settings in the training script. The setting `max_constits` determines the maximum number of constituents considered for each jet. This is default set to 80 to reduce training time and memory consumption, but can be set to the maximum of 200 if the user wishes to ensure all information contained in the data set is available to the tagger.

The training script reports four tagger performance metrics, for all of which higher numbers correspond to better performance. The AUC (area under the reciever operating characteristic curve) and ACC (accuracy) are standard machine learning performance metrics. Background rejection is particle physics terminology for the inverse of the background efficiency (the fraction of correctly classified background events). The script evaluates the background rejection at two fixed signal efficiencies, or *working points*, of 0.5 and 0.8. These metrics are important because any data analysis which makes use of a top tagger will ultimately need to apply a cut on the tagger output to determine which jets are signal and which are background. The location of this cut is often chosen to produce 0.5 or 0.8 signal efficiency, so the performance of a tagger is evaluated by how much of the background is eliminated at these working points.

Top tagger performance is also often evaluated in p<sub>T</sub> bins. The training script also produces plots of the background rejection in bins of jet p<sub>T</sub>, which show how the network performance evolves with jet p<sub>T</sub>.

### Training with Large Data Sets

The training and testing sets require 130GB and 7.6GB respectively when stored on disk. This makes loading all of the data into memory impossible for the vast majority of users. The example training script solves this problem by only using a fraction of the jets in the training set. The user should tune how many jets are taken from the training set, selecting as many jets as will fit within memory constraints. In most cases, using more than a fraction of training set will require data piping. If the user wishes to pursue this option the following resources may be useful:

- Tensorflow: [Data API](https://www.tensorflow.org/guide/data), [Sequence Class](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence), [Pipeline Optimization](https://www.tensorflow.org/guide/data_performance)
- PyTorch: [Datasets and DataLoaders](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)

## Performance Baselines of Existing Taggers

<p align="center">
<img src="https://user-images.githubusercontent.com/27929701/166083546-f24d34cf-89b2-4bb3-bc2d-f2ba08b07dfa.png" width=700 class="centerImage" alt="Performance baselines of existing top taggers on the ATLAS top tagging open data set. These are the numbers to beat.">
</p>

For more information on these baselines, see the public note released with this data set.

## Other Resources

- [ATLAS website](https://atlas.cern/)
- [Glossary of particle physics terms](http://opendata.atlas.cern/books/current/get-started/_book/GLOSSARY.html)
- [An introduction to the top quark](https://indico.cern.ch/event/683640/contributions/2808437/attachments/1629658/2597088/IMFP2018.pdf)

## How to Cite

If you use this data in a research paper, please cite: [https://cds.cern.ch/record/2825328](https://cds.cern.ch/record/2825328)


