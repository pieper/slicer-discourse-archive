# Abnormal segmentation behavior

**Topic ID**: 31520
**Date**: 2023-09-02
**URL**: https://discourse.slicer.org/t/abnormal-segmentation-behavior/31520

---

## Post #1 by @mohammed_alshakhas (2023-09-02 18:42 UTC)

<p>i had this recurring behavior lately . other segments disappearing  upon new segments editing or creation<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550090d037815bc9b0d5dd50a272f0b340ec157d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550090d037815bc9b0d5dd50a272f0b340ec157d.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550090d037815bc9b0d5dd50a272f0b340ec157d.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @ylcnkzy (2023-09-06 13:33 UTC)

<p>You are editing <strong>Segment-2</strong> while <strong>capillary</strong> segmentation is selected. Probably, when you make changes (edits) on " Segment-2 (but actually capillary)", it probably <strong>overwrites all visible segments</strong> (probably due to your segmentation settings). if the area you are editing has different HU values than Segment 2 (as a setting), then any changes you are going to make (even a single pixel) on Segment 2 while “capillary” is selected will overwrite the visible segment.</p>
<p><strong>Solution:</strong> If you intended to make changes to segment 2, just unselect all others (including <strong>capillary</strong>), then select segment 2 and proceed with your editing like that.</p>
<p>I hope that helps.</p>

---

## Post #3 by @mohammed_alshakhas (2023-09-06 13:45 UTC)

<p>thank you for response</p>
<p>my workflow is the following<br>
segment  mandible ( segment 2)  using threshold/paint ( everywhere )<br>
segment condyle (capillary)  : threshold/paint ( inside segment 2 + allow overlap )</p>
<p>i used this workflow many times before and was fine.</p>
<p>which part of the segmentation setting will erase the whole segment despite “allow overlap”?</p>

---

## Post #4 by @lassoan (2023-09-07 17:23 UTC)

<p>Did the segments actually change (e.g., also disappeared in slice views as well) or it was just a rendering issue in the 3D view?</p>

---

## Post #5 by @mohammed_alshakhas (2023-09-07 18:11 UTC)

<p>Only in rendering in view 1. View 2 is not affected</p>

---

## Post #6 by @lassoan (2023-09-07 18:16 UTC)

<p>What Slicer version is this?</p>
<p>Do you have an Apple silicon (ARM) system? Apple’s intel emulator does not seem very robust. Maybe upgrading your system will fix the issue.</p>
<p>Can you reproduce the behavior if you save the scene, restart Slicer, and load the scene?<br>
Can you reproduce it on a different computer? (or can you share the scene with us so that we can try it on different computers)</p>

---

## Post #7 by @mohammed_alshakhas (2023-09-07 18:28 UTC)

<p>Slicer 5.5 but happened more frequent before on 5.4 on Mac m2 .<br>
I don’t have access to other computer .<br>
Once the rendering issues occurs it’s permanent . Even after restart and opening the scene , rendering will not show on view 1 .<br>
The error only occurs once per scene .</p>

---

## Post #8 by @lassoan (2023-09-07 18:32 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="7" data-topic="31520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>Once the rendering issues occurs it’s permanent . Even after restart and opening the scene , rendering will not show on view 1 .</p>
</blockquote>
</aside>
<p>This is great! Any problems that we can reproduce we can fix. Could you share this scene file (upload somewhere and post the link here)? Make sure the image is anonymized (no protected health information is included).</p>

---

## Post #9 by @lassoan (2023-09-08 22:53 UTC)

<p>I was able to reproduce the issue. I’ve submitted a bug report here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7220">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7220" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7220" target="_blank" rel="noopener">Deleting the first segment removes closed surface representation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-08" data-time="22:52:18" data-timezone="UTC">10:52PM - 08 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
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

When removing the first segment in a segmentation and show 3D was <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">enabled, after the segment was removed, 3D is no longer displayed.

## Steps to reproduce

- Load a volume
- Create a segmentation with 3 segments
- Paint something into each segment
- Click Show 3D button to see the segmentation in 3D
- Remove the first segment

### Expected behavior

The first segment should be removed but all the other segments should be still visible in 3D.

### Actual behavior

All the segments disappear. Show 3D button is untoggled.

## Environment
- Slicer version: Slicer-5.4
- Operating system: Windows and Mac</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> would you be able to work on it? It seems that it is due to some modified event triggered by modification of a shared labelmap representation.</p>

---

## Post #10 by @Sunderlandkyl (2023-09-14 15:15 UTC)

<p>The issue is now fixed in the latest preview release with this PR: <a href="https://github.com/Slicer/Slicer/pull/7226" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix closed surface disappearing when segment is removed by Sunderlandkyl · Pull Request #7226 · Slicer/Slicer · GitHub</a>.</p>

---
