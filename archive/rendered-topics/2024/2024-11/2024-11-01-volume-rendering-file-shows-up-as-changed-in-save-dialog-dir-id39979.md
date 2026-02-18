# Volume rendering file shows up as changed in Save dialog directly after opening an mrml scene

**Topic ID**: 39979
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/volume-rendering-file-shows-up-as-changed-in-save-dialog-directly-after-opening-an-mrml-scene/39979

---

## Post #1 by @MMMPPPMMM (2024-11-01 11:08 UTC)

<p>Hello</p>
<p>It seems to me like a bug that the *.vp volume rendering file shows up as changed in Save dialog directly after opening an MRML scene?</p>
<p>Find an example here: <a href="https://easyupload.io/9mbf6h" class="inline-onebox" rel="noopener nofollow ugc">Upload Files | Free File Upload and Transfer Up To 10 GB</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbf736ffb6e2cdca65731761a81d4db942aece43.jpeg" data-download-href="/uploads/short-url/t6mA4DzRnIpMoSP6DAJnZ5NVtXt.jpeg?dl=1" title="Test_VR_Status" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbf736ffb6e2cdca65731761a81d4db942aece43_2_639x500.jpeg" alt="Test_VR_Status" data-base62-sha1="t6mA4DzRnIpMoSP6DAJnZ5NVtXt" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbf736ffb6e2cdca65731761a81d4db942aece43_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbf736ffb6e2cdca65731761a81d4db942aece43_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbf736ffb6e2cdca65731761a81d4db942aece43.jpeg 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Test_VR_Status</span><span class="informations">1222×955 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Tested with Slicer 5.6.2 r32448 / f10cd8c</p>
<p>Kind regards</p>

---

## Post #2 by @pieper (2024-11-01 19:35 UTC)

<p>Yes, that’s probably a bug in the code that manages the <code>ModifiedSinceRead</code> property of the node.  It would be great if someone has time to dig in and fix this.  To start it would be good if you could file an issue to track it.</p>

---

## Post #3 by @MMMPPPMMM (2024-11-04 20:52 UTC)

<p>Done</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8030">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8030" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8030" target="_blank" rel="noopener nofollow ugc">Volume rendering file shows up as changed in Save dialog directly after opening an mrml scene</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-04" data-time="20:52:01" data-timezone="UTC">08:52PM - 04 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/oqilipo" target="_blank" rel="noopener nofollow ugc">
          <img alt="oqilipo" src="https://avatars.githubusercontent.com/u/15254908?v=4" class="onebox-avatar-inline" width="20" height="20">
          oqilipo
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
The *.vp volume rendering file shows up as changed in Save dialog di<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rectly after opening an MRML scene.
Probably a bug in the code that manages the ModifiedSinceRead property of the node.

![cbf736ffb6e2cdca65731761a81d4db942aece43](https://github.com/user-attachments/assets/ffc63ecf-e01c-4d93-a611-cb9076679aab)

## Steps to reproduce

Download the example scene: [Upload Files | Free File Upload and Transfer Up To 10 GB](https://easyupload.io/9mbf6h)

1. Open the scene
2. Open the Save Dialog

## Environment
- Slicer version: Slicer 5.6.2 r32448 / f10cd8c
- Operating system: Windows 11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @jamesobutler (2024-11-04 22:49 UTC)

<p>For reference it appears <a class="mention" href="/u/lassoan">@lassoan</a> has included a bug fix for this in:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8029">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8029" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8029" target="_blank" rel="noopener nofollow ugc">Fix unnecessary node saves</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-unnecessary-node-saves</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-04" data-time="18:16:04" data-timezone="UTC">06:16PM - 04 Nov 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="7 commits changed 13 files with 178 additions and 80 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8029/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+178</span>
            <span class="removed">-80</span>
          </a>
        </div>
      </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
