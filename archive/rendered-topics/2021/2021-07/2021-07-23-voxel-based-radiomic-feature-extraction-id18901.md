# Voxel-based radiomic feature extraction

**Topic ID**: 18901
**Date**: 2021-07-23
**URL**: https://discourse.slicer.org/t/voxel-based-radiomic-feature-extraction/18901

---

## Post #1 by @smcch (2021-07-23 21:02 UTC)

<p>Hi everyone, I am doing radiomic feature extraction using voxel-based mode. Although I can get the feature maps (.nrrd files), I can’t find a way to get each voxel’s values (radiomic feature). I need those values in a .csv or .xls format to train a classification model. Could someone please help me?</p>

---

## Post #2 by @pieper (2021-07-24 12:58 UTC)

<p>The feature maps are the per-voxel radiomics features.  There are a lot of them so the binary nrrd format is more appropriate than a csv file would be.  You can access the per-voxel values by working with the feature maps as a numpy array <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates">like the examples here</a>.</p>

---

## Post #3 by @smcch (2021-07-24 19:31 UTC)

<p>Hi Steve,<br>
Thank you for your quick reply. But, I need to extract all the voxel values (not just for a coordinate) of the feature map. With the code  slicer.util.arrayFromVolume(volumeNode), I can get just some values. Any suggestion ?</p>

---

## Post #4 by @pieper (2021-07-25 14:39 UTC)

<aside class="quote no-group" data-username="smcch" data-post="3" data-topic="18901">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smcch/48/11763_2.png" class="avatar"> smcch:</div>
<blockquote>
<p>With the code slicer.util.arrayFromVolume(volumeNode), I can get just some values.</p>
</blockquote>
</aside>
<p>I’m not sure what you mean here.  The array will have one element for each voxel in the volume.  If the volume is a feature map the element is the feature value for that voxel.</p>

---

## Post #5 by @smcch (2021-07-25 15:02 UTC)

<p>This is the script to obtain one feature (Entropy)</p>
<pre><code class="lang-auto">import numpy
import radiomics
from radiomics import featureextractor
import six
import sys, os
import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk
dataDir = '----my directory-----'
imageName = os.path.join(dataDir, 'brain.nii.gz')
maskName = os.path.join(dataDir, 'roi.nii.gz')
params = os.path.join(dataDir, 'Params.yaml')
extractor = featureextractor.RadiomicsFeatureExtractor(params)
extractor.disableAllFeatures()  # disable all features
extractor.enableFeaturesByName(firstorder=['Entropy'])  # Only enable firstorder Entropy

extractor.settings['initValue'] = 0  # Set the non-calculated voxels to 0

result = extractor.execute(imageName, maskName, voxelBased=True)

for key, val in six.iteritems(result):
  if isinstance(val, sitk.Image):
    parametermap = sitk.GetArrayFromImage(val)
    parametermap[np.isnan(parametermap)] = 0

plt.imshow(parametermap[15, :, :])
plt.show()
print(parametermap)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35969559762731d7e5084460a1cde9de1494d2a8.png" data-download-href="/uploads/short-url/7E3VCvummTslqleWlSrNTMwMXFe.png?dl=1" title="entropy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35969559762731d7e5084460a1cde9de1494d2a8.png" alt="entropy" data-base62-sha1="7E3VCvummTslqleWlSrNTMwMXFe" width="666" height="500" data-dominant-color="ABA0A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">entropy</span><span class="informations">1280×960 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">[[[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]

 [[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]

 [[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]

 ...

 [[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]

 [[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]

 [[0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  ...
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]
  [0. 0. 0. ... 0. 0. 0.]]]

Process finished with exit code 0
</code></pre>
<p>As you see, I got only 0 values…<br>
I tried to save the array to csv, but It seem not to be compatible with 3D arrays. So, I reshaped the array to 3D, but It doesn’t work…</p>
<p>The map looks fine, but I need the values of every voxel from all the radiomic features</p>

---

## Post #6 by @pieper (2021-07-25 15:56 UTC)

<p>Ah, that’s because numpy shortens the output by only showing the first and last values, so for volumes with some padding it often looks empty but isn’t.  Try <code>print(parametermap.mean())</code> or <code>print(parametermap.max())</code> instead.</p>

---

## Post #7 by @smcch (2021-07-25 17:51 UTC)

<p>Yes, with  .mean = 0.5405715539212325,  and with  .max = 4.095795255000928.  But, I need the entire array of the volume (voxel by voxel) in a table format.<br>
Thanks a lot for your help!</p>

---

## Post #8 by @pieper (2021-07-25 18:44 UTC)

<p>Hmm, that’s going to be a long table, but if that’s what you need then you can just make a nested loop through all the slice, row, column indices and save the corresponding values into a table.   You can get the dimensions from the array’s <code>shape</code> property.  You might use a <a href="https://docs.python.org/3/library/csv.html">csv writer</a>.</p>

---

## Post #9 by @smcch (2021-07-26 08:47 UTC)

<p>Thanks Steve, but I can’t get a proper table, there is a problem with 3D array type. I wonder if there is a “clean” way to do what I’m looking for…</p>

---

## Post #10 by @smcch (2021-07-26 09:18 UTC)

<p>By the way, with    np.set_printoptions(threshold=np.inf)   I get all values from 1 slice of my volume</p>

---

## Post #11 by @Rongjun_Dong (2022-06-23 19:39 UTC)

<p>Hi, did you solve this problem please. I recently had this one problem too and would like some advice.</p>

---

## Post #12 by @Ywatana29 (2024-06-02 20:23 UTC)

<p>Have we solved this problem? I need the answer. My question is related. How do I write voxel-based feature map  data in a nrrd file, which I can import to 3D slicer?</p>

---

## Post #13 by @smcch (2024-06-03 12:00 UTC)

<p>Altought Pyradiomics offers the option to save the feature maps as nrrd. The best solution I found is to extract the features and convert them directly into an array while keeping the spatial information from the source segmentation (mask). Please check out this repo <a href="https://github.com/smcch/Predicting_Glioblastoma_Recurrence_MRI/tree/main" class="inline-onebox" rel="noopener nofollow ugc">GitHub - smcch/Predicting_Glioblastoma_Recurrence_MRI</a></p>

---
