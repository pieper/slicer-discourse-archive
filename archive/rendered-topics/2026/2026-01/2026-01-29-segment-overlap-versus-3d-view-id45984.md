---
topic_id: 45984
title: "Segment Overlap Versus 3D View"
date: 2026-01-29
url: https://discourse.slicer.org/t/45984
---

# Segment overlap versus 3D view

**Topic ID**: 45984
**Date**: 2026-01-29
**URL**: https://discourse.slicer.org/t/segment-overlap-versus-3d-view/45984

---

## Post #1 by @Hannnonk (2026-01-29 14:30 UTC)

<p>Two segments.</p>
<p>3D view when segments overlap, and larger segment (segment 1) is 50% transparent:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd64250072bb1a1aa007d8c970e587a2bc44414.jpeg" data-download-href="/uploads/short-url/keKn0Slkm8bFxqwncAona653aqE.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd64250072bb1a1aa007d8c970e587a2bc44414.jpeg" alt="1" data-base62-sha1="keKn0Slkm8bFxqwncAona653aqE" width="413" height="358"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">413×358 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>3D view when smaller segment is subtracted from larger segment (segment 1). Larger segment is 50% transparent:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af791eb7b20202b83d145ceec64011ea0b69f116.jpeg" data-download-href="/uploads/short-url/p2j3s9zUwW4zfBkLntMjOpaIEui.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af791eb7b20202b83d145ceec64011ea0b69f116.jpeg" alt="2" data-base62-sha1="p2j3s9zUwW4zfBkLntMjOpaIEui" width="459" height="370"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">459×370 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why do the opaque bands appear. Is it possible to remove these without expanding the smaller segment to create some overlap?</p>
<p>thx</p>

---

## Post #2 by @cpinter (2026-01-29 16:22 UTC)

<p>Unfortunately there are issues with rendering semi-transparent triangle meshes especially when shadows are enabled. Do you have shadows enabled? If so, what does it look like when you turn it off?</p>

---

## Post #3 by @Hannnonk (2026-01-29 16:35 UTC)

<p>If that is the “shadow visibility” check box obtained in the upper left, then when it is on it is worse, but the above example was with it “off”</p>

---

## Post #4 by @lassoan (2026-01-29 17:38 UTC)

<p>The “z fighting” rendering artifact that you see may be avoided or reduced by making both segments somewhat transparent. Even making segments a little bit transparent, such as opacity=99% instead of opacity=100%, may make a difference.</p>

---
