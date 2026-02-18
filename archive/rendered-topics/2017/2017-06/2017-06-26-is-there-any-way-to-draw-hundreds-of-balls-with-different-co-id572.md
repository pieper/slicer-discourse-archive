# Is there any way to draw hundreds of balls with different colors?

**Topic ID**: 572
**Date**: 2017-06-26
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-draw-hundreds-of-balls-with-different-colors/572

---

## Post #1 by @wpgao (2017-06-26 09:13 UTC)

<p>Is there any way to draw hundreds of balls with different colors more efficiently?<br>
I had obtained the position information from the sensor and hope to illustrate the data using the ball in 3D View. There is hundreds of balls should be illustrated with different color! How to achieve this in a more efficient way?<br>
Thanks very much!</p>

---

## Post #2 by @lassoan (2017-06-26 09:28 UTC)

<p>Create a vtkPolyData (using vtkGlyph3D filter), set that into a Model node, and choose a colormap to color it (based on point data stored in the vtkPolyData). Let us know if you stuck at any point.</p>

---

## Post #3 by @Fernando (2017-06-26 09:31 UTC)

<p>You can check my gist, which includes a minimal example of vtkGlyph3D: <a href="https://gist.github.com/fepegar/bb18198c9dae273e083521db422ec5c0" rel="nofollow noopener">https://gist.github.com/fepegar/bb18198c9dae273e083521db422ec5c0</a></p>

---

## Post #4 by @cpinter (2017-06-26 09:41 UTC)

<p>If you want to visualize positions then I think fiducials could be a good way to do that. You can add fiducials from the toolbar and handle them in the Markups module. They are visualized in 3D as balls by default. The different colors can be set to each fiducial set node.</p>

---

## Post #5 by @Fernando (2017-06-26 09:46 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If you want to visualize positions then I think fiducials could be a good way to do that. You can add fiducials from the toolbar and handle them in the Markups module.</p>
</blockquote>
</aside>
<p>I think it would be hard for Slicer to handle “hundreds” of fiducials, as discussed in this <a href="https://issues.slicer.org/view.php?id=4306" rel="noopener nofollow ugc">issue</a>.</p>

---

## Post #6 by @wpgao (2017-06-27 07:32 UTC)

<p>Hi Lasso,</p>
<p>I had created a vtkPolyData which store the point data and scalars (color), and set it into a Model node. How can I choose the scalars stored in vtkPolyData as the colormap?<br>
Thanks very much!</p>
<pre><code>vtkSmartPointer&lt;vtkPoints&gt; points = vtkSmartPointer&lt;vtkPoints&gt;::New();
for(iter=path-&gt;begin();iter!=path-&gt;end();iter++)
	points-&gt;InsertNextPoint(iter-&gt;pos.x,iter-&gt;pos.y,iter-&gt;pos.z);

vtkSmartPointer&lt;vtkPolyData&gt; polyData = vtkSmartPointer&lt;vtkPolyData&gt;::New();
polyData-&gt;SetPoints(points);

vtkSmartPointer&lt;vtkVertexGlyphFilter&gt; vertexFilter = vtkSmartPointer&lt;vtkVertexGlyphFilter&gt;::New();
vertexFilter-&gt;SetInputData(polyData);
vertexFilter-&gt;Update();

vtkSmartPointer&lt;vtkUnsignedCharArray&gt; Colors=vtkSmartPointer&lt;vtkUnsignedCharArray&gt;::New();
Colors-&gt;SetName("Color");
Colors-&gt;SetNumberOfComponents(3);
std::vector&lt;Point3f&gt;::iterator it1;
for(it1=color-&gt;begin();it1!=color-&gt;end();it1++)
	Colors-&gt;InsertNextTuple3(it1-&gt;x,it1-&gt;y,it1-&gt;z);	

vtkSmartPointer&lt;vtkPolyData&gt; polyData1 = vtkSmartPointer&lt;vtkPolyData&gt;::New();
polyData1-&gt;ShallowCopy(vertexFilter-&gt;GetOutput());
polyData1-&gt;GetPointData()-&gt;SetScalars(Colors);


//create model node
m_PtsModelNode[which] = vtkSmartPointer&lt;vtkMRMLModelNode&gt;::New();
m_PtsModelNode[which].Take(vtkMRMLModelNode::SafeDownCast(m_scene-&gt;CreateNodeByClass("vtkMRMLModelNode")));
m_PtsModelNode[which]-&gt;SetName(m_scene-&gt;GetUniqueNameByString(m_strModelName[which].c_str()));
m_PtsModelNode[which]-&gt;SetAndObservePolyData(polyData1);
</code></pre>
<p>Best,<br>
Wenpeng</p>

---

## Post #7 by @lassoan (2017-06-27 20:54 UTC)

<p>Example:</p>
<pre><code>modelNode.GetDisplayNode().SetActiveScalarName('Distance')
modelNode.GetDisplayNode().SetAndObserveColorNodeID('vtkMRMLFreeSurferProceduralColorNodeBlueRed')
modelNode.GetDisplayNode().ScalarVisibilityOn()
#modelNode.GetDisplayNode().AutoScalarRangeOn()
modelNode.GetDisplayNode().SetScalarRangeFlag(slicer.vtkMRMLDisplayNode.UseColorNodeScalarRange) 
</code></pre>
<p>See API description here: <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html">http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html</a></p>

---

## Post #8 by @wpgao (2017-06-30 05:11 UTC)

<p>Hi Fernando,</p>
<p>Thanks for your reply. It works!</p>
<p>Best,<br>
Wenpeng</p>

---

## Post #9 by @wpgao (2017-06-30 05:12 UTC)

<p>Hi Lasso,</p>
<p>Thanks for your reply. It works!</p>
<p>Best,<br>
Wenpeng</p>

---
