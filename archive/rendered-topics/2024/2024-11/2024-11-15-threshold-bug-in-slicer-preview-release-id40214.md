---
topic_id: 40214
title: "Threshold Bug In Slicer Preview Release"
date: 2024-11-15
url: https://discourse.slicer.org/t/40214
---

# Threshold bug in slicer preview release

**Topic ID**: 40214
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/threshold-bug-in-slicer-preview-release/40214

---

## Post #1 by @alientex (2024-11-15 08:20 UTC)

<p>Hello,</p>
<p>The threshold preview and apply operations do not work after following the steps below:</p>
<ol>
<li>Open the DICOM module, import, and load a DICOM directory.</li>
<li>Go to the Segment Editor and add a segment.</li>
<li>Open the threshold effect (do not apply the threshold yet) and press <strong>Ctrl + S</strong> to save the scene as an MRB file.</li>
<li>Close and reopen Slicer.</li>
<li>Load the saved MRB file.</li>
<li>Go to the Segment Editor. You should see the threshold effect open, but no preview is visible in 2D.</li>
<li>Nonetheless, try applying the threshold. However, the threshold does not apply.</li>
</ol>
<p>Can anyone confirm if this is a bug and suggest how to resolve it?</p>
<p>Slicer version 5.7 preview.</p>

---

## Post #2 by @alientex (2024-11-19 05:45 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/jcfr">@jcfr</a> Any idea?</p>

---

## Post #3 by @muratmaga (2024-11-19 05:59 UTC)

<p>Please share a log file where you reproduce this.</p>

---

## Post #4 by @muratmaga (2024-11-19 06:05 UTC)

<p>I can reproduce this, you don;t need dicom. It definitely reproduces with sample MRHead data as you described.</p>
<p>I suspect this has something to do with saving an empty segmentation object. Because I delete the segmentaiton, and recreate it, threshold tool starts working again.</p>
<p>I think it does qualify as a bug. And I am not seeing any errors in the log file.</p>

---

## Post #5 by @pieper (2024-11-19 13:46 UTC)

<aside class="quote no-group" data-username="alientex" data-post="1" data-topic="40214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e79b87/48.png" class="avatar"> alientex:</div>
<blockquote>
<p>Open the threshold effect (do not apply the threshold yet) and press <strong>Ctrl + S</strong> to save the scene as an MRB file.</p>
</blockquote>
</aside>
<p>This is probably the issue, because a transient ‘preview’ of the threshold is not intended to be saved and restored.  It’s sort of like a popup menu that you wouldn’t expect to be back when you reload the scene.</p>
<aside class="quote no-group" data-username="alientex" data-post="1" data-topic="40214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e79b87/48.png" class="avatar"> alientex:</div>
<blockquote>
<p>Nonetheless, try applying the threshold. However, the threshold does not apply.</p>
</blockquote>
</aside>
<p>This probably is a problem, in that the state of the scene becomes inconsistent.  I guess that save operations should trigger an even that the segment editor (and other modules) can respond to and put the scene into a consistent state.</p>

---

## Post #6 by @muratmaga (2024-11-19 17:41 UTC)

<p>Should we open an issue or do you consider this a corner care?</p>

---

## Post #7 by @pieper (2024-11-19 18:59 UTC)

<p>Yes, I think it’s a corner case, but it should be tracked anyway so thanks if you can file an issue.  <a class="mention" href="/u/lassoan">@lassoan</a> showed us an in-progress fix that he thinks would address this.</p>

---

## Post #8 by @muratmaga (2024-11-19 19:25 UTC)

<p>OK create a brief report to track this:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8057">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8057" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8057" target="_blank" rel="noopener nofollow ugc">Threshold tool becomes unfunctional if a scene saved with a blank segmentation and reloaded</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-19" data-time="19:24:59" data-timezone="UTC">07:24PM - 19 Nov 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
If someone activates the threshold tool, but not use it, and then pr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">oceeds to save scene in that state, and reloads, the threshold tool cannot be activated. I have not tested whether other effects from the same problem 
## Steps to reproduce
Specifics are discussed in this thread: 
https://discourse.slicer.org/t/threshold-bug-in-slicer-preview-release/40214/7

## Environment
- Slicer version: Slicer-5.7 preview</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2024-11-20 21:20 UTC)

<p>The issue is fixed now. It is available in Slicer Preview Releases that you download tomorrow or later.</p>

---
