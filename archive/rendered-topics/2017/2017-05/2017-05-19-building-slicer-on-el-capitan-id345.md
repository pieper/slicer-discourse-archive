# Building Slicer on El Capitan

**Topic ID**: 345
**Date**: 2017-05-19
**URL**: https://discourse.slicer.org/t/building-slicer-on-el-capitan/345

---

## Post #1 by @xliu (2017-05-19 16:09 UTC)

<p>Hi all,</p>
<p>I am trying to build Slicer on my Mac. <strike>Qt4 installer does not work on El Capitan. I have tried homebrew, but it only installs Qt5 now. I also tried compile Qt4 with the homebrew patch, still failed. Is there any other way to get Qt4 working?</strike></p>
<p>I have successfully installed Qt4 with ‘brew install cartr/qt4/qt’ according to the post <a href="http://slicer-devel.65872.n3.nabble.com/Struggling-with-Sierra-build-td4037945.html" rel="nofollow noopener">http://slicer-devel.65872.n3.nabble.com/Struggling-with-Sierra-build-td4037945.html</a>. Thanks Christian!<br>
While building Slicer, I run into the error “This platform’s pyconfig.h needs to define PY_FORMAT_LONG_LONG”. I tried configure python-cmake-buildsystem directly but still got the same error. Anyone has any idea why?</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2017-05-19 17:31 UTC)

<p>Hi xliu,</p>
<p><s>Would be great to share the error so that other building on MacOSX can help you.</s></p>
<p>Also since we build the official Slicer installer on a older MacOSX, we do not have a regularly tested solution.</p>
<p>As a side note, we are also actively working on finalizing the transition to Qt5.</p>
<p>Jc</p>

---

## Post #3 by @pieper (2017-05-19 17:58 UTC)

<p>I haven’t build Qt4 from scratch on mac osx for quite a while.  It used to work but it’s entirely possible that it no longer works.</p>
<p>Following up on Jc’s note, it is possible to build  mostly-working Slicer using the regular Qt5 download binaries.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/Qt5</a></p>

---

## Post #4 by @fedorov (2017-05-19 19:35 UTC)

<p><a class="mention" href="/u/che85">@che85</a> also reported problems building on El Capitan that he could not resolve.</p>

---

## Post #5 by @che85 (2017-05-19 20:09 UTC)

<p>I don’t use El Capitan anymore. I am sure that you can specify the version of qt when using brew.</p>

---

## Post #6 by @fedorov (2017-05-19 20:27 UTC)

<p>Ah, I forgot that El Capitan is no longer the latest one.</p>
<p>Does it work for you on Sierra Christian?</p>

---

## Post #7 by @che85 (2017-05-19 23:12 UTC)

<p>On Sierra it works.</p>
<p>Take a look at this post:</p>
<p><a href="http://slicer-devel.65872.n3.nabble.com/Struggling-with-Sierra-build-td4037945.html" class="onebox" target="_blank" rel="nofollow noopener">http://slicer-devel.65872.n3.nabble.com/Struggling-with-Sierra-build-td4037945.html</a></p>

---
