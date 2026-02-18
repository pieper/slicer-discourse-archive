# Automate setting source volume and geometry in Segment Editor 

**Topic ID**: 31324
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/automate-setting-source-volume-and-geometry-in-segment-editor/31324

---

## Post #1 by @warrj (2023-08-23 22:06 UTC)

<p>Hello,</p>
<p>When I open the segment editor module, I’d like the source volume and geometry to automatically be set to a specific volume which I have loaded into the display view. Is it possible to automate this in my code?</p>
<p>To display the desired node I used :</p>
<pre><code class="lang-python">lm = slicer.app.layoutManager()
redCompositeNode = lm.sliceWidget('Red').mrmlSliceCompositeNode() 
redCompositeNode.SetBackgroundVolumeID(visulization_image_id) 
</code></pre>
<p>Thank you</p>

---

## Post #2 by @jcfr (2023-08-24 04:37 UTC)

<p>You should be able to adapt the following:</p>
<pre><code class="lang-python">mw = slicer.util.mainWindow()
modulePanel = findChild(mw, "ModulePanel")

def onModuleEntered(moduleName):
    if moduleName != "SegmentEditor":
        return
    print(f"Entered {moduleName}")
    # Get reference to the volume loaded a background
    sliceNode = slicer.util.getNode("vtkMRMLSliceNodeRed")
    sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
    sourceVolume = sliceLogic.GetBackgroundLayer().GetVolumeNode()
    
    # Get reference to the vtkMRMLSegmentEditorNode used in the segment editor module
    # This node is storing parameters associated with the segment editor widget (qMRMLSegmentEditorWidget)
    segmentEditorNode = slicer.modules.SegmentEditorWidget.parameterSetNode
    segmentEditorNode.SetAndObserveSourceVolumeNode(sourceVolume)

modulePanel.moduleAdded.connect(onModuleEntered)
</code></pre>
<p>Adding this to the Slicer <code>Application startup file</code> would ensure it always happen.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file</a></p>

---
