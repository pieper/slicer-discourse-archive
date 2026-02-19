---
topic_id: 1388
title: "Registration Of Animated Model Against 4D Multi Volume Seque"
date: 2017-11-06
url: https://discourse.slicer.org/t/1388
---

# Registration of animated model against 4D multi-volume sequence

**Topic ID**: 1388
**Date**: 2017-11-06
**URL**: https://discourse.slicer.org/t/registration-of-animated-model-against-4d-multi-volume-sequence/1388

---

## Post #1 by @jdx-john (2017-11-06 17:36 UTC)

<p>We have a nice, smooth, 24fps animated 3D polygonal heart - based on a single human patient but artist-optimised. We use this in an external realtime 3D application but need to adjust it for each real patient based on CT scans.</p>
<p>We’ve seen from <a class="mention" href="/u/lassoan">@lassoan</a> some demonstration of the powerful registration capabilities in Slicer but how might this apply to an animated model, and a multi-frame CT dataset? I expect heart animation in our 3D model would be a set of static keyframes we interpolate between but whether those keyframes map 1:1 to timepoints in the CT scans is unlikely.</p>
<p>Manually registering each keyframe totally separately would be possible but hugely time consuming. Would Slicer allow us to perform gross manipulations (position and rotate the whole model, crude scaling) across all key-frames, and then fine-tune each keyframe/pose against a given time-point in the CT scan?</p>

---

## Post #2 by @pieper (2017-11-06 23:03 UTC)

<p>Hmm, that’s a tough one.  I don’t think there are any existing tools to do exactly that, but what I’d suggest is exploring a landmark based thin plate spline deformation of the model to match the CT.  Probably the first step would be to do a time base correction so that the animated model matches the patient’s cardiac cycle and then make correspondences between important anatomical structures.  You’d never expect the artist’s model to exactly fit the patient but  you could probably make it look realistic.  Definitely some programming work involved.</p>

---

## Post #3 by @jdx-john (2017-11-08 13:35 UTC)

<p>Thanks Steve.</p>
<p>We’ve seen the landmark approach (I think) used with a single volume and a<br>
single 3D model and it looked probably good enough for cases where the<br>
basic topology of the hearts were equivalent, clearly not cases with<br>
different structures but deforming the 3D heart’s mesh without cutting it,<br>
etc.</p>
<p>What I was unsure about is where we have a lot of frames on our 3D heart -<br>
basically 24 different models at an extreme. Avoiding duplication of work<br>
would be key here, e.g. applying changes to all versions at once while<br>
keeping their differences. I wondered if the deformations are done as some<br>
sort of 3D spatial grid-deformation e.g. mapping a linear 3-space to a<br>
warped one. Then the same grid deformation could be applied to every<br>
animation frame.</p>
<p>Of course there might be per-frame tweaks but being able to do a first pass<br>
in such a fashion would be a huge boon!</p>

---

## Post #4 by @pieper (2017-11-08 18:37 UTC)

<p>Hi John -</p>
<p>Yes, the transforms are hierarchical, so you could apply a bulk linear or nonlinear transform to get the artist’s heart model in roughly the right spot and then compose that with a per-frame deformation to adapt to differences in the motion and you could then animate that.  It would definitely be possible to get an approximation with that method.</p>
<p>Hope that helps,<br>
Steve</p>

---
