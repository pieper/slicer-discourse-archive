---
topic_id: 12071
title: "Question On Using Scissors"
date: 2020-06-17
url: https://discourse.slicer.org/t/12071
---

# Question on using Scissors

**Topic ID**: 12071
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/question-on-using-scissors/12071

---

## Post #1 by @Deepa (2020-06-17 13:40 UTC)

<p>Hello,</p>
<p>I have loaded 2D slices using <code>Image Stacks</code>. Before reconstructing 3D volume using these slices, I’d like to use the <code>Scissors</code> effect in <code>Segment Editor</code> to edit only the region shown in the image below (rectangle -yellow)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d04f9942a6017df1c5cc2d9fc6e6a461c908bc0.png" data-download-href="/uploads/short-url/hPYleDltLuPYU2LqRg2HjZIKA9i.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d04f9942a6017df1c5cc2d9fc6e6a461c908bc0_2_345x150.png" alt="Untitled" data-base62-sha1="hPYleDltLuPYU2LqRg2HjZIKA9i" width="345" height="150" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d04f9942a6017df1c5cc2d9fc6e6a461c908bc0_2_345x150.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d04f9942a6017df1c5cc2d9fc6e6a461c908bc0_2_517x225.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d04f9942a6017df1c5cc2d9fc6e6a461c908bc0_2_690x300.png 2x" data-dominant-color="797A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1664×726 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I 've selected <code>erase outside</code>. But the region outside the rectangle has not been erased. I’m not sure if I have missed any step.</p>
<p>Suggestions will be highly appreciated!</p>

---

## Post #2 by @muratmaga (2020-06-17 15:00 UTC)

<p>As the name implies, <code>segment editor</code> edits segments. Your segment is blank, so there is nothing to erase from. First define segment (via threshold perhaps), then you can remove any selection with scissors tool.</p>
<p>If your goal is to make a smaller volume than the original, then use the <code>crop volume</code> module.</p>

---

## Post #3 by @Deepa (2020-06-17 15:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Your segment is blank, so there is nothing to erase from.</p>
</blockquote>
</aside>
<p>Thank you, I just realized that the SegmentEditorExtraEffects plugin has to be installed to use the mask volume after selecting the region using scissors.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If your goal is to make a smaller volume than the original, then use the <code>crop volume</code> module.</p>
</blockquote>
</aside>
<p>Could you please have a look at <a href="https://discourse.slicer.org/t/resampling-a-volume-and-image-spacing/12066/2">this</a> post?</p>

---
