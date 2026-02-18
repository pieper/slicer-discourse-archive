# Change axis labels of slice view and 3D view

**Topic ID**: 19608
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/change-axis-labels-of-slice-view-and-3d-view/19608

---

## Post #1 by @keri (2021-09-10 15:15 UTC)

<p>Hi,</p>
<p>I’m trying to rename axis labels from medical <code>I, P, A etc </code> to <code>XYZ</code>. I’ve tried to do that in <code>qMyAppMainWindow</code>:</p>
<pre><code class="lang-cpp">  std::vector&lt;std::string&gt; axesNames({"-X", "X", "-Y", "Y", "-Z", "Z"});

  for (int j = 0; j &lt; this-&gt;LayoutManager-&gt;threeDViewCount(); j++)
    for (int i = 0; i &lt; axesNames.size(); i++)
      this-&gt;LayoutManager-&gt;threeDWidget(j)-&gt;mrmlViewNode()-&gt;SetAxisLabel(
          i, axesNames[i].c_str());

  for (const QString&amp; sliceViewName : this-&gt;LayoutManager-&gt;sliceViewNames())
    for (int i = 0; i &lt; axesNames.size(); i++)
      this-&gt;LayoutManager-&gt;sliceWidget(sliceViewName)
          -&gt;mrmlSliceNode()
          -&gt;SetAxisLabel(i, axesNames[i].c_str());
</code></pre>
<p>and in my custom module but apparently after I have set labels some other module reset it to default values by calling <code>vtkMRMLAbstractViewNode::CopyContent()</code></p>
<p>I think I need to make a decision either to put the code above to <code>vtkSlicerModuleLogic::OnMRMLSceneNodeAdded(...)</code> of my module or to control the module loading order (though I don’t know how to do that yet).</p>
<p>In <code>vtkSlicerModuleLogic::OnMRMLSceneNodeAdded(vtkMRMLNode* node)</code> I process the newly added <code>node</code> and  if it is a slice or 3D view then I change its labels. But I think that changing labels of already existind nodes every time new node is added is not the best way.</p>
<p>Probably someone has a better solution?</p>

---

## Post #2 by @lassoan (2021-09-10 23:57 UTC)

<p>Probably you also need to change the axes names in the default view node, similarly to how it is done <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-slice-view-orientation">here</a>.</p>

---

## Post #3 by @keri (2021-09-11 01:05 UTC)

<p>Thank you for the useful info!</p>

---

## Post #4 by @keri (2021-09-11 01:37 UTC)

<p>I have found that disabling <code>DataProbe</code> module (<code> --disable-modules DataProbe</code>) solves my problem with resetting axes labels.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> in the link you gave there is a comment:<br>
<strong># Replace orientation presets in all existing slice nodes and in the default slice node</strong></p>
<p>It is the second time I encounter <strong>default node</strong> and I can’t understand what it is and what it is aimed to? Especially why <strong>default</strong> nodes are some kind of a separate nodes as in the example we append them to the list:</p>
<pre><code class="lang-python">sliceNodes = slicer.util.getNodesByClass("vtkMRMLSliceNode")
sliceNodes.append(slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLSliceNode"))
</code></pre>
<p>Thus <code>slicer.util.getNodesByClass("vtkMRMLSliceNode")</code> doesn’t include defaul nodes…</p>

---

## Post #5 by @lassoan (2021-09-11 01:53 UTC)

<p>The MRML scene can store an instance of each MRML class, the <em>default node</em>. When you create a new node or reset a node then the default node will be used to set its properties. See some more information in the <a href="http://apidocs.slicer.org/master/classvtkMRMLScene.html#ae302c5ed4aabb2910bc35dcc9aa2513f">API documentation</a>.</p>

---

## Post #6 by @keri (2021-09-11 02:05 UTC)

<p>As I understood the default node serves as some kind of a template and the scene may create new nodes of that class with the properties set from that template?</p>
<p>One more thing:<br>
let’s suppose that slicer was launched with the dault layout (single 3D view and three slices). Will that default <code>vtkMRMLSliceNode</code> be one of that three slices or it will be the forth slice node and it is hidden?</p>

---

## Post #7 by @lassoan (2021-09-11 03:24 UTC)

<p>The default slice node is used to initialize all slice nodes. The values are also used when the nodes are reset (e.g., when the scene is closed).</p>

---
