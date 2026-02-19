---
topic_id: 36557
title: "Shadow Rendering Issue With Transparency"
date: 2024-06-02
url: https://discourse.slicer.org/t/36557
---

# Shadow rendering issue with transparency

**Topic ID**: 36557
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/shadow-rendering-issue-with-transparency/36557

---

## Post #1 by @mohammed_alshakhas (2024-06-02 15:33 UTC)

<p>I find the shadow visibility feature to be so good, I love it but<br>
is it possible to make the effect stronger / weaker?<br>
I wish it were not ON by default<br>
it has an issue when segments are transparent. The attached pic is an example, in reality, it looks worse. the overlapped areas look dark/blurred. ( anterior mandible and ramus)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0d4f8ebb6058989a173fc9e6b3869ed8a6b0f0e.jpeg" data-download-href="/uploads/short-url/pekkcWnRuV3F0zbmcXbGbA7ScfY.jpeg?dl=1" title="Screenshot 2024-06-02 at 18.29.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d4f8ebb6058989a173fc9e6b3869ed8a6b0f0e_2_683x500.jpeg" alt="Screenshot 2024-06-02 at 18.29.42" data-base62-sha1="pekkcWnRuV3F0zbmcXbGbA7ScfY" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d4f8ebb6058989a173fc9e6b3869ed8a6b0f0e_2_683x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d4f8ebb6058989a173fc9e6b3869ed8a6b0f0e_2_1024x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0d4f8ebb6058989a173fc9e6b3869ed8a6b0f0e_2_1366x1000.jpeg 2x" data-dominant-color="4C4E44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-02 at 18.29.42</span><span class="informations">1920×1405 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-03 14:27 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>I find the shadow visibility feature to be so good, I love it but<br>
is it possible to make the effect stronger / weaker?</p>
</blockquote>
</aside>
<p>Yes - see <a href="https://discourse.slicer.org/t/improve-ambient-occlusion-in-volume-rendering/33590/6">here</a>. I just did not get around to integrate this improvement.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>I wish it were not ON by default</p>
</blockquote>
</aside>
<p>It is configurable. You can set it to be on or off by default in application settings / Views / Shadows visibility.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>it has an issue when segments are transparent.</p>
</blockquote>
</aside>
<p>There are some limitations.</p>
<p>Transparent surfaces don’t cast a shadow, so even if you set your opacity to 99%, you won’t see any shadow casted by that model. This can be considered either a feature or a limitation (it may be useful in some cases).</p>
<p>Depth peeling does not seem to work when shadows are enabled. This can be probably fixed, but most likely would need dedicated funding sent to Kitware.</p>

---

## Post #3 by @mohammed_alshakhas (2024-06-03 14:43 UTC)

<p>thank you for your reply<br>
What is depth peeling?  I can’t figure out what it does!</p>

---

## Post #4 by @lassoan (2024-06-03 15:23 UTC)

<p>Depth peeling is required for correct display of transparent surfaces (surfaces need to be ordered based on distance from camera).</p>
<p>Note that you may be able to avoid transparency related issues and have much higher fidelity rendering if you use “Colorize volume” module (it displays the result of segmentation combined with the original image).</p>

---

## Post #5 by @cpinter (2024-06-04 08:44 UTC)

<p>This reminded me a related issue so if you don’t mind I just join this discussion.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f8f747754af5077e8cffdaf850aa3035adfe681.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56376cc531fdca16c61f84edbd75f896f1279736.jpeg">
  </div><p></p>
<p>When using transparency, I frequently see artifacts like this. Any idea what these might be and how to mitigate them? Thank you very much!</p>

---

## Post #6 by @lassoan (2024-06-04 15:22 UTC)

<p>What you show looks like depth peeling is disabled.</p>
<p>It is a known issue that if shadows are enabled then depth peeling does not seem to work:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7780">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7780" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7780" target="_blank" rel="noopener">Semi-transparent models are not rendered correctly if shadows visibility is enabled</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-06-03" data-time="19:42:38" data-timezone="UTC">07:42PM - 03 Jun 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Depth peeling (that makes semi-transparent models appear correctly<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> in 3D views) seems to be incompatible with shadows option. Semi-transparent models may appear incorrectly (backface occlude frontface, kind of appearing inside out) if "Shadows visibility" option is enabled in the 3D view.

## Environment
- Slicer version: Slicer-5.7.0 2024-06-02
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Is it the issue that you are seeing?</p>

---

## Post #7 by @cpinter (2024-06-05 09:58 UTC)

<p>I cannot confirm if this is what I see - I don’t know what kind of arfiact the lack of depth peeling would cause in this case. Although I can confirm that this artifact is only visible with the shadows enabled, and if I disable SSAO they disappear too.</p>
<p>I saw the ticket yesterday, thanks for creating it! If there is a way to at least verify if depth peeling is the issue here, please let me know and I’ll investigate. Thank you!</p>

---

## Post #8 by @lassoan (2024-06-05 12:12 UTC)

<p>You can confirm by disabling shadows and toggling depth peeling on and off. If disabling depth peeling produces the same artifacts then it means that the problem is due to depth peeling ineffective or not performed when shadows are enabled.</p>
<p>It may be due to shadows messing up the z buffer, rendering passes missed or performed in the wrong order, or maybe combination of shadows+depth peeling would require implementing some special combined shader code.</p>
<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> is it expected that SSAO interferes with depth peeling?</p>

---

## Post #9 by @LucasGandel (2024-06-05 12:19 UTC)

<p>I’ve been following the discussion but need to perform a few tests locally and check the current order of passes before pointing you in the right direction. I also recall SSAO was interfering with the translucent pass in VTK but thought it had been fixed. I’ll try to dig a bit into this in the coming days and will share updates, but your statement is definitely correct:</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It may be due to shadows messing up the z buffer, rendering passes missed or performed in the wrong order, or maybe combination of shadows+depth peeling would require implementing some special combined shader code.</p>
</blockquote>
</aside>

---

## Post #10 by @cpinter (2024-06-05 12:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If disabling depth peeling produces the same artifacts then it means that the problem is due to depth peeling ineffective or not performed when shadows are enabled.</p>
</blockquote>
</aside>
<p>This I tried, but there were no such artifacts. It may be possible though that depth peeling of the shadows themselves produce these, but that’s the part I cannot confirm.</p>
<aside class="quote no-group" data-username="LucasGandel" data-post="9" data-topic="36557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>I’ll try to dig a bit into this in the coming days and will share updates</p>
</blockquote>
</aside>
<p>Much appreciated <a class="mention" href="/u/lucasgandel">@LucasGandel</a> !</p>

---

## Post #11 by @cpinter (2024-06-05 14:08 UTC)

<p>I showed <a class="mention" href="/u/lassoan">@lassoan</a> this artifact, and the conclusion was that it is indeed the depth peeling. I only kept the jaw bone segment, and in this video you can see that the far side of the jaw, while rotating along AP, became “in front of” the near side, causing the artifact. In the second half of the video I disabled SSAO (this part is not shown in the video as the panel is not in the view) and then also disable depth peeling (this can be seen though), and then a similar effect can be seen, the only difference is that the shadows are not added, so it is not that emphasized.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c68a42e39028eb157df5298458d15f66d83e85de.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b215c0ac408edfb49d9b55c72cbbc61d8953ac4f.jpeg">
  </div><p></p>

---

## Post #12 by @LucasGandel (2024-06-17 12:26 UTC)

<p>Sorry for the late reply. I am still not sure what is exactly producing the artefacts you initially reported <a class="mention" href="/u/cpinter">@cpinter</a>, but at least I could investigate the issue mentioned by <a class="mention" href="/u/lassoan">@lassoan</a> which is the root cause for the transparent models not being supported with shadows. For the record, I answered on the issue directly: <a href="https://github.com/Slicer/Slicer/issues/7780" class="inline-onebox" rel="noopener nofollow ugc">Semi-transparent models are not rendered correctly if shadows visibility is enabled · Issue #7780 · Slicer/Slicer · GitHub</a></p>

---

## Post #13 by @mohammed_alshakhas (2024-06-25 17:32 UTC)

<p>new issue i had today</p>
<p>shoadow visibilty ON , depth peel OFF</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a3ccb29948ff5c549ca500fe9b6af343e99fc30.jpeg" data-download-href="/uploads/short-url/hrmv4bwXwOv4x8DTo9Cs5OiN960.jpeg?dl=1" title="Screenshot 2024-06-25 at 20.28.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3ccb29948ff5c549ca500fe9b6af343e99fc30_2_690x292.jpeg" alt="Screenshot 2024-06-25 at 20.28.45" data-base62-sha1="hrmv4bwXwOv4x8DTo9Cs5OiN960" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3ccb29948ff5c549ca500fe9b6af343e99fc30_2_690x292.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3ccb29948ff5c549ca500fe9b6af343e99fc30_2_1035x438.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3ccb29948ff5c549ca500fe9b6af343e99fc30_2_1380x584.jpeg 2x" data-dominant-color="9C868A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-25 at 20.28.45</span><span class="informations">1920×814 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>shoadow visibilty OFF  , depth peel OFF</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6a5897695a9d2300d017e55f375cf4229034958.jpeg" data-download-href="/uploads/short-url/nMdV7TiAMlsjgC9R7RM33bzAqFi.jpeg?dl=1" title="Screenshot 2024-06-25 at 20.29.18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a5897695a9d2300d017e55f375cf4229034958_2_641x500.jpeg" alt="Screenshot 2024-06-25 at 20.29.18" data-base62-sha1="nMdV7TiAMlsjgC9R7RM33bzAqFi" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a5897695a9d2300d017e55f375cf4229034958_2_641x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a5897695a9d2300d017e55f375cf4229034958_2_961x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6a5897695a9d2300d017e55f375cf4229034958_2_1282x1000.jpeg 2x" data-dominant-color="D7B2B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-25 at 20.29.18</span><span class="informations">1882×1466 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @mohammed_alshakhas (2024-12-16 12:13 UTC)

<p>i found a use for the transparency issue i mentoed bedore <a class="mention" href="/u/lassoan">@lassoan</a> .</p>
<p>here im using teeth as opaque and jaw as transparent . i can alter the shadow on the solid object and it seems to make a good visualization .<br>
like only altering lightining parameter on one object .</p>
<p>is that possible other way , was this intedned ?</p>
<p>thanks</p>

---

## Post #15 by @mohammed_alshakhas (2024-12-16 13:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0704d76907a161a39eb88214242da207df1dc739.jpeg" data-download-href="/uploads/short-url/105IkD2TrShdh0b3Hog2yl5Tnmh.jpeg?dl=1" title="Screenshot 2024-12-16 at 15.09.07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0704d76907a161a39eb88214242da207df1dc739_2_634x500.jpeg" alt="Screenshot 2024-12-16 at 15.09.07" data-base62-sha1="105IkD2TrShdh0b3Hog2yl5Tnmh" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0704d76907a161a39eb88214242da207df1dc739_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0704d76907a161a39eb88214242da207df1dc739_2_951x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0704d76907a161a39eb88214242da207df1dc739.jpeg 2x" data-dominant-color="E5E3E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-16 at 15.09.07</span><span class="informations">1154×910 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
