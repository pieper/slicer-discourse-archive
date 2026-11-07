---
topic_id: 48726
title: "A Segment Selector SegmentEditorEffect for large segmentations"
date: 2026-11-05
url: https://discourse.slicer.org/t/48726
last_bumped: 2026-11-06T16:57:50.623Z
---

# A Segment Selector SegmentEditorEffect for large segmentations

**Topic ID**: 48726
**Date**: 2026-11-05
**URL**: https://discourse.slicer.org/t/a-segment-selector-segmenteditoreffect-for-large-segmentations/48726

---

## Post #1 by @shai-ikko (2026-11-05 09:33 UTC)

<p>Hi,</p>
<p>We’ve had a need to edit large segmentations, with dozens of segments (sometimes more than a hundred). Selecting segments from the segment list was extremely cumbersome, so we wrote a SegmentEditorEffect which lets user pick segments by clicking on them in the slice views. This raised two questions:</p>
<ol>
<li>
<p>Is it just us, or would others be interested?</p>
</li>
<li>
<p>While doing this, we noted that when a segment is selected, the segment table is not scrolled to make it visible; and to reach the segment table to fix this, we needed to walk through the Qt element tree, which felt “dirty”:</p>
</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">    editorModule = slicer.util.getModule("SegmentEditor")
    self.editor = slicer.util.getModuleGui(editorModule).editor
    resizable = self.editor.findChild(
        ctk.ctkExpandableWidget, "SegmentsTableResizableFrame"
    )
    segTableView = resizable.findChild(
        slicer.qMRMLSegmentsTableView, "SegmentsTableView"
    )
    self.tableView = segTableView.tableWidget()

</code></pre>
<p>Should these be fixed in Slicer itself? That is, would it be accepted if we made the table scroll to selected segment when the selection changes, and/or exposed the table view/widget in a more structured API?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2026-11-06 16:57 UTC)

<aside class="quote no-group" data-username="shai-ikko" data-post="1" data-topic="48726">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<ol>
<li>Is it just us, or would others be interested?</li>
</ol>
</blockquote>
</aside>
<p>I would be.</p>
<aside class="quote no-group" data-username="shai-ikko" data-post="1" data-topic="48726">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<ol start="2">
<li>While doing this, we noted that when a segment is selected, the segment table is not scrolled to make it</li>
</ol>
</blockquote>
</aside>
<p>Yep, that would be great too!</p>

---
