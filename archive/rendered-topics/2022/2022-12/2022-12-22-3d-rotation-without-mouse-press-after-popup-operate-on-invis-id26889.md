---
topic_id: 26889
title: "3D Rotation Without Mouse Press After Popup Operate On Invis"
date: 2022-12-22
url: https://discourse.slicer.org/t/26889
---

# 3D Rotation without mouse press after Popup "Operate on invisible segment?"

**Topic ID**: 26889
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/3d-rotation-without-mouse-press-after-popup-operate-on-invisible-segment/26889

---

## Post #1 by @Deep_Learning (2022-12-22 18:12 UTC)

<p>I am assuming that this is a small bug.<br>
Have had this problem with many versions of Slicer including 5.3.0.</p>
<p>Here is a reproducible example.<br>
Download Sample Data CTChest.<br>
Run TotalSegmentator.<br>
Select All Segmentation nodes.<br>
Toggle Visibility.<br>
Turn on only Aorta visibility.<br>
Switch to Segment Module.<br>
Probably need to select master volume.<br>
Press Show 3D and Center View.</p>
<p>Select Scissors.<br>
*<em>Note Aorta is visible, but spleen is selected. <strong>My bad, user error</strong></em></p>
<p>Now, try to use scissors in 3D view. First mouse button.<br>
Popup “Operate on invisible segment?”<br>
Press cancel.</p>
<p>Now move cursor in 3DView without mouse press…<br>
“3D Rotation without mouse press”!!!</p>

---

## Post #2 by @lassoan (2022-12-22 18:47 UTC)

<p>Thanks for reporting this. I’ve also run into this issue a few times and it is indeed a bug. The workaround is to deactivate the effect and click in the view. I’ve added an issue to track the resolution:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6748">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6748" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6748" target="_blank" rel="noopener">Mouse behavior is incorrect after "Operate on invisible segment" popup</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-22" data-time="18:46:55" data-timezone="UTC">06:46PM - 22 Dec 22 UTC</span>
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

Mouse behavior is incorrect after initiating editing operation on <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">a hidden segment and the "Operate on invisible segment" popup is displayed.

Reported at: https://discourse.slicer.org/t/3d-rotation-without-mouse-press-after-popup-operate-on-invisible-segment/26889

## Steps to reproduce

- Download Sample Data CTChest.
- Create a segment
- Hide the segment
- Activate Scissor effect
- Click in the 3D view
- Popup appears: “Operate on invisible segment?”
- Press cancel.
- Move cursor in 3D view (without mouse button press)

The 3D view rotates as the mouse is moved around.

## Expected behavior

After the popup is dismissed, the view should work correctly (only rotates if the mouse button is depressed).

## Workaround

After the popup is displayed, the proper mouse behavior can be achieved by deactivating the effect and clicking in the view. 

## Environment
- Slicer version: Slicer-5.2.1
- Operating system: all</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Deep_Learning (2022-12-22 19:04 UTC)

<p>Thanks, I always thought that it was my fault.<br>
Maybe it was a feature that I did not understand<br>
Maybe I was dragging the mouse, triple clicking, etc.</p>
<p>Only the ease of use of the TotalSegmenter Module allowed reproducibility.</p>

---
