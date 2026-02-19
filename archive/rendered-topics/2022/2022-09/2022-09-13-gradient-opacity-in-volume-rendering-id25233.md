---
topic_id: 25233
title: "Gradient Opacity In Volume Rendering"
date: 2022-09-13
url: https://discourse.slicer.org/t/25233
---

# Gradient Opacity in Volume Rendering

**Topic ID**: 25233
**Date**: 2022-09-13
**URL**: https://discourse.slicer.org/t/gradient-opacity-in-volume-rendering/25233

---

## Post #1 by @user4 (2022-09-13 08:31 UTC)

<p>Hi,all.<br>
What’s the exactly meaning of gradient here?In 2D image,gradient usually calculated with Sobel operator,with a specified kernel(convolution).However,I am not familiar with the gradient in 3D image here.While we can set control points to change opacity,I have no idea of gradient in Slicer.Can someone give some references?<br>
Thanks in advance!</p>

---

## Post #2 by @ebrahim (2022-09-13 14:25 UTC)

<p>I’m not sure what is that gradient opacity setting either-- so someone please correct me if I’m wrong-- but I imagine gradient in this context refers not to the <a href="https://en.wikipedia.org/wiki/Gradient" rel="noopener nofollow ugc">differential operator</a> but rather to the concept of a <a href="https://en.wikipedia.org/wiki/Color_gradient" rel="noopener nofollow ugc">gradual color transition</a>, or in this case a gradual opacity transition.</p>
<p>The connection is that the latter yields an image whose gradient (in the differential operator sense) is constant across the image. This idea applies to any dimension of image: 2D, 3D, etc: if your scalar image is given by <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/137a1c5ab8b236c83bae827138a74b2ec8cf97bd.png" alt="image" data-base62-sha1="2MiGY1lwpM9fM8OVxy8qI7XiB7T" width="120" height="19"> as a “gradient.”</p>

---

## Post #3 by @pieper (2022-09-13 17:54 UTC)

<p>The way I understand it is that the gradient is referring to how quickly the volume intensity changes as the ray moves through the volume.  The change (gradient) being high means you are moving from one intensity region to another at a sharp boundary.  The gradient-opacity mapping generates a scalar between 0 and 1 that allows you to control the features you see in the rendering.  By default, all gradients are mapped to 1, meaning there’s no impact on the rendering.  But if you make some lower levels of gradient map to no opacity then you can enhance the edges and make them more visible as in the examples below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9af92e4d52152be6515102408e6273fc85e8d31.jpeg" data-download-href="/uploads/short-url/sMc8ttEI8zFmQzP7WJIhVsxmqtz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af92e4d52152be6515102408e6273fc85e8d31_2_560x500.jpeg" alt="image" data-base62-sha1="sMc8ttEI8zFmQzP7WJIhVsxmqtz" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af92e4d52152be6515102408e6273fc85e8d31_2_560x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af92e4d52152be6515102408e6273fc85e8d31_2_840x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9af92e4d52152be6515102408e6273fc85e8d31_2_1120x1000.jpeg 2x" data-dominant-color="B5AEB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1536×1371 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a9982010efe4abe787714020e2a43168dc2b85d.jpeg" data-download-href="/uploads/short-url/m3Eq0nViD3IpYIeglDKJAtu3TR3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a9982010efe4abe787714020e2a43168dc2b85d_2_562x500.jpeg" alt="image" data-base62-sha1="m3Eq0nViD3IpYIeglDKJAtu3TR3" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a9982010efe4abe787714020e2a43168dc2b85d_2_562x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a9982010efe4abe787714020e2a43168dc2b85d_2_843x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a9982010efe4abe787714020e2a43168dc2b85d_2_1124x1000.jpeg 2x" data-dominant-color="B2ABAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1546×1374 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These controls are not particularly easy to use in Slicer.  You need to select point 0 and use the text input to set it to zero.  The other control points you can typically drag with the mouse.</p>

---

## Post #4 by @user4 (2022-09-14 01:05 UTC)

<p>Thanks Steve</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="25233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The way I understand it is that the gradient is referring to how quickly the volume intensity changes as the ray moves through the volume.</p>
</blockquote>
</aside>
<p>This is very similar to the concept of gradients for 2D images.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="25233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The change (gradient) being high means you are moving from one intensity region to another at a sharp boundary.</p>
</blockquote>
</aside>
<p>My ultimate goal is to calculate control points based on image gradients.Inside Slicer, is it possible to get such a 3D array about gradients, I want to quantify the gradient values, just like in a 2D image I can calculate dx and dy and then calculate the gradient magnitude.</p>

---

## Post #5 by @user4 (2022-09-14 05:14 UTC)

<p>I am not sure.But I think you may talk about the opacity not gradient.The gradient is not constant across the image but the opacity is a piecewise function and can be constant for whole image or part of the image.I think gradient is the still the largest change in each voxel and each gradient has its maginitude and orientation.</p>

---

## Post #6 by @user4 (2022-09-14 06:48 UTC)

<p>For a quick update,<br>
I am calculating and quantifying the image gradient.</p>
<pre><code class="lang-auto">from scipy import ndimage
import numpy as np

volume_node = slicer.util.getNode("vtkMRMLScalarVolumeNode1")
image = slicer.util.arrayFromVolume(volume_node)

dx = ndimage.sobel(image,0)  # x derivative
dy = ndimage.sobel(image,1)  # y derivative
dz = ndimage.sobel(image,2)  # z derivative
magnitude = np.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))  # gradient magnitude
</code></pre>
<p>Are the calculated results obtained in this way reasonable and correct?</p>

---

## Post #7 by @pieper (2022-09-14 18:46 UTC)

<p>Ah, if you want a volume of the gradient magnitude, then yes, that would be one way to do it.  I understood you to be asking how it’s done in volume rendering and what it means.  If speed is an issue this filter is probably much faster:</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkImageGradient.html#details" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkImageGradient.html#details</a></p>

---

## Post #8 by @mhalle (2022-09-14 19:02 UTC)

<p>The gradient shading parameters in volume rendering simulates the exterior surfaces of structures. It’s basically a way to fake the appearance of surfaces in a volume. If provides the color and opacity where the 3D gradient magnitude of the scalar volume is high.</p>
<p>Effectively, you’re rendering the gradient magnitude volume and compositing it with volume rendering of the underlying scalar. Using the gradient magnitude is useful when multiple layers of semi-transparent structures are desirable, since opacity doesn’t accumulate inside the enclosing volume. It can also be used to simulate, say, enamel on a tooth.</p>
<p>As you’d expect, shading the gradient magnitude may be sensitive to noisy data, though it is often effectively smoothed. Because it’s thin, it is also sensitive to sampling artifacts it the transfer functions are very abrupt.</p>
<p>—Mike</p>

---

## Post #9 by @user4 (2022-09-15 08:15 UTC)

<p>Thanks for sharing the document.<br>
After some exploration,I found <em><strong>vtkImageGradient</strong></em> compute using central differences.It is not same with the method I mentioned.So I am trying to figure out the calculation.I created a random 3D array and then use <em><strong>vtkImageGradient</strong></em>  to see the results.</p>
<pre><code class="lang-auto">import numpy as np
from numpy.random import randint
from vtk.util.numpy_support import numpy_to_vtk,vtk_to_numpy

numpy_arr = randint(0,255,[3,4,5])
--&gt; array([[[253, 164,  53,  64,  41],
        [ 55, 145,  46,  31, 220],
        [204,  37,  91, 231,  57],
        [113, 148, 185, 232, 132]],

       [[ 93, 135, 104, 127, 102],
        [117,  77,   4, 184,  24],
        [210, 100, 101,  15, 204],
        [ 94, 237, 107,  41, 234]],

       [[129, 125, 100, 160, 144],
        [  3, 206,  63, 129,  44],
        [ 29,  32, 253, 238, 248],
        [ 38, 185,  66,  82,  34]]])

# convert numpy to vtk array
vtkArr = numpy_to_vtk(numpy_arr.ravel(),deep=True,array_type = vtk.VTK_UNSIGNED_CHAR)

# since the vtkImageGradient requires a vtkDataObject
imageData = vtk.vtkImageData()
imageData.SetDimensions(numpy_arr.shape)
imageData.SetSpacing([0.1,0.1,0.1])
imageData.SetOrigin([0,0,0])
imageData.GetPointData().SetScalars(vtkArr)

# calculate the image gradient
img_grad = vtk.vtkImageGradient()
img_grad.SetInputData(imageData)
img_grad.SetDimensionality(3)
img_grad.Update()

# for checking the results
vtkDoubleArr = img_grad.GetOutput().GetPointData().GetScalars()
img_grad_numpy = vtk_to_numpy(vtkDoubleArr)
img_grad_numpy.shape   
--&gt; (60, 3)

# I suppose there are three x,y and z gradient components
Gx = img_grad_numpy[:,0]
Gy = img_grad_numpy[:,1]
Gz = img_grad_numpy[:,2]
magnitude = np.sqrt((Gx ** 2) + (Gy ** 2) + (Gz ** 2))

--&gt; '[1321.79801785, 1220.83987484,  555.4502678 ,  604.02814504,
    797.71548813,  662.94796176, 1021.10234551, 1083.52434214,
    331.3985516 ,  572.40719772, 1308.17621137,  949.01264481,
   1035.43469133,  506.31018161, 1086.69222874,  785.90711919,
    941.19604759,  301.08138435,  606.40333113,  777.38343178,
    494.59579456, 1144.49770642,  145.60219779,  351.21218658,
    882.39730281,  715.71642429,  341.50402633, 1211.45573588,
    162.01851746,  862.7861844 ,  860.88617134,  571.51115475,
    433.07043307, 1509.71851681,  828.56804186,  637.27937359,
    664.04066141, 1051.53459287,  585.57663888,  874.32831362,
    697.33420969, 1187.65525301, 1208.35632162,  541.04066391,
    528.10983706, 1153.4621797 ,  717.63500472,  874.78568804,
    841.10046962, 1200.52072035, 1049.40459309, 1610.9469265 ,
   1202.58055863,  966.04865302, 1295.76232389, 1096.51721373,
   1273.83279908,  966.29446858,  677.05243519,  805.3881052 ]'
</code></pre>
<p>However,I don’t know why the magnitude so large.It is larger than manual results.Are there any wrong steps in the above process?<br>
Since I am only interested in gradient magnitude I also saw  <em><strong>vtkImageGradientMagnitude</strong></em> .Also I used this algorithm to compute magnitude but the results are not the same with the above.</p>
<pre><code class="lang-auto">img_gra_mag = vtk.vtkImageGradientMagnitude()
img_gra_mag.SetDimensionality(3)
img_gra_mag.SetInputData(imageData)
img_gra_mag.Update()
vtk_Grad_Mag_Arr = img_gra_mag.GetOutput().GetPointData().GetScalars()
mag_numpy = vtk_to_numpy(vtk_Grad_Mag_Arr)
mag_numpy.shape
--&gt; (60,)

# have no idea why the shape is not same with original array
mag_numpy.reshape(3,4,5)
--&gt; array([[[ 41, 196,  43,  92,  29],
        [150, 253,  59,  75,  60],
        [ 28, 181,  11, 250,  62],
        [ 17, 173,  45,  94,   9]],

       [[238, 120, 145,  95, 114],
        [203,  85, 187, 162,  94],
        [ 92,  59, 177, 229,  60],
        [125, 152,  27,  73, 106]],

       [[185, 163, 184,  29,  16],
        [129, 205, 106,  73, 176],
        [ 25,  74, 178, 198,  15],
        [ 72, 249, 198, 165,  37]]], dtype=uint8)
</code></pre>
<p>While I am only caring about the whole image gradient magnitude and I don’t need Gx,Gy or Gz in different direction.So in summary,I have two questions.</p>
<ol>
<li>
<p>Why with the first method,the magnitude results are so large?</p>
</li>
<li>
<p>Why the two methods gave inconsistent results?</p>
</li>
</ol>
<p>Thanks for your continued attention and help!</p>

---

## Post #10 by @pieper (2022-09-15 13:17 UTC)

<p>Can you describe what you are trying to accomplish overall?  Here at the Slicer forum we tend to focus on solving clinical research problems and maybe we can suggest alternatives.  Debugging the math is often a part of solving clinical problems, but if you think there’s an issue with the vtk implementation of these gradient filters you could check on the vtk discourse.</p>

---

## Post #11 by @Amin_Nasim_saravi (2023-02-08 20:53 UTC)

<aside class="quote no-group" data-username="user4" data-post="9" data-topic="25233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p><code>from vtk.util.numpy_support import numpy_to_vtk,vtk_to_numpy</code></p>
</blockquote>
</aside>
<p>Hello,</p>
<p>So I’m working on a project that has to do much with the gradient opacity function. My results are not yet consistent with 3D Slicer yet. However, while working on that, I found the answer to the discrepancy you are experiencing between <code>vtkImageGradientMagnitude</code> and <code>vtkImageGradient</code>. Based on what I observed the result of <code>vtkImageGradient</code> is correct. However, to get the same effect with <code>vtkImageGradientMagnitude</code> you need to change the type of your data from <code>VTK_UNSIGNED_CHAR</code> to <code>VTK_DOUBLE</code>. As your code also shows, your result of <code>vtkImageGradientMagnitude</code> has the type of uint8 which is not a decent type when calculating gradient numerically.</p>
<p>The order point worth mentioning is, the magnitude of the gradient is big because the spacing is small. If you change <code>imageData.SetSpacing([0.1, 0.1, 0.1])</code> to <code>imageData.SetSpacing([1., 1., 1.])</code> you get smaller magnitudes.</p>
<p>Hopefully, you find this helpful.</p>

---
