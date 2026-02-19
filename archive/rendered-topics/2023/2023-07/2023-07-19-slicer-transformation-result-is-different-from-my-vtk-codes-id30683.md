---
topic_id: 30683
title: "Slicer Transformation Result Is Different From My Vtk Codes"
date: 2023-07-19
url: https://discourse.slicer.org/t/30683
---

# Slicer transformation result is different from my vtk codes

**Topic ID**: 30683
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/slicer-transformation-result-is-different-from-my-vtk-codes/30683

---

## Post #1 by @dzzhang (2023-07-19 15:53 UTC)

<p>Recently I used the <strong>Transform</strong> module in Slicer to apply a linear transformation. Let’s say the translation is [10, 20, 30]. And the model moved to the correct position.</p>
<p>However, when I used my own vtk codes below, the result is not correct.</p>
<pre><code class="lang-auto">vtkSmartPointer&lt;vtkTransform&gt; transform = vtkSmartPointer&lt;vtkTransform&gt;::New();
transform-&gt;Translate(10, 20, 30);
vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt; transformFilter = vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt;::New();
transformFilter-&gt;SetInputData(mesh);
transformFilter-&gt;SetTransform(transform);
transformFilter-&gt;Update();
</code></pre>
<p>First I was thinking it is because of the coordinate system difference (RAS and LPS), so I flipped the two axes:</p>
<pre><code class="lang-auto">translationMatrix-&gt;SetElement(0, 0, -1.0); 
translationMatrix-&gt;SetElement(1, 1, -1.0);
</code></pre>
<p>However, it is still not correct. Did I miss some steps used in Slicer? Thanks for any suggestions!</p>

---

## Post #2 by @pieper (2023-07-19 19:27 UTC)

<p>You would actually need to change the values of the translations, not just the main diagonal.  But in general you should be applying a matrix to do the transform, something like this:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/c5724d5fd588f8de267ddd696b30c18e7c6f9a8f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L788-L801">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/c5724d5fd588f8de267ddd696b30c18e7c6f9a8f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L788-L801" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c5724d5fd588f8de267ddd696b30c18e7c6f9a8f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L788-L801" target="_blank" rel="noopener">Slicer/Slicer/blob/c5724d5fd588f8de267ddd696b30c18e7c6f9a8f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L788-L801</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="788" style="counter-reset: li-counter 787 ;">
          <li>    # map from LPS to RAS</li>
          <li>    lpsToRAS = numpy.array([-1, -1, 1])</li>
          <li>    position *= lpsToRAS</li>
          <li>    rowOrientation *= lpsToRAS</li>
          <li>    columnOrientation *= lpsToRAS</li>
          <li>    rowVector = columns * spacing[1] * rowOrientation  # dicom PixelSpacing is between rows first, then columns</li>
          <li>    columnVector = rows * spacing[0] * columnOrientation</li>
          <li>    # apply the transform to the four corners</li>
          <li>    for column in range(2):</li>
          <li>        for row in range(2):</li>
          <li>            corners[sliceIndex][row][column] = position</li>
          <li>            corners[sliceIndex][row][column] += column * rowVector</li>
          <li>            corners[sliceIndex][row][column] += row * columnVector</li>
          <li>return corners</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @dzzhang (2023-07-19 21:02 UTC)

<p>Hi pieper, thanks for the reply!<br>
Can I ask what do you mean by “not just the diagonal”?</p>
<p>I have tried to apply the two matrix below but the error still exists:</p>
<p>| 1 | 0 | 0 | 10 |<br>
| 0 | 1 | 0 | 20 |<br>
| 0 | 0 | 1 | 30 |<br>
| 0 | 0 | 0 | 1  |</p>
<p>and</p>
<p>| -1 | 0 | 0 | 10 |<br>
| 0 | -1 | 0 | 20 |<br>
| 0 | 0 | 1 | 30 |<br>
| 0 | 0 | 0 | 1  |</p>

---

## Post #4 by @pieper (2023-07-19 23:30 UTC)

<p>This operation from your post only changes the two elements on the diagonal:</p>
<aside class="quote no-group" data-username="dzzhang" data-post="1" data-topic="30683">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dzzhang/48/66871_2.png" class="avatar"> dzzhang:</div>
<blockquote>
<pre><code class="lang-auto">translationMatrix-&gt;SetElement(0, 0, -1.0); 
translationMatrix-&gt;SetElement(1, 1, -1.0);
</code></pre>
</blockquote>
</aside>
<p>What you need to do is multiply your translation matrix by a matrix that is identity but with -1 in the 0,0 and 1,1 locations.  The effect in this case will be to negate the first two translation values.</p>

---

## Post #5 by @dzzhang (2023-07-20 00:39 UTC)

<p>Hi pieper, I have multiplied the two matrix:</p>
<p>the first is [1, 0, 0, 10; 0, 1, 0, 20; 0, 0, 1, 30; 0, 0, 0, 1]<br>
the second is [-1, 0, 0, 0; 0, -1, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]<br>
the result is [-1, 0, 0, 10; 0, -1, 0, 20; 0, 0, 1, 30; 0, 0, 0, 1]</p>
<p>But the error still exists.</p>
<p>I was thinking if it is because my mesh model is not in the center of the bounding box. So I output the center coordinates of the mesh before and after the transformation. It’s weird that the coordinates after transformation are not (-10, -20, 30).</p>
<p>My codes below:</p>
<pre><code class="lang-auto">vtkSmartPointer&lt;vtkMatrix4x4&gt; translationMatrix = vtkSmartPointer&lt;vtkMatrix4x4&gt;::New();
translationMatrix-&gt;SetElement(0, 3, 10); 
translationMatrix-&gt;SetElement(1, 3, 20); 
translationMatrix-&gt;SetElement(2, 3, 30); 
translationMatrix-&gt;SetElement(0, 0, -1.0); 
translationMatrix-&gt;SetElement(1, 1, -1.0); 
transform-&gt;SetMatrix(translationMatrix);
vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt; transformFilter = vtkSmartPointer&lt;vtkTransformPolyDataFilter&gt;::New();
transformFilter-&gt;SetInputData(mesh);

transformFilter-&gt;GetOutput()-&gt;GetCenter(center); // the center is (0, 0, 0)

transformFilter-&gt;SetTransform(transform);
transformFilter-&gt;Update();

transformFilter-&gt;GetOutput()-&gt;GetCenter(center2); // the center is not (-10, -20, 30)
</code></pre>

---

## Post #6 by @pieper (2023-07-20 13:14 UTC)

<p>There’s more information here: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a></p>
<p>You can also search google for LPS and RAS to get more examples.</p>

---

## Post #7 by @lassoan (2023-07-20 13:53 UTC)

<p>You may also find this script useful that shows how to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">convert ITK transform file to Slicer transform</a>.</p>

---

## Post #8 by @Mehran (2023-07-21 09:06 UTC)

<p>Indeed, even in python image direction/coordinates are different. I tried this code and worked. you may have a look and find out how to convert coordinates in c++:<br>
image=sitk.ReadImage(image)<br>
dirs = np.zeros([3,3])<br>
image.GetIJKToRASDirections(dirs)<br>
dirs=np.multiply(dirs,np.array([[-1,-1,-1],[-1,-1,-1],[1,1,1]]))<br>
new_dirctions=np.reshape(dirs,(1,9)).tolist()<br>
new_origin=label.GetOrigin()</p>

---

## Post #9 by @dzzhang (2023-07-23 00:03 UTC)

<p>This worked! Thank you!</p>

---
