---
topic_id: 14857
title: "Masking Overwrite Visible Allowing Overlap Instead Of Overwr"
date: 2020-12-02
url: https://discourse.slicer.org/t/14857
---

# Masking: "Overwrite visible" allowing overlap instead of overwriting

**Topic ID**: 14857
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/masking-overwrite-visible-allowing-overlap-instead-of-overwriting/14857

---

## Post #1 by @sioussou (2020-12-02 23:49 UTC)

<p>Problem report for Slicer 4.11.20200930 win-amd64: in segment editor, I’ve set the masking option “Modify other segments” to “Overwrite visible” before applying smoothing [closing (fill holes) - 1.00mm]. If any of my segments is then hidden before applying the effect, the visible segments end up overlapping instead of one overwriting the other as expected.</p>
<p>Confirmed that performing the analogous operation in Slicer 4.10.2 (same volume, segmentation, “Overwrite other segments” set to “Visible segments”) results in expected overwriting behavior.</p>
<p>Is this a bug or did the functionality of this masking option change? If it changed, is there still a way to cause an effect to overwrite visible segments as in 4.10.2?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2020-12-03 00:07 UTC)

<p>I can’t reproduce this:<br>
This is what I did: created yellow and green segments, and then hid the yellow and create the brown segment using the overwrite to visible segments. As expect it overwrote the green but, overlapped with yellow since it was hidden at the time.</p>
<p>Is this not the behavior you expect?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5297458391a90606b50eca695d647e37605c45.png" data-download-href="/uploads/short-url/zIsjHELXo9J6QekmOHTCMbxryst.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5297458391a90606b50eca695d647e37605c45.png" alt="image" data-base62-sha1="zIsjHELXo9J6QekmOHTCMbxryst" width="583" height="500" data-dominant-color="8B8B7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">667×572 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-12-03 05:05 UTC)

<aside class="quote no-group" data-username="sioussou" data-post="1" data-topic="14857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sioussou/48/9045_2.png" class="avatar"> sioussou:</div>
<blockquote>
<p>Problem report for Slicer 4.11.20200930 win-amd64: in segment editor, I’ve set the masking option “Modify other segments” to “Overwrite visible” before applying smoothing [closing (fill holes) - 1.00mm]. If any of my segments is then hidden before applying the effect, the visible segments end up overlapping instead of one overwriting the other as expected</p>
</blockquote>
</aside>
<p>This is the correct behavior. “Overwrite visible” means that only visible segments are overwritten.</p>

---

## Post #4 by @sioussou (2020-12-03 18:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="14857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This is what I did: created yellow and green segments, and then hid the yellow and create the brown segment using the overwrite to visible segments. As expect it overwrote the green but, overlapped with yellow since it was hidden at the time.</p>
</blockquote>
</aside>
<p>Confirming that if I follow the procedure you’ve described I reproduce the same results and this is the behavior I expect.</p>
<p>However, the problem I’m seeing occurs under slightly different circumstances:</p>
<ol>
<li>Create green, yellow, and brown segments<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999192f6526d19f55c739de1a2cddad0b051bd54.jpeg" data-download-href="/uploads/short-url/lUwWwGFkuK4BSpOTPBQA0oH5Zsg.jpeg?dl=1" title="step-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/999192f6526d19f55c739de1a2cddad0b051bd54_2_690x228.jpeg" alt="step-1" data-base62-sha1="lUwWwGFkuK4BSpOTPBQA0oH5Zsg" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/999192f6526d19f55c739de1a2cddad0b051bd54_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/999192f6526d19f55c739de1a2cddad0b051bd54_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999192f6526d19f55c739de1a2cddad0b051bd54.jpeg 2x" data-dominant-color="ACAEAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step-1</span><span class="informations">1197×397 61.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Hide brown segment</li>
<li>Switch “Modify other segments” to Overwrite visible</li>
<li>Apply smoothing [closing (fill holes) - 3.0mm] to yellow<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48abbe2ad0f5d2cc27d706526f773458f892e9c6.png" data-download-href="/uploads/short-url/amSkMym8rix3kiDgv2mknELu04e.png?dl=1" title="step-4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48abbe2ad0f5d2cc27d706526f773458f892e9c6_2_689x228.png" alt="step-4" data-base62-sha1="amSkMym8rix3kiDgv2mknELu04e" width="689" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48abbe2ad0f5d2cc27d706526f773458f892e9c6_2_689x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48abbe2ad0f5d2cc27d706526f773458f892e9c6_2_1033x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48abbe2ad0f5d2cc27d706526f773458f892e9c6.png 2x" data-dominant-color="ACAFAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step-4</span><span class="informations">1196×396 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>Since yellow and green are visible, I’m expecting the smoothing effect on yellow to overwrite parts of green; instead they end up overlapping, which can be further confirmed by hiding the yellow layer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a47d12308b91d0e0a60749a2f2711e55a0efd13.png" data-download-href="/uploads/short-url/factH64JecpBcCheLXy0N1Hd1jd.png?dl=1" title="step-4-confirm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a47d12308b91d0e0a60749a2f2711e55a0efd13_2_690x230.png" alt="step-4-confirm" data-base62-sha1="factH64JecpBcCheLXy0N1Hd1jd" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a47d12308b91d0e0a60749a2f2711e55a0efd13_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a47d12308b91d0e0a60749a2f2711e55a0efd13_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a47d12308b91d0e0a60749a2f2711e55a0efd13.png 2x" data-dominant-color="ACAEAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step-4-confirm</span><span class="informations">1198×400 91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2020-12-03 18:21 UTC)

<p>Himm, this looks like a bug, perhaps <a class="mention" href="/u/lassoan">@lassoan</a> can comment. Meanwhile if you need to make progress, you can subtract yellow from green using <code>logical operators</code> to get what you need.</p>

---

## Post #6 by @lassoan (2020-12-04 01:31 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has fixed this recently. The problem is not reproducible in Slicer Preview Release.</p>

---

## Post #7 by @sioussou (2020-12-08 13:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="14857" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has fixed this recently. The problem is not reproducible in Slicer Preview Release.</p>
</blockquote>
</aside>
<p>Conducted the test from my previous post in the most recent Slicer Preview Release (Slicer 4.13.0-2020-12-07 win-amd64) and the issue is still present <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @jamesobutler (2020-12-08 14:03 UTC)

<p>I was able to replicate using Slicer 4.13.0-2020-12-07 as well. There is different behavior if Segment_3 is hidden or shown when applying “Closing (fill holes)” smoothing to the selected visible Segment_2.</p>
<ol>
<li>My 3 segments originally applied with default “Overwrite all”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab91db7a779d38da84bb5a2d4e79f03d410ab27f.jpeg" data-download-href="/uploads/short-url/otM90Je0sQLPS8WFGMP9t71u4ij.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab91db7a779d38da84bb5a2d4e79f03d410ab27f_2_690x373.jpeg" alt="image" data-base62-sha1="otM90Je0sQLPS8WFGMP9t71u4ij" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab91db7a779d38da84bb5a2d4e79f03d410ab27f_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab91db7a779d38da84bb5a2d4e79f03d410ab27f_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab91db7a779d38da84bb5a2d4e79f03d410ab27f_2_1380x746.jpeg 2x" data-dominant-color="888887"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Segment_3 remains visible and applying “Closing (fill holes)” for Segment_2 with “Overwrite visible”. Segment_2 is filled in correctly and also correctly overwrites Segment_1. <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0316596c1ead14c6c2bd94e16725082b1262108a.jpeg" data-download-href="/uploads/short-url/rjjz5eyJ26SINEyyrbWnQqHzaa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0316596c1ead14c6c2bd94e16725082b1262108a_2_690x373.jpeg" alt="image" data-base62-sha1="rjjz5eyJ26SINEyyrbWnQqHzaa" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0316596c1ead14c6c2bd94e16725082b1262108a_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0316596c1ead14c6c2bd94e16725082b1262108a_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0316596c1ead14c6c2bd94e16725082b1262108a_2_1380x746.jpeg 2x" data-dominant-color="888887"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>Undo that last action and instead hide Segment_3 and then select Segment_2 again and applying “Closing (fill holes)” for Segment_2 with “Overwrite visible”. Segment_2 new area from smoothing is overlapping Segment_1 instead of overwriting. <img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8901d3adc2732c5f6f1e02ba9c03a1e89e3bb0.jpeg" data-download-href="/uploads/short-url/cUUvxJyIb0JrFMNyfCwrN3CXbHO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8901d3adc2732c5f6f1e02ba9c03a1e89e3bb0_2_690x373.jpeg" alt="image" data-base62-sha1="cUUvxJyIb0JrFMNyfCwrN3CXbHO" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8901d3adc2732c5f6f1e02ba9c03a1e89e3bb0_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8901d3adc2732c5f6f1e02ba9c03a1e89e3bb0_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a8901d3adc2732c5f6f1e02ba9c03a1e89e3bb0_2_1380x746.jpeg 2x" data-dominant-color="888887"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>

---

## Post #9 by @lassoan (2020-12-09 06:08 UTC)

<p>Thanks a lot, based on your description I was able to reproduce this behavior and it is indeed incorrect. I’ve filed a bug report for it:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5338" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5338" target="_blank" rel="noopener">Segment Editor "overwrite visible segments" mode sometimes allow overlap</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-09" data-time="05:02:55" data-timezone="UTC">05:02AM - 09 Dec 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">If "Overwrite visible" mode is enabled and there is a hidden segment then visible segments are not overwritten (which would be...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
