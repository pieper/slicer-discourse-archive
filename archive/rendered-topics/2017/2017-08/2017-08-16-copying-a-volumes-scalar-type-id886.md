# Copying a volume's scalar type

**Topic ID**: 886
**Date**: 2017-08-16
**URL**: https://discourse.slicer.org/t/copying-a-volumes-scalar-type/886

---

## Post #1 by @moselhy (2017-08-16 23:50 UTC)

<p>How do I copy just the image information from a Scalar Volume Node “<code>originalNode</code>” to a new node initialized by <code>newnode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')</code>?</p>
<p>The problem with <code>newnode.Copy(originalNode)</code> is that it also copies the Scalar Type, which is too finicky to change, and it seems to round down the <code>Image Origin</code> and has an extra decimal place in <code>Image Spacing</code>. This causes the sequence to only store as a “Medical Reality Bundle” when I want it to save as a <code>.seq.nrrd</code> file.</p>
<p>I <a href="https://github.com/moselhy/SlicerSequenceRegistration/commit/8b053feedb1b0f7b6a11fa1b10451ecdaf71094c" rel="nofollow noopener">committed a temporary fix where it still registers with the fixed and moving volume being the same</a>, but it is a little time consuming.</p>

---

## Post #2 by @lassoan (2017-08-17 02:15 UTC)

<p>Image geometry (origin, spacing, axis directions) are stored in the IJK to RAS (voxel to physical space transformation) matrix. You can copy that information like this:</p>
<pre><code>ijkToRas = vtk.vtkMatrix4x4()
sourceVolume.GetIJKToRASMatrix(ijkToRas)
targetVolume.SetIJKToRASMatrix(ijkToRas)</code></pre>

---

## Post #3 by @moselhy (2017-08-17 18:03 UTC)

<p>Thanks, then what do I do to copy the signal intensities over without copying the scalar type?</p>

---

## Post #4 by @lassoan (2017-08-17 18:47 UTC)

<p>The problem seems to be that Elastix does not set IJKToRAS matrix of the resampled moving volume accurately. We should confirm this and report to Elastix developers, but until then we can apply the workaround of overwriting IJKToRAS of all the registered volumes to be exactly the same as the fixed volume’s IJKToRAS.</p>
<p>Does Elastix change the scalar type as well? If yes, then the simplest solution is probably to use vtkImageCast filter to set it to the same as the fixed volume’s scalar type.</p>

---

## Post #5 by @moselhy (2017-08-18 19:19 UTC)

<p>Yes, Elastix changes the scalar type.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the simplest solution is probably to use vtkImageCast filter to set it to the same as the fixed volume’s scalar type</p>
</blockquote>
</aside>
<p>Would this be any faster than registering the fixed volume with itself?</p>

---

## Post #6 by @lassoan (2017-08-18 19:56 UTC)

<p>Yes, copying and casting a volume is much faster. Do not register a volume to itself, as the result may not be always identical.</p>

---

## Post #7 by @moselhy (2017-08-18 20:20 UTC)

<p>Thank you, how do I copy and cast the volume <code>inputvol</code> with scalar type <code>int</code> to <code>outputvol</code> with scalar type <code>short</code>?</p>

---

## Post #8 by @lassoan (2017-08-18 21:02 UTC)

<p>VolNode-&gt;GetImageData() =&gt; cast filter =&gt; VolNode-&gt;SetAndObserveImageData()</p>

---

## Post #9 by @moselhy (2017-08-21 15:17 UTC)

<p>Thank you, here is the full code for anyone wanting to change the scalar volume type of a volume node <code>volumeNode</code>:</p>
<pre><code>imageCast = vtk.vtkImageCast()
imageCast.SetInputData(volumeNode.GetImageData())
# This could be substituted by SetOutputScalarTypeToX where X is the desired type
imageCast.SetOutputScalarTypeToShort()
imageCast.Update()
volumeNode.SetAndObserveImageData(imageCast.GetOutput())</code></pre>

---
