---
topic_id: 36620
title: "Deactivation Of No Gpu Is Detected"
date: 2024-06-06
url: https://discourse.slicer.org/t/36620
---

# Deactivation of: No Gpu is detected

**Topic ID**: 36620
**Date**: 2024-06-06
**URL**: https://discourse.slicer.org/t/deactivation-of-no-gpu-is-detected/36620

---

## Post #1 by @farzad2020 (2024-06-06 11:08 UTC)

<p>Hi,</p>
<p>I’m using the Python console to run the Total Segmentator (for automatic segmentation). However, when once the segmentation is started (applied) via code, the attached dialogue box comes up to be clicked (Fast or Full segmentation). I’m wondering if there is a way to deactivate in advance to avoid the pop-up of this dialogue box? Because clicking each time interrupts the automation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37007af4e60914a7aae69cd109dc5c2290c0da5.png" data-download-href="/uploads/short-url/yJy30xoEUIgAp0MDO5aLhbcitQ9.png?dl=1" title="86" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37007af4e60914a7aae69cd109dc5c2290c0da5_2_690x364.png" alt="86" data-base62-sha1="yJy30xoEUIgAp0MDO5aLhbcitQ9" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37007af4e60914a7aae69cd109dc5c2290c0da5_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37007af4e60914a7aae69cd109dc5c2290c0da5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37007af4e60914a7aae69cd109dc5c2290c0da5.png 2x" data-dominant-color="575A55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">86</span><span class="informations">882×466 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2024-06-06 11:39 UTC)

<p><a class="mention" href="/u/evaherbst">@evaherbst</a> made a code change to support running without this pop-up. Make sure to use latest Slicer stable (5.6.2) or Preview and have the latest version of the Slicer TotalSegmentator extension installed. This code change was made on April 24th.</p>
<aside class="quote" data-post="17" data-topic="35461">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/running-totalsegmentator-from-python-console/35461/17">Running TotalSegmentator from Python Console</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi <a class="mention" href="/u/lassoan">@lassoan</a> , 
Thank you for the suggestion. 
I implemented it and it works for me (tested with GUI which gave popup warning, and via command line which did not give popup warning). 
If you could also confirm it works for you that would be great. 
I also adjusted the time estimate in the pop up warning about slow mode. 
Thank you, 
Eva
  </blockquote>
</aside>

<aside class="onebox githubcommit" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/commit/0550cca77854cd4cdc83a6f35d5c2ec0dae7c6ea">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0550cca77854cd4cdc83a6f35d5c2ec0dae7c6ea" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0550cca77854cd4cdc83a6f35d5c2ec0dae7c6ea" target="_blank" rel="noopener nofollow ugc">added interactive argument to process mode</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-04-25" data-time="03:16:04" data-timezone="UTC">03:16AM - 25 Apr 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/evaherbst" target="_blank" rel="noopener nofollow ugc">
          <img alt="evaherbst" src="https://avatars.githubusercontent.com/u/31034865?v=4" class="onebox-avatar-inline" width="20" height="20">
          evaherbst
        </a>
      </div>

      <div class="lines" title="changed 1 files with 6 additions and 6 deletions">
        <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0550cca77854cd4cdc83a6f35d5c2ec0dae7c6ea" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+6</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">interactive argument = false by default to enable running from command line with<span class="show-more-container"><a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/0550cca77854cd4cdc83a6f35d5c2ec0dae7c6ea" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">out warning popups about slow mode. interactive = true when running via GUI, retaining previous warning popups about slow mode. Also adjusted warning text time estimate</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
