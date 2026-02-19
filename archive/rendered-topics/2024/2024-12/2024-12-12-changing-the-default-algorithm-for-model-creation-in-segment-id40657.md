---
topic_id: 40657
title: "Changing The Default Algorithm For Model Creation In Segment"
date: 2024-12-12
url: https://discourse.slicer.org/t/40657
---

# Changing the default algorithm for model creation in segment editor

**Topic ID**: 40657
**Date**: 2024-12-12
**URL**: https://discourse.slicer.org/t/changing-the-default-algorithm-for-model-creation-in-segment-editor/40657

---

## Post #1 by @muratmaga (2024-12-12 17:14 UTC)

<p>Is the new model extraction option (flying edges?) going to be made default in the upcoming stable?</p>
<p>In the previews, one still needs to manually switch to it.</p>

---

## Post #2 by @lassoan (2024-12-13 05:30 UTC)

<p>Still flying edges is used in the Slicer Preview Release. Surface nets is the new, faster option. We agree that we should use that by default (<a href="https://discourse.slicer.org/t/bad-performance-when-segmenting-11gb-micro-ct/38362/8" class="inline-onebox">Bad performance when segmenting 11GB micro-CT - #8 by pieper</a>). We haven’t decided if we should do it in Slicer 5.8 or later, but I think it is better to do it now. I’ve added an issue to track this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8093">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8093" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8093" target="_blank" rel="noopener">Make surface nets the default closed surface generation algorithm</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-12-13" data-time="05:29:36" data-timezone="UTC">05:29AM - 13 Dec 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As discussed, we should use surface nets to generate closed surface representati<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">on from binary labelmap represenation in segmentations. See the discussion at https://discourse.slicer.org/t/bad-performance-when-segmenting-11gb-micro-ct/38362/8?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
