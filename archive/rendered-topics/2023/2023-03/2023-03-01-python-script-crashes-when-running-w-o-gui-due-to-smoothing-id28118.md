---
topic_id: 28118
title: "Python Script Crashes When Running W O Gui Due To Smoothing"
date: 2023-03-01
url: https://discourse.slicer.org/t/28118
---

# Python script crashes when running w/o GUI due to smoothing effect

**Topic ID**: 28118
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/python-script-crashes-when-running-w-o-gui-due-to-smoothing-effect/28118

---

## Post #1 by @Gholl (2023-03-01 15:13 UTC)

<p>I try to run a python script via the command ./Slicer --no-splash --no-main-window --python-script ‘customScript.py’.</p>
<p>It crashes when executing the following line: <code>segmentEditorWidget.setActiveEffectByName("Smoothing")</code>, however, it works when I remove the flag --no-main-window and also when the same code is run via a Jupyter Notebook.</p>
<p>Is there any way to apply smoothing effect w/o a GUI?</p>
<p>Slicer version: 5.2.2</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-03-01 16:02 UTC)

<p>Presence of a main window is required for most application features. Having a main window is generally useful - it allows quick direc visualization, often used side-by-side with the notebook - but if you don’t want to see it then you can minimize the main window right after the application has started.</p>

---

## Post #3 by @pieper (2023-03-01 18:50 UTC)

<p>If you really don’t want a window to pop up you could also run Slicer in a docker, although that’s a lot of installation overhead compared to just minimizing the window.</p>

---

## Post #4 by @Gholl (2023-03-01 19:42 UTC)

<p>Ok, then I know. Thanks!</p>

---
