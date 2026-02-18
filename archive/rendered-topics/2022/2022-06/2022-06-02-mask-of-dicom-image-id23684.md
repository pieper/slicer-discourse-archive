# Mask of dicom image

**Topic ID**: 23684
**Date**: 2022-06-02
**URL**: https://discourse.slicer.org/t/mask-of-dicom-image/23684

---

## Post #1 by @Van_Tran_Sang_Huynh (2022-06-02 13:23 UTC)

<p>I use python pyradiomics for feature extraction. I have imported the DICOM image but about the masking part i still don’t know if i did it right or not. If my masking part is wrong, please tell me how to correct and mask the dicom image!!! Please<br>
import SimpleITK as sitk<br>
import matplotlib.pyplot as plt</p>
<p>imageName = ‘C:/Users/Admin/Desktop/CERR/Gui SV/CT3.DCM’<br>
maskName = ‘C:/Users/Admin/Desktop/CERR/Gui SV/CT3.DCM’<br>
image = sitk.ReadImage(imageName)<br>
mask = sitk.ReadImage(maskName)</p>
<p>ndImg = sitk.GetArrayFromImage(image)<br>
ndLbl = sitk.GetArrayFromImage(mask)<br>
plt.imshow(ndImg[0])<br>
plt.show()<br>
plt.imshow(ndLbl[0])<br>
plt.show()</p>
<p>settings = {}<br>
settings[‘binWidth’] = 25</p>
<h1><a name="p-78858-if-enabled-resample-image-resampled-image-is-automatically-cropped-1" class="anchor" href="#p-78858-if-enabled-resample-image-resampled-image-is-automatically-cropped-1" aria-label="Heading link"></a>If enabled, resample image (resampled image is automatically cropped.</h1>
<p>settings[‘resampledPixelSpacing’] = None  # [3,3,3] is an example for defining resampling (voxels with size 3x3x3mm)<br>
settings[‘interpolator’] = sitk.sitkBSpline<br>
settings[‘label’] = 1 <span class="hashtag-raw">#Since</span> the mask area has a pixel value of 1 (otherwise it is 0).</p>
<p><span class="hashtag-raw">#Check</span> the integrity of the mask and create a bbox# 2020/1/23 Addendum<br>
bb, correctedMask = imageoperations.checkMask(image, mask)<br>
if correctedMask is not None:<br>
mask = correctedMask<br>
image, mask = imageoperations.cropToTumorMask(image, mask, bb)</p>
<p>firstOrderFeatures = radiomics.firstorder.RadiomicsFirstOrder(image, mask, **settings)</p>
<h1><a name="p-78858-firstorderfeaturesenablefeaturebynamemean-true-2" class="anchor" href="#p-78858-firstorderfeaturesenablefeaturebynamemean-true-2" aria-label="Heading link"></a>firstOrderFeatures.enableFeatureByName(‘Mean’, True)</h1>
<p>firstOrderFeatures.enableAllFeatures()</p>
<p>print('Will calculate the following first order features: ‘)<br>
for f in firstOrderFeatures.enabledFeatures.keys():<br>
print(’  ', f)<br>
print(getattr(firstOrderFeatures, ‘get%sFeatureValue’ % f).<strong>doc</strong>)</p>
<p>print(‘Calculating first order features…’)<br>
results = firstOrderFeatures.execute()<br>
print(‘done’)</p>
<p>print('Calculated first order features: ‘)<br>
for (key, val) in six.iteritems(results):<br>
print(’  ', key, ‘:’, val)</p>

---

## Post #2 by @JoostJM (2022-06-04 12:33 UTC)

<p>There are 2 main points regarding your code:</p>
<ol>
<li>The code you use does not reflect the intended use of PyRadiomics. It’s much, much, much better to use the featureextractor module, it’s designed for this.</li>
<li>You load the same file as both image and mask. Generally, your mask should be an image containing only 1’s and 0’s identifying your region. This mask is obtained by segmenting the lesion on the DICOM images. This can be done for example using slicer.</li>
</ol>

---

## Post #4 by @Van_Tran_Sang_Huynh (2022-06-05 13:33 UTC)

<p>Did you find this code useful? And can you help me in more detail about creating labels for lung cancer dicom images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c5c538d533dfd81cc96f74c0dce08e4d9e9051.png" data-download-href="/uploads/short-url/gWI3SMgy0IxRKMYEZLAQWn0dJXr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c5c538d533dfd81cc96f74c0dce08e4d9e9051_2_690x388.png" alt="image" data-base62-sha1="gWI3SMgy0IxRKMYEZLAQWn0dJXr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c5c538d533dfd81cc96f74c0dce08e4d9e9051_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c5c538d533dfd81cc96f74c0dce08e4d9e9051_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c5c538d533dfd81cc96f74c0dce08e4d9e9051_2_1380x776.png 2x" data-dominant-color="FAF8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 375 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
