---
topic_id: 42300
title: "Display Glyph Size Absolue"
date: 2025-03-25
url: https://discourse.slicer.org/t/42300
---

# Display Glyph Size absolue

**Topic ID**: 42300
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/display-glyph-size-absolue/42300

---

## Post #1 by @sarafv (2025-03-25 16:35 UTC)

<p>Hello everybody,<br>
There is a way  to set the display  node glyph size as a physical length programmatically like pressing the button “absolue” in the Display Menu of  Markups Module (see the attach)?<br>
When I set the size using for example :<br>
myDisplayNode.SetGlyphSize(1.7)<br>
I feel like the glyph size remains relative …<br>
Thanks!<br>
Sara<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3952cdd51354fc96e217b683992cedc6a95b7da2.png" data-download-href="/uploads/short-url/8b6CBpQOGzNGuLzzDOEkSTdkAOC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3952cdd51354fc96e217b683992cedc6a95b7da2.png" alt="image" data-base62-sha1="8b6CBpQOGzNGuLzzDOEkSTdkAOC" width="478" height="359"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">478×359 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @TinaNant28 (2025-05-01 16:17 UTC)

<p>Hello, have you find the solution?</p>

---

## Post #3 by @mikebind (2025-05-01 16:53 UTC)

<p>Using <code>SetUseGlyphScale(False)</code> on the display node is what you are looking for.  Then <code>SetGlyphSize(sizeMm)</code> to set the glyph size in mm.</p>

---
