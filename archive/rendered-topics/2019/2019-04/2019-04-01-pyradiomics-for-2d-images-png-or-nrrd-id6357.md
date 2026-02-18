# PyRadiomics for 2D images (png or nrrd)

**Topic ID**: 6357
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/pyradiomics-for-2d-images-png-or-nrrd/6357

---

## Post #1 by @MachadoL (2019-04-01 19:17 UTC)

<p>Hi everyone,</p>
<p>I am trying to extract radiomic features from 2D images (PNG or Nrrd) but I start to get a series of errors saying basically “3D array expected”. When I do that directly on slicer it works well.</p>
<p>I’m using a python script, and I am importing PyRadiomics, but no success so far.<br>
I’ve been adding “force2D”, “force2Dextraction”, and “force2Ddomension”, but none gave positive results.<br>
Does anyone have extracted 2D radiomic features using Python Pyradiomics package or have any guess on how to solve it all?</p>
<p>Thanks!</p>

---

## Post #2 by @fedorov (2019-04-01 20:20 UTC)

<p>Sounds like you are using this by calling extraction programmatically. Note that for using a 2d input, you would still need to read that 2d input into a 3d array with 3rd dimension = 1. Maybe that is what you are doing differently? Sharing the code snipped that you use would probably help.</p>

---

## Post #3 by @MachadoL (2019-04-02 17:32 UTC)

<p>Hey Andrey,</p>
<p>thanks, man.</p>
<p>Sorry for not posting parts of code as well. I thought it was a general problem. I guess, you got it right, though. I was inputting PNG files which are raw 2D files. I’ll try nrrd 3D files version and see how that goes. Thanks for the clue.</p>
<p>ty.</p>

---

## Post #4 by @fedorov (2019-04-03 21:33 UTC)

<aside class="quote no-group" data-username="MachadoL" data-post="3" data-topic="6357">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/machadol/48/3372_2.png" class="avatar"> MachadoL:</div>
<blockquote>
<p>I was inputting PNG files which are raw 2D files. I’ll try nrrd 3D files version and see how that goes.</p>
</blockquote>
</aside>
<p>Let me try to clarify - you do not need to save input image as NRRD. What you do need is to read the PNG image as a 3d image. When you instantiate the ITK reader, you can make a reader that reads a 2d image, or 3d image. If you read PNG with a 3d image reader, you should get a 3d image with the 3rd dimension size of 1. That is what you need to pass down to pyradiomics.</p>
<p>Note that for the questions about pyradiomics specifically, it is better if you use <a href="https://groups.google.com/forum/#!forum/pyradiomics">the pyradiomics google group</a>.</p>

---

## Post #5 by @JoostJM (2019-04-04 11:02 UTC)

<p><a class="mention" href="/u/machadol">@MachadoL</a>,which version of PyRadiomics are you using? Since Feb 20th, most of PyRadiomics does support 2D input. However, some parts (e.g. the LoG filter) still require 3D images. Furthermore, when using PNG images, there is a second (and more difficult) problem: color channels.</p>
<p>PyRadiomics is designed for feature extraction from scalar images (i.e. 1 value for each pixel/voxel). PNG is often encoded as RGB, i.e. 3 values per pixel. Therefore, to extract features from PNG, some preprocessing is required, converting the 3 RGB values into one (e.g. by taking the mean, or a specific channel).</p>

---

## Post #6 by @JoostJM (2019-04-04 11:05 UTC)

<p><a href="https://groups.google.com/forum/?utm_medium=email&amp;utm_source=footer#!searchin/pyradiomics/png%7Csort:date/pyradiomics/QLdD_qEw3PY/sTDsQDgOAgAJ" rel="nofollow noopener">This topic</a> on the PyRadiomics forum deals with this specific problem (although the solution is based on a version where PyRadiomics required 3D input always).</p>

---

## Post #7 by @MachadoL (2019-04-05 16:41 UTC)

<p>Great, <a class="mention" href="/u/fedorov">@fedorov</a>.</p>
<p>I got it!<br>
I’ll work on my things and let you know if everything goes allright.</p>
<p>Thanks again.</p>

---

## Post #8 by @MachadoL (2019-04-05 16:43 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a>,</p>
<p>I am using <strong>pyradiomics 2.1.2</strong>. I’ll try to update my package and let you guys know!</p>

---

## Post #9 by @Rodrigo_Castaldoni (2019-09-29 18:01 UTC)

<p>Hi, I guess I have the same problem. I have a Dicom image and a mask I made (just a numpy array). I transformed both of them to stk image file and then I used the joinSeries function to have the 3 dimensions.</p>
<p>Right now, I was able to make only the first-order features. I guess I can not make shape features, but I would like the GLCM, GLSZM, and so on…</p>
<p>I got the following error:</p>
<p>Thanks in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e45318b002b3600eb8e42176f53c39195b27f18.png" data-download-href="/uploads/short-url/8SRQFVkSTV7ORSotlhDBSU0Pxd6.png?dl=1" title="Selection_023" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e45318b002b3600eb8e42176f53c39195b27f18_2_690x311.png" alt="Selection_023" data-base62-sha1="8SRQFVkSTV7ORSotlhDBSU0Pxd6" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e45318b002b3600eb8e42176f53c39195b27f18_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e45318b002b3600eb8e42176f53c39195b27f18_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e45318b002b3600eb8e42176f53c39195b27f18_2_1380x622.png 2x" data-dominant-color="F5F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_023</span><span class="informations">1710×771 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @JoostJM (2019-09-30 09:28 UTC)

<p><a class="mention" href="/u/rodrigo_castaldoni">@Rodrigo_Castaldoni</a>,</p>
<p>What kind of DICOM file(s) do you have?  As it stands, I most often saw that DICOM is loaded as a 3D volume, even when it’s just a single file (e.g. single slice, but also X-Ray). JoinSeries may have the effect of concatenating in the 4th dimension, which is not really supported in PyRadiomics.</p>
<p>If you have volumetric DICOM with scalar pixel values (i.e. a grayscale image), I’d advise using a tool to convert them to a volumetric and SimpleITK-readable image format, such as NRRD (e.g. <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">dicom2niix</a>).</p>

---

## Post #11 by @JoostJM (2019-09-30 09:31 UTC)

<p>Additionally, the error you report is quite strange, as <code>P_gldm</code> is returned from the C-extension and should always be a numpy array. If the function fails, no array is returned, but the function will have thrown a <code>RuntimeException</code> instead, meaning that that line of code should not be reached.</p>
<p>Can you share the full log so I might look into this error?</p>

---

## Post #12 by @Rodrigo_Castaldoni (2019-09-30 17:14 UTC)

<aside class="quote no-group" data-username="JoostJM" data-post="11" data-topic="6357">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joostjm/48/1091_2.png" class="avatar"> JoostJM:</div>
<blockquote>
<p>function fai</p>
</blockquote>
</aside>
<p>First of all, thank you for the amazing package.</p>
<p>The problem was the numpy version. I was using the 1.14 instead of the 1.17. I checked somewhere the requirements and I guess it should work with the 1.14 version.</p>
<p>About the DICOM file, the shape of the pixel data is 2 dimensional (Did I answer the question?). Using the joinSeries I got the (512,512,1) or (1,512,512), I can’t remember right now.</p>
<p>I would like to ask, is there some information in the metadata that is necessary in order to calculate the features? I am asking because I would like to work just with a nump_array transformed to stk image object.</p>
<p>Should I calculate the shape2D features with the “force2D = True” parameter? I was wondering if make any sense at all these features in my case.</p>
<p>Sorry if these questions are too much specific. If you need some information I would be glad to provide.</p>
<p>Thank you for the fast answer and once more for the amazing package</p>

---

## Post #13 by @JoostJM (2019-10-01 08:24 UTC)

<p>Hi,</p>
<p>First of all, if your data is 2D, you don’t have to use the JoinSeries anymore. PyRadiomics now supports 2D input as well. Setting <code>force2D=True</code> has 2 use cases:</p>
<ol>
<li>In case of 3D image input, whole volume segmentation (multi-slice) - Deals with out-of-plane voxel anisotropy (i.e. same spacing in-plane, but different slice thickness). By removing angle offsets that move between slices in texture calculation, the assumption in the feature formulas that the distance between neighboring voxels is equal is met. Sometimes this is described as the 2.5D approach. Otherwise you’d need to deal with this by resampling, or taking the distance between neigbors into account (e.g. matrix weighting)</li>
<li>In case of 3D image input, single slice segmentation - Allows for calculating 2D features, including shape2D, even though the input is 3D (i.e. image has 3 dimensions, even though a dimension may have size 1).</li>
</ol>
<p>In your case, I’d say you fall under 2, so yes, I’d advise setting <code>force2D=True</code> and calculating shape2D.</p>
<p>P.s. this numpy version may need some investigating. Can you create an issue on the <a href="https://github.com/Radiomics/pyradiomics/issues" rel="nofollow noopener">PyRadiomics github</a>?</p>

---

## Post #14 by @Manju_Manju (2022-05-17 13:04 UTC)

<p>Sir Im trying segmentation on 2d images but im not able to get the output table of radiomic feature generator.can you please guide me</p>

---
