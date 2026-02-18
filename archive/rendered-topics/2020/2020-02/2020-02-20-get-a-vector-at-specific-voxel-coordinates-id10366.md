# Get a vector at specific voxel coordinates

**Topic ID**: 10366
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/get-a-vector-at-specific-voxel-coordinates/10366

---

## Post #1 by @loubna (2020-02-20 15:16 UTC)

<p>Hi,</p>
<p>I have applied a 3d sobel filter on vtkImageData like this:</p>
<pre><code class="lang-auto">vtkSmartPointer&lt;vtkImageSobel3D&gt; sobelFilter =
vtkSmartPointer&lt;vtkImageSobel3D&gt;::New();
sobelFilter-&gt;SetInputData(image);
sobelFilter-&gt;Update();
</code></pre>
<p>My question is how can I extract the vector field at a specific voxel coordinates. For exemple to extract a value we can do:</p>
<p>int coords[3] = {i, j, k};</p>
<p>vtkVariant variant = image-&gt;GetPointData()-&gt;GetScalars()-&gt; GetVariantValue(input&gt;ComputePointId(coords));     // to get 0 or 1</p>
<p>but what about vectors , I want to get the vector field produced by soble filter at {i,j,k] coordinates in c++? I have tried many solutions but I have not get good results.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-02-20 16:12 UTC)

<p>Regardless of number of scalar components, there many different ways to access voxel data in C++. Methods that provide a single voxel’s value (such as GetVariantValue or GetScalarComponentAsDouble) are provided only for testing, diagnostics, and single-point probing only. Since all image filters in VTK access voxel data, a good starting point is to have a look at any of the filters in VTK source code. You may also ask such pure VTK questions on <a href="https://discourse.vtk.org/">VTK forum</a>.</p>
<p>We might be able to give some tips here if you provide more information about your specific use case. How large is your image? How many points you would like to probe? What are you going to do with the results? Do you have any special needs or constraints?</p>

---

## Post #3 by @loubna (2020-02-20 18:26 UTC)

<p>Thank you for your suggestion. I have posted the question on VTK forum. I just want to pick up a vector at a specific voxel coordinates. It is so easy if have applied gradiant  filter but with sobel filter there are few examples.</p>

---

## Post #4 by @lassoan (2020-02-20 18:40 UTC)

<p>Probably very few poeple, if any, uses Sobel filter. Why do you think you need to use this filter? If you need the gradient then you would normally use the image gradient filter.</p>
<p>Probably they both Sobel and gradient produce vector volume (vtkImageData with 3 scalar components) as a result, so you can access the resulting voxel data exactly the same way.</p>

---

## Post #5 by @loubna (2020-02-20 18:46 UTC)

<p>I have chosen SobelFilter. Because the method which I try to implement apply the sobleFilter then the vectors obtained are normalized and negated to get the normal vectors of each voxel. Can i use the gradiant to obtain normal vector or other ways to get normal vectors from volume dara (vtkImageData)</p>

---

## Post #6 by @lassoan (2020-02-20 18:55 UTC)

<p>The image gradient filter computes the surface normal vector direction. If you prefer to have the vectors normalized then run the result through vtkImageNormalize.</p>

---

## Post #7 by @loubna (2020-02-20 19:51 UTC)

<p>Thank’s for the response. I found this method but I want to be sure that I will use correct normal vectors to get the good reconstruction. That is why I confirm my ideas with you:</p>
<p>vtkimageData image;<br>
vtkDataArray* inScalars;;<br>
inScalars = input-&gt;GetPointData()-&gt;GetScalars());</p>
<p>image-&gt;GetPointGradient(i, j, k, inScalars, Normals[0]);</p>

---

## Post #8 by @lassoan (2020-02-20 20:59 UTC)

<p>If you only want to sample a very small percentage of points at integer voxel coordinates then GetPointGradient is a good choice. Most likely the best choice (fastest, most general, most accurate) is still vtkImageGradient followed by vtkProbeFilter.</p>

---

## Post #10 by @loubna (2020-02-21 15:29 UTC)

<p>Hi Mr;</p>
<p>I have applied vtkImageGradient  followed by vtkImageNormalize then  vtkProbeFilter to get the normal vector at each polydata point as follows:</p>
<p>vtkSmartPointer gradientFilter =<br>
vtkSmartPointer::New();<br>
gradientFilter-&gt;SetInputData(imageData);   //   image data is vtkimagedata<br>
gradientFilter-&gt;Update();</p>
<p>vtkSmartPointer normalizeFilter =<br>
vtkSmartPointer::New();<br>
normalizeFilter-&gt;SetInputData(gradientFilter-&gt;GetOutput());<br>
normalizeFilter-&gt;Update();</p>
<p>vtkSmartPointer polydata =<br>
vtkSmartPointer::New();<br>
polydata-&gt;SetPoints(points1);</p>
<p>vtkSmartPointer probe =<br>
vtkSmartPointer::New();<br>
probe-&gt;SetSourceData(normalizeFilter-&gt;GetOutput());<br>
probe-&gt;SetInputData(polydata);<br>
probe-&gt;Update();</p>
<p>however? I guess that I can recover normal vectors or at least vectors with:</p>
<p>vtkSmartPointer Normals =<br>
vtkFloatArray::SafeDownCast(probe-&gt;GetOutput()-&gt;GetPointData()-&gt;GetVectors()); // or GetNormals</p>
<p>but this generate an error. but when I do :<br>
probe-&gt;GetOutput()-&gt;GetPointData()-&gt;GetScalars(); instead of GetVectors , it works fine.</p>
<p>I have tried display the first element using</p>
<p>for(int i = 0; i &lt; 1; i++) {</p>
<pre><code>double val= Normals-&gt;GetValue(i);
cout &lt;&lt; "doubleData-&gt;GetValue(" &lt;&lt; i &lt;&lt; "): " &lt;&lt; val&lt;&lt; endl;
} 
</code></pre>
<p>I get a float value instead of 3d Normal vector? I Don’t understand what’s wrong</p>
<p>I need your help please.</p>

---

## Post #11 by @lassoan (2020-02-21 15:44 UTC)

<p>To retrieve a vector from a VTK array, use methods that return “tuple”.</p>

---

## Post #12 by @loubna (2020-02-21 16:20 UTC)

<p>But according to vtk documentation, vtkImage Gradiant return scalars and not vectors . I Don’t understand how it computes vectors</p>

---

## Post #13 by @lassoan (2020-02-21 16:57 UTC)

<p>Vectors, Scalars, Normals, Tensors, TCoords words on <a href="https://vtk.org/doc/nightly/html/classvtkDataSetAttributes.html">vtkDataSetAttributes</a> interface do <em>not</em> refer to the type of the array. Scalars array may contain multiple scalar components (making it essentially vector data). I understand that it may be confusing and I would recommend to read the <a href="https://vtk.org/vtk-textbook/">VTK textbook</a> to get better insight into why it is like this.</p>

---
