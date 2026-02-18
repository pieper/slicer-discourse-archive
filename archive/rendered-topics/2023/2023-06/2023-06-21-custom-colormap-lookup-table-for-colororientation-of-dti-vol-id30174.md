# Custom Colormap Lookup Table for 'ColorOrientation' of DTI Volume?

**Topic ID**: 30174
**Date**: 2023-06-21
**URL**: https://discourse.slicer.org/t/custom-colormap-lookup-table-for-colororientation-of-dti-volume/30174

---

## Post #1 by @ste (2023-06-21 18:32 UTC)

<p>Operating system: Ubuntu 20.04.6 LTS<br>
Slicer version: 4.10.2</p>
<p>Would it be possible to import a custom colormap for the ‘ColorOrientation’ of a DTI volume?</p>
<p>Currently that option is locked to the conventional color-code:<br>
R: Left-Right<br>
G: Anterior-Posterior<br>
B: Inferior-Superior<br>
and interpolated colors for intermediate directions of fibers.</p>
<p>Different from the canonical convention, I would like to design/import a custom color-code to map such orientations. Is that possible?</p>
<p>If yes, how can I enable such option? Is there a specific file/configuration I can look into?</p>
<p>Thank You<br>
S.</p>

---

## Post #2 by @pieper (2023-06-21 18:47 UTC)

<p>It would be doable, but you would need to change the C++ code for that.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/d7c9a0dbd10552fac6eb33933ecc7c4fd0c8ed5f/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L686-L712">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/d7c9a0dbd10552fac6eb33933ecc7c4fd0c8ed5f/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L686-L712" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d7c9a0dbd10552fac6eb33933ecc7c4fd0c8ed5f/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L686-L712" target="_blank" rel="noopener">Slicer/Slicer/blob/d7c9a0dbd10552fac6eb33933ecc7c4fd0c8ed5f/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L686-L712</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="686" style="counter-reset: li-counter 685 ;">
          <li>case vtkDiffusionTensorMathematics::VTK_TENS_COLOR_ORIENTATION:</li>
          <li>  // If the user has set the rotation matrix</li>
          <li>  // then transform the eigensystem first</li>
          <li>  // This is used to rotate the vector into RAS space</li>
          <li>  // for consistent anatomical coloring.</li>
          <li>  v_maj[0]=v[0][0];</li>
          <li>  v_maj[1]=v[1][0];</li>
          <li>  v_maj[2]=v[2][0];</li>
          <li>  if (useTransform)</li>
          <li>    {</li>
          <li>    trans-&gt;TransformPoint(v_maj,v_maj);</li>
          <li>    }</li>
          <li>  // Color R, G, B depending on max eigenvector</li>
          <li>  // scale maps 0..1 values into the range a char takes on</li>
          <li>  cl = vtkDiffusionTensorMathematics::LinearMeasure(w);</li>
          <li>  rgb_temp = (rgb_scale*fabs(v_maj[0])*cl);</li>
          <li>  *outPtr = (T)tensor_math_clamp(rgb_temp, (double)VTK_UNSIGNED_CHAR_MIN, (double)VTK_UNSIGNED_CHAR_MAX);</li>
          <li>  outPtr++;</li>
          <li>  rgb_temp = (rgb_scale*fabs(v_maj[1])*cl);</li>
          <li>  *outPtr = (T)tensor_math_clamp(rgb_temp, (double)VTK_UNSIGNED_CHAR_MIN, (double)VTK_UNSIGNED_CHAR_MAX);</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/d7c9a0dbd10552fac6eb33933ecc7c4fd0c8ed5f/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L686-L712" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
