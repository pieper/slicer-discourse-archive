---
topic_id: 33711
title: "Wrong Orientation When Using The Imagestacks Module"
date: 2024-01-10
url: https://discourse.slicer.org/t/33711
---

# Wrong orientation when using the ImageStacks module

**Topic ID**: 33711
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/wrong-orientation-when-using-the-imagestacks-module/33711

---

## Post #1 by @sansui (2024-01-10 04:28 UTC)

<p>I have a set of mouse brain images (Coronal Serial sections). When I load a single image as “Any Data”, the image appears correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37dc231b28edc78e4dcb1c73ba9f01d6f0347cf2.jpeg" data-download-href="/uploads/short-url/7Y9TXeLICyyXYJhuGE3LBF997km.jpeg?dl=1" title="anydata" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37dc231b28edc78e4dcb1c73ba9f01d6f0347cf2_2_690x380.jpeg" alt="anydata" data-base62-sha1="7Y9TXeLICyyXYJhuGE3LBF997km" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37dc231b28edc78e4dcb1c73ba9f01d6f0347cf2_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37dc231b28edc78e4dcb1c73ba9f01d6f0347cf2_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37dc231b28edc78e4dcb1c73ba9f01d6f0347cf2_2_1380x760.jpeg 2x" data-dominant-color="75757A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">anydata</span><span class="informations">1920×1059 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I use the ImageStacks module, the R and G views show a thin image and the Y view shows a fuzzy image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f25cb1698e98f28933a07d74c0fbf5a971f4ce41.png" data-download-href="/uploads/short-url/yA28MMcP4ZaSN19Ge0WHD9Isnol.png?dl=1" title="imagestacks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f25cb1698e98f28933a07d74c0fbf5a971f4ce41_2_690x380.png" alt="imagestacks" data-base62-sha1="yA28MMcP4ZaSN19Ge0WHD9Isnol" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f25cb1698e98f28933a07d74c0fbf5a971f4ce41_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f25cb1698e98f28933a07d74c0fbf5a971f4ce41_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f25cb1698e98f28933a07d74c0fbf5a971f4ce41_2_1380x760.png 2x" data-dominant-color="747479"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagestacks</span><span class="informations">3386×1868 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there some option that needs to be set for the orientation?</p>

---

## Post #2 by @pieper (2024-01-10 15:58 UTC)

<p>Looks like you are till in Preview mode in ImageStacks.  Clicking full resolution should help.  Also it looks like your data are not 1x1x1mm, but likely much more thickly sliced in the Z axis, so you can adjust that (ideally to a known value from your experiment).  Once you have it loaded you can adjust the orientation using the Transforms module.</p>

---

## Post #3 by @muratmaga (2024-01-10 16:49 UTC)

<aside class="quote no-group" data-username="sansui" data-post="1" data-topic="33711">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sansui/48/68936_2.png" class="avatar"> sansui:</div>
<blockquote>
<p>I have a set of mouse brain images (Coronal Serial sections). When I load a single image as “Any Data”, the image appears correctly.</p>
</blockquote>
</aside>
<p>Please check the tutorial about setting the image spacing correctly when you are importing data via ImageStacks.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" target="_blank" rel="noopener">//github.com/SlicerMorph/Tutorials/tree/main/ImageStacks</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
