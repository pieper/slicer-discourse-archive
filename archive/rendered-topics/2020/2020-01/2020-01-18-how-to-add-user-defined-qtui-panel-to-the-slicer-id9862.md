---
topic_id: 9862
title: "How To Add User Defined Qtui Panel To The Slicer"
date: 2020-01-18
url: https://discourse.slicer.org/t/9862
---

# How to add user-defined QTUI panel to the slicer

**Topic ID**: 9862
**Date**: 2020-01-18
**URL**: https://discourse.slicer.org/t/how-to-add-user-defined-qtui-panel-to-the-slicer/9862

---

## Post #1 by @Shicong (2020-01-18 08:57 UTC)

<p>I’d like to add a displayed qt panel qslicerlogindialog.ui to the slider, which is placed in the directory shown below, but cannot be used; a panel like qslicerdatadialog.ui automatically generates a qslicerdialog_p.h header file and a qslicerdatadialogprivate class, but how can I add a new qslicerlogindialog.ui to generate a qslicerlogindialog_p.h header file and aqslicerlogerlogePrivate class? Qslicerdatadialog_p.h How was this file generated? Thanks.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1449a166d97b2f91846a9ef35fbeb4e3da9f58f.png" data-download-href="/uploads/short-url/rzJ86poq7S2XSCdDaJCQAsonww7.png?dl=1" title="pzha1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1449a166d97b2f91846a9ef35fbeb4e3da9f58f.png" alt="pzha1" data-base62-sha1="rzJ86poq7S2XSCdDaJCQAsonww7" width="660" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pzha1</span><span class="informations">757×573 37.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Shicong (2020-01-18 10:25 UTC)

<p>This question is how to make your own pop-up box in slicer app。</p>

---

## Post #3 by @lassoan (2020-01-18 14:37 UTC)

<p>You can create and edit .ui files using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner">Qt designer</a>. You can write everything from scratch but I usually start from copying and renaming .cxx, .h, .ui files of an existing similar widget.</p>

---

## Post #4 by @Shicong (2020-01-19 01:47 UTC)

<p>Thank you very much!</p>

---
