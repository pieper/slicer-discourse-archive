---
topic_id: 20674
title: "How To Save The Volume Pixel Data In Display Area"
date: 2021-11-18
url: https://discourse.slicer.org/t/20674
---

# How to save the volume pixel data in display area?

**Topic ID**: 20674
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/how-to-save-the-volume-pixel-data-in-display-area/20674

---

## Post #1 by @user4 (2021-11-18 03:31 UTC)

<p>Hi all, i am new to this open source software. Here is the thing i want to do.</p>
<p>1.Open a volume, in volume rendering module,we can see an opaque cube（300x300x400 volume pixel）<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a133e69377bbd8d4360e35a821248d1c871462d3.png" data-download-href="/uploads/short-url/n044iYy8qqHGloiaAiFxm2KOWbN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133e69377bbd8d4360e35a821248d1c871462d3_2_567x500.png" alt="image" data-base62-sha1="n044iYy8qqHGloiaAiFxm2KOWbN" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133e69377bbd8d4360e35a821248d1c871462d3_2_567x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a133e69377bbd8d4360e35a821248d1c871462d3_2_850x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a133e69377bbd8d4360e35a821248d1c871462d3.png 2x" data-dominant-color="979AC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1012×891 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>
<p>Use kinds of filters to make the image in the cube clear<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a00bc11d37c6e312fe1b7a82962643cf1e6ffc60.png" data-download-href="/uploads/short-url/mPPzT7msUroS3GfNED5iOM2oq8E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00bc11d37c6e312fe1b7a82962643cf1e6ffc60_2_690x310.png" alt="image" data-base62-sha1="mPPzT7msUroS3GfNED5iOM2oq8E" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00bc11d37c6e312fe1b7a82962643cf1e6ffc60_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00bc11d37c6e312fe1b7a82962643cf1e6ffc60_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00bc11d37c6e312fe1b7a82962643cf1e6ffc60_2_1380x620.png 2x" data-dominant-color="C0C4E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×864 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Now,we need to save the image in the display area,that is processed image.Click the save button,however the .vtk format file is still the raw data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f12d67247215fe38d1ee2b9f2fb84dbf1d49b65.png" data-download-href="/uploads/short-url/6IqNDIZhTwl3HGbqfH1FLE26jc1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f12d67247215fe38d1ee2b9f2fb84dbf1d49b65_2_690x153.png" alt="image" data-base62-sha1="6IqNDIZhTwl3HGbqfH1FLE26jc1" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f12d67247215fe38d1ee2b9f2fb84dbf1d49b65_2_690x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f12d67247215fe38d1ee2b9f2fb84dbf1d49b65_2_1035x229.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f12d67247215fe38d1ee2b9f2fb84dbf1d49b65_2_1380x306.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1811×404 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>I think the processed image in display area is available in some RAM memory.So, is there any way to save the new values of voxel instead of the sequence of opacity filters that we applied to change the image(Scene).<br>
By the <em>slicer.util</em> based on <em>python</em>, I can use the <em>getNode</em> and <em>arrayFromVolume</em> method to get the raw data(three dimensional numpy array).Sadly, I haven’t find any existing interface to access the display area data.<br>
Alternatively can I access display graphical card memory and save that information in the same *vtk format typical for 3D images?But I prefer to save the pixel value array directly if possible.</p>
<p>I will be very grateful if anyone can give me any possible advice <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2021-11-18 14:25 UTC)

<p>Do you just need an image of it for display?  If so you can use the ScreenCapture module to get images or a movie of the rendering.</p>

---

## Post #3 by @user4 (2021-11-19 09:48 UTC)

<p>Actually not, what I need is the new pixel value data after mapping.</p>

---

## Post #4 by @lassoan (2021-11-19 13:22 UTC)

<p>The original voxels are never converted, only the sampled values along the viewing ray. Samples can be more or less dense than the original spacing, rays are usually terminated before getting across the whole volume, and you don’t need huge extra storage to store the transformed samples, so generally you would not want to transform each original voxel value.</p>
<p>If you want to do it anyway, then you can compute lookup tables from the scalar opacity, color, gradient opacity transfer functions (available in the volume property node) and apply the lookup tables using numpy (<code>np.take</code>).</p>

---

## Post #5 by @user4 (2021-11-30 02:53 UTC)

<p>Thank you very much for your ideas.<br>
Just to make sure,what I am interested in is the post-image processed volume (and not necessarily the projected/displayed 2D image as seen on the screen)<br>
I may have said what I need is the data in the display area but that was insinuating the whole 3D volume and not the 2D projection.</p>

---

## Post #6 by @lassoan (2021-11-30 03:47 UTC)

<aside class="quote no-group" data-username="user4" data-post="5" data-topic="20674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p>what I am interested in is the post-image processed volume</p>
</blockquote>
</aside>
<p>No post-processing is performed on the volume, as it would slow down the volume rendering and/or decrease the rendered image quality. All the transfer functions are applied during raycasting on the resampled voxels on-the-fly.</p>

---

## Post #7 by @user4 (2021-12-07 03:06 UTC)

<p>Thank you very much for your reply again,<br>
So, if I want to save the post-processed image data, I have to compute the look-up tables and apply them to the volume data, is that right?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd254cb75c67b8d61fba7dc0b5ea4817f688b488.png" data-download-href="/uploads/short-url/vylqYInB9tYzwOQuNqcwNYPWtAY.png?dl=1" title="d074b6c366c2cbecda4111f1c4beda7.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd254cb75c67b8d61fba7dc0b5ea4817f688b488_2_493x51.png" alt="d074b6c366c2cbecda4111f1c4beda7.png" data-base62-sha1="vylqYInB9tYzwOQuNqcwNYPWtAY" width="493" height="51" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd254cb75c67b8d61fba7dc0b5ea4817f688b488_2_493x51.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd254cb75c67b8d61fba7dc0b5ea4817f688b488_2_739x76.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd254cb75c67b8d61fba7dc0b5ea4817f688b488_2_986x102.png 2x" data-dominant-color="3D474C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">d074b6c366c2cbecda4111f1c4beda7.png</span><span class="informations">1607×166 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have seen the volume property node in the scene.mrml. What do the lookup tables from transfer functions exactly mean? Or say ,how to compute the lookup tables?</p>
<p>Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; 于2021年11月30日周二 11:47写道：</p>

---

## Post #8 by @lassoan (2021-12-07 04:05 UTC)

<p>The transfer functions simply assign an opacity or an RGB triplet to a voxel intensity value; or an opacity value to a voxel gradient value. They can be internally implemented as piecewise linear functions or discretized lookup tables. The <a href="https://gitlab.kitware.com/vtk/textbook/raw/master/VTKBook/VTKTextBook.pdf">VTK textbook</a> describes this in great detail.</p>

---

## Post #9 by @user4 (2021-12-14 11:00 UTC)

<p>THX Andras again.<br>
I have downloaded and seen the textbook and I found the theory is much richer than practice.Are there any programming-related document? I also have seen some official documentation and find something.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce69d0637f947321fff34857588b755dc29c29d2.png" data-download-href="/uploads/short-url/ts13ZyyL97YI8ZMocl9TO33bgl4.png?dl=1" title="6809fcd8c4e3fb889060d0068d246f4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce69d0637f947321fff34857588b755dc29c29d2_2_690x138.png" alt="6809fcd8c4e3fb889060d0068d246f4" data-base62-sha1="ts13ZyyL97YI8ZMocl9TO33bgl4" width="690" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce69d0637f947321fff34857588b755dc29c29d2_2_690x138.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce69d0637f947321fff34857588b755dc29c29d2_2_1035x207.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce69d0637f947321fff34857588b755dc29c29d2_2_1380x276.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6809fcd8c4e3fb889060d0068d246f4</span><span class="informations">1641×329 38.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But there is no detail.</p>

---

## Post #10 by @lassoan (2021-12-14 13:53 UTC)

<p>Why would you like to apply these transfer functions? If the goal is rendering, such preprocessing would increase memory requirements, slow down the rendering, and potentially reduce rendering quality (because you would need to interpolate RGBA voxels instead of scalar values). If the goal is further processing then probably you don’t want to apply color mapping.</p>
<p>Can you describe your end goal?</p>

---

## Post #11 by @user4 (2021-12-15 02:43 UTC)

<p>Thanks Andras.<br>
Please let me describe the thing in detail.<br>
The voxel data from visualization is the first step,let me call the data <em><strong>new volume</strong></em>.<br>
The new volume is created based on transfer functions in volume rendering.<br>
Then we create <em><strong>mask</strong></em>,<em><strong>mask</strong></em> = threshold(new volume)<br>
In the end,we create <em><strong>final volume</strong></em>,<em><strong>final volume</strong></em> =mask * original volume<br>
These final 3D volumes can be manipulated for functional and molecular imaging.<br>
So the data in the volume rendering is fundamental to us.According your reply,there is no visualization data because all the transfer functions are applied during raycasting on the resampled voxels on-the-fly.<br>
That’s why I want to do volume rendering outside ourselves or maybe you can have more convenient way to do it?<br>
Thank you again for your continued attention to this issue.</p>

---

## Post #12 by @lassoan (2021-12-15 03:48 UTC)

<p>You can threshold the volume, apply mask, rescale or apply any arithmetic operations simply by getting the voxels as a numpy array and modify them. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">script repository</a>. You can then display the resulting volume using volume rendering.</p>

---

## Post #14 by @user4 (2021-12-17 12:51 UTC)

<p>Thanks Andras.<br>
I have looked this script repository carefully and searched some examples.But I am stucked with this situation now：<br>
I have successfully get the raw voxel data in 400x300x300 numpy array as follows：<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13828cfa9de9e964fdba7e1da2480a57b929606.png" data-download-href="/uploads/short-url/phKPF5mvc2IRc2U92eN5Phf4O5o.png?dl=1" title="b44080a8e63ef84fdf612479356d66d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13828cfa9de9e964fdba7e1da2480a57b929606_2_690x83.png" alt="b44080a8e63ef84fdf612479356d66d" data-base62-sha1="phKPF5mvc2IRc2U92eN5Phf4O5o" width="690" height="83" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13828cfa9de9e964fdba7e1da2480a57b929606_2_690x83.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b13828cfa9de9e964fdba7e1da2480a57b929606_2_1035x124.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13828cfa9de9e964fdba7e1da2480a57b929606.png 2x" data-dominant-color="F7F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b44080a8e63ef84fdf612479356d66d</span><span class="informations">1309×159 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then I defined the transfer functions including color,scalar opacity and gradient opacity as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ad7150c0e04cac169c4099612684e316ee74920.png" data-download-href="/uploads/short-url/ff9qfvjlSKOJILjmglv191ehGiA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ad7150c0e04cac169c4099612684e316ee74920.png" alt="image" data-base62-sha1="ff9qfvjlSKOJILjmglv191ehGiA" width="690" height="205" data-dominant-color="EBEFED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1016×302 9.15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a27e72d5e923c135a56a7021af6e00a6812c3cf3.png" alt="image" data-base62-sha1="nbugqO5NxgKLJR6jLXRr5NLQDCP" width="553" height="190"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d0cc6fd10f9aa00b04d6b0e8b42b1d4c36fe88c.png" alt="image" data-base62-sha1="8I4v3AEhih4xXnVvfKRb1A0TOdm" width="558" height="182"><br>
Then set the VolumeProperty node as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab292ba8c8170eee34e6350423d0fcf515efacbf.png" alt="image" data-base62-sha1="oq9R0lX9H858wx8sFnKNOr3s7vN" width="589" height="99"><br>
Now,how can I apply this VolumeProperty node to VolumeNode in order to change the voxel values?</p>

---

## Post #15 by @lassoan (2021-12-17 13:59 UTC)

<p>By setting these transfer functions in the <a href="http://apidocs.slicer.org/master/classvtkMRMLVolumePropertyNode.html#a86357bd3b43089f0d11bd55d110b91f0">VolumeProperty in a volume property node</a> will not change voxel values. It will only change the pixels of the rendered 2D image.</p>
<p>Modifying voxels should not be necessary. If you feel that you need to change all the voxel values of the 3D volume then your implementation is most likely not optimal.</p>
<p>However, if you want to do this anyway, then you can use<br>
<a href="https://vtk.org/doc/nightly/html/classvtkImageMapToColors.html">vtkImageMapToColors</a> to map scalar values to RGBA values, using the transfer functions. The filter takes only a single transfer function, so you need to fuse the scalar opacity and color transfer functions into a function. If you want to apply gradient opacity then you need to compute the image gradient and combine it with the existing RGBA volume (you can probably do that by getting the RGBA volume and the gradient opacity mapped volume as numpy arrays and apply element-wise multiplication).</p>

---

## Post #16 by @user4 (2021-12-20 02:35 UTC)

<p>Thanks Andras.<br>
I have come out an alternative possible method to save the visualization data using the ScreenCapture Module：</p>
<ol>
<li>
<p>Choose a dimension to slice (for example Axial or XZ) and start with the first slice.</p>
</li>
<li>
<p>Start recording (or screenshot) from start/0 to the end of length/dimension and stack them in-sequence to re-create the volume.</p>
</li>
</ol>
<p>Do you think it is feasible or maybe easier compared to code transfer functions?</p>

---

## Post #17 by @lassoan (2021-12-20 03:12 UTC)

<p>Screen capture module is good for getting images for publications or presentations.</p>
<p>If you need colored slices for volumetric 3D printing then you can use the <a href="https://github.com/SlicerFab/SlicerFab">SlicerFab extension</a>, which uses the current volume rendering transfer functions.</p>
<p>We cannot help you very effectively here without knowing what your end goal is (what you want to ultimately achieve).</p>

---

## Post #18 by @user4 (2021-12-20 08:05 UTC)

<p>Thanks Andras.<br>
What we actually need is oxygen saturation (SO2) from vessels.<br>
We need the rendered data as a clean mask and element-wise multiply the raw volume in order to get the cleaned volume without unnecessary parts inside and so that we can observe the oxygen saturation (SO2).</p>

---

## Post #19 by @user4 (2021-12-21 06:35 UTC)

<p>I have checked this extension and I have used this tool to slice my rendered volume.<br>
If I put all these slices into Matlab and stack over in order, does this mean I get the volume rendered voxel array data since the SlicerFab uses the volume rendering transfer functions.</p>

---

## Post #20 by @pieper (2021-12-21 13:05 UTC)

<p>Don’t use SlicerFab if your goal is to quantify the resulting images because SlicerFab uses the output of volume rendering, and that introduces. nonlinearities such as transfer functions and lighting.  For quantitative imaging it’s better to work with the raw pixel values, for example, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-reformatted-image-from-a-slice-viewer-as-numpy-array">using numpy</a>.</p>

---

## Post #21 by @user4 (2021-12-22 03:51 UTC)

<p>Thanks Steve.<br>
Actually,we just need the output of volume rendering <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20">.We need the pixel values after nonlinearities that’s why I use SlicerFab to slice from the bottom to top along the Z axial and get all the slices.<br>
I set the layer thickness parameter according to our volume image spacing and click the generate bitmaps button:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8745ca1a5097ec02cc0b2b9b2a3f84679a393df3.png" data-download-href="/uploads/short-url/jiFYRPY8J4ti1ceJFDq9Qb5pGDN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8745ca1a5097ec02cc0b2b9b2a3f84679a393df3.png" alt="image" data-base62-sha1="jiFYRPY8J4ti1ceJFDq9Qb5pGDN" width="690" height="221" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">929×298 8.94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then I picked one of the slices to show in Matlab:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d42733af35f9ee419c0595af0902cf3a1c0d2ae.png" data-download-href="/uploads/short-url/k9DGUg6K7cFnU0evtc5BEqdJrDE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d42733af35f9ee419c0595af0902cf3a1c0d2ae_2_536x499.png" alt="image" data-base62-sha1="k9DGUg6K7cFnU0evtc5BEqdJrDE" width="536" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d42733af35f9ee419c0595af0902cf3a1c0d2ae_2_536x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d42733af35f9ee419c0595af0902cf3a1c0d2ae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d42733af35f9ee419c0595af0902cf3a1c0d2ae.png 2x" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">757×706 12.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But I found the dimensions are not correct.From the picture above we saw about 1000x1000 which is different from the X and Y resolution that are 600DPI and 300DPI.<br>
So,what’s the meaning of the printer resolution parameters and how can I just match the dimension to the volume data?In other words,how can I just save the volume slice without any background.</p>

---

## Post #22 by @pieper (2021-12-29 00:10 UTC)

<p>Yes, if you have different dots per inch in the x and y directions you would expect to see a distortion like that.  You can set both dpi values to match what your matlab code expects.</p>

---

## Post #23 by @user4 (2021-12-30 09:28 UTC)

<p>Thanks Steve,<br>
I set the XY resolution 300 x 300 which is according to my volume information in Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d995e7e207f864e20177dda7e222c667bec40a.png" data-download-href="/uploads/short-url/9oxd3cS9QRFur3qqzPhvPRgezGy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d995e7e207f864e20177dda7e222c667bec40a_2_518x500.png" alt="image" data-base62-sha1="9oxd3cS9QRFur3qqzPhvPRgezGy" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d995e7e207f864e20177dda7e222c667bec40a_2_518x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d995e7e207f864e20177dda7e222c667bec40a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d995e7e207f864e20177dda7e222c667bec40a.png 2x" data-dominant-color="57596E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×676 87.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3142bc34efa5245914d960431746573b22001f8b.png" data-download-href="/uploads/short-url/71MnhvjvOlDsRQOOgo2NgkNVqEH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3142bc34efa5245914d960431746573b22001f8b.png" alt="image" data-base62-sha1="71MnhvjvOlDsRQOOgo2NgkNVqEH" width="690" height="101" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×134 3.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/788a6ca4c2b26977f70b1677e2896bb5fb3ff6c2.png" data-download-href="/uploads/short-url/hclRTJYAWSG8rOcsmqUG684nWfM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/788a6ca4c2b26977f70b1677e2896bb5fb3ff6c2.png" alt="image" data-base62-sha1="hclRTJYAWSG8rOcsmqUG684nWfM" width="690" height="107" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×149 2.43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I load one slice into MATLAB,the 2D image seemingly is compressed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8affd793546fe9efc883b26a773c9084a0b7ee4c.png" data-download-href="/uploads/short-url/jPE1RBSQswHsPt6i3HTsKqzkYiM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8affd793546fe9efc883b26a773c9084a0b7ee4c_2_582x500.png" alt="image" data-base62-sha1="jPE1RBSQswHsPt6i3HTsKqzkYiM" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8affd793546fe9efc883b26a773c9084a0b7ee4c_2_582x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8affd793546fe9efc883b26a773c9084a0b7ee4c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8affd793546fe9efc883b26a773c9084a0b7ee4c.png 2x" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">824×707 4.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79f5f2fa8790810ff7b6f154c71da96ddacbbba4.png" data-download-href="/uploads/short-url/hoUIu8fQNrNBAxhAcsBggUVdgtS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79f5f2fa8790810ff7b6f154c71da96ddacbbba4.png" alt="image" data-base62-sha1="hoUIu8fQNrNBAxhAcsBggUVdgtS" width="441" height="500" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">453×513 7.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The dimension should be 300x300 right?</p>

---

## Post #24 by @pieper (2021-12-30 20:32 UTC)

<aside class="quote no-group" data-username="user4" data-post="23" data-topic="20674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p>I set the XY resolution 300 x 300 which is according to my volume information in Slicer</p>
</blockquote>
</aside>
<p>The output resolution in dpi is not related to the resolution of your input volume, since Slicer is volume rendering in patient space.  So you want to specify the output resolution in terms of the physical size of your subject and the expectations of the matlab code.  HTH.</p>

---

## Post #25 by @user4 (2021-12-31 03:37 UTC)

<p>Thanks Steve,<br>
I have tried several times and set the XY resolution by 510 and got the 2D slice image dimension 300x300 in MATLAB.So it is confused to me,what’s the relationship between the output image and the printer parameters setting?<br>
Another quesion,If I do some volume rendering and silce with the same parameters setting,the output image size is different from the raw volume without any rendering.<br>
Can you describe the reason in detail? Thank you very much!</p>

---
