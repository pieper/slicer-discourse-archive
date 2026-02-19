---
topic_id: 20519
title: "Erase Using A Segment As Only Editable Area"
date: 2021-11-07
url: https://discourse.slicer.org/t/20519
---

# Erase using a segment as only editable area

**Topic ID**: 20519
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/erase-using-a-segment-as-only-editable-area/20519

---

## Post #1 by @Michele_Bailo (2021-11-07 17:35 UTC)

<p>Hi everyone,<br>
I’m using a Slicer version 4.13.0-2021-06-03 for Windows.<br>
I noticed that the function “Masking - Editable area - Inside segment <em>XXX</em>” doesn’t seem to apply to the “Erase” function of the “Segment Editor” (it works correctly only with the “Paint” function)</p>
<p>Thank you very much for your support!</p>
<p>MB!</p>

---

## Post #2 by @lassoan (2021-11-07 18:29 UTC)

<p>Please try with the latest Slicer Preview Release and let us know if it does not work as you expect.</p>

---

## Post #3 by @Michele_Bailo (2021-11-08 14:33 UTC)

<p>I tried with the latest version but unfortunately it doesn’t work properly either</p>
<p>many thanks</p>
<p>MB</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbd5563032345acf45780fdd15bbec6eb9898397.jpeg" data-download-href="/uploads/short-url/t5bZT8yx4wSiHx9zSQgEtXTl2N9.jpeg?dl=1" title="Screenshot 2021-11-08 at 15.29.53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbd5563032345acf45780fdd15bbec6eb9898397_2_690x388.jpeg" alt="Screenshot 2021-11-08 at 15.29.53" data-base62-sha1="t5bZT8yx4wSiHx9zSQgEtXTl2N9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbd5563032345acf45780fdd15bbec6eb9898397_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbd5563032345acf45780fdd15bbec6eb9898397_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbd5563032345acf45780fdd15bbec6eb9898397_2_1380x776.jpeg 2x" data-dominant-color="6D6E6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-11-08 at 15.29.53</span><span class="informations">1920×1080 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d161802cd5bbb26de76613207173e05bb396d02f.jpeg" data-download-href="/uploads/short-url/tSgGvm01CK9kaCEGc4aevEIGwaj.jpeg?dl=1" title="Screenshot 2021-11-08 at 15.30.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161802cd5bbb26de76613207173e05bb396d02f_2_690x388.jpeg" alt="Screenshot 2021-11-08 at 15.30.08" data-base62-sha1="tSgGvm01CK9kaCEGc4aevEIGwaj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161802cd5bbb26de76613207173e05bb396d02f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161802cd5bbb26de76613207173e05bb396d02f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d161802cd5bbb26de76613207173e05bb396d02f_2_1380x776.jpeg 2x" data-dominant-color="6D6E6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-11-08 at 15.30.08</span><span class="informations">1920×1080 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-11-08 17:36 UTC)

<p>I was able to reproduce this.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you have a look at this? If it is not an easy fix then you can submit a bug report and post the link here.</p>
<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> As a workaround, you can create a temporary segment and paint with that instead of erasing. When you finished “erasing” then you can remove that temporary segment.</p>

---

## Post #5 by @Michele_Bailo (2021-11-08 19:14 UTC)

<blockquote>
<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> As a workaround, you can create a temporary segment and paint with that instead of erasing. When you finished “erasing” then you can remove that temporary segment.</p>
</blockquote>
<p>Yes, this is exactly what I have been doing for the past months. But I thought I’d tell you about it because I wasn’t sure if I was doing something wrong or if there were other ways.<br>
Thank you so much for your availability!</p>

---

## Post #6 by @hherhold (2022-08-24 13:32 UTC)

<p>Has this been looked into at all?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #7 by @jamesobutler (2022-08-24 14:37 UTC)

<p>Here I have Segment 1 and Segment 2 painted. I have selected the “Erase” effect, selected Segment_1 in the segment table as my active segment, changed the editable area to “Inside Segment_1” and placed my cursor over the boundary line.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfe914015a8f9ae03492b424dc2a7434c5ea3864.jpeg" data-download-href="/uploads/short-url/rnIyZRkTaDRZ0jY1oLiYs0f0InO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfe914015a8f9ae03492b424dc2a7434c5ea3864_2_690x368.jpeg" alt="image" data-base62-sha1="rnIyZRkTaDRZ0jY1oLiYs0f0InO" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfe914015a8f9ae03492b424dc2a7434c5ea3864_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfe914015a8f9ae03492b424dc2a7434c5ea3864_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfe914015a8f9ae03492b424dc2a7434c5ea3864_2_1380x736.jpeg 2x" data-dominant-color="6F6F6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1024 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then when I click to erase, it erased only inside Segment_1 and did not erase Segment_2 as well which had been contained inside my erase circle.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fab00196ce0a088e61e2b5c1d5c760f36dc8719.jpeg" data-download-href="/uploads/short-url/kuWDZ3tQPDioXtM3atlbpUZLkYF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fab00196ce0a088e61e2b5c1d5c760f36dc8719_2_690x368.jpeg" alt="image" data-base62-sha1="kuWDZ3tQPDioXtM3atlbpUZLkYF" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fab00196ce0a088e61e2b5c1d5c760f36dc8719_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fab00196ce0a088e61e2b5c1d5c760f36dc8719_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fab00196ce0a088e61e2b5c1d5c760f36dc8719_2_1380x736.jpeg 2x" data-dominant-color="6F6F6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1026 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I could also select Segment_2 as the active segment, then select “Inside Segment_1” and oddly edit another segment (Segment_1) that doesn’t match my currently active segment (Segment_2) in the segment table.</p>

---

## Post #8 by @hherhold (2022-08-24 14:48 UTC)

<p>Thanks James. My use case is slightly different:</p>
<p>I have multiple segments visible and multiple hidden. I want to erase all visible segments but leave hidden unchanged. If I click “erase all segments” AND select editable area inside all visible segments, when I erase, it erases ALL segments, not just the visible ones.</p>
<p>Hopefully that makes sense…</p>

---

## Post #9 by @lassoan (2022-08-28 19:35 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> should be able to have a look at this when he gets back from vacation in a week or two. You can ping him here or submit a bug report at <a href="http://issues.slicer.org">issues.slicer.org</a> and assign the issue to Kyle Sunderland.</p>

---

## Post #10 by @hherhold (2022-08-28 19:49 UTC)

<p>Sounds good, no rush. In the meantime I’ve been using your suggested workaround to make a new segment, paint that, and then subtract. Thanks!</p>

---

## Post #11 by @lassoan (2022-08-29 04:10 UTC)

<p>There is no need to subtract: if you enable overwrite then it is enough to paint in the new segment. In the very end you can delete that new segment.</p>

---

## Post #12 by @Sunderlandkyl (2022-09-06 20:22 UTC)

<p>I don’t seem to be able to reproduce the issue.</p>
<p>Can you clarify if the setting that is causing the unexpected behavior is “Editable area” or “Modify other segments”?</p>

---

## Post #13 by @hherhold (2022-09-12 12:24 UTC)

<p>Sorry for the slow reply.</p>
<p>I think my confusion was the inconsistency in behavior between scissors and erase. In scissors, there is an “Apply to all segments” checkbox, which is actually “apply to all visible segments”. I thought (incorrectly) that the “Erase all segments” checkbox would behave similarly, but it does exactly what it says it does - erase all segments, visible or not. The tooltips for both checkboxes (which I had turned off, unfortunately) do document the appropriate behavior correctly.</p>
<p>Erase all segments <em>does</em> work correctly with Editable area set appropriately, I do not see any issue with that.</p>
<p>So I guess this is a case of “nothing to see here, move along…”</p>
<p>Thanks!</p>

---

## Post #14 by @jamesobutler (2022-09-12 14:08 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="13" data-topic="20519">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>In scissors, there is an “Apply to all segments” checkbox, which is actually “apply to all visible segments”. I thought (incorrectly) that the “Erase all segments” checkbox would behave similarly, but it does exactly what it says it does - erase all segments, visible or not.</p>
</blockquote>
</aside>
<p>We should probably update the wording to clarify these meanings based on the confusion you faced which I’m sure others face as well.</p>
<p>“Apply to visible segments” and “Erase all segments” could be options where using “all” is only used when referring to visible and non-visible segments.</p>

---

## Post #15 by @jamesobutler (2022-09-12 22:44 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> see if the following naming change proposed by <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> makes sense</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6526">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6526" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6526" target="_blank" rel="noopener nofollow ugc">ENH: Update scissors "Apply to visible segments" label</a>
    </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Sunderlandkyl:scissors_apply_visible_label</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-09-12" data-time="19:51:30" data-timezone="UTC">07:51PM - 12 Sep 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
          <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
          Sunderlandkyl
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6526/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The "Apply to all segments" label was misleading, since enabling it caused the s<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6526" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">cissors effect to only apply on all visible segments.
Changed label from "Apply to all segments" to "Apply to visible segments".

See: https://discourse.slicer.org/t/erase-using-a-segment-as-only-editable-area/20519/13</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @lassoan (2022-09-13 02:20 UTC)

<p>We used the “Apply to all segments” as checkbox  label to keep things simpler and shorter (to increase the chance that users read and understand the label). However, this is the second time that users report the current behavior as an error, so it seems that the current label is misleading and using a longer but more accurate label is justified. We’ll proceed with the changes that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> proposed.</p>

---

## Post #17 by @hherhold (2022-09-13 14:15 UTC)

<p>This change makes sense to me.</p>
<p>Thanks!</p>

---
