---
topic_id: 16518
title: "Display Tab Of Markups Module Incompatible With Dark Display"
date: 2021-03-12
url: https://discourse.slicer.org/t/16518
---

# Display tab of Markups module incompatible with dark display

**Topic ID**: 16518
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/display-tab-of-markups-module-incompatible-with-dark-display/16518

---

## Post #1 by @aohowens (2021-03-12 22:16 UTC)

<p>I’m using the dark display with slicer and there seems to be a bug with the Display tab of the Markups module, here’s a screenshot of what I’m seeing. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/068621774aed40d84a6594ad32dfb3d9f060c0eb.png" data-download-href="/uploads/short-url/VIeN61Sqt35qjTJBj7rAzHSZ7B.png?dl=1" title="Screen Shot 2021-03-11 at 1.40.10 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/068621774aed40d84a6594ad32dfb3d9f060c0eb_2_690x369.png" alt="Screen Shot 2021-03-11 at 1.40.10 PM" data-base62-sha1="VIeN61Sqt35qjTJBj7rAzHSZ7B" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/068621774aed40d84a6594ad32dfb3d9f060c0eb_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/068621774aed40d84a6594ad32dfb3d9f060c0eb_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/068621774aed40d84a6594ad32dfb3d9f060c0eb_2_1380x738.png 2x" data-dominant-color="848594"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-11 at 1.40.10 PM</span><span class="informations">1804×966 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system: macOS Big Sur Version 11.2<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: Able to read sliders and such in the Display tab of the Markups module<br>
Actual behavior: See screenshot, much of the information for each slider is not shown</p>

---

## Post #2 by @jamesobutler (2021-03-12 22:32 UTC)

<p>Thanks for reminding us about this issue. We currently have it tracked as part of <a href="https://github.com/Slicer/Slicer/issues/5135" class="inline-onebox" rel="noopener nofollow ugc">Some widgets not updating appropriately on style change · Issue #5135 · Slicer/Slicer · GitHub</a>. Toggling style may be a workaround for you to trigger an appropriate update for you to be able to read the label text. Edit → Application settings → Appearance → Style</p>
<p>xref: <a href="https://discourse.slicer.org/t/parts-of-a-module-user-interface-are-unreadable-in-dark-mode-on-macos/15956" class="inline-onebox">Parts of a module user interface are unreadable in dark mode on macOS</a></p>

---
