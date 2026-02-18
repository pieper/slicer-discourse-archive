# Folder visibility confusing

**Topic ID**: 23753
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/folder-visibility-confusing/23753

---

## Post #1 by @fbordignon (2022-06-07 12:36 UTC)

<p>The eye icon is both loved and hated by our users, but I believe there is a confusing behavior for the folder eye icon. When I close the folder’s eye and have both 2D and 3D renderings, only the 3D hides:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9476b52f52e1fc783edf8de6c4fdbf9ef93fc87.jpeg" data-download-href="/uploads/short-url/qr3lw0KkqCNblk5wKtyRaHkeK1x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9476b52f52e1fc783edf8de6c4fdbf9ef93fc87_2_690x453.jpeg" alt="image" data-base62-sha1="qr3lw0KkqCNblk5wKtyRaHkeK1x" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9476b52f52e1fc783edf8de6c4fdbf9ef93fc87_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9476b52f52e1fc783edf8de6c4fdbf9ef93fc87_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9476b52f52e1fc783edf8de6c4fdbf9ef93fc87.jpeg 2x" data-dominant-color="A6A7AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1043×685 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c58b905ae67d0427b99d4e329279db5660b38d93.jpeg" data-download-href="/uploads/short-url/sbz4HRCxP8xPy0TqiRgRYsyee2L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c58b905ae67d0427b99d4e329279db5660b38d93_2_690x453.jpeg" alt="image" data-base62-sha1="sbz4HRCxP8xPy0TqiRgRYsyee2L" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c58b905ae67d0427b99d4e329279db5660b38d93_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c58b905ae67d0427b99d4e329279db5660b38d93_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c58b905ae67d0427b99d4e329279db5660b38d93.jpeg 2x" data-dominant-color="A9AAAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1043×685 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To confuse even more the users, the 2D slice is kept on the 3D view. I’ve personally spent 10 minutes fiddling with the volume rendering sliders only to discover that the folder eye was closed. I was seeing the 2D slice at the 3D view and at the slicewidgets but the 3D rendering was not showing, so I thought the visibility was fine.</p>

---

## Post #2 by @mau_igna_06 (2022-06-07 12:50 UTC)

<p>Plesse report it as a bug</p>

---

## Post #3 by @fbordignon (2022-06-07 12:55 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6413">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6413" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6413" target="_blank" rel="noopener nofollow ugc">Folder visibility affects 3D rendering but not 2D</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-07" data-time="12:55:42" data-timezone="UTC">12:55PM - 07 Jun 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fbordignon" target="_blank" rel="noopener nofollow ugc">
          <img alt="fbordignon" src="https://avatars.githubusercontent.com/u/4790289?v=4" class="onebox-avatar-inline" width="20" height="20">
          fbordignon
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As reported on https://discourse.slicer.org/t/folder-visibility-confusing/23753
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">

The eye icon is both loved and hated by our users, but I believe there is a confusing behavior for the folder eye icon. When I close the folder’s eye and have both 2D and 3D renderings, only the 3D hides:

![image](https://user-images.githubusercontent.com/4790289/172384582-08113351-73e5-48a4-9e64-a5b77eabbc80.png)

![image](https://user-images.githubusercontent.com/4790289/172384604-57108b69-ab8d-4f87-af99-69d81c7be87b.png)


To confuse even more the users, the 2D slice is kept on the 3D view. I’ve personally spent 10 minutes fiddling with the volume rendering sliders only to discover that the folder eye was closed. I was seeing the 2D slice at the 3D view and at the slicewidgets but the 3D rendering was not showing, so I thought the visibility was fine.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @cpinter (2022-06-07 13:13 UTC)

<p>This is not a bug. It is the Nth iteration of a super hard problem. We can discuss it in the ticket.</p>

---
