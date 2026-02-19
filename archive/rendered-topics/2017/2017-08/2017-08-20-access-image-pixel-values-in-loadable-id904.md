---
topic_id: 904
title: "Access Image Pixel Values In Loadable"
date: 2017-08-20
url: https://discourse.slicer.org/t/904
---

# Access image pixel values in LOADABLE

**Topic ID**: 904
**Date**: 2017-08-20
**URL**: https://discourse.slicer.org/t/access-image-pixel-values-in-loadable/904

---

## Post #1 by @Alexandre_Freitas_Du (2017-08-20 13:38 UTC)

<p>Hello everyone, everything good? Could someone help me with a question.</p>
<p>In the CLI I was able to get the pixels of the image using the GetBufferPointer () method.<br>
Here’s the example:</p>
<pre><code>	typedef itk::Image&lt;float, 3&gt; ImageType;
typedef itk::ImageFileReader&lt; ImageType  &gt;  ReaderType;

typename ReaderType::Pointer reader;
typename ImageType::Pointer image;

reader = ReaderType::New();	
reader-&gt;SetFileName( inputVolume.c_str() );
reader-&gt;Update();
image = reader-&gt;GetOutput();

*float dataPixel = image-&gt;GetBufferPointer();
</code></pre>
<p>Now in LOADABLE I was looking for some method of the vtkImageData class that could return the pixel values similar to the object used above itk :: Image. Here is the code I am using:</p>
<pre><code>vtkMRMLVolumeNode* volumeNode = vtkMRMLVolumeNode::SafeDownCast(d-&gt;InputVolumeComboBox-&gt;currentNode());
vtkImageData* image = volumeNode-&gt;GetImageData();

float *dataPixel= static_cast&lt;float *&gt;(image-&gt;GetScalarPointer(0,0,0));
</code></pre>
<p>I can get the dimension and other information from the vtkImageData object, but I am not able to get the values of the pixels, using the GetScalarPointer () function returns empty.</p>
<p>Would anyone have any suggestions or tell me the correct way to do this ??</p>

---

## Post #2 by @lassoan (2017-08-20 14:15 UTC)

<aside class="quote no-group" data-username="Alexandre_Freitas_Du" data-post="1" data-topic="904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/278dde/48.png" class="avatar"> Alexandre_Freitas_Du:</div>
<blockquote>
<p>GetScalarPointer () function returns empty</p>
</blockquote>
</aside>
<p>What do you mean by empty? Are you sure your image is float type?<br>
What you do seems mostly correct. It is safer to get scalar for a specific extent by using <code>GetScalarPointerForExtent()</code> or get the full buffer using <code>GetScalarPointer()</code>. Most often origin is (0,0,0) and extent starts from (0,0,0), so <code>GetScalarPointer(0,0,0)</code> should work as well.</p>
<p>In general, it is better to avoid pixel-wise access and use VTK filters for any processing. What would you like to achieve?</p>

---

## Post #3 by @Alexandre_Freitas_Du (2017-08-20 15:11 UTC)

<p>Andras, thanks for the reply.</p>
<p>Let me explain to you what I was doing in CLI, I was working with image processing (.nrrd) on GPUs, using OPENCL. I upload an image into an object with type of pixel float “itk :: Image &lt;float, 3&gt;”.</p>
<p>In order to send the image to GPU, I get a multidimensional float vector containing all pixel values ​​using the “image-&gt; GetBufferPointer ()”. Just  to I can send “image” (float vector) via Opencl to a GPU or CPU in my machine, the GPU will process the image and I get a result also in a one-dimensional float vector.</p>
<p>With this I import this vector using an itk class ImportImageFilter, creating an itk image object of type float, and finally I use the class CastImageFilter to convert the image to pixel of type short.</p>
<p>I was able to implement in CLI and compare different types of filters, comparing their traditional version with the version using Opencl (as a result I have a gain of up to 200x faster depending on the complexity of the algorithm, image size … etcc).</p>
<p>But the CLI has its limitations, right? So I started to venture into LOADABLE. But I’m having difficulties in this matter, I need to get the values of the pixels in float (the image is of short type in the 3D Slicer display), so after the result of the execution in the GPU I will have to convert to short so to display the result the image.</p>
<p>Can did you understand more or less?  <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=5" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"></p>
<p>Thanks again for your attention.</p>

---

## Post #4 by @lassoan (2017-08-20 16:04 UTC)

<p>I would recommend to implement processing in CLI (as you have done it already), and if needed add more sophisticated user interface in a Python (or maybe C++) loadable module.</p>
<p>CLIs are nice because you can easily run them without GUI, in batch mode and you can easily run them from loadable modules, too.</p>

---
