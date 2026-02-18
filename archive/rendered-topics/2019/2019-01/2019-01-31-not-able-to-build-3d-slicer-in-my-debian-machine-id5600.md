# Not able to build 3d slicer in my debian machine 

**Topic ID**: 5600
**Date**: 2019-01-31
**URL**: https://discourse.slicer.org/t/not-able-to-build-3d-slicer-in-my-debian-machine/5600

---

## Post #1 by @Mahesh_Kumar (2019-01-31 14:59 UTC)

<p>I want to debug one of the module in 3d slicer. I tried to install 3d slicer as per the documentation mentioned in link below (section<br>
Quick build on debian) <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Quick_Build_on_Debian" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/438b1490ab1a9248f3f97938620284ea28d15331.png" data-download-href="/uploads/short-url/9DvY3UbDmfvX3499wbTbxJqK5fH.png?dl=1" title="slicer_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/438b1490ab1a9248f3f97938620284ea28d15331_2_690x394.png" alt="slicer_error" data-base62-sha1="9DvY3UbDmfvX3499wbTbxJqK5fH" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/438b1490ab1a9248f3f97938620284ea28d15331_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/438b1490ab1a9248f3f97938620284ea28d15331_2_1035x591.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/438b1490ab1a9248f3f97938620284ea28d15331.png 2x" data-dominant-color="090D09"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_error</span><span class="informations">1245×711 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I am getting error like QTemporaryDir: No such file or directory.</p>
<p>Please find the attached snapshot of that error.</p>
<p>Can any please help me on how to fix this error.</p>
<p>I am using cmake version 3.13.3 and qmake --version is Qt version 4.8.7</p>
<p>Please let me know if you need any information.</p>
<p>Thanks.</p>

---

## Post #2 by @ihnorton (2019-01-31 17:19 UTC)

<p>Qt4 support is deprecated and will be removed soon on all platforms (if it has not been already since 4.10 – the docs may be outdated). So I suggest to build against Qt5.</p>

---

## Post #3 by @gcsharp (2019-01-31 17:25 UTC)

<p>Agree.  You need this:</p>
<pre><code>cmake -DQt5_DIR:PATH=/usr/lib/x86_64-linux-gnu/cmake/Qt5 &lt;etc&gt;</code></pre>

---
