---
topic_id: 22604
title: "Volume Overlay With Different Dimensions And Resampling"
date: 2022-03-20
url: https://discourse.slicer.org/t/22604
---

# Volume overlay with different dimensions and resampling

**Topic ID**: 22604
**Date**: 2022-03-20
**URL**: https://discourse.slicer.org/t/volume-overlay-with-different-dimensions-and-resampling/22604

---

## Post #1 by @Vinny (2022-03-20 02:10 UTC)

<p>Hi,</p>
<p>I have two MRI volumes (diffusion-weighted and T1-weighted) with different dimensions and voxel sizes from the same scanning session.  The diffusion-weighted image (DWI) series has been processed and registered to the T1w image; the DWI series retains its original dimensions and voxel size.  From the DWI series, fractional anistropy (FA) map and white matter tracts have been generated; the FA map overlays well with the anatomical T1.</p>
<p>Question: I’d like to make some measurements from the outputted tracts to features defined in the anatomical T1, and was wondering if these tracts should be resampled to T1 space.  I’m guessing it is probably not necessary given they exist in the same physical space?</p>
<p>Thanks for your help,</p>
<p>Vinny</p>

---
