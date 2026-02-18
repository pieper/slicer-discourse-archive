# Can I extract only 1 slice from 3d input (use 2d param)

**Topic ID**: 21587
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/can-i-extract-only-1-slice-from-3d-input-use-2d-param/21587

---

## Post #1 by @Napat_Ritlumlert (2022-01-24 02:47 UTC)

<p>I have 3d image as a Dicom file which I want to extract radiomics only 1 image cut like a 2d extraction. When segment it on 1 cut of image series and save the image out as nrrd file its come all of the series and cannot use pyradiomics extract as a 2d approaches.</p>

---

## Post #2 by @JoostJM (2022-01-24 09:41 UTC)

<p>I’m not sure if I completely understand your question, but it is possible to extract features from a single segmented slice in a 3D volume. If you load the volume and only segment one slice, then feed it into PyRadiomics, only features from that slice will be computed.</p>
<p>If you also want the shape features to represent the fact that you’ve segmented only 1 slice, enable shape2D instead of shape, and set <code>force2DDimension</code> to your slice dimension (z = 0, y = 1 and x = 2). Be aware that the x, y and z are relative to the image acquisition plane, which is not necessarily identical to the patient plane.</p>

---
