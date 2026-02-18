# How to replace viewer layout with a png image

**Topic ID**: 34120
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/how-to-replace-viewer-layout-with-a-png-image/34120

---

## Post #1 by @tbone (2024-02-02 15:22 UTC)

<p>Hi everyone, I’m new to Slicer and this might be a simple question, but I’ve been trying to change the viewer layout from a Python script so that I can load a simple png image into it. For example, it could just replace the Red view and show the image.</p>
<p>From the other topics I understood that layouts are customizable with <code>slicer.vtkMRMLLayoutNode</code>, and that you can use <code>slicer.mrmlScene.AddNewNodeByClass</code> to add new nodes to it.<br>
But I was having trouble using these methods, so I was uncertain if I was in the right direction of figuring this out.</p>
<p>Would much appreciate help from the experts. Thank you!</p>

---

## Post #2 by @cpinter (2024-02-07 11:58 UTC)

<p>You can load the image as any other volume:</p>
<pre><code class="lang-auto">imageVolumeNode = slicer.util.loadVolume('/path/to/image.png')
</code></pre>
<p>Then something like this to show it in a 2D view:</p>
<pre><code class="lang-auto">redSliceLogic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()
redSliceLogic.GetSliceCompositeNode().SetBackgroundVolumeID(imageVolumeNode.GetID())
redSliceLogic.GetSliceNode().SetOrientationToAxial()
redSliceLogic.SetSliceOffset(0)
redSliceLogic.GetSliceNode().SetSliceVisible(False)
redSliceLogic.FitSliceToAll()        
</code></pre>

---
