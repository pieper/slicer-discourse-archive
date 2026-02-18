# SlicerCAT build issues.

**Topic ID**: 15236
**Date**: 2020-12-27
**URL**: https://discourse.slicer.org/t/slicercat-build-issues/15236

---

## Post #1 by @sherinsugathan (2020-12-27 01:41 UTC)

<p>Hi,<br>
I am trying to build SlicerCAT on my Windows 10 machine.<br>
CMake went through without any problem.<br>
I have Qt(v5.12) already installed.</p>
<p>After building the solution file in visual studio I got a linking error related to Qt (attached)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b045c71211951e804f2fd939a9d64d6f0200b267.png" data-download-href="/uploads/short-url/p9nx1xBVofjnpUBxwyWfvcCVfAr.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b045c71211951e804f2fd939a9d64d6f0200b267.png" alt="error" data-base62-sha1="p9nx1xBVofjnpUBxwyWfvcCVfAr" width="690" height="76" data-dominant-color="2B3F4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1381×153 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I went back to Cmake, I saw a variable “Slicer_REQUIRED_QT_VERSION” assigned with a value 5.6.0.<br>
Obviously mine is a v5.12 of Qt. Would that be a problem? Should I uninstall Qt-v5.12 and install a Qt-v5.6?</p>

---

## Post #2 by @lassoan (2020-12-27 01:46 UTC)

<p>Current build instructions are available here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html</a></p>
<p>If you follow the instructions word by word then the build will succeed.</p>

---
