# error no attribute 'setParameter' when using segment editor in python interactor

**Topic ID**: 27177
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/error-no-attribute-setparameter-when-using-segment-editor-in-python-interactor/27177

---

## Post #1 by @ibowennn (2023-01-10 20:52 UTC)

<p>Hi, I used the segment editor in python interactor for a list of segmentations. However, the codes work for a while and raise Error: ‘NoneType’ object has no attribute ‘setParameter.’<br>
Below is my code:</p>
<pre><code class="lang-auto">dir_roi = '/my/segment/folder'
names = os.listdir(dir_roi)
for name in names:
    path_roi = os.path.join(dir_roi, name)
    path_img = path_roi.replace('roi', 'video_nii')
    path_out = path_roi.replace('roi', 'roi_smooth')
    volumn = slicer.util.loadVolume(path_img)
    seg = slicer.util.loadSegmentation(path_roi)

    seg.CreateClosedSurfaceRepresentation() 
    slicer.util.mainWindow().moduleSelector().selectModule('SegmentEditor')
    segmentEditorWidget = (
        slicer.modules.segmenteditor.widgetRepresentation().self().editor
    )  

    segmentEditorWidget.setActiveEffectByName("Smoothing")  
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "MORPHOLOGICAL_CLOSING")
    effect.setParameter("KernelSizeMm", 12)
    effect.self().onApply()

    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "MORPHOLOGICAL_OPENING")
    effect.setParameter("KernelSizeMm", 12)
    effect.self().onApply()

    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "JOINT_TAUBIN")
    effect.setParameter("JointTaubinSmoothingFactor", 1)
    effect.self().onApply()

    masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass(
        'vtkMRMLScalarVolumeNode'
    )  
    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(
        seg, labelmapVolumeNode, masterVolumeNode
    )
    slicer.util.saveNode(labelmapVolumeNode, path_out)
    slicer.mrmlScene.Clear(0)
</code></pre>
<p>Sometimes “setParameter” works, but most of the time, it fails.<br>
I would appreciate any help. Thanks!</p>

---

## Post #2 by @cpinter (2023-01-11 13:10 UTC)

<p>This is what you need to do for example:<br>
<code>smoothingEffect.scriptedEffect.setParameter('SmoothingMethod', 'MORPHOLOGICAL_OPENING')</code></p>

---
