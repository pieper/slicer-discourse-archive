---
topic_id: 16102
title: "Setting Lut Window And Level From C Cli Module"
date: 2021-02-20
url: https://discourse.slicer.org/t/16102
---

# Setting LUT/ window and level from C++ CLI module

**Topic ID**: 16102
**Date**: 2021-02-20
**URL**: https://discourse.slicer.org/t/setting-lut-window-and-level-from-c-cli-module/16102

---

## Post #1 by @cold-pac (2021-02-20 02:57 UTC)

<p>Is there any way to set the colors and window/level for a MRML display node produced by a C++ CLI module?</p>
<p>Can I access the MRML scene/vtkMRMLScalarVolumeDisplayNode?</p>
<p>Should I do this by creating a Python CLI module that calls the C++ CLI module and then sets the color of the outputted display node?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2021-02-20 04:19 UTC)

<aside class="quote no-group" data-username="cold-pac" data-post="1" data-topic="16102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cold-pac/48/8593_2.png" class="avatar"> cold-pac:</div>
<blockquote>
<p>Should I do this by creating a Python CLI module that calls the C++ CLI module and then sets the color of the outputted display node?</p>
</blockquote>
</aside>
<p>Exactly. Once you determined a good processing workflow, you can create a Python scripted module that implements that with a simple and convenient GUI.</p>

---
