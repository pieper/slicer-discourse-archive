---
topic_id: 41525
title: "Hololens 2 To See The 3D View"
date: 2025-02-06
url: https://discourse.slicer.org/t/41525
---

# Hololens 2 to see the 3D view

**Topic ID**: 41525
**Date**: 2025-02-06
**URL**: https://discourse.slicer.org/t/hololens-2-to-see-the-3d-view/41525

---

## Post #1 by @PaoloZaffino (2025-02-06 09:50 UTC)

<p>Hi,<br>
I tried to connect my hololens 2 to Slicer (just to see the 3d rendering in the visor, no interaction) and I had no luck.</p>
<p>I tried on a Windows 10 machine (equipped with an NVIDIA GeForce GTX 1050Ti), Slicer 5.8, and openXR installed.</p>
<p>I put the visor IP and then it crashes.</p>
<p>Any idea/suggestion?<br>
Any tested configuration to try?</p>
<p>Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @LucasGandel (2025-02-10 07:02 UTC)

<p>Hi Paolo,</p>
<p>Last time I tried it was working fine with Slicer 5.7 IIRC. Do you get any error message in Slicer before the crash, or do you see any error message in the Holographic Remoting Player app that is running in your Hololens?</p>

---

## Post #3 by @PaoloZaffino (2025-04-07 14:14 UTC)

<p>Hi <a class="mention" href="/u/lucasgandel">@LucasGandel</a><br>
sorry for the delay.</p>
<p>Do you have any guide/tutorial?</p>
<p>We are trying to connect it on Windows 10, Slicer (5.7.0, 5.8.0, and 5.8.1), and openXR toolikit installed.<br>
No luck so far…</p>
<p>Thanks.<br>
Paolo</p>

---

## Post #4 by @LucasGandel (2025-04-11 13:30 UTC)

<p>You don’t need the OpenXR toolkit to be installed, SlicerVR should provide all the required dlls. SlicerVR uses version 2.9.3 of OpenXRRemoting, make sure you are using the same version for the player in your Hololens</p>

---
