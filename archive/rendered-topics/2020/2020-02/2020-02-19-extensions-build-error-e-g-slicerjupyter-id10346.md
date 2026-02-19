---
topic_id: 10346
title: "Extensions Build Error E G Slicerjupyter"
date: 2020-02-19
url: https://discourse.slicer.org/t/10346
---

# Extensions build error (e.g. SlicerJupyter)

**Topic ID**: 10346
**Date**: 2020-02-19
**URL**: https://discourse.slicer.org/t/extensions-build-error-e-g-slicerjupyter/10346

---

## Post #1 by @ungi (2020-02-19 00:14 UTC)

<p>Hi,</p>
<p>I wanted to update my Slicer Preview version. I need the SlicerJupyter extension, but I noticed that it has build errors for a couple of weeks now. I went back in the CDash calendar to a date when it was built, but the yellow box icon was missing that I usually use to download the Slicer installer for Windows (it was there for the other platforms, just not Windows). I had to go back to early January to find a date when both the Windows installer and SlicerJupyter was available.<br>
Is anybody working on fixing these build errors?</p>
<p>Thanks,<br>
Tamas</p>

---

## Post #2 by @jamesobutler (2020-02-19 00:30 UTC)

<p>I haven’t been working on fixing SlicerJupyter, but did just take a look. The main build error for the extension started for the Slicer build started February 8th 2020.</p>
<p>SlicerJupyter has an external project for cppzmq which uses the master branch for that project. That project issued <a href="https://github.com/zeromq/cppzmq/commit/324b11f23951127423f66839bdc8cad53ff76c8f" rel="nofollow noopener">https://github.com/zeromq/cppzmq/commit/324b11f23951127423f66839bdc8cad53ff76c8f</a> on the 7th which is also still the latest commit on the master branch.</p>

---

## Post #3 by @lassoan (2020-02-19 00:38 UTC)

<p>Thanks for checking this. I’ll try if using a specific hash on cppzmq master fixes the build error.</p>

---

## Post #4 by @lassoan (2020-02-19 01:14 UTC)

<p>Confirmed that the change <a class="mention" href="/u/jamesobutler">@jamesobutler</a> found caused the build error. I’ve <a href="https://github.com/zeromq/cppzmq/issues/385">reported the error to cppzmq</a>. In the meantime, to fix the build error, I have <a href="https://github.com/Slicer/SlicerJupyter/commit/2d867440bf98f2bff483a7df7a73a92a022b2cc7">locked SlicerJupyter to use the previous commit</a>.</p>

---
