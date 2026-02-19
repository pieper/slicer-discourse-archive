---
topic_id: 23088
title: "3D Slicer Accurate Heart Chambers Segmentation"
date: 2022-04-22
url: https://discourse.slicer.org/t/23088
---

# 3D slicer accurate heart chambers segmentation

**Topic ID**: 23088
**Date**: 2022-04-22
**URL**: https://discourse.slicer.org/t/3d-slicer-accurate-heart-chambers-segmentation/23088

---

## Post #1 by @Qazi (2022-04-22 13:40 UTC)

<p>Hi</p>
<p>I need to segment atria and ventricles, their lumen, walls reasonably accurately so as to measure their volumes subsequently. I used paint tool and then" segment statistics" to do this. but doing segmentation for each part of heart separately takes quite a lot time. Is there a quick way to do segmentation of all parts of heart together in a quicker way? If there are more than one ways, please share all. I ll like the simplest ones though as I am not the computer guy <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Secondly, for osirix I had to scale down data to 50% and then further more scaling down. In osirix I use values for x=1, y=1 and section interval value (=calculated by my presdesigned excel sheet). I cant see these x, y and section interval things in 3D slicer and hence the 3D image is very abnormally oblong/elongated in 3D slicer. How can I bring it back to normal 3D shape (of heart)?<br>
Thirdly, What addditional different features pyradiomics offer in relation to measurements? How is it useful?</p>

---

## Post #2 by @lassoan (2022-04-23 04:48 UTC)

<aside class="quote no-group" data-username="Qazi" data-post="1" data-topic="23088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/a4c791/48.png" class="avatar"> Qazi:</div>
<blockquote>
<p>Is there a quick way to do segmentation of all parts of heart together in a quicker way?</p>
</blockquote>
</aside>
<p>Yes, after some practice, you can segment all the heart chambers in a couple of minutes. See this tutorial for details:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="BJoIexIvtGo" data-video-title="Whole heart segmentation from cardiac CT in 10 minutes" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BJoIexIvtGo/maxresdefault.jpg" title="Whole heart segmentation from cardiac CT in 10 minutes" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="Qazi" data-post="1" data-topic="23088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/a4c791/48.png" class="avatar"> Qazi:</div>
<blockquote>
<p>Secondly, for osirix I had to scale down data to 50% and then further more scaling down.</p>
</blockquote>
</aside>
<p>If you have a CT with slices of 512x512 then you can downsample the image (e.g., using a spacing scale of 2.0) and also crop away irrelevant image regions using <code>Crop volume</code> module - without impacting accuracy of volumetric measurements. The downsampling and cropping are useful because they reduce the amount of data, thereby make all processing and visualization significantly faster.</p>
<aside class="quote no-group" data-username="Qazi" data-post="1" data-topic="23088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/a4c791/48.png" class="avatar"> Qazi:</div>
<blockquote>
<p>I cant see these x, y and section interval things in 3D slicer and hence the 3D image is very abnormally oblong/elongated in 3D slicer. How can I bring it back to normal 3D shape (of heart)?</p>
</blockquote>
</aside>
<p>I’m not sure what you mean by interval things, but DICOM images that you load into Slicer should appear without any distortion. Import original DICOM images using the latest Slicer Preview Release and let us know if you run into any issue.</p>
<aside class="quote no-group" data-username="Qazi" data-post="1" data-topic="23088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/a4c791/48.png" class="avatar"> Qazi:</div>
<blockquote>
<p>What addditional different features pyradiomics offer in relation to measurements? How is it useful?</p>
</blockquote>
</aside>
<p>pyradiomics can compute features that might be used for tissue characterization. Most likely not very relevant for cardiac CTs. What is the clinical problem you are trying to solve?</p>

---

## Post #3 by @Qazi (2022-04-23 09:17 UTC)

<p>Thanks very much <a class="mention" href="/u/lassoan">@lassoan</a>. I have mouse-hearts which I sectioned at 2micron thickness using a high resolution microscope (with, of course, microtomy). The data stack I got was around 2000 (section) images. I scaled down the data, as very heavy data crashes the different imaging programs. so I was able to reduce data size from the raw 40 GB to ~230MB. In osirix, when I import the same 230MB data as DICOM files, in the “calibrate the dataset” window,  it asks for x, y resolution and slice interval. If I enter Pixel x resolution =1mm Pixel y=1mm and slice interval as 1mm, then I get a highly elongated/oblong heart in 3D. But if I use x=1, y=1 and for slice interval if I use the “scaling factor” value calculated by my excel sheet taking into account the scaling down of data, it gives me a nice 3D image in osirix.<br>
Importing the same data into 3D slicer, gives me similar oblonged heart since I dont know how to change the “slice interval” to the one I used for osirix.<br>
My ultimate aim is that I need to segment the ventricles, atria to measure their volume, using 2D images, and then using “fill in between slices” effect, which gives me an oblong 3D segment (e.g. ventricle volume). I am just wondering if the volume measurements will be different if I have the oblong/elongated 3D-heart versus a nice 3D heart? If latter is the case, how can i insert the slicing interval  in 3D slicer as I used in the Osirix? which measurements will be more accurate?<br>
Moreover, I am just thinking that wouldnt it be even more accurate to have a segment quantification/segment stats without putting the slicing interval? not sure?</p>
<p>Thanks in advance for your time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e820f2af020f8ff1ae56a5fe47471b05cd483fa.png" data-download-href="/uploads/short-url/4lSYr0N0cqVsXH5eX11UiVlMT7Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e820f2af020f8ff1ae56a5fe47471b05cd483fa_2_690x321.png" alt="image" data-base62-sha1="4lSYr0N0cqVsXH5eX11UiVlMT7Y" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e820f2af020f8ff1ae56a5fe47471b05cd483fa_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e820f2af020f8ff1ae56a5fe47471b05cd483fa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e820f2af020f8ff1ae56a5fe47471b05cd483fa.png 2x" data-dominant-color="434348"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">944×440 87.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a544472562a65be9dcde4941e50a0ae4cc3d7ab8.jpeg" data-download-href="/uploads/short-url/nA14b0GGteqmTn6ya2NnKZPYB1S.jpeg?dl=1" title="LV Epicard vol" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a544472562a65be9dcde4941e50a0ae4cc3d7ab8_2_690x414.jpeg" alt="LV Epicard vol" data-base62-sha1="nA14b0GGteqmTn6ya2NnKZPYB1S" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a544472562a65be9dcde4941e50a0ae4cc3d7ab8_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a544472562a65be9dcde4941e50a0ae4cc3d7ab8_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a544472562a65be9dcde4941e50a0ae4cc3d7ab8_2_1380x828.jpeg 2x" data-dominant-color="78787B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LV Epicard vol</span><span class="informations">1920×1154 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-04-24 05:42 UTC)

<p>I would recommend to load the original DICOM, resample (and crop as much as you can) using Crop volume module, save it as a nrrd file, then use that nrrd file. There will be no distortion then.</p>
<p>If your computer does not have enough physical memory to load the entire data set at full resolution then make sure you have virtual memory that is a few times more than the full-resolution data size. On Windows, you can adjust virtual memory size in Windows system settings; on Linux this is called swap space; on macOS the size is increased on demand and you just need to make sure there is enough free disk space.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I know that ImageStacks can downsample large images without ever loading the full image. Do you provide a solution like this for DICOM images, too?</p>

---

## Post #5 by @pieper (2022-04-24 14:12 UTC)

<p>ImageStacks uses SimpleITK to read, so it should work for dicom as long as the file names follow a compatible scheme.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L638">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L638" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L638" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L638</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="628" style="counter-reset: li-counter 627 ;">
            <li>if self.reverseSliceOrder:</li>
            <li>  paths.reverse()</li>
            <li>
            </li>
<li>volumeArray = None</li>
            <li>sliceIndex = 0</li>
            <li>firstArrayFullShape = None</li>
            <li>for inputSliceIndex, path in enumerate(paths):</li>
            <li>  if inputSliceIndex &lt; extent[4] or inputSliceIndex &gt; extent[5]:</li>
            <li>    # out of selected bounds</li>
            <li>    continue</li>
            <li class="selected">  reader = sitk.ImageFileReader()</li>
            <li>  reader.SetFileName(path)</li>
            <li>  image = reader.Execute()</li>
            <li>  sliceArray = sitk.GetArrayFromImage(image)</li>
            <li>  if len(sliceArray.shape) == 3 and self.outputGrayscale:</li>
            <li>    # We convert to grayscale by simply taking the first component, which is appropriate for cases when grayscale image is stored as R=G=B,</li>
            <li>    # but to convert real RGB images it could better to compute the mean or luminance.</li>
            <li>    sliceArray = sitk.GetArrayFromImage(image)[:,:,0]</li>
            <li>  currentArrayFullShape = sliceArray.shape</li>
            <li>  if firstArrayFullShape is None:</li>
            <li>    firstArrayFullShape = currentArrayFullShape</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
