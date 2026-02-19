---
topic_id: 6905
title: "Display And Interact With Fiducials In Vr"
date: 2019-05-23
url: https://discourse.slicer.org/t/6905
---

# Display and interact with fiducials in VR

**Topic ID**: 6905
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/display-and-interact-with-fiducials-in-vr/6905

---

## Post #1 by @drouin-simon (2019-05-23 18:57 UTC)

<p>Hi,</p>
<p>Is it possible to show and interact with markup fiducials in VR?</p>

---

## Post #2 by @lassoan (2019-05-23 19:29 UTC)

<p>This feature should be available within a few weeks (<a class="mention" href="/u/cpinter">@cpinter</a> is working on it).</p>

---

## Post #3 by @TinaNant28 (2025-02-27 21:26 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/cpinter">@cpinter</a><br>
I have tested the feature for displaying and interacting with markup fiducials in VR, but I still cannot interact with them. Is there a specific version or update I should install? Or are there particular settings that need to be enabled in the VR environment?</p>
<p>I use MetaQuest3, Slicer 5.6.2</p>
<p>Thanks in advance for your help!</p>

---

## Post #4 by @cpinter (2025-02-28 12:27 UTC)

<p>Funding for VR/AR has been pretty scarce in the past years unfortunately, and the majority went toward OpenXR support to make SlicerVR (and other VTK based XR apps) future-proof, in the light of the older OpenVR backend being phased out.</p>
<p>There have been other funded initiatives (in-VR widget, collaborative feature, etc), probably the Kitware folks can give you more details, but as far as I know none of them are in an advanced state yet.</p>
<p>In particular the above feature that I was going to work on never actually got finished or integrated, as well as some other small projects I did in the spirit of proving that they can be done (like <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerVRInteraction/">this in-VR widget project</a>).</p>
<p>The current reality is that only such features and improvements are done in the XR topic that are directly funded by some driving use case.</p>

---
