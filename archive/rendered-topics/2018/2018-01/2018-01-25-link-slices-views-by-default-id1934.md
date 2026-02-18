# Link slices views by default?

**Topic ID**: 1934
**Date**: 2018-01-25
**URL**: https://discourse.slicer.org/t/link-slices-views-by-default/1934

---

## Post #1 by @gcsharp (2018-01-25 18:17 UTC)

<p>Every time I load a close a scene or restart slicer, the slice views<br>
become unlinked.  Is there a way to make them linked by default?</p>

---

## Post #2 by @pieper (2018-01-25 21:01 UTC)

<p>You could put something like this in your .slicerrc.py</p>
<pre><code class="lang-auto">for node in getNodesByClass('vtkMRMLSliceCompositeNode'):
  node.SetLinkedControl(1)
</code></pre>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F</a></p>

---

## Post #3 by @lassoan (2018-01-26 15:58 UTC)

<p>In addition to Steve’s code snippet above, to make all <em>new</em> slice viewers linked as well, you can change the default composite node properties like this:</p>
<pre><code>defaultSliceCompositeNode = slicer.vtkMRMLSliceCompositeNode()
defaultSliceCompositeNode.SetLinkedControl(1)
slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
</code></pre>
<p>This code has only effect on latest trunk version, as I’ve just fixed slice composite node creation to use scene’s <a href="http://apidocs.slicer.org/master/classvtkMRMLScene.html#a147b4127ffcbbf0dbc5ed894bd4c92a4">CreateNodeByClass</a> method instead of the node’s New method.</p>

---

## Post #4 by @pieper (2018-01-26 16:23 UTC)

<p>Nice Andras! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>
<p>If this feature is widely useful we could look into adding it as a settings option.</p>

---

## Post #5 by @gcsharp (2018-01-26 19:39 UTC)

<p>Out of sight!   This works great!!</p>

---

## Post #6 by @Fernando (2018-06-20 10:57 UTC)

<p>I think it would be useful to add the option as a setting. I consistently link the slice views as soon as I load an image.</p>

---

## Post #7 by @lassoan (2018-06-20 13:40 UTC)

<p>It would be quite simple to implement this (just need to add it to qSlicerSettingsViewsPanel.cxx and qSlicerSettingsViewsPanel.ui), but since it can be <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default">set using .slicerrc file</a> and not that many people have asked for this, the priority of implementing this is low. I would be happy to help you implementing this if you decide to give it a go.</p>

---

## Post #8 by @Alex_Vergara (2020-08-05 09:21 UTC)

<p>I am having issues with the following code</p>
<pre><code class="lang-auto">def makeSlicerLinkedCompositeNodes():
    # Set linked slice views  in all existing slice composite nodes and in the default node
    sliceCompositeNodes = slicer.util.getNodesByClass(
        "vtkMRMLSliceCompositeNode")
    defaultSliceCompositeNode = slicer.mrmlScene.GetDefaultNodeByClass(
        "vtkMRMLSliceCompositeNode")
    if not defaultSliceCompositeNode:
        defaultSliceCompositeNode = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLSliceCompositeNode")
        slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
    for sliceCompositeNode in sliceCompositeNodes:
        sliceCompositeNode.SetLinkedControl(True)
    defaultSliceCompositeNode.SetLinkedControl(True)


def setSlicerViews(backgroundID, foregroundID):
    if not utils.checkTesting():
        makeSlicerLinkedCompositeNodes()

        slicer.util.setSliceViewerLayers(background=str(
            backgroundID), foreground=str(foregroundID), foregroundOpacity=0.5)

        slicer.app.layoutManager().setLayout(
            slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
        slicer.util.resetSliceViews()
        slicer.app.processEvents()
</code></pre>
<p>It creates extra composite nodes.</p>
<p>Is there a better way to set background and foreground in a forced linked views scheme?</p>

---

## Post #9 by @lassoan (2020-08-05 17:35 UTC)

<p>It is not necessary to add default nodes to the scene, so instead of <code>AddNewNodeByClass</code> you can use <code>CreateNewNodeByClass</code>. See complete example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default</a></p>

---

## Post #10 by @Alex_Vergara (2020-08-06 10:12 UTC)

<p>Thanks, that solved the issue!</p>

---

## Post #11 by @Alex_Vergara (2020-08-11 13:18 UTC)

<p>the example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_all_slice_views_linked_by_default</a><br>
contradicts the memory management in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement</a></p>
<p>it says that after <code>slicer.mrmlScene.GetNodesByClass</code> it must follow an unregister call.</p>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLLinearTransformNode')
nodes.UnRegister(slicer.mrmlScene)  # reference count is increased by both the factory method and the python reference; unregister to keep only the python reference
...
</code></pre>
<p>if I do</p>
<pre><code class="lang-auto">nodes = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")
nodes.UnRegister(slicer.mrmlScene)
</code></pre>
<p>Then Slicer complains as <code>AttributeError: 'list' object has no attribute 'UnRegister'</code></p>
<p>Why does the linked views example works? What is the correct way then?</p>

---

## Post #12 by @lassoan (2020-08-11 13:29 UTC)

<p>One method returns a Python list, the other returns a VTK collection.</p>
<p>For Python scripts, it is simpler to use <code>slicer.util.getNodesByClass</code> because it returns a Python list, which is easier to iterate through and UnRegister has been already called internally.</p>

---
