---
topic_id: 12428
title: "Code Stop Extracting Wavelet And Gradient Features It Used T"
date: 2020-07-07
url: https://discourse.slicer.org/t/12428
---

# Code stop extracting wavelet and gradient features (it used to do so)

**Topic ID**: 12428
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/code-stop-extracting-wavelet-and-gradient-features-it-used-to-do-so/12428

---

## Post #1 by @MachadoL (2020-07-07 19:58 UTC)

<p>I have this code which is an adaption of the examples offered and it use to extract all the features as described in the params.yaml . The code use to work well, now it is extracting less features than it has to.</p>
<p>extractor.py file:</p>
<pre><code>from __future__ import print_function

import os
import sys
import logging
import numpy as np
import SimpleITK as sitk
import six
import radiomics

reader1 = sitk.ImageFileReader()
reader2 = sitk.ImageFileReader()
reader1.SetFileName(input_imageName)
reader2.SetFileName(input_maskName)
image = reader1.Execute()
mask = reader2.Execute()

dataDir = '/home/leonardo/Desktop/Mestrado/DataSet-Pesquisa/Estudo-I/Included-Reprocessamento'
params = os.path.join(dataDir,"params.yaml")

extractor = radiomics.featureextractor.RadiomicsFeatureExtractor(params)
results = extractor.execute(image, mask)

features = []
features.append("Patients")
values = []
values.append(patient_id)

i = 0 # feature counter 
for (key, val) in six.iteritems(results):
    
    # the results comes with a 32 lines header. The first condition is to avoid storing those information;
    if (i &gt;= 32):   

    if (key.find("wavelet") == -1) and (key.find("gradient") == -1):
        # This condition means if the feature is neither wavelet nor gradient it WILL BE SAVED; 
        features.append(key) 
        values.append(val)
    elif (key.find("wavelet") != -1) and (key.find("firstorder") != -1):
        # This condition means if the feature is WAVELET it MUST BE FIRSTORDER too to be SAVED;
        features.append(key) 
        values.append(val)
    elif (key.find("gradient") != -1) and (key.find("firstorder") != -1):
        # This condition means if the feature is GRADIENT it MUST BE FIRSTORDER too to be SAVED;
        features.append(key) 
        values.append(val)
    i += 1
print('done')

feature_vals = ','.join(str(e) for e in values)    
feature_keys = ','.join(str(e) for e in features)

print("Total number of features extrated: ", len(features), ".")

if os.path.exists("pyRadiomicsOutput.csv"):
    with open("pyRadiomicsOutput.csv", "a+") as f:
        f.write(feature_vals)
        f.write("\n")
else:
    with open("pyRadiomicsOutput.csv", "a+") as f:
        f.write(feature_keys) 
        f.write("\n")
        f.write(feature_vals)
        f.write("\n")
</code></pre>
<p>Now, the params.yaml:</p>
<pre><code>imageType:
  Original: {}
  Wavelet: {}
  Gradient: {}

featureClass:
  # redundant Compactness 1, Compactness 2 an Spherical Disproportion features are disabled by default, they can be
  # enabled by specifying individual feature names (as is done for glcm) and including them in the list.
  firstorder:
  glcm:
  glrlm:
  glszm:
  gldm:
  ngtdm:
  shape:

setting:
  resegmentMode: 'sigma'
  resegmentRange: [-3, 3]

 binWidth: 3
 label: 1
</code></pre>
<p>Any thoughts are welcomed.</p>

---

## Post #2 by @MachadoL (2020-07-08 18:57 UTC)

<p>I found out the issue: The params.yaml was badly connected. I fixed and it worked.</p>

---
