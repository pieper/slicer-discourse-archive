---
topic_id: 46834
title: "Volume Property json file is incorrectly saved"
date: 2026-04-25
url: https://discourse.slicer.org/t/46834
last_bumped: 2026-04-27T22:07:15.446Z
---

# Volume Property json file is incorrectly saved

**Topic ID**: 46834
**Date**: 2026-04-25
**URL**: https://discourse.slicer.org/t/volume-property-json-file-is-incorrectly-saved/46834

---

## Post #1 by @muratmaga (2026-04-25 18:51 UTC)

<p>I Load a 16bit unsigned dataset, set up its volume rendering properties such as</p>
<ol>
<li>Use shift slider</li>
<li>Change the material preset to a non-default one (the second brightest)</li>
<li>Remove some points from the scalar mapping and shift the colors aroun</li>
</ol>
<p>At this stage I have perfectly fine rendering. if I save this file to disk and reload and assign this new volume property, the rendering dissappears as the scalar opacity flat lines (all points are 0.0). Reproduces on today preview build on mac.</p>
<p>I asked copilot what is different between the unmodified VP and the one saved and it said:</p>
<p><code>Works.vp.json effectiveRange: [0, 65535] (full 16-bit range). doesntwork.json effectiveRange: [3800, 69335]. 69335 &gt; 65535 — outside the actual data range. The min 3800 also chopped off the (0, …) and (2.22e-308, …) baseline points, which probably explains why the start of the tent is gone in the broken file. If effectiveRange was edited in the UI (or auto-recomputed from “current threshold” rather than data range), the saver may have culled all control points outside that range — including the peak’s left base — leaving just a flat-zero function.</code></p>
<p>Not entirely sure what that means, I hope it is helpful. But there is clear bug in saving.</p>
<p>If you want the original volume I used, it is here: <a href="https://github.com/muratmaga/Bumblebee_Stained/releases/download/v1/Bumblebee.nrrd" rel="noopener nofollow ugc">https://github.com/muratmaga/Bumblebee_Stained/releases/download/v1/Bumblebee.nrrd</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d21e2a584ca76700b6ab99a83d194427ad907ed.png" data-download-href="/uploads/short-url/fzqDSLSIMWTcvuQ357qdcdMreMd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d21e2a584ca76700b6ab99a83d194427ad907ed_2_232x500.png" alt="image" data-base62-sha1="fzqDSLSIMWTcvuQ357qdcdMreMd" width="232" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d21e2a584ca76700b6ab99a83d194427ad907ed_2_232x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d21e2a584ca76700b6ab99a83d194427ad907ed_2_348x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d21e2a584ca76700b6ab99a83d194427ad907ed_2_464x1000.png 2x" data-dominant-color="ECEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">503×1081 67.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b649c8eda21ae3bead1085ee0f2030b162649cd9.png" data-download-href="/uploads/short-url/q0AYWBULikwU2nYT9vqkMTVEOQ9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b649c8eda21ae3bead1085ee0f2030b162649cd9.png" alt="image" data-base62-sha1="q0AYWBULikwU2nYT9vqkMTVEOQ9" width="526" height="243"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">526×243 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-04-27 22:07 UTC)

<p>A bug report was submitted, let’s continue the discussion there:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9129">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9129" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9129" target="_blank" rel="noopener">Volume Property json file is incorrectly saved</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-04-27" data-time="21:41:56" data-timezone="UTC">09:41PM - 27 Apr 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As reported in the forum: https://discourse.slicer.org/t/volume-property-json-fi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">le-is-incorrectly-saved/46834

I load a 16bit unsigned dataset, set up its volume rendering properties such as

1. Use shift slider
2. Change the material preset to a non-default one (the second brightest)
3. Remove some points from the scalar mapping and shift the colors aroun

At this stage I have perfectly fine rendering. if I save this file to disk and reload and assign this new volume property, the rendering dissappears as the scalar opacity flat lines (all points are 0.0). Reproduces on today preview build on mac.

I asked copilot what is different between the unmodified VP and the one saved and it said:

`Works.vp.json effectiveRange: [0, 65535] (full 16-bit range). doesntwork.json effectiveRange: [3800, 69335]. 69335 &gt; 65535 — outside the actual data range. The min 3800 also chopped off the (0, …) and (2.22e-308, …) baseline points, which probably explains why the start of the tent is gone in the broken file. If effectiveRange was edited in the UI (or auto-recomputed from “current threshold” rather than data range), the saver may have culled all control points outside that range — including the peak’s left base — leaving just a flat-zero function.
`
Not entirely sure what that means, I hope it is helpful. But there is clear bug in saving.

If you want the original volume I used, it is here: https://github.com/muratmaga/Bumblebee_Stained/releases/download/v1/Bumblebee.nrrd</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
