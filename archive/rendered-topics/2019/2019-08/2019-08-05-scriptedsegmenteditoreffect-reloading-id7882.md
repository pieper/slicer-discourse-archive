---
topic_id: 7882
title: "Scriptedsegmenteditoreffect Reloading"
date: 2019-08-05
url: https://discourse.slicer.org/t/7882
---

# ScriptedSegmentEditorEffect - reloading?

**Topic ID**: 7882
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/scriptedsegmenteditoreffect-reloading/7882

---

## Post #1 by @hherhold (2019-08-05 15:03 UTC)

<p>I’m working on a new Segment Editor Effect, created using the wizard. When I modify some code and I want to test, clicking the “Reload” button seems to only reload the SegmentEditor module, not the new Editor Effect. Is there a way to have it “traverse the heirarchy” and reload all the effects?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-08-05 15:22 UTC)

<p>Dependencies are quite complex when you register segment editor effects and so we did not implement reload. I usually create a test scene and set up auto-loading at startup using slicerrc.py. Then I simply restart the application when I need to test changes. You can also create automatic test script to speed up test cycles.</p>

---

## Post #3 by @hherhold (2019-08-05 15:38 UTC)

<p>Got it - sounds good. Thanks!</p>

---
