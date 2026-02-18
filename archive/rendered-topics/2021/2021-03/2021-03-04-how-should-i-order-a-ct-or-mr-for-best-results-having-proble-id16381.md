# How should I order a CT or MR for Best results? Having problems with multiple series when loading to 3D Slicer

**Topic ID**: 16381
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/how-should-i-order-a-ct-or-mr-for-best-results-having-problems-with-multiple-series-when-loading-to-3d-slicer/16381

---

## Post #1 by @chedepablo (2021-03-04 22:07 UTC)

<p>Hello!</p>
<p>I’m new at 3D slicer and I want to basically create Anatomical Models for research and training development (segmentation and 3D printing). I have a bunch of MR and CT Studies, each study with a number of series, for example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83d4438c5cbb7c6cefe33c6264ba1e85d8a08711.png" data-download-href="/uploads/short-url/iOdjXctKqXnt7wQBOky5YmDK2Gt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83d4438c5cbb7c6cefe33c6264ba1e85d8a08711.png" alt="image" data-base62-sha1="iOdjXctKqXnt7wQBOky5YmDK2Gt" width="690" height="74" data-dominant-color="324453"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1045×113 4.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I load any of those series it will give me the three planes, let say I choose “Series#401 SAGITAL II”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/588a1935879d3a7de85b2eaa81f6e9f15c8fa183.png" data-download-href="/uploads/short-url/cDfTiTMG27Zoq31pnNEGnN7fByr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/588a1935879d3a7de85b2eaa81f6e9f15c8fa183_2_596x500.png" alt="image" data-base62-sha1="cDfTiTMG27Zoq31pnNEGnN7fByr" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/588a1935879d3a7de85b2eaa81f6e9f15c8fa183_2_596x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/588a1935879d3a7de85b2eaa81f6e9f15c8fa183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/588a1935879d3a7de85b2eaa81f6e9f15c8fa183.png 2x" data-dominant-color="4E4E5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">812×681 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m getting the images, however, shouldn’t the other series “add” to create a better outcome?</p>
<p>So my questions are:</p>
<p>If I’m capable of asking a radiologist technician/provider to create a study what imaging specifications should I ask for?<br>
If I already have the study, like the one in the images, how can I have a more accurate result?<br>
Is the technician mixing the results of the study?</p>
<p>I’m confused, because if I load the three series, it will create different volumes and every volume will have the three planes.</p>
<p>It would love if somebody could help me get some clarity or point me in the right direction.</p>
<p>I appreciate all the help!</p>
<p>Best,</p>
<p>CDP</p>

---

## Post #2 by @pieper (2021-03-04 22:25 UTC)

<p>These ‘sagittal’ and ‘coronal’ series are just pre-computed versions of what Slicer does on the fly by reslicing the axials, so they don’t really add extra information.  Better to only load the original axial (series 2).  The convention used here is not uncommon, where series numbers in the hundreds mean derived or extra data (like the 999 dose report).</p>
<p>In terms of getting the best from the scan, there’s a medically indicated level of dose that is appropriate for the patient, and only the provider radiologist / institution can set that policy.  For a given amount of dose, you can ask that they reconstruct the images at a high slice spacing.  E.g. the you may get a 5mm collimation at a kVp / mAs for a certain table speed, but then you can reconstruct at 1mm and should get better results for 3D than if you interpolated the 5mm slices.  This is not typically done for radiology review since they take time &amp; space plus it’s extra images to look at and they are all very similar, but for 3D purposes they add value.</p>

---
