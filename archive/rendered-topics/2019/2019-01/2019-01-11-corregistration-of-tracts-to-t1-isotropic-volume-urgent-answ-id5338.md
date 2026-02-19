---
topic_id: 5338
title: "Corregistration Of Tracts To T1 Isotropic Volume Urgent Answ"
date: 2019-01-11
url: https://discourse.slicer.org/t/5338
---

# corregistration of tracts to T1 isotropic volume (urgent answer please)

**Topic ID**: 5338
**Date**: 2019-01-11
**URL**: https://discourse.slicer.org/t/corregistration-of-tracts-to-t1-isotropic-volume-urgent-answer-please/5338

---

## Post #1 by @Gonzalo_Rojas_Costa (2019-01-11 22:42 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8<br>
Expected behavior: How can I corregister that tracts to T1 isotropic volume<br>
Actual behavior:  I got the visual tracts with SlicerDMRI and DTIProces.</p>

---

## Post #2 by @ljod (2019-01-11 23:01 UTC)

<p>Hi you can use an FA or baseline image from the DTI, register it to the T1, and apply that registration transform to the tracts. That will put the FA/baseline and tracts all into T1 space. You can save the transform by saving the scene or optionally harden it to modify the tract vtk file (if you need to do that for some reason).</p>

---

## Post #3 by @ljod (2019-01-11 23:04 UTC)

<p>For getting a baseline image or FA see the first few tutorials here<br>
<a href="http://dmri.slicer.org/docs/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>
<p>For image registration within subject use rigid or affine only. There is a lot of information online for registration in slicer or ask again here for more help as needed.</p>

---
