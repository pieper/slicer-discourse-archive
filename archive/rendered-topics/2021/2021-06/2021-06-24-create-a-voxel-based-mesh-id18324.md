# Create a voxel based mesh

**Topic ID**: 18324
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/create-a-voxel-based-mesh/18324

---

## Post #1 by @ellismckenzielee (2021-06-24 14:28 UTC)

<p>Hi there,</p>
<p>I was wondering if it is possible to create a 3D mesh, where each voxel is an element using 3Dslicer? I have tried using the segmentmesher plugin but to no avail. At this point in time, I only need the mesh to validate an Abaqus subroutine. Hence, it does not to be smooth.</p>
<p>Thanks,<br>
Ellis</p>

---

## Post #2 by @lassoan (2021-06-24 14:58 UTC)

<p>SegmentMesher works well for creating volumetric meshes. Please give more specifics about what problems you had.</p>

---

## Post #3 by @ellismckenzielee (2021-06-24 15:40 UTC)

<p>Thanks for getting back so quick!</p>
<p>I found that I mainly had an issue with irregular shaped elements, particularly with high aspect ratios.</p>
<p>I’m first thresholding my image (which is already binary)  and then using segment mesher. The image comprises a bulk material with a single pore at the centre.</p>
<p>With cleaver, I tend to find that elements ‘stick out’ of the original image (in other words, the volume is no longer a cuboid). For example:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49940ed17c4a0ee512a036191499ac89cb8deaf8.png" alt="image" data-base62-sha1="auU4cZA7NuFJJhHiHh1zBfB87c4" width="525" height="396"></p>
<p>With Tetgen I’m just having trouble optimising at the moment, which I’m hoping I can resolve.</p>
<p>I just wondered if it is possible to create a voxel based mesh using slicer?</p>

---

## Post #4 by @lassoan (2021-06-25 04:23 UTC)

<p>Cleaver is designer for generating volumetric meshes from labelmap volumes. Its accuracy of reproducing a continuous spatial domain is limited by Shannon-Nyquist sampling theorem (i.e., edges will be always somewhat smoothed). You can increase the resolution to be high enough so that the smoothing become negligible, but then the computation time and memory usage (during computation) will increase dramatically.</p>
<p>Therefore, what you can get with Cleaver is something like this:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6b64eca392850889e5791ef3b1e0a49b27cb42.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6b64eca392850889e5791ef3b1e0a49b27cb42.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6b64eca392850889e5791ef3b1e0a49b27cb42.mp4</a>
    </source></video>
  </div><p></p>
<p>With these parameters:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69392f02e18edabca9a079dbafc0426dfeb6fdf2.png" data-download-href="/uploads/short-url/f0QEhJNdHRRTtqbh6PjJonyCLf4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69392f02e18edabca9a079dbafc0426dfeb6fdf2_2_376x500.png" alt="image" data-base62-sha1="f0QEhJNdHRRTtqbh6PjJonyCLf4" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69392f02e18edabca9a079dbafc0426dfeb6fdf2_2_376x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69392f02e18edabca9a079dbafc0426dfeb6fdf2_2_564x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69392f02e18edabca9a079dbafc0426dfeb6fdf2.png 2x" data-dominant-color="404040"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">646×859 99.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to create a volumetric mesh of a rectangular prism then probably the best is to generate the mesh programmatically (specify mesh point positions and cells). If you want to create arbitrary volumetric meshes from a surface mesh as input then instead of Cleaver you can use tetgen, tetwild, or hundreds of other mesh generators.</p>
<p>What is your overall goal?</p>

---

## Post #5 by @ellismckenzielee (2021-06-25 08:06 UTC)

<p>Thanks again.</p>
<p>So the aim of my project is to create an FE model from a real material microstructure. I am then hoping to assign material properties to each element based on the nearest pore within the microstructure. At the moment, since I am in the testing phase, the microstructure that I am using to create an FE model consists of a single pore. This will enable to me verify that all my scripts are working correctly when assigning the properties to elements. This will be completed in abaqus.</p>
<p>With Tetgen, I found that the mesh quality was quite good but I ended up with far too many elements (it crashed abaqus when I tried to load). I am now running cleaver with the parameters you sent, though my PC seems to be struggling! Am I correct in thinking that my segmented volume, consisting of a global threshold to separate the bulk from the porosity is a labelmap volume?</p>
<p>Kind regards,<br>
Ellis</p>

---

## Post #6 by @ellismckenzielee (2021-06-25 08:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46c47159dcc54ac9708524c52aca6220c484a477.png" data-download-href="/uploads/short-url/a62izOQFxdbqK8iTEM2pwvzSncj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46c47159dcc54ac9708524c52aca6220c484a477_2_690x373.png" alt="image" data-base62-sha1="a62izOQFxdbqK8iTEM2pwvzSncj" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46c47159dcc54ac9708524c52aca6220c484a477_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46c47159dcc54ac9708524c52aca6220c484a477_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46c47159dcc54ac9708524c52aca6220c484a477_2_1380x746.png 2x" data-dominant-color="3F5044"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1040 83.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The paramaters you suggested have returned a much more suitable mesh. I’m not sure why my choice of parameters was producing such a bad quality but I think this will be great for what I’m intending to do for the time being.</p>
<p>Thanks for your time and help.</p>
<p>Kind regards,<br>
Ellis</p>

---

## Post #7 by @lassoan (2021-06-25 13:46 UTC)

<aside class="quote no-group" data-username="ellismckenzielee" data-post="5" data-topic="18324">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/58956e/48.png" class="avatar"> ellismckenzielee:</div>
<blockquote>
<p>Am I correct in thinking that my segmented volume, consisting of a global threshold to separate the bulk from the porosity is a labelmap volume?</p>
</blockquote>
</aside>
<p>Correct, and Cleaver is designed to create meshes for FEA from such labelmaps. Tetgen and other mesh generators that require a surface mesh as input would struggle (and most likely fail) to create volumetric meshes from such complex geometry.</p>

---
