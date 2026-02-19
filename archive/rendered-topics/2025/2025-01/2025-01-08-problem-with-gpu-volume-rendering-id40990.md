---
topic_id: 40990
title: "Problem With Gpu Volume Rendering"
date: 2025-01-08
url: https://discourse.slicer.org/t/40990
---

# Problem with gpu volume rendering

**Topic ID**: 40990
**Date**: 2025-01-08
**URL**: https://discourse.slicer.org/t/problem-with-gpu-volume-rendering/40990

---

## Post #1 by @bonebiologist (2025-01-08 01:28 UTC)

<p>Hello, I’m working on big (~7GB) file and my GPU won’t render a 3D model. I’ve been waiting ages, but it seems it’s not even processing it. CPU render works fine, but it slows down my unit significantly. I’m working with AMD Radeon RX 7600. I tried every solution I’ve found here, centering the view doesn’t help either. Is there a way to fix this?</p>

---

## Post #2 by @muratmaga (2025-01-08 01:35 UTC)

<p>This comes up often with AMD gpus. For volume rendering to work, you need there are two requirements:</p>
<ol>
<li>Your volume size should fit into your GPUs texture memory. and that specific card seems to have 8GB of VRAM, so it should be fine.</li>
<li>The largest dimension of your volume should be equal or less than the 3D Max Texture Size specified by your graphics card and its driver. Unfortunately, for AMD GPUs, this is rather low at 2K (2048). So if one of your dimensions is larger than 2048 voxels, your card will not display the 3D volume.</li>
</ol>

---

## Post #3 by @chir.set (2025-01-08 14:38 UTC)

<aside class="quote no-group" data-username="bonebiologist" data-post="1" data-topic="40990">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bonebiologist/48/79043_2.png" class="avatar"> bonebiologist:</div>
<blockquote>
<p>Is there a way to fix this?</p>
</blockquote>
</aside>
<p>Try to cast your volume to ‘short’, it often helps to render big volumes.</p>

---

## Post #4 by @chir.set (2025-01-08 14:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="40990">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>this is rather low at 2K (2048)</p>
</blockquote>
</aside>
<p>It’s <a href="https://opengl.gpuinfo.org/listreports?sortby=date_desc" rel="noopener nofollow ugc">8196</a> for the Rx 7600 on Windows. There are nvidia cards with low values for this parameter also.</p>

---

## Post #5 by @bonebiologist (2025-01-08 15:05 UTC)

<p>Thank you, this seems to be a solution for me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
