# Why are my segmentations being saved as only the bounding box size rather than the size of the original image?

**Topic ID**: 9909
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/why-are-my-segmentations-being-saved-as-only-the-bounding-box-size-rather-than-the-size-of-the-original-image/9909

---

## Post #1 by @LisaDuff (2020-01-22 20:37 UTC)

<p>hi<br>
I have made a large amount of segmentations on 3D slicer but when I try to save them they are only the size of the area covered by the segmentation. For example if the segmentation covers 100x40x40 slices it only saves the slices covered rather than the size of the original image. I want to use it as a mask so this is causing issues. I have tried saving straight fromt he segmentation editor as a seg.nrrd file and through the segmentation module by exporting it as a label map. how do I fix this?</p>

---

## Post #2 by @cpinter (2020-01-23 17:59 UTC)

<p>You need to specify a Reference volume if you want a larger extent in your saved file.</p>
<p>See these topics that answer the same question:</p><aside class="quote" data-post="6" data-topic="818">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/output-from-segmentation/818/6">Output from segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you want simpler, then you can export DICOM. Unfortunately the DICOM SEG exporter is currently broke, but very close to fixing, see <a href="https://github.com/QIICR/QuantitativeReporting/issues/140">https://github.com/QIICR/QuantitativeReporting/issues/140</a> 
Exporting the segmentation to the labelmap takes around 8 clicks additinally to the few hundred you made when doing the segmentation. I think it is still much simpler than coming up with an elaborate workaround. If you want to make it quicker you can always write a python script that does that for you.
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="2" data-topic="1580">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-dicom-rtstruct-format-to-nifti-format/1580/2">Convert DICOM-RTSTRUCT format to Nifti format</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer can certainly read DICOM RTSTRUCT and save it as a labelmap in Nifti format. 

By default, when you export a segmentation to a labelmap volume, Slicer uses the smallest necessary image extent, so the input grayscale volume’s geometry will not be the same as labelmap volume’s. If your software requires the grayscale and labelmap volumes to have the exact same geometry then you just need to specify the grayscale volume as reference volume for labelmap export (see Segmentations module Expor…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="1126">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/adjusting-and-saving-binary-labelmaps/1126">Adjusting and saving binary labelmaps</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have cropped ROI volumes that were registered and their segmentations transforms and exported to binary labelmaps. I am trying to save those labelmaps to files that have the same dimensions so that I can create a probabilistic atlas from them. I assumed that the registration and transformation of those segmentations would have constrained the labelmap images to the same dimensions, but I guess I was wrong. Is there a way to shift all of the segmentation labelmaps to have the same number of bin…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="3921">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e9a140/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/conerting-rtstruct-file-to-nrrd-getting-a-meaningful-result-with-correct-dimensions/3921">Conerting RTstruct file to nrrd : Getting a meaningful result with correct dimensions?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: MacOS 
Slicer version: 4.9.0.-2018-08-04 
Expected behavior: Produce nrrd file with 15x512x512x128 dimensions 
Actual behavior: Finding nrrd file with 15x357x211x128 dimensions 
Hi All, 


Would someone be able to post step by step instructions for converting an RTstruct file to an nrrd file? 
I am new to 3dslicer and am finding the program and its UI rather confusing. I believe screenshots would be helpful. 


I tried to follow the question <a href="https://discourse.slicer.org/t/how-can-i-convert-an-rtstruct-to-an-nrrd/539">here</a> and I think that I did it corre…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-01-23 18:50 UTC)

<p>Also note that in recent Slicer Preview Releases we save the entire segmentation region by default (crop to segmented region is an option in Save data dialog). This way, more memory and disk space is used but the saved file is compatible with software that rely on having exact match of image extents with the master volume.</p>

---

## Post #4 by @LisaDuff (2020-02-11 14:41 UTC)

<p>Thank you, since I am on a work laptop I can’t use preview releases at the moment but I will keep it in mind if I get the chance to change.</p>

---

## Post #5 by @LisaDuff (2020-02-11 14:46 UTC)

<p>Thank you. I didn’t realise there was another reference volume section in the advanced part of the segmentations module. I was relying on the segmentation editor master geometry.</p>

---

## Post #6 by @lassoan (2020-06-24 15:34 UTC)

<p>4 posts were split to a new topic: <a href="/t/how-to-get-segmentations-as-numpy-arrays-with-same-dimensions/12202">How to get segmentations as numpy arrays with same dimensions?</a></p>

---
