---
topic_id: 46821
title: "New Scene Snapshot action in Animator"
date: 2026-04-24
url: https://discourse.slicer.org/t/46821
last_bumped: 2026-04-26T02:21:38.702Z
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

## Post #2 by @muratmaga (2026-04-26 02:21 UTC)

<p>I added a few more things (like copy/paste keyframes and rearrange them easily), along with integration with existing ExplodeModels. Demo below shows transition from volume rendering to models followed by explode model effect. It is sufficiently functional that I merged into development branch of the SlicerMorph extension. It should be available in tomorrow’s preview build.</p>
<p>Thanks again to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for the new SceneViews architecture and the new volume property format and <a class="mention" href="/u/pieper">@pieper</a> for designing the original version this is based on. It become so much easier to make animations like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f8b854cab7d2b153df27b6c9de8de4f7d63910.png" data-download-href="/uploads/short-url/7HsbxDxuZDopuUrdsu76FRQyzMk.png?dl=1" title="Screenshot 2026-04-25 at 7.08.11 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35f8b854cab7d2b153df27b6c9de8de4f7d63910_2_690x396.png" alt="Screenshot 2026-04-25 at 7.08.11 PM" data-base62-sha1="7HsbxDxuZDopuUrdsu76FRQyzMk" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35f8b854cab7d2b153df27b6c9de8de4f7d63910_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f8b854cab7d2b153df27b6c9de8de4f7d63910.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35f8b854cab7d2b153df27b6c9de8de4f7d63910.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-25 at 7.08.11 PM</span><span class="informations">993×570 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d36a120ebd7094ed690aa42cf51848f62db213a.mp4">
  </div><p></p>

---
