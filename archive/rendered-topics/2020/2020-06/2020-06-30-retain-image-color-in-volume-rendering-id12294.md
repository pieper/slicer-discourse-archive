# Retain Image Color in Volume Rendering

**Topic ID**: 12294
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294

---

## Post #1 by @David_Brouwer (2020-06-30 12:27 UTC)

<p>I am looking to create a 3D model of a stack of images, retaining the original image color. See the screenshot as a reference.</p>
<p>By creating a segmentation with a threshold of 22 - 255 I am able to select the desired part and create a model, however, then the color becomes the label color. I’d like to create the exact same 3D model, except with the original colors.</p>
<p>Is this possible?</p>
<p>I have already consulted this tread, yet the code suggested there gives me errors (if a trace is useful I can provide that)</p><aside class="quote" data-post="4" data-topic="6472">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/4">Merge colored images and show them as 1 volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you just want to visualize them with their original color, apply spatial transforms, etc. then you don’t need to convert to scalar volume. What would you like to do with the image?
  </blockquote>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24372b67979821b2bea2adbef5a9e03be72ae8ec.jpeg" data-download-href="/uploads/short-url/5ano7TvDKthI32hJ9W6UYLTR2Jm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24372b67979821b2bea2adbef5a9e03be72ae8ec_2_590x500.jpeg" alt="image" data-base62-sha1="5ano7TvDKthI32hJ9W6UYLTR2Jm" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24372b67979821b2bea2adbef5a9e03be72ae8ec_2_590x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24372b67979821b2bea2adbef5a9e03be72ae8ec_2_885x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24372b67979821b2bea2adbef5a9e03be72ae8ec.jpeg 2x" data-dominant-color="1B1B22"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1033×875 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>P.s. I’ve had quite a few issues with 4.11 on Linux; 1. I can’t load saved files, as this crashes the program, 2. I can’t use “Surface smoothing”, as that crashes the application. (4.10 gives me even more issues)</p>
<pre><code class="lang-auto">SetConversionParameter: Conversion parameter 'Collapse labelmaps' not found in converter rules!

SetConversionParameter: Conversion parameter 'Joint smoothing' not found in converter rules!

error: [/home/tyler/Downloads/Slicer-4.10.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @lassoan (2020-06-30 12:32 UTC)

<p>If Slicer crashes then it is almost surely because you run out of memory. How large is your input image and how much physical RAM do you have and how much swap space have you configured?</p>
<p>Please also provide the trace for the error.</p>
<p>Have you tried it with the very latest Slicer Preview Release?</p>

---

## Post #3 by @David_Brouwer (2020-06-30 12:59 UTC)

<p>16GB of ram, no swap set up. Trace is here <a href="https://pastebin.com/qr5U16MJ" rel="nofollow noopener">https://pastebin.com/qr5U16MJ</a></p>
<p>Memory usage goes up to 92% and then crashes.</p>
<p>Although that’s not my primary issue, do you have any clue whether original colored 3d models are possible?</p>

---

## Post #4 by @rkikinis (2020-06-30 13:21 UTC)

<p>Have you tried volume rendering? Slicer takes the LUT setting and window/level as a startpoint for the transfer function of the volume renderer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fc077a565eb348e44bde74aedfac08fce949fd8.jpeg" data-download-href="/uploads/short-url/bnw4VYzTJdHHZuLrzj2b1DwSVfy.jpeg?dl=1" title="Screen Shot 2020-06-30 at 9.21.49 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc077a565eb348e44bde74aedfac08fce949fd8_2_539x500.jpeg" alt="Screen Shot 2020-06-30 at 9.21.49 AM.png" data-base62-sha1="bnw4VYzTJdHHZuLrzj2b1DwSVfy" width="539" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc077a565eb348e44bde74aedfac08fce949fd8_2_539x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc077a565eb348e44bde74aedfac08fce949fd8_2_808x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc077a565eb348e44bde74aedfac08fce949fd8_2_1078x1000.jpeg 2x" data-dominant-color="275E45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-06-30 at 9.21.49 AM.png</span><span class="informations">2070×1920 1.25 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-06-30 13:45 UTC)

<p>Yes, you should be able to color a model’s surface using a color volume using latest Slicer Preview Release. I’ll double-check if it works as expected.</p>
<p>Memory usage at 92% means there is a high chance of running out of memory. If you configure a few ten GB of swap space then it should take care of it.</p>
<p>What is the size and d your data set? What is the scalar type? (these are shown in Volumes module Volume information section)</p>

---

## Post #6 by @David_Brouwer (2020-06-30 15:24 UTC)

<p>The first thing I tried was volume rendering, but then I just get a black box, so I’m wondering how I can cut out the black parts.</p>
<p>Scalar type is unsigned char, and 1.2gb of 388 1080x1080 tiff images</p>
<p>This is my dataset : <a href="https://1drv.ms/u/s!AprYdPzSEdGHgpo5lgPqkwL-hQdi8g?e=xW1FPa" rel="nofollow noopener">https://1drv.ms/u/s!AprYdPzSEdGHgpo5lgPqkwL-hQdi8g?e=xW1FPa</a></p>

---

## Post #7 by @lassoan (2020-06-30 15:37 UTC)

<p>How did you create these images? Can you just export them as scalar volume? Then you could apply color mapping in Slicer, easily use volume rendering, etc. The problem really is that the color look-up is burnt into the image.</p>

---

## Post #8 by @David_Brouwer (2020-06-30 15:53 UTC)

<p>Ah hmm. I’m not sure, I didn’t create them. I’ll ask if that’s possible.</p>
<p>Is there any work around for these images?</p>

---

## Post #9 by @lassoan (2020-06-30 16:01 UTC)

<p>If the colors are result of color imaging there is not much to do (then you probably want to use the original color) but if they are result of applying a color map (color look-up table) then it would be better to get the original scalar images.</p>
<p>Anyway, color volume rendering should work, too, as described in this post: <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6" class="inline-onebox">Merge colored images and show them as 1 volume</a></p>

---

## Post #10 by @lassoan (2020-06-30 16:41 UTC)

<p>I’ve downloaded your images and used this script to convert it to add an alpha channel and enable direct RGBA volume rendering (just copy-paste it into Slicer’s Python console after you loaded your data set):</p>
<pre><code class="lang-python"># Find loaded vector volume
colorVolume = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLVectorVolumeNode")

# Convert RGB image to RGBA
luminance = vtk.vtkImageLuminance()
luminance.SetInputConnection(colorVolume.GetImageDataConnection())
append=vtk.vtkImageAppendComponents()
append.AddInputConnection(colorVolume.GetImageDataConnection())
append.AddInputConnection(luminance.GetOutputPort())
append.Update()
colorVolume.SetAndObserveImageData(append.GetOutput())

# Enable volume rendering
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(colorVolume)
displayNode.SetVisibility(True)
# Enable direct RGBA color mapping
displayNode.GetVolumePropertyNode().GetVolumeProperty().SetIndependentComponents(0)
</code></pre>
<p>After slightly adjusting scalar opacity mapping in Volume rendering module and changing background to black I got this beautiful rendering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b6a99fe5cbd18821242f9986ee535590653a1fd.jpeg" data-download-href="/uploads/short-url/6c4VhJWtWNijghnEl5KODBMyM4R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6a99fe5cbd18821242f9986ee535590653a1fd_2_690x365.jpeg" alt="image" data-base62-sha1="6c4VhJWtWNijghnEl5KODBMyM4R" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6a99fe5cbd18821242f9986ee535590653a1fd_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6a99fe5cbd18821242f9986ee535590653a1fd_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6a99fe5cbd18821242f9986ee535590653a1fd_2_1380x730.jpeg 2x" data-dominant-color="919492"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1591×842 359 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>A video created by Screen Capture module:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="o5I_XWkm1nk" data-video-title="Color volume rendering" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=o5I_XWkm1nk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/o5I_XWkm1nk/maxresdefault.jpg" title="Color volume rendering" width="" height="">
  </a>
</div>

<p>We plan to release Slicer5 soon and looking for nice images that could demonstrate capabilities of the application. Would you consider allowing this data set to be showcased as an image or video (with proper acknowledgments and reference to publication)?</p>

---

## Post #11 by @David_Brouwer (2020-06-30 18:58 UTC)

<p>Oh wow that looks really good, thanks!<br>
I’ll ask at work if they are fine with that, I’ll let you know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #12 by @David_Brouwer (2020-07-01 14:15 UTC)

<p>I’ve been able to recreate the Volume, which is really cool. Now I am looking to export it of some sort (with the end goal of creating more complex animations)</p>
<p>Therefore I tried to segment it as I read from all the other treads you can’t export a volume rendering, however, is it possible to retain the color of the model in the segmentation?</p>
<p>I have referenced your answers <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6">here</a> , yet was unsuccessful in creating a mesh with colors, is it possible to do this with this software?</p>

---

## Post #13 by @lassoan (2020-07-01 14:49 UTC)

<p>Volume rendering is a display technique, which produces a 2D color picture. There is nothing else that could be “exported”. See more detailed description <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">here</a>.</p>
<p>To display a volume like this, you need to use volume rendering. Blender can do everything, including volume rendering, but of course it is very complicated to achieve something like that is shown above. If you want to try it anyway then you can find some pointers <a href="https://discourse.vtk.org/t/bvtknodes-photorealistic-rendering-of-vtk-data-in-blender/3268/16">here</a>.</p>

---

## Post #14 by @David_Brouwer (2020-07-01 15:39 UTC)

<p>Thanks a lot for the info, it is greatly appreciated. The BVTKNodes link you provided looks very interesting. The result of the sample set you provided looks really nice.</p>
<p>I am looking to give it a shot. If doesn’t take too much time, with the programs mentioned being Paraview, the BVTKNodes plugin, and Blender itself, what would be the general workflow here?</p>

---

## Post #15 by @lassoan (2020-07-01 17:25 UTC)

<p>You should be able to load the volume directly into Blender and render it there.</p>

---

## Post #16 by @tgterra (2021-04-14 13:10 UTC)

<p>I have the same question <a class="mention" href="/u/lassoan">@lassoan</a>: is it possible to retain the color of the model in the segmentation?</p>
<p>I tried to use Probe volume with model, like you explain <a href="https://discourse.slicer.org/t/creating-real-colour-models-using-visible-human-data/14627/2">here</a>, but my results were very “weird”.</p>
<p>This is the volume rendering of the segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a33a52b64374fbc698897322c12ab6607eab8a2.jpeg" data-download-href="/uploads/short-url/61kHACwXkCSEGnmwxxC31O8R9K2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a33a52b64374fbc698897322c12ab6607eab8a2_2_690x373.jpeg" alt="image" data-base62-sha1="61kHACwXkCSEGnmwxxC31O8R9K2" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a33a52b64374fbc698897322c12ab6607eab8a2_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a33a52b64374fbc698897322c12ab6607eab8a2_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a33a52b64374fbc698897322c12ab6607eab8a2.jpeg 2x" data-dominant-color="4A4955"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×693 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This was the result with “Probe volume with model” &gt; “Direct color mapping”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0880bb2f25187896f8815f9e48f86b3b319216c3.png" data-download-href="/uploads/short-url/1ddCKJOjRiqizMGzLffr4s6iwLh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0880bb2f25187896f8815f9e48f86b3b319216c3_2_690x373.png" alt="image" data-base62-sha1="1ddCKJOjRiqizMGzLffr4s6iwLh" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0880bb2f25187896f8815f9e48f86b3b319216c3_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0880bb2f25187896f8815f9e48f86b3b319216c3_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0880bb2f25187896f8815f9e48f86b3b319216c3_2_1380x746.png 2x" data-dominant-color="696A86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Change from “Direct color mapping” to “color table”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a6071a0ccfba993ae32b4f9bcb4490efd001205.png" data-download-href="/uploads/short-url/cTvBlsAMYYPw57tTeM4Ot2rnfAp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a6071a0ccfba993ae32b4f9bcb4490efd001205_2_690x373.png" alt="image" data-base62-sha1="cTvBlsAMYYPw57tTeM4Ot2rnfAp" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a6071a0ccfba993ae32b4f9bcb4490efd001205_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a6071a0ccfba993ae32b4f9bcb4490efd001205_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a6071a0ccfba993ae32b4f9bcb4490efd001205_2_1380x746.png 2x" data-dominant-color="5F677E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2021-04-14 15:01 UTC)

<p>You would need to create a color map similar to the color transfer function that you use for volume rendering, but of course you will never get similar image quality with surface rendering as with volume rendering. This has been discussed previously in other topics, see for example here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b19c9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am a new user on 3D slicer. 
I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file. 
For example, I was viewing a sample MRI using the CT-cardiac3 preset display. 
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable. 
I was only able to see .vp (volume property), .txt formats. 
Is there a way to accomplish what I desire in 3D slic…
  </blockquote>
</aside>


---

## Post #18 by @tgterra (2021-04-14 20:09 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your reply. Could you help me to create this color map? I’m new with 3d slicer <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #19 by @lassoan (2021-04-15 00:03 UTC)

<h2><a name="p-58063-for-scalar-not-rgb-volumes-1" class="anchor" href="#p-58063-for-scalar-not-rgb-volumes-1" aria-label="Heading link"></a>For scalar (not RGB) volumes</h2>
<p>You can copy the color transfer function to a color node by copy-pasting this into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">volumeRenderingPropertyNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLVolumePropertyNode')
colorNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLProceduralColorNode')
colorNode.GetColorTransferFunction().DeepCopy(volumeRenderingPropertyNode.GetColor())
</code></pre>
<p>However, as I wrote above, do not expect surface rendering to even remotely similar to volume rendering, but something like this instead (left: volume rendering; right: surface rendering of probed surface):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97f4020a47f1c415965d15702ea48ecd07efb497.jpeg" data-download-href="/uploads/short-url/lGeSJ6oBE6WXEqj4fN1qwD3p9Vt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4020a47f1c415965d15702ea48ecd07efb497_2_690x339.jpeg" alt="image" data-base62-sha1="lGeSJ6oBE6WXEqj4fN1qwD3p9Vt" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4020a47f1c415965d15702ea48ecd07efb497_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97f4020a47f1c415965d15702ea48ecd07efb497_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97f4020a47f1c415965d15702ea48ecd07efb497.jpeg 2x" data-dominant-color="948799"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×567 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The reason is that the texture/discoloration in the volume rendering is due to the cloud of lower or higher intensity voxels around the isosurface value, while in case of surface rendering the discoloration mainly comes from image interpolation artifacts (because if you segment by thresholding then you ideally get a surface where all the points have the exact same scalar value and any difference is due to small interpolation errors).</p>
<p>If you want a little bit more similar results then you can apply some Gaussian smoothing (using Gaussian Blur Image Filter module) to the input volume before you probe the volume with the model (that makes surrounding regions somewhat influence each point’s intensity):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4d343479df2b6a81558d0f1ad841f97cde379c.jpeg" data-download-href="/uploads/short-url/fs4YtEAYIQAXeM6xVGpYjaP2ALa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c4d343479df2b6a81558d0f1ad841f97cde379c_2_690x341.jpeg" alt="image" data-base62-sha1="fs4YtEAYIQAXeM6xVGpYjaP2ALa" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c4d343479df2b6a81558d0f1ad841f97cde379c_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c4d343479df2b6a81558d0f1ad841f97cde379c_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c4d343479df2b6a81558d0f1ad841f97cde379c.jpeg 2x" data-dominant-color="9C8F98"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×574 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-58063-for-rgb-volumes-2" class="anchor" href="#p-58063-for-rgb-volumes-2" aria-label="Heading link"></a>For RGB volumes</h2>
<p>If you have RGB volumes then you don’t need a colormap but you use direct color mapping. The fundamental difference between volume rendering/surface rendering still applies, and you’ll basically get a uniformly colored surface if you create segments by thresholding.</p>
<p>You must have chosen a wrong volume when you used Probe volume with model (not the RGB volume) if it came out like that in your screenshot. Try the probing again and if you cannot figure out what’s wrong then upload your scene as a .mrb file somewhere and post the link here.</p>
<p>I get this with the default red-green-blue colormap:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c31847f0466b62b303ed1b20eb3f8645c423933c.jpeg" data-download-href="/uploads/short-url/rPT7YbQISUlx74YSGpqnrLME5RO.jpeg?dl=1" title="2021-04-14_19-52-34"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c31847f0466b62b303ed1b20eb3f8645c423933c_2_690x384.jpeg" alt="2021-04-14_19-52-34" data-base62-sha1="rPT7YbQISUlx74YSGpqnrLME5RO" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c31847f0466b62b303ed1b20eb3f8645c423933c_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c31847f0466b62b303ed1b20eb3f8645c423933c_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c31847f0466b62b303ed1b20eb3f8645c423933c.jpeg 2x" data-dominant-color="383A3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-04-14_19-52-34</span><span class="informations">1378×768 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this is what I see when I switch to direct mapping:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6acd0e377e5a986f2dd34f4129d41e93aec001.jpeg" data-download-href="/uploads/short-url/1u9ASmAaFmEOy6gx9HFpXPXkQlH.jpeg?dl=1" title="2021-04-14_19-53-00"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6acd0e377e5a986f2dd34f4129d41e93aec001_2_690x385.jpeg" alt="2021-04-14_19-53-00" data-base62-sha1="1u9ASmAaFmEOy6gx9HFpXPXkQlH" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6acd0e377e5a986f2dd34f4129d41e93aec001_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6acd0e377e5a986f2dd34f4129d41e93aec001_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6acd0e377e5a986f2dd34f4129d41e93aec001.jpeg 2x" data-dominant-color="3C383D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-04-14_19-53-00</span><span class="informations">1377×770 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m not sure what your goal is, but I don’t think you can get realistic surface textures from the color in these cross-sectional images. If you want to see nice surface texture then it is better to take a photo of dissected organs and apply that texture to surface models.</p>

---

## Post #20 by @tgterra (2021-04-15 13:07 UTC)

<p>Wow, thank you so much <a class="mention" href="/u/lassoan">@lassoan</a> ! Your answer will help me a lot, thanks again!</p>

---

## Post #21 by @tgterra (2021-04-15 13:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="12294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probe volume with model</p>
</blockquote>
</aside>
<p>I tried to use the Probe volume with model but it didn’t work <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> . I used the RGBA volume to Probe volume with the model (with direct color mapping) and I choose my segmented model. My goal is to try to export my segmented models with the RGB volume as texture.</p>
<p>Here is the link to access the .mrb file: <a href="https://drive.google.com/drive/folders/129_MfWNBdJIzO6D4qiiVZVZXhXQmKKmw?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/129_MfWNBdJIzO6D4qiiVZVZXhXQmKKmw?usp=sharing</a></p>

---

## Post #22 by @lassoan (2021-04-15 15:58 UTC)

<p>I’ve checked the scene. The problem was that the transform was not hardened on the <code>rgb</code> volume and CLI modules, such as “Probe volume with model” do not take into account transforms that are dynamically applied to a node. You can harden a transform in Data module by right-clicking on the icon in the transform column.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7299cd226472d4cf857555c0e9d27ff424121953.jpeg" data-download-href="/uploads/short-url/glNWRwU3xbQIjARLlSxih0uiCK7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7299cd226472d4cf857555c0e9d27ff424121953_2_590x500.jpeg" alt="image" data-base62-sha1="glNWRwU3xbQIjARLlSxih0uiCK7" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7299cd226472d4cf857555c0e9d27ff424121953_2_590x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7299cd226472d4cf857555c0e9d27ff424121953.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7299cd226472d4cf857555c0e9d27ff424121953.jpeg 2x" data-dominant-color="7E747C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">845×716 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @tgterra (2021-04-15 17:35 UTC)

<p>Nice! I reach that result too! Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #24 by @tgterra (2021-04-16 13:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> when I try to save this model by clicking at “Save” and select “OBJ” I get this result with MeshLab:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b39ecbe2a963a18fd7fe5e3d85e914e4621d7106.png" data-download-href="/uploads/short-url/pCZGAMcJhEiK2qzgKABfgFMf2cK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39ecbe2a963a18fd7fe5e3d85e914e4621d7106_2_690x373.png" alt="image" data-base62-sha1="pCZGAMcJhEiK2qzgKABfgFMf2cK" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39ecbe2a963a18fd7fe5e3d85e914e4621d7106_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39ecbe2a963a18fd7fe5e3d85e914e4621d7106_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39ecbe2a963a18fd7fe5e3d85e914e4621d7106_2_1380x746.png 2x" data-dominant-color="666385"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, when I duplicated the model, disable the Scalars and stay both visibilities I get this result at 3D Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43242f476836a72628642f4fbd41a544539749c1.jpeg" data-download-href="/uploads/short-url/9zXvYUGxwsRvMn2XLlzW1udlYBP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43242f476836a72628642f4fbd41a544539749c1.jpeg" alt="image" data-base62-sha1="9zXvYUGxwsRvMn2XLlzW1udlYBP" width="644" height="500" data-dominant-color="81778A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×536 70.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For me, this model is pretty good (considering the segmentation). My question is: can I export exactly this model as OBJ?</p>

---

## Post #25 by @lassoan (2021-04-16 13:23 UTC)

<p>OBJ format does not support per-vertex color, so you would need to save this model as a format that does, for example VTK, VTP, or PLY. If you must use OBJ format then you can load the per-vertex colored model into a 3D modeling software and create a texture from the per-vertex colors.</p>

---

## Post #26 by @tgterra (2021-04-16 17:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Even exporting as PLY or another format I get a model without texture:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2ed4a4450fc8d875da72abb86b9562e2bc2a7c.jpeg" data-download-href="/uploads/short-url/oqlYRjFa7rXgRDm5s5eakclOITW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2ed4a4450fc8d875da72abb86b9562e2bc2a7c_2_393x500.jpeg" alt="image" data-base62-sha1="oqlYRjFa7rXgRDm5s5eakclOITW" width="393" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2ed4a4450fc8d875da72abb86b9562e2bc2a7c_2_393x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2ed4a4450fc8d875da72abb86b9562e2bc2a7c_2_589x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2ed4a4450fc8d875da72abb86b9562e2bc2a7c.jpeg 2x" data-dominant-color="747096"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">639×812 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @lassoan (2021-04-18 04:49 UTC)

<p>You can save the RGB values in PLY by a few lines of Python script, but I’ve <a href="https://github.com/Slicer/Slicer/pull/5600">submitted a pull request</a> that makes this available automatically via standard save data feature. It will be probably available in Slicer Preview Release on Monday or Tuesday.</p>

---
