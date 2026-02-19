---
topic_id: 37771
title: "How To Build Nvidia Nvapi In Slicer Environment"
date: 2024-08-08
url: https://discourse.slicer.org/t/37771
---

# How to build NVidia NVAPI in slicer environment

**Topic ID**: 37771
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/how-to-build-nvidia-nvapi-in-slicer-environment/37771

---

## Post #1 by @alientex (2024-08-08 09:40 UTC)

<p>Hello everyone,</p>
<p>I want to add the <a href="https://developer.nvidia.com/gameworksdownload#?search=nvapi" rel="noopener nofollow ugc">nvapi</a> SDK to the Slicer environment so that users can choose which GPU to use, similar to how we select a GPU in the NVIDIA Control Panel for a specific application.</p>
<p>Can anybody guide me on how to add the sdk?</p>
<p>Thanks</p>

---

## Post #2 by @alientex (2024-08-13 05:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a> Is it possible to add such library in slicer?</p>

---

## Post #3 by @pieper (2024-08-13 14:12 UTC)

<p>I don’t know of any work in that area, but you could build Slicer from source and link in the library.  Or you could write a command line wrapper for the functions you want and then invoke that as a subprocess from Slicer.</p>

---

## Post #4 by @jcfr (2024-08-13 14:58 UTC)

<p>To follow-up on <a class="mention" href="/u/pieper">@pieper</a> answer, you may be interested in reviewing the following:</p>
<ul>
<li><a href="https://stackoverflow.com/questions/6165628/use-python-ctypes-to-interface-with-nvapi-follow-up-with-demonstration-code">https://stackoverflow.com/questions/6165628/use-python-ctypes-to-interface-with-nvapi-follow-up-with-demonstration-code</a></li>
<li><a href="https://github.com/verybigbadboy/NVAPI-example/blob/master/example/main.cpp">NVAPI-example</a></li>
</ul>
<p>It should help you understand how to work with the associated API.</p>

---

## Post #5 by @alientex (2024-08-23 04:07 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="37771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>you could write a command line wrapper for the functions you want and then invoke that as a subprocess from Slicer</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, I tried this approach, and it worked perfectly with the wrapper. However, I would like to use the library without the wrapper by linking it directly to the slicer, so I can become familiar with adding other libraries to the slicer in the future.</p>

---

## Post #6 by @alientex (2024-08-23 04:18 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Thanks for providing the reference links.</p>
<p>I’ve reviewed both links, and my requirement is in C++. I am already familiar with using basic NVAPI functions, and the example link you provided will be additional help.</p>
<p>I am trying to link the library in Slicer, and for that, I’ve created a <code>CMakeLists.txt</code> file with the necessary code. I am able to build it without any errors and can include the NVAPI header files in Slicer. However, after writing some basic GPU information retrieval code, I encounter the following error after building Slicer.sln:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92636b1a8a835354e4efa01b88c58ad06f5c8706.png" data-download-href="/uploads/short-url/kT0IeXsfVWz1rqNpVDcVe9OLZ2e.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92636b1a8a835354e4efa01b88c58ad06f5c8706.png" alt="image" data-base62-sha1="kT0IeXsfVWz1rqNpVDcVe9OLZ2e" width="690" height="386" data-dominant-color="2C2F35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1108×620 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, I can provide more information about the CMake code and how I built the library if you could help me resolve this issue.</p>
<p>Thank you.</p>

---

## Post #7 by @alientex (2024-09-05 04:27 UTC)

<p>Hello, can anybody help me solve this issue? I’ve been stuck on this error for several days.</p>
<p>I appreciate any hints or help.</p>
<p>Thank you.</p>

---
