---
topic_id: 41775
title: "Run Commands At Pythonslicer"
date: 2025-02-19
url: https://discourse.slicer.org/t/41775
---

# Run commands at PythonSlicer

**Topic ID**: 41775
**Date**: 2025-02-19
**URL**: https://discourse.slicer.org/t/run-commands-at-pythonslicer/41775

---

## Post #1 by @Djonathan_Souza (2025-02-19 18:32 UTC)

<p>Hi,</p>
<p>Is there a way to run these commands in PythonSlicer?</p>
<p>I need to access <code>mrmlScene</code> from PythonSlicer, but I’m not sure how to do it. Any suggestions?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949dd0723387c19ba309c606c8addacf9ab3ff2d.png" data-download-href="/uploads/short-url/lcIMqtF8UkJz2yVvGjPlpCBqMJ7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949dd0723387c19ba309c606c8addacf9ab3ff2d.png" alt="image" data-base62-sha1="lcIMqtF8UkJz2yVvGjPlpCBqMJ7" width="345" height="204"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">345×204 6.36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-02-19 19:13 UTC)

<p>PythonSlicer exposes only the python part, not the slicer application part.  You can use the <code>--no-main-window</code> to run a script with app features but no gui.</p>

---
