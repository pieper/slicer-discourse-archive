---
topic_id: 35156
title: "Locking A Segment For Edits"
date: 2024-03-28
url: https://discourse.slicer.org/t/35156
---

# Locking a segment for edits

**Topic ID**: 35156
**Date**: 2024-03-28
**URL**: https://discourse.slicer.org/t/locking-a-segment-for-edits/35156

---

## Post #1 by @muratmaga (2024-03-28 16:39 UTC)

<p>Would it be possible to implement a function that will lock a segment for further edits (regardless whether it is set to visible or not, and overriding all other editable area settings)?</p>
<p>Sometimes I overlook my editable area settings and proceed a quite a few steps only to find out that I edit my other segments (in slices that I wasn’t looking) were overwritten.</p>

---

## Post #2 by @VincentYu (2024-03-28 23:11 UTC)

<p>How about making a copy of the segments you want to preserve to another segmentation? Sometimes I create like processing/processed segmentations to deal with this problem.</p>

---

## Post #3 by @muratmaga (2024-03-28 23:37 UTC)

<p>That’s a possibility, but more cumbersome and possibly more error prone. I can totally see (at least myself) forgetting to switch to the right segmentation to continue the procedure.</p>

---

## Post #4 by @lassoan (2024-03-29 00:42 UTC)

<aside class="quote no-group" data-username="VincentYu" data-post="2" data-topic="35156">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincentyu/48/69793_2.png" class="avatar"> VincentYu:</div>
<blockquote>
<p>How about making a copy of the segments you want to preserve to another segmentation?</p>
</blockquote>
</aside>
<p>Yes, this is what I would recommend, too.</p>
<p>This use case was one of the reasons why we decided not to immediately resample a segment to the common geometry when it is drag-and-dropped into a segmentation (it is done only when the segmentation is edited). This allows keeping segments exactly the same while moving them between segmentations.</p>
<p>It would be possible to move out “locked” segments into some read-only layers within a segmentation internally, but drag-and-dropping segments between segmentations is already quite easy, adding locking would further complicate the already complex GUI, and the implementation would proably take several weeks</p>

---

## Post #5 by @muratmaga (2024-03-29 04:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="35156">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This use case was one of the reasons why we decided not to immediately resample a segment to the common geometry when it is drag-and-dropped into a segmentation (it is done only when the segmentation is edited). This allows keeping segments exactly the same while moving them between segmentations.</p>
</blockquote>
</aside>
<p>It works certainly, but it is a bit cumbersome. First, it requires me to leave the segment editor and stop what I am doing. Second, it takes additional effort to set the visibility of the copied segment off. Since it all segmentations are displayed by default, it gets confusing.</p>
<p>As a trade of would it be possible to some how incorporate copy functionality into the segment editor’s right-click interaction? Something like “copy segment to a new segmentation” and maybe set the resultant segmentation invisible?</p>

---

## Post #6 by @lassoan (2024-03-29 12:57 UTC)

<p>Moving segments between segmentations is available in Segmentations module (<code>Copy/Move segments</code>). You can create a new segmentation, select one or more segments and move them to the new segmentation by a few clicks. Moving them is similarly very easy. I recommend moving instead of copying, as copying would create a new segment IDs, you would need to adjust visibility, etc.</p>
<p><code>Copy/move segments</code> is not in Segment Editor module because there are just so many operations on Segmentations that adding them all to a single module made the GUI very difficult to navigate. We keep a dedicated button to jump between Segmentations and Segment Editor to make all features available for both modules by a single click. But if it is still not easy enough then we can think about how to make even simpler:</p>
<ul>
<li>We could add a <code>Copy/move segments</code> to the drop-down menu of the green arrow button (similarly to <code>Import/export nodes</code>) - that would jump right to the relevant section in the Segmentations module GUI. This way the user would not need to scroll, but it would mean one extra click.</li>
<li>We could duplicate the <code>Copy/move segments</code> section in <code>Segment Editor</code> module. This would make the Segment Editor module GUI more complex, which may worth it if this feature is used very often during segment editing, but if it is not used routinely then it may be better to have it two clicks away.</li>
</ul>

---

## Post #7 by @mikebind (2024-03-29 23:27 UTC)

<p>In terms of complexity, the meaning and screen real estate needed to accommodate a a locked/unlocked column in the Segment Editor module seems minimal and like it would be easily understood by users.  The implementation, of course, would be more complex, since it would probably need to function sort of like a per-segment editable/masking function that would need to interact correctly with the implementations of all segment editing tools. If available, I would probably use this functionality sometimes, but I can’t say I miss it very much.  I occasionally make mistakes because of inattentiveness to masking/editable area settings, but I run into <a href="https://discourse.slicer.org/t/segment-editor-clicking-eye-to-toggle-visibility-should-not-select-segment/20237">the segment visibility selection  issue</a> far more often.</p>

---

## Post #8 by @lassoan (2024-03-30 13:48 UTC)

<p>There are a lot of potential new features that compete with each other, not just in term of development and maintenance time but also screen real estate, complexity that users can handle, complexity of software implementation, perserving or improving speed despite adding more features, etc. Therefore, we need very strong use cases to justify significant changes and find solutions that satisfy multiple use cases; or find creative ways of solving issues with minimal changes.</p>
<p>I’ve modified segments accidentally many times and undo/redo and visibility warnings helped a lot, but it still happens to me sometimes, so I think it is worth spending some time with thinking about how to improve this. But we need better solutions than locking segment, because that does not address the original issue (I would often not think about locking a segment or I would often not want to spend time with locking/unlocking). It would also increase complexity of GUI, implementation, may case performance degradation, etc.</p>
<p>So, let’s keep thinking about solutions that would directly address the issue of unintended changes, and try to find a solution that would be easy to implement and use.</p>
<p>For example, if the issue is that you don’t realize that changes are made to other segments then we could indicate to the users when other segments are changes. We could flash modified segments in the segment list (although this would not work well when there are many segments and not all of them are visible in the list) or show in the status bar for a few seconds which segments are modified (if other segments than just the current one are modified). You would then have a chance to undo immediately. These are just examples, keep the ideas coming.</p>

---

## Post #9 by @jamesobutler (2024-03-30 14:10 UTC)

<p>I would prefer the default masking settings to be “Allow Overlap” instead of “Overwrite All”. This from the perspective that a new user is more confused when a segment overwrites another segment as there is no clear indication or expectation that will happen without reviewing masking options. Once you know, you know, but it doesn’t seem to be intuitive expectation.</p>

---

## Post #10 by @chir.set (2024-03-30 16:37 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="35156">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>instead of “Overwrite All”.</p>
</blockquote>
</aside>
<p>‘Allow Overlap’ is not factory default but can be globally set in ‘Application settings / Segmentations’.</p>

---

## Post #11 by @bobcieri (2025-03-19 18:57 UTC)

<p>I also agree that this would be very useful. Sometimes I need to separate connections between materials and the best way to do this is to create ‘blockages’ between the connected segments, and then use the brush tool to re-add the materials at the borders of the blockages.</p>
<p>Moving the ‘blocked’ material over to another segmentation is not completely effective, because it won’t allow me to prevent those voxels from being assigned to materials in the original segmentation.</p>
<p>Another solution could be to add something to the “Masking: Editable Area” functionality to include the option to say OUTSIDE Segment 1, for example. It would have to actually be OUTSIDE Segment 1 &amp; Inside All Other Visible Segments.</p>
<p>Another solution could be to have another box in the Masking window that allowed you to mask materials individually.</p>

---
