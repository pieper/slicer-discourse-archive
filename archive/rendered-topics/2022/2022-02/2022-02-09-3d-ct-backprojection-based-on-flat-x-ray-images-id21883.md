# 3D CT Backprojection based on flat X-ray images

**Topic ID**: 21883
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/3d-ct-backprojection-based-on-flat-x-ray-images/21883

---

## Post #1 by @ferhue (2022-02-09 23:18 UTC)

<p>Hello,<br>
I am looking for advice regarding CT reconstruction.</p>
<p>My dataset is made of 360 X-ray images (flat panel) of an object taken in steps of 1 degree. I also know the source to detector distance.</p>
<p>My question if there is a plugin for 3DSlicer to reconstruct a 3D CT image based on these 360 flat X-ray images. (Absolute calibration to HU is not that important, is mostly about the geometry).</p>
<p>If not, do you recommend a good independent code on GitHub to do this?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2022-02-09 23:28 UTC)

<p>We usually suggest RTK: <a href="https://www.openrtk.org/">https://www.openrtk.org/</a></p>

---

## Post #3 by @muratmaga (2022-02-09 23:28 UTC)

<p>Slicer does not do reconstructions from shadow images. You should look into Reconstruction Toolkit (<a href="https://www.openrtk.org/" rel="noopener nofollow ugc">https://www.openrtk.org/</a>)  for that purpose.</p>

---
