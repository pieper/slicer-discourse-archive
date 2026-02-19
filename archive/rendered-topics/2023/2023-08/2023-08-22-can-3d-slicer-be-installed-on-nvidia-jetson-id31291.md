---
topic_id: 31291
title: "Can 3D Slicer Be Installed On Nvidia Jetson"
date: 2023-08-22
url: https://discourse.slicer.org/t/31291
---

# Can 3D Slicer be installed on NVIDIA Jetson?

**Topic ID**: 31291
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/can-3d-slicer-be-installed-on-nvidia-jetson/31291

---

## Post #1 by @FWSU (2023-08-22 14:26 UTC)

<p>hi i want using slicer on nvidia jetson(os : jetpack)<br>
but it linux install file is for amd64 so i can’t install this<br>
how can i do this<br>
help me…</p>

---

## Post #2 by @jcfr (2023-08-22 16:27 UTC)

<p>NVIDIA Jetson is indeed running on Arm processor which is not yet supported.</p>
<p>See <a href="https://developer.nvidia.com/embedded/jetson-modules#tech_specs">https://developer.nvidia.com/embedded/jetson-modules#tech_specs</a></p>
<p>Would you have funding to help prioritize this ?</p>

---

## Post #3 by @FWSU (2023-08-23 01:34 UTC)

<p>I’m still a college student and studying this on my own, so I’m afraid I don’t have the financial means to provide any funding. I’ll continue my research using a Windows environment for now, but it would be great if support for Jetson could be available someday in the future. Thank you for your reply!</p>

---

## Post #4 by @jcfr (2023-08-23 01:45 UTC)

<p>Thanks for the follow up and for reaching out in the first place. We completely understand your situation.</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="31291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>NVIDIA Jetson is indeed running on Arm processor which is not yet supported.</p>
</blockquote>
</aside>
<p>In term of timeline regarding “arm” support, we are currently focusing on arm64 support for macOS.<br>
See <a href="https://github.com/Slicer/Slicer/issues/6811" class="inline-onebox">Support for building/testing/packaging Slicer on Apple arm64 · Issue #6811 · Slicer/Slicer · GitHub</a></p>
<p>Once this is done, we will be better positioned to tackle arm support for NVIDIA Jetson.</p>

---

## Post #5 by @jcfr (2023-08-23 01:46 UTC)

<p>In the meantime, do not hesitate to subscribe to the issue I linked above. You can do so by clicking on the subscribe button on the left. See <a href="https://github.com/Slicer/Slicer/issues/6811">#6811</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded661f3710c857f0e405ec7f4613fdfbc929efa.png" data-download-href="/uploads/short-url/vNjjhODU9LaUl5NPFrk72cOAUaK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/ded661f3710c857f0e405ec7f4613fdfbc929efa_2_345x137.png" alt="image" data-base62-sha1="vNjjhODU9LaUl5NPFrk72cOAUaK" width="345" height="137" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/ded661f3710c857f0e405ec7f4613fdfbc929efa_2_345x137.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/ded661f3710c857f0e405ec7f4613fdfbc929efa_2_517x205.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/ded661f3710c857f0e405ec7f4613fdfbc929efa_2_690x274.png 2x" data-dominant-color="293338"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">746×298 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
