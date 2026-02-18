# How to make lung lesion analysis by parenchyma subtype training in Chest Imaging Platform module

**Topic ID**: 682
**Date**: 2017-07-12
**URL**: https://discourse.slicer.org/t/how-to-make-lung-lesion-analysis-by-parenchyma-subtype-training-in-chest-imaging-platform-module/682

---

## Post #1 by @chenjl1972 (2017-07-12 18:49 UTC)

<p>I plan to make lung lesion analysis in IPF patients based on Dr.Samuel Y. Asharticle’s article:“Densitometric and local histogram based analysis of computed tomography images in patients with idiopathic pulmonary fibrosis” in Respiratory Research2017,which is really a great milestone in the history of lung lesion analysi.<br>
I have some questions about this work.<br>
1 In the module: parenchyma subtype training,the selecting lung areas are divided by lobes ,not 6 zones of lung(upper, middle and lower) as Dr.Samuel’s articlfe. So should I only choose the “any” in the opitional box?<br>
2 After the training,how can I get the labels of different specific type of lesion such as honey comb,reticulation,and then measure the volume of specific lesion and the propotion of each lesion in the total lung?Should I creat the label by fiducial ?However,in the edit module,I have not found a way to tranfer the fiducials to the label.I wonder how are the specific lesion labels created through the training ILD subtype fiducials?<br>
3 How to use the training data to automated analyze the lung lesion?<br>
which module can be used for analyze after finishing the training moduel?There is a module called “lung lesion analyzer”,it seems to be only applicable to nodule analysis.If I want to analysis lung fibrosis lesion in ipf patients,which module can be used for analyze?<br>
Thank you very much<br>
Jinglong Chen</p>

---

## Post #2 by @raul (2017-07-19 04:06 UTC)

<p>Hi Jinglong</p>
<p>Thanks you for your interest in our paper.</p>
<p>The parenchyma subtype training model allows you to build a training dataset of ILD subtypes based on points.  The classifier that labels a full lung is based on a kNN classifier on local histogram features. Currently the Slicer does not implement a the classification step due to some limitation with python. You could use the python skitlearn package to implement your own kNN classifier or you could use the implementation that is provided in the Chest Imaging Platform (CIP) Library [1]. Currently, there is no a Slicer module wrapper for this functionality.</p>
<p>The lung lesion analyzer module is tailored for lung nodule segmentation and radiomics feature extraction and does not perform any IPF related quantification.</p>
<p>I hope this is helpful</p>
<p>Raul</p>
<p>[1] <a href="https://github.com/acil-bwh/ChestImagingPlatform/blob/develop/cip_python/classification/classify_image_subtypes.py" rel="nofollow noopener">https://github.com/acil-bwh/ChestImagingPlatform/blob/develop/cip_python/classification/classify_image_subtypes.py</a>)</p>

---
