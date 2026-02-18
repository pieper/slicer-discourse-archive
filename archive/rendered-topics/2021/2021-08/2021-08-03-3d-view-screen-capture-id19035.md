# 3D view screen capture

**Topic ID**: 19035
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/3d-view-screen-capture/19035

---

## Post #1 by @liku (2021-08-03 08:15 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.11</p>
<p>I captured images of 3D view (refer to the ScreenCapture module), and transferred these images to the library which uses OpenCL and performs image processing.<br>
Now I want to improve the execution time of the modulle.<br>
Is it possible to get the screen image of 3D view in the GPU?<br>
If possible, that would save the time to transfer the image from CPU to GPU</p>

---

## Post #2 by @lassoan (2021-08-03 13:27 UTC)

<p>Slicer uses VTK library for rendering. You can access both the 3D data (meshes, textures, etc.) and rendering in the GPU via VTK.</p>

---

## Post #3 by @liku (2021-08-04 07:02 UTC)

<p>I have gotten the screen image of 3D view via vtkRenderWindow.<br>
Like this.</p>
<blockquote>
<p>qMRMLThreeDView* threeDView = qSlicerApplication::application()-&gt;layoutManager()<br>
-&gt;threeDWidget(0)-&gt;threeDView();<br>
vtkRenderWindow* renderWindow = threeDView-&gt;renderWindow();<br>
int* dims = renderWindow-&gt;GetSize();<br>
unsigned char* pixelData = renderWindow-&gt;GetPixelData(0, 0, dims[0]-1, dims[1]-1, 1, 0);</p>
</blockquote>
<p>There are two questions</p>
<ol>
<li>Does GetPixelData() get the image from the GPU?</li>
<li>If yes, how to get the address of the image in the GPU?</li>
</ol>

---

## Post #4 by @lassoan (2021-08-04 13:12 UTC)

<p>Would you like to implement augmented reality? What hardware do you use with what interface?</p>

---

## Post #5 by @liku (2021-08-05 07:32 UTC)

<p>For example, in Unity,  the camera is assigned the texture to display what it capture.<br>
<a href="https://docs.unity3d.com/Manual/class-RenderTexture.html" rel="noopener nofollow ugc">https://docs.unity3d.com/Manual/class-RenderTexture.html</a></p>
<p>I could transfer the id/name of texture to the library which uses OpenCL. Then the library get displayed image via id/name, and performs image processing.</p>
<p>Can this method be implemented in 3D Slicer?</p>

---

## Post #6 by @pieper (2021-08-05 11:40 UTC)

<p>It is possible to share buffers between OpenGL and OpenCL but we don’t provide any support for that in Slicer.  It would be best to do it at the VTK level and then it could be exposed in Slicer.  If you figure out a good way to do this please post it for others to learn from.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://livebook.manning.com/book/opencl-in-action/chapter-15/1">
  <header class="source">
      <img src="https://d19npu3b8zepp3.cloudfront.net/assets/images/favicon.png?v=1" class="site-icon" width="32" height="32">

      <a href="https://livebook.manning.com/book/opencl-in-action/chapter-15/1" target="_blank" rel="noopener">livebook.manning.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:250/313;"><img src="https://drek4537l1klr.cloudfront.net/scarpino2/Figures/cover.jpg" class="thumbnail" width="250" height="313"></div>

<h3><a href="https://livebook.manning.com/book/opencl-in-action/chapter-15/1" target="_blank" rel="noopener">Chapter 15. Combining OpenCL and OpenGL · OpenCL in Action: How to Accelerate...</a></h3>

  <p>The functions needed to configure OpenGL-OpenCL interoperability · A method for coding OpenGL-OpenCL applications · Rendering animated models with OpenGL and OpenCL</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2021-08-05 12:55 UTC)

<p><a class="mention" href="/u/liku">@liku</a> What would you like to achieve? Slicer has been around for so long and used by so many people that most likely somebody has already done something similar that you can build on and we can help you find it.</p>
<p>For example, if you just want to use the rendering as an augmented reality overlay in Hololens, on a tablet, or other AR devices then there are several solutions for that, too (both old, current, and solutions that will be available soon). If you want to process the rendered image then it is probably better to use custom shaders rather than post-process the 2D rendering.</p>

---

## Post #9 by @lassoan (2021-08-05 14:51 UTC)

<p>There were dozens of Slicer-based AR projects over the years. Most of them are public, so you can find out a lot by searching on the web, but there are some current ones and others in infrastructure development phase that may be hard to find information online. Can you narrow it down a bit of what you are interested in?</p>
<p>What device are you planning to use: HoloLens, tablet, half-silvered mirror, video overlay on endoscope/microscope, …?<br>
(the potentially usable approaches mostly depend on this)</p>
<p>What kind of procedure do you plan to use it for: burr hole placement, vertebra level localization, etc. or higher-accuracy application, such as tumor resection, needle guidance, or pedicle screw placement…? (so that we get an idea about accuracy requirements and applicable calibration/registration procedures)</p>

---

## Post #10 by @slicer365 (2021-08-05 22:30 UTC)

<p>We want to superimpose the video from endoscope/microscope onto the 3D model on the computer screen.</p>
<p>HoloLens is very expensive. At present, we want to implement a simple AR.</p>
<p>We are more concerned about tumor resection. By using a video capture card, the endoscope The /microscope video is displayed on a computer, and 3DSlicer is running on this computer.</p>
<p>If the captured video can be directly displayed in the slicer’s 3D window, it will be great.</p>
<p>Of course, we tested and found that Plus can help us  display the video  in the 2D window of the slicer, but the 3D model cannot be superimposed.</p>

---

## Post #11 by @pieper (2021-08-06 11:42 UTC)

<p>That sounds like an interesting project and worthy goal.  Of course it can be very difficult to know the exact geometry of the endoscopy camera relative to the patient and the 3D model made from pre-procedure imaging.  But leaving that aside, did you try the “Show in 3D” button in <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">the Slice controller widget</a>?  (it is an icon that looks like an open or closed eye).  If you’ve got the endoscope video in 2D view this will let you view it in the 3D view as well.  Then you can focus on getting them to line up accurately.</p>

---

## Post #12 by @slicer365 (2021-08-06 13:32 UTC)

<p>Thank you very much, we will try your method.</p>
<p>At present, we use OBS to display the captured video and the captured slicer’s 3D window at the same time.</p>
<p>At the same time, we use OBS to adjust the background of the Slicer3D view by chroma key for transparency.</p>

---

## Post #13 by @maryam_shakeri (2025-01-14 19:38 UTC)

<p>Hi!</p>
<p>I’m trying to capture some images of my 3d views from Slicer.  Can I export just the sample’s image, without the blue background? If not, could I change the background color and if so, where?</p>
<p>Thanks</p>

---

## Post #14 by @pieper (2025-01-14 20:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ca101b5e0cdb2324bced601dd2ba51533079cae.jpeg" data-download-href="/uploads/short-url/ddqSIlLCYNK60LVtXSKayCqAYXQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ca101b5e0cdb2324bced601dd2ba51533079cae.jpeg" alt="image" data-base62-sha1="ddqSIlLCYNK60LVtXSKayCqAYXQ" width="479" height="294"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">479×294 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
