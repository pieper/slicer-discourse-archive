---
topic_id: 11925
title: "Build Slicer With Ubuntu 20 04 Qt5 15 Cmake 3 17 3"
date: 2020-06-08
url: https://discourse.slicer.org/t/11925
---

# Build Slicer with ubuntu 20.04, Qt5.15, cmake 3.17.3

**Topic ID**: 11925
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/build-slicer-with-ubuntu-20-04-qt5-15-cmake-3-17-3/11925

---

## Post #1 by @Davide_Punzo (2020-06-08 12:09 UTC)

<p>Hi guys,</p>
<p>I managed to build latest Slicer on ubuntu 20.04, Qt5.15, cmake 3.17.3, gcc 9.3.0, but I had two minor issues:</p>
<ol>
<li>
<p>I had to set Slicer_USE_PYTHONQT_WITH_OPENSSL = OFF (Slicer was crashing in line <a href="https://github.com/Slicer/Slicer/blob/43a758c3d4a0b1568e505606166fd8f68d19095a/Base/QTCore/qSlicerCoreApplication.cxx#L265" class="inline-onebox" rel="noopener nofollow ugc">Slicer/qSlicerCoreApplication.cxx at 43a758c3d4a0b1568e505606166fd8f68d19095a · Slicer/Slicer · GitHub</a> )</p>
</li>
<li>
<p>Once I build the project and I try to load the inner-build folder (Slicer-build) in QtCreator (4.12.2), QtCreator will reconfigure the full Superbuild inside the inner-build and all the compilation of the inner-build will be compromised. Does anyone have a fix or a workaround?</p>
</li>
</ol>
<p>Davide.</p>

---

## Post #2 by @jcfr (2020-06-08 13:23 UTC)

<blockquote>
<p>managed to build latest Slicer on ubuntu 20.04, Qt5.15, cmake 3.17.3, gcc 9.3.0</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>I had to set Slicer_USE_PYTHONQT_WITH_OPENSSL = OFF (Slicer was crashing in line <a href="https://github.com/Slicer/Slicer/blob/43a758c3d4a0b1568e505606166fd8f68d19095a/Base/QTCore/qSlicerCoreApplication.cxx#L265" class="inline-onebox">Slicer/Base/QTCore/qSlicerCoreApplication.cxx at 43a758c3d4a0b1568e505606166fd8f68d19095a · Slicer/Slicer · GitHub</a> )</p>
</blockquote>
<p>We are long over due to an openssl update.<br>
By any change, do you have a more details stacktrace ?</p>
<blockquote>
<p>Once I build the project and I try to load the inner-build folder (Slicer-build) in QtCreator (4.12.2), QtCreator will reconfigure the full Superbuild inside the inner-build and all the compilation of the inner-build will be compromised. Does anyone have a fix or a workaround?</p>
</blockquote>
<p>Based on my experience with older Qt Creator …</p>
<p>After building the project using <code>Makefile</code> or <code>Ninja</code> generator, did you make sure to open the inner-build project using Qt creator ?</p>
<p>While doing so, you also need to make sure that the compiler, qt version, … all match the one you used to build Slicer.</p>

---

## Post #3 by @Davide_Punzo (2020-06-08 13:44 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="11925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>We are long over due to an openssl update.<br>
By any change, do you have a more details stacktrace ?</p>
</blockquote>
</aside>
<p>ok, I have cleaned the inner-build folder, as soon as I finished recompiling again, I’ll run gdb again.</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="11925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>After building the project using <code>Makefile</code> or <code>Ninja</code> generator, did you make sure to open the inner-build project using Qt creator ?</p>
</blockquote>
</aside>
<p>yes</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="11925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>While doing so, you also need to make sure that the compiler, qt version, … all match the one you used to build Slicer.</p>
</blockquote>
</aside>
<p>ok, in the past for me it was quite automatic and smooth, I’ll check the kit variables.</p>

---

## Post #4 by @Davide_Punzo (2020-06-08 15:17 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="11925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>By any change, do you have a more details stacktrace ?</p>
</blockquote>
</aside>
<p>screenshot of the levels:<br>
</p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a2e209b195ffe5ac3964b964b9f11dc1a54f98.png" data-download-href="/uploads/short-url/gm7pdBlMSfT1sxjQpOVxj9LG5QI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72a2e209b195ffe5ac3964b964b9f11dc1a54f98_2_690x221.png" alt="image" data-base62-sha1="gm7pdBlMSfT1sxjQpOVxj9LG5QI" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72a2e209b195ffe5ac3964b964b9f11dc1a54f98_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a2e209b195ffe5ac3964b964b9f11dc1a54f98.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a2e209b195ffe5ac3964b964b9f11dc1a54f98.png 2x" data-dominant-color="E8EEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×268 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
please let me know if you need variables or pointer info for some levels.<p></p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="11925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>While doing so, you also need to make sure that the compiler, qt version, … all match the one you used to build Slicer.</p>
</blockquote>
</aside>
<p>It was indeed a wrong compiler version in the qtcreator kit (I should have checked <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20">), thanks for the hint!</p>

---
