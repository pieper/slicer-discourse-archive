# 2D Shape features for multiple ROIs in single image

**Topic ID**: 12911
**Date**: 2020-08-09
**URL**: https://discourse.slicer.org/t/2d-shape-features-for-multiple-rois-in-single-image/12911

---

## Post #1 by @kalyani7195 (2020-08-09 01:07 UTC)

<p>Hello Pyradiomics team,<br>
I am currently working on Mammograms from INBreast dataset and each mammogram has multiple calcifications. The mask is white(65535) for ROIs i.e. calcifications and black for the rest of the area. What should I do if I want to compute shape features for each calcification present in an image? Currently, the 2D shape features return a single value of each feature for each image and I am not clear what that value represents.<br>
Thanks for your help,<br>
Kalyani</p>

---

## Post #2 by @timeanddoctor (2020-08-09 14:37 UTC)

<p>Do you mean the radiomic features?</p>
<aside class="quote no-group" data-username="kalyani7195" data-post="1" data-topic="12911">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/51bf81/48.png" class="avatar"> kalyani7195:</div>
<blockquote>
<p>Currently, the 2D shape features return a single value of each feature for each image and I am not clear what that value represents.</p>
</blockquote>
</aside>
<p>Sorry, I am not very clearly for this. Could you explain what’s the result getted from a single 2d picture,and how to get it.</p>

---

## Post #3 by @JoostJM (2020-08-10 05:15 UTC)

<p>It is possible, though you need to update the segmentation to do so. What you need to do is to assign a unique label to each lesion, this can be achieved via connected components. In Slicer, this possible using the islands effect in the segment editor. If you are using PyRadiomics as standalone, you need to load the mask yourself, and use SimpleITK’s ConnectedComponentImageFilter. This will yield a new mask (which you can save to disk or directly pass to PyRadiomics, though I recommend the former). Each calcification will then have a unique label  starting at 1. The ObjectCount function yields the total number of lesions in the image.<br>
You can extract featurs for each lesion separately by passing the image, the mask and the corresponding label value (also possible in a batch using a csv file)</p>

---
