---
topic_id: 39884
title: "Curve Tool Not Producing Measurements"
date: 2024-10-27
url: https://discourse.slicer.org/t/39884
---

# Curve Tool Not Producing Measurements

**Topic ID**: 39884
**Date**: 2024-10-27
**URL**: https://discourse.slicer.org/t/curve-tool-not-producing-measurements/39884

---

## Post #1 by @milbelle (2024-10-27 15:30 UTC)

<p>Hello!</p>
<p>I’m quite new to Slicer so please be patient with me! I’m attempting to measure sulcal length on an endocast with the curve tool, however no measurements pop up. Is there something I’m doing wrong? In my attempts to look into it, it seems that the measurements should just appear.</p>
<p>Let me know what you think!</p>
<p>Thanks so much for your help.</p>

---

## Post #2 by @lassoan (2024-10-27 15:34 UTC)

<p>You can choose what measurements are done in Markups module, Measurements section. At some point there were issues with using SlicerMorph customizations removing measurements, but those were fixed in revent Slicer Preview Releases. If you don’t see measurements in Markups module then install the latest Slicer Preview Release.</p>

---

## Post #3 by @milbelle (2024-10-27 16:10 UTC)

<p>For some reason my mac refused to open the preview release file saying that it can’t verify that the software is free from malware. Any work arounds?</p>

---

## Post #4 by @milbelle (2024-10-27 16:21 UTC)

<p>I got it to open, but the measurement section is still blank when I use the curve tool.</p>

---

## Post #5 by @lassoan (2024-10-27 16:54 UTC)

<p>Can you save the scene as a .mrb file and share it (upload somewhere - dropbox, onedrive, google drive, … - and post ths link here) so that we can have a look?</p>

---

## Post #6 by @jamesobutler (2024-10-27 17:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="39884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>At some point there were issues with using SlicerMorph customizations removing measurements, but those were fixed in revent Slicer Preview Releases.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> That resolved the following linked issue or it still exists and the issue should remain open?</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7239">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7239" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7239" target="_blank" rel="noopener nofollow ugc">Adding a default Markups node to scene removes measurements</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-22" data-time="19:48:40" data-timezone="UTC">07:48PM - 22 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/smrolfe" target="_blank" rel="noopener nofollow ugc">
          <img alt="smrolfe" src="https://avatars.githubusercontent.com/u/43060230?v=4" class="onebox-avatar-inline" width="20" height="20">
          smrolfe
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

The [code snippet ](https://projectweek.na-mic.org/PW39_2023_Montr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eal/Projects/UndoRedo/)to enable undo/redo for Markups is causing a bug where the measurements for the nodes are no longer displayed, even when measurements are enabled. This occurs for any Markups node when a default node for that class is added to the scene. Removing the default nodes from the scene fixes the bug. This issue was discussed on the Slicer forum [here](https://discourse.slicer.org/t/markups-tools-not-measuring-slicer-5-4-0/31609/8).

## Steps to reproduce
1. Add a line node to the scene to confirm measurements are displayed.

2. Run the following snippet:
`className = "vtkMRMLMarkupsLineNode"`
`node = slicer.mrmlScene.CreateNodeByClass(className)`
`slicer.mrmlScene.AddDefaultNode(node)`

3. Add another line node to the scene to confirm measurements are no longer displayed.

4. To restore measurements, run:
`slicer.mrmlScene.RemoveAllDefaultNodes()`

## Expected behavior

Adding a default node to the scene should not impact unmodified node properties.

## Environment
- Slicer version: Slicer-5.4.0 and 5.5.0
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2024-10-27 17:39 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for finding the relevant ticket.</p>
<p>This issue was “fixed” by <a href="https://github.com/SlicerMorph/SlicerMorph/commit/248235d5814e8cb91d709598658971d4753d35f9">avoiding defining default nodes for markups</a>, but I’ve now submitted a <a href="https://github.com/Slicer/Slicer/pull/8012">pull request that fixes the root cause of the issue</a>.</p>
<p><a class="mention" href="/u/milbelle">@milbelle</a> It would help if you could share your scene with us or provide step-by-step instructions for reproducing the issue.</p>

---

## Post #8 by @milbelle (2024-11-24 12:59 UTC)

<p>Hi! I would like to provide an update. I figured out how to make the curve tool work. I just have to create a line using the line tool first, and then the curve tool will show measurements. Thanks!</p>

---

## Post #9 by @lassoan (2024-11-24 13:04 UTC)

<p>Curve measurements should work well in the latest Slicer Preview Release. If your find that your still need any workaroundin this Slicer version then let us know. Thanks!</p>

---
