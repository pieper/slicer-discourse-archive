# Push 2D slice to slice view

**Topic ID**: 27738
**Date**: 2023-02-10
**URL**: https://discourse.slicer.org/t/push-2d-slice-to-slice-view/27738

---

## Post #1 by @Karthik (2023-02-10 07:03 UTC)

<p>Hi all. I am writing a scripted module in python.</p>
<p>I have multiple 2d numpy arrays. Each array represents a slice (in paraview terms) of a volume. I have calculated internally the origin, orientation of each slice. I would like to push each of these slices to a SliceView. The slices are not necessarily continuous. Slices have different centers and orientations. Also, I would like them to be visible in 3D view. In SliceView, I should be able to look at the pixels and their values (using DataProbe). But, in 3D view, I want the plane to be oriented properly according to the orientation I give it (like in vtkOrientedImageData). I was wondering how to go about this.</p>
<p>Currently, I am converting 2d numpy array to 3d numpy array by reshaping and adding another dimension. Then, I create itk image from it and then use ‘sitkUtils.PushVolumeToSlicer’ to then push the image to slicer. However, I have to do this again for every slice ( i have more than 200 slices. This will create 200 volumes). Is there a way to push 2d array to slice view directly (first converting it to vtk or itk image of course) and connect it with 3d view also?</p>

---

## Post #2 by @lassoan (2023-02-11 20:09 UTC)

<p>We usually store series of 2D image slices that move freely in 3D space (such as tracked free-hand ultrasound image acquisitions) in a sequence node. You can browse and replay these sequences very conveniently using Sequences module. You can show a moving slice in 3D views using Volume Reslice Driver module. Check out <a href="https://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> for more details.</p>

---

## Post #3 by @Karthik (2023-02-17 03:02 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , using sequence node and sequences module seems like it would work well for me.<br>
I am slightly confused about how to push a volume to slicer through python code that is rotated at an arbitrary angle. Normally, the way I push volume is using ‘sitkUtils.PushVolumeToSlicer’.</p>
<ol>
<li>
<p>Do I do the same thing when creating a volumeNode from a numpy array and use SequenceNode.SetDataNodeAtValue?</p>
</li>
<li>
<p>How would I push an arbitrarily rotated volume to mrmlScene? Normally, when I use ‘sitkUtils.PushVolumeToSlicer’, it takes an itk image as input. But as far as I know, only vtkOrientedImageData allows to set arbitrary angle. Is there something similar I can do for an itk image? Basically, my question is: what is the best way to create an image from numpy array whose center, orientation are known and push it to mrmlScene (either directly as a vtkMRMLScalarVolume Node or as part of a SequenceNode using python?</p>
</li>
</ol>

---

## Post #4 by @lassoan (2023-02-17 04:38 UTC)

<p>Your can set arbitrary origin, spacing, and axis directions in an ITK image. When you push that image into Slicer then these information are preserved.</p>

---

## Post #5 by @Karthik (2023-02-21 07:11 UTC)

<p>Is it possible to derive axis direction matrix from plane normal?<br>
I have a plane. I know the x,y,z components of the normal unit vector. Is it possible to derive 3d direction cosine matrix from it? I need to set this matrix for itk image before I push to Slicer</p>

---

## Post #6 by @Karthik (2023-02-27 08:36 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I have used vtkImageReslice to derive a 2d slice at required angle given by the direction cosine matrix.<br>
The direction cosine matrix used is row-wise direction cosine vectors. [[d_cosine1],[d_cosine2],[d_cosine_normal]]</p>
<p>I now have the slice I want to push to Slicer. I am first converting this into itk image. Because then I can use sitk.PushVolumeToSlicer(). I set the origin, spacing, direction through python code and push it to slicer. However, the orientation of that slice is not exactly what I want. Its direction is not aligning with what I expect.<br>
These are some questions I have regarding direction matrix of itk image.</p>
<ol>
<li>itk_image.SetDirection(). This direction matrix is column-wise vector?<br>
[[d_cosine1][d_cosine2][d_cosine_normal]].T ?</li>
<li>Is there any transformation I have to do to convert LPS to RAS so that it matches in 3D space correctly? I have gone through the following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>. But, I may have misunderstood it.</li>
</ol>
<p>The direction matrix I have to set for an itk image, is it not the same as that I have used in vtkImageReslice?</p>
<p>I basically want it to match properly in 3d space. The information available with me are the direction cosines used to derive the slice from vtkImageReslice.</p>
<p>For example, my current direction cosines are:<br>
d_cosine1 = [-0.20142868 -0.51576966 -0.8327114 ]<br>
d_cosine2 = [ 0.8410469  0.3446795 -0.4169346]<br>
d_cosine_normal = [ 0.50232667 -0.7836509   0.36545756]</p>
<p>For input to vtkImageReslice, I have used,<br>
direction_matrix = [d_cosine1, d_cosine2, d_cosine_normal]<br>
How would I go about the same when I need to get direction input for itk image. Finally, I want to do this:<br>
itk_image.SetDirection(direction)</p>

---

## Post #7 by @lassoan (2023-03-27 18:36 UTC)

<p>In Slicer, after the image is read into memory the index to physical transformation matrix must be IJKtoRAS (not IJKtoLPS). If you print this matrix to the Python console then the columns will be I, J, K axis vectors and origin in RAS coordinate system.</p>

---
