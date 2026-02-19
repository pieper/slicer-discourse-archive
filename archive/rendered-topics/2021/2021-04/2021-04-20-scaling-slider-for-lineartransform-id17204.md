---
topic_id: 17204
title: "Scaling Slider For Lineartransform"
date: 2021-04-20
url: https://discourse.slicer.org/t/17204
---

# Scaling slider for LinearTransform

**Topic ID**: 17204
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/scaling-slider-for-lineartransform/17204

---

## Post #1 by @FriedrichKretschmer (2021-04-20 12:28 UTC)

<p>Dear community,<br>
I am trying to register multiple 2D in-situ images to a 3D CT brain scan. For this purpose I do an initial coarse alignment by a manual linear transform. In a second step I apply landmark registration. I finally use the registered data to segment specific brain areas in the CT scan based on the overlayed in-situ data.</p>
<p>For the first manual alignment it would be very helpful to have an additional “Scaling” slider in the transform module. I currently manually alter the transform matrix for this purpose or use the image spacing parameters from the “volume” module.</p>
<p>I don’t see any technical reason why there should not be a scaling slider in the transformation module.<br>
What am I missing? Thank you in advance!<br>
Fritz</p>

---

## Post #2 by @pieper (2021-04-20 20:20 UTC)

<p>There’s no technical reason except that typically only rigid registration is used for most volumetric registration (since they are already in calibrated units).  But I suppose it wouldn’t hurt to have an advanced checkbox or something that exposes a scale slider.  Could also add shears if people would find it useful.</p>

---

## Post #3 by @FriedrichKretschmer (2021-04-21 07:17 UTC)

<p>Thank you for the fast reply. This would be very helpful indeed!</p>

---

## Post #4 by @pieper (2021-04-21 12:27 UTC)

<p>I’m not sure if anyone has the time to add this, but you can file a feature request <a href="https://github.com/Slicer/Slicer/issues">on the issue tracker</a> and anyone can vote for the feature using the <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  emoji.  This is an example of a good intermediate programming task that would be an excellent learning project for a new developer who wants to learn the C++ side of Slicer (adding this involves making changes to <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Transforms">the Transforms loadable module</a>).</p>
<p>If you just want a more easy way to scale a transform to accelerate your work of course you can add a little script to implement the feature.</p>

---
