---
topic_id: 40416
title: "Segment Color Bug"
date: 2024-11-28
url: https://discourse.slicer.org/t/40416
---

# Segment color bug

**Topic ID**: 40416
**Date**: 2024-11-28
**URL**: https://discourse.slicer.org/t/segment-color-bug/40416

---

## Post #1 by @muratmaga (2024-11-28 00:00 UTC)

<p>Looks like there is a bug with segment color display in the last preview. I opened an issue:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8069">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8069" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8069" target="_blank" rel="noopener nofollow ugc">segmentation colors look incorrect, when chosen from terminology </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-27" data-time="23:54:44" data-timezone="UTC">11:54PM - 27 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is with today's preview build.

1. Load MRHead and start segmenting.
2. <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Use threshold to create a segment, and double click to change it is name to Skin from terminology selector
3. Note that there are now two colors. Original segment color (green), and then another color box that shows the color specified in terminology (brown).
4. Create another segment, and choose another term to see that it contiuues to do the same thing. 

The actual displayed segment color is the color on the left (original segment color, not the terminology one)

![image](https://github.com/user-attachments/assets/23131083-3e39-47c5-8e9c-22a7ee594b8d)

@jcfr  @cpinter @lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad426deccea8314122a6ff0c58681e9e36f90d69.png" data-download-href="/uploads/short-url/oIIVsgMc3Lg99QCKqNEBZaSzmpX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad426deccea8314122a6ff0c58681e9e36f90d69_2_690x307.png" alt="image" data-base62-sha1="oIIVsgMc3Lg99QCKqNEBZaSzmpX" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad426deccea8314122a6ff0c58681e9e36f90d69_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad426deccea8314122a6ff0c58681e9e36f90d69.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad426deccea8314122a6ff0c58681e9e36f90d69.png 2x" data-dominant-color="DFE5E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×319 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
