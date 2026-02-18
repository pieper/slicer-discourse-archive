# Transform CT mask to MR

**Topic ID**: 33063
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/transform-ct-mask-to-mr/33063

---

## Post #1 by @Walid_D (2023-11-27 15:46 UTC)

<p>Hey,</p>
<p>I am new to the 3D Slicer, I have CT and MR images of the same patient, the segmentation for the tumor mask is only done on the CT, how can I transform the mask to be used on MR images?</p>

---

## Post #2 by @muratmaga (2023-11-27 17:10 UTC)

<p>You have to register the MR to CT rigidly so that it is in the same space as CT. Then you can apply the mask to MR.</p>
<p>You can use Brain Registration or Elastix (separate extension) to do this.</p>

---

## Post #3 by @Walid_D (2023-11-29 12:45 UTC)

<p>Okay, thank you very much.</p>

---
