---
topic_id: 35474
title: "Non Rigid Registration Of Breast Mri In Prone Position To Br"
date: 2024-04-13
url: https://discourse.slicer.org/t/35474
---

# Non-rigid registration of breast MRI in prone position to breast CT in supine position

**Topic ID**: 35474
**Date**: 2024-04-13
**URL**: https://discourse.slicer.org/t/non-rigid-registration-of-breast-mri-in-prone-position-to-breast-ct-in-supine-position/35474

---

## Post #1 by @DAT_Minh (2024-04-13 12:37 UTC)

<p>Hello everyone. In breast cancer diagnosis, patients undergo breast MRI in a prone position. However, the surgery is conducted in a supine position. Due to gravity, the breast deforms from the prone to the supine position, causing the position of the tumor in the MRI not to align with its position during surgery. Surgeons often find it difficult to locate the tumor. This paper proposes a method to conduct non-rigid registration using large deformation diffeomorphic metric mapping and B-spline registration based on surface landmarks to predict the tumor’s location in the surgical position (supine). I have some questions:<br>
1/ Do we have large deformation diffeomorphic metric mapping extension?<br>
2/ Do SlicerElastix and other registration extensions perform non-rigid registration automatically?<br>
3/ If not, what specific parameters do I need to adjust to achieve non-rigid registration. Thank you.<br>
Here is the link to the paper: <a href="https://ieeexplore.ieee.org/document/9956838" class="inline-onebox" rel="noopener nofollow ugc">Breast Tumor Localization by Prone to Supine Landmark Driven Registration for Surgical Planning | IEEE Journals &amp; Magazine | IEEE Xplore</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29f6577a5d6da4fb211217f8c4108fc6f2773f3.jpeg" alt="Picture1" data-base62-sha1="u3fLYVnBe3wsx7VbXtYF7oiqCIz" width="624" height="333"></p>

---

## Post #2 by @pieper (2024-04-13 17:15 UTC)

<p>Maybe you can contact the authors directly.  Several of them are long-time Slicer researchers and maybe they plan to make an extension from this technique.</p>

---

## Post #3 by @DAT_Minh (2024-04-14 03:31 UTC)

<p>Thank you. I’ve sent them email. Hope to get replies soon. As far as I know, there are some softwares that offer large deformation diffeomorphic metric mapping tool such as ANTs (Advanced Normalization Tools), Deformetrica, DiffeoMap, ITK (Insight Segmentation and Registration Toolkit) but they look complicated.</p>

---
