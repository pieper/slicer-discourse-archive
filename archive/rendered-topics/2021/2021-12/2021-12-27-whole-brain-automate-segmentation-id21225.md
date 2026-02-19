---
topic_id: 21225
title: "Whole Brain Automate Segmentation"
date: 2021-12-27
url: https://discourse.slicer.org/t/21225
---

# Whole brain automate segmentation

**Topic ID**: 21225
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/whole-brain-automate-segmentation/21225

---

## Post #1 by @mahinaz (2021-12-27 02:01 UTC)

<p>Hello . i am using two mri PD images of one patient in 2 consecutive year of his  disease.<br>
i done below steps :</p>
<ol>
<li>i registered two images by General Registration Module ( fixed image was the image of patient in 2012 and moving image was image of patient in 2014)</li>
<li>i applied Median Filter  and i used from this Module for smoothing my images.</li>
<li>i removed skull of brain by Swiss Skull Remove Module.<br>
and now i want to segment whole brain automaticlly specially GM and WM and Basal Ganglia. how should i do this?<br>
more explain:  i used from segment editor module for segmentation but it’s results weren’t satisfactory.</li>
</ol>

---

## Post #2 by @pieper (2021-12-29 00:06 UTC)

<p>I suggest <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a>.  I’ve had good luck with it on a wide variety of scans.  There’s no Slicer extension for it (yet?) but you can run it from the command line and use the results in Slicer.</p>

---

## Post #3 by @mahinaz (2021-12-29 00:17 UTC)

<p>Thanks for your guidness. And how about FSL software? not freesurfer</p>

---

## Post #4 by @pieper (2021-12-29 00:44 UTC)

<p>FSL has good tools too, but I haven’t used them myself.</p>

---

## Post #5 by @mahinaz (2021-12-29 00:59 UTC)

<p>And i think i can import my data from FreeSurfer by FreeSurfer Importer module.right?</p>

---

## Post #6 by @pieper (2021-12-29 04:25 UTC)

<p>Yes, the <a href="https://github.com/PerkLab/SlicerFreeSurfer">SlicerFreeSurfer</a> extension should work well.  But traditional FreeSurfer requires high resolution T1 data, where SynthSeg (which comes from many of the same developers) is robust for different resolutions and contrasts.</p>

---

## Post #7 by @Greydon_Gilmore (2022-01-01 21:14 UTC)

<p>I’ve had some success with Atropos from ANTS (<a href="https://pubmed.ncbi.nlm.nih.gov/21373993/" class="inline-onebox" rel="noopener nofollow ugc">An open source multivariate framework for n-tissue segmentation with evaluation on public data - PubMed</a>).</p>
<p>The segmentation tool from FSL is called FAST (<a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FAST" class="inline-onebox" rel="noopener nofollow ugc">FAST - FslWiki</a>).</p>
<p>If you choose FreeSurfer I suggest looking into FastSurfer (<a href="https://github.com/Deep-MI/FastSurfer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Deep-MI/FastSurfer: PyTorch implementation of FastSurferCNN</a>). segmentation finishes in half the time.</p>

---

## Post #8 by @mahinaz (2022-01-22 19:43 UTC)

<p>thanks. i segmented my images in 6 chapter by fsl. now i want to crop a region very accurately with high accuracy. with which tool in 3dslicer can i do this?<br>
should i do this automaticlly?</p>

---

## Post #9 by @lassoan (2022-01-24 21:11 UTC)

<p>You can use “Crop volume” module crop with an axis-aligned rectangular prism shaped region. You can clip the image using freehand shapes using Segment Editor module. Both performs pixel-perfect cropping: nothing is changed in the image except the cropped regions are removed or blanked out.</p>

---
