# can't rename markup line

**Topic ID**: 14656
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/cant-rename-markup-line/14656

---

## Post #1 by @chendong9416 (2020-11-17 05:23 UTC)

<p>Hi, i want to chang the markupsline/markupsline_1 to other name, but after i did this, nothing changed in the image of cross-section analysis, how can I do it ?</p>

---

## Post #2 by @lassoan (2020-11-17 05:35 UTC)

<p>Where and how did you attempt to change the node name? Where did you expect to see a name change? Attach a few screenshots. Try with latest Slicer Stable and Preview releases, too.</p>

---

## Post #3 by @chendong9416 (2020-11-17 06:05 UTC)

<p>i’m with the latest slicer stable now, i expect to see a name change in the image for screenshots, and i change the node name in markup, it doesn’t influence the name in image.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b401fdf24f62eac37a6b8e017d0c25a268beed4.png" data-download-href="/uploads/short-url/aJHcaURFMoVx4tZI9OfVXRTij8o.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b401fdf24f62eac37a6b8e017d0c25a268beed4_2_690x111.png" alt="捕获" data-base62-sha1="aJHcaURFMoVx4tZI9OfVXRTij8o" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b401fdf24f62eac37a6b8e017d0c25a268beed4_2_690x111.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b401fdf24f62eac37a6b8e017d0c25a268beed4_2_1035x166.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b401fdf24f62eac37a6b8e017d0c25a268beed4.png 2x" data-dominant-color="9EA3A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1313×212 42.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-11-17 06:16 UTC)

<p>Thank you, I was able to reproduce the issue. I’ve filed a bug report:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5302" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5302" target="_blank" rel="noopener">Line label is not updated until measurements are updated</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-11-17" data-time="06:15:37" data-timezone="UTC">06:15AM - 17 Nov 20 UTC</span>
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
  <p class="github-content">Line label in slice views (L: 13.5mm) is not updated when the node is renamed, only when points are moved.
Steps to...</p>
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

## Post #5 by @chendong9416 (2020-11-17 06:30 UTC)

<p>thank you for solving my problem!</p>

---
