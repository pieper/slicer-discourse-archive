---
topic_id: 29092
title: "Should We Use More Vtk Object Factory Methods"
date: 2023-04-24
url: https://discourse.slicer.org/t/29092
---

# Should we use more VTK object "factory" methods?

**Topic ID**: 29092
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/should-we-use-more-vtk-object-factory-methods/29092

---

## Post #1 by @lassoan (2023-04-24 14:56 UTC)

<p>We call those methods that create and return a new VTK object “factory method”. Previously, we avoided using such methods because it was too easy to forget to take ownership of the new object (and delete it when no longer used).</p>
<p>However, now the chance of factory method misuse is much lower. 1-2 years ago VTK introduced the <code>VTK_NEWINSTANCE</code> hint that makes ownership transfer automatic when the method is used from Python. Since most beginner Slicer programmers now use Python now, we could expect much less memory leaks.</p>
<p>Using factory methods allow much simpler usage. For example, instead of this:</p>
<pre><code class="lang-python">mesh = vtk.vtkPolyData()
getNode('R').CreateROIBoxPolyDataWorld(mesh)
slicer.modules.models.logic().AddModel(mesh)
</code></pre>
<p>We can use this:</p>
<pre><code class="lang-auto">slicer.modules.models.logic().AddModel( getNode('R').CreateROIBoxPolyDataWorld() )
</code></pre>
<p>It is not just shorter but also much easier to write because the user does not have to know what type of output object need to be instantiated.</p>
<p>We could use factory methods again for most new methods that create a single new VTK object as output. For example, there is a pull request with a new method like this <a href="https://github.com/Slicer/Slicer/pull/6958">here</a>. We may consider adding factory method variants for existing methods, too.</p>
<p><strong>What do you think? Does the much simpler usage in Python justifies the small risk of misusing of factory methods in C++?</strong></p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #2 by @pieper (2023-04-24 17:54 UTC)

<p>I like the idea of a shorter cleaner interface on the python side.  It would be nice for all methods with similar names to behave the same with respect to reference counts.</p>

---

## Post #3 by @jcfr (2023-04-24 18:32 UTC)

<blockquote>
<p>use factory methods again for most new methods that create a single new VTK object as output.</p>
</blockquote>
<p>Agreed.</p>
<blockquote>
<p>We may consider adding factory method variants for existing methods</p>
</blockquote>
<p>Which name were you thinking ?</p>
<p>Instead of introducing new method, I am wondering if we could:</p>
<ul>
<li>toggle the new behavior on a case by case</li>
<li>report a warning if old behavior is being used</li>
</ul>
<p>Before adding such complexity, we should also assess how prevalent the use of factory methods (and associated hack consisting in calling <code>UnRegister</code> is).</p>
<p>References:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#factory-methods">https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#factory-methods</a></li>
<li><a href="https://github.com/Kitware/VTK/blob/master/Documentation/Doxygen/PythonWrappers.md#wrapper-hints-wrapper-hints">https://github.com/Kitware/VTK/blob/master/Documentation/Doxygen/PythonWrappers.md#wrapper-hints-wrapper-hints</a></li>
</ul>

---

## Post #4 by @cpinter (2023-04-24 19:32 UTC)

<p>Great to know! This will make life easier for sure. This decorator should be added to similar functions, starting with the ones in the scene returning vtkCollection. Thanks for bringing this up!</p>

---

## Post #5 by @pieper (2023-04-24 19:36 UTC)

<p>Are we going to be changing the behavior of the existing API with this?  Seems like it could lead to leaks or double frees or who knows what.</p>

---

## Post #6 by @lassoan (2023-04-24 20:20 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="3" data-topic="29092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<blockquote>
<p>We may consider adding factory method variants for existing methods</p>
</blockquote>
<p>Which name were you thinking ?</p>
</blockquote>
</aside>
<p>Adding new method variants should not be difficult.</p>
<p>Current non-factory methods usually start with <code>Get...</code> and take the output object pointer as an argument.</p>
<p>In VTK, a public method is factory method if an only if its name starts with <code>Create...</code>. (There are just a handful of exceptions: <code>New...</code> is used for iterators and <code>Make...</code> for keys, transform, camera, and render window interactor). So, name of any new factory method in VTK classes in Slicer should start with <code>Create...</code>.</p>
<p>Since the old methods names start with <code>Get...</code> and have a different argument list, the method signature will be different, so there would be no backward compatibility issues.</p>
<p>The new method names could be <code>Create...Copy</code> when we want to get an object but it is only feasible to get a copy (because we don’t want to expose an internal object or the object is not stored internally). For example:</p>
<p>Instead of:</p>
<pre><code class="lang-auto">int vtkMRMLTransformNode::GetMatrixTransformToParent(vtkMatrix4x4* matrix)
</code></pre>
<p>we could use:</p>
<pre><code class="lang-auto">VTK_NEWINSTANCE vtkMatrix4x4* vtkMRMLTransformNode::CreateMatrixTransformToParentCopy()
</code></pre>
<p>Instead of:</p>
<pre><code class="lang-auto">bool vtkMRMLSegmentationNode::GetBinaryLabelmapRepresentation(const std::string segmentId, vtkOrientedImageData* outputBinaryLabelmap); 
</code></pre>
<p>we could use:</p>
<pre><code class="lang-auto">VTK_NEWINSTANCE vtkOrientedImageData* vtkMRMLSegmentationNode::CreateBinaryLabelmapRepresentationCopy(const std::string segmentId); 
</code></pre>
<p>A complication is that in Slicer some factory methods don’t start with <code>Create...</code>. For these we could invent a new name and deprecate the old one. However, this can be quite difficult.</p>
<p>For example:</p>
<p>Current non-conform factory method name:</p>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode')
</code></pre>
<p>What would be the factory method name?</p>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.CreateNodeCollectionByClass('vtkMRMLScalarVolumeNode')
nodes = slicer.mrmlScene.CreateNodeListByClass('vtkMRMLScalarVolumeNode')
nodes = slicer.mrmlScene.CreateCollectionOfNodesByClass('vtkMRMLScalarVolumeNode')
...?
</code></pre>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="29092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Are we going to be changing the behavior of the existing API with this?</p>
</blockquote>
</aside>
<p>Yes, ideally we should add this to all current factory methods. The issue is that currently when a factory method is called from Python then <code>Unregister</code> is called, which would crash Slicer after if we simply add the VTK_NEWINSTANCE hint.</p>
<p>Maybe we could do it in phases:</p>
<ol>
<li>Add <code>CreateAndTake...</code> method variant (only expose in Python)</li>
</ol>
<p>For example:</p>
<pre><code class="lang-auto">node = slicer.mrmlScene.CreateAndTakeNodeByClass('vtkMRMLMultiVolumeNode')
</code></pre>
<ol start="2">
<li>Remove Python wrapping from the original <code>Create...</code> method</li>
</ol>
<p>In this phase Python code that is not updated to <code>CreateAndTake...</code> would fail. This should force every maintained extensions to switch to <code>CreateAndTake...</code></p>
<ol start="3">
<li>
<p>Re-enable Python wrapping of <code>Create...</code>, but now with VTK_NEWINSTANCE hint enabled.</p>
</li>
<li>
<p>Remove <code>CreateAndTake...</code> methods</p>
</li>
</ol>
<p>If we don’t want to rush developers then we would need to spend at least 6 months in each phase.</p>

---

## Post #7 by @pieper (2023-04-24 20:38 UTC)

<p>I’m not a fan of changing the behavior of existing methods in such a subtle and possibly dangerous way.  Especially not multiple times over many months.  That would be very hard to maintain since you would have version-specific scripts or scripts that would behave differently on different versions.</p>
<p>I’d much prefer introducing new methods with a clear naming convention to expose the new functionality.  If we think the old way is really dangerous we could deprecate the methods but if they work I would leave them be and not even warn when they are used.</p>
<p>To me, <code>CreateAndTake</code> is a bit clunky but it seems consistent with the meaning and the usage of take in other APIs.  <code>GetNew</code> might make sense, since we are talking about new instances.  This would fit nicely beside the existing <code>Get</code> classes.</p>

---

## Post #8 by @lassoan (2023-04-24 21:06 UTC)

<p>As a maintainer of many extension I hate API changes, too. It is just a time sink, with marginal benefit for existing code. At the same time, for new users it would be nice to avoid having magical <code>Unregister(0)</code> calls. Maybe we could just do step 1 and maybe 2 (and put off step 3 and 4 indefinitely).</p>
<p>For this, we would need alternative method name that could remain in the code long term.</p>
<p><code>CreateAndTake...</code> is meant to be clunky - optimized for ease of search-and-replace, and ugly enough that people are happy to get rid of it when they can.</p>
<p><code>GetNew...</code> sounds quite good. It is very nice in that when the user searches for <code>Get...</code> method names with autocomplete then it shows up there. However, it would complicate the factory method definition: <code>GetNew...</code> would be yet another pattern that C++ users would need to learn to recognize. It may lead to confusing names if used as a drop-in replacement for <code>Get...</code>:</p>
<h3><a name="p-93983-example-1-1" class="anchor" href="#p-93983-example-1-1" aria-label="Heading link"></a>Example 1</h3>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode')
</code></pre>
<p> → </p>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.GetNewNodesByClass('vtkMRMLScalarVolumeNode')
</code></pre>
<p>Quite misleading.</p>
<pre><code class="lang-auto">nodes = slicer.mrmlScene.GetNewCollectionOfNodesByClass('vtkMRMLScalarVolumeNode')
</code></pre>
<p>It is much better.</p>
<h3><a name="p-93983-example-2-2" class="anchor" href="#p-93983-example-2-2" aria-label="Heading link"></a>Example 2</h3>
<pre><code class="lang-auto">matrix = vtk.vtkMatrix4x4()
transformNode.GetMatrixTransformToParent(matrix)
</code></pre>
<p> → </p>
<pre><code class="lang-auto">matrix = transformNode.GetNewMatrixTransformToParent()
</code></pre>
<p>Not very clear.  Maybe OK.</p>
<h3><a name="p-93983-example-3-3" class="anchor" href="#p-93983-example-3-3" aria-label="Heading link"></a>Example 3</h3>
<pre><code class="lang-auto">outputBinaryLabelmap = vtk.vtkOrientedImageData()
segmentationNode.GetBinaryLabelmapRepresentation(segmentId, outputBinaryLabelmap); 
</code></pre>
<p> → </p>
<pre><code class="lang-auto">outputBinaryLabelmap = segmentationNode.GetNewBinaryLabelmapRepresentation(segmentId); 
</code></pre>
<p>This is probably OK as is.</p>
<hr>
<p>Overall <code>GetNew...</code> is not too bad, and in most cases probably better than <code>Create...Copy</code> (because it preserves the <code>Get...</code> prefix), but maybe someone else has even better name suggestion.</p>

---

## Post #9 by @jcfr (2023-04-24 21:12 UTC)

<p>Listed below are the methods that require to use <code>UnRegister</code> when used in Slicer python scripts:</p>
<pre><code class="lang-auto">vtkMRMLScene::GetNodesByClass
vtkMRMLScene::CreateNodeByClass
vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
vtkSlicerSegmentationsModuleLogic::CreateSegmentFromModelNode
vtkSlicerSegmentationsModuleLogic::CreateSegmentFromLabelmapVolumeNode
vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
vtkSlicerCLIModuleLogic::CreateNode
</code></pre>
<p>And to understand the usage context:</p>
<pre><code class="lang-plaintext">$ ack --py UnRegister -B1
Libs/MRML/Core/Documentation/generate_default_color_node_property_table.py
24-nodes = slicer.mrmlScene.GetNodesByClass("vtkMRMLColorNode")
25:nodes.UnRegister(slicer.mrmlScene)

Base/Python/slicer/util.py
1508-    nodes = slicer.mrmlScene.GetNodesByClass(className)
1509:    nodes.UnRegister(slicer.mrmlScene)

Base/Python/slicer/ScriptedLoadableModule.py
291-        node = slicer.mrmlScene.CreateNodeByClass("vtkMRMLScriptedModuleNode")
292:        node.UnRegister(None)  # object is owned by the Python variable now

Modules/Loadable/Segmentations/Testing/Python/SegmentationWidgetsTest1.py
184-        mrOrientedImageData = vtkSlicerSegmentationsModuleLogic.vtkSlicerSegmentationsModuleLogic.CreateOrientedImageDataFromVolumeNode(mrVolumeNode)
185:        mrOrientedImageData.UnRegister(None)

Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py
342-        modelSegment = slicer.vtkSlicerSegmentationsModuleLogic.CreateSegmentFromModelNode(bodyModelNode)
343:        modelSegment.UnRegister(None)  # Need to release ownership
--
371-        labelSegment = slicer.vtkSlicerSegmentationsModuleLogic.CreateSegmentFromLabelmapVolumeNode(allSegmentsLabelmapNode)
372:        labelSegment.UnRegister(None)  # Need to release ownership
--
417-        modelSegmentTranformed = slicer.vtkSlicerSegmentationsModuleLogic.CreateSegmentFromModelNode(bodyModelNodeTransformed, modelTransformedImportSegmentationNode)
418:        modelSegmentTranformed.UnRegister(None)  # Need to release ownership

Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMaskVolumeEffect.py
356-            img = slicer.modules.segmentations.logic().CreateOrientedImageDataFromVolumeNode(maskVolumeNode)
357:            img.UnRegister(None)

Modules/Loadable/SubjectHierarchy/Testing/Python/SubjectHierarchyCorePluginsSelfTest.py
218-        segmentationNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSegmentationNode')
219:        segmentationNodes.UnRegister(None)

Modules/Scripted/DICOMLib/DICOMUtils.py
506-            nodeCollection = slicer.mrmlScene.GetNodesByClass(nodeType)
507:            nodeCollection.UnRegister(None)
--
515-            nodeCollection = slicer.mrmlScene.GetNodesByClass(nodeType)
516:            nodeCollection.UnRegister(None)

Modules/Scripted/ImportItkSnapLabel/ImportItkSnapLabel.py
63-            colorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLColorTableNode")
64:            colorNode.UnRegister(None)  # to prevent memory leaks

Modules/Scripted/DICOMPlugins/DICOMVolumeSequencePlugin.py
46-        browserNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSequenceBrowserNode')
47:        browserNodes.UnRegister(None)
--
64-        # (a reference is still kept by createDicomSeriesParameterNode Python variable).
65:        createDicomSeriesParameterNode.UnRegister(None)

Modules/Scripted/SegmentEditor/SegmentEditor.py
82-            segmentEditorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLSegmentEditorNode")
83:            segmentEditorNode.UnRegister(None)

Applications/SlicerApp/Testing/Python/ScenePerformance.py
258-            newNode = node.CreateNodeInstance()
259:            newNode.UnRegister(node)

Applications/SlicerApp/Testing/Python/MRMLCreateNodeByClassWithSetReferenceCountMinusOne.py
5-    n = slicer.mrmlScene.CreateNodeByClass('vtkMRMLViewNode')
6:    n.UnRegister(None)  # the node object is now owned by n Python variable therefore we can release the reference that CreateNodeByClass added

</code></pre>

---

## Post #10 by @jcfr (2023-04-24 21:20 UTC)

<p>And here are the current Slicer core APIs already using <code>VTK_NEWINSTANCE</code></p>
<pre><code class="lang-plaintext">ack VTK_NEWINSTANCE -A1
Libs/MRML/Core/vtkMRMLMeasurement.h
88:  VTK_NEWINSTANCE
89-  virtual vtkMRMLMeasurement* CreateInstance() const = 0;

Libs/MRML/Core/vtkMRMLStaticMeasurement.h
38:  VTK_NEWINSTANCE
39-  vtkMRMLMeasurement* CreateInstance() const override { return vtkMRMLStaticMeasurement::New(); }

Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.h
86:  VTK_NEWINSTANCE
87-  vtkMRMLMarkupsJsonElement* ReadMarkupsFile(const char* filePath);

Modules/Loadable/Markups/MRML/vtkMRMLMeasurementArea.h
37:  VTK_NEWINSTANCE
38-  vtkMRMLMeasurement* CreateInstance() const override { return vtkMRMLMeasurementArea::New(); }

Modules/Loadable/Markups/MRML/vtkMRMLMeasurementAngle.h
37:  VTK_NEWINSTANCE
38-  vtkMRMLMeasurement* CreateInstance() const override { return vtkMRMLMeasurementAngle::New(); }

Modules/Loadable/Markups/MRML/vtkMRMLMeasurementLength.h
37:  VTK_NEWINSTANCE
38-  vtkMRMLMeasurement* CreateInstance() const override { return vtkMRMLMeasurementLength::New(); }

Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonElement.h
99:  VTK_NEWINSTANCE
100-  vtkCodedEntry* GetCodedEntryProperty(const char* propertyName);
--
105:  VTK_NEWINSTANCE
106-  vtkDoubleArray* GetDoubleArrayProperty(const char* propertyName);
--
115:  VTK_NEWINSTANCE
116-  vtkMRMLMarkupsJsonElement* GetArrayProperty(const char* arrayName);
--
121:  VTK_NEWINSTANCE
122-  vtkMRMLMarkupsJsonElement* GetObjectProperty(const char* objectName);
--
132:  VTK_NEWINSTANCE
133-  vtkMRMLMarkupsJsonElement* GetArrayItem(int childItemIndex);
--
169:  VTK_NEWINSTANCE
170-  vtkMRMLMarkupsJsonElement* ReadFromFile(const char* filePath);

Modules/Loadable/Markups/MRML/vtkMRMLMeasurementVolume.h
37:  VTK_NEWINSTANCE
38-  vtkMRMLMeasurement* CreateInstance() const override { return vtkMRMLMeasurementVolume::New(); }
</code></pre>

---

## Post #11 by @jcfr (2023-04-24 21:28 UTC)

<p>Based on <a class="mention" href="/u/lassoan">@lassoan</a> proposal above, these new methods with the <code>VTK_NEWINSTANCE</code> attribute could be added:</p>
<pre><code class="lang-diff">-vtkMRMLScene::GetNodesByClass
+vtkMRMLScene::GetNewNodeCollectionByClass # Or GetNewCollectionOfNodesByClass
-vtkMRMLScene::CreateNodeByClass
+vtkMRMLScene::GetNewNodeByClass
-vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
+vtkSlicerSegmentationsModuleLogic::GetNewOrientedImageDataFromVolumeNode
-vtkSlicerSegmentationsModuleLogic::CreateSegmentFromModelNode
+vtkSlicerSegmentationsModuleLogic::GetNewSegmentFromModelNode
-vtkSlicerSegmentationsModuleLogic::CreateSegmentFromLabelmapVolumeNode
+vtkSlicerSegmentationsModuleLogic::GetNewSegmentFromLabelmapVolumeNode
-vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
+vtkSlicerSegmentationsModuleLogic::GetNewOrientedImageDataFromVolumeNode
-vtkSlicerCLIModuleLogic::CreateNode
+vtkSlicerCLIModuleLogic::GetNewNode
</code></pre>

---

## Post #12 by @jamesobutler (2023-04-24 21:32 UTC)

<p>I find it a little confusing at first that “GetNew” equals “Create”. The “GetNew” still sounds like you are retrieving an existing object that was recently created.  It is something I could learn, but does not immediately make sense upon first reading it.</p>

---

## Post #13 by @jcfr (2023-04-24 21:36 UTC)

<p><code>CreateNew</code> instead of <code>Create</code> may be more natural then and the word “New” would align with the use of <code>VTK_NEWINSTANCE</code></p>

---

## Post #14 by @lassoan (2023-04-24 22:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="29092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I find it a little confusing at first that “GetNew” equals “Create”.</p>
</blockquote>
</aside>
<p>I agree.</p>
<p><code>GetNew...</code> name is intuitive when I want to get a property of an object but for some reason it is only available as a copy in a new object (e.g., because it is not safe to expose the internal object or the object is constructed on-the-fly).</p>
<p><code>Create...</code> name is intuitive when you actually want to create a new object.</p>
<p>Maybe in addition to <code>vtkMRMLScene::CreateNodeByClass</code> we could add a <code>vtkMRMLScene::CreateNodeByClassOwned</code> method? The <code>...Owned</code> method would only be available in Python and it would use the VTK_NEWINSTANCE hint. The new Python method would start with the same words as the old method, so auto-complete would bring up both (in contrast <code>CreateNew...</code> would not show up together in automcompete along with with <code>CreateNode...</code>). Maybe there could be a better word instead of <code>...Owned</code> (<code>...Auto</code>, <code>...Ref</code>, …?).</p>
<p><code>vtkMRMLMarkupsJsonElement* GetArrayProperty(arrayName)</code> and similar methods in Markups module are very new, we could still change the names without worrying about backward compatibility (only affects a few extensions that use pluggable markups). We could use <code>GetNewArrayFromProperty(arrayName)</code> here.</p>

---

## Post #15 by @jcfr (2023-04-24 22:45 UTC)

<p>Instead of <code>Owned/Auto/Ref</code>, what about the <code>Instance</code> suffix, this would be needed only for the &lt; 10 methods:</p>
<pre><code class="lang-diff">-vtkMRMLScene::CreateNodeByClass
+vtkMRMLScene::CreateNodeInstanceByClass
-vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
+vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataInstanceFromVolumeNode
-vtkSlicerSegmentationsModuleLogic::CreateSegmentFromModelNode
+vtkSlicerSegmentationsModuleLogic::CreateSegmentInstanceFromModelNode
-vtkSlicerSegmentationsModuleLogic::CreateSegmentFromLabelmapVolumeNode
+vtkSlicerSegmentationsModuleLogic::CreateSegmentInstanceFromLabelmapVolumeNode
-vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode
+vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataInstanceFromVolumeNode
-vtkSlicerCLIModuleLogic::CreateNode
+vtkSlicerCLIModuleLogic::CreateNodeInstance
</code></pre>
<p>and for the widely used <code>GetNodesByClass</code> (<code>Nodes</code> → <code>NodeCollection</code>)</p>
<pre><code class="lang-diff">-vtkMRMLScene::GetNodesByClass
+vtkMRMLScene::GetNodeCollectionByClass
</code></pre>

---

## Post #16 by @lassoan (2023-04-25 18:21 UTC)

<p>We discussed this further at the weekly meeting and concluded that we will not change the current API in an incompatible way but add new variants with proper Python decoration.</p>
<p>For existing <code>Create...</code> method names (such as <code>CreateOrientedImageDataFromVolumeNode</code>) we will add a new Python variant with the <code>...Safe</code> suffix to indicate that it is memory-safe (no leak or invalid reference).</p>
<p>I’ll follow up with pull requests.</p>

---
