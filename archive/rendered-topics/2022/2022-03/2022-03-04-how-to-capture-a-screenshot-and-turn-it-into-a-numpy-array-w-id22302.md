---
topic_id: 22302
title: "How To Capture A Screenshot And Turn It Into A Numpy Array W"
date: 2022-03-04
url: https://discourse.slicer.org/t/22302
---

# How to capture a screenshot and turn it into a numpy array with python code?

**Topic ID**: 22302
**Date**: 2022-03-04
**URL**: https://discourse.slicer.org/t/how-to-capture-a-screenshot-and-turn-it-into-a-numpy-array-with-python-code/22302

---

## Post #1 by @user4 (2022-03-04 02:56 UTC)

<p>Slicer version 4.11<br>
I can capture a screenshot here:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b20a94b9e54d0137ac5e713b1f0492d50a23c15.png" alt="image" data-base62-sha1="8r498bu5ZOp20JfdKt5E0CC6qtT" width="380" height="351"><br>
or I can capture a screenshot in Script Repository <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#screen-capture" rel="noopener nofollow ugc">here</a></p>
<p>However,both of the two methods are saving the image as .png file.If I want to see the image pixel value I have to load this image file.<br>
So there is some way to capture a screenshot in python and make it a numpy array without saving it?</p>
<p>Thank you advance for your help and advice!!</p>

---

## Post #2 by @jamesobutler (2022-03-04 03:10 UTC)

<p>To get a slice of a volume as a numpy array you can use some of the examples such as</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-axial-slice-as-numpy-array" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-axial-slice-as-numpy-array</a></p>

---

## Post #3 by @user4 (2022-03-04 07:08 UTC)

<p>Thank you james but this is not what I need,<br>
I have to use the screenshots image cause it is after ray casting.</p>
<pre><code class="lang-auto"># Capture RGBA image
renderWindow = view.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
writer = vtk.vtkPNGWriter()
writer.SetFileName("c:/tmp/screenshot.png")
writer.SetInputConnection(wti.GetOutputPort())
writer.Write()
</code></pre>
<p>I think there must be an interface to get the image in buffer,however I am not sure how to get the data.</p>

---

## Post #4 by @pieper (2022-03-04 14:36 UTC)

<p>This example <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L414-L426"><code>vtkImageDataToPNG</code></a> may help.  It’ll give you an array of the png compressed image by you can get something similar if you just use the <code>vtkWindowToImageFilter</code> output directly.</p>

---

## Post #5 by @user4 (2022-03-05 17:52 UTC)

<p>Thanks Steve! You really gave me some insight!  I think I am close to the solution but maybe need a little more help!<br>
I saw the example and did it in three steps:</p>
<ol>
<li>Get the render window</li>
</ol>
<pre><code class="lang-auto">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
</code></pre>
<ol start="2">
<li>Use the filter to get vtk data</li>
</ol>
<pre><code class="lang-auto">wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
# wti.ReadFrontBufferOff()
wti.Update()
vtk_data = wti.GetOutput()
</code></pre>
<ol start="3">
<li>Use <em>vtkImageDataToPNG</em> function to get pngArray</li>
</ol>
<pre><code class="lang-auto">def vtkImageDataToPNG(imageData):
    """
    Return pngArray using the data from the vtkImageData.
    """
    writer = vtk.vtkPNGWriter()
    writer.SetWriteToMemory(True)
    writer.SetInputData(imageData)
    # use compression 0 since data transfer is faster than compressing
    writer.SetCompressionLevel(0)
    writer.Write()
    result = writer.GetResult()
    pngArray = vtk.util.numpy_support.vtk_to_numpy(result)

    return pngArray


pngArray = vtkImageDataToPNG(vtk_data)
</code></pre>
<p>After the above three steps,I checked the type and shape of the pngArray as follows:</p>
<pre><code class="lang-auto">type(pngArray)
--&gt; &lt;class 'numpy.ndarray'&gt;

pngArray.shape
--&gt; (3721789,)
</code></pre>
<p>I have two question for the above results:</p>
<ol>
<li>
<p>It seems the array has been flattened,so my next quesion is how to reshape the array to the render window size, in other words,how to get the render window size (height,width).</p>
</li>
<li>
<p>I compared the dimension of the pngArray with the screenshot produced by GUI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b031798a7c41509b3c7c096bd8d33d8c15404a1.png" data-download-href="/uploads/short-url/hydlW48W7eeF1xVhz9hkd4XxU9H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b031798a7c41509b3c7c096bd8d33d8c15404a1_2_690x417.png" alt="image" data-base62-sha1="hydlW48W7eeF1xVhz9hkd4XxU9H" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b031798a7c41509b3c7c096bd8d33d8c15404a1_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b031798a7c41509b3c7c096bd8d33d8c15404a1_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b031798a7c41509b3c7c096bd8d33d8c15404a1_2_1380x834.png 2x" data-dominant-color="B9BBE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1571×951 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Theoretically,the png image is the same dimension with the pngArray,so I read the image and check both dimensions:</p>
</li>
</ol>
<pre><code class="lang-auto">import matplotlib.image as mpimg
img = mpimg.imread('test.png')
img.shape
--&gt; (925, 1004, 4)

925 * 1004 * 4
--&gt; 3714800
</code></pre>
<p>It is strange that the two images are not the same size,in other words,the flattened numbers are different. (3714800 v.s. 3721789).Did something go wrong during the procedure of producing the pngArray?</p>
<p>Thank you for your continued attention and help again!</p>

---

## Post #6 by @pieper (2022-03-05 18:34 UTC)

<p>Hi <a class="mention" href="/u/user4">@user4</a> -</p>
<p>Yes, you are very close - the example I pointed to was for getting the compressed png data as an array (e.g. the data in a .png file).  Instead you need to get the array from the <code>vtkImageData</code> that comes from the <code>vtkWindowToImageFilter</code>.</p>
<p>Here’s the snippet:</p>
<pre><code class="lang-auto">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderWindow.SetAlphaBitPlanes(1)
wti = vtk.vtkWindowToImageFilter()
wti.SetInputBufferTypeToRGBA()
wti.SetInput(renderWindow)
wti.Update()
image_array = vtk.util.numpy_support.vtk_to_numpy(vtk_data.GetPointData().GetScalars())
image_array = image_array.reshape((view.height, view.width, 4))
</code></pre>
<p>You may need to swap width and height - I didn’t check that for sure.</p>

---

## Post #7 by @user4 (2022-03-06 08:10 UTC)

<p>Thanks Steve! You are quite right,with your code above I have get the image array:</p>
<pre><code class="lang-auto">image_array.shape
--&gt; (925, 1136, 4)
</code></pre>
<p>While I took a screenshot with GUI, and saved the png image file marked in red:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d9a5dfe0d62ecbf7f7504e0fea185ae99fbe8b3.png" data-download-href="/uploads/short-url/8MXR3IV1JvXBdcyBO2Q72yjnn4D.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d9a5dfe0d62ecbf7f7504e0fea185ae99fbe8b3_2_638x500.png" alt="image" data-base62-sha1="8MXR3IV1JvXBdcyBO2Q72yjnn4D" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d9a5dfe0d62ecbf7f7504e0fea185ae99fbe8b3_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d9a5dfe0d62ecbf7f7504e0fea185ae99fbe8b3_2_957x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d9a5dfe0d62ecbf7f7504e0fea185ae99fbe8b3_2_1276x1000.png 2x" data-dominant-color="B0B0D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×1080 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">from skimage import io
img = io.imread('test.png')
img.shape

--&gt; (925, 1136, 4)
</code></pre>
<p>yeah, It seems okay because the dimensions of both images are the same.<br>
However,when I check the value of array it is not the same,am I missing something or maybe forgot some parameters setting?</p>
<pre><code class="lang-auto">(img == image_array).all()
--&gt; False
</code></pre>
<p>P.S<br>
This image is produced by image array with your help and code:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e0270d3da805b8c3f6b68b896e4f0895d7da8d0.png" alt="image" data-base62-sha1="fHbKyP7ukPj8dzJ0WNIodOshARO" width="416" height="286"></p>
<p>This image is produced by screenshot capture GUI:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/242a1b224d00c93e6c469664fef3a3d506f53a5a.png" alt="image" data-base62-sha1="59VoPWapQPedjOQBf9tsxzd7D9o" width="407" height="291"></p>
<p>Apparently,the two images are different from each other,do you think I am missing some parameters?</p>

---

## Post #8 by @pieper (2022-03-06 13:56 UTC)

<p>Ah yes, I forgot that detail.  It would be easier to tell if you load some data but you can see it in the gradient too: the images are mirrored vertically from each other.  This is because vtk image rows go from bottom to top (like xy coordinates of a graph), while most image formats stack the rows from top to bottom (like scan lines of an old tv).  So you need to rearrange the rows in memory to make the match.</p>

---

## Post #9 by @user4 (2022-03-06 14:53 UTC)

<p>Thanks a lot Steve! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">I have solved the problem just reversing the image array.<br>
However it can not be done without your help,I am really grateful to your help again!</p>

---
