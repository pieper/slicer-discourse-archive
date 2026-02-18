# Grid transform Set-/GetIJKToRASMatrix

**Topic ID**: 14330
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/grid-transform-set-getijktorasmatrix/14330

---

## Post #1 by @mangotee (2020-10-30 14:24 UTC)

<p>Hi,<br>
I am playing around with <a href="https://airlab.readthedocs.io/en/latest/" rel="noopener nofollow ugc">Airlab</a> (a nice toolkit and research environment for autograd/pytorch based deformable registration). With Airlab it is possible to non-linearly register two volumes, and save the computed deformation field as a nrrd file, under the hood it uses <code>sitk.WriteImage()</code> to do that. When loading the deformation field, I realized that I need to change the <code>IJKToRASMatrix</code> from sth like <code>diag([-1,-1,1,1])</code> to <code>diag([1,1,1,1])</code>, to appear at the “right location”, and I need to invert the x-/y-components of the deformation field (by multiplying with -1).</p>
<p>The only way I am right now able to change the affine matrix of the GridTransform, is to load the grid transform via <code>loadVolume()</code>, manipulate its affine transform via <code>GetIJKToRASMatrix()</code> and <code>SetIJKToRASMatrix()</code> (also, change the vector x/y components via <code>arrayFromVolume()</code> and <code>updateVolumeFromArray()</code>), then write it back to disk via <code>saveNode()</code>, and then load it back into Slicer via <code>loadTransform()</code>.</p>
<p>My question now is whether there is a way to avoid handling the grid transform as a volume entirely. E.g. when I load the transform via <code>loadTransform()</code>, the <code>vtkMRMLGridTransformNode</code> class does not have the methods <code>GetIJKToRASMatrix</code> and <code>SetIJKToRASMatrix</code>. Is there an equivalent? Alternatively: Is there a way to conveniently convert the grid transform to a volume and back, without the “detour” of having to read/write a volume first?</p>

---

## Post #2 by @lassoan (2020-10-30 16:45 UTC)

<p>Files are always in LPS coordinate systems, while Slicer uses RAS internally. If you transfer the volume and displacement field via files then everything should work correctly (ITK will work in LPS, Slicer works in RAS, Slicer knows that it has to transform displacement field vectors from LPS to RAS on load). If you don’t use compression then file reading/writing time should be negligible compared to registration time. You can run your processing script as a <a href="https://github.com/lassoan/SlicerPythonCLIExample">Python scripted CLI module</a>, which naturally does all transfers via files and it also has the advantage that it runs the registration in the background (so that the application GUI is not blocked during execution) and any error or exceeding available memory cannot crash the application (because the script runs in a separate process).</p>
<p>You can of course run everything in the same process and pass images in the memory but then you need to take car of IJK&lt;-&gt;RAS conversion yourself. For example you can find conversion implemented in C++ here: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkITKTransformConverter.h#L928-L986" class="inline-onebox">Slicer/Libs/MRML/Core/vtkITKTransformConverter.h at main · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="14330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>My question now is whether there is a way to avoid handling the grid transform as a volume entirely.</p>
</blockquote>
</aside>
<p>You can load the transform using loadTransform. Both the image geometry (origin, spacing, axis directions) and vectors inside the volume are expected to be in LPS.</p>
<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="14330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p><code>vtkMRMLGridTransformNode</code> class does not have the methods <code>GetIJKToRASMatrix</code> and <code>SetIJKToRASMatrix</code></p>
</blockquote>
</aside>
<p>Since a transform node can contain arbitrarily complex composition of various transforms, the node does not have direct GetIJKToRASMatrix method. If you know that you have a simple transform in the node then you can get the <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#a663ef3ba2eaa13137e0f8f1a40de448e">ToParent or FromParent transform as the specified type</a> and get direction matrix from the returned <a href="https://github.com/Slicer/vtkAddon/blob/master/vtkOrientedGridTransform.h">vtkOrientedGridTransform</a>. To convert a displacement field between LPS&lt;-&gt;RAS it is of course not enough to change the image geometry but each vector must be transformed, too (as shown in the C++ code above).</p>

---
