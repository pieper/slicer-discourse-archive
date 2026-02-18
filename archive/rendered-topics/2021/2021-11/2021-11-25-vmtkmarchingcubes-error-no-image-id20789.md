# Vmtkmarchingcubes error No Image

**Topic ID**: 20789
**Date**: 2021-11-25
**URL**: https://discourse.slicer.org/t/vmtkmarchingcubes-error-no-image/20789

---

## Post #1 by @Lottep (2021-11-25 15:04 UTC)

<p>Hello everyone,</p>
<p>I am a new user of VMTK and I have finished multiple tutorials to get familiar with the software. Now I wanted to use VMTK for my own data, I have read in the dcm file and performed levelsetsegmentation. After this I wanted to use marchingcubes but it shows the error: no image. Is there anyone who knows what possible has been going wrong?</p>
<p>Kind regards,</p>
<p>Lotte</p>

---

## Post #2 by @lassoan (2021-11-26 03:57 UTC)

<p>What is your end goal? Would you like to extract vessel centerline, quantify geometry, run CFD simulations, …?</p>

---

## Post #3 by @Lottep (2021-11-26 06:59 UTC)

<p>My end goal is to obtain the geometry to use in Ansys for running CFD simulations.</p>

---

## Post #4 by @lassoan (2021-11-26 14:49 UTC)

<p>OK. In this case, the first step is segmentation. For this, I’ve found that VMTK can automate segmentation of simple cases (large and/or well contrasted vessels), but these are trivially easy to segment using basically any of the automated segmentation tools in Segment Editor in Slicer (Grow from seeds, Local thresholding, Fast marching, etc.). For harder problems, you need to use a combination of interactive segmentation tools anyway (again, available in the Segment Editor).</p>
<p>VMTK has some useful features for CFD mesh generation, such as adding inlet/outlet extensions (but this can be probably more easily achieved using Segment Editor’s Draw tube effect) and adding layers of smaller elements at the the boundary.</p>

---

## Post #5 by @Lottep (2021-11-26 17:40 UTC)

<p>Thankyou for your help and quick reply!</p>

---
