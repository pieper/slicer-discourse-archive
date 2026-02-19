---
topic_id: 1331
title: "General Registration Brains Descriptors Or Features Used To"
date: 2017-10-31
url: https://discourse.slicer.org/t/1331
---

# General Registration (BRAINS) descriptors or features used to make Affine Registration (12 DOF)

**Topic ID**: 1331
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/general-registration-brains-descriptors-or-features-used-to-make-affine-registration-12-dof/1331

---

## Post #1 by @Mohammed_EL_ADOUI (2017-10-31 14:53 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.5.0</p>
<p>Recently, I used 3D slicer to make co-registration between breast tumor images (MRI). I used the General Registration (BRAINS), in which I used the linear transform initialized with “useMomentsAlign”. Then ,I used the flowing registration phases in order : Rigid(6 ODF), Rigid+scale(7 ODF) and Affine(12 DOF).  As results, I have a good registration with the transformation file (.h5) containing the 12 transformations. My question is about the descriptors/features used in this registration, I means what is the operations used to found the 12 unknown variables (12 DOF). I imagine that a comparison between the two inputs images descriptors are made but which features exactly? (is it the shape, intensities …?)</p>

---

## Post #2 by @ihnorton (2017-10-31 14:56 UTC)

<p>(please only post once – the first post must be approved, and usually someone will see it within 1-2 hours)</p>

---

## Post #3 by @pieper (2017-10-31 15:25 UTC)

<p>The module documentation page has lots of information on that:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSFit" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSFit</a></p>

---
