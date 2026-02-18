# Semi automated segmentation

**Topic ID**: 7761
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/semi-automated-segmentation/7761

---

## Post #1 by @tenzin_kunkyab (2019-07-25 18:57 UTC)

<p>Hi Developers,</p>
<p>Thank you very much for continuing to improve 3d Slicer. It has been a great help in my project.</p>
<p>I would like to ask about GrowCut Algorithm, in the newly built version, there isn’t seem to be grow cut algorithm and I realized there is a watershed option that works the similar way?</p>
<p>The question is where can I find Growcut segmentation option in the new release and does watershed give the same quality of accuracy of segmentation?</p>
<p>Thank you very much once again,<br>
best<br>
Tenzin</p>

---

## Post #2 by @lassoan (2019-07-25 19:13 UTC)

<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="1" data-topic="7761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>in the newly built version, there isn’t seem to be grow cut algorithm</p>
</blockquote>
</aside>
<p>There is, implemented in “Grow from seeds” effect.</p>
<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="1" data-topic="7761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>does watershed give the same quality of accuracy of segmentation?</p>
</blockquote>
</aside>
<p>Watershed enforces a spatial smoothness constrain, therefore created segment edges are always smooth, while Grow from seeds require applying smoothing as a separate step (using Smoothing effect, Joint smoothing method). However, Watershed is recomputed from scratch each time an input seed is modified, while Grow from seeds effect is updated incrementally, therefore the latter is much better suited for interactive editing.</p>

---

## Post #3 by @tenzin_kunkyab (2019-07-25 23:18 UTC)

<p>Hi Lassoan,</p>
<p>thank you so much, by any chance is oneCut graph segmentation algorithm implemented in 3D slicer?</p>
<p>best<br>
Tenzin</p>

---

## Post #4 by @lassoan (2019-07-26 01:59 UTC)

<aside class="quote no-group" data-username="tenzin_kunkyab" data-post="3" data-topic="7761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tenzin_kunkyab/48/3916_2.png" class="avatar"> tenzin_kunkyab:</div>
<blockquote>
<p>by any chance is oneCut graph segmentation algorithm implemented in 3D slicer</p>
</blockquote>
</aside>
<p>Yes, I think it is available. Do you mean <a href="http://www.csd.uwo.ca/~olga/Papers/iccv13_one_cut.pdf">this one</a>?</p>

---

## Post #5 by @tenzin_kunkyab (2019-07-26 18:50 UTC)

<p>Hii Andras,</p>
<p>yes this one, and how do I implement it? I didn’t find any resource yet for this online?</p>
<p>best<br>
Tenzin</p>

---

## Post #6 by @lassoan (2019-07-26 20:00 UTC)

<p>It is already available as a Slicer extension but it needs a little work to make it work with recent Slicer versions. I can have a look at it next week.</p>
<p>Until then, you can use Grow from seeds or Watershed effects, which should work just as well.</p>

---

## Post #7 by @tenzin_kunkyab (2019-07-26 20:33 UTC)

<p>thank you very much,</p>
<p>best<br>
Tenzin</p>

---

## Post #8 by @tenzin_kunkyab (2019-07-30 18:02 UTC)

<p>between which extension is Onecut in grabcut is it? I would like to try working with all of them.</p>
<p>best<br>
Tenzin</p>

---

## Post #9 by @lassoan (2019-07-30 18:16 UTC)

<p>The extension is <a href="https://github.com/Slicer/SlicerGraphCutSegment" rel="nofollow noopener">here</a>, it is not yet updated to work with recent Slicer Preview Releases but should be available later this week.</p>

---

## Post #10 by @tenzin_kunkyab (2019-07-30 18:18 UTC)

<p>I will check, thanks so much Lassoan!</p>
<p>I will continue checking this week.</p>
<p>best<br>
Tenzin</p>

---

## Post #11 by @tenzin_kunkyab (2019-07-30 20:11 UTC)

<p>Hi Lassoan,</p>
<p>I get the following error when I tried to find GraphCut Segment in the slicer 4.10.2 version.</p>
<p>“No extensions found for win:64-bit, revision: ‘28257’. Please try a different combination”</p>
<p>best<br>
tenzin</p>

---
