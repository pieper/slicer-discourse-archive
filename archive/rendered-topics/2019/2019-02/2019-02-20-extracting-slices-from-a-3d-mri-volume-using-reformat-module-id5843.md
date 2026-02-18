# Extracting Slices from a 3D MRI volume using Reformat Module

**Topic ID**: 5843
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/extracting-slices-from-a-3d-mri-volume-using-reformat-module/5843

---

## Post #1 by @nish91 (2019-02-20 13:03 UTC)

<p>I used reformat module to fix an arbitrary plane using a normal vector and then visualized the slices by moving the plane on that normal. However, I am not able to extract all the slices from the defined plane and Reformat module only helps me in visualization of the intensities on those slices. Basically I would like to extract the slices containing the MRI intensities and store it in a 3D array for further processing. Please let me know how to solve this in 3D Slicer. Thanks<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e75028f89ba45fa0036672552ac6476d0485174.png" data-download-href="/uploads/short-url/mBM8fEMSc0YejWF0t9TshTbWyDW.png?dl=1" title="Selection_073" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e75028f89ba45fa0036672552ac6476d0485174_2_690x391.png" alt="Selection_073" data-base62-sha1="mBM8fEMSc0YejWF0t9TshTbWyDW" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e75028f89ba45fa0036672552ac6476d0485174_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e75028f89ba45fa0036672552ac6476d0485174_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e75028f89ba45fa0036672552ac6476d0485174_2_1380x782.png 2x" data-dominant-color="808093"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_073</span><span class="informations">3610×2047 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-02-20 13:36 UTC)

<p>H <a class="mention" href="/u/nish91">@nish91</a> - there isn’t a built-in operation for this, but it can be done with a little programming and linear algebra.  The Reformat operation changes the SliceToRAS matrix of the vtkMRMLSliceNode (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slice_Orientation_Presets" rel="nofollow noopener">this documentation</a> should help.  Then the information can be converted into a linear transform (maybe some modification needed) and then the volume can be resampled through the transform.  You can then access the result volume as a numpy array.</p>
<p>Another option could be to use the ScreenCapture to get s movie of the slice viewer but you’d lose the geometry information.</p>

---

## Post #3 by @lassoan (2019-02-20 14:06 UTC)

<p>You can also follow this example to get resliced image as a volume node and access it as a numpy array:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array</a></p>

---

## Post #4 by @nish91 (2019-02-20 14:51 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>  for your reply, This works for me. I would like to save this array out of 3D Slicer so that I can access the voxel in other environments. Do you know which command will do that in python interactor??</p>

---

## Post #5 by @nish91 (2019-02-20 14:53 UTC)

<p>Thanks for the reply. I will try this solution too.</p>

---

## Post #6 by @lassoan (2019-02-20 15:08 UTC)

<aside class="quote no-group" data-username="nish91" data-post="4" data-topic="5843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/da6949/48.png" class="avatar"> nish91:</div>
<blockquote>
<p>This works for me. I would like to save this array out of 3D Slicer so that I can access the voxel in other environments</p>
</blockquote>
</aside>
<p>How you are going to use the image? In what software, what programming language/environment? What format do you usually use for storing images?</p>

---

## Post #7 by @nish91 (2019-02-20 15:13 UTC)

<p>I am going to use the voxel array in Jupyter notebook and I don’t have Slicer installed in my notebook. Therefore my best bet is to extract these images out of python interactor in 3D Slicer. I will use these images to feed into a neural network. I prefer any format (such as TIFF etc) which preserves the gray scale intensities.</p>

---

## Post #8 by @lassoan (2019-02-20 15:20 UTC)

<p>Thanks for the details. To preserve all information, I would recommend to save in .nrrd format using <code>slicer.util.saveNode(volumeNode, 'c:/tmp/myvolume.nrrd')</code>.</p>

---

## Post #9 by @nish91 (2019-02-20 15:29 UTC)

<p>Thanks a lot. This works for me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #10 by @Sharada (2021-10-11 23:12 UTC)

<p>Hi Andras,</p>
<p>I am trying to achieve something similar, and the solution you recommended works fine for re-slicing images in a reformatted way, but is there a way to reformat and get voxel values for a whole volume?<br>
I saw that Steve Pieper mentioned that there is no built-in operation and a transformation might need to be created. Please let me know!</p>
<p>Thanks,<br>
Sharada</p>

---
