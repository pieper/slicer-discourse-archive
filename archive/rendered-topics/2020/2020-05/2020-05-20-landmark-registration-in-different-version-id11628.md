---
topic_id: 11628
title: "Landmark Registration In Different Version"
date: 2020-05-20
url: https://discourse.slicer.org/t/11628
---

# Landmark Registration in different version

**Topic ID**: 11628
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/landmark-registration-in-different-version/11628

---

## Post #1 by @syh91006 (2020-05-20 03:38 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.2 and 4.11.0<br>
Expected behavior: try to use Landmark Registration and “create and place” in the same version</p>
<p>Actual behavior:<br>
<strong>I would like to use Landmark Registration and the “create and place” in the same version!</strong></p>
<p>The “line” and " angle" in “create and place” are new functions which are only could found in ver. 4.11.0, but there is no Landmark Registration module in ver. 4.11.0. I used Landmark Registration module in old ver. 4.10.2, but there is no “create and place”  in old ver. 4.10.2.</p>
<p>Because there is always some problem if I transfer data from one version to the other, therefore I don’t like to do that. I would like to use this two function in the same version.</p>
<p>Could you give me some advice to solve this problem?<br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2020-05-20 04:19 UTC)

<p>Landmark registration module will soon be re-enabled in Slicer-4.11. You can track the progress here:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4764" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4764" target="_blank">Make Landmark registration module available</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-24" data-time="20:17:48" data-timezone="UTC">08:17PM - 24 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Landmark Registration module needs to be updated to work with redesigned markups module. Currently it is excluded from the build.</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">priority:medium</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">status:in-progress</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
