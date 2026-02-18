# Create a vtkMRMLModelNode from a polyData

**Topic ID**: 8679
**Date**: 2019-10-05
**URL**: https://discourse.slicer.org/t/create-a-vtkmrmlmodelnode-from-a-polydata/8679

---

## Post #1 by @danial (2019-10-05 06:27 UTC)

<p>Operating system: macOS 10.146<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I want to create a vtkMRMLModelNode and display it in slicer, i did it like this :</p>
<pre><code>vtkNew&lt;vtkMRMLModelNode&gt; mesh;
mesh-&gt;SetAndObservePolyData(poly);
mesh-&gt;CreateDefaultDisplayNodes();
mesh-&gt;SetName(nameOfNode.c_str());
this-&gt;mrmlScene()-&gt;AddNode(mesh.GetPointer());
</code></pre>
<blockquote>
<p>Blockquote vtkMRMLModelNode::CreateDefaultDisplayNodes failed: scene is invalid<br>
error: [/RealTimeAblation/Slicer/Slicer-SuperBuild/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.<br>
09:49:38: /Slicer/Slicer-SuperBuild/Slicer-build/Slicer exited with code 1</p>
</blockquote>
<p>Can you help me to solve this problem, please ?</p>
<p>Thanks for your help.</p>

---

## Post #2 by @lassoan (2019-10-05 12:14 UTC)

<p>The warning is because you need to add the model node to scene before calling CreateDisplayNodes (because display nodes must be added to the same scene).</p>
<p>The crash is probably because scene is nullptr.</p>
<p>You can simplify things a bit, too:</p>
<pre><code class="lang-python">vtkMRMLModelNode* mesh = this-&gt;mrmlScene()-&gt;AddNewNodeByClass("vtkMRMLModelNode", nameOfNode.c_str());
mesh-&gt;SetAndObservePolyData(poly);
mesh-&gt;CreateDefaultDisplayNodes();
</code></pre>

---

## Post #3 by @danial (2019-10-05 12:43 UTC)

<p>Thank you so much, this solution works very well.</p>

---
