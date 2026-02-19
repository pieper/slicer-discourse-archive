---
topic_id: 20193
title: "Creating A Roi Within A Roi Based On Hu"
date: 2021-10-17
url: https://discourse.slicer.org/t/20193
---

# Creating a ROI within a ROI based on HU

**Topic ID**: 20193
**Date**: 2021-10-17
**URL**: https://discourse.slicer.org/t/creating-a-roi-within-a-roi-based-on-hu/20193

---

## Post #1 by @Fabio_Nunes (2021-10-17 17:42 UTC)

<p>Dear members,</p>
<p>I’ve been working on delimiting the pericardial surface of the Heart and I’ve finally been able to do that semi-automatically using a EATSeg tool available on GitHub. This tool creates a ROI encompassing the entire pericardium (+heart inside). I then exported the ROI to 3D Slicer and merged it with the DICOM file, creating the image that I attach bellow. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/719bfe319825cc29421b9e7a36bdfb6fc72452c2.png" data-download-href="/uploads/short-url/gd2anSw46v0CC0OC1KlQIOfXtuO.png?dl=1" title="Imagem1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/719bfe319825cc29421b9e7a36bdfb6fc72452c2_2_690x372.png" alt="Imagem1" data-base62-sha1="gd2anSw46v0CC0OC1KlQIOfXtuO" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/719bfe319825cc29421b9e7a36bdfb6fc72452c2_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/719bfe319825cc29421b9e7a36bdfb6fc72452c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/719bfe319825cc29421b9e7a36bdfb6fc72452c2.png 2x" data-dominant-color="404243"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Imagem1</span><span class="informations">790×427 79.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I am only interested in the pericardial fat, so, what I was wondering was if there was any way to create a ROI within the pericardial ROI containing all the volume of tissue corresponding to adipose tissue (ie, with HU between -150 and -50).</p>
<p>Hopefully someone has dealt with this issue before and could help out<br>
Thank you<br>
Fábio Nunes</p>

---

## Post #2 by @lassoan (2021-10-17 17:57 UTC)

<p>You can achieve this with Threshold effect with masking.</p>
<ul>
<li>Create a new segment</li>
<li>Select Trheshold effect</li>
<li>Set the desired range</li>
<li>In masking section (near the bottom) choose editable area → inside all segments</li>
<li>Click Apply</li>
</ul>
<p>These can be automated easily, by writing a few lines of Python script.</p>
<p>Also note that pericardium segmentation on CT is a relatively easy segmentation task. You can segment it in a minute or so using semi-automatic segmentation tools in the Segment Editor. You can use Surface Cut effect (provided by SegmentEditorExtraEffects extension) to get the surface by clicking on pericardium points. For higher accuracy you can segment 4-5 slices using the Paint or Draw effect and then create the complete segmentation using Fill between slices effect. It would be also easy to make the segmentation fully automatic by training an neural network using MONAILabel extension.</p>

---

## Post #3 by @Fabio_Nunes (2021-10-24 22:36 UTC)

<p>Thank you!<br>
Perfect answer.</p>

---
