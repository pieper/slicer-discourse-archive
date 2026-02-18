# Calling module with slicer functions fail in Jupyter notebook

**Topic ID**: 17712
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/calling-module-with-slicer-functions-fail-in-jupyter-notebook/17712

---

## Post #1 by @mc_barbour (2021-05-20 15:50 UTC)

<p>I’m currently using slicer via jupyter. I’ve written a number of functions to help me batch segment 4dct data and I’m attempting to load those functions into my notebook via a module as I’ve got multiple patients to evaluate. When I try to access the functions, however, I get "name ‘slicer’ is not defined.</p>
<p>When the function is defined from within my notebook, it executes without an issue. I’ve checked the python path from within the module functions and it points to all the slicer-python locations.</p>
<p>Is there something special I need to do to import this module which calls numerous slicer executables?</p>
<p>OS: MacOS, 10:15<br>
slicer: 4.11.20201026</p>

---

## Post #2 by @lassoan (2021-05-20 17:07 UTC)

<p>The <code>slicer</code> namespace is only available if you use the Slicer kernel. You can choose the kernel when you create the notebook or later in the notebook’s menu (Kernel → Change kernel).</p>

---

## Post #3 by @mc_barbour (2021-05-20 19:18 UTC)

<p>Right, I do start the notebook with the slicer kernel and the slicer gui launches. I then try to import a module in which I’ve written some functions in that also use the slicer namespace.</p>
<p>The notebook loads the module okay. Since the functions are not explicitly defined within the notebook, but loaded, does it not have access to the slicer namespace? I’ve included a section of the module that I’m trying to load into the notebook which is running the slicer kernel.</p>
<pre><code class="lang-python">import sys
import slicer


def setup_airway_segment_editor(segmentationNode=None, masterVolumeNode=None):
    
"""
Runs standard setup of segment editor widget and segment editor node
"""
    if segmentationNode is None:
    # Create segmentation node
        segmentationNode = slicer.vtkMRMLSegmentationNode()
        slicer.mrmlScene.AddNode(segmentationNode)
        segmentationNode.CreateDefaultDisplayNodes()
    
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    if masterVolumeNode:
        segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
    
    # Add airway segment
    airwaySegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Airway")
    
    # Add mask segment
    maskLabelMap = slicer.util.getNode('maskLabelMap')
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(maskLabelMap, segmentationNode)
    maskSegmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('mask')

    return segmentEditorWidget, segmentEditorNode, segmentationNode, airwaySegmentID, maskSegmentID
</code></pre>

---

## Post #4 by @lassoan (2021-05-20 19:32 UTC)

<p>You can add functions to the <code>global()</code> namespace or <code>slicer</code> namespace (by simply using the <code>=</code> operator). However, normally you would not want to pollute these global namespaces but instead add helper functions to your module’s namespace or into your module logic, which you can import and use from anywhere.</p>
<p>For example, you can reach <code>SampleData</code> module functions logic like this:</p>
<ol>
<li>Run function specified in a module’s namespace:</li>
</ol>
<pre><code class="lang-python">from SampleData import *

downloadSample('MRHead')
</code></pre>
<ol start="2">
<li>Run method specified in a module logic class:</li>
</ol>
<pre><code class="lang-python">import SampleData

logic = SampleData.SampleDataLogic()
logic.downloadCTACardio()
</code></pre>

---
