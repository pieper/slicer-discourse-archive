---
topic_id: 38133
title: "Cannot Open Fusion Images Of Pet"
date: 2024-08-30
url: https://discourse.slicer.org/t/38133
---

# Cannot open fusion images of PET 

**Topic ID**: 38133
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/cannot-open-fusion-images-of-pet/38133

---

## Post #1 by @Emm (2024-08-30 18:26 UTC)

<p>Hey there,</p>
<p>I have the following problem:<br>
I try to open an exam with a native, PET and fusion series. Although the first two open when I try to load the fusion I get two messages:</p>
<p>“606: Unnamed Series [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.”</p>
<p>and  then: Could not load: “606: Unnamed Series as a Scalar Volume”</p>
<p>Any thoughts what can be wrong?</p>

---

## Post #2 by @lassoan (2024-08-30 18:30 UTC)

<p>Fused PET/CT images are usually saved as a set of screenshots (secondary captures). These screenshots usually don’t contain 3D geometry (position and orientation of slices), so you cannot reconstruct a 3D volume. They have low dynamic range (8 bit, RGB color) and the CT and PET information is mixed together in an irreversible way, so no further analysis is possible. I would recommend to get the original PET and CT series and visualize/analyze those.</p>

---

## Post #3 by @pieper (2024-08-30 18:30 UTC)

<p>Probably your fusion images are Secondary Captures (screen grabs) not real 3D data.  You typically would want to load the original CT and attenuation corrected PET to look at them in Slicer.</p>

---
