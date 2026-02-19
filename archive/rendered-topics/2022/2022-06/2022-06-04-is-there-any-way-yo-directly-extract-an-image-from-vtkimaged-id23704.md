---
topic_id: 23704
title: "Is There Any Way Yo Directly Extract An Image From Vtkimaged"
date: 2022-06-04
url: https://discourse.slicer.org/t/23704
---

# Is there any way yo directly extract an image from vtkImageData to export it as a tiff/png image?

**Topic ID**: 23704
**Date**: 2022-06-04
**URL**: https://discourse.slicer.org/t/is-there-any-way-yo-directly-extract-an-image-from-vtkimagedata-to-export-it-as-a-tiff-png-image/23704

---

## Post #1 by @chz31 (2022-06-04 21:53 UTC)

<p>Hi,</p>
<p>I am testing loading a series of rgb images as a volume using the ImageStacksModule, cropped them with an ROI, and export them as a new series of rgb images in the format of tiff or png.</p>
<p>An example image is here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f44af3d945dd9e6dcd1c274ba1f712be07fe4467.jpeg" data-download-href="/uploads/short-url/yR75rHSvafXkTwvScptIShZJTjF.jpeg?dl=1" title="DSC_1705" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f44af3d945dd9e6dcd1c274ba1f712be07fe4467_2_467x500.jpeg" alt="DSC_1705" data-base62-sha1="yR75rHSvafXkTwvScptIShZJTjF" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f44af3d945dd9e6dcd1c274ba1f712be07fe4467_2_467x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f44af3d945dd9e6dcd1c274ba1f712be07fe4467_2_700x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f44af3d945dd9e6dcd1c274ba1f712be07fe4467_2_934x1000.jpeg 2x" data-dominant-color="353536"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DSC_1705</span><span class="informations">1482×1586 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So far, I can successfully export a slice of image from a volume by first extracting the numpy array of an image from a vector volume. I then use this numpy array to create a new vector volume node <code>vectorVolume</code> that only contains one image.</p>
<p>After that, I can use <code>vectorVolume.GetImageData()</code> to extract the <code>vtkImageData</code> of the <code>vectorVolume</code>, which now contains only 1 image. This allows me export it using <code>vtkTIFFWriter()</code> or <code>vtkPNGWriter()</code>, which can only take  the <code>vtkImageData</code> object.</p>
<p>However, for every image in the original volume, I have to create a new volume with just one image to export it.</p>
<p>Therefore, I’m also thinking about directly output each image from the vtkImageData of the volume acquired from vectorVolumeNode.GetImageData() so that I don’t have to build a new volume for each image.</p>
<p>I could not find a way to do it. For an experiment, I tried to directly pass the numpy array of an image into vtkImageData object following the example here: <a href="https://discourse.slicer.org/t/how-to-convert-3d-numpy-array-to-vtk-and-save-the-vtk-file/22327/3" class="inline-onebox">How to convert 3D numpy array to vtk and save the .vtk file? - #3 by user4</a></p>
<pre><code class="lang-auto">image = imageArray[0, :, :, :] #Get the first image array from slicer.util.arrayFromVolume(vectorVolume)
shape = image.shape
vtype = vtk.util.numpy_support.get_vtk_array_type(image.dtype)

flat_img_array = image.flatten()
vtk_arr = vtk.util.numpy_support.numpy_to_vtk(num_array=flat_img_array, deep=True, array_type=vtype)

imgVTK = vtk.vtkImageData()
imgVTK.GetPointData().SetScalars(vtk_arr)
imgVTK.SetDimensions(shape)
</code></pre>
<p>I then exported the imgVTK as PNG:</p>
<pre><code class="lang-auto">w_png = vtk.vtkPNGWriter()
w_png.SetInputData(imgVTK)
w_png.GetInput()
w_png.SetFileName('tmp/test.png')
w_png.Write()
</code></pre>
<p>However, all I got is an image with pixels re-arranged.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/093e18fb47e60bee2a721f02164d3b7f9188c241.png" data-download-href="/uploads/short-url/1jLl7D5coZ4zJTWWfTkcsOog1TH.png?dl=1" title="test3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/093e18fb47e60bee2a721f02164d3b7f9188c241_2_535x500.png" alt="test3" data-base62-sha1="1jLl7D5coZ4zJTWWfTkcsOog1TH" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/093e18fb47e60bee2a721f02164d3b7f9188c241_2_535x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/093e18fb47e60bee2a721f02164d3b7f9188c241_2_802x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/093e18fb47e60bee2a721f02164d3b7f9188c241_2_1070x1000.png 2x" data-dominant-color="1D1D1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test3</span><span class="informations">1586×1482 359 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any way I can directly extract each image from <code>vectorVolumeNode.GetImageData()</code> as a single <code>vtkImageData</code> object and export it using <code>vtkTIFFWriter</code> without building a new volume for each image?</p>
<p>Thank you!</p>

---

## Post #2 by @mau_igna_06 (2022-06-05 11:04 UTC)

<p>I don’t know if it helpful but have you tried using vtkOriemtedImageData?</p>

---

## Post #3 by @pieper (2022-06-05 18:22 UTC)

<p>Looks like the data is there, just scrambled.  The image you get out is going to be 2D rgb but in your code you set the <code>vtkImageData</code> dimensions as if it were 3D.  You need to set the width and height dimensions and the slice dimension to be 1.  Then you set the number of components to be 3,  Probably best using <code>AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 3)</code>.</p>
<aside class="quote no-group" data-username="chz31" data-post="1" data-topic="23704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>Is there any way I can directly extract each image from <code>vectorVolumeNode.GetImageData()</code> as a single <code>vtkImageData</code> object and export it using <code>vtkTIFFWriter</code> without building a new volume for each image?</p>
</blockquote>
</aside>
<p>If you want one tiff file per frame, then you can just use the same <code>vtkImageData</code> in a loop that just copies the data and re-runs the writer.  It should run pretty fast.</p>

---

## Post #4 by @chz31 (2022-06-05 21:46 UTC)

<p>Thanks! I’ll try that, but I could not find information about this method. Can you send me an introduction of vtkOrientedImageData?</p>

---

## Post #5 by @chz31 (2022-06-05 21:58 UTC)

<p>Thank you, Steve! What I did successfully is to use <code>slicer.util.arrayFromVolume</code> to get the np array for all rgb images, and then create a single-image volume for each image using <code>slicer.util.updateVolumeFromArray(outputNode, singleImageArray)</code>. From each single-image volume, I then get the vtkImage data and export it as tiff/png.</p>
<p>This is still relatively fast, but being able to loop through the original multi-image <code>vtkImageData</code> would be most straightforward and efficient.</p>
<p>However, I could not find a way to directly loop through a multi-image <code>vtkImageData</code>. Can you give me some suggestions  about how to do it, or maybe what I did about building a volume for each image is proper?</p>

---

## Post #6 by @mau_igna_06 (2022-06-06 07:58 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="23704">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>vtkOriemtedImageData</p>
</blockquote>
</aside>
<p>Here you have code with explamations</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/vtkSegmentationCore/vtkOrientedImageData.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/vtkSegmentationCore/vtkOrientedImageData.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/vtkSegmentationCore/vtkOrientedImageData.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/vtkSegmentationCore/vtkOrientedImageData.cxx</a></h4>


      <pre><code class="lang-cxx">/*==============================================================================

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

==============================================================================*/

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/vtkSegmentationCore/vtkOrientedImageData.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Mauro</p>

---

## Post #7 by @chz31 (2022-06-06 18:23 UTC)

<p>I figured what I did wrong. In addition to the dimensions and <code>AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 3)</code> as you suggested, I also forgot to set up the component number for the vtk array. of the rgb image using <code>SetNumberOfComponents</code>. I did:</p>
<pre><code class="lang-auto">channel_count =3
vtk_arr.SetNumberOfComponents(channel_count) #vtk_arr is the vtkDataArray from the flattened np image array of the single RGB image
</code></pre>
<p>Then I successfully output a slice of cropped image! Thanks!</p>

---

## Post #8 by @mau_igna_06 (2022-06-06 18:40 UTC)

<p>I think that’s veey fantastix</p>

---
