# Transform a vtkMRMLModelNode

**Topic ID**: 8684
**Date**: 2019-10-05
**URL**: https://discourse.slicer.org/t/transform-a-vtkmrmlmodelnode/8684

---

## Post #1 by @danial (2019-10-05 14:07 UTC)

<p>Operating system: macOS 10.14.6<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I want to set and apply a transformation on a vtkMRMLModelNode by its polyData. I did it like this :</p>
<pre><code class="lang-auto">&gt; vtkSmartPointer&lt;vtkPolyData&gt; cylinder = vtkMRMLModelNode::SafeDownCast(node)-&gt;GetPolyData();
&gt;
&gt; / create transform filter
&gt; vtkSmartPointer&lt;vtkTransform&gt; translation = vtkSmartPointer&lt;vtkTransform&gt;::New();
&gt; translation-&gt;Translate(vectranslation[0], vectranslation[1], vectranslation[2]);
&gt; 
&gt; // apply filter on cylinder
&gt; vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt; transformFilter = vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt;::New();
&gt; transformFilter-&gt;SetInputData(m_cylinder);
&gt; transformFilter-&gt;SetTransform(translation);
&gt; transformFilter-&gt;Update();
&gt; cylinder-&gt;ShallowCopy(transformFilter-&gt;GetOutput());
</code></pre>
<p>But it would not display the modifications in Slicer. Can you help me to do it, please ?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-10-05 15:32 UTC)

<p>Try calling <code>node-&gt;Modified()</code>.</p>
<p>Also as a general suggestion, I always prototype this kind of thing in the python console before doing it in C++.  It’s much quicker and easier to learn how the nodes and viewers behave without needing to exit, recompile, and restart for each experiment.</p>

---

## Post #3 by @danial (2019-10-05 17:37 UTC)

<p>You are right. It’s much quicker and easier.</p>
<p>Thank you.</p>

---
