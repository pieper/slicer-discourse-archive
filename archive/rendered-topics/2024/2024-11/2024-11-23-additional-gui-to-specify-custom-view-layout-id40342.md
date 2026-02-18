# Additional GUI to specify custom view layout

**Topic ID**: 40342
**Date**: 2024-11-23
**URL**: https://discourse.slicer.org/t/additional-gui-to-specify-custom-view-layout/40342

---

## Post #1 by @mohammed_alshakhas (2024-11-23 10:28 UTC)

<p>it would be great if additoinal view are implenmented in slicer . my wishes  are the following<br>
TMJ view : this is done with a control axial view and multi section coronal and sagittla .  it is a standard now in all cbcts viewers like romexis and others .</p>
<p>series view: this is similar to old fashion fillms where you choose a seerial like coronal and you get and all the cuts .  it helps a lot if you see all the sections same time without scrolling .</p>

---

## Post #2 by @mohammed_alshakhas (2024-11-24 12:07 UTC)

<p>example of view</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00690028bd7264bc86ffa2308739c3b01451bb17.jpeg" data-download-href="/uploads/short-url/3CXGYQS2PSCBurw6ed0dA197uL.jpeg?dl=1" title="Screenshot 2024-11-24 at 14.26.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00690028bd7264bc86ffa2308739c3b01451bb17_2_690x374.jpeg" alt="Screenshot 2024-11-24 at 14.26.50" data-base62-sha1="3CXGYQS2PSCBurw6ed0dA197uL" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00690028bd7264bc86ffa2308739c3b01451bb17_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00690028bd7264bc86ffa2308739c3b01451bb17_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00690028bd7264bc86ffa2308739c3b01451bb17_2_1380x748.jpeg 2x" data-dominant-color="565451"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-24 at 14.26.50</span><span class="informations">1920×1041 87.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2024-11-24 13:17 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="40342">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>would be great if additoinal view are implenmented in slicer</p>
</blockquote>
</aside>
<p>It could be nice to add GUI to allow defining and saving custom view layouts. However, you can already define such layouts quote easily using the Python console. You can specify it with in a simple XML text format as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">here</a>.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="40342">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>series view: this is similar to old fashion fillms</p>
</blockquote>
</aside>
<p>This is called the “lightbox” view and it can be generated in the Screen Capture module.</p>
<p>You can also enable lightbox mode in any slice view. However, this is a very rarely used feature that is hard to maintain for developers (and it is slow and interactions are limited to one slice), so we plan to remove it in a future Slicer version.</p>

---
