---
topic_id: 47141
title: "PCA visualization parameters"
date: 2026-05-26
url: https://discourse.slicer.org/t/47141
last_bumped: 2026-05-26T21:22:04.643Z
---

# PCA visualization parameters

**Topic ID**: 47141
**Date**: 2026-05-26
**URL**: https://discourse.slicer.org/t/pca-visualization-parameters/47141

---

## Post #1 by @Stephan_Collins (2026-05-26 16:44 UTC)

<p>Hi everyone,<br>
I am working with the GPA module from slicermorph and I noticed some changes which are most likely intentional and for good reasons but I need to ask.</p>
<p>When you have a PCA showing segregation thanks to multiple axes such as here (not the best significant example I guess), the Interactive 3D visualization tab from the GPA module would allow you to play with two PCs simultaneously. This has changed in the latest version I think and I can only use one at a time. I suppose I can show the effect of one composant on one axis (show a distance to distance map for small values on PC1 vs high values and then do the same on the second axis (pc2). More work but possibly more accurate to describe what may be going on ? Conceptually, though, combining PC1 and PC2 absolutely makes sense when data separate “diagonally”. but a scaled displacements along PC1 and PC2 is not really like applying two transforms in sequence, is it ?<br>
Is this why this approach was removed. What should we do in these cases ?<br>
My apologies if this was discussed elsewhere</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a97d38601c5002b18886d4425b30da3a70c919.png" data-download-href="/uploads/short-url/ucrSfN1njIvcQTZYbWeVvWNP7Lz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a97d38601c5002b18886d4425b30da3a70c919.png" alt="image" data-base62-sha1="ucrSfN1njIvcQTZYbWeVvWNP7Lz" width="436" height="372"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">436×372 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-05-26 21:22 UTC)

<aside class="quote no-group" data-username="Stephan_Collins" data-post="1" data-topic="47141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/stephan_collins/48/81446_2.png" class="avatar"> Stephan_Collins:</div>
<blockquote>
<p>I suppose I can show the effect of one composant on one axis (show a distance to distance map for small values on PC1 vs high values</p>
</blockquote>
</aside>
<p>Yes, that is normally how most PC visualization are done; by reconstructing min and max of the specific PC and providing them as visuals on the corresponding side of the PCA plot. One slider is enough to do that.</p>
<p>Where two slider was marginally useful was for a specific PC value in one slider, you can add the other one (stacking the PCs). But then why two? Why not five? We can’t possibly add all PCs as sliders, this is better done programmatically (a case of scripting is being much more simple than trying to accomplish the same thing via UI).</p>
<p>As for visualizing the diagonal transects, that’s never possible with the old interface, because that means you have to simultaneously increase the both sliders. this is now replaced with much easier way of achieving the same thing via clicking the PCA plot. First enable, 3D visualization, then choose the option “Drive 3D model from PCA scatter plot” and then click anywere on the PCA plot. The model (or the point cloud) in Viewer 2 will dynamically change based on the PC coordinates (aka value) of you clicked. So you can do diagonal or any angle.</p>
<p>This is a new change, that I introduced recently to the preview version. I will be talking more about it in the SlicerMorph office hour on the June 3rd.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5190f8fac023e5ee76a0adcb1d194ca28f9ae7c0.jpeg" data-download-href="/uploads/short-url/bDzhcoxT5Nw6WkRzSjMM8l9cADK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/5190f8fac023e5ee76a0adcb1d194ca28f9ae7c0_2_638x500.jpeg" alt="image" data-base62-sha1="bDzhcoxT5Nw6WkRzSjMM8l9cADK" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/5190f8fac023e5ee76a0adcb1d194ca28f9ae7c0_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/5190f8fac023e5ee76a0adcb1d194ca28f9ae7c0_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/5190f8fac023e5ee76a0adcb1d194ca28f9ae7c0_2_1276x1000.jpeg 2x" data-dominant-color="BDB9C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1384×1083 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
