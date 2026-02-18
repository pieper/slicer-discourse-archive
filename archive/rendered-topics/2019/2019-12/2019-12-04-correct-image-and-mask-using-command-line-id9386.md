# Correct image and mask using command line

**Topic ID**: 9386
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/correct-image-and-mask-using-command-line/9386

---

## Post #1 by @Bassam (2019-12-04 15:07 UTC)

<p>Hi pyradiomics team,</p>
<p>kindly I imported DICOM images into 3D slicer and did segmentation and extract the features properly using 3D slicer, then I saved the image and the mask into file. now I wanna make sure that the same features I will get it If i used command line. Unfortunately, I did not get the features by command line using pyradiomics specifying the image and the mask and it showed me an error, here is the message I’ve got it:</p>
<p>C:\features&gt;pyradiomics pancreas_image.nrrd pancreas_label.nrrd<br>
[2019-12-04 22:13:22] E: radiomics.script: Feature extraction failed!<br>
Traceback (most recent call last):<br>
File “C:\Python27\lib\site-packages\pyradiomics-2.2.0.post35+g8da1db7-py2.7-win-amd64.egg\radiomics\scripts\segment.py”, line 70, in _extractFeatures<br>
feature_vector.update(extractor.execute(imageFilepath, maskFilepath, label, label_channel))<br>
File “C:\Python27\lib\site-packages\pyradiomics-2.2.0.post35+g8da1db7-py2.7-win-amd64.egg\radiomics\featureextractor.py”, line 273, in execute<br>
boundingBox, correctedMask = imageoperations.checkMask(image, mask, **_settings)<br>
File “C:\Python27\lib\site-packages\pyradiomics-2.2.0.post35+g8da1db7-py2.7-win-amd64.egg\radiomics\imageoperations.py”, line 239, in checkMask<br>
raise ValueError('Image/Mask datatype or size mismatch. Potential fix: enable correctMask, see ’<br>
ValueError: Image/Mask datatype or size mismatch. Potential fix: enable correctMask, see Documentation:Usage:Customizing the Extraction:Settings:correctMask for more information<br>
Case-1_Image: C:\features\pancreas_image.nrrd<br>
Case-1_Mask: C:\features\pancreas_label.nrrd</p>

---

## Post #2 by @pieper (2019-12-06 15:30 UTC)

<p>You probably need to export to labelmap.</p>
<p>See:</p>
<aside class="quote quote-modified" data-post="1" data-topic="9394">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/crispy13/48/5316_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/the-resolutions-of-segment-and-mri-are-different/9394">The resolutions of segment and mri are different</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Win 10 Pro x64 
Slicer version: 4.10.2 
Expected behavior: 
Actual behavior: 
Some segmentation file resolutions are different with originial mri image resolutions. 
ex1) mri - (150, 512, 512) / seg - (44, 101, 101) 
This seems to happen to the most of the segmentation files with multiple segmentations. 
I created multiple nodes for each tumor and merged them into one node. Was this the cause for it? 
Is there any way to fit seg’s res to mri’s? and if the above method causes pr…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="7446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andrea_barucci1/48/4105_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/aligning-segmentations-and-images-using-python/7446">Aligning Segmentations and images using python</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Dear all 
I have a problem to understand how to use Segmentations nrrd file with image files in Python. 
My problem is: 
I’m able to open a stack of images and its segmentations using pynrrd. 
However I can’t understand how to align the segmentation with the stack of images. 
Reading the header of the segmentation I can’t understand how to shift the segmentation to align with the original image. 
The same operation when performed in 3DSlicer is straightforward, and the alignment perfect. 
So, I …
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-12-06 20:10 UTC)

<p>To make things easier, we have made automated segmentation cropping optional. By default, extents of segmentation will match extents of master volume. Cropping can be enabled/disabled in the Save dialog’s additional options section. This feature is available in Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #4 by @JoostJM (2019-12-10 06:39 UTC)

<p>Alternatively, you can enable <code>correctMask</code> in the PyRadiomics configuration, which will resample the mask back to the image space.</p>

---
