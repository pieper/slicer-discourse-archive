---
topic_id: 13548
title: "Scatter Plot Colour Each Point Differently"
date: 2020-09-18
url: https://discourse.slicer.org/t/13548
---

# Scatter Plot: Colour each point differently

**Topic ID**: 13548
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/scatter-plot-colour-each-point-differently/13548

---

## Post #1 by @sthirumal (2020-09-18 15:15 UTC)

<p>For the scatter plot in Slicer, I’m wondering if there is a way to colour each point uniquely. I’d like for each point to be coloured based on the density of nearest points. I’ve attached an image of what I would like the plot to look like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fb45d26ff3177a8dfe0b3de52fb617958fce4d.png" data-download-href="/uploads/short-url/7Qo8endwisIFqtFATOeGVjiENUV.png?dl=1" title="Density scatter plot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb45d26ff3177a8dfe0b3de52fb617958fce4d_2_685x500.png" alt="Density scatter plot" data-base62-sha1="7Qo8endwisIFqtFATOeGVjiENUV" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb45d26ff3177a8dfe0b3de52fb617958fce4d_2_685x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fb45d26ff3177a8dfe0b3de52fb617958fce4d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fb45d26ff3177a8dfe0b3de52fb617958fce4d.png 2x" data-dominant-color="EBECF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Density scatter plot</span><span class="informations">970×708 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-18 15:25 UTC)

<p>I don’t think the plot view is prepared for this, but it should not be hard to create similar plots in slice or 3D views. And of course you can use any of Python’s dozens of plotting libraries in Slicer to create such images.</p>

---
