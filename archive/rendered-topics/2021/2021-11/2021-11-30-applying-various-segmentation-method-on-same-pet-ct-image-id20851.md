---
topic_id: 20851
title: "Applying Various Segmentation Method On Same Pet Ct Image"
date: 2021-11-30
url: https://discourse.slicer.org/t/20851
---

# Applying various segmentation method on same PET/CT image

**Topic ID**: 20851
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/applying-various-segmentation-method-on-same-pet-ct-image/20851

---

## Post #1 by @MPhilip (2021-11-30 18:52 UTC)

<p>Operating system:Windows 10 enterprise<br>
Slicer version:Slicer 4.13.0-2021-10-25</p>
<p>Hi,<br>
I would like to know whether it is possible to apply various semi-automated segmentation methods on the same loaded PET-CT image by hiding the segments created by previous methods one by one as shown in the image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08727962e5ebef0be8fa3d39436c23eb82aecd4c.png" data-download-href="/uploads/short-url/1cJ4VICsK0ooIwGMs4bvgsGaXcE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08727962e5ebef0be8fa3d39436c23eb82aecd4c_2_690x167.png" alt="image" data-base62-sha1="1cJ4VICsK0ooIwGMs4bvgsGaXcE" width="690" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08727962e5ebef0be8fa3d39436c23eb82aecd4c_2_690x167.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08727962e5ebef0be8fa3d39436c23eb82aecd4c_2_1035x250.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08727962e5ebef0be8fa3d39436c23eb82aecd4c_2_1380x334.png 2x" data-dominant-color="AFAFAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1781×433 69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Or is there a better way to do this? After segmenting, for further feature extraction using 3D slicer do I have to use the <strong>import/export nodes</strong> or <strong>export to files</strong> option? Or just clicking on the <strong>save button</strong> and saving the segment with a common name  in the .nrrd format helps for further feature extraction?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a831700699ce86d0f7186425349c2ac7cbdce0b.png" alt="image" data-base62-sha1="fcftaTriVkm2zZ9wLDncR1etEX9" width="246" height="82"></p>
<p>Once it is saved/exported how the ‘segment’ with different segmentation methods applied can be loaded to the radiomics module for feature extraction from each of those semi-automatically segmented regions? Does it have to be in the label map format?I would like to know the steps involved.</p>
<p>When I tried to implement this(feature extraction), I got empty tables. Is it actually possible? i.e to try different segmentation methods on the same PET-CT image and save with a common name and extract features from all these segments segmented using different methods?</p>
<p>Any help would be appreciated as I am totally confused with the steps I implement.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @mikebind (2021-12-01 00:37 UTC)

<p>Perhaps easiest would be to have a different segmentation for each approach rather than different segments within a single segmentation. You can change between segmentations (and create new ones and rename them) using the dropdown menu to the right of “Segmentation:” in your screenshot above. I recommend this because some segmentation approaches require multiple segments (e.g. Grow from Seeds) and this could get confusing within a single segmentation approach.  Also, it would be easy to have the results from one approach overwrite the results from another approach unless you were careful about the masking settings. With the results in separate Segmentations you can be sure they can’t inadvertently affect one another.</p>

---

## Post #3 by @MPhilip (2021-12-01 10:14 UTC)

<p>Thanks for your reply and I will try it that way.<br>
Could you please let me know how each segment can be saved so that it can be loaded for further feature extraction? Do I need to export it as a label map or save the segments as .nrrd? Is it possible to get the features from all those different segments(using different segmentation methods) in a single table in one go?</p>
<p>Thank you</p>

---

## Post #4 by @mikebind (2021-12-01 17:53 UTC)

<p>Take a look at the Segment Statistics module. It is capable of making a wide variety of measurements of all segments in a segmentation.  For saving, you can save whole segmentations from Slicer as <code>.seg.nrrd</code> files.  If you need to access those from outside Slicer using python, you can use the <code>slicerio</code> package</p>

---

## Post #5 by @MPhilip (2021-12-03 10:54 UTC)

<p>Hi<br>
I tried the grow from seeds segmentation on a PET image and saved the segment as seg.nrrd. But when I switched to the <strong>radiomics</strong> module to calculate features(loaded segmentation.nrrd) as input, I got an empty table. Then I tried converting the segment (from <strong>DICOM module&gt;right clicked on the segmentation node&gt;export visible segments to binary labelmap</strong>) to binary label and in the <strong>radiomics</strong> module I loaded the ROI as ‘segementation -tumour-label’ and calculated the features and I could see the features in the new table. Is it always necessary to convert the segmentation to labelmap than just saving it .nrrd?</p>
<p>Also is there a difference between the ‘grow from seeds’ tool in the <strong>segmentation editor</strong> module and ‘<strong>simple region growing method</strong>’ module. I could see seeds have to be defined for <strong>simple region growing method</strong> along with some additional parameters.</p>
<p>Thanks in advance</p>

---

## Post #6 by @mikebind (2021-12-03 17:26 UTC)

<p>I’m not familiar with the Radiomics module.  It looks like it might basically be a wrapper for pyradiomics, which looks like it might generally operate on images/labelmaps rather than segmentations (<a href="https://pyradiomics.readthedocs.io/en/latest/features.html" class="inline-onebox">Radiomic Features — pyradiomics v3.0.1.post9+gdfe2c14 documentation</a>), but I don’t really know.</p>
<p>“Simple region growing” is old and deprecated, I would not recommend using it (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/simpleregiongrowingsegmentation.html" class="inline-onebox">Simple Region Growing Segmentation — 3D Slicer documentation</a>)</p>
<p>“Grow from seeds” effect is maintained and recommended (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds" class="inline-onebox">Segment editor — 3D Slicer documentation</a>). It also requires seed regions to start from.</p>
<p>Segmentations can be easily converted to labelmaps (and vice-versa) using the “Segmentations” module, from the “Export/import models and labelmaps” section.</p>
<p>Do you need to calculate features which are only available from the Radiomics module?  Many basic features are available through the Segment Statistics module, which operates on segmentations and would not require conversion to labelmap.</p>

---

## Post #7 by @pieper (2021-12-03 20:43 UTC)

<p>At least with the latest versions of SlicerRadiomics (for quite a while) you can select a Segmentation directly as input.</p>
<p>SlicerRadiomics has quite a few more features available that aren’t in Segment Statistics, so you just need to decide which is better suited to your study.</p>

---

## Post #8 by @MPhilip (2021-12-09 10:40 UTC)

<p>Thanks for the reply. It was helpful.<br>
I need the basic features which can be calculated from the Segment statistics module and from the radiomics module.</p>

---
