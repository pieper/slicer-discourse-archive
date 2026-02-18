# Coronary centerline extraction problem 

**Topic ID**: 14415
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/coronary-centerline-extraction-problem/14415

---

## Post #1 by @yuyang (2020-11-04 04:41 UTC)

<p>Hi all，</p>
<p>I am working on extraction cardiovascular centerline from CT images using VMTK following the instructions of <a href="https://www.slicer.org/wiki/Modules:VMTK_in_3D_Slicer_Tutorial:_Coronary_Artery_Centerline_Extraction" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Modules:VMTK_in_3D_Slicer_Tutorial:_Coronary_Artery_Centerline_Extraction</a>.</p>
<p>Vesselness filtering works well. But when switch to “level set segmentation” module, a critical error occurred and the start button in the bottom was disabled.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e90738ab1ae95120a0aab8be4291885ecb3d502d.png" data-download-href="/uploads/short-url/xfsIMyr9VRLmBLtzZC1vJwzIyNT.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e90738ab1ae95120a0aab8be4291885ecb3d502d.png" alt="1" data-base62-sha1="xfsIMyr9VRLmBLtzZC1vJwzIyNT" width="690" height="393" data-dominant-color="DEE7F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">751×428 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It was able to show the segmented vessel by “Preview” and was able to see created levelsetsegmentation model in “centerline computation” moduel, but the program will crush when start the computation.</p>
<p>I have tried to change slicer version, but the problem remains (4.11 stable version and 4.13 nightly version).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cec7da09ea7a089e6b868bd6be18eb7d62b7db9.png" data-download-href="/uploads/short-url/aYuXWq6IJcvdRbybsrCTdYcPNTX.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cec7da09ea7a089e6b868bd6be18eb7d62b7db9_2_690x358.png" alt="3" data-base62-sha1="aYuXWq6IJcvdRbybsrCTdYcPNTX" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cec7da09ea7a089e6b868bd6be18eb7d62b7db9_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cec7da09ea7a089e6b868bd6be18eb7d62b7db9_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cec7da09ea7a089e6b868bd6be18eb7d62b7db9_2_1380x716.png 2x" data-dominant-color="9895A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1928×1001 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Could anyone provide any suggestions to help me out?<br>
Any feedbacks will be appreciated.</p>

---

## Post #2 by @lassoan (2020-11-04 04:49 UTC)

<p>If you extracted centerline then it means that you have already segmented the vessel. What are you trying to segment with level-set segmentation?</p>
<p>I have not found level-set segmentation very robust - it worked for me for very large vessel and short coronary segments with good contrast. However, these are so easy segmentation tasks, that you can solve with many more robust tools in Segment Editor module (simple local thresholding, grow from seeds, watershed, local thresholding).</p>
<p>For more challenging segmentation tasks, such as longer, not very well contrasted coronaries, you probably need to use the Segment Editor’s semi-automatic tools.</p>

---
