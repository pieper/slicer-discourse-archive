---
topic_id: 14219
title: "Lineprofile Following Proportional Distance Pr"
date: 2020-10-24
url: https://discourse.slicer.org/t/14219
---

# LineProfile : following proportional distance PR

**Topic ID**: 14219
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/lineprofile-following-proportional-distance-pr/14219

---

## Post #1 by @chir.set (2020-10-24 07:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Following commit and merge of that <a href="https://github.com/PerkLab/SlicerSandbox/pull/7" rel="noopener nofollow ugc">PR</a>,  an inconveniant behaviour of the ‘Apply button’ appeared by introducing</p>
<p>self.applyButton.checkBoxControlsButtonToggleState = True</p>
<p>It seems to be a <a href="https://github.com/Slicer/Slicer/issues/4717" rel="noopener nofollow ugc">desired</a> button behavior.</p>
<p>The check status of the checkbox controls the state of the toggle button. The problem is that whenever the button is clicked, the checkbox always gets unchecked. The button is no longer a toogle button (as it was before), but a simple button.</p>
<p>Now we can all live with that. Just in case you might deem it useful to restore back the previous parameter of the ‘Apply button’.</p>
<p>Thanks to the commit and its optmization.</p>

---

## Post #2 by @lassoan (2020-10-24 13:10 UTC)

<p>This how all the checkable pushbuttons work in Slicer when they control manual/automatic update. The problem with the previous behavior was that users were confused when the button was in a contradicting state: having the checkbox checked but the button not being pressed.</p>
<p>The current behavior avoids this possibility of misunderstanding and you can always enable auto-update the same way, with a single click (clicking on the checkbox).</p>

---
