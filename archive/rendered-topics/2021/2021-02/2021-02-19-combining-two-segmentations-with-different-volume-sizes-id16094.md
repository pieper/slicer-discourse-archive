# Combining two segmentations with different volume sizes

**Topic ID**: 16094
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/combining-two-segmentations-with-different-volume-sizes/16094

---

## Post #1 by @Aep93 (2021-02-19 17:55 UTC)

<p>Hello all,<br>
I have two segmentations and the size of the references volume of these segmentations are different from each other. Now I want to combine these two segmentations and edit them in the Segment Editor module. How is it possible?<br>
How can I manage different sizes of my segmentations? Should I make the sizes of both segmentations exactly the same, if yes, how should I do this?<br>
Thanks in advane</p>

---

## Post #2 by @Aep93 (2021-02-20 00:12 UTC)

<p>Hello all,<br>
I could manage to somehow combine my segmentations. Now, when I go to segment editor, the quality of my segments are considerably different. This is a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c15b13f97afe6cc4e2ff195f0912c3742323d5ef.jpeg" data-download-href="/uploads/short-url/rAvhHIt0xJ93EagXaTj53DpmpCn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c15b13f97afe6cc4e2ff195f0912c3742323d5ef_2_690x372.jpeg" alt="image" data-base62-sha1="rAvhHIt0xJ93EagXaTj53DpmpCn" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c15b13f97afe6cc4e2ff195f0912c3742323d5ef_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c15b13f97afe6cc4e2ff195f0912c3742323d5ef_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c15b13f97afe6cc4e2ff195f0912c3742323d5ef.jpeg 2x" data-dominant-color="7A947A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×578 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I added the segmentation of white part to the segmentation of green part and it can be seen that the qualities are very different. I should note that the quality of white part was not this bad when it was in separate segment. What should I do to solve this problem?<br>
Also, now when I want to paint in segment mesher it takes a lot of time for the combined segmentation while when I want to paint each segmentation separatetly, it is very fast.<br>
Any helps would be greatly appreciated.</p>

---

## Post #3 by @lassoan (2021-02-20 04:25 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="16094">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Now I want to combine these two segmentations and edit them in the Segment Editor module. How is it possible?</p>
</blockquote>
</aside>
<p>You can drag-and-drop segments between segmentations in Data module. The segmentation will be resampled to the resolution of the segmentation’s internal labelmap representation at the next editing operation (not immediately to allow lossless copying/moving of segments between segmentations). If the quality is not sufficiently good then follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">these instructions</a>.</p>
<aside class="quote no-group quote-modified" data-username="Aep93" data-post="2" data-topic="16094">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Also, now when I want to paint in segment mesher it takes a lot of time for the combined segmentation while when I want to paint each segmentation separately, it is very fast.</p>
</blockquote>
</aside>
<p>Meshing two segments is a harder problem than one, so it is normal that meshing takes more time. You can adjust meshing options to find a good balance between meshing speed, memory usage, and size and quality of the created mesh.</p>

---

## Post #4 by @Aep93 (2021-02-20 04:29 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I made a mistake in my previous question, I mentioned “segment mesher” but in fact I meant “segment editor”. I wanted to say that when I want to paint combined segmentation in segment editor, the time is too long, but when I paint each of my segmentations separately (before combination) in segment editor, it is very fast. Do you have any comments in this regard?<br>
Your help is greatly appreciated.</p>

---

## Post #5 by @lassoan (2021-02-20 04:57 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="4" data-topic="16094">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>when I want to paint combined segmentation in segment editor, the time is too long</p>
</blockquote>
</aside>
<p>Slowdown is expected if you copy a segment to a finer resolution segmentation or the two segments are far from each other, but it is hard to tell what is the best way to make the performance better without seeing your data. If you can share an example data set the demonstrates the issue (upload somewhere and post the link) then we can take a look.</p>

---

## Post #6 by @Aep93 (2021-02-22 06:40 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Sure, I will spend a little more time on my model and if I was not able what I want, I will share a sample dataset so that you can take a quick look. Thanks a lot.</p>

---

## Post #7 by @Aep93 (2021-06-01 05:35 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I still have some problems with this. I attached one of the segmentations here. I transformed this segmentation from low-resolution volume to high resolution. However, it is very heavy now. It takes a lot to perform some operations (such as painting) on it. On the other hand, I do not want to reduce its quality as I want to combine it with another segmentation as mentioned above. Can you please take a look at this segmentation and help me to reduce its size.</p>
<p>Download link:<br>
<a href="https://github.com/A-ep93/SlicerTest/blob/main/Segmentation2.seg.nrrd" rel="noopener nofollow ugc">Segmentation</a></p>
<p>Thanks in advance</p>

---

## Post #9 by @Aep93 (2021-06-04 01:53 UTC)

<p>Any help is greatly appreciated. I think the size of my volume gets unnecessarily large when I increase the resolution. I am saying this because I have other models with the same volume size as my “high” resolution volume, but they are very fast.<br>
I am wondering whether I should do anything special when I convert my low res model to high res.<br>
Thanks in advance</p>

---

## Post #10 by @lassoan (2021-06-04 02:00 UTC)

<p>You need to find a good tradeoff between details, accuracy vs computation time and memory usage. Try increasingly finer resolution and see how your segmentation size is changing.</p>

---

## Post #11 by @Aep93 (2021-06-04 04:24 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I will try changing the resolution to find a trade-off between accuracy and memory. Thanks.</p>

---

## Post #12 by @jamessmith (2021-06-05 18:36 UTC)

<p>Interesting and useful discussion. Thanks for sharing, I appreciate that! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
