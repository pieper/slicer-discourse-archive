# Segment Editor:  clicking eye to toggle visibility should not select segment

**Topic ID**: 20237
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/segment-editor-clicking-eye-to-toggle-visibility-should-not-select-segment/20237

---

## Post #1 by @DIV (2021-10-19 11:51 UTC)

<p>In a segmentation it is common to create multiple segments in the Segment Editor module.</p>
<p>The current behaviour is that clicking eye displayed adjacent to an individual segment to toggle the visibility of that segment will automatically result in that segment being selected.<br>
I believe that this behaviour is undesirable.</p>
<p>A common usage of Segment Editor is as follows.</p>
<ol>
<li>Segment “1” is visible, and being edited with some Effect, while all other segments are hidden.</li>
<li>Editing of Segment 1 seems complete.  To check that it matches well with the current Segment 3, click the eye adjacent to Segment 3 to make Segment 3 visible.  (Segment 3 is automatically selected.)</li>
<li>Now it is desired to edit Segment 3.  Therefore it may be preferred to hide Segment 1 — e.g. if using the Scissors effect, or to prevent Segment 1 from obscuring portions of Segment 3.  To do this, click the eye adjacent to Segment 1 to make Segment 1 hidden.  (Segment 1 is automatically selected.)</li>
<li>Now Segment 3 is visible, and Segment 1 is hidden, so it seems safe to apply the preferred effect to Segment 3.  But — oops! — actually it was Segment 1 that was unintentionally selected!!!</li>
</ol>
<p>Desired behaviour.</p>
<ul>
<li>toggling visibility does <em>not</em> cause a segment to be selected;</li>
<li>editing a segment’s colour (double-clicking the swatch) does <em>not</em> cause a segment to be selected;</li>
<li>toggling/setting a segment’s status does <em>not</em> cause a segment to be selected;</li>
<li>segments are <em>only</em> selected by clicking (or double-clicking) on their <strong>Name</strong>.</li>
</ul>
<p>—DIV</p>

---

## Post #2 by @lassoan (2021-10-20 02:36 UTC)

<p>Agreed. We already have a feature request for this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5290">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5290" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5290" target="_blank" rel="noopener">Toggling visibility shouldn't affect selection (segmentations, markers, models, etc...)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-11-02" data-time="17:31:18" data-timezone="UTC">05:31PM - 02 Nov 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fusentasticus" target="_blank" rel="noopener">
          <img alt="fusentasticus" src="https://avatars.githubusercontent.com/u/11786553?v=4" class="onebox-avatar-inline" width="20" height="20">
          fusentasticus
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I believe this is a bug, not a feature request, in so far as the behavior is inc<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">onsistent with standard UI design (afaik).

In the Segmentation Editor, when toggling visibility of a segment, the selection should not be affected; in particular, it should not be changed to that of the segment whose visibility was changed. 

This leads (for me) to very frequent operations of the wrong segment and it's sometimes hard to discover that the operation was misapplied.

The problem is general to all of the 3D slicer UI it seems:  toggling visibility for markups, models, etc. affects the selection. I think the correct behavior is that it shouldn't.

## Environment
- Slicer version: Slicer-4.11
- Operating system: Windows / Linux / Mac + which version</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can add a thumbs up to the issue to indicate that you are interested. While it should not be a too difficult change, it would not be trivial either, and there are many higher-priority tasks, so if you want to see this fixed in the near future then your contribution would be welcome (developing yourself or hiring a developer).</p>

---

## Post #3 by @DIV (2021-10-20 06:31 UTC)

<p>Thanks, lassoan: I have added my support to the feature request (or, alternatively, bug report).<br>
Although I did search the forum before posting, I hadn’t found that logged issue.<br>
—DIV</p>

---

## Post #4 by @mikebind (2023-07-18 19:15 UTC)

<p>I run into this problem all the time and accidentally edit the wrong segment.  I added my vote here (I think this is the current preferred method?) and also a thumbs up to the bug report (maybe an old method?, but recommended above).  Changing visibility or status should definitely not affect which segment is selected.  Changing color I am ambivalent about as that feels more like working with the segment because of Slicer’s involved methods of color selection, but would be happy either way.</p>

---

## Post #5 by @lassoan (2023-07-25 12:28 UTC)

<p>Voting here is the right method for bringing feature requests into the developers’ attention.</p>
<p>I ran into the issue of accidentally editing the wrong segment after hiding it, but since invisible segments are not allowed to be edited by default (you get a warning popup), this does not happen to me anymore. Updating the selection when you show a segment is actually a quite useful feature (you often want to edit the segment that you have just displayed). So, overall the current implementation is quite safe now (and maybe I even prefer how it works now).</p>
<p>However, this can be still considered as a bug in the sense that “a bug is a feature that cannot be turned off”. I agree that at least we should make it optional to update the selection on any click.</p>

---

## Post #6 by @mikebind (2023-07-25 16:26 UTC)

<p>Yes, I appreciate the warning pop-up, and since it was implemented it does often prevent me from <em>actually</em> editing the wrong segment.  However, it is very much not the case that if I make a segment visible that means that I want to edit it; I am often actively managing the visibility of different segments while preparing to edit one, and I still often accidentally edit the wrong one and have to undo the edit (because the one I accidentally edited is visible).</p>
<p>My intuitive workflow is:</p>
<ol>
<li>Select segment to edit</li>
<li>Set up the operation parameters</li>
<li>Manage other segment visibility to ensure that the correct segment has been selected as a modifier (if relevant), or to ensure that the results will be visible as desired, or to ensure that the correct regions are editable or excluded from editing (if using editable region as inside, or outside, all visible segments).</li>
<li>Press Apply.</li>
</ol>
<p>To me, step 3 (managing visibility as part of setting operation parameters) is independent of step 1 (selecting the segment to edit), but in Slicer changing visibility changes the selection, and I need to remember to add in a step between 3 and 4 to “Re-select the segment to edit”.</p>
<p>For some concrete examples, when using logical operations to add, subtract, copy, or intersect segments, I usually want both the segment I am working on editing AND the modifier segment to be visible when I carry out that operation.  That usually means that I select the segment I want to edit, set up the operation, and then I very often have several clicks to to show the modifier segment and perhaps hide other segments, and then I click Apply.  When I do this, I either accidentally apply the effect to the intended modifier segment (a silent error that I have to catch on my own) or I get a warning that I am trying to edit a segment which is not visible and it is automatically made visible. This second outcome is much better than silently editing a hidden segment, but I don’t want that segment visible, and thick as I am, after canceling the edit, I click on the desired segment to select it, then click to hide the newly visible undesired segment (unintentionally selecting it again!) and click Apply.  This raises the warning again, shows the undesired segment again, and usually this time I remember, and click the desired segment to select it, click to hide the undesired segment, then click to select the desired segment again.</p>

---

## Post #7 by @Martin2 (2025-09-06 21:34 UTC)

<p>Just registered to ask for this feature, and then saw it’s already been requested.<br>
Currently it behaves contrary to Photoshop, so users that are used to Photoshop probably run into this trap a lot.</p>

---
