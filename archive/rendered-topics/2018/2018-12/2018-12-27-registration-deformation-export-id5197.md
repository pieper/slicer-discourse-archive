---
topic_id: 5197
title: "Registration Deformation Export"
date: 2018-12-27
url: https://discourse.slicer.org/t/5197
---

# Registration Deformation Export

**Topic ID**: 5197
**Date**: 2018-12-27
**URL**: https://discourse.slicer.org/t/registration-deformation-export/5197

---

## Post #1 by @miniBin (2018-12-27 04:31 UTC)

<p>I am doing the example from the Slicer Sequence Registration Module found online (<a href="https://github.com/moselhy/SlicerSequenceRegistration" rel="nofollow noopener">https://github.com/moselhy/SlicerSequenceRegistration</a>).</p>
<p>I can visualize the results but how do I export them?</p>
<p>How do I know how many nodes I have and how do I export their positions? Can you fit an equation to the deformation?</p>
<p>I will need to make code for updating grid motion.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2018-12-27 05:20 UTC)

<aside class="quote no-group" data-username="miniBin" data-post="1" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>how do I export them?</p>
</blockquote>
</aside>
<p>You can save all data that is in the scene from menu: File / Save.</p>
<aside class="quote no-group" data-username="miniBin" data-post="1" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>How do I know how many nodes I have and how do I export their positions?</p>
</blockquote>
</aside>
<p>Displacement field matches the fixed volume geometry (origin, spacing, axis direction, and extents). This information is stored in the displacement field transform file.</p>
<aside class="quote no-group" data-username="miniBin" data-post="1" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>Can you fit an equation to the deformation?</p>
</blockquote>
</aside>
<p>There is no equation to fit. What would you like to do?</p>
<aside class="quote no-group" data-username="miniBin" data-post="1" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>I will need to make code for updating grid motion.</p>
</blockquote>
</aside>
<p>You can apply the transform to any node in Slicer. For example, you can load a grid model and apply the transform to it - without writing any code. You can then view the deformed grid, save to file, etc.</p>
<p>Let us know if you need more detailed instructions.</p>

---

## Post #3 by @miniBin (2018-12-29 21:06 UTC)

<p>Hello and thank you for your reply.</p>
<p>I can export the txt file with the info but every time I open it, it crashes. I am using a macbook.</p>
<p>I need to extract the x y and z components of each node. Is there a way I can have less nodes so the txt file does not crash every time I try to open it?</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2018-12-29 21:57 UTC)

<p>Sequence Registration uses Elastix and the only standard file format it supports is displacement field, which is typically very large. You may need tens of gigabytes of memory space and if you don’t have it then you run out of memory (the application crashes). Upgrade your computer with more RAM, make available more space (at least 50-100GB) on your hard disk, and/or crop and resample your input image sequence.</p>

---

## Post #5 by @miniBin (2018-12-29 22:11 UTC)

<p>I see. I can eventually open the file…it takes a long time.</p>
<p>I am having trouble understanding the file. Screen capture below shows what I see. There are four columns with many rows, what do each column/row mean? I need x y z displacements that I can use in another program to tell the program to move the mesh at each time point.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6941926c2f55c14a7e4e1df3ba4c00370129a531.png" data-download-href="/uploads/short-url/f18CxJSvltvJdm2MnNhzTgbpojf.png?dl=1" title="deform_file" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6941926c2f55c14a7e4e1df3ba4c00370129a531.png" alt="deform_file" data-base62-sha1="f18CxJSvltvJdm2MnNhzTgbpojf" width="690" height="182" data-dominant-color="D9D9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">deform_file</span><span class="informations">1280×338 26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-12-30 03:07 UTC)

<aside class="quote no-group" data-username="miniBin" data-post="5" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>I need x y z displacements that I can use in another program to tell the program to move the mesh at each time point.</p>
</blockquote>
</aside>
<p>The file contains exactly that.</p>
<p>In the Save data dialog you can also choose to save the displacement field as a nrrd file: in the <em>File Format</em> column choose <em>Displacement field (.nrrd)</em>. Saving/loading will also be much faster if you don’t save the values in a text file (.tfm file).</p>

---

## Post #7 by @miniBin (2018-12-30 03:13 UTC)

<p>Thank you for your solution!</p>

---

## Post #8 by @miniBin (2018-12-31 00:24 UTC)

<p>Hello and sorry to bother again,</p>
<p>I have saved displacement field as .nrrd format but I cannot load it to matlab 2018b. I used the nrrdread.m file but it could not recognize the file. I do not know how to use python so is there another way to open it to view numerical data?</p>
<p>I need to extract x y and z numerical displacements.</p>
<p>Thank you again.</p>

---

## Post #9 by @brhoom (2018-12-31 00:40 UTC)

<p>I would try two things:</p>
<ol>
<li>
<a href="https://www.mathworks.com/help/matlab/ref/hdf5read.html" rel="nofollow noopener">matlab support hdf5</a>,  load the nrrd file in slicer and save it as transform. You can view hdf5 also using [hdfview].(<a href="https://www.hdfgroup.org/downloads/hdfview/#obtain" rel="nofollow noopener">https://www.hdfgroup.org/downloads/hdfview/#obtain</a>)</li>
<li>use the text format.</li>
</ol>

---

## Post #10 by @lassoan (2018-12-31 01:55 UTC)

<aside class="quote no-group" data-username="miniBin" data-post="8" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e79b87/48.png" class="avatar"> miniBin:</div>
<blockquote>
<p>used the nrrdread.m file but it could not recognize the file</p>
</blockquote>
</aside>
<p>It should work. If there was a problem then it msut be something trivial to fix. Maybe due to some minor syntax difference between Matlab versions. What error message did you get exactly?</p>
<p>Unless you are near the end of your career, it is probably a good idea to switch from Matlab to Python. Analyzing displacement field using Python can be a good learning exercise. Check out <a href="https://github.com/Slicer/SlicerJupyter">Slicer’s Jupyter notebooks</a>, too.</p>

---

## Post #11 by @miniBin (2018-12-31 03:28 UTC)

<p>I think I will make the transition to python. Thank you again for the extended help.</p>

---

## Post #12 by @labixin (2019-06-20 04:42 UTC)

<p>Hi,</p>
<p>I think I am doing the similar thing. I have saved displacement field as .nrrd format and loaded it to matlab 2018a. Maybe you need to modify the last sentence in nrrdread.m (the default setting is for 3D but the dvf is 4D array). Do you still use matlab or just make the transition to python? (I am new to python so I’d like to hear your suggestions~)</p>
<p>I need to extract x y and z numerical displacements of specific voxel points. But I am a bit confused about the coordinate definition (especially when the nrrdread.m contains matrix permutation). Did you ever verify the displacement of voxel located at specific position? Or how to check the displacement results?</p>
<p>Your help is highly appreciated!</p>
<p>Crayon</p>

---

## Post #13 by @labixin (2019-06-20 05:21 UTC)

<p>Hi everyone,</p>
<p>Thanks for your discussion. I have tried to register pre-operative ct (moving image) with post-operative ct (fixed image) using Plastimatch (B-spline deformable registration) and also Elastix. The resulting displacement field was saved as .nrrd format.</p>
<p>Also I have done segmentation of fixed image and exported the segment to STL file format.</p>
<p>I need to extract x y and z numerical displacements of specific voxel points (in fixed volume) related to my segment. I wonder when I export to STL files, which coordinate system should I choose?</p>
<p>I know from <a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a> and also the metadata that Displacement field is defined in LPS Coordinate system. So maybe I also need to export my stl file with LPS coordinate?</p>
<p>Sorry but I am just entangled in the coordinate definition which I think is quite important for the displacement extraction of specific points. Can I check the displacement results of specific points? Hope for some advice. Thank you all!</p>
<p>Crayon</p>

---

## Post #14 by @lassoan (2019-06-20 12:49 UTC)

<aside class="quote no-group" data-username="labixin" data-post="12" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Maybe you need to modify the last sentence in nrrdread.m</p>
</blockquote>
</aside>
<p><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrdread.m</a> supports reading of 4D volumes, so it should work as is. Let me know if you find any issues with it.</p>
<aside class="quote no-group" data-username="labixin" data-post="12" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I need to extract x y and z numerical displacements of specific voxel points</p>
</blockquote>
</aside>
<p>The displacement field volume contains exactly that. Each element in the 3D array is a 3-element vector.</p>
<p>What may be confusing is that Slicer stores elements in RAS coordinates, while the geometry of image saved to file is specified in LPS. Displacement vector elements are defined in RAS coordinates in Slicer and when we save a vector volume from Slicer, we do not alter the stored vector components (we don’t know if the vector components correspond to color, spatial coordinates, etc.). Image geometry is stored in LPS by most medical imaging software, that’s why we follow this convention, too. We should probably change Slicer to somehow know that vector components should be converted to LPS for displacement field images, but for now you can do this yourself by inverting the sign of the first two components of the displacement vector that you have read using nrrdread.</p>
<aside class="quote no-group" data-username="labixin" data-post="12" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I am a bit confused about the coordinate definition (especially when the nrrdread.m contains matrix permutation)</p>
</blockquote>
</aside>
<p>Fortunately, this is very simple: Image is specified in LPS physical space. You can convert between LPS and IJK array indexes by using <code>img.ijkToLpsTransform</code> provided by <code>nrrdread.m</code>.</p>
<aside class="quote no-group" data-username="labixin" data-post="13" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I wonder when I export to STL files, which coordinate system should I choose?</p>
</blockquote>
</aside>
<p>If you process data outside Slicer, I would recommend using LPS coordinate system.</p>
<aside class="quote no-group" data-username="labixin" data-post="13" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Can I check the displacement results of specific points?</p>
</blockquote>
</aside>
<p>In Slicer, displacement vector values at current mouse pointer position are shown in Transforms module’s Information section (“Displacement vector  RAS: (…, …, …)”).</p>
<p>If you exported a transform to a displacement field image and that image is shown in a slice viewer, you can also see the displacement values in the Data Probe window (in the bottom left corner).</p>

---

## Post #15 by @lassoan (2019-06-20 13:07 UTC)

<p>By the way, most probably everything would be much simpler to do in Slicer’s Python environment. If you describe what your end goal is, I can give specific advice about how to achieve that.</p>

---

## Post #16 by @labixin (2019-06-22 14:42 UTC)

<p>Thanks for your help. I want to combine intensity based registration with finite element method. My end goal is to modify the displacement vector field and then evaluate the new transform.</p>
<p>I will use the displacement of boundary node as boundary condition. And the position of boundary node is related to the segment (in fixed volume) which is exported to STL file in LPS coordinate. I know that the dvf defines the displacement of voxels in fixed volume. So I will first extract the displacements of specific voxel points. Then write back new displacements calculated by fem to generate new transform (may need some interpolation).</p>
<p>That’s why I am more concerned with coordinate definition, including the position and displacement of specific voxel points. Many thanks if you have any suggestions.</p>
<p>Best,<br>
Crayon</p>

---

## Post #17 by @labixin (2019-06-22 15:15 UTC)

<p>Thanks for the clarifications. I have succeeded in reading 4D transform using nrrdread.m you provided. But I don’t quite understand that “Displacement vector elements are defined in RAS coordinates in Slicer” and “for now you can do this yourself by inverting the sign of the first two components of the displacement vector that you have read using nrrdread”.</p>
<p>After loading the dvf (.nrrd) to matlab, it showed LPS coordinate (shown below)? Besides, when I located the displacement of specific point in matlab, the absolute value of three directions are all the same as viewed values at current mouse pointer position (“Displacement vector RAS: (…, …, …)”), except the sign of the first two components? I wonder which are the actual displacement results related to voxel points (of segment) defined in LPS coordinate?</p>
<p>Sorry for being entangled in the coordinate definition. I have got inspiration from this discussion thread (<a href="https://discourse.slicer.org/t/porting-a-transformation-from-matlab-to-slicer/868" class="inline-onebox">Porting a transformation from Matlab to Slicer</a>). But I was still not sure related to my own problem. Your help is highly appreciated!</p>
<p>Best,<br>
Crayon</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1a0a5ca1e09fca9322b8b0db9df28600ca22334.png" alt="dvf" data-base62-sha1="ytxfTf3r9jMlnIHDbgqvpPgazQ0" width="571" height="235"></p>

---

## Post #18 by @lassoan (2019-06-22 18:14 UTC)

<p>Slicer can compute for you the displacement at each surface mesh point and save it in the mesh: after you exported the displacement field to image volume in Transforms module, go to “Probe volume with model” module to compute displacement of each model point and save it in the model as point data. This output model must be saved in a file format that can store vector data associated with points: VTK or VTP (STL file can only store point positions and triangles, not the displacement vectors, so STL will not work).</p>
<p>You can find VTK and VTP file readers for Matlab, but it would be probably much more user-friendly to implement the whole registration workflow in Python. There are many free FEM solvers in Python (such as <a href="https://www.researchgate.net/deref/https%3A%2F%2Ffenicsproject.org">FEniCS</a>) that can be installed in recent Slicer Preview versions and directly used by Slicer modules.</p>
<aside class="quote no-group" data-username="labixin" data-post="17" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>except the sign of the first two components? I wonder which are the actual displacement results related to voxel points (of segment) defined in LPS coordinate?</p>
</blockquote>
</aside>
<p>Yes, conversion between LPS (left-posterior-superior) and RAS (right-anterior-superior) coordinates is simply inverting the sign of the first two components.</p>

---

## Post #19 by @labixin (2019-06-26 14:44 UTC)

<p>Thanks for the extended help. I think I will make the transition to python soon and will try to implement the whole workflow in python environment.</p>
<p>Now I have got modified displacement field calculated by fem and imported it back to slicer as transform (.nrrd format using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" rel="nofollow noopener">nrrdwrite.m</a>). I wonder if I have a contour/segment in moving image, can I apply transform to get a deformed one in fixed image? Then I could use Segment Comparison module in SlicerRT extension to compare the deformed contour/segment to the reference one delineated by radiation oncologist.</p>
<p>Sorry but I didn’t find relevant discussion thread which I could follow. Hope for some advice. Thanks a lot for your kindness.</p>
<p>Best,<br>
Crayon</p>

---

## Post #20 by @lassoan (2019-06-27 04:22 UTC)

<aside class="quote no-group" data-username="labixin" data-post="19" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I wonder if I have a contour/segment in moving image, can I apply transform to get a deformed one in fixed image?</p>
</blockquote>
</aside>
<p>You can load the displacement field as a Transform (in Add data dialog, choose “Transform” in Description column) and apply it to any node (image, segment, etc.) using Transforms module. If you want to do analysis, then it may be necessary to harden the transform on the node.</p>

---

## Post #21 by @Xiaogai_Li (2019-08-12 10:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What may be confusing is that Slicer stores elements in RAS coordinates, while the geometry of image saved to file is specified in LPS. Displacement vector elements are defined in RAS coordinates in Slicer and when we save a vector volume from Slicer, we do not alter the stored vector components (we don’t know if the vector components correspond to color, spatial coordinates, etc.). Image geometry is stored in LPS by most medical imaging software, that’s why we follow this convention, too. We should probably change Slicer to somehow know that vector components should be converted to LPS for displacement field images, but for now you can do this yourself by inverting the sign of the first two components of the displacement vector that you have read using nrrdread.</p>
<p><img src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/40/1965_2.png" alt="" width="20" height="20" role="presentation"> labixin:</p>
</blockquote>
</aside>
<p>Hi! I am a bit confused Andras says following “<strong>Displacement</strong> vector elements are defined in <strong>RAS</strong> coordinates in Slicer …”. But according to the link, <strong>Displacement field</strong> used Coordinate System <strong>LPS</strong>.</p>
<p>According to my test, seems Slicer output displacement field is indeed with LPS coordinate system, consistent with the link said. Then would be really appreciated if Andras <a class="mention" href="/u/lassoan">@lassoan</a>  could please explain the difference? Thank you very much.<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/984964cda975b1bbf8510c11d2200c3c1d100a83.png" data-download-href="/uploads/short-url/lJbOTCmDQkq6BvO71pSHSMLPZ99.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/984964cda975b1bbf8510c11d2200c3c1d100a83.png" alt="image" data-base62-sha1="lJbOTCmDQkq6BvO71pSHSMLPZ99" width="690" height="204" data-dominant-color="E6EFE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">856×254 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @lassoan (2019-08-12 13:15 UTC)

<p><strong>Transforms</strong> are written and read as LPS. Since Slicer uses RAS internally, there is an automatic conversion between RAS&lt;-&gt;LPS when reading/writing a transform file.</p>
<p><strong>Vector volumes</strong> can store color, displacements, etc. in their voxels and they are read/written to file without any modification.</p>
<p>If you export a transform to a vector volume in Transforms module then vectors will contain displacements in RAS coordinate system and since there is no conversion during read/write to file, if you save this volume, then the resulting file will contain displacement vectors in RAS. If you load this volume as a <em>transform</em> in Slicer or in most other software, they will all assume that the vectors are in LPS, so the displacement field will be incorrect.</p>
<p>We should probably distinguish between different kind of vector components in Slicer (color, spatial, etc.) and convert RAS&lt;-&gt;LPS automatically during file read/write if vectors store spatial information. Until this is implemented, you need to manually convert from RAS to LPS before you save a displacement field volume to file that you intend to use as transform.</p>

---

## Post #23 by @Xiaogai_Li (2019-08-12 14:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="22" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you export a transform to a vector volume in Transforms module then vectors will contain displacements in RAS coordinate system and since there is no conversion during read/write to file, if you save this volume, then the resulting file will contain displacement vectors in RAS. If you load this volume as a <em>transform</em> in Slicer or in most other software, they will all assume that the vectors are in LPS, so the displacement field will be incorrect.</p>
</blockquote>
</aside>
<p>Thank you very much for the explanation, but I am not sure if I understand correctly. The <strong>Vector volume</strong> I am interested in is a dense <strong>Displacement</strong> vector obtained by nonlinear registration in Slicer (i.e. not by reading any external but generated by Slicer internally). As Slicer uses RAS, I assume this Displacement vector should be in RAS. But what about when save it from Slicer? Will Slicer do as for an image file to convert LPS to RAS first, then convert to LPS when save? Or simply save to RAS without any converting? (then if indeed RAS without converting, my confusion is still according to my test, it seems Slicer saved Displacement Vector in LPS). Please correct if I am wrong. Thanks!</p>

---

## Post #24 by @lassoan (2019-08-12 15:02 UTC)

<p>Image grid (origin, spacing, axis directions) is always saved as LPS. Vector components in the voxel data are saved as is (if it was RAS in Slicer then it is RAS in the file, too).</p>

---

## Post #25 by @Xiaogai_Li (2019-08-12 16:35 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a> for your answer which sounds certain (indeed Image grid is saved LPS which is consistent to what I see). Just Disp grid is also LPS as it is align with the LPS image (used Paraview to verify). Perhaps I should reflect my testing procedure, maybe I made a mistake somewhere… Will come back if I figure out later. Thanks.</p>

---

## Post #26 by @lassoan (2019-08-12 18:47 UTC)

<p>Paraview completely ignores image axis directions, so it cannot be used for verification.</p>
<p>What are you trying to achieve? What is your current workflow?</p>

---

## Post #27 by @Xiaogai_Li (2019-08-12 22:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What are you trying to achieve? What is your current workflow?</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the remind regarding Paraview. Indeed seems it ignores axis directions. But my strategy is always to convert the image to RAI in Slicer (to get a TransformMatrix = Identity matrix), in this way, I would verify in Paraview that Slicer indeed export image file back to LPS.</p>
<p>My ultimate goal is to use the disp field to displace node coordinate of stl surface generated from Slicer. This stl surface when export from Slicer and import to Paraview, I could see it is in RAS.</p>
<p>Following image shows what I described above</p>
<ul>
<li>White gray shows the image exported from Slicer in mhd format (in LPS) and open in Paraview, then Thresholding to show the head geometry</li>
<li>Blue shows the stl surface generated from Slicer and open in Paraview (in RAS - make sense as this is generated in Slicer with RAS)</li>
</ul>
<p>Did I misunderstand something during the process? Thanks!</p>
<p><strong><img src="https://lh4.googleusercontent.com/z6xNKBTHIP25kSvCmu-MqlIUnhp-c-MzuHQ1AiOHpayTuEACs8__63Ni7mimEOn0YEm7ZwPgQgg6qlR0dMSlOHyeaVooriTO4IyBjCzicrRwldOj_5o6tR7-tT21yubPvkA15rVE" alt="" width="624" height="427" role="presentation"></strong></p>

---

## Post #28 by @lassoan (2019-08-13 03:11 UTC)

<p>For historical reasons, Slicer still saves STL files in RAS coordinate system by default. You can find the coordinate system definition in the STL header. We’ll probably change this default soon for consistency with other software (see this <a href="https://issues.slicer.org/view.php?id=4445">ticket</a>).</p>
<p>For now, you can use “Export to files” feature in Segment Editor/Segmentation modules and choose LPS for export (or save model and rotate it by 180deg to get it in LPS coordinate system).</p>
<p>Since Paraview ignores direction matrix and its support for volumetric images and dense displacement fields in general have been deteriorated in recent years, I only use Paraview for mesh visualization. I don’t know what coordinate system Paraview uses for mhd files.</p>
<aside class="quote no-group" data-username="Xiaogai_Li" data-post="27" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>My ultimate goal is to use the disp field to displace node coordinate of stl surface generated from Slicer.</p>
</blockquote>
</aside>
<p>This works very well in Slicer. You can apply the transform (it can be simple linear transform, bspline, displacement field, or a combination of these) to the model node. When you read the displacement field from a nrrd file, make sure to choose “Transform” in “Add data” window to load the field as a transform and not as a vector image.</p>

---

## Post #29 by @Xiaogai_Li (2019-08-13 06:46 UTC)

<p>Thanks! OK seems all clear: Indeed I misunderstood and my alignment should be just a coincidence (without awareness of my misunderstanding). Will reflect further on RAS&lt;-&gt;LPS in Slicer. With all the info you provided I should be able to sort out.</p>
<p>Thanks for the tip to export to LPS and great that Slicer will make effort updating to LPS.</p>
<p>Then just two short questions would be great if you could clarify:</p>
<ul>
<li>
<p>Orient Scaler Image In Slicer has 48 options like RAI, LPI also RAS and LPS. Is the RAS and LPS there the same as we are taking about here? (Shouldn’t be same because Slicer always reads in RAS? Then what is the difference between RAS Orientation and the RAS anatomical orientation?)</p>
</li>
<li>
<p>When save (scalar) image to mhd in Slicer, it saved to mhd+zraw (compressesed raw). Is there any way to save to mhd+raw (uncompressed)?</p>
</li>
</ul>

---

## Post #30 by @pieper (2019-08-13 15:17 UTC)

<p>Hi <a class="mention" href="/u/xiaogai_li">@Xiaogai_Li</a> -</p>
<aside class="quote no-group" data-username="Xiaogai_Li" data-post="29" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>Orient Scaler Image In Slicer has 48 options like RAI, LPI also RAS and LPS. Is the RAS and LPS there the same as we are taking about here? (Shouldn’t be same because Slicer always reads in RAS? Then what is the difference between RAS Orientation and the RAS anatomical orientation?)</p>
</blockquote>
</aside>
<p>Good question - perhaps a subtle point: <a href="https://www.slicer.org/wiki/Documentation/4.0/Modules/OrientScalarVolume">This one just reshuffles the pixels and then updates the origin and directions to match</a>.  So the resulting volume headers (nrrd or mha) can still be written as LPS or whatever.  I don’t use this module but I guess the purpose is to make it easier to export data to something like matlab that might expect a certain pixel layout in memory.</p>
<aside class="quote no-group" data-username="Xiaogai_Li" data-post="29" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>When save (scalar) image to mhd in Slicer, it saved to mhd+zraw (compressesed raw). Is there any way to save to mhd+raw (uncompressed)?</p>
</blockquote>
</aside>
<p>Sure, in the save dialog you can show the options and uncheck Compressed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78fd2d72fca194cb4c6da99f7393342f94172488.png" data-download-href="/uploads/short-url/hgjJ3UcnT7yXD9VQ9eKgWgtSP8I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78fd2d72fca194cb4c6da99f7393342f94172488_2_690x101.png" alt="image" data-base62-sha1="hgjJ3UcnT7yXD9VQ9eKgWgtSP8I" width="690" height="101" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78fd2d72fca194cb4c6da99f7393342f94172488_2_690x101.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78fd2d72fca194cb4c6da99f7393342f94172488_2_1035x151.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78fd2d72fca194cb4c6da99f7393342f94172488.png 2x" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×157 27.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #31 by @Xiaogai_Li (2019-08-13 16:13 UTC)

<p>Thanks a lot <a class="mention" href="/u/pieper">@pieper</a> for your reply! OK after reading the link you sent, I think the RAI, LPI,RAS and LPS in Slicer Orient Scalar Image module is indeed the same thing as we are discussing here on RAS and LPS. Interestingly, after some test, I realised that the RAI in Slicer Orient Image Module = LPS (anatomical orientation defined in <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a>). Hope some expert could confirm if this is indeed correct.</p>
<p>A great tip for saving uncompressed. Thanks a lot!</p>

---

## Post #33 by @Xiaogai_Li (2019-08-13 16:27 UTC)

<aside class="quote no-group" data-username="Xiaogai_Li" data-post="27" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the remind regarding Paraview. Indeed seems it ignores axis directions. But my strategy is always to convert the image to RAI in Slicer (to get a TransformMatrix = Identity matrix), in this way, I would verify in Paraview that Slicer indeed export image file back to LPS.</p>
<p>My ultimate goal is to use the disp field to displace node coordinate of stl surface generated from Slicer. This stl surface when export from Slicer and import to Paraview, I could see it is in RAS.</p>
<p>Following image shows what I described above</p>
<ul>
<li>White gray shows the image exported from Slicer in mhd format (in LPS) and open in Paraview, then Thresholding to show the head geometry</li>
<li>Blue shows the stl surface generated from Slicer and open in Paraview (in RAS - make sense as this is generated in Slicer with RAS)</li>
</ul>
<p>Did I misunderstand something during the process? Thanks!</p>
<p><strong><img src="https://lh4.googleusercontent.com/z6xNKBTHIP25kSvCmu-MqlIUnhp-c-MzuHQ1AiOHpayTuEACs8__63Ni7mimEOn0YEm7ZwPgQgg6qlR0dMSlOHyeaVooriTO4IyBjCzicrRwldOj_5o6tR7-tT21yubPvkA15rVE" alt="z6xNKBTHIP25kSvCmu-MqlIUnhp-c-MzuHQ1AiOHpayTuEACs8__63Ni7mimEOn0YEm7ZwPgQgg6qlR0dMSlOHyeaVooriTO4IyBjCzicrRwldOj_5o6tR7-tT21yubPvkA15rVE" width="" height=""></strong></p>
</blockquote>
</aside>
<p>A retrospective note (2019-08-13):</p>
<p>After more insightful info from <a class="mention" href="/u/lassoan">@lassoan</a> in a later post, need to update regarding this figure description:</p>
<ul>
<li>I made a mistake in the text description: white gray color should be the stl generated from Slicer which indeed is in RAS as the stl header says - a remind from <a class="mention" href="/u/lassoan">@lassoan</a> (Thanks!). Blue color should be the Thresholding of mhd image saved from Slicer indeed in LPS (as it is rotated to the stl in RAS).</li>
<li>Apparently this fig shown in Paraview can not tell anything about RAS and LPS (another mistake I made).</li>
<li>Realised my misunderstanding was sourced to misinterpret RAS and LPS (had the opposite in mind). <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox" rel="noopener nofollow ugc">Coordinate systems - Slicer Wiki</a></li>
</ul>
<p>Now seems all clear to me and appreciated very much all the insightful discussions.</p>

---

## Post #34 by @pieper (2019-08-13 16:52 UTC)

<aside class="quote no-group quote-modified" data-username="Xiaogai_Li" data-post="31" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>I realised that the RAI in Slicer Orient Image Module = LPS (anatomical orientation defined in <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a>). Hope some expert could confirm if this is indeed correct.</p>
</blockquote>
</aside>
<p>The two are related, but be sure to note that Orient Image (renamed Orient Scalar Volume in recent Slicers) shuffles the data and updates the origin and directions accordingly.  So the acronyms there refer to slice/row/column layouts.  You can see this in the Volumes module Information tab if for example you convert an axial scan to a coronal (the header values will change the volume cover the same extent and the same pixel values will be at the same spots in space).  The LPS/RAS difference in nrrd headers is related to the reference coordinate system used to encode points and vectors.  (Sorry it’s a bit hard to describe but I wanted to be sure it’s clear).</p>

---

## Post #35 by @lassoan (2019-08-14 05:31 UTC)

<aside class="quote no-group" data-username="Xiaogai_Li" data-post="31" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiaogai_li/48/4401_2.png" class="avatar"> Xiaogai_Li:</div>
<blockquote>
<p>I realised that the RAI in Slicer Orient Image Module = LPS</p>
</blockquote>
</aside>
<p>Yes, RAI in a mha file header means LPS. It is unclear if this inversion was intentional or somehow misinterpreted, see more details in <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1017">this discussion</a>.</p>

---

## Post #36 by @Xiaogai_Li (2019-08-14 13:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="35" data-topic="5197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, RAI in a mha file header means LPS. It is unclear if this inversion was intentional or somehow misinterpreted, see more details in <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1017" rel="noopener nofollow ugc">this discussion </a>.</p>
</blockquote>
</aside>
<p>Thanks for the confirmation and sharing the link (very illuminating discussions there!).</p>

---

## Post #37 by @lassoan (2022-03-17 00:39 UTC)

<p>A post was merged into an existing topic: <a href="/t/export-the-displacement-vector-to-matlab/22543/2">Export the displacement vector to matlab</a></p>

---
