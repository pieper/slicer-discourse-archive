# Adding a new effect to the Segment Editor module

**Topic ID**: 34717
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/adding-a-new-effect-to-the-segment-editor-module/34717

---

## Post #1 by @yaraabdelazim (2024-03-05 16:07 UTC)

<p>Hello,</p>
<p>I am trying to develop a SegmentEditor effect that works kind of like the Level Tracing effet but instead of detecting levels, it would detect the edges in the volume. However, I can’t really find any documentation on how to include an effect in the Segment Editor module. Does anyone know where I can find this information?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @muratmaga (2024-03-05 17:03 UTC)

<p>Normally you cannot add an effect directly into the Segment Editor module (unless you build your own Slicer from scratch), but you can do your own extension and register with Segment Editor. some examples are:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/adeb95cdbf2c585d13aa9ec4fe23df1c2acd69ffcf645f62dcd10164026de0e1/lassoan/SlicerSegmentEditorExtraEffects" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" target="_blank" rel="noopener">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional...</a></h3>

  <p>Many additional segmentation tools for 3D Slicer's Segment Editor - lassoan/SlicerSegmentEditorExtraEffects</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/19d6c083af1690f17eea6d46e6fc87c9073e035f4a9539b0d46662124b3e7701/sebastianandress/Slicer-SurfaceWrapSolidify" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" target="_blank" rel="noopener">GitHub - sebastianandress/Slicer-SurfaceWrapSolidify: 3D Slicer extension...</a></h3>

  <p>3D Slicer extension which contains a Segment Editor Effect that solidifies and extracts the surface of a segmentation - sebastianandress/Slicer-SurfaceWrapSolidify</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @yaraabdelazim (2024-03-06 09:23 UTC)

<p>Hello,</p>
<p>Thank you for your response. I tried to follow these examples but I’m not able to find my effect in 3D Slicer. Where can I find it to be able to test it?</p>

---
