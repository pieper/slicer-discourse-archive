# Ukf tractography

**Topic ID**: 2747
**Date**: 2018-05-01
**URL**: https://discourse.slicer.org/t/ukf-tractography/2747

---

## Post #1 by @Jin (2018-05-01 17:46 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.8.0<br>
Expected behavior: DTI Process<br>
Actual behavior: Standard error<br>
The current UKF Tractography is different from the tutorial(4.4)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dd0ddea85b4f48d265b63253002d5e3c68220b1.png" data-download-href="/uploads/short-url/8OQCuFeUnr9NX6hRJeKPhc5WK9b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd0ddea85b4f48d265b63253002d5e3c68220b1_2_690x412.png" alt="image" data-base62-sha1="8OQCuFeUnr9NX6hRJeKPhc5WK9b" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd0ddea85b4f48d265b63253002d5e3c68220b1_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd0ddea85b4f48d265b63253002d5e3c68220b1_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd0ddea85b4f48d265b63253002d5e3c68220b1_2_1380x824.png 2x" data-dominant-color="CACACE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×860 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1788c1b1435d4cdb1ffaf9a1760205a74723f7d7.png" data-download-href="/uploads/short-url/3mbYQUTEsRCFn0aMSYZf7VgvQEL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1788c1b1435d4cdb1ffaf9a1760205a74723f7d7_2_667x500.png" alt="image" data-base62-sha1="3mbYQUTEsRCFn0aMSYZf7VgvQEL" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1788c1b1435d4cdb1ffaf9a1760205a74723f7d7_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1788c1b1435d4cdb1ffaf9a1760205a74723f7d7_2_1000x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1788c1b1435d4cdb1ffaf9a1760205a74723f7d7.png 2x" data-dominant-color="F0E5E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×809 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ihnorton (2018-05-01 19:44 UTC)

<p>Hi <a class="mention" href="/u/jin">@Jin</a>, thanks for the report. The <code>minGA</code> error has already been fixed in the 4.8.1 release, so please download that (or a more recent SlicerPreview build).</p>
<p>We will update the documentation.</p>

---

## Post #3 by @ljod (2018-05-01 20:18 UTC)

<p>Also, here’s an explanation of the change to UKF tractography. We have made this change (removing GA and adding the new parameter of normalized mean signal) to provide a measure that is suitable for both single-shell and multi-shell (multiple b-values) data.</p>

---

## Post #4 by @Jin (2018-05-02 01:14 UTC)

<p>I will try it, thanks very much!</p>

---

## Post #5 by @mnrad22 (2019-03-06 15:42 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.10</p>
<p>Is it possible to set waypoints or endpoints in the UKF tractography module?</p>

---

## Post #6 by @ljod (2019-03-06 16:05 UTC)

<p>Those mainly are used for probabilistic tractography. For UKF, the traditional processing is to seed tractography in a large area or in the whole brain, then select the tracts of interest. You can use regions of interest for selection, and these can correspond to the waypoints or endpoints you are interested in.</p>
<p>If you let us know your overall goal we may have more suggestions to help.</p>

---

## Post #7 by @fpsiddiqui91 (2020-06-01 12:04 UTC)

<p>Hello <a class="mention" href="/u/ljod">@ljod</a></p>
<p>I was wondering if it is possible to perform seeding tractography with seed and endpoint. I am quite aware that streamline tractography needs only the seeding region. However, in my case, I want to add some endpoints as well to explore the tracts starting from one region and end at the specific region. I do have the seeding label and end label.</p>
<p>I am just not sure how to perform region-based stratigraphy. Is ROI selection in the diffusion module helpful? Can you guide me to how to perform this tractography?</p>
<p>Thank you.</p>

---

## Post #8 by @ljod (2020-07-28 13:19 UTC)

<p>I apologize for the late reply. We have tutorials about ROI selection here under Slicer Fiber Bundle Selection:<br>
<a href="http://dmri.slicer.org/docs/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>

---
