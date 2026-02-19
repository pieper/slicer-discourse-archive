---
topic_id: 749
title: "Landmark Registration Wont Allow Selection Of Point In Coron"
date: 2017-07-23
url: https://discourse.slicer.org/t/749
---

# Landmark registration won't allow selection of point in Coronal or Axial view, but allows it in Saggital

**Topic ID**: 749
**Date**: 2017-07-23
**URL**: https://discourse.slicer.org/t/landmark-registration-wont-allow-selection-of-point-in-coronal-or-axial-view-but-allows-it-in-saggital/749

---

## Post #1 by @aharris (2017-07-23 16:22 UTC)

<p>Hi,<br>
I’m currently trying to do a landmark transform on a 3D image to compare the time it takes me to do this with my automated pipeline in ITK.  The problem I’m having is moving the selected point in the moving image to match it with the fixed image, currently Slicer won’t allow the finger tool to appear over top of the point in the Axial or Coronal view of the Moving Image portion of the window, and instead things I’m trying to do a window/level adjustment when I’m trying to click and drag the point to its corresponding location.  Any assistance would be appreciated.</p>

---

## Post #2 by @lassoan (2017-07-23 16:35 UTC)

<p>It should be possible to move the fiducials in any view. Which module do you use?</p>
<p>In the latest nightly version you can go to Volumes module and lock window/level to avoid changing it unintentionally.</p>

---
