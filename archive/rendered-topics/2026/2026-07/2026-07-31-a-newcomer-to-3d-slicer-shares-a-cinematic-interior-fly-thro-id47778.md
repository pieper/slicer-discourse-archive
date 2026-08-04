---
topic_id: 47778
title: "A newcomer to 3D Slicer shares a cinematic interior fly-through of his own LAD and asks whether the rippled texture on the lumen wall is real anatomy or a segmentation/reconstruction artifact."
date: 2026-07-31
url: https://discourse.slicer.org/t/47778
last_bumped: 2026-08-03T17:20:26.937Z
---

# A newcomer to 3D Slicer shares a cinematic interior fly-through of his own LAD and asks whether the rippled texture on the lumen wall is real anatomy or a segmentation/reconstruction artifact.

**Topic ID**: 47778
**Date**: 2026-07-31
**URL**: https://discourse.slicer.org/t/a-newcomer-to-3d-slicer-shares-a-cinematic-interior-fly-through-of-his-own-lad-and-asks-whether-the-rippled-texture-on-the-lumen-wall-is-real-anatomy-or-a-segmentation-reconstruction-artifact/47778

---

## Post #1 by @Passerby (2026-07-31 13:37 UTC)

<p>Hi all, This is my first real project in 3D Slicer, and my first time using Guided Artery Segmentation, so I’d value a reality check from people who work with cardiac CTA.</p>
<p>I’m a retired electrical engineer and commercial artist. I’ve been building interior “fly-through” renders of coronary anatomy — the camera travels inside the lumen instead of viewing the vessel from outside. The clip below is my own LAD (my data, so nothing to de-identify): <a href="https://www.youtube.com/watch?v=GJ9EIpZb9oM" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=GJ9EIpZb9oM</a></p>
<p>Here’s my question: in places the lumen wall has a rippled, undulating texture. As a newcomer I can’t tell how much of that is genuine anatomy versus segmentation or reconstruction artifact — voxel staircase, threshold noise, partial volume, and so on. Before I trust it, I’d love to know what experienced eyes make of it. Are those ripples real?</p>
<p>Here’s how green I was — I did all the lumen segmentation before realizing the calcium was just a separate threshold. I was puzzled by the divots in the wall, until the calcification I segmented dropped into them like a hand in a glove.</p>
<p>Slicer 5.12.3 on Windows. Happy to walk through the pipeline if that helps.</p>

---

## Post #2 by @pieper (2026-07-31 15:51 UTC)

<p>Very cool, and welcome to the community <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Regarding the artifacts you mentioned, a good way to explore that in Slicer is to compare your segmentation carefully to the source images.  You can use the shift-mouse move in any of the views to scroll the slices to the same places (I like to use the linked slice views and jump slice with centering option).  You may also want to explore volume rendering (maybe with the ColorizeVolume module from the Sandbox extension).</p>
<p>Regarding ripples, it could be that you are pushing the resolution limits (lumen is small relative to voxel size) or it could be reconstruction artifact (the CTA is gated to account for heart movement but it’s not perfect).</p>

---

## Post #3 by @Passerby (2026-08-01 02:22 UTC)

<p>Thanks for the feedback! The ripples are definitely there in Slicer, that’s how I chose the fine tuning Guided Segmentation settings, they made the ripples show up. But it’s not a voxel thing, and irregular in a very realistic way. And here’s the thing, I used those “ripple” settings to create the lumen, and did it ignorant of the fact that calcification was a simple threshold, the easiest thing in the world to do. And when I did, it fit in the dents in the lumen rather precisely. Even more precisely than it looks, I deliberately thresholded the calcification for worst case and I hear it tends to bloom anyway. Where it sticks out, it would stick out a lot less. It’s been my experience that slicer creates excellent stl files. Nothing seems to be lost in that translation to the vector world.</p>

---

## Post #4 by @amyers (2026-08-03 17:20 UTC)

<p>Hi Rick,</p>
<p>Thanks for sharing your information of a virtual endoscopy using 3D Slicer’s Guided Segmentation and Auto Desk’s 3ds Max software.</p>
<p>I think a video of an actual endoscopy performed right after a CT Angiogram would be the best way to determine whether the ripples are real anatomy or segmentations. What do you think?</p>
<p>I’m actually putting together a CT Angiogram study on the side that is focused on visualizing coronary arteries through volume rendering, similar to ColorizeVolume. If you’re interested in having another researcher explore your dataset, I can help you anonymize it before sharing.</p>
<p>Alex</p>

---
