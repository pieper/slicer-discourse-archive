# Build errors with slicer

**Topic ID**: 36817
**Date**: 2024-06-16
**URL**: https://discourse.slicer.org/t/build-errors-with-slicer/36817

---

## Post #1 by @slicer365 (2024-06-16 02:45 UTC)

<p>When I compile Slicer, it always shows the following error. I am using the main version from GitHub. Can someone tell me how to solve this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d02a3874278db9bec14d0f190880304e4c04670.png" data-download-href="/uploads/short-url/moYCdxDpRIoEmm0uVRKNsb5GXGU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d02a3874278db9bec14d0f190880304e4c04670_2_517x202.png" alt="image" data-base62-sha1="moYCdxDpRIoEmm0uVRKNsb5GXGU" width="517" height="202" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d02a3874278db9bec14d0f190880304e4c04670_2_517x202.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d02a3874278db9bec14d0f190880304e4c04670_2_775x303.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d02a3874278db9bec14d0f190880304e4c04670_2_1034x404.png 2x" data-dominant-color="302F30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1475×579 58.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2024-08-12 11:38 UTC)

<p>What is your Windows OS Build Number?<br>
Visual Studio Version?<br>
CMake Version?</p>

---

## Post #3 by @slicer365 (2024-08-12 23:04 UTC)

<p>Thank you for your response, James. I feel like there are always some strange issues, but I finally solved this one by reinstalling the computer system.</p>

---

## Post #4 by @jamesobutler (2024-08-12 23:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="36817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Windows OS Build Number?<br>
Visual Studio Version?<br>
CMake Version?</p>
</blockquote>
</aside>
<p>Could you provide the versions of these things that you are using with your newly reinstalled operating system? This will provide the community with a known working configuration upon facing this you issue that you reported.</p>

---

## Post #5 by @slicer365 (2024-08-13 00:15 UTC)

<p>OS: win10 64 19045.4651<br>
VisualStudio: 2022 LTS 17.6  community<br>
CMake: 3.29.6</p>
<p>In the meantime, I switched between different versions of Visual Studio and CMake, but the issue remained unresolved. I still believe the problem might be related to the version of Visual Studio rather than CMake. Although reinstalling the system resolved the issue, I’m not sure if upgrading Visual Studio changed something.</p>
<p>I noticed that during that time, the community did discuss some issues related to the latest version of Visual Studio.</p>

---
