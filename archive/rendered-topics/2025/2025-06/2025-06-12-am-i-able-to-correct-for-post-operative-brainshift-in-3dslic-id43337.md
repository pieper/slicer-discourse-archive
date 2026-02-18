# Am I able to correct for post-operative brainshift in 3DSlicer?

**Topic ID**: 43337
**Date**: 2025-06-12
**URL**: https://discourse.slicer.org/t/am-i-able-to-correct-for-post-operative-brainshift-in-3dslicer/43337

---

## Post #1 by @SegmenterSam (2025-06-12 21:38 UTC)

<p>Hello all. I am a student researcher and have found 3DSlicer to be incredibly useful.</p>
<p>For my research the goal is to overlay a post-operative segmentation of a resection cavity over the pre-operative segmentation of a glioblastoma, and from that derive which parts of the glioblastoma have been resected and which have been left behind. Unfortunately, as you can imagine, brain shift plays a detremental role here as the resection cavity is unvariably smaller than the original tumor size (even when 95+ percent of the tumor was resected) because the brain tissue shifts back to its original place and thus underestimating the actual resection by a wide margin.</p>
<p>In a perfect world, there would be a way to somehow create a Transform that corrects for brain shift in the post-operative scan.</p>
<p>I am wondering if anybody else here has worked with the same problem and has ideas for workarounds or tools that can help with this?</p>
<p>Thank you very much.</p>

---

## Post #2 by @pieper (2025-06-12 22:33 UTC)

<p>I did something like this using pre- and mid-resection ultrasound volumes of a tumor resection and this video shows an animation of the transform as the brain responds as the mass effect of the tumor recedes.  The pre-resection (gray) is being warped to the mid-resection image (green).  It’s a very researchy video so you might need to watch a couple times or scroll back and forth to get a sense of what’s happening.  If you are good at looking at brain ultrasound you can see structures like sulci and ventricles shifting in response as the tumor gets smaller.</p>
<p>My use case was kind of the opposite of yours, where I wanted to try updating the pre-op MRI to account for the shifting brain and bring it into the coordinates of the ultrasound for navigation purposes.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8dputUoKBTA" data-video-title="MR US p3 2017 08 09" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8dputUoKBTA" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8dputUoKBTA/maxresdefault.jpg" title="MR US p3 2017 08 09" width="690" height="388">
  </a>
</div>

<p>I made this using the LandmarkRegistration module in Slicer (in fact this is what the module was written for), so you should be able to do basically the same thing for your MRI data.  I warn you though that this can be tricky get a good feel for.</p>
<p>The method is basically to select the two volumes and create a thin plates spline transform, and then select create a point in one of the images and then drag it to the same landmark point in the other volume.  As you do this you can watch the transformed volume shift and eventually line up.  I usually start by putting several landmarks far away from the place where the deformation is happening to “pin down” the parts that aren’t moving.</p>
<p>There may be simpler ways to achieve what you are working on but I felt this gave me a nice sense of control which was useful for this very noisy ultrasound data.  The transform is “correct” when the features of the transformed brain match up with the other brain.  Note the transform is asymmetric because rigid structures in the midline resist deformation more than, say, the ventricles.</p>

---

## Post #3 by @SegmenterSam (2025-06-12 23:24 UTC)

<p>Thanks for your quick reply. Sounds like a very hands-on approach but also very doable. I’ll try it out and see what the result is. I can imagine that this method does not have much scientific basis to lean on so it will come down to a neurosurgeons/neuroradiologists expertise to determine if it works sufficiently well to base the research on.</p>
<p>Will let you know how this went.</p>

---
