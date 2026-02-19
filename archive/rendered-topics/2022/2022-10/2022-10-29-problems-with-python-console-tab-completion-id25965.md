---
topic_id: 25965
title: "Problems With Python Console Tab Completion"
date: 2022-10-29
url: https://discourse.slicer.org/t/25965
---

# Problems with Python console tab completion

**Topic ID**: 25965
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/problems-with-python-console-tab-completion/25965

---

## Post #1 by @jamesobutler (2022-10-29 17:05 UTC)

<p>With recent python console changes I’m having difficulties using [TAB] to inspect available methods from the python console. I’m getting output upon pressing [TAB] which then breaks things up that I’m trying to type. It constantly prints out this error output when I type a new letter in the example below.</p>
<p>I’m using Slicer as of <a href="https://github.com/Slicer/Slicer/commit/9a56f644406357394f42004133c6ee13ae7e3ad3" class="inline-onebox" rel="noopener nofollow ugc">COMP: Fix Qt dependencies for application update · Slicer/Slicer@9a56f64 · GitHub</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f5381ca741357baeeebd815f45e8b16cbccc10.png" data-download-href="/uploads/short-url/tOwGZXL5RD7i6e3zwworvUm7pKw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f5381ca741357baeeebd815f45e8b16cbccc10.png" alt="image" data-base62-sha1="tOwGZXL5RD7i6e3zwworvUm7pKw" width="690" height="186" data-dominant-color="FBF3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1320×356 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-29 20:33 UTC)

<p>Auto-complete works by evaluating the expression. It has been always having side-effects but now that we display errors in the Python console, this side effect is more visible.</p>
<p>Maybe the simplest would be to suppress all outputs during these auto-completion evaluations. Please submit a Slicer issue and set its target to 5.2.</p>

---

## Post #3 by @jamesobutler (2022-10-29 21:10 UTC)

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6630">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6630" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6630" target="_blank" rel="noopener nofollow ugc">Auto complete difficult to use with latest python console changes</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-29" data-time="21:10:23" data-timezone="UTC">09:10PM - 29 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
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

As originally discussed in https://discourse.slicer.org/t/problems<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">-with-python-console-tab-completion/25965

## Steps to reproduce

Use `slicer.app.layoutManager().threeDWidget(index).[TAB]` as shown in the video below:

https://user-images.githubusercontent.com/15837524/198852374-3f19cd0b-f310-48e3-b9bf-f08a4c2d1e4a.mp4

From @lassoan 

&gt; Maybe the simplest would be to suppress all outputs during these auto-completion evaluations. 


## Environment
- Slicer version: Slicer-5.1.0-2022-10-27
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @jcfr (2022-11-02 03:13 UTC)

<p>Following the integration of the <a href="https://github.com/Slicer/Slicer/pull/6638">Slicer pull request #6638</a> integrating CTK changes from <a class="mention" href="/u/lassoan">@lassoan</a> and tested by <a class="mention" href="/u/jamesobutler">@jamesobutler</a> , the autocomplete behavior has been revisited:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://user-images.githubusercontent.com/219043/199385422-d7917607-eec8-4416-90d2-71119d468fd7.png" alt="image" width="690" height="133"></td>
<td><img src="https://user-images.githubusercontent.com/219043/199386361-bfa23e84-706b-4692-8d85-2b53f5278e92.png" alt="image" width="690" height="77"></td>
</tr>
</tbody>
</table>
</div>

---
