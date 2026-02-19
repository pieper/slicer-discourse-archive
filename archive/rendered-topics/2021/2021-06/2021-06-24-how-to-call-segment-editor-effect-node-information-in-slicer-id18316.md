---
topic_id: 18316
title: "How To Call Segment Editor Effect Node Information In Slicer"
date: 2021-06-24
url: https://discourse.slicer.org/t/18316
---

# How to call segment editor effect node information in slicer main window

**Topic ID**: 18316
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/how-to-call-segment-editor-effect-node-information-in-slicer-main-window/18316

---

## Post #1 by @qiqi5210 (2021-06-24 09:23 UTC)

<p>Hello, I’d like to write a qdockwidget in qslicermainwindow and make it superimposed with the paneldockwidget as a tab. If I want to put the effect of qmrml segment editor widget in the qdockwidget, how can I operate？</p>

---

## Post #2 by @lassoan (2021-06-25 18:25 UTC)

<p>This should be no problem at all. You can add the segment editor widget (<code>slicer.qMRMLSegmentEditorWidget()</code>) to a layout as any other Qt widgets.</p>
<p>We do something like what you describe in the <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/Guidelet/GuideletLib/Guidelet.py#L57-L96">guidelets user interface</a>, but it is all just standard Qt, so you can find answers by searching the web and Qt forums.</p>

---

## Post #3 by @qiqi5210 (2021-06-26 09:11 UTC)

<p>Thank you very much for your reply. I can solve my problem. Thank you again.</p>

---
