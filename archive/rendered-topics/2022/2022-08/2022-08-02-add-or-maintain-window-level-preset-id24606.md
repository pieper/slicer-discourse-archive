---
topic_id: 24606
title: "Add Or Maintain Window Level Preset"
date: 2022-08-02
url: https://discourse.slicer.org/t/24606
---

# Add or maintain window level preset

**Topic ID**: 24606
**Date**: 2022-08-02
**URL**: https://discourse.slicer.org/t/add-or-maintain-window-level-preset/24606

---

## Post #1 by @rhodesdante (2022-08-02 19:29 UTC)

<p>I am trying to create a window/level preset so it pops down on right-click of the slice panes, or make a previous manual preset “sticky”, as described <a href="https://github.com/Project-MONAI/MONAILabel/issues/447" rel="noopener nofollow ugc">here</a>. I would prefer to do the sticky option, because the person for whom I am implementing this is interrogating a lot of volumes back-to-back. However, I’m not really sure where to start with this. I’ve made python modules before, but this seems like I would need to write something in the C++ code for the application, perhaps <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Data/qSlicerDataModuleWidget.cxx" rel="noopener nofollow ugc">here</a>. Are there any tips for how I should go about implementing such a feature? Thanks so much for your support!</p>

---

## Post #2 by @lassoan (2022-08-03 17:48 UTC)

<p>When Slicer loads an image, it uses the window/level that is stored in the image file. If the image is loaded from a research format, which does not store display settings then the window/level is automatically computed from the image content.</p>
<p>You can add or modify window/level presets in this file:</p>
<pre><code>&lt;SlicerHome&gt;\share\Slicer-5.0\qt-loadable-modules\Volumes\VolumeDisplayPresets.json
</code></pre>
<p>You can copy-paste these few lines of of Python code into the Python console if you want to apply a custom window/level preset when a node is loaded:</p>
<pre><code class="lang-python">@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(caller, event, node):
    if isinstance(node, slicer.vtkMRMLScalarVolumeDisplayNode):
        # Call using a timer instead of calling it directly to allow the volume loading to fully complete.
        qt.QTimer.singleShot(0, lambda: setCustomWindowLevel(node))

def setCustomWindowLevel(displayNode):
    displayNode.SetAutoWindowLevel(False)
    displayNode.SetWindowLevel(16, 128)

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)
</code></pre>

---

## Post #3 by @rhodesdante (2022-08-03 18:33 UTC)

<p>Thank you very much!</p>

---
