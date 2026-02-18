# Classification of features radiomics

**Topic ID**: 17077
**Date**: 2021-04-14
**URL**: https://discourse.slicer.org/t/classification-of-features-radiomics/17077

---

## Post #1 by @Tonyale1975 (2021-04-14 01:39 UTC)

<p>Dear PyRadiomics / 3DSlicer community,</p>
<p>I have been extracting radiomic features with PyRadiomics.<br>
But, when I try to carry out a classification using machine learning techniques, usually the different classifiers classify one class very well and the other does not. I have already tried some pre-processing techniques, such as normalization, scaling, dimensionality reduction, class balancing, feature selection, but without better results.<br>
I am using 3 different datasets, and in both results it has the same characteristic.<br>
The radiomics features have any particular characteristics that need to be addressed?<br>
Thank you for your help.<br>
Tony</p>

---

## Post #2 by @JoostJM (2022-01-11 12:09 UTC)

<p>There are many caveats at performing radiomics features, pertaining to variation in data acquisition, segementation etc. Some important caveats and how to deal with them are listed in the PyRadiomics documentation. Aside from that, investigating if and to what extent sources of noise are messing up your features and how you can deal with them is the bread and butter of a radiomics researcher. Training a classifier is not the difficult part. Getting your labels and feature values right is the hard part.</p>

---
