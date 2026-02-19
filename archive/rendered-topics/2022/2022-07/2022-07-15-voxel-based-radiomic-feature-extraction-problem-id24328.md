---
topic_id: 24328
title: "Voxel Based Radiomic Feature Extraction Problem"
date: 2022-07-15
url: https://discourse.slicer.org/t/24328
---

# Voxel-based radiomic feature extraction problem

**Topic ID**: 24328
**Date**: 2022-07-15
**URL**: https://discourse.slicer.org/t/voxel-based-radiomic-feature-extraction-problem/24328

---

## Post #1 by @Rongjun_Dong (2022-07-15 11:43 UTC)

<p>Hi , I want to komw how to get a feature map that is the same size as the original? I am tring to extract voxel_based feature, and I am confused about the size of feature map? I already tring to do zero paddings at the boundary before extraction, but the feature map has the same size as before padding.<br>
here is my code.</p>
<p>Very thank you for your help！</p>
<blockquote>
<p>import six<br>
import os  # needed navigate the system to get the input data<br>
import SimpleITK as sitk<br>
import radiomics<br>
from radiomics import featureextractor  # This module is used for interaction with pyradiomics<br>
import pandas as pd</p>
<p>img = sitk.ReadImage(“padding_20CA015_N001.nii.gz”)<br>
mask = sitk.ReadImage(“padding_20CA015_N001_SAX_mask2.nii.gz”)</p>
<p>settings = {}<br>
<span class="hashtag-raw">#Voxel-based</span> specific settings<br>
settings[‘kernelRadius’] = 1  <span class="hashtag-raw">#Expecting</span> kernelRadius &gt; 0,the actual size is 2 * kernelRadius + 1 ,defult value is 1,integer, specifies the size of the kernel to use as the radius from the center voxel.<br>
settings[‘maskedKernel’] = True <span class="hashtag-raw">#defult</span> value is True,boolean, specifies whether to mask the kernel with the overall mask.<br>
settings[‘initValue’] = 0 <span class="hashtag-raw">#float</span>, value to use for voxels outside the ROI, or voxels where calculation failed. If set to nan, 3D slicer will treat them as transparent voxels<br>
settings[‘voxelBatch’] = 1000 <span class="hashtag-raw">#integer</span> &gt; 0, this value controls the maximum number of voxels that are calculated in one batch.only by not providing it is the default value of -1 used (which means: all voxels in 1 batch).</p>
<p><span class="hashtag-raw">#Instantiate</span> the extractor<br>
extractor = featureextractor.RadiomicsFeatureExtractor(**settings)  # ** ‘unpacks’ the dictionary in the function call<br>
extractor.disableAllFeatures()<br>
extractor.enableFeaturesByName(glszm=[‘GrayLevelNonUniformity’])</p>
<p>print(‘Extraction parameters:\n\t’, extractor.settings)<br>
print(‘Enabled filters:\n\t’, extractor.enabledImagetypes)  # Still the default parameters<br>
print(‘Enabled features:\n\t’, extractor.enabledFeatures)  # Still the default parameters</p>
<p>result = extractor.execute(img, mask, voxelBased=True)<br>
for key, val in six.iteritems(result):<br>
if isinstance(val, sitk.Image):  # Feature map<br>
sitk.WriteImage(val, key + ‘.nrrd’, True)<br>
print(“Stored feature %s in %s” % (key, key + “.nrrd”))<br>
else:  # Diagnostic information<br>
print(“\t%s: %s” %(key, val))</p>
</blockquote>

---

## Post #2 by @Panos_p (2025-05-10 12:03 UTC)

<p>Hello,<br>
I think i found the exact topic regarding my issue<br>
Its my first dive into the radiomics/medical imaging, and I want to ask you from your experience, if the output feature map which is calculated within the segmentation mask, has the same dimensions with the original image. For example suppose we have a CT volume 128x128x100(height,width,number of slices). I have also the 3D segmentation. The output will have feature values within the 3D ROI, while the voxels outside ROI will have a default dummy value, yielding again 128x128x100 output volume? Thanks in advance</p>

---
