---
topic_id: 46821
title: "New Scene Snapshot Action In Animator"
date: 2026-04-24
url: https://discourse.slicer.org/t/46821
---

# New Scene Snapshot action in Animator

**Topic ID**: 46821
**Date**: 2026-04-24
**URL**: https://discourse.slicer.org/t/new-scene-snapshot-action-in-animator/46821

---

## Post #1 by @muratmaga (2026-04-24 02:53 UTC)

<p>I update the Animator module in SlicerMorph to make use of the SceneView architecture. The old volume rendering, rotation and animation actions were too complicated to use. In this one, you specify the duration of the animation (which you can increase later), capture a few keyframes adjust their position on the time track and then let the animation run.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bd520ca3c2551c99f710239448f25b0350a6b10.png" data-download-href="/uploads/short-url/fnVIhdo61Dx1HUKYLWtFKo5ubLy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bd520ca3c2551c99f710239448f25b0350a6b10_2_591x500.png" alt="image" data-base62-sha1="fnVIhdo61Dx1HUKYLWtFKo5ubLy" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bd520ca3c2551c99f710239448f25b0350a6b10_2_591x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bd520ca3c2551c99f710239448f25b0350a6b10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bd520ca3c2551c99f710239448f25b0350a6b10.png 2x" data-dominant-color="F0F1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">763×645 58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Attached animation is done with these three keyframes shown above. If you want to try, prototype is in this branch: <a href="https://github.com/SlicerMorph/SlicerMorph/tree/animator-snapshot-timeline" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph at animator-snapshot-timeline · GitHub</a></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6949bf86e4d928c18ce767118ebf320624e6e5ed.mp4">
  </div><p></p>

---
