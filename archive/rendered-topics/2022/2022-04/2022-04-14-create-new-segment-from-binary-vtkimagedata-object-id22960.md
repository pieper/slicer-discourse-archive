# Create new segment from binary vtkimagedata object

**Topic ID**: 22960
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/create-new-segment-from-binary-vtkimagedata-object/22960

---

## Post #1 by @Haytham (2022-04-14 10:21 UTC)

<p>Hello,<br>
I create a 3D vtkImageData objet using this code:</p>
<p>``<br>
<strong>vtkNew imageTumor;</strong><br>
**  imageTumor-&gt;SetExtent(0, 100, 0, 100, 0, 100);**<br>
**  imageTumor-&gt;AllocateScalars(VTK_DOUBLE, 1);**<br>
**  imageTumor-&gt;SetSpacing(1.5, 2.25, 8);**<br>
**  imageTumor-&gt;SetOrigin(0.0, 0.0, 0.0);**<br>
**  int* extent = imageTumor-&gt;GetExtent();**</p>
<pre><code class="lang-auto">
And I inisilize this image by 0 and 1 depending on a certain conditions,  using this code:

</code></pre>
<p><strong>for (int x = extent[0]; x &lt; extent[1]; x++)</strong><br>
**  {**<br>
**    for (int y = extent[2]; y &lt; extent[3]; y++)**<br>
**    {**<br>
**      for (int z = extent[4]; z &lt; extent[5]; z++)**<br>
**      {**<br>
**        if(imageMTT-&gt;GetScalarComponentAsDouble(x, y, z, 0)&gt;150)**<br>
**          imageTumor-&gt;SetScalarComponentFromDouble(x, y, z, 0, 1.0);**<br>
**        else**<br>
**          imageTumor-&gt;SetScalarComponentFromDouble(x, y, z, 0, 0.0);**<br>
**      }**<br>
**    }**<br>
**  }**</p>
<pre><code class="lang-auto">
the question is how can visualize this image? i don't know if we can transform a vtkimagedata ona segment. any ideas to help me.
thanks</code></pre>

---

## Post #2 by @lassoan (2022-04-14 12:46 UTC)

<p>You can import a vtkImageData into a vtkMRMLSegmentationNode using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#afd85ead2153b7e973600f0b27b0583cd">ImportLabelmapToSegmentationNode</a> method.</p>
<p>A small comment: <code>GetScalarComponentAsDouble</code> is intended for testing or get/set single values in a volume. It is not intended for filling an entire volume. It may be 10x or more slower than using VTK image filters or iterating through an image using a pointer. The loop in the example above is also much slower because the hottest loop jumps between slices instead of processing neighbor voxels (<code>for (int x... for (int y... for (int z...</code> should be changed to <code>for (int z... for (int y... for (int x...</code>). Processing all voxels in a single thread also slows down the operation. I would recommend to either learn more about how to implement image processing filters or use existing VTK filters to achieve reasonable processing speed. If you describe the processing you want to do (<code>initialize this image by 0 and 1 depending on a certain conditions</code>) then we may give advice on how to fill the volume more efficiently.</p>

---

## Post #3 by @Haytham (2022-04-14 13:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>all voxels in a single thread</p>
</blockquote>
</aside>
<p>thanks for your responce and the important comment</p>
<p>I try to select the value of Perfusion parameters (MTT, TPP, rCBV, rCBF) from a vtkImageData object. And depending on those parameters, Idecide whether this voxel contains tumors or not.<br>
After this, we obtain a vtkImagedata object (0 or 1)  I need to visualize this object…<br>
thanks</p>

---

## Post #4 by @mau_igna_06 (2022-04-14 13:46 UTC)

<p>I believe you could use simpleITK for creating the label map from a numpy array. Should be easier I think.</p>
<p>Hope it helps</p>

---

## Post #5 by @lassoan (2022-04-14 17:07 UTC)

<p>I agree that it would make sense to start prototyping in Python and then if you need better speed then vectorize the code and/or port slowest parts to C++.  By “vectorizing” the operations I mean process an entire line, slice, or volume of voxels at a time (using numpy, ITK, or other tools) then you may be able to implement the whole computation in Python.</p>
<p>Note that there have been previous projects for processing time-resolved images, such <a href="https://github.com/QIICR/PkModeling">PK modeling extension</a> for analyzing DCE-MRI.</p>
<p>I’m not sure if there are CT perfusion modeling extensions (or algorithms that could be easily converted to extensions) for computing MTT, TP, rCBV, rCBF. <a class="mention" href="/u/fedorov">@fedorov</a> has features like this been developed as part of the QIICR project?</p>

---

## Post #6 by @fedorov (2022-04-14 20:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="22960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure if there are CT perfusion modeling extensions (or algorithms that could be easily converted to extensions) for computing MTT, TP, rCBV, rCBF. <a class="mention" href="/u/fedorov">@fedorov</a> has features like this been developed as part of the QIICR project?</p>
</blockquote>
</aside>
<p>No, nothing like that was done in QIICR. There is also this relevant extension, but it is for PET: <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Modules/dPetBrainQuantification" class="inline-onebox">Documentation/Nightly/Modules/dPetBrainQuantification - Slicer Wiki</a>.</p>

---
