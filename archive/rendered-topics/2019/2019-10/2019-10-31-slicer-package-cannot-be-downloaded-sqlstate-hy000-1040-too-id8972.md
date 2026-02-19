---
topic_id: 8972
title: "Slicer Package Cannot Be Downloaded Sqlstate Hy000 1040 Too"
date: 2019-10-31
url: https://discourse.slicer.org/t/8972
---

# Slicer package cannot be downloaded - 'SQLSTATE[HY000] [1040] Too many connections'

**Topic ID**: 8972
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/slicer-package-cannot-be-downloaded-sqlstate-hy000-1040-too-many-connections/8972

---

## Post #1 by @lassoan (2019-10-31 13:55 UTC)

<p>Right now, Slicer package download from <a href="https://download.slicer.org/">https://download.slicer.org/</a> fails due to the following Midas3 error:</p>
<blockquote>
<p>Uncaught exception ‘PDOException’ with message ‘SQLSTATE[HY000] [1040] Too many connections’</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3b2f8a0ed6ed51c2470e351fab55eb12c3f50e8.png" data-download-href="/uploads/short-url/yLRt6diqP1x9AgJEUkifyxOQ2Hm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3b2f8a0ed6ed51c2470e351fab55eb12c3f50e8.png" alt="image" data-base62-sha1="yLRt6diqP1x9AgJEUkifyxOQ2Hm" width="690" height="365" data-dominant-color="DFE2E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">943×499 45.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @Sam_Horvath (2019-10-31 13:59 UTC)

<p>Okay, going to have the Midas instance rebooted.</p>

---

## Post #3 by @lassoan (2019-10-31 14:11 UTC)

<p>Thank you. The issue has been resolved.</p>

---
