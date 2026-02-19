---
topic_id: 14593
title: "4 11 And 4 10 Show Differences On Loaded Stl Model And Fiduc"
date: 2020-11-14
url: https://discourse.slicer.org/t/14593
---

# 4.11 and 4.10 show differences on loaded STL model and fiducial

**Topic ID**: 14593
**Date**: 2020-11-14
**URL**: https://discourse.slicer.org/t/4-11-and-4-10-show-differences-on-loaded-stl-model-and-fiducial/14593

---

## Post #1 by @Bruce_Wu (2020-11-14 02:40 UTC)

<p>Dear,</p>
<p>I have a dental model (STL file) and a fiducial file (FCSV). In 4.10, all fiducials are on the model. However, in 4.11, the fiducials are in the air instead of on the model. It looks like the model has been transformed, but I didn’t apply any transform on it. Any suggestions?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d978cd3c978b8c9227a685c019c5b9dc566dc865.png" alt="image" data-base62-sha1="v1QqvuMcBCw7fcTAkZKFCURw1RX" width="466" height="376"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d5c90104108fb3eefea6928c302b66c2de50e09.jpeg" data-download-href="/uploads/short-url/ms5hddQ1D4rSHGQFfnacaXEug4x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d5c90104108fb3eefea6928c302b66c2de50e09_2_648x500.jpeg" alt="image" data-base62-sha1="ms5hddQ1D4rSHGQFfnacaXEug4x" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d5c90104108fb3eefea6928c302b66c2de50e09_2_648x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d5c90104108fb3eefea6928c302b66c2de50e09_2_972x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d5c90104108fb3eefea6928c302b66c2de50e09.jpeg 2x" data-dominant-color="9D9D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">976×753 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-14 13:34 UTC)

<p>See explanation why this happens and how to fix here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default</a></p>

---
