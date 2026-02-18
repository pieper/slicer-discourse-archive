# Fading out segments in animation with SlicerMorph

**Topic ID**: 31539
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/fading-out-segments-in-animation-with-slicermorph/31539

---

## Post #1 by @div1708 (2023-09-04 08:25 UTC)

<p>Hi all,</p>
<p>I am using the Animator utility in SlicerMorph, essentially hoping to recreate this video</p>
<p>(I.e animation begins with all segments visible, some segments fade out during the animation to leave deeper segments visible).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="oGtvTOhIFtA" data-video-title="SlicerAnimator" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oGtvTOhIFtA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oGtvTOhIFtA/maxresdefault.jpg" title="SlicerAnimator" width="" height="">
  </a>
</div>

<p>I have tried to export my segments to a labelmap and then use it in the VolumeProperties actions to string different volumes containing different segments together in the animation, but this approaches loses the smooth surfaces I am hoping to show.</p>
<p>Any advice much appreciated!</p>

---

## Post #2 by @muratmaga (2023-09-08 04:33 UTC)

<p>In this video, the skull is not a segmentation object. it is a volume rendering. At this point, you can only fade in/out the volumes using the volume rendering. It is probably possible to add the fading to the models but we don’t have the bandwidth to do that now.</p>
<p>Depending on the number of segments, you can try the same trick. Also instead of exporting the segments as labelmap, just export the contents as volumes (you can use the SplitVolumes effect of the SegmentEditorExtraEffects). If you export them as volumes you will not encounter the staircase effects.</p>

---
