# updateParameterNodeFromGUI not called when ui is updated because connect() don't work

**Topic ID**: 29778
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/updateparameternodefromgui-not-called-when-ui-is-updated-because-connect-dont-work/29778

---

## Post #1 by @tux (2023-06-01 17:45 UTC)

<p>hi,</p>
<p>I want to create a python module for slicer and i got a problem with the UI.<br>
When the UI is updated it doesn’t call the updateParameterNodeFromGUI() function and i think it’s because the widget i use isn’t supported by the slicer library.<br>
I’ve got the line :</p>
<p>self.ui.thresholdFloatInput.connect(“currentNodeChanged(vtkMRMLNode*)”, self.updateParameterNodeFromGUI)</p>
<p>but there’s this error that show up every time :</p>
<p>PythonQt: QObject::connect() signal ‘currentNodeChanged(vtkMRMLNode*)’ does not exist on qMRMLSpinBox</p>
<p>I already tried to use different widget (from Qt designer, ctkVTK, ctk and qMRML) but none of them worked.<br>
I would greatly appreciate any help on what i should use or what i’m misunderstanding here.<br>
Thanks !</p>

---

## Post #2 by @Sunderlandkyl (2023-06-01 17:52 UTC)

<p>For qMRMLSpinBox, you will want to use the “valueChanged(double)” signal.</p>

---

## Post #3 by @tux (2023-06-02 07:05 UTC)

<p>It worked perfectly, thank you very much !<br>
Do you know where i can get the assigned signal of every widget please ?</p>

---

## Post #4 by @Sunderlandkyl (2023-06-02 14:23 UTC)

<p>The API documentation for Slicer is a good place to start for MRML widgets: <a href="https://apidocs.slicer.org/main/classqMRMLSpinBox.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: qMRMLSpinBox Class Reference</a>.</p>
<p>In this case however, despite valueChanged being inherited from ctkDoubleSpinBox it is not documented in in the <a href="https://apidocs.slicer.org/main/classqMRMLSpinBox-members.html" rel="noopener nofollow ugc">member list</a>.</p>
<p>For CTK widgets I would check the <a href="http://www.commontk.org/docs/html/classes.html" rel="noopener nofollow ugc">CTK API documentation</a>, though it appears to be down right now.<br>
For Qt widgets I would check the <a href="https://doc.qt.io/qt-5.15/classes.html" rel="noopener nofollow ugc">Qt API documentation</a>.</p>

---

## Post #5 by @tux (2023-06-02 15:18 UTC)

<p>I already saw the documentation for MRML widget but i never learned c++ so i was a bit lost and i couldn’t find the signaled associated with the widget, but thank you for the other link !</p>

---
