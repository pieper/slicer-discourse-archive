---
topic_id: 47912
title: "Cannot install any extension updates"
date: 2026-08-17
url: https://discourse.slicer.org/t/47912
last_bumped: 2026-08-18T19:00:07.636Z
---

# Cannot install any extension updates

**Topic ID**: 47912
**Date**: 2026-08-17
**URL**: https://discourse.slicer.org/t/cannot-install-any-extension-updates/47912

---

## Post #1 by @RushAR3DLab (2026-08-17 23:03 UTC)

<p>hi, I upgraded today from 3d Slicer v 5.8 to 5.12 (latest stable version), because I had been experiencing the same issue already with v 5.8. When I launch Extension Manager it cannot download the files for updates. The python console shows this:</p>
<blockquote>
<p>[Qt] An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.</p>
<p>[Qt] A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> .</p>
<p>[Qt] Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/6a709511e5707846f0878d73/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/6a709511e5707846f0878d73/download</a></p>
</blockquote>
<p>On top of that, it will only get to the Extension Manager if it does not freeze upon start up. I am running this version from a Win 11, Intel Core Ultra 7 255HX (2.40 GHz), w 64 GB RAM HP laptop.</p>
<p>Still a newbie on this, so any help is appreciated. When I first installed v 5.8, the extension manager worked seamlessly on this same laptop. Can it be something in my network? BTW this happens on two different Win 11 PCs.</p>

---

## Post #2 by @ebrahim (2026-08-18 12:24 UTC)

<p>From your network are you able to download the package directly from the URL in your error message? <a href="https://slicer-packages.kitware.com/api/v1/file/6a709511e5707846f0878d73/download">https://slicer-packages.kitware.com/api/v1/file/6a709511e5707846f0878d73/download</a></p>
<p>Just to test first whether it’s a network access problem or somehting else</p>
<p>(as for the extension manager sometimes freezing up on windows maybe some others can reply if they have encountered this)</p>

---

## Post #3 by @RushAR3DLab (2026-08-18 18:15 UTC)

<p>thanks for the suggestion. I was able to download manually, so that possibly discards the network theory. Since I have that file, I should be able to install manually as well, right?</p>

---

## Post #4 by @ebrahim (2026-08-18 19:00 UTC)

<p>Yes you can install the package manually using the “install from file” button (like shown <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions.html#install-extensions">here</a>)</p>
<p>(But the extension manager should work <img src="https://emoji.discourse-cdn.com/twitter/face_with_diagonal_mouth.png?v=15" title=":face_with_diagonal_mouth:" class="emoji" alt=":face_with_diagonal_mouth:" loading="lazy" width="20" height="20">)</p>

---
