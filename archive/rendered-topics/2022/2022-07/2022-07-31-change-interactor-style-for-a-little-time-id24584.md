# Change interactor style for a little time

**Topic ID**: 24584
**Date**: 2022-07-31
**URL**: https://discourse.slicer.org/t/change-interactor-style-for-a-little-time/24584

---

## Post #1 by @keri (2022-07-31 20:43 UTC)

<p>Hi,</p>
<p>I’m trying to allow <a href="https://kitware.github.io/vtk-examples/site/Cxx/Interaction/RubberBand2D/" rel="noopener nofollow ugc">rubber band 2D</a> to change field of view of a slice node.<br>
Thus I change interactor style for <code>vtkInteractorStyleRubberBand2D</code> for a while and then I need to restore the default <code>vtkMRMLSliceViewInteractorStyle</code>.</p>
<p>The problem is that <code>vtkMRMLSliceViewInteractorStyle</code> is initialized in <a href="https://github.com/Slicer/Slicer/blob/38e026f75f78320a2cb579b5fa96f0917ab4f02c/Libs/MRML/Widgets/qMRMLSliceView.cxx#L154-L178" rel="noopener nofollow ugc">qMRMLSliceViewPrivate</a> as <code>vtkNew&lt;&gt;</code> pointer so the interactor is the owner and gets some displayable managers.<br>
Thus it seems I cannot simply create new instance of that style and pass it to the interactor.</p>
<p>Can’t understand how to restore the default <code>vtkMRMLSliceViewInteractorStyle</code>. Or maybe there are other ways to implement that.</p>

---

## Post #2 by @keri (2022-07-31 22:00 UTC)

<p>Oh completely forgot about <code>vtkWeakPointer&lt;&gt;</code>.<br>
It seems I’m able to store previous interactor style in weak pointer in member variable within diplayable manager.<br>
After changing FOV I can restore it back to the interactor.</p>

---
