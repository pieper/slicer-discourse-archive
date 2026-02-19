---
topic_id: 37459
title: "Getting Error While Trying To Load Tracts"
date: 2024-07-18
url: https://discourse.slicer.org/t/37459
---

# Getting error while trying to load tracts

**Topic ID**: 37459
**Date**: 2024-07-18
**URL**: https://discourse.slicer.org/t/getting-error-while-trying-to-load-tracts/37459

---

## Post #1 by @egemen4552 (2024-07-18 22:47 UTC)

<p>Dear SlicerDMRI forum,</p>
<p>I am very new with Slicer and I have been using other MRI tools such as MRtrix, FreeSurfer, DSI studio etc.</p>
<p>I couldnt find a visualization tool better than Slicer and I am trying to visualize a vascular structure with tractography combined together.</p>
<p>But the problem is, whenever I try to load my tractography (generated with either MRtrix or DSI studio) I keep getting error.</p>
<p>What should I do about this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3709594a28dc1511a50672422474fb1ad1a24bca.png" data-download-href="/uploads/short-url/7QSi0UE24o9hqFV6wgt0RfaMPHk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3709594a28dc1511a50672422474fb1ad1a24bca_2_690x368.png" alt="image" data-base62-sha1="7QSi0UE24o9hqFV6wgt0RfaMPHk" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3709594a28dc1511a50672422474fb1ad1a24bca_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3709594a28dc1511a50672422474fb1ad1a24bca_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3709594a28dc1511a50672422474fb1ad1a24bca_2_1380x736.png 2x" data-dominant-color="555566"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×1019 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ljod (2024-10-19 18:38 UTC)

<p>Dear Egemen,<br>
You can employ a converter to change your tracts from tck to vtk format, then load in Slicer.</p>

---
