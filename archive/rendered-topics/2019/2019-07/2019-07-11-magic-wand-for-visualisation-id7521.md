# Magic Wand for visualisation

**Topic ID**: 7521
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/magic-wand-for-visualisation/7521

---

## Post #1 by @Melodicpinpon (2019-07-11 07:53 UTC)

<p>Hello,</p>
<p>I would like to use the magic wand, not to create a 3D model, but to mask the dicom itself. Is it possible?<br>
I have seen some tutos about the segment editor tools like grow from seed, refine etc, but it will give me a plain model without textures or possibility to change the contrast on the 3D window.</p>
<p>Thank you for your help!</p>

---

## Post #3 by @lassoan (2019-07-11 14:07 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="1" data-topic="7521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I would like to use the magic wand</p>
</blockquote>
</aside>
<p>“Magic wand” usually refers to selecting similar regions when you click on a single point in the image. This feature is available in “Flood filling” effect in Segment Editor (provided by SegmentEditorExtraEffects extension).</p>
<aside class="quote no-group quote-post-not-found" data-username="muratmaga" data-post="2" data-topic="7521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>all you need to use the Mask Volume (or Split Volume if you want to remove the black space around your segmentation) to mask the dicom.</p>
</blockquote>
</aside>
<p>Here is a short demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" width="" height="">
  </a>
</div>


---
