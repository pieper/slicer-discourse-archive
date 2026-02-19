---
topic_id: 42314
title: "Tools In Virtual Reality"
date: 2025-03-26
url: https://discourse.slicer.org/t/42314
---

# Tools in Virtual Reality

**Topic ID**: 42314
**Date**: 2025-03-26
**URL**: https://discourse.slicer.org/t/tools-in-virtual-reality/42314

---

## Post #1 by @Larad (2025-03-26 14:21 UTC)

<p>Slicer version: 5.8.1</p>
<p>Hi,</p>
<p>I am new to 3D Slicer and I am exploring the Virtual Reality extension using the HTC Vive Pro 2 headset. I am doing a project about the application of VR in the orthopaedic department in our hospital.</p>
<p>When I press the menu button on the controller, it opens a menu where I can choose “grab mode”, “probe mode” and “clipping mode” (and exit). But is it possible to perform measurements on the segmented model within the VR environment? So not performing the measurement on the desktop and then showing it in the VR environment, but directly in the environment as a tool?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @cpinter (2025-03-27 10:06 UTC)

<p>The in-VR interactions in the current SlicerVR are very limited. It is possible to add measurement and such, but since the infrastructure development is not funded and so probably on hold, the best option would be as a custom scripted solution. We can add this for your hospital if this project allows subcontracts, but otherwise my short answer would be that no, it is not possible.</p>

---

## Post #3 by @Larad (2025-03-31 07:42 UTC)

<p>Thank you for your quick response!</p>
<p>I am going to try to write a script for this function. In the meantime, is it possible to move around measurepoints when they are placed within the VR environment on beforehand on the desktop? I have tried this and the measurepoints turn green when I touch them with the controllers, but I haven’t figured out how to grab them.</p>
<p>I am currently using Slicer version 5.8.1. Is there a difference in updates for the VR environment between versions? What would be the best version to use for the VR environment?</p>

---

## Post #4 by @cpinter (2025-03-31 09:12 UTC)

<aside class="quote no-group" data-username="Larad" data-post="3" data-topic="42314">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/larad/48/78049_2.png" class="avatar"> Larad:</div>
<blockquote>
<p>measurepoints turn green when I touch them with the controllers, but I haven’t figured out how to grab them.</p>
</blockquote>
</aside>
<p>Another feature that is missing, sorry!</p>
<aside class="quote no-group" data-username="Larad" data-post="3" data-topic="42314">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/larad/48/78049_2.png" class="avatar"> Larad:</div>
<blockquote>
<p>I am currently using Slicer version 5.8.1. Is there a difference in updates for the VR environment between versions? What would be the best version to use for the VR environment?</p>
</blockquote>
</aside>
<p>I think the latest is the best. There was a long gap in between working releases (as I remember after 4.10 the first one that had the VR working completely well again was 5.7).</p>

---

## Post #5 by @Larad (2025-04-03 09:07 UTC)

<p>In the YouTube video (" Pedicle screw insertion in virtual reality ") the user is using a feature “dynamic slice view”. How can I activate this feature?</p>

---

## Post #6 by @cpinter (2025-04-03 10:04 UTC)

<aside class="quote no-group" data-username="Larad" data-post="5" data-topic="42314">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/larad/48/78049_2.png" class="avatar"> Larad:</div>
<blockquote>
<p>Pedicle screw insertion in virtual reality</p>
</blockquote>
</aside>
<p>I used the Volume Reslice Driver module from the SlicerIGT extension, setting the transform of the screw as driver.</p>

---
