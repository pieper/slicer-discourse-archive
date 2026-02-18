# Help in deep understanding pyRadiomics

**Topic ID**: 16269
**Date**: 2021-02-28
**URL**: https://discourse.slicer.org/t/help-in-deep-understanding-pyradiomics/16269

---

## Post #1 by @11117 (2021-02-28 08:36 UTC)

<p>Hello everyone,</p>
<p>I’m trying to understand my results that I get from pyradiomics - FeatureExtractor and I have two questions:</p>
<ol>
<li>I want to understand what values the extractor gets me, so I calculate manually the energy, max, min in the ROI to compare the results with pyradomics results. I didn’t get the same values. I checked this on the example in radiomics (brain) (with one label)<br>
my method - I upload the mask and the image to an float array with nrrd.read() and did manually calculate…for exp, I calculate the max value in the lesion :<br>
image = nrrd.read(path/to/brain_image)<br>
mask =  = nrrd.read(path/to/brain_mask_image)<br>
max(image[mask == 1])</li>
</ol>
<p>and then compare the results from the pyradiomics value.<br>
anyone can explain me why I don’t get the same values?</p>
<ol start="2">
<li>what the different between seg Extract to voxel Extract? what the meaning of feature map?<br>
how can I analyse the voxel Extract?</li>
</ol>
<p>Tnx!<br>
Hodaya</p>

---

## Post #2 by @JoostJM (2021-03-09 12:15 UTC)

<ol>
<li>The best start would be to run PyRadiomics with log-level set to debug and read the log, it will give you more insight into what PyRadiomics does.<br>
Additionally, you can review the diagnostic features, which records the mask in the ROI at various stages in pre-processing.</li>
</ol>
<p>What type of settings are you using?</p>
<ol start="2">
<li>Voxel-based calculates feature values for each voxel, using a kernel around each voxel. Segment-based calculates 1 value per feature for the entire ROI, based on all voxels in the ROI.<br>
As to analyzing voxel extract; this results in feature <em>maps</em>, which need to be analyed as such (e.g. by the recombining the values into a single value, or, even better, working with outcomes that give results on a voxel-level, such as areas in a histology slice matched to your image).</li>
</ol>

---

## Post #3 by @11117 (2021-05-20 11:58 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>my settings is:</p>
<p>binWidth: 25<br>
label: 1<br>
normalize: True<br>
interpolator: ‘sitkBSpline’<br>
resampledPixelSpacing: [2.2,2.2,2.2]<br>
minimumROIDimensions : 1</p>
<p>I still don’t get the same first order values when I compere manual computation and what i get from the  pyRadiommics extractor.</p>
<p><strong>my code:</strong><br>
import numpy as np<br>
import nrrd<br>
import SimpleITK as sitk<br>
from radiomics import featureextractor, getTestCase<br>
import six</p>
<p><strong>manually:</strong><br>
imageName, maskName = getTestCase(‘brain1’, dataDir)<br>
im ,im_dir= nrrd.read(imageName)<br>
msk, msk_dir = nrrd.read(maskName )<br>
im = im.astype(float)<br>
seg_val = im[msk&gt;0]</p>
<p><em>i want to use the same normalization as pyRadiommics use, so i convert to sitk and back:</em><br>
seg_val = sitk.GetImageFromArray(seg_val .reshape(-1,1))<br>
seg_val = sitk.Normalize(seg_val )<br>
seg_val = sitk.GetArrayFromImage(seg_val )</p>
<p>maximum = seg_val .max()<br>
energy = np.nansum(seg_val **2)</p>
<p><strong>and for pyRadioimics:</strong></p>
<p>extractor = featureextractor.RadiomicsFeatureExtractor(‘params.yaml’)<br>
results = extractor.execute(imageName, maskName , label = 1)<br>
results[‘original_firstorder_Energy’]<br>
results[‘original_firstorder_Maximum’]</p>
<p>I don’t get the same values for the energy and max, and for the rest first order features. what I’m missing?<br>
also if I don’t use normalization, I don’t get the same results.<br>
I tried also to do it with binWidth=1, didn’t get any changes.</p>
<p>Tnx<br>
Hodaya</p>

---

## Post #4 by @JoostJM (2022-01-21 10:01 UTC)

<p>For PyRadiomics, you have enabled resampling, which changes the pixel spacing and thereby also the pixel values. This isn’t applied in your manual case.</p>
<p>Moreover, in your manual case, you apply normalization only on the values inside your ROI. In PyRadiomics, normalization is applied to the entire image. Normalizing just the ROI is invalid.</p>

---
