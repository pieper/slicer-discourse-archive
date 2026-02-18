# How to put a volume in a 3D view programmatically?

**Topic ID**: 38163
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/how-to-put-a-volume-in-a-3d-view-programmatically/38163

---

## Post #1 by @shai-ikko (2024-09-02 16:50 UTC)

<p>Hello, I’ve been scratching my head and trying to look through documentation and code samples, and found nothing…</p>
<p>I can use this code (up to typos, edited a little here from live code), based on code found in the CompareVolumes module, to put a volume into a slice view:</p>
<pre data-code-wrap="python"><code class="lang-python">def showVolumeInSlice(volumeNode, viewName, orientation) 
        layoutManager = slicer.app.layoutManager()
        sliceWidget = layoutManager.sliceWidget(viewName)  # Use the view's singletontag
        compositeNode = sliceWidget.mrmlSliceCompositeNode()
        compositeNode.SetBackgroundVolumeID(volumeNode.GetID())
        compositeNode.SetForegroundVolumeID("")
        sliceNode = sliceWidget.mrmlSliceNode()
        sliceNode.SetOrientation(orientation)
</code></pre>
<p>How do I do the equivalent for a 3D view? In CompareVolumes, this was left as a <code>#TODO</code>; none of the relevant classes (<code>vtkMRMLViewNode</code>, <code>qMRMLThreeDView</code>, <code>qMRMLThreeDWidget</code>) seem to carry any methods referring to volume ID. I looked at <code>DisplayManager</code>s, but it didn’t seem to be there either…</p>
<p>Am I going all wrong about it?</p>

---

## Post #2 by @pieper (2024-09-02 22:26 UTC)

<p>Volume rendering in the threeD views is handled differently from the Slice layers.  What you would want to do is create display nodes with <code>vtkSlicerVolumeRenderingLogic::CreateDefaultVolumeRenderingNodes</code> and set the ViewIDs for each of the threeD views where you want them to show up.  If you want more than one volume in a view (i.e. to show overlap or to cross-fade) you can make multiple display nodes per volume and then use the Multi-Volume renderer, which is still marked as experimental as it probably doesn’t handle all the same modes as the normal ones.</p>
<p>It would be great if you could expand the CompareVolumes module to include volume rendering.</p>

---

## Post #3 by @shai-ikko (2024-09-04 17:29 UTC)

<p>Thanks! that was definitely a step in the right direction, but things aren’t quite working the way I want them to.</p>
<p>Some context: I’m trying to write a module where a user can select a volume (using a standard <code>qMRMLNodeComboBox</code>), and then, among other things, that volume gets displayed in a 3D view (and also a slice view). I want the volume to switch if the user changes the selected volume.</p>
<p>My function (called, ultimately, from the selector’s <code>currentNodeChanged(bool)</code> signal) looks like this:</p>
<pre data-code-wrap="python"><code class="lang-python">def showVolumeIn3DView(volumeNode):
    renderingLogic = slicer.modules.volumerendering.logic()
    displayNode = renderingLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
    widget = slicer.app.layoutManager().threeDWidget(0)  # See note below
    displayNode.SetViewNodeIDs([widget.mrmlViewNode().GetID()])
    renderingLogic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>
<p>Before I added the last line (which I found <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering" rel="noopener nofollow ugc">here</a>), the volume that was active before opening my module was shown in the 3D view, and didn’t change at all. With this line, it does change – but only the first time every volume is selected. That is, if Vol1 was active, the module opens showing Vol1. Now,</p>
<ul>
<li>select Vol2 → shows Vol2.</li>
<li>Then, select Vol1 again → still shows Vol2, nothing happens in the 3D view.</li>
</ul>
<p>I’ve tried storing the <code>displayNode</code>, and calling <code>renderingLogic.RemoveVolumeRenderingDisplayNode()</code> on the “old” <code>displayNode</code> before the <code>CreateDefaultVolumeRenderingNodes()</code> for the new volume, thinking that would help reset the display node – but it did nothing. I also tried to do</p>
<pre data-code-wrap="python"><code class="lang-python">    displayNode.SetViewNodeIDs([])
    displayNode.SetViewNodeIDs([widget.mrmlViewNode().GetID()])
</code></pre>
<p>to try to force the display node to “re-install” itself on the view node – again, to no avail. I also tried both together. I have to say, my instinct is still that I’m trying things in a fundamentally misguided way – except, I could find no guide…</p>
<p>While working on this, I think I also found a bug in the view node management. Docs <a href="https://apidocs.slicer.org/v5.2/classqMRMLLayoutManager.html#a810df79c97d1772d995de70b9e4b442d" rel="noopener nofollow ugc">seem to indicate</a> I can pick a 3D-view by name; for slice views, this “name” is the value set in the layout XML by the <code>singletontag</code> attribute. But for 3D views – first, the name gets a funny prefix; but then, the function just doesn’t work at all, always returning <code>None</code>. The singleton tag I used for the 3D view was “1”.</p>
<pre data-code-wrap="pycon"><code class="lang-pycon">&gt;&gt;&gt; lm = slicer.app.layoutManager()
&gt;&gt;&gt; w = lm.threeDWidget(0)
&gt;&gt;&gt; w.name
'ThreeDWidget1'
&gt;&gt;&gt; lm.threeDWidget('ThreeDWidget1')
&gt;&gt;&gt; print(lm.threeDWidget(w.name))
None
</code></pre>
<p>Thanks again – you’ve already been very helpful!</p>

---

## Post #4 by @chir.set (2024-09-04 19:35 UTC)

<aside class="quote no-group" data-username="shai-ikko" data-post="1" data-topic="38163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<p>How do I do the equivalent for a 3D view?</p>
</blockquote>
</aside>
<p>This code may be helpful. I use it daily to switch the current volume rendered in 3D.</p>
<pre><code class="lang-auto">def doVolumeRendering(inputVolume, presetName):
    if inputVolume is None:
        return
    
    # Go to VolumeRendering module.
    mainWindow = slicer.util.mainWindow()
    mainWindow.moduleSelector().selectModule("VolumeRendering")
    
    # Hide current displayed node. N.B - using widgetRepresentation, not logic of VolumeRendering.
    currentDisplayNode=slicer.modules.volumerendering.widgetRepresentation().mrmlDisplayNode()
    if currentDisplayNode is not None:
        currentDisplayNode.SetVisibility(False)
    
    # Change current volume of VolumeRendering module.
    slicer.modules.volumerendering.widgetRepresentation().setMRMLVolumeNode(inputVolume)
    
    # Show 3D of current volume.
    displayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(inputVolume)
    displayNode.SetVisibility(True)
    
    # Apply a preset.
    preset=slicer.modules.volumerendering.logic().GetPresetByName(presetName)
    displayNode.GetVolumePropertyNode().Copy(preset)
</code></pre>

---

## Post #5 by @pieper (2024-09-04 21:02 UTC)

<p><a class="mention" href="/u/shai-ikko">@shai-ikko</a> - I think what <a class="mention" href="/u/chir.set">@chir.set</a> sent looks like it should help you.</p>
<p>If you are still having trouble it would help if you could reduce the issue to a single script that downloads sample data, and implements the volume switching behavior so that anyone could try running it in their own slicer just by pasting into the python console.  This would be helpful because it’s hard to debug code just by looking at snippets.  Also (at least for me) creating such a self-contained example helps me narrow down the issue and sometimes even solve it.</p>

---

## Post #6 by @jamesobutler (2024-09-04 23:39 UTC)

<p>I wonder if it would be valuable to be able to show volume renderings in the 3D viewer from the popup widget view controller similarly to the 2D Slice views being able to select volumes to show from the popup widget slice controller. There is currently different methods for being able to select a volume to show in the 3D view vs 2D view. There is the drag-and-drop method from the Data module which works for propagation to the 2D and 3D view, but there is not a similar thing for click selection. With such a feature then maybe <a class="mention" href="/u/shai-ikko">@shai-ikko</a> wouldn’t have to create a custom qMRMLNodeComboBox to do this propagation.</p>

---

## Post #7 by @shai-ikko (2024-09-12 11:18 UTC)

<p>Hi,</p>
<p>Thanks, all, for your suggestions. I’ve had to go do other things, and it will take some time before I get back to this. I do intend to, but not in the next few weeks.</p>

---
