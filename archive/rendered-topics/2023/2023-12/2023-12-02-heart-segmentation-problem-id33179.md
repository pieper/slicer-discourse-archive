# Heart segmentation problem

**Topic ID**: 33179
**Date**: 2023-12-02
**URL**: https://discourse.slicer.org/t/heart-segmentation-problem/33179

---

## Post #1 by @Isabel_Smith (2023-12-02 13:19 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.4.0.<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi! I am having trouble with replicating this segmentation of the heart:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8841876a1b624c7ab8424311a29e9bce8c69cb97.jpeg" data-download-href="/uploads/short-url/jrnkwT4LUagHGwMsQpcBLCmKMGX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8841876a1b624c7ab8424311a29e9bce8c69cb97_2_690x314.jpeg" alt="image" data-base62-sha1="jrnkwT4LUagHGwMsQpcBLCmKMGX" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8841876a1b624c7ab8424311a29e9bce8c69cb97_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8841876a1b624c7ab8424311a29e9bce8c69cb97_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8841876a1b624c7ab8424311a29e9bce8c69cb97_2_1380x628.jpeg 2x" data-dominant-color="96959C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×875 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to segment this sample (below picture) like this as well, but so far I couldn’t. If you could help me with the process, I would be grateful!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bfccc630c0433900de01b839d62cdbd46e4e73b.jpeg" data-download-href="/uploads/short-url/fpiHRb8NCH9bYUNzljB6jdj37Rh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfccc630c0433900de01b839d62cdbd46e4e73b_2_690x307.jpeg" alt="image" data-base62-sha1="fpiHRb8NCH9bYUNzljB6jdj37Rh" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfccc630c0433900de01b839d62cdbd46e4e73b_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfccc630c0433900de01b839d62cdbd46e4e73b_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfccc630c0433900de01b839d62cdbd46e4e73b_2_1380x614.jpeg 2x" data-dominant-color="98999F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×853 311 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!<br>
Esther</p>

---

## Post #2 by @lassoan (2023-12-03 01:58 UTC)

<p>There does not seem to be a visible difference between the heart muscle regions, so you need to manually separate them. You can start with Threshold effect, specify the intensity range that highlights the myocardium, and click “Use for masking”. You can then try to segment a few axial slices and then use “Fill between slices” to create a 3D segmentation from them. You can also <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">use Scissors effect to split a segment into parts</a>.</p>

---

## Post #3 by @Isabel_Smith (2023-12-03 16:27 UTC)

<p>Thank you! I was able to do this way.</p>

---
