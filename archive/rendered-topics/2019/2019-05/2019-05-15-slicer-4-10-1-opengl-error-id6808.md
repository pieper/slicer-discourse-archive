---
topic_id: 6808
title: "Slicer 4 10 1 Opengl Error"
date: 2019-05-15
url: https://discourse.slicer.org/t/6808
---

# Slicer 4.10.1 OpenGL error

**Topic ID**: 6808
**Date**: 2019-05-15
**URL**: https://discourse.slicer.org/t/slicer-4-10-1-opengl-error/6808

---

## Post #1 by @DK_Jang (2019-05-15 21:01 UTC)

<p>Operating system: MacOS Mojave 10.14.5 &amp; XQuartz 2.7.11.<br>
Slicer version: 4.10<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello everyone, I am having an issue launching slicer 4.10 on my computer. Once my mac is connected to Linux server and run Slicer 4.10, it gives me this error:</p>
<p>[jang@poblano ~]$ Slicer</p>
<p>libGL error: No matching fbConfigs or visuals found</p>
<p>libGL error: failed to load driver: swrast</p>
<p>Switch to module: “Welcome”</p>
<p>Unable to find a valid OpenGL 3.2 or later implementation. Please update your video card driver to the latest version. If you are using Mesa please make sure you have version 11.2 or later and make sure your driver in Mesa supports OpenGL 3.2 such as llvmpipe or openswr. If you are on windows and using Microsoft remote desktop note that it only supports OpenGL 3.2 with nvidia quadro cards. You can use other remoting software such as nomachine to avoid this issue.</p>
<p>But our linux server is running Mesa v. 18.0.5 which does support OpenGL 3.2. Other previous versions (4.8, 4.6, and 4.5) run just fine. Of course I can just go ahead and install the mac version, but one of the extension tools that I need to use only runs on Linux (DTI atlas builder). Any help would be appreciated.</p>

---

## Post #2 by @lassoan (2019-05-15 22:06 UTC)

<aside class="quote no-group" data-username="DK_Jang" data-post="1" data-topic="6808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dk_jang/48/3720_2.png" class="avatar"> DK_Jang:</div>
<blockquote>
<p>previous versions (4.8, 4.6, and 4.5) run just fine</p>
</blockquote>
</aside>
<p>Minimum OpenGL version requirement was increased for Slicer-4.10.</p>
<p>Google “libgl error: no matching fbconfigs or visuals found” and try solutions described there. For example, <a href="https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update" class="inline-onebox">drivers - Problems with libGl, fbConfigs, swrast through each update? - Ask Ubuntu</a>.</p>

---

## Post #3 by @njvack (2019-05-16 20:44 UTC)

<p>Hi Andras,</p>
<p>Thanks for your reply! Our server is running Mesa 18.0.5, which <a href="https://mesa3d.org/relnotes/18.0.5.html" rel="nofollow noopener">supports OpenGL 4.5</a> as far as we can tell. We’re running Slicer remotely, using XQuartz/macOS Mojave on the client. The server has no 3D hardware to speak of; we’re planning on using software rendering.</p>
<p>Maybe… maybe our mesa doesn’t have llvmpipe or openswr? Is there a way to check? Or to check and see what Slicer thinks it’s loading and what, exactly, it thinks is missing?</p>
<p>Thanks!<br>
-Nate</p>

---

## Post #4 by @njvack (2019-05-16 22:48 UTC)

<p>Update: Rebuilt Mesa from source, looks like this fixes all the things. <a class="mention" href="/u/dk_jang">@DK_Jang</a>, I’ll be in touch Friday.</p>

---
