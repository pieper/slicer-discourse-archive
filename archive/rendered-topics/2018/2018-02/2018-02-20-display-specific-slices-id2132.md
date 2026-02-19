---
topic_id: 2132
title: "Display Specific Slices"
date: 2018-02-20
url: https://discourse.slicer.org/t/2132
---

# Display specific slices

**Topic ID**: 2132
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/display-specific-slices/2132

---

## Post #1 by @brhoom (2018-02-20 20:56 UTC)

<p>Dear all,</p>
<p>I am trying to display a specific location (providing the world coordinates in self.CPos )I tried this code but I keep getting slicer default:</p>
<pre><code>    # The volumes are added to the Red (axial) slice of the scene.
    red_logic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()
    red_cn    = red_logic.GetSliceCompositeNode()
    red_cn.SetBackgroundVolumeID(inputNode.GetID())
    red_cn.SetLabelVolumeID(resultNode.GetID())
    red_logic.SetSliceOffset(self.CPos[2])

    # The volumes are added to the Yellow (sagittal) slice of the scene.
    yellow_logic = slicer.app.layoutManager().sliceWidget("Yellow").sliceLogic()
    yellow_cn = yellow_logic.GetSliceCompositeNode()
    yellow_cn.SetBackgroundVolumeID(inputNode.GetID())
    yellow_cn.SetLabelVolumeID(resultNode.GetID())
    yellow_logic.SetSliceOffset(self.CPos[1])

    # The volumes are added to the Green (coronal) slice of the scene.
    green_logic = slicer.app.layoutManager().sliceWidget("Green").sliceLogic()
    green_cn = green_logic.GetSliceCompositeNode()
    green_cn.SetBackgroundVolumeID(inputNode.GetID())
    green_cn.SetLabelVolumeID(resultNode.GetID())
    green_logic.SetSliceOffset(self.CPos[0])

    # The layout is set to show only the Red slice by default.
    lm = slicer.app.layoutManager()
    lm.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)

    # Fit slices to window
    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
    layoutManager = slicer.app.layoutManager()
    for sliceNode in sliceNodes.values():
        sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
        if sliceWidget:
            sliceWidget.sliceLogic().FitSliceToAll() 
</code></pre>
<p>so if I commented out the lines contains SetSliceOffset or use them I get the same default result. I tried the function in slicer python interactor and it works. I tried replacing the variable self.Cpos with the actual values but nothing change.</p>
<p>Am I missing something?</p>
<p>Thanks<br>
Ibraheem</p>

---

## Post #2 by @brhoom (2018-02-21 10:32 UTC)

<p>I figured out that I loaded some images after this code which remove its effect. The code works now.</p>

---
