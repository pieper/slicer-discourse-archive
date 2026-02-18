# Liver segmentation from CT

**Topic ID**: 6413
**Date**: 2019-04-05
**URL**: https://discourse.slicer.org/t/liver-segmentation-from-ct/6413

---

## Post #1 by @Marco_Festugato (2019-04-05 20:32 UTC)

<p>Hi guys, I’m very new to 3D slicer…I have to segment the liver from 199 DICOM images of the same patient…do u have any example I could use to do this? I cant find much on the internet…<br>
Thank u!</p>

---

## Post #2 by @lassoan (2019-04-05 21:13 UTC)

<p>Do you mean you have a volume that consists of 199 slices? What is the purpose of the segmentation? What structures you would like to obtain?</p>
<p>To get started, you need to learn anatomy of liver and surrounding tissues and how they appear on CT. You should be able to find anatomic atlases and probably even tutorials for liver contouring on the web. There are also data sets with expert liver segmentation that you can learn from.</p>

---

## Post #3 by @Marco_Festugato (2019-04-06 08:40 UTC)

<p>Ty Andras for your kind answer. Yes, I have a volume that consists of 199 dicom slices (axial). My purpose is to segment the liver in these slices and save those 199 slices ONLY with the liver segmented (segmentation doesnt need to be perfect though) in dicom format.</p>

---

## Post #4 by @Marco_Festugato (2019-04-06 09:28 UTC)

<p>I’ve managed to roughly segment the liver <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8424eadd171b36ecac6fce814d2db66b9a682c97.jpeg" data-download-href="/uploads/short-url/iR07wr1o44eLJUfT3aYJw5v1mir.jpeg?dl=1" title="liver" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8424eadd171b36ecac6fce814d2db66b9a682c97_2_690x388.jpeg" alt="liver" data-base62-sha1="iR07wr1o44eLJUfT3aYJw5v1mir" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8424eadd171b36ecac6fce814d2db66b9a682c97_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8424eadd171b36ecac6fce814d2db66b9a682c97_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8424eadd171b36ecac6fce814d2db66b9a682c97_2_1380x776.jpeg 2x" data-dominant-color="A4A69D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">liver</span><span class="informations">1920×1080 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>how can i save the original dicom series in order to ‘‘contain’’ only the liver? So, I started with 199 dicom images and now i want 199 dicom images containing only the segmented liver…thanks in advance!</p>

---

## Post #5 by @lassoan (2019-04-06 13:38 UTC)

<p>Would you like to blank out voxels outside the segment? You can use Mask Volume effect for that (provided by SegmentEditorExtraEffects extension).</p>
<p>You can then export the masked image as a CT image by right-clicking on the image in Data module and choose DICOM export.</p>

---

## Post #6 by @Marco_Festugato (2019-04-06 13:41 UTC)

<p>Thank you again Andras for your kind answer. Yes, I want to keep the segmentation in grey levels and then put everything else to 0 (black). Then, I want to save my 199 segmented slices in DICOM format.</p>

---
