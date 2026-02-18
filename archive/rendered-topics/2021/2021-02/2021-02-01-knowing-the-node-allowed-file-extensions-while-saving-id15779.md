# Knowing the node allowed file extensions while saving

**Topic ID**: 15779
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/knowing-the-node-allowed-file-extensions-while-saving/15779

---

## Post #1 by @Alex_Vergara (2021-02-01 18:50 UTC)

<p>while using saveNode I need to provide the correct file extension, however I failed to know the node class type to create the proper if sentence.<br>
Example:</p>
<pre><code class="lang-nohighlight">node is vtkMRMLScalarVolumeNode =&gt; filename ends in .nrrd
node is vtkMRMLSegmentationNode =&gt; filename ends in .seg.nrrd
node is vtkMRMLTransformNode    =&gt; filename ends in .h5
</code></pre>
<p>How to achive this?</p>

---

## Post #2 by @lassoan (2021-02-01 19:01 UTC)

<p>Supported file extension also depends on the associated node content (for example, if master representation of a segmentation if closed surface then file extension will be .seg.vtm). You can get the list is usable file type descriptions and file extensions from the storage node:</p>
<pre><code class="lang-python">fileTypes = storageNode.GetSupportedWriteFileTypes()
fileExtensions = vtk.vtkStringArray()
storageNode.GetFileExtensionsFromFileTypes(fileTypes, fileExtensions);
print(fileExtensions.GetValue(0))
</code></pre>

---

## Post #3 by @Alex_Vergara (2021-02-01 19:11 UTC)

<p>So it is as easy as <code>storageNode=node.GetStorageNode()</code> to get the storage Node?</p>

---

## Post #4 by @lassoan (2021-02-01 19:15 UTC)

<p>Yes you can get the storage node from the data node like that. If you are not sure if the data node has a storage node already then call <code>node.AddDefaultStorageNode()</code> before (it is safe to always call it because the method simply does not do anything if the data node has a storage node already).</p>

---

## Post #5 by @Alex_Vergara (2021-02-01 19:17 UTC)

<p>Although this solves my problem, the original question (knowing the node class programatically) I think stills open for another possible cases</p>

---

## Post #6 by @lassoan (2021-02-01 19:26 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="5" data-topic="15779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>the original question (knowing the node class programatically) I think stills open for another possible cases</p>
</blockquote>
</aside>
<p>What is the information that you are still not sure how to get programmatically?</p>

---

## Post #7 by @Alex_Vergara (2021-02-01 19:53 UTC)

<p>given a node obtaing its class (ex vtkMRMLScalarVolumeNode)</p>

---

## Post #8 by @lassoan (2021-02-01 19:55 UTC)

<p>You can get a node’s class name by calling <code>node.GetClassName()</code>.</p>

---
