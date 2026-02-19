---
topic_id: 22912
title: "I Want To Get The Surface Of A Mri Volume"
date: 2022-04-11
url: https://discourse.slicer.org/t/22912
---

# I want to get the surface of a MRI volume

**Topic ID**: 22912
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/i-want-to-get-the-surface-of-a-mri-volume/22912

---

## Post #1 by @mikhail_lermontov (2022-04-11 18:45 UTC)

<p>Hello,</p>
<p>I’m intern engineer in biomedical lab and I’m new with 3D Slicer and 3D visualization / 3D imaging.</p>
<p>I am currently working on MRI data of brains and I’m interesting only in the information located at the brain surface (blood vessels at the brain surface, lobes, sulcus). To be more accurate, I would like to project this 3D surface into a 2D plan in order to do some image processing on it.</p>
<p>Do you have any idea on how I can extrat the surface from my nifti datas with 3D Slicer?</p>
<p>Thank you very much</p>

---

## Post #2 by @pieper (2022-04-11 20:44 UTC)

<p>You may be able to use freesurfer for your project, since it projects each brain hemisphere to a sphere and I think they can project to a plane too.  You would need several steps if your mri isn’t already in a form freesurfer supports, but SynthSR is good for that.  Also freesurfer only does the brain part, so you would need to also segment the surface vessels another way, perhaps by thresholding near the surface as extracted by freesurfer.  The links below might help.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://surfer.nmr.mgh.harvard.edu/">
  <header class="source">

      <a href="https://surfer.nmr.mgh.harvard.edu/" target="_blank" rel="noopener">FreeSurfer</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://surfer.nmr.mgh.harvard.edu/landing/images/og_brain.png" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://surfer.nmr.mgh.harvard.edu/" target="_blank" rel="noopener">FreeSurfer</a></h3>

  <p>Software Package for Brain MRI Analysis</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/BBillot/SynthSR">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BBillot/SynthSR" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/6e376ab18cb291bd057bc32b70ca371a84eab4a11059391b555cd0942e49ec90/BBillot/SynthSR" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/BBillot/SynthSR" target="_blank" rel="noopener">GitHub - BBillot/SynthSR: A framework for joint super-resolution and image...</a></h3>

  <p>A framework for joint super-resolution and image synthesis, without requiring real training data - GitHub - BBillot/SynthSR: A framework for joint super-resolution and image synthesis, without requ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/" target="_blank" rel="noopener">NA-MIC Project Weeks</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mikhail_lermontov (2022-04-12 12:37 UTC)

<p>Thank you very much, I’ll investigate these links. About the segmentations : we’re not approaching segmentation by machine learning/deep learning.</p>
<p>The idea would be :</p>
<ul>
<li>from a nifti data, extract the surface points (I guess it’s possible with slicer ) and withdraw useless information (inside of the brain)</li>
<li>rotate the camera to a given plan looking at the region of the surface we want to observe</li>
<li>project this surface into the camera plan</li>
</ul>
<p>I would like to obtain a 2D image of my surface before using a segmentation of vessels on it. Since I don’t need an accurate segmentation, simple morphological tools should be enough (I use T1 MRI where the blood vessels are hypersignal).  My biggest issue is to extract the surface points of my MRI volume.</p>
<p>I’ve already found a python function that allows me to extract the surface mesh from volume node. Then from this surface mesh I can generate a segmentation node. And it would be greate if I could erode this segmentation node of 1 or 2 voxels.</p>
<p>I am not sure to be clear, but it’s the idea my project.</p>

---

## Post #4 by @lassoan (2022-04-13 21:42 UTC)

<p>You can extract the surface geometry using any of the skull stripping modules in Slicer (try the new <a href="https://github.com/lassoan/SlicerHDBrainExtraction#slicerhdbrainextraction">HD-BrainExtraction</a> extension) or any external tool.</p>
<p>You can then use <code>Probe volume with model</code> module to color it by a chosen volume’s voxels. I would recommend to segment the brain surface vessels in the 3D image and probe that volume, because you can segment the vessels more reliably and accurately in the original 3D volume then in some extracted surface.</p>
<p>If you need a flattened (2D) model then cut off the surface regions that you don’t need using Dynamic Modeler module, and use texture mapping to get 2D coordinates. If you don’t care too much about distortion then you can use <a href="https://vtk.org/doc/nightly/html/classvtkTextureMapToPlane.html">vtkTextureMapToPlane</a> or <a href="https://vtk.org/doc/nightly/html/classvtkTextureMapToSphere.html">vtkTextureMapToSphere</a>. If you want to flatten with minimal distortion then you can use some conformal mapping algorithm, such as the <code>Conformal texture mapping</code> module in SlicerHeart extension.</p>

---

## Post #5 by @mikhail_lermontov (2022-04-14 13:01 UTC)

<p>Thank you very much ! I’ve been trying some of the tools you gave me, it’s exactly what I need.</p>
<p>I have another question, is there a tool/reference python script to rotate the camera from a given angle, take a screen of the 3d view and then rotate again, and screen again? This for a whole round !</p>

---

## Post #6 by @pieper (2022-04-14 14:54 UTC)

<p>Yes, see the ScreenCapture module.</p>

---

## Post #7 by @mikhail_lermontov (2022-04-19 12:30 UTC)

<p>Thank you, I was able to do what I wanted.  Though I face a new problem, I want to withdraw the lighting effect from the 3D rendering in order to have a uniform lighting and withdraw reflects, is it possible? I saw a module name sandbox/lights that should do what I want but I struggle to build it from source and my extension manager doesn’t work.</p>
<p>I’m on fedora linux.</p>

---

## Post #8 by @pieper (2022-04-19 13:44 UTC)

<p>If you go to the advanced section of the Models module you can set the surface properties.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/models.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/models.html</a></p>

---

## Post #9 by @mikhail_lermontov (2022-04-20 12:15 UTC)

<p>I’ve already found such options, but I didn’t understand yet how to apply model changes to volume rendering ! I create model from a volume thanks to this : <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html" class="inline-onebox" rel="noopener nofollow ugc">Python FAQ — 3D Slicer documentation</a></p>

---

## Post #10 by @lassoan (2022-04-25 12:31 UTC)

<p>You can change appearance of models in <code>Models</code> module. You can change appearance of volume-rendered images in <code>Volume rendering</code> module.</p>

---

## Post #11 by @mikhail_lermontov (2022-05-12 11:24 UTC)

<p>Hey everyone,</p>
<p>I was able thanks to your advises to complete my objectives. Though, I have met an issue I would like to resolve. The spacing of MRI images is saved into the nifti files, I guess this spacing is then used for the 3d reconstruction of the structure through the volume rendering. Though, I would like to know if we could access to the new “voxel spacing” generated by the 3d view. To be more clear, I need to get the pixel spacing of screen captured images. Indeed, this information is needed for my registration task.</p>

---

## Post #12 by @lassoan (2022-05-12 12:12 UTC)

<p>Screen captures are typically not used for analysis, as they have low bit depth (8 bits per pixel; while most original images use at least 10-12), they may contain burnt-in annotations, etc. However, if you still want to use them then you can get the spacing by dividing the slice view’s field of view (FOV, in physical size) by the slice view’s dimensions (in pixels).</p>

---

## Post #13 by @mikhail_lermontov (2022-06-13 14:15 UTC)

<p>Thank you for the information, I answer one month later because I let this issue aside in order to work on other relevant parts of the project. Though, I’m going back to this problem : since I want only to segment to external surface of the brain cortex, how can I access to this information without using screen capture ? I use screen capture to make a binary segmentation of the surface (blood vessels and gray matter) but indeed, the bit depth is quite low and I lose many information about smaller blood vessels.</p>
<p>Ideally I would like to have a 2d flattened version of the surface, with a minimum of distorsion. Using screen capture in our project was somehow useful because we could imitate the view taking of the camera.</p>

---

## Post #14 by @lassoan (2022-06-13 19:57 UTC)

<p>Measuring the surface area, creating flattened surface with minimal distortion, and segmenting surface blood vessels are all quite different tasks. Slicer has solutions for all of them, but it is not clear what you want to do exactly. Could you attach a few screenshots and other illustrations that explains what your end goal is?</p>

---

## Post #15 by @mikhail_lermontov (2022-06-14 10:45 UTC)

<p>The main idea is to perform image registration between MRI datas and optical images in order to compare functional area mapping, here is an illustrate example :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/828aed9f2ba68968cfeeb4fecf1b59c2d43b9c1b.png" data-download-href="/uploads/short-url/iCPIR2tHC5h4N1672SqZAHszpNh.png?dl=1" title="registra" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/828aed9f2ba68968cfeeb4fecf1b59c2d43b9c1b_2_690x318.png" alt="registra" data-base62-sha1="iCPIR2tHC5h4N1672SqZAHszpNh" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/828aed9f2ba68968cfeeb4fecf1b59c2d43b9c1b_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/828aed9f2ba68968cfeeb4fecf1b59c2d43b9c1b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/828aed9f2ba68968cfeeb4fecf1b59c2d43b9c1b.png 2x" data-dominant-color="C89DBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registra</span><span class="informations">861×398 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The optical image is registered during chirurgical process while functional MRI is registered few hours before the operation.<br>
We have two type of MRI sequences : T1 and FLAIR, on T1 we see blood vessels better and on FLAIR sulcus better. On optical images, we can see sulcus and blood vessels, we got the idea to segment on T1 and optical images the blood vessels, in order to perform the registration. Here is anoter example below :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ff9ad55a19909ab40600761959bad06ec54d30.jpeg" data-download-href="/uploads/short-url/nPkTeAnkVe0febIS3mjcNLjtQ76.jpeg?dl=1" title="t1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6ff9ad55a19909ab40600761959bad06ec54d30_2_690x229.jpeg" alt="t1" data-base62-sha1="nPkTeAnkVe0febIS3mjcNLjtQ76" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6ff9ad55a19909ab40600761959bad06ec54d30_2_690x229.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6ff9ad55a19909ab40600761959bad06ec54d30_2_1035x343.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6ff9ad55a19909ab40600761959bad06ec54d30.jpeg 2x" data-dominant-color="80657D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">t1</span><span class="informations">1358×452 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Though, we do not want to perfom a 2D/3D registration (where optical image is the moving image), we want to perfom 2D/2D registration from the optical image to the surface of the reconstructed brain MRI. That’s why we need a flattened image of the reconstructed brain surface.</p>

---

## Post #16 by @lassoan (2022-06-19 00:18 UTC)

<p>Thank you, this additional information was very helpful.</p>
<p>The “proper” solution for this task would be 2D/3D registration.</p>
<p>You can compute your <a href="https://www.ipb.uni-bonn.de/html/teaching/photo12-2021/2021-pho1-20-camera-params.pptx.pdf">optical camera’s intrinsic and extrinsic parameters</a> from a set of corresponding points in the optical image and the 3D volume rendered image. Once you have your camera calibration, you can do anything: you can rectify the image (remove non-linear distortions) by using the intrinsic camera parameters, and then using the extrinsic camera parameters either project the 3D volume rendered image (or extracted 3D brain surface) to the camera image; or project the optical image to the brain surface. This would be fairly easy to implement if you can find a readily usable 2D/3D calibration algorithm implementation.</p>
<p>Alternatively, you could compute the camera intrinsic parameters using a standard camera calibration in OpenCV (very well-established method). Then you could compute extrinsic parameters (camera position and orientation) fully automatically using 2D/3D image registration (align the volume-rendered image with the optical image). ITK registration framework could be usable for this: ITK has similarity metrics and optimizer, the only non-trivial part is that you need to incorporate the volume rendering in the registration process.</p>

---
