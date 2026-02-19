---
topic_id: 40230
title: "Slice View Does Not Fit To Background On Loading A Volume"
date: 2024-11-17
url: https://discourse.slicer.org/t/40230
---

# Slice view does not fit to background on loading a volume

**Topic ID**: 40230
**Date**: 2024-11-17
**URL**: https://discourse.slicer.org/t/slice-view-does-not-fit-to-background-on-loading-a-volume/40230

---

## Post #1 by @chir.set (2024-11-17 13:44 UTC)

<p>Usually, and in Slicer stable, when loading a volume of any dimension, the slice views would fit the extent of the volume nicely.</p>
<p>That’s no longer the case since recently. The image below shows the effect when a small volume is loaded (212 x 92 x 114) with spacing 0.6 x 0.6 x 0.6: on loading, with FitSliceToAll() and with FitSliceToBackground().</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe2491e41288a83f09386c1740ea956a7743b787.gif" alt="FitSlice" data-base62-sha1="AgfCWtcXBX5Tgo6v7zHE3mH83RR" width="690" height="406" class="animated"></p>
<p>It seems that the problem is with FitSliceToAll(). Formerly, it would behave like FitSliceToBackground(). Is it how it should be considered now, a feature?</p>
<p>Slicer is started with --ignore-slicerrc and the slice composite node has a single background scalar volume node. Using self-built preview on Linux.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2024-11-17 19:52 UTC)

<p>Can you share an example volume that leads to the issue?  I tried the latest nightly preview build of today and didn’t see anything unusual.</p>

---

## Post #3 by @chir.set (2024-11-17 20:42 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="40230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>share an example volume</p>
</blockquote>
</aside>
<p>Sure, here is <a href="https://disk.yandex.com/d/zlErI05tuga7vg" rel="noopener nofollow ugc">one</a>, cropped from CTA-cardio. I just tested with 5.7.0-2024-11-15 r33115 / 7438bf2 from your website with the same unexpected result. It’s not a big issue, I just reported it in case there might be something to fix.</p>

---

## Post #4 by @pieper (2024-11-17 21:13 UTC)

<p>I can confirm this is a regression - the nightly preview is first below, and the latest 5.6.2 release is below that.  All I did was drag-and-drop the file provided by <a class="mention" href="/u/chir.set">@chir.set</a> on each.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4f9d28d57d68dc48fc12cdf488f943003369bf.png" data-download-href="/uploads/short-url/hs0P38PuM2w1tgJCvB2U3Wyo0sn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a4f9d28d57d68dc48fc12cdf488f943003369bf_2_565x499.png" alt="image" data-base62-sha1="hs0P38PuM2w1tgJCvB2U3Wyo0sn" width="565" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a4f9d28d57d68dc48fc12cdf488f943003369bf_2_565x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a4f9d28d57d68dc48fc12cdf488f943003369bf_2_847x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a4f9d28d57d68dc48fc12cdf488f943003369bf_2_1130x998.png 2x" data-dominant-color="737075"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1276×1128 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/591854313b64ed96c9f5276a09edccb52b9125a3.jpeg" data-download-href="/uploads/short-url/cIaConRScBw4Lg0xtm91dsAMgP9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591854313b64ed96c9f5276a09edccb52b9125a3_2_562x500.jpeg" alt="image" data-base62-sha1="cIaConRScBw4Lg0xtm91dsAMgP9" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591854313b64ed96c9f5276a09edccb52b9125a3_2_562x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591854313b64ed96c9f5276a09edccb52b9125a3_2_843x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/591854313b64ed96c9f5276a09edccb52b9125a3_2_1124x1000.jpeg 2x" data-dominant-color="88858A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×1130 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-11-18 21:40 UTC)

<p>Indeed, <code>Reset to field of view</code> does not work for this volume. How to reproduce: link slice views, click <code>Reset to field of view</code> button in any of the slice views.</p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> to make sure we take care of this before the new stable release, would you mind submitting a bug report to <a href="http://issues.slicer.org">issues.slicer.org</a> and post the link here? Thank you!</p>

---

## Post #6 by @chir.set (2024-11-19 07:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="40230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>post the link here</p>
</blockquote>
</aside>
<p>The issue is reported <a href="https://github.com/Slicer/Slicer/issues/8053" rel="noopener nofollow ugc">here</a>.</p>
<p>Thank you all.</p>

---

## Post #7 by @lassoan (2024-11-25 17:54 UTC)

<p>Fix is provided in this pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8063">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8063" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8063" target="_blank" rel="noopener">Fix fit slice to volume</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-fit-slice-to-volume</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-22" data-time="13:50:39" data-timezone="UTC">01:50PM - 22 Nov 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 18 files with 89 additions and 146 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8063/files" target="_blank" rel="noopener">
            <span class="added">+89</span>
            <span class="removed">-146</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixed and fit slice to volume and made it work consistently for both when backgr<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8063" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ound clipping is enabled (default) or disabled.

&lt;img width="1394" alt="image" src="https://github.com/user-attachments/assets/1936df0b-75ba-45ef-89bf-0d059423ca4c"&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
