---
topic_id: 38494
title: "Question On 3D Rendering In Slicer"
date: 2024-09-23
url: https://discourse.slicer.org/t/38494
---

# Question on 3D rendering in Slicer

**Topic ID**: 38494
**Date**: 2024-09-23
**URL**: https://discourse.slicer.org/t/question-on-3d-rendering-in-slicer/38494

---

## Post #1 by @alientex (2024-09-23 09:46 UTC)

<p>Hello all,</p>
<p>I am aware that Slicer uses the VTK library for rendering. I have read a few sources on the internet that describe how VTK uses the OpenGL graphics library by default. Therefore, I believe there is no doubt that VTK uses the OpenGL renderer.</p>
<p>My question is: Is it possible for Slicer to enable VTK to use the Direct3D renderer? I am not suggesting completely replacing OpenGL with Direct3D, as Direct3D is Windows-oriented, but rather allowing users to choose between OpenGL and Direct3D for rendering.</p>
<p>Additionally, I believe Slicer should have a dedicated 3D settings option in its configuration for rendering and visualization. This could include various options related to rendering. I think this is an interesting topic to consider in Slicer.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2024-09-23 13:11 UTC)

<p>That would be a pretty significant change, and many parts of Slicer are closely tied to the parts of VTK that rely heavily on OpenGL (e.g. volume rendering, interactive 3d widgets, etc).  But the data in Slicer can be exported to other renderers if you want to do other things, like render with shadows or custom shaders.</p>

---

## Post #3 by @alientex (2024-09-24 06:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="38494">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But the data in Slicer can be exported to other renderers if you want to do other things, like render with shadows or custom shaders.</p>
</blockquote>
</aside>
<p>My requirement is to use Direct3D for the things you mentioned, such as volume rendering, interactive 3D widgets etc. The data export functionality you mentioned is completely different from my requirements.</p>

---

## Post #4 by @lassoan (2024-09-24 12:13 UTC)

<p><a href="https://discourse.vtk.org/t/vtk-webgpu-native-graphics-apis-on-the-desktop/11550">VTK is adding support for Direct3D/Vulkan/Metal rendering</a> via its new WebGPU backend and Slicer will switch to that when feature parity and stability is comparable with the current OpenGL backend. However, this low-level implementation detail generally should not matter for application developers. What is the reason that you are interested in Direct3D?</p>

---

## Post #5 by @alientex (2024-09-26 12:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38494">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is the reason that you are interested in Direct3D?</p>
</blockquote>
</aside>
<p>OpenGL is no longer being developed, which is why I am looking for alternative libraries.</p>

---

## Post #6 by @lassoan (2024-09-26 12:56 UTC)

<p>VTK provides a higher level API than OpenGL. If you use VTK then you can be sure that your code will run on Windows, macOS, Linux, web, and mobile, without ever having to adapt to low-level, platform-specific APIs.</p>
<p>Currently, under the hood, VTK is adding WebGPU support, which - depending on the underlying platform - uses Direct3D, Metal, and Vulkan. You can already enable the WebGPU backend in VTK and render using Direct3D.</p>
<p>By the way, OpenGL API will be available in the foreseeable future (few decades or so), just its runtime performance, maintenance, etc. cost will gradually increase, so it will become less and less desirable. I would also note that Direct3D is not a very safe bet either. It is entirely possible that it will be replaced by WebGPU or some new API in the years to come. If you want to be isolated from these industry changes then you are better off using higher-level frameworks and not get stuck with one of today’s low-level platform-specific APIs.</p>

---

## Post #7 by @alientex (2024-09-27 04:05 UTC)

<p>Great. Thanks for the explanation. I understand it now.</p>

---
