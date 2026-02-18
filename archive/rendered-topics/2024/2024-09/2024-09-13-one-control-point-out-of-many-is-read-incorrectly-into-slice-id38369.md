# One control point out of many is read incorrectly into Slicer

**Topic ID**: 38369
**Date**: 2024-09-13
**URL**: https://discourse.slicer.org/t/one-control-point-out-of-many-is-read-incorrectly-into-slicer/38369

---

## Post #1 by @muratmaga (2024-09-13 18:07 UTC)

<p>I have <a href="https://app.box.com/s/a3nbgdr9q86asf5qrdeaxn5jqesku80m" rel="noopener nofollow ugc">this mrk.json file</a> that generated from our SlicerMorphR package. When this file is loaded into the scene, control point 121 (alignedPoints-121) points gets undefined (see the screenshot below).</p>
<p>But it is defined in the file.</p>
<pre><code class="lang-auto">          "id": 120,
          "label": "alignedPoints-120",
          "position": [4.9336, 11.6169, 0.0273],
          "orientation": "[-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0]",
          "selected": true,
          "locked": false,
          "visibility": true,
          "positionStatus": "defined"
        },
        {
          "id": 121,
          "label": "alignedPoints-121",
          "position": [5.6459, 11.6355, 0],
          "orientation": "[-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0]",
          "selected": true,
          "locked": false,
          "visibility": true,
          "positionStatus": "defined"
        },
        {
          "id": 122,
          "label": "alignedPoints-122",
          "position": [4.7923, 11.4034, -0.0187],
          "orientation": "[-1.0, -0.0, -0.0, -0.0, -1.0, -0.0, 0.0, 0.0, 1.0]",
          "selected": true,
          "locked": false,
          "visibility": true,
          "positionStatus": "defined"
        },
</code></pre>
<p>I am not sure what’s going on or how to debug this. This is with the latest stable. Any pointer is much appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6db8c9578fab5353082ccf330ad049af813d61.png" data-download-href="/uploads/short-url/ya5bZgsmZ3lwaiN6Fq5VCnnh0qd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef6db8c9578fab5353082ccf330ad049af813d61_2_690x125.png" alt="image" data-base62-sha1="ya5bZgsmZ3lwaiN6Fq5VCnnh0qd" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef6db8c9578fab5353082ccf330ad049af813d61_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef6db8c9578fab5353082ccf330ad049af813d61_2_1035x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef6db8c9578fab5353082ccf330ad049af813d61_2_1380x250.png 2x" data-dominant-color="BACFE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1434×260 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-09-13 18:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="38369">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>"position": [5.6459, 11.6355, 0],</code></p>
</blockquote>
</aside>
<p>By setting the Z position value to 0.0, the error message does not appear in the python console. The reader seems to strictly interpret integers and doubles.</p>

---

## Post #3 by @lassoan (2024-09-13 19:03 UTC)

<p>Good catch, I’ve submitted a pull request with the fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7928">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7928" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7928" target="_blank" rel="noopener">BUG: Fix reading of markup point position from integer value</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-markup-position-reading</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-09-13" data-time="19:08:15" data-timezone="UTC">07:08PM - 13 Sep 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 6 additions and 6 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7928/files" target="_blank" rel="noopener">
            <span class="added">+6</span>
            <span class="removed">-6</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When markup point position was defined as an integer (0) instead of float (0.0) <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7928" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">the markup reader rejected the position value. The problem was that the code only accepted double type. Fixed by accepting any numeric type.

Fixes issue reported at https://discourse.slicer.org/t/one-control-point-out-of-many-is-read-incorrectly-into-slicer/38369</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
