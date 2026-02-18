# Vtk transform matrix as python list/tuple array

**Topic ID**: 11797
**Date**: 2020-05-30
**URL**: https://discourse.slicer.org/t/vtk-transform-matrix-as-python-list-tuple-array/11797

---

## Post #1 by @talmazov (2020-05-30 22:59 UTC)

<p>Hey,<br>
I have a model object i am exporting to PLY then trying to obtain its transform node as python list/tuple<br>
I am doing this in my script</p>
<blockquote>
<p>my_matrix = transform.GetMatrixTransformFromParent()<br>
matrix_Array = my_matrix.GetData()</p>
</blockquote>
<p>where matrix_Array should look like [[row1,…],[row2,…],[…]]</p>
<p>or so i thought that GetData would provide me with per<br>
<a href="https://vtk.org/doc/nightly/html/classvtkMatrix4x4.html#a46a8fab5dec2c21f6379beb89730bd74" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkMatrix4x4.html#a46a8fab5dec2c21f6379beb89730bd74</a><br>
The document says it returns a raw double array, im not sure what “raw” would entail, I was hoping for it to be a native python array object but when I try to print the object it gives me a mem pointer / instance address… i’m a little confused what to do with it at this point.</p>
<p>I know I can try to iterate through the matrix, and I know it’s fixed 4x4, and manually create the array by pulling data via GetElement but is there a more elegant way of doing this that has already been implemented?</p>
<p>thanks!</p>

---

## Post #2 by @lassoan (2020-05-30 23:54 UTC)

<p>You can use this function to convert a raw pointer to a Python list:</p>
<aside class="quote quote-modified" data-post="9" data-topic="6209">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/centering-on-a-segment-from-a-script/6209/9">Centering on a segment from a script</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Using a custom extension is certainly a solution, but in the long term I would recommend developers to use Slicer core functions if available. 
Slicer-4.10 returning a swig pointer (such as _000001bfd4897340_p_void) is a minor inconvenience. You can still access the values using the helper function below (in the nightly version the VTK hint is there so the position is directly returned as a Python tuple). 
def getListFromPointer(bufferPtr, scalarType=vtk.VTK_DOUBLE, numberOfElements=3):
  """Con…
  </blockquote>
</aside>

<p>A bit more elegant, but probably not much faster or simpler method is to use DeepCopy method:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/e53e8af9c4a0b60adee28b5eca5fc1b5ff2da9ea/Base/Python/slicer/util.py#L1114-L1151">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/e53e8af9c4a0b60adee28b5eca5fc1b5ff2da9ea/Base/Python/slicer/util.py#L1114-L1151" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e53e8af9c4a0b60adee28b5eca5fc1b5ff2da9ea/Base/Python/slicer/util.py#L1114-L1151" target="_blank" rel="noopener">Slicer/Slicer/blob/e53e8af9c4a0b60adee28b5eca5fc1b5ff2da9ea/Base/Python/slicer/util.py#L1114-L1151</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1114" style="counter-reset: li-counter 1113 ;">
          <li>def arrayFromVTKMatrix(vmatrix):</li>
          <li>  """Return vtkMatrix4x4 or vtkMatrix3x3 elements as numpy array.</li>
          <li>  The returned array is just a copy and so any modification in the array will not affect the input matrix.</li>
          <li>  To set VTK matrix from a numpy array, use :py:meth:`vtkMatrixFromArray` or</li>
          <li>  :py:meth:`updateVTKMatrixFromArray`.</li>
          <li>  """</li>
          <li>  from vtk import vtkMatrix4x4</li>
          <li>  from vtk import vtkMatrix3x3</li>
          <li>  import numpy as np</li>
          <li>  if isinstance(vmatrix, vtkMatrix4x4):</li>
          <li>    matrixSize = 4</li>
          <li>  elif isinstance(vmatrix, vtkMatrix3x3):</li>
          <li>    matrixSize = 3</li>
          <li>  else:</li>
          <li>    raise RuntimeError("Input must be vtk.vtkMatrix3x3 or vtk.vtkMatrix4x4")</li>
          <li>  narray = np.eye(matrixSize)</li>
          <li>  vmatrix.DeepCopy(narray.ravel(), vmatrix)</li>
          <li>  return narray</li>
          <li></li>
          <li>def vtkMatrixFromArray(narray):</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/e53e8af9c4a0b60adee28b5eca5fc1b5ff2da9ea/Base/Python/slicer/util.py#L1114-L1151" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @talmazov (2020-05-31 08:45 UTC)

<p>worked well, thanks.</p>

---

## Post #4 by @lassoan (2020-05-31 15:19 UTC)

<p>Note that in Slicer’s Python environment you can simply use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromTransformMatrix">slicer.util.arrayFromTransformMatrix</a> to get a numpy array from a transform node (and there are similar convenience functions for getting/settings various other node contents as numpy array).</p>

---
