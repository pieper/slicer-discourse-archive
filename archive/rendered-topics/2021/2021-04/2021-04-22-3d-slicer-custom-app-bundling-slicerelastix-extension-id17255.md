---
topic_id: 17255
title: "3D Slicer Custom App Bundling Slicerelastix Extension"
date: 2021-04-22
url: https://discourse.slicer.org/t/17255
---

# 3D Slicer Custom App bundling SlicerElastix extension

**Topic ID**: 17255
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/3d-slicer-custom-app-bundling-slicerelastix-extension/17255

---

## Post #1 by @marianaslicer (2021-04-22 20:49 UTC)

<p>Hi everyone,</p>
<p>I was able to create an executable file for my 3D Slicer Custom App following this tutorial <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> and with your useful suggestions.</p>
<p>The last step of the BUILD file is:</p>
<pre data-code-wrap="bash"><code class="lang-bash">cmake --build . --config Release --target PACKAGE
</code></pre>
<p>What exactly does it do? I would like to share the executable file with other people, do I need to share all of the generated files? That isn’t what I wanted because I would be sending the source code…</p>
<p>I also already tried to build the <code>PACKAGE</code> but I’m having this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a0372886482e9e62075b57e08e122b39b80f6b1.png" data-download-href="/uploads/short-url/8hd4UNJktUDZ0tvkVRBWIoHhh17.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a0372886482e9e62075b57e08e122b39b80f6b1.png" alt="image" data-base62-sha1="8hd4UNJktUDZ0tvkVRBWIoHhh17" width="690" height="394" data-dominant-color="210304"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×561 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would appreciate some help. Thanks</p>

---

## Post #2 by @jcfr (2021-04-23 02:18 UTC)

<aside class="quote no-group" data-username="marianaslicer" data-post="1" data-topic="17255">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>What exactly does it do? I would like to share the executable file with other people, do I need to share all of the generated files?</p>
</blockquote>
</aside>
<p>Building the <code>PACKAGE</code> target would have the following effect:</p>
<ul>
<li>Build Slicer dependencies, Slicer modules as well as the Slicer executable</li>
<li>Create an windows installer that you can distribute.</li>
</ul>
<p>The C++ source files would not be distributed.</p>
<blockquote>
<p>I also already tried to build the <code>PACKAGE</code> but I’m having this error:</p>
</blockquote>
<p>Based on the error message, it looks like you included the <a href="https://github.com/lassoan/SlicerElastix/">SlicerElastix</a> extension and the packaging is failing.</p>
<p>Few questions:</p>
<ul>
<li>Could you confirm this is the case by sharing how you integrate it in your <code>CMakeLists.txt</code> ?</li>
<li>Could you share the complete error message ?</li>
</ul>

---

## Post #3 by @marianaslicer (2021-04-23 07:24 UTC)

<p>Hi Jean,</p>
<p>Thank you for your response. That is what I’m looking for.<br>
My source files are written in Python programming language.</p>
<p>To integrate the SlicerElastix extension I used the following instructions in the CMakeLists.txt:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db10274edef064eb642eab1e62a82dbd044b9929.png" alt="image" data-base62-sha1="vfVaQ68B6imm1BznBgl5RaQxXLz" width="678" height="225"></p>
<p>Where can I find the complete error message? Please find in this link the complete message on cmd: <a href="https://drive.google.com/file/d/1O9KdvEjxj1BX7sTg1BwTyykowcL9MACY/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1O9KdvEjxj1BX7sTg1BwTyykowcL9MACY/view?usp=sharing</a></p>
<p>Thank you.</p>

---

## Post #4 by @marianaslicer (2021-04-23 08:30 UTC)

<p>In VS 2017 I’m getting the following error message:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e48e9e92df034b29984f4071f7ab8533a8d30e8.png" data-download-href="/uploads/short-url/4jUxxHBXyY8ayN0d18E5YviQ2YU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e48e9e92df034b29984f4071f7ab8533a8d30e8.png" alt="image" data-base62-sha1="4jUxxHBXyY8ayN0d18E5YviQ2YU" width="690" height="221" data-dominant-color="2A3137"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">975×313 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
