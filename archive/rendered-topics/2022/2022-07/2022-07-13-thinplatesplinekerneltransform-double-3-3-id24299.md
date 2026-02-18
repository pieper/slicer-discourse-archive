# ThinPlateSplineKernelTransform_double_3_3

**Topic ID**: 24299
**Date**: 2022-07-13
**URL**: https://discourse.slicer.org/t/thinplatesplinekerneltransform-double-3-3/24299

---

## Post #1 by @Jean_Jacquemier (2022-07-13 19:55 UTC)

<p>The author of a this paper (<a href="https://www.sciencedirect.com/science/article/pii/S0896627321000805" class="inline-onebox" rel="noopener nofollow ugc">Brain microvasculature has a common topology with local differences in geometry that match metabolic load - ScienceDirect</a>) published his data: a mouse brain vasculature and the transormation files needed to aligned the vasculature to an ATLAS.</p>
<p>There are 2 transformation files. I managed to apply it to the vasculature thanks to SimpleITK Python library.</p>
<p>I dit not manage to do the same with the second transformation file.</p>
<p>This second transformation is of type : ThinPlateSplineKernelTransform_double_3_3</p>
<p>I already read some subjects on this forum about this issue but none of the existing solutions seems to work in my case.</p>
<p>1/ The “standard” SimpleITK Python library ('version 2.2.0rc2) can not read the file:</p>
<p>"Could not create an instance of “ThinPlateSplineKernelTransform_double_3_3”</p>
<p>The usual cause of this error is not registering the transform with TransformFactory … "</p>
<p>The SimpleITK python package installed inside Slicer3D (Python interactor) can read it. It returns SimpleITK.SimpleITK.CompositeTransform. But the object cannot execute:</p>
<p>" Only storage methods are implemented for InverseThinPlateSplineKernelTransform"</p>
<p>2/ I managed to invert this transformation thanks to Slicer3D transform tab and save it. Then I can open it with the Python Interactor but I cannot obtain the inverse (what I need) :</p>
<p>“sitk::ERROR: Unable to create inverse!”</p>
<p>3/ I cannot load the vasculature into Slicer3D to apply the transformation because the Dataset is huge ( &gt; 20 GB)</p>
<p>4/ I tried to convert it to a displacement but without success.</p>
<p>Is there something else that I can try ? Thank you for your help, Jean</p>

---

## Post #2 by @lassoan (2022-07-13 22:56 UTC)

<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="1" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>Only storage methods are implemented for InverseThinPlateSplineKernelTransform</p>
</blockquote>
</aside>
<p>This is due to ITK’s limited support for inverted transforms. You often need a transform and the inverse of that transform, but ITK lacks two features:</p>
<ol>
<li>Save a transform and indicate with a flag that it is an inverse transform.</li>
<li>Compute inverse of a transform dynamically, at any position.</li>
</ol>
<p>We addressed (1) in Slicer by adding special “inverse” transform types (such as <code>InverseThinPlateSplineKernelTransform</code>). These transform are only used to allow reading/writing inverse transforms in ITK files. If you try to apply these inverse transform types to an image then you get an error (<code>Only storage methods are implemented for InverseThinPlateSplineKernelTransform</code>).</p>
<p>We addressed (2) in Slicer by using VTK to apply transforms to images, meshes, point lists, etc. Unlike ITK, VTK can compute inverse of a transform at any position, in real-time very robustly and efficiently (and it can even do it for composite transforms, i.e., a list of concatenated transforms).</p>
<p>If you want to do everything in ITK then you have to implement inverse transform support yourself.</p>
<p>One option is to not use <code>Inverse...Transform...</code> classes, but always store the “forward” transform and if you need an inverse transform then compute it using <code>InverseDisplacementFieldImageFilter</code>. It will be very slow and brittle, but if you only do batch processing then it may be acceptable.</p>
<p>Another option is to do something similar that Slicer does (incorporate transform direction flag in transform files and/or use VTK transforms). You can either reimplement these features or you can use Slicer’s implementation. Since Slicer can do everything out of the box, using Slicer would be probably the easiest solution, but of course it would add a dependency to your processing workflow.</p>

---

## Post #3 by @Jean_Jacquemier (2022-07-14 12:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>using Slicer would be probably the easiest solution, but of course it would add a dependency to your processing workflow.</p>
</blockquote>
</aside>
<p>Thank you for being so helpful. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Using Slicer Python API would be the perfect solution for me.<br>
I have been searching for documentation, examples or tutorials on using Slicer Python API for registration/transformation without success.</p>
<p>Could you please provide me with a link to such a material.<br>
For information, following is the SimpleITK equivalent of what I want to perform with slicer.</p>
<pre><code class="lang-auto">transform = SimpleITK.ReadTransform(path)

registered_vasculature_points = list()
for point in 3d_array.astype(np.double):
   registered_vasculature_points.append(transform.TransformPoint(point))
</code></pre>

---

## Post #4 by @lassoan (2022-07-14 15:59 UTC)

<p>You can call <code>ApplyTransform</code> method of a node to persistently modify it with a transform (corresponds to “Harden transform” on Slicer GUI).</p>

---

## Post #5 by @Jean_Jacquemier (2022-08-02 13:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>ApplyTransform</code></p>
</blockquote>
</aside>
<p>What is the Python type of the node on which I can call ApplyTranform ? vtkActor ?</p>

---

## Post #6 by @cpinter (2022-08-02 13:37 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> wrote it is a method of a MRML node.</p>

---

## Post #7 by @Jean_Jacquemier (2022-08-03 09:42 UTC)

<p>I succeed to apply the transformation (and the inverse transform btw) to a vtkMRMLScalarVolumeNode (the mrHead from the sample data).</p>
<p>But I do not figure out how to create a  vtkMRMLScalarVolumeNode from my numpy array of 3D cartesian coordiates of shape (N, 3).</p>
<p>Could you provide my any tips or clues ?</p>

---

## Post #8 by @Jean_Jacquemier (2022-08-03 11:49 UTC)

<p>I managed to create a vtkPoints and a vtkPolyData objects from my numpy 3D array.</p>

---

## Post #9 by @cpinter (2022-08-03 13:38 UTC)

<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="7" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>numpy array of 3D cartesian coordiates of shape (N, 3)</p>
</blockquote>
</aside>
<p>What do these coordinates represent exactly?</p>

---

## Post #10 by @lassoan (2022-08-03 19:33 UTC)

<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="7" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>But I do not figure out how to create a vtkMRMLScalarVolumeNode from my numpy array</p>
</blockquote>
</aside>
<p>You can add a scalar volume node to the scene and then set its voxels from a numpy array using updateVolumeFromArray (see example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">script repository</a>).</p>

---

## Post #11 by @Jean_Jacquemier (2022-08-04 05:22 UTC)

<p>A mouse brain vasculature. The numpy array of shape (N, 3) represents X,Y and Z coordinates of the nodes that owned the vasculature</p>

---

## Post #12 by @Jean_Jacquemier (2022-08-04 05:46 UTC)

<p>My dataset is quite huge (1um resolution for the full mouse brain vasculature). Thus, I cannot convert my numpy array of shape (N, 3) (representing X, Y and Z cartesian 3d coordinates of node) to a Matrix of shape (30000, 40000, 65000) like it is in the script you provided to me.<br>
Is there a slicer utility function that allows to create or fill) a VolumeNode from 3D points like for vtkPoints for example ?</p>
<pre><code class="lang-auto">    vpoints = vtk.vtkPoints()
    vpoints.SetNumberOfPoints(points.shape[0])
    for i in range(points.shape[0]):
        vpoints.SetPoint(i, points[i])
    vpoly = vtk.vtkPolyData()
    vpoly.SetPoints(vpoints)
</code></pre>

---

## Post #13 by @pieper (2022-08-04 13:34 UTC)

<p>To work with this data as a volume you could make a more manageable sized array, say 1k^3, and make a kind of histogram of the number of sample points within a given voxel.  From there you could volume render or segment the result.</p>

---

## Post #14 by @Jean_Jacquemier (2022-08-08 07:53 UTC)

<p>Thank you for your answer. If I understand correctly, this solution is a workaround to work with a huge dataset with a quite important loss of precision due to the histogram. It is well noted and I will use it if I cannot find a way to apply the transform without loss of precision.</p>
<p>1/ If I split my “huge” volume into smaller volumes that fit with my memory size and apply the full transform on every sub volume, does the resulting merge of all submodules after transformation provide a correct result ?</p>
<p>2/ ITK allows to apply a transform on 3D points with the following method (itk::simple::Transform::TransformPoint).<br>
Does a similar method exist in MRML lib ?</p>

---

## Post #15 by @mau_igna_06 (2022-08-08 08:15 UTC)

<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="14" data-topic="24299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>1/ If I split my “huge” volume into smaller volumes that fit with my memory size and apply the full transform on every sub volume, does the resulting merge of all submodules after transformation provide a correct result ?</p>
</blockquote>
</aside>
<p>Yes</p>
<blockquote>
<p>2/ ITK allows to apply a transform on 3D points with the following method (itk::simple::Transform::TransformPoint).<br>
Does a similar method exist in MRML lib ?</p>
</blockquote>
<p>Once you have created the scalar volume nodes, you will need a linear transform node to do the transformation and then harden it for each parcell… regarding your question about transforming points, you already can do this on Slicer’s python interactor:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkAbstractTransform.html#a978fb5d88da39f847dbcd562f5eaa433" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkAbstractTransform.html#a978fb5d88da39f847dbcd562f5eaa433</a><br>
using a vtkTransform and setting it’s matrixToParent</p>

---

## Post #16 by @Jean_Jacquemier (2022-08-09 11:46 UTC)

<p>After so many tested methods and readed documentation, I finally found the solution to my issue.<br>
And the solution is so simple …</p>
<p>Thank you very much lassoan, cpinter and mau_igna_06 for your time and your help.</p>
<p>The solution In a nutshell</p>
<p>1/ convert my 3d cartesian coordinate to VTK coordinate system (RAS)</p>
<p>2/ Opening my transformation file (the one that contains ThinPlateSplineKernelTransform_double_3_3 transform) with slicer.util.loadTransform() method</p>
<p>3/ Get the vtkThinPlateSplineTransform using the GetTransformFromParent() method</p>
<p>4/ Use the TransformPoint method to apply the transform on each 3D point coordinate.</p>

---

## Post #17 by @lassoan (2022-08-10 09:52 UTC)

<p>Thanks for the update. You can also achieve what you described by loading your vasculature model into a model node a s then harden the transform on the model.</p>

---
