# How to scale up and down an object imported from STL ?

**Topic ID**: 19517
**Date**: 2021-09-05
**URL**: https://discourse.slicer.org/t/how-to-scale-up-and-down-an-object-imported-from-stl/19517

---

## Post #1 by @mdear (2021-09-05 13:49 UTC)

<p>I am using a David SLS-1 scanner to produce an STL file of a small smooth opaque white tubular medical object (tracheostomy tube). When I take measurements inside slicer  I notice there are some scaling issues. I have figured how to rotate and translate this object in slicer but I have yet to be able to accurately scale up/down the object so it’s virtual measurement matches it’s real world measurement. Suggestions welcome.  We are qualifying some Nobel tubes from Medtronic and it’s important to get this right the first time.</p>

---

## Post #2 by @lassoan (2021-09-05 19:45 UTC)

<p>You can use the “Scale” option in “Surface Toolbox module” to change the size of a model by scaling.</p>

---

## Post #3 by @mdear (2021-09-06 20:29 UTC)

<p>Thanks very much, <a class="mention" href="/u/lassoan">@lassoan</a> .  This appears to work, but I’m seeing some funny interactions between scale and translate.  The original object is scaled, but the translated object that I move around with mouse movements on the 3d viewer remains original size.  Any hints on how I can get that scaled object translated as well?</p>

---

## Post #4 by @lassoan (2021-09-08 04:02 UTC)

<p>After you scale the objects, I would recommend to delete the old unscaled objects from the scene to avoid any confusion. Do the positioning after you have taken care of the scaling.</p>

---
