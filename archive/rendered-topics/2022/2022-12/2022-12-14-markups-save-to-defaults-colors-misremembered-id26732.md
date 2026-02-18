# Markups "save to defaults" colors misremembered

**Topic ID**: 26732
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/markups-save-to-defaults-colors-misremembered/26732

---

## Post #1 by @muratmaga (2022-12-14 17:46 UTC)

<p>In stable 5.2.1 in Linux,  I change the colors of markups states and hit save to defaults.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e666c84b6c633eb2c687c8a49bb665e241b15f9.jpeg" data-download-href="/uploads/short-url/6Ctpa1IqY7j1WKxJaJOKFbnxwhj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e666c84b6c633eb2c687c8a49bb665e241b15f9_2_690x342.jpeg" alt="image" data-base62-sha1="6Ctpa1IqY7j1WKxJaJOKFbnxwhj" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e666c84b6c633eb2c687c8a49bb665e241b15f9_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e666c84b6c633eb2c687c8a49bb665e241b15f9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e666c84b6c633eb2c687c8a49bb665e241b15f9.jpeg 2x" data-dominant-color="E6E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×408 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After slicer restart, this is what it comes back as:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc014a080b54635b6ce0b3bb4f11fec3af791c49.png" data-download-href="/uploads/short-url/t6Iaifz4B60EFtHzgfbiwa8QX33.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc014a080b54635b6ce0b3bb4f11fec3af791c49_2_690x279.png" alt="image" data-base62-sha1="t6Iaifz4B60EFtHzgfbiwa8QX33" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc014a080b54635b6ce0b3bb4f11fec3af791c49_2_690x279.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc014a080b54635b6ce0b3bb4f11fec3af791c49.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc014a080b54635b6ce0b3bb4f11fec3af791c49.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">830×336 56.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Same on windows. saved to defaults<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fc13807f5944bacfde4e8084c0142c3c61d5413.png" alt="image" data-base62-sha1="2fn89N6vzW3H9GJaQRxEV849Hd9" width="69" height="203"></p>
<p>after restart<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78efa2f014b373a89d1324e056c89dca1bb7a699.png" alt="image" data-base62-sha1="hfQIlmEl6Do2Wqttn0hILDskulb" width="66" height="195"></p>
<p>Looks like active color is written to the field of unselected, and then get’s back reset to the default green.</p>

---

## Post #2 by @lassoan (2022-12-14 20:02 UTC)

<p>Thanks for reporting. Please test if this change fixes it:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6736/files">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6736/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6736/files" target="_blank" rel="noopener">BUG: Fix reading of default markup active color</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Slicer:lassoan-fix-markup-active-color</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-14" data-time="20:01:51" data-timezone="UTC">08:01PM - 14 Dec 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6736/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes issue reported at https://discourse.slicer.org/t/markups-save-to-defaults-<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6736" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">colors-misremembered/26732</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2022-12-15 17:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Was this merged too late for todays preview?<br>
For me it is still the same issue with today’s preview (windows).</p>
<p>(looks like it wasn’t merged. I will see if we can get a local build to test it).</p>

---

## Post #4 by @lassoan (2022-12-17 14:26 UTC)

<p>Let me know if it fixes the problem and then i neve it. Thank you!</p>

---

## Post #5 by @muratmaga (2022-12-23 22:50 UTC)

<p>This seems to fix the issue on our test build (linux).</p>

---
