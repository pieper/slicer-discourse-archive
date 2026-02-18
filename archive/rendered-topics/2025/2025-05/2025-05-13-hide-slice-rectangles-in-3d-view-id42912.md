# Hide slice rectangles in 3D view

**Topic ID**: 42912
**Date**: 2025-05-13
**URL**: https://discourse.slicer.org/t/hide-slice-rectangles-in-3d-view/42912

---

## Post #1 by @spichardo (2025-05-13 20:38 UTC)

<p>Operating system: macOS 15.4.1<br>
Slicer version: 5.8.1<br>
Expected behavior: Old versions of 3DSlicer didn’t show these rectangles, they are in the way for illustration purposes<br>
Actual behavior: The “new” rectangles are shown all the time, I can’t find what option to select to hide them. I tried to click every option but I can’t find which is the one controlling its visibility. I know it has to be somewhere. Thanks for any tip.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820.jpeg" data-download-href="/uploads/short-url/8wx7FQlUCMxzldwQVxJs57xYldm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820_2_508x500.jpeg" alt="image" data-base62-sha1="8wx7FQlUCMxzldwQVxJs57xYldm" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820_2_508x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820_2_762x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbee0a001d241dd831c6fdadbb174ff31644820.jpeg 2x" data-dominant-color="918EB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×992 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2025-05-13 23:08 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="11381">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/show-slice-edges-in-3d-view/11381">Show slice edges in 3D view</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    Most medical image viewer software uses color coding to make it easier to distinguish slices in  3D  views. It would not be hard to do (you can try by copy-pasting a few lines of code into the Python console). 
<img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/play_button.png?v=14" title="play_button" alt="play_button" class="emoji"> 
Code snippet to show slice edges
Should we do it, too? 
My concern would be that it may make the views a bit too busy: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a672ba2b6f39a766975b4a5550c2296940b1db.jpeg" data-download-href="/uploads/short-url/rD6LrTfnJVcvvf8QWIORlJfORTR.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
It might be particularly confusing when the displayed image is smaller than the frame (this happens most of the case): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d85d37cf479516c564217d415f201f41dd67b69.jpeg" data-download-href="/uploads/short-url/mtvGplaX2EsokcDtCz49n8CyJ8R.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
It could be possible to set …
  </blockquote>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8008">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener nofollow ugc">ENH: Add option to display slice edges in 3D view</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>Punzo:slices3Dedge</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-25" data-time="09:30:38" data-timezone="UTC">09:30AM - 25 Oct 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
            Punzo
          </a>
        </div>

        <div class="lines" title="1 commits changed 25 files with 1298 additions and 294 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8008/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1298</span>
            <span class="removed">-294</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- Implemented functionality to show slice edges in the 3D view.
- Added user in<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8008" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">terface controls to control the visibility of slice edges.
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

## Post #3 by @lassoan (2025-05-14 03:14 UTC)

<p>You can show/hide it here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ba6c324056da3e856696f8a856ba13ac1459ee.jpeg" data-download-href="/uploads/short-url/tVlcoLE2GMM5WL1b8hbBJTvlDBQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ba6c324056da3e856696f8a856ba13ac1459ee_2_690x435.jpeg" alt="image" data-base62-sha1="tVlcoLE2GMM5WL1b8hbBJTvlDBQ" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ba6c324056da3e856696f8a856ba13ac1459ee_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ba6c324056da3e856696f8a856ba13ac1459ee_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1ba6c324056da3e856696f8a856ba13ac1459ee_2_1380x870.jpeg 2x" data-dominant-color="77777B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1212 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can set to show/hide it by defaut in the Application Settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4483fc35ebd13dd11082aaf75ee39ceeb82ccc43.png" data-download-href="/uploads/short-url/9M7fbFPz0olUDQq4mGMZRhNLozN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4483fc35ebd13dd11082aaf75ee39ceeb82ccc43.png" alt="image" data-base62-sha1="9M7fbFPz0olUDQq4mGMZRhNLozN" width="573" height="500" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">677×590 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @spichardo (2025-05-14 14:59 UTC)

<p>Hi, thanks a lot,<br>
Yes, that was one of the options I tried select/unselect several times, and the rectangle remained visible.<br>
For the record, this was a scene saved in a previous version of 3DSlicer (5.7.0), so no matter if I closed and reopened 3DSlicer and loaded the scene, the issue persisted. I used the IGT reslicer for the views. After seeing your answer, I just started a new scene from scratch, and then checkbox  works as expected. Not sure how to reproduce it. Thanks for the help, cheers.</p>

---

## Post #5 by @lassoan (2025-05-14 16:20 UTC)

<p>Let us know if you can reproduce the problem of not being able to hide the rectangle (using a saved scene or by following specific steps) and then we can investigate.</p>

---

## Post #6 by @mikebind (2025-05-14 19:27 UTC)

<p>I’ve run into this also, also when loading a scene from an earlier version of Slicer (5.6.1).  To reproduce:</p>
<ol>
<li>In Slicer 5.6.1, load MRHead sample data</li>
<li>Show one or more slice views in 3D</li>
<li>Save to MRB</li>
<li>Open MRB in Slicer 5.8.1<br>
Colored rectangles cannot be hidden. They resize appropriately with slices, but do not go away when slices are hidden.</li>
</ol>

---

## Post #7 by @lassoan (2025-08-29 17:04 UTC)

<p>For reference, a fix has been submitted here:</p>
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

## Post #8 by @sulli419 (2025-09-01 17:25 UTC)

<p>Glad I found this discussion.  I was having this issue as well.  Is the idea that we have to install a newer version of slicer to fix the bug, or is there some other way to hide the immortal frame?  Thanks.</p>

---

## Post #9 by @lassoan (2025-09-02 15:50 UTC)

<p>Probably the simplest is to switch to the Slicer Preview Release. You can probably also get rid of the frames by loading individual data files instead of loading the scene file (.mrml or .mrb file).</p>

---
