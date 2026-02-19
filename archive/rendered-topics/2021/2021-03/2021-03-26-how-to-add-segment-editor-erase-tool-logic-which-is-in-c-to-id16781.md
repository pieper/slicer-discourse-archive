---
topic_id: 16781
title: "How To Add Segment Editor Erase Tool Logic Which Is In C To"
date: 2021-03-26
url: https://discourse.slicer.org/t/16781
---

# How to add segment editor erase tool logic which is in C++ to a dummy python tool?

**Topic ID**: 16781
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/how-to-add-segment-editor-erase-tool-logic-which-is-in-c-to-a-dummy-python-tool/16781

---

## Post #1 by @akshay_pillai (2021-03-26 18:19 UTC)

<p>So I was able to create a copy of the smoothing tool in segment editor and name it as “x” (using info from:<a href="https://discourse.slicer.org/t/how-can-i-create-a-copy-of-the-segment-editor-erase-effect-and-rename-it/16499" class="inline-onebox">How can I create a copy of the segment editor erase effect and rename it?</a>), but how can I add C++ functionality of erase into this tool in python? Any help is appreciated. Thanks.</p>

---

## Post #2 by @lassoan (2021-04-14 05:54 UTC)

<p>All you need to do is to modify <code>paintApply</code> to call <code>modifySelectedSegmentByLabelmap</code> with the <code>maskImage</code> (similarlt as it is done in C++ in <code>qSlicerSegmentEditorPaintEffect::paintApply</code>).</p>

---
