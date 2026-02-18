# Problem with TotalSegmentator - my computer freezes

**Topic ID**: 46068
**Date**: 2026-02-05
**URL**: https://discourse.slicer.org/t/problem-with-totalsegmentator-my-computer-freezes/46068

---

## Post #1 by @jimenagonzalezsal (2026-02-05 22:14 UTC)

<p>Hello! I need help. I’m trying to segment lumbar spine DICOMs, but whenever I click <strong>Apply</strong>, my computer freezes and the segmentation never finishes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a2b75953eab0f80041856b6721f6a29f3a7a46d.jpeg" data-download-href="/uploads/short-url/3JvwzwzAWp98N1WU3Zb0JGy1DIh.jpeg?dl=1" title="Screenshot 2026-02-04 at 12.33.56 p.m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2b75953eab0f80041856b6721f6a29f3a7a46d_2_690x382.jpeg" alt="Screenshot 2026-02-04 at 12.33.56 p.m." data-base62-sha1="3JvwzwzAWp98N1WU3Zb0JGy1DIh" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2b75953eab0f80041856b6721f6a29f3a7a46d_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2b75953eab0f80041856b6721f6a29f3a7a46d_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a2b75953eab0f80041856b6721f6a29f3a7a46d_2_1380x764.jpeg 2x" data-dominant-color="A6A3A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-02-04 at 12.33.56 p.m.</span><span class="informations">1920×1065 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-02-05 22:17 UTC)

<p>It seems that you have run into the same issue that was reported here:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/issues/79">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/79" target="_blank" rel="noopener">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/79" target="_blank" rel="noopener">When running this plugin on a Macbook Pro with an M3Max chip, it gets stuck at "saved in 2.62s" after the partitioning is complete.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-12-04" data-time="06:14:53" data-timezone="UTC">06:14AM - 04 Dec 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/QianMuXiao" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/40720829?v=4" class="onebox-avatar-inline" width="20" height="20">
          QianMuXiao
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When running the segmentation plugin, the 3D slicer becomes unresponsive and can<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">not be operated.

![Image](https://github.com/user-attachments/assets/242a9619-f0ae-4316-86ac-d0e46647975d)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Unless someone else have time to investigate this earlier, I’ll try to have a look at this next week.</p>

---

## Post #3 by @kazim (2026-02-15 14:08 UTC)

<p>I am having the exact same issue, MacBook Pro with M4 Pro chip</p>

---
