---
topic_id: 30468
title: "Ability To Generate A Mean Projection Image Using Only Selec"
date: 2023-07-09
url: https://discourse.slicer.org/t/30468
---

# Ability to Generate a Mean Projection Image Using only Selected Slices Based on Fiducial Markups

**Topic ID**: 30468
**Date**: 2023-07-09
**URL**: https://discourse.slicer.org/t/ability-to-generate-a-mean-projection-image-using-only-selected-slices-based-on-fiducial-markups/30468

---

## Post #1 by @Bethrg (2023-07-09 07:17 UTC)

<p>Hello,</p>
<p>I need to markup many landmarks on head MRIs with the intent for them to be used like a lateral ceph radiograph is currently used for orthodontic treatment planning.</p>
<p>I can visualize/place the markers on the MRI scans in the individuals panes, but when I go to condense the images into a single 2D-image, I lose the anatomical detail of landmarks I need. I can scroll through the stack and see them, but the goal is to have a single 2D image to analyze. I’ve played around with the code to get the mean projection image (slab numbers/slice thickness) based on code Andras provided in another post, and I’ve adjusted contrasts, etc, but the image is still too ill-defined.</p>
<p>Is there a way I can combine the image slices specifically around my fiducials into one mean projection image and ignore the other slices? I think that may sharpen the landmarks I need to see.  I’m also open to other ideas/ways to improve the image quality.</p>
<p>For reference, code from Andras for mean projection image generation:<br>
sliceLogic = appLogic.GetSliceLogic(sliceNode)<br>
sliceLayerLogic = sliceLogic.GetBackgroundLayer()<br>
reslice = sliceLayerLogic.GetReslice()<br>
reslice.SetSlabModeToMax()<br>
reslice.SetSlabNumberOfSlices(500)<br>
reslice.SetSlabSliceSpacingFraction(0.1)<br>
sliceNode.Modified()</p>
<p>Picture from internet showing what a lateral ceph for ortho treatment planning looks like and what I am trying to obtain similarity to (with the understanding the colors/bone will be inverted):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/273ed0d338b139cdd0e29f0cd698ff58f2097c75.jpeg" data-download-href="/uploads/short-url/5BbcBV5yA1PUEmxdi5fYGeCX4tn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273ed0d338b139cdd0e29f0cd698ff58f2097c75_2_570x500.jpeg" alt="image" data-base62-sha1="5BbcBV5yA1PUEmxdi5fYGeCX4tn" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273ed0d338b139cdd0e29f0cd698ff58f2097c75_2_570x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/273ed0d338b139cdd0e29f0cd698ff58f2097c75.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/273ed0d338b139cdd0e29f0cd698ff58f2097c75.jpeg 2x" data-dominant-color="84898A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×626 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(Taken from: Durão, Ana &amp; Morosolli, Aline &amp; Pittayapat, Pisha &amp; Bolstad, Napat &amp; Pinhão Ferreira, Afonso &amp; Jacobs, Reinhilde. (2015). Cephalometric landmark variability among orthodontists and dentomaxillofacial radiologists: A comparative study. Imaging Science in Dentistry. 45. 213. 10.5624/isd.2015.45.4.213. )</p>
<p>My images. Note: I have many more markers to place - these are just to insure I can get this to work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ef70479bbfded2d76f93e0dffa7414c16fbaa6.jpeg" data-download-href="/uploads/short-url/tXaMJVOSNfUDOyxabbr4DzKIXZk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ef70479bbfded2d76f93e0dffa7414c16fbaa6_2_558x500.jpeg" alt="image" data-base62-sha1="tXaMJVOSNfUDOyxabbr4DzKIXZk" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ef70479bbfded2d76f93e0dffa7414c16fbaa6_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ef70479bbfded2d76f93e0dffa7414c16fbaa6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ef70479bbfded2d76f93e0dffa7414c16fbaa6.jpeg 2x" data-dominant-color="2A2A28"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">612×548 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Close up of the best quality mean projection image I was able to get using the above code<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc4eca84ddc08e80f2b89fcedf4bf7be5d9d33d.png" alt="image" data-base62-sha1="46vhe2vMnBJ49zp4qc7nJiMq1v7" width="351" height="357"></p>
<p>Thanks in advance for your assistance. This community is great!</p>

---
