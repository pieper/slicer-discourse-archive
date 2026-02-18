# SegmentMesher in Slicer 5.2 and 5.3 fail: Error: 'vtkmodules.vtkFiltersCore.vtkThreshold' object has no attribute 'ThresholdByUpper'

**Topic ID**: 27894
**Date**: 2023-02-18
**URL**: https://discourse.slicer.org/t/segmentmesher-in-slicer-5-2-and-5-3-fail-error-vtkmodules-vtkfilterscore-vtkthreshold-object-has-no-attribute-thresholdbyupper/27894

---

## Post #1 by @Mat (2023-02-18 02:40 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.3<br>
Expected behavior: complete successfully<br>
Actual behavior: fails</p>
<p>I’m trying to create a volume mesh using segmentMesher and it keeps failing:</p>
<p>Generating volumetric mesh…</p>
<p>Error: ‘vtkmodules.vtkFiltersCore.vtkThreshold’ object has no attribute ‘ThresholdByUpper’</p>
<p>Is there something I’m missing out?</p>
<p>Thanks!</p>
<p>Mathieu</p>

---

## Post #2 by @lassoan (2023-02-18 04:50 UTC)

<p>This is due to an incorrect API change in VTK (they removed a very widely used method). The fix should be really simple. I’ll try to get to it within a few days.</p>

---

## Post #3 by @Mat (2023-02-19 21:20 UTC)

<p>Thanks Andras, let me know when it is ready, I’ll give it a try! The goal is to import the geometry in COMSOL software for CFD modelling.</p>
<p>Thanks again!</p>
<p>Mat</p>

---

## Post #4 by @Mat (2023-03-14 01:28 UTC)

<p>Hello Iassoan, I was wondering if you had the chance to look at my issue? Your sure are a busy man with all the requests from users <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>Thanks!</p>
<p>Mathieu</p>

---

## Post #5 by @Shajia_Ali (2025-09-26 14:15 UTC)

<p>This post is quite Old, I am using Slicer 5.8.1 and I have a similar problem <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
AttributeError: ‘vtkmodules.vtkFiltersCore.vtkThreshold’ object has no attribute ‘ThresholdBetween’<br>
Is there a solution for that?<br>
I wanted to split my mesh created by Segmented mesher into two meshes.</p>
<p>Edit: My workaround right now:</p>
<pre data-code-wrap="python"><code class="lang-python">meshNode = getNode('200µm_Wuerfel')
mesh = meshNode.GetMesh()
cellData = mesh.GetCellData()
labelsRange = cellData.GetArray("labels").GetRange()

for labelValue in range(int(labelsRange[0]), int(labelsRange[1]) + 1):
    threshold = vtk.vtkThreshold()
    threshold.SetInputData(mesh)
    threshold.SetInputArrayToProcess(
        0, 0, 0,
        vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS,
        "labels"
    )
    # untere &amp; obere Schwelle gleich setzen
    threshold.SetLowerThreshold(labelValue)
    threshold.SetUpperThreshold(labelValue)
    threshold.SetThresholdFunction(vtk.vtkThreshold.THRESHOLD_BETWEEN)

    threshold.Update()

    if threshold.GetOutput().GetNumberOfPoints() &gt; 0:
        modelNode = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLModelNode",
            f"{meshNode.GetName()}_{labelValue}"
        )
        modelNode.SetAndObserveMesh(threshold.GetOutput())
        modelNode.CreateDefaultDisplayNodes()
</code></pre>

---
