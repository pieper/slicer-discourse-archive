# "Volume Information" in "Volumes" module not updated for modified volumes

**Topic ID**: 12856
**Date**: 2020-08-04
**URL**: https://discourse.slicer.org/t/volume-information-in-volumes-module-not-updated-for-modified-volumes/12856

---

## Post #1 by @mikebind (2020-08-04 18:03 UTC)

<p>When I clone a volume node and then modify the array values, the “Volume Information” section shows outdated information and I can’t find a way to get it to update.</p>
<pre><code>volNode = getNode('vtkMRMLScalarVolume1')
newVolNode = slicer.modules.volumes.logic().CloneVolume(slicer.mrmlScene, volNode, 'copiedVolume')
newVolArray = slicer.util.arrayFromVolume(newVolNode)
newVolArray[newVolArray&gt;0] = 0
newVolNode.Modified()
</code></pre>
<p>After this code, the newVolumeNode() has a maximum value of 0, but “Volume Information” still shows it to have a “Scalar Range” up to whatever value the original volNode had.  The actual display of the volume in the slice views shows the modified voxel values, and in all other relevant ways the volume is updated, but there seems to be nothing which updates the “Volume Information”.</p>

---

## Post #2 by @lassoan (2020-08-04 18:19 UTC)

<p>You need to call <code>slicer.util.arrayFromVolumeModified(newVolNode)</code> to indicate that you have finished with your modifications. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume">documentation</a> for details.</p>

---

## Post #3 by @mikebind (2020-08-05 00:29 UTC)

<p>Thanks, I saw the call to volNode.Modified() somewhere, and thought that was all I needed to do to trigger updates. My mistake!  Thanks for your help!</p>

---

## Post #4 by @lassoan (2020-08-05 01:07 UTC)

<p><code>volNode.Modified()</code> only indicates that metadata stored in the volume node’s attributes are changed (but not that pixels are changed).</p>

---

## Post #5 by @rbahegne (2021-01-11 19:11 UTC)

<p>Hello, i kind of have a similar problem but i use C++ and after a long search in the documentation I failed to find the C++ counterpart of <code>slicer.util.arrayFromVolumeModified(newVolNode)</code></p>
<p>Does it really exist ? Or have a different name ?</p>

---

## Post #6 by @pieper (2021-01-11 19:14 UTC)

<p>No, it doesn’t exist.  You can just look at the corresponding python implementation and make the same calls.  Usually it’s just one or two <code>Modified()</code> calls.  Note you only need this if you change the array directly.  If you work with VTK pipelines it’s typically automatic.</p>

---

## Post #7 by @lassoan (2021-01-11 19:24 UTC)

<p>A great side-effect of Slicer (and libraries it uses) being open, along with all documentation, discussion, etc. is that all information is indexed by search engines. So, if you need documentation or source code then you can simply do a web search. For example if you google for <code>arrayFromVolumeModified</code> then for me the second hit in the search result is the <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py">source code</a>.</p>

---

## Post #8 by @rbahegne (2021-01-12 15:25 UTC)

<p>I though that was what i needed, but in fact it is not.</p>
<p>So, i received data via webSocket, created a node, updated his data, displayed it using something like :</p>
<p>selectionNode-&gt;SetActiveVolumeID(node.GetID());<br>
appLogic-&gt;PropagateVolumeSelection();</p>
<p>And i would like that the volume information section update with his data.</p>
<p>So the node is selected (the eye icon is on) but it seems that the update of the volume information section is triggered by highlighting a node in the hierarchy tree. After some research on the vtkMRMLSelectionNode or vtkMRMLSubjectHierarchyNode i couldn’t find what i was looking for.</p>
<p>I also tried something like :</p>
<pre><code>    QString errorMsg;
    qSlicerAbstractCoreModule* volumeModule = qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("Volumes");
    if (!volumeModule)
    {
        errorMsg += "VolumesModule module is not found. ";
        qCritical() &lt;&lt; "VolumesModule module is not found";
        return;
    }
    vtkSlicerVolumesLogic* volumeLogic = vtkSlicerVolumesLogic::SafeDownCast(volumeModule-&gt;logic());
    if (!volumeLogic)
    {
        errorMsg += "VolumesModule logic is not found. ";
        qCritical() &lt;&lt; "VolumesModule logic is not found";
        return;
    }
    volumeLogic-&gt;SetActiveVolumeNode(node);
</code></pre>
<p>But it did’nt have any effect, i miss an update or something ? Any hint ?</p>

---

## Post #9 by @lassoan (2021-01-12 16:51 UTC)

<p>You can change the currently selected node in Volumes module GUI by calling:</p>
<pre><code>slicer.modules.volumes.widgetRepresentation().setEditedNode(volumeNode)
</code></pre>
<p>This feature is used when you right-click on a node and choose “Edit node…”. This API should not be necessary for implementing a custom workflow. Instead, <strong>the recommended way to implement workflows is not to switch between modules at all, just put all the widgets that you need into your own module GUI</strong>.</p>
<p>For example, if you want to show volume information in your module, just add a qMRMLVolumeInfoWidget to your module GUI. You can try this easily from the Python console:</p>
<pre><code class="lang-python">w=slicer.qMRMLVolumeInfoWidget()
w.setMRMLScene(slicer.mrmlScene)
w.setVolumeNode(volumeNode)
w.show()
</code></pre>
<p>All the other parts of the Volumes module are widgets that you can reuse (and customize) in your module. For example, you can show/edit volume display options by adding a <code>slicer.qSlicerScalarVolumeDisplayWidget()</code> to your module GUI. Similarly, all other Slicer core module GUI is assembled from widgets that you can reuse in your own module. There could be some exceptions, where some shortcuts were taken and some parts of a module GUI is not a reusable widget. If you encounter anything like that then you can file a bug report.</p>

---

## Post #10 by @rbahegne (2021-01-13 18:35 UTC)

<pre><code class="lang-auto">slicer.modules.volumes.widgetRepresentation().setEditedNode(volumeNode)
</code></pre>
<p>Did not have any effect, i would like to try the solution you advised :</p>
<pre><code class="lang-auto">w=slicer.qMRMLVolumeInfoWidget()
w.setMRMLScene(slicer.mrmlScene)
w.setVolumeNode(volumeNode)
w.show()
</code></pre>
<p>But i did not manage to get the qMRMLVolumeInfoWidget as i work in C++, i could not find any example of use in the source. How should i access it ?</p>

---

## Post #11 by @lassoan (2021-01-13 18:55 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="10" data-topic="12856">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<pre><code class="lang-auto">slicer.modules.volumes.widgetRepresentation().setEditedNode(volumeNode)
</code></pre>
<p>Did not have any effect</p>
</blockquote>
</aside>
<p>It does what I described above: changes the currently selected node in Volumes module GUI.</p>
<aside class="quote no-group" data-username="rbahegne" data-post="10" data-topic="12856">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>i could not find any example of use in the source</p>
</blockquote>
</aside>
<p>You can use the Volumes module as an example. It displays this widget in its module GUI. The module GUI is designed in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner">Qt Designer</a>, so the best is to view/edit the GUI there.</p>
<p>Developing modules in C++ is for advanced users. It is recommended to first get to know Slicer using Python scripting.</p>

---
