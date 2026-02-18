# Cant get rid of red window frame

**Topic ID**: 44606
**Date**: 2025-09-27
**URL**: https://discourse.slicer.org/t/cant-get-rid-of-red-window-frame/44606

---

## Post #1 by @Hannnonk (2025-09-27 12:48 UTC)

<p>Even though it is turned off, I cant get rid of the red frame. Other windows are behaving normally. I have closed and reopened the program with no effect.</p>
<p>thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35187112e29732a7549f7a2eab4759c1fe6e8e59.jpeg" data-download-href="/uploads/short-url/7zHFFfNk9tXBOjbYYADTpvrsRfP.jpeg?dl=1" title="2025-09-27_8-43-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35187112e29732a7549f7a2eab4759c1fe6e8e59_2_690x386.jpeg" alt="2025-09-27_8-43-58" data-base62-sha1="7zHFFfNk9tXBOjbYYADTpvrsRfP" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35187112e29732a7549f7a2eab4759c1fe6e8e59_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35187112e29732a7549f7a2eab4759c1fe6e8e59_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35187112e29732a7549f7a2eab4759c1fe6e8e59_2_1380x772.jpeg 2x" data-dominant-color="8C8C9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-09-27_8-43-58</span><span class="informations">1886×1056 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2025-09-27 13:01 UTC)

<p>I believe this has been fixed in a recent Slicer Preview release as of:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8684">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener nofollow ugc">BUG: Fixed hidden slice edges kept appearing in 3D views</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-slice-edge-cannot-be-hidden</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-29" data-time="17:03:43" data-timezone="UTC">05:03PM - 29 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 2 files with 2 additions and 4 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8684/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-4</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When loading certain scenes (e.g., created by Slicer-5.6) slice edge frames coul<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">d not be hidden in 3D views.
This was cause by multiple slice edge representations were added to the renderer due to a logic error in vtkMRMLThreeDSliceEdgeDisplayableManager.

Fixes issues reported here:
https://discourse.slicer.org/t/hide-slice-rectangles-in-3d-view/42912
https://discourse.slicer.org/t/annoying-frame-after-slice-view-on-3d/44247

Also added a minor fix of the vtkMRMLViewNode API that I discovered while investigating this issue. It is not directly related to the fix, just included in this pull request because it is so small change that I did not want to add another pull request for it.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Download the latest Slicer preview and let us know how it goes.</p>

---

## Post #3 by @Hannnonk (2025-09-27 15:21 UTC)

<p>Download of 5.9.0-2025-09-26 r33973 / 95d5844 corrected the issue</p>
<p>thx</p>

---
