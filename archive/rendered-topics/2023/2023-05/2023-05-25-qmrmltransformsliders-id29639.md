# qMRMLTransformSliders

**Topic ID**: 29639
**Date**: 2023-05-25
**URL**: https://discourse.slicer.org/t/qmrmltransformsliders/29639

---

## Post #1 by @Mehran (2023-05-25 08:05 UTC)

<p>Hi all,<br>
I have struggle with  MRMLTransformSliders. since there are 3 sliders inside it, how we can access each slider’s value? Or if it is an attribute to extract transform matrix still is useful.<br>
thanks</p>

---

## Post #2 by @Mehran (2023-05-26 07:30 UTC)

<p>I guess I need to find them in findChildren attribute as:</p>
<p><em>import slicer</em><br>
<em>from qt import QSlider</em></p>
<p><em># Create an instance of qMRMLTransformSliders</em><br>
<em>transformSliders = slicer.qMRMLTransformSliders()</em></p>
<p><em># Find all sliders within the qMRMLTransformSliders widget</em><br>
<em>sliders = transformSliders.findChildren(QSlider)</em></p>
<p><em># Access the translation sliders</em><br>
<em>translationSliders = sliders[0:3]  # Assuming the translation sliders are the first three in the list</em></p>
<p><em># Get the values of the translation sliders</em><br>
<em>lrTranslation = translationSliders[0].value()</em><br>
<em>paTranslation = translationSliders[1].value()</em><br>
<em>isTranslation = translationSliders[2].value()</em></p>

---

## Post #3 by @ungi (2023-05-26 09:59 UTC)

<p>I think it’s a better strategy to observe the transform node. Whenever there is a TransformModifiedEvent evoked by the transform node, you can take the transformation matrix (or vtkTransform) out of the transform node, and obtain the translation and rotation values using VTK.</p>

---

## Post #4 by @Mehran (2023-05-26 12:31 UTC)

<p>Thanks <a class="mention" href="/u/ungi">@ungi</a> do you have any example for that?</p>

---

## Post #5 by @lassoan (2023-05-26 13:25 UTC)

<p>You can find examples in the Slicer script repository for adding observers to nodes. In this case you need to observe the TransformModified event.</p>

---
