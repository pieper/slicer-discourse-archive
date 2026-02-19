---
topic_id: 8965
title: "Buttonwidget Cant Interaction"
date: 2019-10-31
url: https://discourse.slicer.org/t/8965
---

# Buttonwidget can't interaction

**Topic ID**: 8965
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/buttonwidget-cant-interaction/8965

---

## Post #1 by @pingdan (2019-10-31 08:28 UTC)

<p>I created a buttonwidget, when I set the buttonwidget on the rightupper view, it works well, when I click the button, the yellow color and the orange color changed .but when I set the buttonwidget on a leftbottom view, the button can’t change color when click. the codes are the same. why?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f348aa0281c8eb37426c33a9b16427b0baf616b0.png" data-download-href="/uploads/short-url/yIbHRo2Ba4WWgZYo1mpQ80esKsM.png?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f348aa0281c8eb37426c33a9b16427b0baf616b0_2_481x500.png" alt="0" data-base62-sha1="yIbHRo2Ba4WWgZYo1mpQ80esKsM" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f348aa0281c8eb37426c33a9b16427b0baf616b0_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f348aa0281c8eb37426c33a9b16427b0baf616b0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f348aa0281c8eb37426c33a9b16427b0baf616b0.png 2x" data-dominant-color="2F302D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">613×636 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe94200a36f80418e73e75535865472e9f3b539e.png" data-download-href="/uploads/short-url/Ak6DjM6rDGIDt7saYs6CEANK262.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe94200a36f80418e73e75535865472e9f3b539e_2_484x500.png" alt="1" data-base62-sha1="Ak6DjM6rDGIDt7saYs6CEANK262" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe94200a36f80418e73e75535865472e9f3b539e_2_484x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe94200a36f80418e73e75535865472e9f3b539e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe94200a36f80418e73e75535865472e9f3b539e.png 2x" data-dominant-color="30302E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">615×635 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76fb1c9fd6ef7414a20607094a89efa41db80468.png" data-download-href="/uploads/short-url/gYylsnGActzR2hYzbirSNIqZ0sE.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fb1c9fd6ef7414a20607094a89efa41db80468_2_481x500.png" alt="2" data-base62-sha1="gYylsnGActzR2hYzbirSNIqZ0sE" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76fb1c9fd6ef7414a20607094a89efa41db80468_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76fb1c9fd6ef7414a20607094a89efa41db80468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76fb1c9fd6ef7414a20607094a89efa41db80468.png 2x" data-dominant-color="2F302D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">611×635 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-10-31 11:08 UTC)

<p>VTK widgets are a mess (extremely slow, inconsistent design, inflexible event mapping, not shareable between views, not visually appealing). We tried to use them for a couple of years and we ended up wasting enormous amount of time (hundreds of thousands of dollars). It’s not just us - most VTK-based applications don’t use them, VTK.js redesigned them from scratch, etc.</p>
<p>Finally last year we gave up on them and developed new version of the widget infrastructure - see results in Markups module. We could develop features that we have been just wanting to have for years. We still have some of the old-style widgets (plane and box) but we are getting rid of those, too.</p>
<p>We put general purpose buttons, sliders in the view header (see script repository for example of adding custom widget), which is also food because we don’t pollute the view with non-location-specific elements. Location specific items (points, lines, etc. in the view’s coordinate system) are interactive, clickable.</p>

---
