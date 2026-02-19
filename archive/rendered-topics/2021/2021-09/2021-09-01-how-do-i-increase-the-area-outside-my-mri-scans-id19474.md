---
topic_id: 19474
title: "How Do I Increase The Area Outside My Mri Scans"
date: 2021-09-01
url: https://discourse.slicer.org/t/19474
---

# How do I increase the area outside my mri scans?

**Topic ID**: 19474
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/how-do-i-increase-the-area-outside-my-mri-scans/19474

---

## Post #1 by @akshay_pillai (2021-09-01 20:38 UTC)

<p>I want to create a sphere in front of my mri scans in 3d but the space outside the scans is very less I need to increase this space to obtain a sphere. How do I increase the boundary size in the mri scans for both 3d and slice views? Is there any way to do this?</p>

---

## Post #2 by @mikebind (2021-09-01 21:37 UTC)

<p>You can use the “Crop Volume” module to extend your image volumes. Choose your MRI volume as the “Input Volume”, click so that the eye icon is open by “Display ROI”, and click “Fit to Volume” button. In the 3D view, you should see a cube with colored dots on each face. This cube encloses the image volume which will be produced, and you can expand it by clicking on the colored dots and dragging them outward.  The colored dots will also show in the slicer views and can be dragged there if that is easier.  Decide if you want to create a new volume or overwrite an existing volume and make the appropriate selection in “Output Volume”.  Then click the “Apply” button.  You can look through the “Advanced” section to see what else is possible, but changes there are optional. You can preview the dimensions and resolution of the input and output volumes in the “Volume information” section.</p>

---
