---
topic_id: 33765
title: "How To Contribute My Matlab Coding Into 3D Slicer"
date: 2024-01-14
url: https://discourse.slicer.org/t/33765
---

# How to contribute my Matlab coding into 3D Slicer

**Topic ID**: 33765
**Date**: 2024-01-14
**URL**: https://discourse.slicer.org/t/how-to-contribute-my-matlab-coding-into-3d-slicer/33765

---

## Post #1 by @akmal871026 (2024-01-14 09:06 UTC)

<p>Dear All,</p>
<p>I have some code in Matlab syntax. This is about the segmentation tumor on Iodine-131 SPECT imaging.</p>
<p>Anyone know how to contribute my coding into 3D Slicer?</p>
<p>What I meant is I want put into the extension manager.</p>

---

## Post #2 by @mau_igna_06 (2024-01-14 18:15 UTC)

<p>As far as I know you only have two ways:</p>
<ol>
<li>Use <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/MatlabBridge" rel="noopener nofollow ugc">this extension</a> as interface between Slicer and the Matlab script</li>
<li>Port your code to Python and make a normal Python scripted module Slicer extension (maybe you could ask ChatGPT to do it for you)</li>
</ol>
<p>Hope it helps</p>

---

## Post #3 by @lassoan (2024-01-15 05:33 UTC)

<p>I would recommend the second approach (ask ChatGPT or Microsoft Copilot to convert your Matlab functions to Python) to avoid Matlab licensing hassles.</p>

---
