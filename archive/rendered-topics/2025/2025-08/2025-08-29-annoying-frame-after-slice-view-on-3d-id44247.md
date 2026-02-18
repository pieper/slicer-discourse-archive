# Annoying frame after slice view on 3d

**Topic ID**: 44247
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/annoying-frame-after-slice-view-on-3d/44247

---

## Post #1 by @mohammed_alshakhas (2025-08-29 13:29 UTC)

<p>often  i get this frame not going away after slice view on 3d . no matter what i do i cant get rid of . i have to start all over again</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e4e028b7fcf16f87d64ac67bde67d3367d9ab19.png" data-download-href="/uploads/short-url/i1lioUPFVKB5ueyF4n6v7xRR9BT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e4e028b7fcf16f87d64ac67bde67d3367d9ab19_2_690x331.png" alt="image" data-base62-sha1="i1lioUPFVKB5ueyF4n6v7xRR9BT" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e4e028b7fcf16f87d64ac67bde67d3367d9ab19_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e4e028b7fcf16f87d64ac67bde67d3367d9ab19_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e4e028b7fcf16f87d64ac67bde67d3367d9ab19.png 2x" data-dominant-color="F6F6F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1165×559 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-08-29 13:37 UTC)

<p>Yes, that’s annoying.  You can try the workaround here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="43285">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/red-boundary-border-around-frame-in-version-5-8-1/43285/2">Red Boundary/Border Around Frame in Version 5.8.1</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    I had this problem a few weeks ago for the first time, when making figures for publication. 
Can’t remember how I solved it, but try clicking off show slicer edges. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad407d3ae83daae5826b9ff91ea4fe1787239990.png" data-download-href="/uploads/short-url/oIELJbnKGKfnlNOWznBG48HVdio.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="42912">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/spichardo/48/15092_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/hide-slice-rectangles-in-3d-view/42912">Hide slice rectangles in 3D view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Operating system: macOS 15.4.1 
Slicer version: 5.8.1 
Expected behavior: Old versions of 3DSlicer didn’t show these rectangles, they are in the way for illustration purposes 
Actual behavior: The “new” rectangles are shown all the time, I can’t find what option to select to hide them. I tried to click every option but I can’t find which is the one controlling its visibility. I know it has to be somewhere. Thanks for any tip. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820.jpeg" data-download-href="/uploads/short-url/8wx7FQlUCMxzldwQVxJs57xYldm.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> <a class="mention" href="/u/lassoan">@lassoan</a> is there an issue filed already about this?  I think there’s a logic issue from this:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8008">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener">ENH: Add option to display slice edges in 3D view</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>Punzo:slices3Dedge</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-25" data-time="09:30:38" data-timezone="UTC">09:30AM - 25 Oct 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Punzo" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
            Punzo
          </a>
        </div>

        <div class="lines" title="1 commits changed 25 files with 1298 additions and 294 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8008/files" target="_blank" rel="noopener">
            <span class="added">+1298</span>
            <span class="removed">-294</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- Implemented functionality to show slice edges in the 3D view.
- Added user in<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">terface controls to control the visibility of slice edges.
- Implemented linking controls to synchronize the visibility of slice edges across different views.

![image](https://github.com/user-attachments/assets/eb4afd25-4697-4b62-9028-b935dcac43d2)

Reference: https://discourse.slicer.org/t/show-slice-edges-in-3d-view/11381</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2025-08-29 14:33 UTC)

<p>Slice frames allow users to identify in 3D views which slice view an image corresponds to. In the future, the frame will be interactive, so that you will be able to click and drag it to translate or rotate the slice. It is a feature, not a bug, because it can be turned off, as described <a href="https://discourse.slicer.org/t/hide-slice-rectangles-in-3d-view/42912/3">here</a>.</p>
<p>If you cannot hide a slice frame then please provide detailed list of steps to reproduce it and we’ll investigate.</p>

---

## Post #4 by @pieper (2025-08-29 15:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I haven’t really investigated much but I recall also seeing these frames hang around, at various times, typically after closing a scene in some unusual situation.</p>
<p>Here for example with today’s preview build I got this after dowloading MRHead, linking the slice views, making them visible, switching to dual-3d, linking the 3d views, and closing the scene.  There may be simpler ways to reproduce but this is an example of what I’ve seen before.  If we don’t already have one we should file an issue for this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab8fb0eb115de55df845ee5044b9a09cd381207.jpeg" data-download-href="/uploads/short-url/vcUphPzEQyEUbTynVhrt0J4Bj7h.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab8fb0eb115de55df845ee5044b9a09cd381207_2_690x243.jpeg" alt="image" data-base62-sha1="vcUphPzEQyEUbTynVhrt0J4Bj7h" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab8fb0eb115de55df845ee5044b9a09cd381207_2_690x243.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab8fb0eb115de55df845ee5044b9a09cd381207_2_1035x364.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab8fb0eb115de55df845ee5044b9a09cd381207_2_1380x486.jpeg 2x" data-dominant-color="AEAFD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×672 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @chir.set (2025-08-29 15:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="44247">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If we don’t already have one we should file an issue for this.</p>
</blockquote>
</aside>
<p>Would this <a href="https://github.com/Slicer/Slicer/issues/8086#issue-2729737631" rel="noopener nofollow ugc">issue</a> be of similar kind?</p>

---

## Post #6 by @lassoan (2025-08-29 15:43 UTC)

<p>I was able to reproduce the issue using <a class="mention" href="/u/mikebind">@mikebind</a> instructions <a href="https://discourse.slicer.org/t/hide-slice-rectangles-in-3d-view/42912/6">here</a>. I’ll push a fix later today.</p>

---

## Post #7 by @lassoan (2025-08-29 17:04 UTC)

<p>The fix is here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8684">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener">Fix slice edge cannot be hidden</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-slice-edge-cannot-be-hidden</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-29" data-time="17:03:43" data-timezone="UTC">05:03PM - 29 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 2 files with 2 additions and 4 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8684/files" target="_blank" rel="noopener">
            <span class="added">+2</span>
            <span class="removed">-4</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When loading certain scenes (e.g., created by Slicer-5.6) slice edge frames coul<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8684" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d not be hidden in 3D views.
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


---

## Post #8 by @lassoan (2025-08-29 17:39 UTC)

<p>A post was split to a new topic: <a href="/t/make-clipping-to-be-separate-module/44266">Make clipping to be separate module</a></p>

---

## Post #9 by @lassoan (2025-08-29 18:50 UTC)

<p>A post was split to a new topic: <a href="/t/resize-and-move-the-slice-view-interactively-in-the-3d-view/44270">Resize and move the slice view interactively in the 3D view</a></p>

---

## Post #10 by @Davide_Punzo (2025-08-29 22:16 UTC)

<p>Thanks Andras for fixing it so fast !</p>

---
