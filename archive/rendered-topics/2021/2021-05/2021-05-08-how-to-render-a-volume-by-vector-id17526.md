---
topic_id: 17526
title: "How To Render A Volume By Vector"
date: 2021-05-08
url: https://discourse.slicer.org/t/17526
---

# How to render a volume by vector?

**Topic ID**: 17526
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/how-to-render-a-volume-by-vector/17526

---

## Post #1 by @Raykie (2021-05-08 14:30 UTC)

<p>Generally, the volume rendering works based on the intensity of a voxel. What if I need to do it based on a vector (k1, k2)? Thanks!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f225377ad14df4947b45c7851bfd6aab3e92fb58.jpeg" alt="image" data-base62-sha1="yy7hCQmLLdhXXCv9U0gGy4iMING" width="669" height="336"></p>

---

## Post #2 by @lassoan (2021-05-10 04:44 UTC)

<p>If k1 and k2 are intensity and gradient then you can use VTK’s 2D transfer function (an image that assigns RGBA value for coordinate pairs). See description of the transfer function <a href="https://blog.kitware.com/2d-transfer-function-support-in-gpuvolumemapper/#:~:text=A%202D%20transfer%20function%20is%20defined%20as%20a,backend%29.%20More%20information%20can%20be%20found%20in%20TestGPURayCastTransfer2D">here</a>. You can set the 2D transfer function by typing this into the Python console:</p>
<pre><code class="lang-python">slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLVolumePropertyNode").GetVolumeProperty().SetTransferFunction2D(image)
</code></pre>
<p>If k1 and k2 are arbitrary scalar components then you can apply your 2D transfer function to the volume to get an RGBA volume (e.g., using numpy) and use that as input for volume rendering.<br>
To render an RGBA volume, you need to <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6">turn off independent component volume property option</a>).</p>

---

## Post #3 by @Raykie (2021-05-19 10:00 UTC)

<p>Really thanks for your reply! I followed your suggestion but failed to render the RGBA volume.</p>
<p>The k1 k2 volume shape is (128, 128, 112), so I simply generate a new volume whose shape is (128, 128, 112, 4) by following codes, and saved it as a NIfTI file:</p>
<pre><code class="lang-auto">    arrRGBA = np.empty(arrk1.shape+(4,), dtype=np.float)
    arrRGBA[..., 0] = ((arrk1-k1min)/(k1max-k1min)) * 255
    arrRGBA[..., 1] = ((arrk2-k2min)/(k2max-k2min)) * 255
    arrRGBA[..., 2] = np.zeros(arrk1.shape, dtype=np.float)
    arrRGBA[..., 3] = ((arrGrad-gradMin)/(gradMax-gradMin)) * 1
</code></pre>
<p>Then I turn off the independent component volume property option by copy-pasting your code:<br>
<code>getNode('VolumeProperty').GetVolumeProperty().SetIndependentComponents(0)</code></p>
<p>As a result, it still rendered it as scalar rather than a RGBA volume. I think I must be wrong with something but I am not sure.</p>
<p>Any way, thanks very much!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f5a4674abd225ebe5c61f5f811b5ce4ad359a6.jpeg" data-download-href="/uploads/short-url/eghyrAftgylFyci7HbhXvcSCSbQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63f5a4674abd225ebe5c61f5f811b5ce4ad359a6_2_690x333.jpeg" alt="image" data-base62-sha1="eghyrAftgylFyci7HbhXvcSCSbQ" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63f5a4674abd225ebe5c61f5f811b5ce4ad359a6_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63f5a4674abd225ebe5c61f5f811b5ce4ad359a6_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63f5a4674abd225ebe5c61f5f811b5ce4ad359a6_2_1380x666.jpeg 2x" data-dominant-color="8D8E9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×929 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-05-19 12:10 UTC)

<p>I would recommend to first try the method that I linked above that worked for many people. Then, you can compare the volume that works with the one that you generate using numpy. If volume dimensions, scalar type, etc. are all the same then probabably the issue is how you configure volume rendering.</p>
<p>If you share an example nifti volume that you generate then I can have a quick look, too.</p>

---

## Post #5 by @Raykie (2021-05-19 12:24 UTC)

<p>Here is the link for downloading. Thanks!<br>
<a href="https://drive.google.com/file/d/1J7MO-z5FYlnk12rCI-SXu7n5nSCg6-a9/view?usp=sharing" rel="noopener nofollow ugc">Example nifti volume</a></p>

---

## Post #6 by @lassoan (2021-05-19 15:53 UTC)

<p>Slicer loads this volume as a single-component scalar volume.</p>
<p>It may be because it has wrong data type: it uses datatype=64 (double) instead of 2304 (RGBA). RGBA volumes must use 8 bits for each component. If you fix these issues and Slicer still loads the volume as a single-component scalar volume then you can save the volume in nrrd file instead, or don’t save it to file and load it update a volume with the new voxel array, or use VTK filters as in the example linked above.</p>

---

## Post #7 by @Raykie (2021-05-28 08:33 UTC)

<p>I transfer the dtype to 8 bits unsigned integer and saved it as Nrrd file, but the result is not as expected. Slicer still renders it as single component scalar volume.</p>
<p>I put the Nrrd file <a href="https://drive.google.com/file/d/1n9cIxJ76jxM9GAKQi1tiY7vLTL3v8Q6-/view?usp=sharing" rel="noopener nofollow ugc">here</a> so that you can check it if you are free.</p>
<p>Thanks for all the help!</p>

---
