---
topic_id: 46835
title: "Strange folder bug"
date: 2026-04-25
url: https://discourse.slicer.org/t/46835
last_bumped: 2026-05-07T11:14:40.118Z
---

# Strange folder bug

**Topic ID**: 46835
**Date**: 2026-04-25
**URL**: https://discourse.slicer.org/t/strange-folder-bug/46835

---

## Post #1 by @muratmaga (2026-04-25 23:12 UTC)

<p>In the latest preview in Macos, data module is behaving strangely:</p>
<ol>
<li>Load two models in a blank scene</li>
<li>Create a NewFolder</li>
<li>Put the models in the NewFolder</li>
<li>Hit the visibility icon at the NewFolder and notice that those two models are now moved out of the NewFolder (they are at the same level, not nested in).</li>
</ol>
<p>Subsequent ones (newfolders) do not show this behavior. They work correctly. This is vanilla slicer.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @mikebind (2026-04-27 02:01 UTC)

<p>I have noticed odd bugs like this in subject hierarchy for a long time (I think since at least 5.6), but I never successfully came up with a reproducible series of actions which triggered incorrect behavior.  Thanks for reporting and finding a reproducible way to trigger. Hopefully this will help lead to a solution!</p>

---

## Post #3 by @muratmaga (2026-04-27 04:52 UTC)

<p>yeah there are more than one. For example,</p>
<p>Opacity slider is not visible the first time. it becomes visible after you toggle the visibility:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa4cbaf27dd0edc80f2d1d98f5e4f9b531ec30f7.png" data-download-href="/uploads/short-url/zIfLcYTlhRejd2rxv1EEVEFzKPJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4cbaf27dd0edc80f2d1d98f5e4f9b531ec30f7_2_690x179.png" alt="image" data-base62-sha1="zIfLcYTlhRejd2rxv1EEVEFzKPJ" width="690" height="179" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4cbaf27dd0edc80f2d1d98f5e4f9b531ec30f7_2_690x179.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa4cbaf27dd0edc80f2d1d98f5e4f9b531ec30f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa4cbaf27dd0edc80f2d1d98f5e4f9b531ec30f7.png 2x" data-dominant-color="CDD7DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">877×228 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2026-05-07 11:14 UTC)

<p>Reference to the GitHub issue, where this conversation will be continued</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9130">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9130" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9130" target="_blank" rel="noopener">SH folder is misbehaving in Data module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-04-27" data-time="21:46:40" data-timezone="UTC">09:46PM - 27 Apr 26 UTC</span>
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
    <p class="github-body-container">as reported on the forum: https://discourse.slicer.org/t/strange-folder-bug/4683<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">5/3

### issue1: losing hierarchy:
In the latest preview in Macos, data module is behaving strangely:

    Load two models in a blank scene
    Create a NewFolder
    Put the models in the NewFolder
    Hit the visibility icon at the NewFolder and notice that those two models are now moved out of the NewFolder (they are at the same level, not nested in).

Subsequent ones (newfolders) do not show this behavior. They work correctly. This is vanilla slicer.

### issue2: Missing opacity slider

1. Create a segmentation (with couple items in it)
2. Convert to model reprsentation using the right click in Data module.
3. Right click the visibility (eye) icon for the Model folder and notice that opacity slider is not there. 
4. Toggle the folder visibility on/off and see that opacity slider comes back.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
