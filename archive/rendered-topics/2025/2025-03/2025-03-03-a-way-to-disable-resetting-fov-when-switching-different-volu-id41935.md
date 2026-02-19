---
topic_id: 41935
title: "A Way To Disable Resetting Fov When Switching Different Volu"
date: 2025-03-03
url: https://discourse.slicer.org/t/41935
---

# A way to disable resetting FOV when switching different volumes

**Topic ID**: 41935
**Date**: 2025-03-03
**URL**: https://discourse.slicer.org/t/a-way-to-disable-resetting-fov-when-switching-different-volumes/41935

---

## Post #1 by @muratmaga (2025-03-03 02:24 UTC)

<p>I have a bunch of volumes that are in the same coordinate space and orientation. They are loaded into the scene and when I zoom in one volume and then, go to data module to turn on the visibility of the volume, slice views resets my zoom levels and the slice I am on.</p>
<p>This is a reasonable behavior normally, but for my use case it is rather annoying. Is there a way to stop this from happening through some sort of a python command?</p>

---

## Post #2 by @jamesobutler (2025-03-03 04:00 UTC)

<p>Something like the following in the right-click context menu of the visibility column in the Data module?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adbc9ab724c3c1e9c9e3f457457dc702f40d2a86.png" data-download-href="/uploads/short-url/oMWGuwfFAtumjXwjFLNUcStG8jc.png?dl=1" title="{9B344B2F-5D4E-4209-BBCE-8282BEF79981}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adbc9ab724c3c1e9c9e3f457457dc702f40d2a86.png" alt="{9B344B2F-5D4E-4209-BBCE-8282BEF79981}" data-base62-sha1="oMWGuwfFAtumjXwjFLNUcStG8jc" width="560" height="383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{9B344B2F-5D4E-4209-BBCE-8282BEF79981}</span><span class="informations">560×383 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2025-03-03 04:48 UTC)

<p>Yes, exactly. I didn’t know about this!</p>

---
