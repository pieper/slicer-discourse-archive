---
topic_id: 23374
title: "Add Storagenode To Volumenode Created From A Numpy Array"
date: 2022-05-11
url: https://discourse.slicer.org/t/23374
---

# Add storageNode to volumeNode created from a numpy array

**Topic ID**: 23374
**Date**: 2022-05-11
**URL**: https://discourse.slicer.org/t/add-storagenode-to-volumenode-created-from-a-numpy-array/23374

---

## Post #1 by @Marc-3d (2022-05-11 15:59 UTC)

<p>Hello,</p>
<p>I am creating a volumeNode and populating it with data from a 3D numpy array.</p>
<pre><code class="lang-auto"> volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
 slicer.util.updateVolumeFromArray(volumeNode, data)
</code></pre>
<p>Later in my code, I expect all volumes to have a storageNode() and a fileName.</p>
<p>I tried both:</p>
<pre><code class="lang-auto">   storageNode = volumeNode.createDefaultStorageNode();
   storageNode.setFileName('path/to/the/file/that/contains/the/data')
</code></pre>
<p>and</p>
<pre><code class="lang-auto">    storageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()
    storageNode.SetFileName( 'path/to/the/file/that/contains/the/data' )   
    volumeNode.AddAndObserveStorageNodeID( storageNode.GetID() )
</code></pre>
<p>but in both cases when I try to get the storage node from the volumes I get nothing.</p>
<pre><code class="lang-auto">    volumeNode.getStorageNode() #returns a NoneType
</code></pre>
<p>Any idea on how to add a storageNode successfully?</p>
<p>Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Marc</p>

---

## Post #2 by @pieper (2022-05-11 16:49 UTC)

<p>Hi -</p>
<p>Looks like you are close.  My suggestion is to make reproducible snippets that anyone can paste into a freshly started Slicer instance and reproduce your question.  Disconnected lines of code are really impossible to debug, but I can tell they aren’t part of a real program because of syntax errors like <code>setFileName</code> instead of <code>SetFileName</code>.  Formulating such concise and reproducible examples can often help you find the issues yourself.  We often point to this page for guidance: <a href="http://sscce.org/">http://sscce.org/</a></p>

---

## Post #3 by @Marc-3d (2022-05-11 18:07 UTC)

<p>Hi, my bad. Here is reproducible code that you should be able to copy into Slicer’s Python Interactor.</p>
<pre><code class="lang-python"># Method 1
import numpy as np
data = np.random.rand( 50, 50, 50 ); # dummy data. In reality I am loading czi files, ex "C:/users/marc/data.czi"
volumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode');
slicer.util.updateVolumeFromArray(volumeNode1, data );
storageNode1 = slicer.vtkMRMLVolumeArchetypeStorageNode() # creating storageNode separeate from volumeNode
storageNode1.SetFileName( "C:/users/marc/data.czi" ) 
volumeNode1.AddAndObserveStorageNodeID( storageNode1.GetID() ) # AddAndObserve to link storageNode to volumeNode
print( "Method 1", volumeNode1.GetStorageNode() )
</code></pre>
<p>And the other version:</p>
<pre><code class="lang-python"># Method 2
import numpy as np
data = np.random.rand( 50, 50, 50 );  # dummy data. In reality I am loading czi files, ex "C:/users/marc/data.czi"
volumeNode2 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode');
slicer.util.updateVolumeFromArray(volumeNode2, data );
storageNode2 = volumeNode2.CreateDefaultStorageNode()  # Creating storageNode from volumeNode. I don't think AddAndObserve is required.
storageNode2.SetFileName( "C:/users/marc/data.czi" )
print( "Method 2", volumeNode2.GetStorageNode() )
</code></pre>

---

## Post #4 by @Marc-3d (2022-05-11 18:18 UTC)

<p>I found the problem: In method 1, I needed to add the storageNode to the scene… otherwise the storageNode.GetID() is not available to the rest of nodes, and it cannot be “AddedAndObserved”.</p>
<p>This now works:</p>
<pre><code class="lang-python">import numpy as np
data = np.random.rand( 50, 50, 50 ); 
volumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode');
slicer.util.updateVolumeFromArray(volumeNode1, data );
storageNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLVolumeArchetypeStorageNode') # this creates storageNode and adds it to the scene
storageNode1.SetFileName( "C:/users/marc/data.czi" ) 
volumeNode1.AddAndObserveStorageNodeID( storageNode1.GetID() )
print( "Method 1", volumeNode1.GetStorageNode() )
</code></pre>

---

## Post #5 by @lassoan (2022-05-12 12:39 UTC)

<p>You can simplify this even further (based on examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>):</p>
<pre><code class="lang-python">import numpy as np
voxelArray = np.random.rand(50, 50, 50)

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
slicer.util.updateVolumeFromArray(volumeNode, voxelArray)
volumeNode.AddDefaultStorageNode()
volumeNode.GetStorageNode().SetFileName( "C:/users/marc/volume.nrrd" ) 
</code></pre>
<p>Or, if you want to immediately save to file:</p>
<pre><code class="lang-python">import numpy as np
voxelArray = np.random.rand(50, 50, 50)

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
slicer.util.updateVolumeFromArray(volumeNode, voxelArray)
slicer.util.saveNode(volumeNode, "C:/users/marc/volume.nrrd") 
</code></pre>

---
