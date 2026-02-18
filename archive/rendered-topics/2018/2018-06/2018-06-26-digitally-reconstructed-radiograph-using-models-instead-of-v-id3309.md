# Digitally Reconstructed Radiograph Using Models Instead of Volumes

**Topic ID**: 3309
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/digitally-reconstructed-radiograph-using-models-instead-of-volumes/3309

---

## Post #1 by @_jmichael (2018-06-26 18:16 UTC)

<p>Is it possible using Slicer to create a simulated x-ray image, similar to a digitally reconstructed radiograph, that takes 3D models as its input rather than volumetric data (i.e. CT scans)? I’m envisioning a scenario in which 3D models (e.g. STL files) of one or more bones/implants/tools etc. can be placed in a 3D scene, assigned x-ray attenuation values, and an x-ray image simulated? Solutions that require the use of python are viable options for me.</p>
<p>I know it’s possible to generate a digitally reconstructed radiograph from a CT scan as per the post linked to below, but wasn’t sure if it’s possible to do that using a more simplified model of a finite number of structures each with constant x-ray attenuation. I know it’s possible to convert surface models to volumetric data and then generate a DRR of those volumes, but that seems like a fairly inefficient solution (computationally) compared to something that can calculate ray-triangle intersections directly.</p>
<p>Thanks in advance for your help!</p>
<aside class="quote quote-modified" data-post="1" data-topic="2010">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5e925/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/generate-digitally-reconstructed-radiograph-from-3dct/2010">Generate digitally reconstructed radiograph from 3DCT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello again, 
I would like to create some digitally reconstructed radiographs (DRR) in slicer from come 3DCt data that I have to compare to actual radiograph images that I have acquired. I saw one thread here: 


that talked about how to do it. At the end, Andras suggested installing the plastimatch module for more realistic DRR generation. I did install this extension (well I installed slicerRT which contains the plastimatch module) but I didn’t see the option anywhere to create a DRR. 
Ideally…
  </blockquote>
</aside>


---

## Post #2 by @Hamburgerfinger (2018-06-27 01:22 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dd5b2d51dc4504e200cee756186bc8374b13386.png" data-download-href="/uploads/short-url/8P0YjhXflZTky9zUOrv56Tlbd54.png?dl=1" title="22%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd5b2d51dc4504e200cee756186bc8374b13386_2_562x500.png" alt="22%20PM" data-base62-sha1="8P0YjhXflZTky9zUOrv56Tlbd54" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd5b2d51dc4504e200cee756186bc8374b13386_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd5b2d51dc4504e200cee756186bc8374b13386_2_843x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dd5b2d51dc4504e200cee756186bc8374b13386_2_1124x1000.png 2x" data-dominant-color="353332"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">22%20PM</span><span class="informations">1432×1274 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Try this out… seems to work reasonably well, but not sure if it qualifies as a “simulation”.</p>
<p>Create an empty image volume with Image Maker module.  Then import your .stl files or whatever and convert to segmentation (Segmentation module → import models).  Fill the voxels in the empty image volume with values for the linear attenuation coefficient (look these up for e.g. bone, soft tissue, lung tissue at the photon energy you’re interested in… here I used 10 kVp and looked up the values from the NIST database), for each tissue; you could script it or use a combination of Segmentations → “Mask Volume” and Add Scalar Volumes module in the GUI.  Finally, once you have your linear attenuation coefficient map (image) completed, use Simple Filters module → MeanProjectionImageFilter, or SumProjectionImageFilter.</p>
<p>The result is at the bottom right.</p>
<p>Best,<br>
Luke</p>

---

## Post #3 by @lassoan (2018-06-27 07:23 UTC)

<p>There are many options how to do this. The ideal solution depends on what your requirements are (how many input models you have, what resolution you need, how quickly the objects move, how complex their geometry is, what CPU and GPU are available, etc.).</p>
<p><a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a>’s suggestion is good. Generating binary or fractional volumes and render it using GPU is good, too (after the volumes are generated, GPU renderer can probably render the DRR image at a high frame rate).</p>

---

## Post #4 by @_jmichael (2018-06-27 15:43 UTC)

<p>Perfect. Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a>!</p>

---

## Post #5 by @Jan_Alexander (2020-05-13 16:35 UTC)

<p>Hi,</p>
<p>For me this is still unclear. I cannot find a module named ‘Image Maker’. I have no idea how I should create an empty volume and there is no clear explanation how to do this. I imported my .stl and exported this as a binary labelmap. Now I can find this back in the volume module. I cannot set any linear attenuation coefficient values though.</p>

---

## Post #6 by @lassoan (2020-05-16 19:27 UTC)

<p>You are almost there. You can already generate a DRR from this using Volume Rendering module. To make it look more realistic, you need to adjust transfer functions, which might be a bit hard if your voxel values are 0 and 1 (defaults for binary labelmaps).</p>
<p>I would recommend to convert the labelmap volume to scalar volume in Volumes module, then replace labelmap values by Hounsfield unit values (e.g., air -1000, bones and tools around 1000-2000) and add some noise using numpy. See this example for details:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_noise_to_image" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_noise_to_image</a></p>
<p>You can change label value 3 to Hounsfield unit 1200  by calling <code>voxels[voxels==3] = 1200</code>.</p>

---

## Post #7 by @phantom_gen (2024-11-12 11:42 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0f0942399a0c3e194f6df46f270a81d17e161e.png" data-download-href="/uploads/short-url/40dAcWf3NF8TuK0IxYnJiRM50om.png?dl=1" title="middeslab_projektion simpel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0f0942399a0c3e194f6df46f270a81d17e161e_2_625x500.png" alt="middeslab_projektion simpel" data-base62-sha1="40dAcWf3NF8TuK0IxYnJiRM50om" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0f0942399a0c3e194f6df46f270a81d17e161e_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0f0942399a0c3e194f6df46f270a81d17e161e_2_937x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0f0942399a0c3e194f6df46f270a81d17e161e_2_1250x1000.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">middeslab_projektion simpel</span><span class="informations">1280×1024 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi Guys!  Although this is an older topic I thought I give it a try since I have a similiar question:</p>
<p>The uploaded picture is an orthographic projection of a STL Design I did, which shall mimic a female breast parenchym in Mammography. I created the projection using an orthographic projection script in python.<br>
So much for the introduction, now here is my problem: I want to use 3D slicer to create a more advanced orthographic projection, like a DRR. I have voxelized the STL file and want every voxel that is filled, to have a certain attenuation A, and all the space inbetween (so all empty voxels) to have a certain attenuation B. Thanks in advance for your help!</p>

---
