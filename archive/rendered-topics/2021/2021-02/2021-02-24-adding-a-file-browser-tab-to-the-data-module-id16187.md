---
topic_id: 16187
title: "Adding A File Browser Tab To The Data Module"
date: 2021-02-24
url: https://discourse.slicer.org/t/16187
---

# Adding a file browser tab to the Data module

**Topic ID**: 16187
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/adding-a-file-browser-tab-to-the-data-module/16187

---

## Post #1 by @muratmaga (2021-02-24 17:35 UTC)

<p>I think Data module is becoming more and more important to the user experience, but opening data set is still happening outside of the data module. I am wondering if it is feasible to implement a file browser section within the data module, so that we can navigate within Slicer and point and click the files natively supported by Slicer or if options needed -such as coordinate specification in 3D Models- bring the load dialog box prepopulated?</p>
<p>While drag and drops are useful and convenient, I personally find a bit obstructive to switch windows…</p>

---

## Post #2 by @muratmaga (2021-02-24 19:01 UTC)

<p>Just as a visual guide of what i meant, adding something like this as the fourth tab to the Data module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c121119458226c297cf8093cdc57c903806b33b.png" data-download-href="/uploads/short-url/40k4Mm2N33P7ojzZ6rGJzEI2F6P.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c121119458226c297cf8093cdc57c903806b33b.png" alt="image" data-base62-sha1="40k4Mm2N33P7ojzZ6rGJzEI2F6P" width="382" height="500" data-dominant-color="2F3D5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">558×730 39.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-02-25 06:40 UTC)

<p>On Windows, I can very easily snap Slicer to one side of the screen and a file browser to the other. I guess it should be similarly easy on other operating systems, too. So, it is not clear for me what this could simplify.</p>
<p>Also note that you can drag-and-drop and entire folder and load all of its content into the scene and then right-click in the empty region in Subject hierarchy tree and choose “Create hierarchy from loaded directory structure” to reproduce the file folder tree using Subject hierarchy folders.</p>

---

## Post #4 by @muratmaga (2021-02-25 20:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="16187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>So, it is not clear for me what this could simplify.</p>
</blockquote>
</aside>
<p>I was imaging a tighter integration, for example directly dragging things into 3D viewer and bypassing the load dialog box. Or right-click menus that can enable operation (e.g., segment this volume).</p>

---

## Post #5 by @lassoan (2021-02-25 20:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="16187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I was imaging a tighter integration, for example directly dragging things into 3D viewer and bypassing the load dialog box.</p>
</blockquote>
</aside>
<p>This would be nice, but unfortunately we need the “Add data” window so that the user can specify how the file should be interpreted. Maybe the real issue is the need for “Add data” window. We could do something similar to DICOM module, which allows direct loading with default options (and user can enable an “Advanced mode” for the rare cases when custom loading options are needed).</p>

---
