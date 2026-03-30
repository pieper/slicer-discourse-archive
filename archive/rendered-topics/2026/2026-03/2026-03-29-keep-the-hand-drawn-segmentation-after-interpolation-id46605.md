---
topic_id: 46605
title: "Keep The Hand Drawn Segmentation After Interpolation"
date: 2026-03-29
url: https://discourse.slicer.org/t/46605
---

# Keep the hand-drawn segmentation after interpolation

**Topic ID**: 46605
**Date**: 2026-03-29
**URL**: https://discourse.slicer.org/t/keep-the-hand-drawn-segmentation-after-interpolation/46605

---

## Post #1 by @mrrezaie (2026-03-29 14:28 UTC)

<p>Hello all. I’m working with a non-isotropic MRI, only the sagittal view with 31 slices. More info can be found in this post: <a href="https://discourse.slicer.org/t/segmentation-using-curves/46511" class="inline-onebox">Segmentation using curves</a> . I drew the segmentation on each slice, however, the 3D shape is not smoothed and there are lots of steps and many holes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6166434f98bab8a65cee68cd6421941e3db471e.jpeg" data-download-href="/uploads/short-url/nHhetEadky20JOzJs5I6AubrzPw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6166434f98bab8a65cee68cd6421941e3db471e.jpeg" alt="image" data-base62-sha1="nHhetEadky20JOzJs5I6AubrzPw" width="362" height="342"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">362×342 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One suggestion was to interpolate the slices using Crop module. This ended up with hundreds of slices (e.g., 600), but I don’t want to go through all. I want to interpolate the segmentation as well.</p>
<p>My plane now is to keep the initial hand-drawn segmentation and Fill between the intermediate slices after interpolation. However, my initial segmentation appears in all intermediate slices and the “Fill between slices” doesn’t actually work.</p>
<p>By any chance, is there any way to handle this? (I can draw the segmentation after interpolation, but I cannot find the original slices)</p>
<p>Thank you in advance.</p>

---

## Post #2 by @mrrezaie (2026-03-29 14:46 UTC)

<p>Here is a video that better explains the issue.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7d84cfc6c1ced042b0082a1d0de41e4e6024dea.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4834c8d77a6a6d4bbc92ecb7ed8eae246f7d97c3.png" data-video-base62-sha1="zmxm9JoCCkS4J61tpehvfSwTf3I.mp4">
  </div>This also happens even if I draw segmentation on only one slice after interpolation.<p></p>

---
