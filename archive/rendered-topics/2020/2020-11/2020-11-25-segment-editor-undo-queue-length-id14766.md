# Segment Editor undo queue length

**Topic ID**: 14766
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/segment-editor-undo-queue-length/14766

---

## Post #1 by @hherhold (2020-11-25 12:51 UTC)

<p>How much memory is used up when the state is saved for Undo in Segment Editor? Sometimes when working with really large datasets (&gt;10GB) in Segment Editor I will tweak <code>SegmentEditorWidget.setup()</code> to set <code>self.editor.setMaximumNumberOfUndoStates(10)</code> to something like 1 or even zero.</p>
<p>This <em>seems</em> to help but I have not done any quantitative comparisons. If it actually <em>does</em> use less memory, would it be useful to have a configurable “Number of undo steps” setting in Segment Editor?</p>
<p>(I’m happy to look into doing this if it would be useful.)</p>

---

## Post #2 by @lassoan (2020-11-25 17:57 UTC)

<p>A copy of each modified segmentation layer (3D volume containing non-overlapping segments) is stored in each undo state. You can check the process memory usage to see if it makes a significant difference for you.</p>
<p>Number of undo states could be exposed somewhere on the GUI (maybe in application settings / segmentations), but this adds a little bit of complication and room for user error (user changing this setting to 0 at some point for testing something and then forget about it and not understanding why undo does not work). So, I would only add this if there is a strong, confirmed need for it.</p>

---

## Post #3 by @hherhold (2020-11-25 17:59 UTC)

<p>Yeah, I only do it for big datasets with complicated segmentations. I think I’ll just continue with tweaking the source when necessary. I can definitely see where someone might change this in a configuration and forget about it, or inherit a config file and get confused.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2020-11-25 18:02 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="14766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I think I’ll just continue with tweaking the source when necessary</p>
</blockquote>
</aside>
<p>You don’t need to tweak the source - you can change the number of undo states by a one-line command.</p>

---

## Post #5 by @hherhold (2020-11-25 18:06 UTC)

<p>DOH! Yes, this is now painfully obvious. (Insert embarrassed emoji here.)</p>
<p>Thanks!!!</p>

---
