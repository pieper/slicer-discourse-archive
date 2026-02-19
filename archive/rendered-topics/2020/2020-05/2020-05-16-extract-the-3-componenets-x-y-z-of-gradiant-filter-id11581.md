---
topic_id: 11581
title: "Extract The 3 Componenets X Y Z Of Gradiant Filter"
date: 2020-05-16
url: https://discourse.slicer.org/t/11581
---

# Extract the 3 componenets x,y,z of gradiant filter

**Topic ID**: 11581
**Date**: 2020-05-16
**URL**: https://discourse.slicer.org/t/extract-the-3-componenets-x-y-z-of-gradiant-filter/11581

---

## Post #1 by @loubna (2020-05-16 21:54 UTC)

<p>Hi;</p>
<p>I have applied two filters on 3d vtkImagedata (binary volume) in order to compute the gradient at each (i,j,k) voxel like:</p>
<p>vtkImageGaussianSmooth *gaussianFilter = vtkImageGaussianSmooth::New();<br>
gaussianFilter-&gt;SetInputData(ContourImg);<br>
gaussianFilter-&gt;SetDimensionality(3);<br>
gaussianFilter-&gt;SetStandardDeviations (2, 2, 2);<br>
gaussianFilter-&gt;Update();</p>
<p>vtkImageGradient *gradientFilter = vtkImageGradient::New();<br>
gradientFilter-&gt;SetInputData(gaussianFilter-&gt;GetOutput());<br>
gradientFilter-&gt;SetDimensionality(3);<br>
gradientFilter-&gt;HandleBoundariesOn();<br>
gradientFilter-&gt;Update();</p>
<p>Now I want recover the x ,y and z component of each voxel. I have see some example on net but i am confused about the right solution so here is my solution:</p>
<p>vtkDataArray* grad = gradImg-&gt;GetPointData()-&gt;GetScalars();<br>
int coords[3]= {i, j, k};<br>
vtkIdType tupleId = gradImg-&gt;ComputePointId(coords);</p>
<pre><code>  g[0]= grad-&gt;GetComponent(tupleId, 0);
  g[1]= grad-&gt;GetComponent(tupleId, 1);
  g[2]= grad-&gt;GetComponent(tupleId, 2);
</code></pre>
<p>But in other examples, they use the “vtkImageExtractComponents” to extract x and y components of the gradient like this:</p>
<p>vtkSmartPointer extractXFilter =<br>
vtkSmartPointer::New();<br>
extractXFilter-&gt;SetComponents(0);<br>
extractXFilter-&gt;SetInputConnection(gradientFilter-&gt;GetOutputPort());</p>
<p>double xRange[2];</p>
<p>extractXFilter-&gt;Update();<br>
extractXFilter-&gt;GetOutput()-&gt;GetPointData()-&gt;GetScalars()-&gt;GetRange(xRange);</p>
<p>I Dont understand how can I use this filter to extract the gradiant components at each i,j,k voxel</p>
<p>thank’s in advance</p>

---

## Post #2 by @lassoan (2020-05-16 22:14 UTC)

<p>There are many ways to access voxel data. Simple methods, such as GetScalarComponentAsDouble are extremely slow, raw buffer access, such as GetScalarPointer only work well for known memory layout (Slicer uses only the default memory layout, so it should be fine), fast and flexible methods use multithreading and array dispatching, which are extremely complicated.</p>
<p>In your case, I would recommend using GetScalarPointer.</p>

---
