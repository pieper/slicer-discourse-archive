---
topic_id: 42687
title: "Segmentation With Ellipse Shape"
date: 2025-04-25
url: https://discourse.slicer.org/t/42687
---

# Segmentation with ellipse shape

**Topic ID**: 42687
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/segmentation-with-ellipse-shape/42687

---

## Post #1 by @HvNie (2025-04-25 16:06 UTC)

<p>Hi there,</p>
<p>I have a question regarding the segmentation tools. What I’m trying to do in 3D Slicer is segment abdominal aortic aneurysms in 3D ultrasound images. I’ve found that it would be easiest to use a tool that allows me to draw an ellipse shape, rather than using a freehand drawing tool. Is there a way to do this in 3D Slicer?</p>
<p>I know I can draw ellipse-like shapes with the <em>Closed Curve</em> markup tool, but I don’t know how to convert these into a segmentation.</p>
<p>I’ve read that this can be done using the “Surface Cut” effect (provided by the SegmentEditorExtraEffects extension), but I haven’t been able to get it to work. The main issue I’m running into is that I can’t seem to select an already-created markup when I enter the Surface Cut effect. Additionally, the point selection tool within Surface Cut only generates straight lines instead of curved ones.</p>
<p>Does anyone know a solution to this? I’m also open to using other tools or effects.</p>

---

## Post #2 by @pieper (2025-04-25 18:17 UTC)

<p>This might have what you need:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/chir-set/SlicerExtraMarkups">
  <header class="source">

      <a href="https://github.com/chir-set/SlicerExtraMarkups" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/487f1aed183b603ec1fdd33d15b434a0/chir-set/SlicerExtraMarkups" class="thumbnail">

  <h3><a href="https://github.com/chir-set/SlicerExtraMarkups" target="_blank" rel="noopener">GitHub - chir-set/SlicerExtraMarkups: Custom markups for Slicer</a></h3>

    <p><span class="github-repo-description">Custom markups for Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2025-04-25 18:58 UTC)

<p>Since you have a 3D dataset, are you trying to make multiple 2D ellipse shapes and then use the “Fill Between slices” effect to interpolate across them?</p>
<p>The Surface cut effect would seem to work if you are placing the points in 3D rather than in a single 2D slice view. Once you start placing Surface cut points across different slice offsets it will no longer be straight lines, but instead generated an ellipsoidal convex hull object.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f7865ea781ec743f035f123537fa73167b7c47d.jpeg" data-download-href="/uploads/short-url/ibEABU4xNS6HZTUOCBzgWeSLdj7.jpeg?dl=1" title="{CA15EA88-BE10-4CE2-AF0B-E50820C6EE18}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7865ea781ec743f035f123537fa73167b7c47d_2_690x493.jpeg" alt="{CA15EA88-BE10-4CE2-AF0B-E50820C6EE18}" data-base62-sha1="ibEABU4xNS6HZTUOCBzgWeSLdj7" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7865ea781ec743f035f123537fa73167b7c47d_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7865ea781ec743f035f123537fa73167b7c47d_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f7865ea781ec743f035f123537fa73167b7c47d.jpeg 2x" data-dominant-color="3E3D39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{CA15EA88-BE10-4CE2-AF0B-E50820C6EE18}</span><span class="informations">1147×821 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
