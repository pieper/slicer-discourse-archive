# Is there a python api for void qSlicerReformatModuleWidgetPrivate:: resetSlider(qMRMLLinearTransformSlider* slider)?

**Topic ID**: 33338
**Date**: 2023-12-11
**URL**: https://discourse.slicer.org/t/is-there-a-python-api-for-void-qslicerreformatmodulewidgetprivate-resetslider-qmrmllineartransformslider-slider/33338

---

## Post #1 by @derekcbr (2023-12-11 13:27 UTC)

<p>BreadcrumbsSlicer/Modules/Loadable/Reformat<br>
/qSlicerReformatModuleWidget.cxx<br>
Is it possible to call resetSlider method?<br>
reformatLogic = slicer.modules.reformat.logic()<br>
reformatLogic.RotateSlice(sliceNode, 0, rotateX)<br>
reformatLogic.RotateSlice(sliceNode, 1, rotateZ)<br>
reformatLogic.RotateSlice(sliceNode, 2, rotateY)<br>
Cause when I change the above rotation, the result will be wrong if not calling resetSlider.<br>
Thanks!</p>

---

## Post #2 by @RafaelPalomar (2023-12-11 14:55 UTC)

<p><a class="mention" href="/u/derekcbr">@derekcbr</a>, what is the effect that you consider wrong?  Is it that the GUI is not updated accordingly?</p>

---

## Post #3 by @derekcbr (2023-12-12 01:05 UTC)

<p>Is it possible to use python to update sliders in GUI? qSlicerReformatModuleWidget</p>

---

## Post #4 by @RafaelPalomar (2023-12-14 09:51 UTC)

<p><a class="mention" href="/u/derekcbr">@derekcbr</a>, I’m understanding that your question is due to a mismatch between the reslice rotations you try to implement in python and the UI of the <code>reformat module</code>. Based on that:</p>
<ul>
<li>
<p>The <code>reformat module</code> is a loadable module where UI, data model and logic are tightly integrated. Modifications on the data model (e.g., MRML nodes) should be correctly reflected in the UI and vice-versa; logic typically modifies the data model, which in turn, should correctly update the values in the UI.</p>
</li>
<li>
<p>You should not need to adjust the UI to reflect changes you produce by changing MRML nodes or invoking public logic functions. This could be a bug int he <code>reformat module</code>. Do you have data + python snippet to reproduce the issue. Maybe it is something that should be reported and fixed</p>
</li>
</ul>

---
