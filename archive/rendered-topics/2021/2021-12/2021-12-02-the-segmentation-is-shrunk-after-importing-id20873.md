---
topic_id: 20873
title: "The Segmentation Is Shrunk After Importing"
date: 2021-12-02
url: https://discourse.slicer.org/t/20873
---

# The segmentation is shrunk after importing 

**Topic ID**: 20873
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/the-segmentation-is-shrunk-after-importing/20873

---

## Post #1 by @ll688ll (2021-12-02 04:56 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Edit imported segmentation using segment-editor for the whole volume<br>
Actual behavior: The editable area / segmentation dimension is smaller than the master volume dimension</p>
<p>Hello,</p>
<p>I’m working on a lung detection project. I use ML models to identify the lung area and generate masks. To further adjust the masks, I want to load them into 3D slicer and use segment-editor. First, I imported the original CT images as master volume with dimensions 512*512. Then the masks of the same size were imported as segmentations. Both original CT images and masks are loaded as .nii files.</p>
<p>When I try to edit the segmentation with Paint tool, two problems show up.</p>
<ol>
<li>
<p>For the layers with the highlighted regions, the editable area of the segmentation is smaller than the original size (or volume dimensions). The screenshot is attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d7b1bb619022757beb88434858aab10ae311f43.jpeg" data-download-href="/uploads/short-url/hU3rp5gDlMdIotjtaUFdlTlRxOr.jpeg?dl=1" title="Screenshot-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7b1bb619022757beb88434858aab10ae311f43_2_690x374.jpeg" alt="Screenshot-1" data-base62-sha1="hU3rp5gDlMdIotjtaUFdlTlRxOr" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7b1bb619022757beb88434858aab10ae311f43_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7b1bb619022757beb88434858aab10ae311f43_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7b1bb619022757beb88434858aab10ae311f43_2_1380x748.jpeg 2x" data-dominant-color="606260"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-1</span><span class="informations">1920×1042 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>For the layers with no highlighted regions, I can’t paint anything on the segmentation. It’s not editable.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b69e8eb70d53d1e1bf69a0c2e264282aa5b3bc1.jpeg" data-download-href="/uploads/short-url/3UvNKMC97Y0jIaA4wi36Hx7wSbL.jpeg?dl=1" title="Screenshot-2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b69e8eb70d53d1e1bf69a0c2e264282aa5b3bc1_2_690x372.jpeg" alt="Screenshot-2" data-base62-sha1="3UvNKMC97Y0jIaA4wi36Hx7wSbL" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b69e8eb70d53d1e1bf69a0c2e264282aa5b3bc1_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b69e8eb70d53d1e1bf69a0c2e264282aa5b3bc1_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b69e8eb70d53d1e1bf69a0c2e264282aa5b3bc1_2_1380x744.jpeg 2x" data-dominant-color="5F605F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-2</span><span class="informations">1918×1036 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>If you meet the similar problem, please let me know how you fix it.</p>

---

## Post #2 by @lassoan (2021-12-02 05:06 UTC)

<p>Check that the CT and the segmentation has the exact same geometry (origin, spacing, axis directions, and extents). This is hard to do for nifti files, as the header is not human-readable and axis directions are stored redundantly in two different fields and the behavior is practically undefined if both are set. To avoid this, save the images as nrrd files instead and have a look at the headers in a text file viewer. If they are the same then you will be able to load these nrrd files into Slicer correctly. If they are different then you need to fix the software that copies the origin, spacing, axis directions, and extents from the input CT to the segmentation.</p>
<p>Also, as always, if you find any unexpected behavior try if things are any different with the latest Slicer Preview Release.</p>

---

## Post #3 by @pieper (2021-12-02 13:41 UTC)

<p>Whatever code you used to process the CTs has led to a serious corruption, so you shouldn’t expect volumes to line up coorectly.  You can see that that the axial view is upside down (the table is at the top of the image and the chest is pointing down, and that the strip at the top of the scan in sagittal/coronal views does not match the rest of the volume.</p>

---

## Post #4 by @ll688ll (2021-12-02 15:44 UTC)

<p>Thank you for your reply. First, I tried to save both CT and masks into nrrd files. But the problem is not solved. Then I tried to eliminate the data I generated. Here is what I did:</p>
<ol>
<li>
<p>Load the original CT (Dicom file) into 3D slicer and add new segmentation in segment_editor. Save the segmentation into nrrd file. To avoid size change, in the export section, the reference volume is set as master volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c34fd8005f1d95def0affc81525420ab7f9cdc0.jpeg" data-download-href="/uploads/short-url/frf64brHkLLhWFtzfsqRP02l3Fe.jpeg?dl=1" title="Screenshot-7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c34fd8005f1d95def0affc81525420ab7f9cdc0_2_690x374.jpeg" alt="Screenshot-7" data-base62-sha1="frf64brHkLLhWFtzfsqRP02l3Fe" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c34fd8005f1d95def0affc81525420ab7f9cdc0_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c34fd8005f1d95def0affc81525420ab7f9cdc0_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c34fd8005f1d95def0affc81525420ab7f9cdc0_2_1380x748.jpeg 2x" data-dominant-color="4D4E56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-7</span><span class="informations">1920×1043 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Then I use python libraries (pydicom and pynrrd) to check the dimensions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aafacf817790498d7a7b5557197ecabe8e73092.png" data-download-href="/uploads/short-url/3O4NrY4XONzXwY8mmTnQxMnllho.png?dl=1" title="Screenshot-4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aafacf817790498d7a7b5557197ecabe8e73092_2_494x500.png" alt="Screenshot-4" data-base62-sha1="3O4NrY4XONzXwY8mmTnQxMnllho" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aafacf817790498d7a7b5557197ecabe8e73092_2_494x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aafacf817790498d7a7b5557197ecabe8e73092_2_741x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aafacf817790498d7a7b5557197ecabe8e73092.png 2x" data-dominant-color="444546"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-4</span><span class="informations">887×897 76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45dbd5770959350d5af158d0983daaae5606d5f9.png" data-download-href="/uploads/short-url/9XZW70zlPVZA0O5jg4zEr1tRkAF.png?dl=1" title="Screenshot-5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45dbd5770959350d5af158d0983daaae5606d5f9_2_690x52.png" alt="Screenshot-5" data-base62-sha1="9XZW70zlPVZA0O5jg4zEr1tRkAF" width="690" height="52" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45dbd5770959350d5af158d0983daaae5606d5f9_2_690x52.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45dbd5770959350d5af158d0983daaae5606d5f9_2_1035x78.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45dbd5770959350d5af158d0983daaae5606d5f9_2_1380x104.png 2x" data-dominant-color="333637"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-5</span><span class="informations">1785×136 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I load the segmentation file back to 3D slicer again. Then I use segment_editor to paint the mask. The editable area changes as well. Also, for the layer without painting, I still cannot paint anything on it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1207c080d50801969b7919722d6a4308b1fc4ad.jpeg" data-download-href="/uploads/short-url/mZotarjkt2I8Ijga6gGDKPQ9vn7.jpeg?dl=1" title="Screenshot-6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1207c080d50801969b7919722d6a4308b1fc4ad_2_690x373.jpeg" alt="Screenshot-6" data-base62-sha1="mZotarjkt2I8Ijga6gGDKPQ9vn7" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1207c080d50801969b7919722d6a4308b1fc4ad_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1207c080d50801969b7919722d6a4308b1fc4ad_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1207c080d50801969b7919722d6a4308b1fc4ad_2_1380x746.jpeg 2x" data-dominant-color="4D4E55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-6</span><span class="informations">1920×1040 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>

---

## Post #5 by @pieper (2021-12-02 15:53 UTC)

<p>Your CT looks better now.  It’s not clear what you are doing in step 2.  The dicom is a 2D slice but you are trying to work with a 3D volume.  You should probably use the slicerio or pynrrd packages in python to operate on the 3D volumes and make sure the nrrd files you load back into slicer are consistent with what you exported.</p>

---

## Post #6 by @ll688ll (2021-12-02 16:14 UTC)

<p>Hello, I’m not working with 3D volume. The only thing I’m trying to do is to edit the masks. In the first post, it’s one batch of my ML model. I want to load the ct images into 3D slicer and edit the masks. But I don’t know why the masks couldn’t load properly. I guest that the software is trying to save the RAM and reduce the data size.</p>

---

## Post #7 by @lassoan (2021-12-04 15:01 UTC)

<p>DICOM file format is very complex, so if you are not sure how to properly extract and modify slices while preserving their correct physical size, position, and orientation then I would recommend to only work with nrrd files. You can read and write the entire 3D volume as a numpy array and you can very easily access individual slices using numpy indexing.</p>

---
