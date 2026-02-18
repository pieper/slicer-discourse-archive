# How to apply different kernels to different areas of an image using deconvolution process?

**Topic ID**: 4922
**Date**: 2018-12-01
**URL**: https://discourse.slicer.org/t/how-to-apply-different-kernels-to-different-areas-of-an-image-using-deconvolution-process/4922

---

## Post #1 by @shahrokh (2018-12-01 10:02 UTC)

<p>Hi Dear developers and users</p>
<p>I have a image that has degraded its quality due to blurring. The blurring process can be modelled as degradation function. The amount of blurring (degradation function) varies in different areas of the image.<br>
Also suppose that I have knowledge about these degradation functions (kernels) as following:</p>
<p>For pixel value equal to 10 → kernel1<br>
For pixel value equal to 20 → kernel2<br>
For pixel value equal to 30 → kernel3<br>
…<br>
For pixel value equal to 100 → kernel10</p>
<p>These kernels are 20x20 pixels in size. Now, I want to apply these kernels to the image depending on the pixel values of the image through deconvolution process. The kernel is selected depending on the pixel value of the image. For pixel values of an image whose kernels are not available, I can interpolate them using existing kernels. I expect that this process improves the quality of the image.<br>
I know there are some deconvolution filters in “itk SimpleFilters” module, but I think that all these filters apply a specific kernel over the entire image (unlike my case that I want to apply different kernels to different areas of image).</p>
<p>At now, my main problem is that how can I apply these kernels on different areas based on pixel values of image?<br>
What is the solution to do this?</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2018-12-01 15:25 UTC)

<p>I don’t know of existing code that does just what you describe, but it sounds like you could implement that pretty easily (sounds like you know exactly what you need it to do).  If you aren’t concerned about speed, probably the easiest is to do it in python by accessing the image data as a numpy array.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<p>If performance is an issue, then you can write C++ code for it, but that’ll require compiling and adds complexity.</p>

---

## Post #3 by @lassoan (2018-12-01 15:35 UTC)

<p>You can also perform the filtering with 10 different kernels on the entire image, then use numpy array operations to combine the 10 processed image into 1 (see a simple example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" rel="nofollow noopener">here</a>).</p>

---

## Post #4 by @shahrokh (2018-12-04 12:26 UTC)

<p>Thank you very much for your guidance and links you sent to me.</p>
<p>Andras pointed out that <em>I perform the filtering with 10 different kernels on the entire image and then combine 10 processed image to 1</em>.</p>
<p>Can this be equivalent to getting an average of ten kernels and then filtering with the resulting kernel (averaged kernel) on the entire image? I’m not really sure that this is true in my case.</p>
<p>I think the result of this proposed solution (by Andras) is different with what I apply different kernels in different areas of the image.</p>
<p>Please guide me further.<br>
Shahrokh</p>

---

## Post #5 by @lassoan (2018-12-04 13:34 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="4" data-topic="4922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Can this be equivalent to getting an average of ten kernels and then filtering with the resulting kernel (averaged kernel) on the entire image? I’m not really sure that this is true in my case.</p>
</blockquote>
</aside>
<p>You don’t average kernels but instead apply the candidate kernels one by one on the original image. Then in the final image you choose voxel value from one of the processed images, based on what was the intensity in the original image.</p>
<p>For certain kernel types (e.g., Gaussian smoothing) you can get magnitudes faster speeds and very similar results if you use an image pyramid (you apply filtering on the result of previous filtering).</p>

---
