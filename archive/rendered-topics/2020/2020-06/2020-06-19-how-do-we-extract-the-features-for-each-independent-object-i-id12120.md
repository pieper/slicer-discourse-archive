---
topic_id: 12120
title: "How Do We Extract The Features For Each Independent Object I"
date: 2020-06-19
url: https://discourse.slicer.org/t/12120
---

# How do we extract the features for each independent object in an image?

**Topic ID**: 12120
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/how-do-we-extract-the-features-for-each-independent-object-in-an-image/12120

---

## Post #1 by @mozdag (2020-06-19 18:04 UTC)

<p>I have a tissue image and there are around 100 cells in it. I also have the corresponding mask image which includes those 100 cells. How do I calculate the radiomics features for each cell?</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-06-21 14:36 UTC)

<p>Hi <a class="mention" href="/u/mozdag">@mozdag</a></p>
<p>Yes, you can do this using SlicerRadiomics extension module.</p>
<ol>
<li>
<p>Load your tissue image and the corresponding mask as a lablel image in Slicer.</p>
</li>
<li>
<p>In the SlicerRadiomics module, you can then specify your Input Image Volume (tissue image), and Input Regions (your converted labelimage) and then run the module.</p>
</li>
</ol>
<p>HTH<br>
Andinet</p>

---

## Post #3 by @fedorov (2020-06-23 20:18 UTC)

<p>Note that if you want to have features separately for the individual cells, you will need to assign a unique label value for each of the cell segmentations.</p>
<p>You can do this using the “Islands” effect of Segment Editor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b2d5321299142ce03deb20232d187890abe4d89.png" data-download-href="/uploads/short-url/1ASmjE8Ds2MEapeTY3oOQVULDFn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b2d5321299142ce03deb20232d187890abe4d89_2_388x500.png" alt="image" data-base62-sha1="1ASmjE8Ds2MEapeTY3oOQVULDFn" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b2d5321299142ce03deb20232d187890abe4d89_2_388x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b2d5321299142ce03deb20232d187890abe4d89_2_582x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b2d5321299142ce03deb20232d187890abe4d89_2_776x1000.png 2x" data-dominant-color="C5C7C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×1059 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mozdag (2020-06-23 20:46 UTC)

<p>Thank you for your response. I won’t be using the Slicer app. I’ll have to use some library such as connected component:</p>
<p>from cc3d import connected_components<br>
labels_out = connected_components(data_mask)</p>
<p>I believe, labels_out is a set of those ROI regions for each cell? Another point is that my images will be 2D. Have any of you got an idea on this?</p>
<p>I still run this code and got error: Attribute Error; image has no attribute “shape”.</p>

---

## Post #5 by @fedorov (2020-06-23 21:25 UTC)

<p>There are some additional attributes you need to make sure are set, did you check this documentation page: <a href="https://pyradiomics.readthedocs.io/en/latest/features.html#module-radiomics.shape2D">https://pyradiomics.readthedocs.io/en/latest/features.html#module-radiomics.shape2D</a> ?</p>

---

## Post #6 by @JoostJM (2020-06-25 05:45 UTC)

<p>As to splitting connected components and extracting features, check out <a href="https://github.com/Radiomics/pyradiomics/issues/591">this issue</a>, which deals with the same problem.</p>

---
