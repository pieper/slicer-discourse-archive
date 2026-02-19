---
topic_id: 45645
title: "Downloading Older Releases Is Problematic"
date: 2025-12-30
url: https://discourse.slicer.org/t/45645
---

# Downloading older releases is problematic

**Topic ID**: 45645
**Date**: 2025-12-30
**URL**: https://discourse.slicer.org/t/downloading-older-releases-is-problematic/45645

---

## Post #1 by @dzenanz (2025-12-30 17:47 UTC)

<p>Accessing older releases does not offer download of previous stable releases. I had to take a good look at <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F" rel="noopener nofollow ugc">access older releases</a> page to come up with this link to what I wanted: <a href="https://download.slicer.org/download?os=windows&amp;stability=release&amp;version=5.8.1" rel="noopener nofollow ugc">https://download.slicer.org/download?os=windows&amp;stability=release&amp;version=5.8.1</a></p>
<p>The first link there (<a href="https://download.slicer.org/?offset=-50" rel="noopener nofollow ugc">with offset</a>) provides a surprising result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e4b9ad3b6a6e557855fc17cf396cd3e862e15c7.png" data-download-href="/uploads/short-url/22sFmmz8EyYSG6raScOGGT9qGQD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4b9ad3b6a6e557855fc17cf396cd3e862e15c7_2_604x500.png" alt="image" data-base62-sha1="22sFmmz8EyYSG6raScOGGT9qGQD" width="604" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4b9ad3b6a6e557855fc17cf396cd3e862e15c7_2_604x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4b9ad3b6a6e557855fc17cf396cd3e862e15c7_2_906x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4b9ad3b6a6e557855fc17cf396cd3e862e15c7_2_1208x1000.png 2x" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1869×1545 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Namely, 5.9.0 is offered as both stable and preview version. With <code>offset=-250</code> version 5.7.0 is offered twice.</p>

---

## Post #2 by @lassoan (2025-12-30 20:30 UTC)

<p>Thanks for the feedback. I’ve submitted a pull request that should make the documentation more clear:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/slicer.org/pull/362">
  <header class="source">

      <a href="https://github.com/Slicer/slicer.org/pull/362" target="_blank" rel="noopener">github.com/Slicer/slicer.org</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/slicer.org/pull/362" target="_blank" rel="noopener">Update download.markdown with older releases info</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>update-access-older-releases</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-12-30" data-time="19:50:10" data-timezone="UTC">07:50PM - 30 Dec 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 36 additions and 1 deletions">
          <a href="https://github.com/Slicer/slicer.org/pull/362/files" target="_blank" rel="noopener">
            <span class="added">+36</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Moved instructions for accessing older Slicer releases and extensions from the o<span class="show-more-container"><a href="https://github.com/Slicer/slicer.org/pull/362" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ld wiki to this site.

To reduce usage of the old wiki and address difficulties @dzenanz reported at https://discourse.slicer.org/t/downloading-older-releases-is-problematic/45645</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
