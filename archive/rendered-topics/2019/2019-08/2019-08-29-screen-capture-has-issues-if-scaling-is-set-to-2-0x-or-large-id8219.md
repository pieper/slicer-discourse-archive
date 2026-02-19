---
topic_id: 8219
title: "Screen Capture Has Issues If Scaling Is Set To 2 0X Or Large"
date: 2019-08-29
url: https://discourse.slicer.org/t/8219
---

# Screen capture has issues if scaling is set to 2.0x or larger

**Topic ID**: 8219
**Date**: 2019-08-29
**URL**: https://discourse.slicer.org/t/screen-capture-has-issues-if-scaling-is-set-to-2-0x-or-larger/8219

---

## Post #1 by @muratmaga (2019-08-29 04:22 UTC)

<p>When I try to do a screen capture of the 3D rendering window at magnification equal or greater to 2.0x, it superimposes two images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380c26b75b7535a31e42b50cc786021734879c3c.png" data-download-href="/uploads/short-url/7ZOLSw1aCXWvryLX3cJwrq3Uo3O.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/380c26b75b7535a31e42b50cc786021734879c3c_2_690x491.png" alt="image" data-base62-sha1="7ZOLSw1aCXWvryLX3cJwrq3Uo3O" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/380c26b75b7535a31e42b50cc786021734879c3c_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380c26b75b7535a31e42b50cc786021734879c3c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380c26b75b7535a31e42b50cc786021734879c3c.png 2x" data-dominant-color="E8E4E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">799×569 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This only happens with 3D view only setting.</p>
<p>Also Screen shot window stays behind the main application window, if Slicer is maximized, and clicking its icon on the toolbar doesn’t bring it back. These issues are with r28464 on windows 10.</p>

---

## Post #2 by @pieper (2019-08-29 21:53 UTC)

<p>Yes, there’s some weird behavior there (confirmed on mac and linux).  For me it only seems to happen with volume rendering but not with other things.  It’s probably some kind of issue related to the way viewports are handled.</p>
<p>I just did some tests and I found that only GPU rendering led to issues.   Can you use CPU rendering and see if the issue goes away?  If so we can try to nail this down to a VTK issue and file a bug there.</p>

---
