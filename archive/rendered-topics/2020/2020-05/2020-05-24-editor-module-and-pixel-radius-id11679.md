# Editor module and pixel radius

**Topic ID**: 11679
**Date**: 2020-05-24
**URL**: https://discourse.slicer.org/t/editor-module-and-pixel-radius/11679

---

## Post #1 by @aileeno (2020-05-24 14:35 UTC)

<p>Hi everyone,</p>
<p>A colleague and I are working on a project where we want to do repeated measurements on images acquired by different scanners. In an effort to hold as many variables constant as is possible, we have noted that the scanners produce images of differing matrix sizes (e.g. 256 x 256 versus 512 x 512). I was planning to use a standard radius on the paint function e.g. 10 mm but have also noted that there is an option to select, for example, 10 px and I am wondering if that is the more correct way to do this, in order to minimize differences caused by matrix size? Any advice would be much appreciated.</p>

---

## Post #2 by @lassoan (2020-05-24 14:39 UTC)

<p>You can use any brush size, it should not affect measurements.</p>
<p>Are you using Segment Editor module or the legacy Editor module?</p>
<p>What are you segmenting and what measurements do you perform?</p>

---

## Post #3 by @aileeno (2020-05-24 14:54 UTC)

<p>I am using the legacy Editor module.</p>
<p>My question is whether using a standard pixel selection will account for differences in matrix size?</p>
<p>When discussing our project design plan, we felt that using a standard 10mm paint ROI would minimize differences between scans (we are doing radiomics feature analysis) but realized that not all of the CT matrices are the same, introducing some variability.</p>

---

## Post #4 by @lassoan (2020-05-24 15:41 UTC)

<p>In Slicer, all data and operations are defined in physical space and everything is displayed physical space. Radiomics features should not be sensitive to image resolution either. Manual egmentation relies on visual feedback to user, so the result should only depend on physical size.</p>
<p>What do you segment? How do you segment? Just a single click in the middle of a lesion?</p>
<p>The old Editor module has been deprecated for several years and will not be included in the next Slicer release, so I would recommend to switch to Segment Editor module soon.</p>

---
