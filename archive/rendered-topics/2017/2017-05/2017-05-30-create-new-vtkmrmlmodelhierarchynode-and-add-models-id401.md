# Create new vtkMRMLModelHierarchyNode() and add models

**Topic ID**: 401
**Date**: 2017-05-30
**URL**: https://discourse.slicer.org/t/create-new-vtkmrmlmodelhierarchynode-and-add-models/401

---

## Post #1 by @Fernando (2017-05-30 12:37 UTC)

<p>Hi slicers,</p>
<p>This is a simple question:<br>
I have a <code>modelNodeA</code> and <code>modelNodeB</code>.<br>
Using Python, I would like to create a <code>modelHierarchyNode</code> and add my two model nodes inside. Can you please give me a hint?</p>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @cpinter (2017-05-30 13:09 UTC)

<p>Hi Fernando,</p>
<p>This is how I do it in C++:</p>
<pre><code>  vtkSmartPointer&lt;vtkMRMLModelHierarchyNode&gt; rootModelHierarchyNode = vtkSmartPointer&lt;vtkMRMLModelHierarchyNode&gt;::New();
  scene-&gt;AddNode(rootModelHierarchyNode);
  rootModelHierarchyNode-&gt;SetName(rootModelHierarchyNodeName.c_str());
  rootModelHierarchyNode-&gt;SetSingletonTag(rootModelHierarchyNodeName.c_str());

  if (!rootModelHierarchyNode-&gt;GetDisplayNode())
  {
    vtkSmartPointer&lt;vtkMRMLModelDisplayNode&gt; rootModelHierarchyDisplayNode = vtkSmartPointer&lt;vtkMRMLModelDisplayNode&gt;::New();
    scene-&gt;AddNode(rootModelHierarchyDisplayNode);
    rootModelHierarchyNode-&gt;SetAndObserveDisplayNodeID( rootModelHierarchyDisplayNode-&gt;GetID() );
  }

...

  vtkSmartPointer&lt;vtkMRMLModelHierarchyNode&gt; collimatorModelHierarchyNode = vtkSmartPointer&lt;vtkMRMLModelHierarchyNode&gt;::New();
  scene-&gt;AddNode(collimatorModelHierarchyNode);
  collimatorModelHierarchyNode-&gt;SetModelNodeID(collimatorModelNode-&gt;GetID());
  collimatorModelHierarchyNode-&gt;SetParentNodeID(rootModelHierarchyNode-&gt;GetID());
  collimatorModelHierarchyNode-&gt;HideFromEditorsOn();</code></pre>

---

## Post #3 by @lassoan (2017-05-30 13:36 UTC)

<p>Are you sure you want to build model hierarchy? What is your use case? You may be better off using subject hierarchy instead, as subject hierarchy is:</p>
<ul>
<li>more robust: model hierarchy tree widget has some issues, for example sometimes items randomly change place within a branch</li>
<li>has much simpler <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html">API</a>
</li>
<li>has more features: you can define custom actions, you can save the order of nodes in the hierarchy into the scene, and you can group all kinds of related nodes in a branch, not just models</li>
<li>much faster</li>
</ul>
<p>For example, to create a branch and put a node in it:</p>
<pre><code>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
newParentFolderItem = shNode.CreateFolderItem(shNode.GetSceneItemID(), "my folder")
volumeItem = shNode.GetItemByDataNode(getNode('MRHead'))
shNode.SetItemParent(volumeItem, newParentFolderItem)</code></pre>

---

## Post #4 by @Fernando (2017-05-30 13:56 UTC)

<p>Hi Csaba and Andras,</p>
<p>Thanks for your quick answers.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> My Python version:</p>
<pre><code>modelNodeA = getNode('4648J_xscp_model')
modelNodeB = getNode('4648J_RH_lq_model')

rootModelHierarchyNodeName = 'My hierarchy'

rootModelHierarchyNode = slicer.vtkMRMLModelHierarchyNode()
slicer.mrmlScene.AddNode(rootModelHierarchyNode)
rootModelHierarchyNode.SetName(rootModelHierarchyNodeName)
rootModelHierarchyNode.SetSingletonTag(rootModelHierarchyNodeName)  # Not sure what this is

rootModelHierarchyDisplayNode = slicer.vtkMRMLModelDisplayNode()
slicer.mrmlScene.AddNode(rootModelHierarchyDisplayNode)
rootModelHierarchyNode.SetAndObserveDisplayNodeID(rootModelHierarchyDisplayNode.GetID())

modelAHierarchyNode = slicer.vtkMRMLModelHierarchyNode()
slicer.mrmlScene.AddNode(modelAHierarchyNode)
modelAHierarchyNode.SetModelNodeID(modelNodeA.GetID())
modelAHierarchyNode.SetParentNodeID(rootModelHierarchyNode.GetID())
modelAHierarchyNode.HideFromEditorsOn()  # Not sure what this is

modelBHierarchyNode = slicer.vtkMRMLModelHierarchyNode()
slicer.mrmlScene.AddNode(modelBHierarchyNode)
modelBHierarchyNode.SetModelNodeID(modelNodeB.GetID())
modelBHierarchyNode.SetParentNodeID(rootModelHierarchyNode.GetID())
modelBHierarchyNode.HideFromEditorsOn()
</code></pre>
<p>What I expect:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/f6c300e3271fdd7eb639b1aa6e3c3efaaa40cd30.png" width="580" height="59"></p>
<p>What I get:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/9e16a3df2ced1bef623fe33862cee8884d592faa.png" width="580" height="86"></p>
<p>I had already tried with some code I found (probably yours), and got similar results.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I have a lot of models and I want to divide them in groups so that the user can easily change their display properties, using Slicer default modules if possible. I know there are some <a href="http://na-mic.org/Mantis/view.php?id=4249" rel="noopener nofollow ugc">issues</a> though…<br>
I have never taken the time to look into subject hierarchy. It does looks simpler. Running your snippet makes a folder, from which I cannot modify the children display properties (at least I don’t know how to do it).</p>

---

## Post #5 by @cpinter (2017-05-30 14:23 UTC)

<p><code>modelAHierarchyNode.HideFromEditorsOn() # Not sure what this is</code></p>
<p>This call is supposed to make the leaf hierarchy nodes disappear from the tree (to get from what you get to what you expect). Not sure why it doesn’t work, try SetHideFromEditors(1)</p>

---

## Post #6 by @Fernando (2017-05-30 14:59 UTC)

<p><code>SetHideFromEditors(1)</code> worked as expected. I tried to dive into the code to solve the issue I commented before, but I didn’t manage. Do you think it’s hard to fix?</p>
<p>Thank you again</p>

---

## Post #7 by @cpinter (2017-05-30 16:20 UTC)

<p>You mean the slice intersection issue you linked?</p>
<p>I quickly took a look, and it seems that the checkbox in the Models module that applies color/opacity on the branch drives the vtkMRMLDisplayableHierarchyNode::Expanded flag, which is handled by the 3D displayable manager in vtkMRMLModelDisplayableManager::SetModelDisplayProperty, when getting the hierarchy display node (line 1488: vtkMRMLDisplayNode *hierarchyDisplayNode = this-&gt;GetHierarchyDisplayNode(model) ). This call is responsible for getting the right properties. The 2D displayable manager (vtkMRMLModelSliceDisplayableManager) does not use this, and this is what needs to be fixed.</p>
<p>I don’t have time to fix it, but I hope this will help. I’m adding this info on Mantis as well.</p>

---

## Post #8 by @Fernando (2017-05-30 17:43 UTC)

<p>Yes that’s what I meant. Thank you!</p>

---

## Post #9 by @brhoom (2020-05-14 19:25 UTC)

<p>I created two model trees using this approach. I can access each tree and its children names. How can I get a model node from a specific child? e.g. to get their display node, polydata , …etc</p>
<pre><code>  self.shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
  self.modelTreeID = self.shNode.GetItemChildWithName(self.shNode.GetSceneItemID(), "modelTreeName" ) 
  self.modelTreeChildrenIDs = vtk.vtkIdList()
  self.shNode.GetItemChildren(self.modelTreeID, self.modelTreeChildrenIDs)
  for i in xrange(self.modelTreeChildrenIDs GetNumberOfIds()):
      print("modelChildID   : ", self.modelTreeChildrenIDs.GetId(i)) 
      print("modelChildName : ", self.shNode.GetItemName(self.modelTreeChildrenIDs.GetId(i)))</code></pre>

---

## Post #10 by @lassoan (2020-05-15 01:41 UTC)

<p>Model hierarchy is replaced by the much more generic subject hierarchy in recent Slicer versions. It should be easier to use and has many more capabilities. <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy">Script repository</a> contains examples to most common tasks.</p>

---

## Post #11 by @brhoom (2020-05-15 07:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for your quick reply.</p>
<blockquote>
<p>Model hierarchy is replaced by the much more generic subject hierarchy</p>
</blockquote>
<p>I am using  subject hierarchy, kindly see the code above.</p>
<blockquote>
<p>. <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy" rel="noopener nofollow ugc">Script repository</a> contains examples to most common tasks.</p>
</blockquote>
<p>I already checked that. It is not clear to me how to get a “model node” from a child. I can get the child ID e.g. modelTreeChildrenIDs.GetId(i) or the chile name e.g. shNode.GetItemName(self.modelTreeChildrenIDs.GetId(i)) but not the model node.</p>

---

## Post #12 by @cpinter (2020-05-15 08:35 UTC)

<p>You can get the model node using this function<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.h#L115" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.h#L115" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.h#L115</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="105" style="counter-reset: li-counter 104 ;">
<li>
</li><li>// Get/Set methods</li>
<li>public:</li>
<li>  /// Get the (practically) singleton subject hierarchy node from MRML scene.</li>
<li>  /// Merges subject hierarchy nodes if multiple found, and returns the merged one.</li>
<li>  static vtkMRMLSubjectHierarchyNode* GetSubjectHierarchyNode(vtkMRMLScene* scene);</li>
<li>
</li><li>  /// Get ID of root subject hierarchy item (which can be interpreted as the scene in terms of hierarchy)</li>
<li>  vtkIdType GetSceneItemID();</li>
<li>  /// Get data node for a subject hierarchy item</li>
<li class="selected">  vtkMRMLNode* GetItemDataNode(vtkIdType itemID);</li>
<li>  /// Set name for a subject hierarchy item</li>
<li>  void SetItemName(vtkIdType itemID, std::string name);</li>
<li>  /// Get name for a subject hierarchy item</li>
<li>  /// \return Name of the associated data node if any, otherwise the name of the item</li>
<li>  std::string GetItemName(vtkIdType itemID);</li>
<li>  /// Convenience function to set level attribute for a subject hierarchy item</li>
<li>  void SetItemLevel(vtkIdType itemID, std::string level);</li>
<li>  /// Convenience function to get level attribute for a subject hierarchy item</li>
<li>  std::string GetItemLevel(vtkIdType itemID);</li>
<li>  /// Set owner plugin name (role) for a subject hierarchy item</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @brhoom (2020-05-15 10:23 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks a lot , this works, Here is the complete code I used:</p>
<pre><code>self.shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
self.modelTreeID = self.shNode.GetItemChildWithName(self.shNode.GetSceneItemID(), "modelTreeName" ) 
self.modelTreeChildrenIDs = vtk.vtkIdList()
self.shNode.GetItemChildren(self.modelTreeID, self.modelTreeChildrenIDs)
for i in xrange(self.modelTreeChildrenIDs GetNumberOfIds()):
  print("modelChildID   : ", self.modelTreeChildrenIDs.GetId(i)) 
  print("modelChildName : ", self.shNode.GetItemName(self.modelTreeChildrenIDs.GetId(i)))
  print("modelChildNode  : ", self.shNode.GetItemDataNode(self.modelTreeChildrenIDs.GetId(i)))</code></pre>

---

## Post #14 by @Saima (2021-11-07 05:29 UTC)

<p>Hi,<br>
I tried to get model itself using</p>
<pre><code class="lang-auto">shNode.GetItemDataNode(self.modelTreeChildrenIDs.GetId(i))

but I can get the name and id but not the model node.

Is there a bug in the latest version for this 
I get 

modelChildID   :  534
modelChildName :  B_22
modelChildNode  :  None


regards,
Saima Safdar</code></pre>

---

## Post #15 by @Fernando (2021-11-07 11:13 UTC)

<p>Hi <a class="mention" href="/u/saima">@Saima</a>. I think the method is called <code>GetID</code>, not <code>GetId</code>.</p>

---

## Post #16 by @Saima (2021-11-08 03:34 UTC)

<p>Hi,<br>
No the function is GetId() with GetID() its giving error</p>
<p>File “/home/saima/Downloads/Downloads/slicer/BoneModelExtractor/BoneModelExtractor/BoneModelExtractor.py”, line 454, in process<br>
print("modelChildNode  : ", shNode.GetItemDataNode(modelTreeChildrenIDs.GetID(i)))<br>
AttributeError: ‘vtkCommonCorePython.vtkIdList’ object has no attribute ‘GetID’</p>

---

## Post #17 by @Saima (2021-11-08 03:37 UTC)

<p>Hi,<br>
fior me</p>
<pre><code class="lang-auto">self.shNode.GetItemDataNode(self.modelTreeChildrenIDs.GetId(i)))
</code></pre>
<p>is not working its giving none</p>
<p>any help.</p>
<p>Regards,<br>
Saima Safdar</p>

---
