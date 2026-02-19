---
topic_id: 38526
title: "Monailabel Without 3D Slicer"
date: 2024-09-25
url: https://discourse.slicer.org/t/38526
---

# MONAILabel without 3D Slicer

**Topic ID**: 38526
**Date**: 2024-09-25
**URL**: https://discourse.slicer.org/t/monailabel-without-3d-slicer/38526

---

## Post #1 by @h_z1 (2024-09-25 00:43 UTC)

<p>Hello everyone,<br>
I was wondering if it is possible to use MONAILabel inference without having the 3D Slicer application installed. Currently I have the extension working well for segmentation from the radiology sample app using the command “Slicer.exe --python-script  --no-splash --no-main-window” however I am trying to find a way to get my inference running without needing to have Slicer installed (just using python or other libraries). I have tried looking into the code for MONAILabel for Slicer plugin and monailabel library, but haven’t found out a way to do it.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-09-25 00:53 UTC)

<aside class="quote no-group" data-username="h_z1" data-post="1" data-topic="38526">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> h_z1:</div>
<blockquote>
<p>if it is possible to use MONAILabel inference without having the 3D Slicer application installed</p>
</blockquote>
</aside>
<p>Yes, sure. Slicer application is portable, so you don’t need to install it. You can just copy the folder of files anywhere and run it.</p>
<aside class="quote no-group" data-username="h_z1" data-post="1" data-topic="38526">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> h_z1:</div>
<blockquote>
<p>I am trying to find a way to get my inference running without needing to have Slicer installed (just using python or other libraries)</p>
</blockquote>
</aside>
<p>Size of Pytorch and other required Python libraries are about 7GB. Slicer size is 1GB, so if you find the Slicer distribution easier to use then it makes sense to use it. But of course if you don’t need anything from Slicer or its packaging then you can set up MONAILabel inference independently. You can ask on MONAILabel forum for details.</p>

---
