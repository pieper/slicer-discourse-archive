# New segment editor effect for creating hollow objects

**Topic ID**: 2464
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects/2464

---

## Post #1 by @lassoan (2018-03-29 05:24 UTC)

<p>Making a solid segment hollow is useful in many applications, such as creating 3D-printable vessel walls from contrast-CT volumes.</p>
<p>While it was possible to create hollow segments in 3D Slicer by using Margins and Logical operators effect, it was not very convenient.</p>
<p>A new effect - Hollow - has been added to Segment editor to create hollow objects from solid objects in one simple step.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1.jpeg" data-download-href="/uploads/short-url/8ODYv3Esp7oHaIyuhVKlro8AbsZ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_544x500.jpg" alt="image" data-base62-sha1="8ODYv3Esp7oHaIyuhVKlro8AbsZ" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_544x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_816x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_1088x1000.jpg 2x" data-dominant-color="75727C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1842×1690 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Short demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="jtDHTaAEilU" data-video-title="Make hollow - new segment editor effect in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jtDHTaAEilU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/jtDHTaAEilU/maxresdefault.jpg" title="Make hollow - new segment editor effect in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #2 by @doc-xie (2018-04-08 08:47 UTC)

<p>Hi,Professor Lassoan,<br>
In order to use the Hollow effect,which extention should be downloaded or installed into 3D Slicer of the old version(4.8.1)?<br>
Thanks a lot!<br>
Dr.Xie</p>

---

## Post #3 by @brhoom (2018-04-08 09:00 UTC)

<p>SegmentEditorExtraEffects<br>
Here is the source code, as well.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8e010956a14a16f4c3d0066e0c449a9c0134030bf6fc57bee1cdf6d6b6448ea7/lassoan/SlicerSegmentEditorExtraEffects" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional...</a></h3>

  <p>Many additional segmentation tools for 3D Slicer's Segment Editor - GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional segmentation tools for 3D Slicer's Segment Editor</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @doc-xie (2018-04-09 02:44 UTC)

<p>Thank you for the quick reply!<br>
The SegmentEditorEffects extention had been installed in the software.Even if I downloaded the SegmentEditorHollow.py,add its path into the additional module and restart 3D Slicer,the button of the hollow have not shown in the Effects file as below.What is the reason about this?Otherwise,there is a file named “<strong>init</strong>.py”,what is the meaning about is?<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae97357082503e888c90304d852ace978c3a0c2.jpeg" alt="%E6%97%A0%E6%A0%87%E9%A2%98" data-base62-sha1="jOS3uQtoaVwGy0WTJ2R6nH2hW3E" width="567" height="364"><br>
Best!<br>
Dr.Xie</p>

---

## Post #5 by @lassoan (2018-04-09 04:36 UTC)

<p>If you installed SegmentEditorExtraEffects extension for Slicer-4.8.1 before, then you need to update it (or uninstall and install it again) to get the new effect.</p>
<p>For manual install, it is not enough to copy a single file but the entire content of <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorHollow">SegmentEditorHollow folder</a>, including subdirectories. The folder containing <code>SegmentEditorHollow.py</code> must be added to <code>Additional module paths</code>.</p>

---
