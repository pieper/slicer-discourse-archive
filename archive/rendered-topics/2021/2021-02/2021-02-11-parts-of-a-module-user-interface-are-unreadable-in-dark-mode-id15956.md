---
topic_id: 15956
title: "Parts Of A Module User Interface Are Unreadable In Dark Mode"
date: 2021-02-11
url: https://discourse.slicer.org/t/15956
---

# Parts of a module user interface are unreadable in dark mode on macOS

**Topic ID**: 15956
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/parts-of-a-module-user-interface-are-unreadable-in-dark-mode-on-macos/15956

---

## Post #1 by @canoe_ccrg (2021-02-11 17:32 UTC)

<p>On my macbook pro, this extension show unnormal<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60e5a6d6914c0806c312232adc72609e70f166e2.jpeg" data-download-href="/uploads/short-url/dPbRy0wP3aUl6MX3NVVQLYrRihQ.jpeg?dl=1" title="截屏2021-02-12 01.29.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e5a6d6914c0806c312232adc72609e70f166e2_2_400x500.jpeg" alt="截屏2021-02-12 01.29.54" data-base62-sha1="dPbRy0wP3aUl6MX3NVVQLYrRihQ" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e5a6d6914c0806c312232adc72609e70f166e2_2_400x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e5a6d6914c0806c312232adc72609e70f166e2_2_600x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e5a6d6914c0806c312232adc72609e70f166e2_2_800x1000.jpeg 2x" data-dominant-color="626263"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2021-02-12 01.29.54</span><span class="informations">1318×1646 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2021-02-11 17:34 UTC)

<p>Thanks for reporting! I’ll take a look at it.</p>

---

## Post #3 by @lassoan (2021-02-11 17:44 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> there may be issues with ctk groupbox in dark mode (see also <a href="https://github.com/Slicer/Slicer/issues/5135" class="inline-onebox">Some widgets not updating appropriately on style change · Issue #5135 · Slicer/Slicer · GitHub</a>).</p>
<p><a class="mention" href="/u/canoe_ccrg">@canoe_ccrg</a> until the problem is fixed you can change from automatic (Slicer) to fixed light or dark mode (Light Slicer or Dark Slicer) in menu: Edit → Application settings → Appearance → Style.</p>

---
