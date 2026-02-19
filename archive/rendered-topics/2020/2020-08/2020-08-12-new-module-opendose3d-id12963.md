---
topic_id: 12963
title: "New Module Opendose3D"
date: 2020-08-12
url: https://discourse.slicer.org/t/12963
---

# New module: OpenDose3D

**Topic ID**: 12963
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/new-module-opendose3d/12963

---

## Post #1 by @Alex_Vergara (2020-08-12 10:05 UTC)

<p>Hello</p>
<p>We have released a beta test of our OpenDose3D extension. It is available in the last nightly using extension manager. We expect it to have bugs and we need to solve every bug you find in this stage.</p>
<p>Please report any bug in <a href="https://gitlab.com/opendose/opendose3d/-/boards" class="inline-onebox" rel="noopener nofollow ugc">Development · Boards · OpenDose / SlicerOpenDose3D · GitLab</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fd463684fbf976c5a5a541c760966fa69c308e.png" data-download-href="/uploads/short-url/v6qfq1Qta1ffFGs8pf575tBhZrE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9fd463684fbf976c5a5a541c760966fa69c308e_2_620x500.png" alt="image" data-base62-sha1="v6qfq1Qta1ffFGs8pf575tBhZrE" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9fd463684fbf976c5a5a541c760966fa69c308e_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9fd463684fbf976c5a5a541c760966fa69c308e_2_930x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fd463684fbf976c5a5a541c760966fa69c308e.png 2x" data-dominant-color="E7E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1017×820 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Alex_Vergara (2020-08-12 10:33 UTC)

<p>I found the first error, when installed it does not create the logic see the error trace:</p>
<pre><code class="lang-auto">File “/Applications/Slicer.app/Contents/Extensions-29265/OpenDose3D/lib/Slicer-4.11/qt-scripted-modules/Dosimetry4D.py”, line 230, in setup
    self.setupWidgets()
  File “/Applications/Slicer.app/Contents/Extensions-29265/OpenDose3D/lib/Slicer-4.11/qt-scripted-modules/Dosimetry4D.py”, line 820, in setupWidgets
    self.logic = Dosimetry4DLogic(parent=self, isotopeText=isotopeText)
TypeError: ‘module’ object is not callable
</code></pre>
<p>However, this doesn’t happened when installed as a custom script.<br>
<a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a><br>
Is there anything wrong in the packaging?</p>

---

## Post #3 by @Alex_Vergara (2020-08-12 14:08 UTC)

<p>The commit <a href="https://gitlab.com/opendose/opendose3d/-/commit/a28818c27f61ab302ce87cb9cf17fa3b34a8681b" rel="nofollow noopener">https://gitlab.com/opendose/opendose3d/-/commit/a28818c27f61ab302ce87cb9cf17fa3b34a8681b</a> shall fix the issue. Let’s see tomorrow how it goes</p>

---

## Post #4 by @Alex_Vergara (2020-08-13 10:33 UTC)

<p>I have successfully tested it in MacOS</p>
<p>May somebody test in Windows and Linux?</p>

---

## Post #5 by @Alex_Vergara (2020-08-13 13:28 UTC)

<p>Tested in Windows, it works fine.</p>

---

## Post #6 by @Alex_Vergara (2020-08-13 13:40 UTC)

<p>There is a test failing and reported <a href="https://gitlab.com/opendose/opendose3d/-/issues/26" rel="nofollow noopener">here</a></p>

---
