---
topic_id: 26890
title: "Markup Subject Folder Disappears After Toggling Visibility I"
date: 2022-12-22
url: https://discourse.slicer.org/t/26890
---

# Markup subject/folder disappears after toggling visibility in data module

**Topic ID**: 26890
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/markup-subject-folder-disappears-after-toggling-visibility-in-data-module/26890

---

## Post #1 by @Karl_Hahn (2022-12-22 20:12 UTC)

<p>The following steps seem to produce unexpected behavior.</p>
<ol>
<li>In Markups module “Node” table, right click and choose either “Create new subject” or “Create new folder”.</li>
<li>In Data module, locate newly created subject/folder and modify visibility or color.</li>
<li>Return to Markups module and observe that the newly created subject/folder is no longer available.</li>
</ol>
<p>Is it actually expected? Are markup folders not supposed to be modified via the Data module?</p>
<p>Edit: if a markup is subsequently made a child of the subject/folder via the Data module, then the folder/subject appears as expected in the Markups module.</p>

---

## Post #2 by @jamesobutler (2022-12-22 21:11 UTC)

<p>Yes this is a topic currently being tracked in the Slicer issues tracker:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6596">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6596" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6596" target="_blank" rel="noopener nofollow ugc">Toggling empty markups folder visibility makes it disappear</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-18" data-time="15:46:05" data-timezone="UTC">03:46PM - 18 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/malbi" target="_blank" rel="noopener nofollow ugc">
          <img alt="malbi" src="https://avatars.githubusercontent.com/u/26160797?v=4" class="onebox-avatar-inline" width="20" height="20">
          malbi
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
    <p class="github-body-container">## Summary

In markups module, clicking on the eye icon to set visibility OFF <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">of an empty folder makes it disappear.
In data module, clicking on the eye icon to set visibility ON of the same folder does not make it reappear in markups module.

## Steps to reproduce

- Choose "Markups" module
- In subject hierarchy, create a folder
- Toggle folder visibility off
- Folder disappear from markups subject hierarchy

## Expected behavior

Folder is still visible in markups subject hierarchy with visibility off (closed eye). This is the behavior in data module.

## Environment
- Slicer version: Slicer-5.1.0-2022-10-17-linux-amd64
- Operating system:  Linux 5.13.0-52-generic Ubuntu 20.04.1</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please see the first comment made in that GitHub issue which has specific details of what is going on currently. The issue is currently targeted for this next development period, but an estimated date for this issue to be resolved is TBD.</p>

---

## Post #3 by @Karl_Hahn (2022-12-22 21:59 UTC)

<p>Thanks for the reference!</p>

---
