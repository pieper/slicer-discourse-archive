# Slicer layout not correct on Mac

**Topic ID**: 2574
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/slicer-layout-not-correct-on-mac/2574

---

## Post #1 by @priya.vada4 (2018-04-13 01:07 UTC)

<p>Hi</p>
<p>I recently built Slicer 4.8.1 on my Mac from source. When I start Slicer on my external display, the layout looks correct. However, when I start Slicer on my Macbook without an external display, the layout is distorted and size the tabs, collapsible tabs and drop-down menus are large. I have attached a screenshot with this posting. Could someone suggest a solution for the problem.</p>
<p>Slicer version - 4.8.1-2017-12-19 r26813<br>
Qt version - 4.8.7</p>
<p>Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3ccbd17d4a6991cda237fb34f46cb7fdd33646c7.png" data-download-href="/uploads/short-url/8FPkgPzO71lVtioZ94gIPmkpn83.png?dl=1" title="Slicer-layout" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ccbd17d4a6991cda237fb34f46cb7fdd33646c7_2_466x500.png" alt="Slicer-layout" data-base62-sha1="8FPkgPzO71lVtioZ94gIPmkpn83" width="466" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ccbd17d4a6991cda237fb34f46cb7fdd33646c7_2_466x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ccbd17d4a6991cda237fb34f46cb7fdd33646c7_2_699x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ccbd17d4a6991cda237fb34f46cb7fdd33646c7_2_932x1000.png 2x" data-dominant-color="F1F1F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-layout</span><span class="informations">1552×1662 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @RafaelPalomar (2018-04-13 11:30 UTC)

<p>Hello Priya,</p>
<p>can’t you just resize it down by drag-and-dropping the border between the 3D view and the widgets panel?</p>
<p>If not, maybe you could try to build 3D Slicer with Qt5 instead of Qt4 and see if the problem persists?</p>
<p>Best,<br>
Rafael.</p>

---

## Post #3 by @lassoan (2018-04-13 13:05 UTC)

<p>All widget scaling problems should be fixed in recent nightly builds that use Qt5. If there are remaining issues then let us know.</p>

---

## Post #4 by @priya.vada4 (2018-04-13 13:55 UTC)

<p>Thanks very much, Rafael and Andras.</p>
<p>Should we change the instructions on the Slicer webpage for building the source to reflect the need to use Qt5?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#MacOSX" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#MacOSX</a></p>
<p>Thanks</p>

---

## Post #5 by @lassoan (2018-04-16 14:19 UTC)

<aside class="quote no-group" data-username="priya.vada4" data-post="4" data-topic="2574">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/d26b3c/48.png" class="avatar"> priya.vada4:</div>
<blockquote>
<p>Should we change the instructions</p>
</blockquote>
</aside>
<p>Yes. We’ll discuss this at the next developer tcon.</p>

---
