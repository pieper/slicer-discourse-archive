# Loading an MRB file

**Topic ID**: 5116
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/loading-an-mrb-file/5116

---

## Post #1 by @smrolfe (2018-12-17 21:53 UTC)

<p>Hello,<br>
I’m trying to load an MRB file into Slicer using the following snippet:</p>
<p>loadedNodes = vtk.vtkCollection()<br>
fileProperties = {}<br>
fileProperties[‘fileName’] = ‘…localData/Slicer/RemoteIO/mCT_mouse.mrb’<br>
success = slicer.app.coreIOManager().loadNodes(‘SceneFile’, fileProperties, loadedNodes)</p>
<p>the MRB file I’m using for testing can be downloaded from: <a href="http://slicermorph.fhl.washington.edu/mCT_mouse.mrb" rel="nofollow noopener">http://slicermorph.fhl.washington.edu/mCT_mouse.mrb</a></p>
<p>When I try this, the files are loaded into slicer, but the nodes are not returned in ‘loadedNodes’.Trying this code with a .nrrd file returns the correct nodes. Is this expected behavior?</p>
<p>Thanks,<br>
Sara</p>

---

## Post #2 by @Sam_Horvath (2018-12-18 13:34 UTC)

<p>Some thoughts:</p>
<p>What is the value of the success variable after attempting the load?  are you specifying the full path when you run the snippet?</p>
<p>Would slicer.util.loadScene work for your application?</p>

---

## Post #3 by @lassoan (2018-12-18 13:53 UTC)

<p>The scene reader does not provide a list of all nodes that are loaded, only a success/fail flag. However, you can easily get the list of loaded nodes by adding an observer to the scene:</p>
<pre><code class="lang-auto">loadedNodes = []

@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(caller, event, calldata):
    loadedNodes.append(calldata)

sceneObservationId = slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)
slicer.util.loadScene('c:/tmp/MyScene.mrb')
slicer.mrmlScene.RemoveObserver(sceneObservationId)

print(loadedNodes)
</code></pre>

---

## Post #4 by @smrolfe (2018-12-19 23:15 UTC)

<p>Thanks <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>. The success variable was ‘True’ and slicer.util.loadScene() does work.</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for clarifying how the scene reader works. I now understand that the Sample Data module was checking for a list of loaded nodes after importing my MRB file because the parameters were not set properly when registering the custom data set.</p>

---
