---
topic_id: 16711
title: "How Do I Use Python To Call A Transform Module To Another Mo"
date: 2021-03-23
url: https://discourse.slicer.org/t/16711
---

# How do I use Python to call a Transform module to another module

**Topic ID**: 16711
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/how-do-i-use-python-to-call-a-transform-module-to-another-module/16711

---

## Post #1 by @Carl098 (2021-03-23 08:05 UTC)

<p>self.transformsLogic = slicer.modules.transforms.logic()<br>
self.transformsModuleWidget = PythonQt.qSlicerTransformsModuleWidgets.qSlicerTransformsModuleWidget()<br>
editWidget = slicer.util.findChild(self.transformsModuleWidget, ‘DisplayEditCollapsibleWidget’)<br>
vrGroupBoxLayout.addRow(editWidget)</p>

---

## Post #3 by @Carl098 (2021-03-23 08:07 UTC)

<p>Sorry, I am a beginner, I’d like to know how to write the correct code. Thanks!</p>

---

## Post #4 by @lassoan (2021-03-23 12:14 UTC)

<p>In general, you are not supposed to modify any other module’s GUI, but you can interact with another module using MRML and module logic classes and you can put into your module GUI Qt widgets that other modules provide. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">tutorials</a>.</p>
<p>If you describe what you want to achieve then we can give more specific advice.</p>

---
