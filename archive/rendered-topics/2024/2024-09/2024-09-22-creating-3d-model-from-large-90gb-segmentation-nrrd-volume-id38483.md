---
topic_id: 38483
title: "Creating 3D Model From Large 90Gb Segmentation Nrrd Volume"
date: 2024-09-22
url: https://discourse.slicer.org/t/38483
---

# Creating 3D model from large (90GB) segmentation (NRRD volume)

**Topic ID**: 38483
**Date**: 2024-09-22
**URL**: https://discourse.slicer.org/t/creating-3d-model-from-large-90gb-segmentation-nrrd-volume/38483

---

## Post #1 by @Tyler (2024-09-22 14:04 UTC)

<p>So I have a nrrd volume about 90 Gb in size, I can segment this fine but converting the segmentation to model via export would throw the error of out of memory ( although I have plenty of memory left (tried on one machine with 512gb memory and another one with 128gb but excessive 512 virtual memory set).<br>
Is this some known limitation of the vtk converter module eventually?</p>
<p>Second approach I tried is to split the nrrd into two halves that slightly overlap. Thinking I could segment and convert to model with the exact same workflow/settings this would give me to geometries that I can flawlessy merge afterwards. Apparently the overlapping geometry parts exhibit a different topology though so merging wouldnt work.</p>
<p>So it seems the vtk conversion isnt mathematically accurate in creating the very same model twice of the same source volume? Is that the case? if so, why?</p>

---

## Post #2 by @pieper (2024-09-22 16:19 UTC)

<aside class="quote no-group" data-username="Tyler" data-post="1" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/35a633/48.png" class="avatar"> Tyler:</div>
<blockquote>
<p>model via export would throw the error of out of memory</p>
</blockquote>
</aside>
<p>It probably takes more memory than you think to perform the conversion.  There are many options like changing the smoothing parameters, using surface nets instead of the default pipeline, etc.  Try downsampling the volume to see what sizes can be handled by your machine (either CropVolume on the source data or change the segmentation resolution).</p>
<aside class="quote no-group" data-username="Tyler" data-post="1" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/35a633/48.png" class="avatar"> Tyler:</div>
<blockquote>
<p>Apparently the overlapping geometry parts exhibit a different topology though so merging wouldnt work.</p>
</blockquote>
</aside>
<p>This is probably due to the smoothing and decimation operations that operate differently with different boundary conditions.  You could turn off all smoothing and they should match.  Then maybe you can merge and smooth the result but it may not be a great approach.</p>

---

## Post #3 by @muratmaga (2024-09-22 16:23 UTC)

<aside class="quote no-group" data-username="Tyler" data-post="1" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/35a633/48.png" class="avatar"> Tyler:</div>
<blockquote>
<p>So I have a nrrd volume about 90 Gb in size, I can segment this fine but converting the segmentation to model via export would throw the error of out of memory ( although I have plenty of memory left (tried on one machine with 512gb memory and another one with 128gb but excessive 512 virtual memory set).</p>
</blockquote>
</aside>
<p>How do you know you have plenty of memory left? Did you trace the Slicer’s memory consumption during the process? Our rule of thumb is 4-6 times more memory than your dataset size, and even your 512GB computer is below that requirement.</p>
<p>Does your segmentation encompass the whole volume? If not, then instead of splitting into two parts, crop the volume to its minimum extend (you can use the SplitVolume in SegmentEditorExtraEffects, if you don’t know how to do that) and then try converting the model.</p>
<p>Also, often downsampling by factor of 2 has almost no significant effect on the model’s geometry and works much faster.</p>

---

## Post #4 by @Tyler (2024-09-22 17:09 UTC)

<p>Thank you dearly for the reply and suggestions.</p>
<p>How or where could I disable the smoothing in this case? Which settings are used, the 3D Visualization ones or the surface creation from labelmaps?</p>
<p>I saw the available virtual memory wasnt used fully in the process, tried multiple times and with different 3D Slicer builds too.</p>
<p>I already am at the lowest desired resolution, cropped tightly to the necessary boundaries of the volume too.</p>
<p>My goal is to reduce visible the voxel stepping but still maintaining the tiniest possible details.</p>
<p>So is there some different approach to this, like splitting the segmentation instead of the volume and generate the geometry from there, ensuring a coherent topology?</p>
<p>Thanks again, both of you.</p>

---

## Post #5 by @muratmaga (2024-09-22 17:52 UTC)

<aside class="quote no-group" data-username="Tyler" data-post="4" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/35a633/48.png" class="avatar"> Tyler:</div>
<blockquote>
<p>My goal is to reduce visible the voxel stepping but still maintaining the tiniest possible details.</p>
</blockquote>
</aside>
<p>I think you can empirically test this very easily. Crop out a small region where you have the smallest detail you want to preserve, then create different downsampled volumes and extract models out of them and see if the difference is noticeable to you.</p>
<aside class="quote no-group" data-username="Tyler" data-post="4" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/35a633/48.png" class="avatar"> Tyler:</div>
<blockquote>
<p>How or where could I disable the smoothing in this case?</p>
</blockquote>
</aside>
<p>These are controlled under the Show3D button of segment editor. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>

---

## Post #6 by @Tyler (2024-09-22 18:08 UTC)

<p>Did that already, I can deal with the slight stepping.</p>
<p>I managed to get the model out in two parts, just the flawless merging didnt work as I hoped. Ill check again with any smoothing disabled and see if that holds the topology intact despite the splitting</p>

---

## Post #7 by @muratmaga (2024-09-22 18:12 UTC)

<p>If you want full control over model generation, you can export your segmentation as a labelmap and run the Model Maker module on it:</p>
<p><a href="https://slicer.readthedocs.io/en/5.6/user_guide/modules/modelmaker.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/5.6/user_guide/modules/modelmaker.html</a></p>

---

## Post #8 by @pieper (2024-09-22 18:20 UTC)

<p>We might have more suggestions if you send screenshots or more description of the source data.</p>
<p>if you are just thresholding you might try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/grayscalemodelmaker.html">GrayscaleModelMaker</a> module.  If there are parts you don’t want to include you can use masking in the Segment Editor.</p>

---

## Post #9 by @Tyler (2024-09-22 18:37 UTC)

<p>Ill prepare a detailed explanation with screens.<br>
Thanks for the help and effort!</p>

---

## Post #10 by @lassoan (2024-09-23 04:57 UTC)

<p>It is expected to have some artifacts near the data boundary, as algorithms often need information in a small neighborhood around the processed position. Near the dataset’s boundary, algorithms extrapolate the data, but of course the extrapolation is not exactly the same as the real data.</p>
<p>A common solution is to use “ghost cells”: you extend your data a little bit beyond the region of interest (these extra data elements are the “ghost cells”), perform the processing, and then clip your results to the region of interest.</p>
<p>Your workflow could be: cut up your data set into 2-3 pieces, make each piece overlap a little bit with its neighbor, process each piece, then cut off the overlapping regions from each processing result (e.g., Dynamic modeler module’s clipping tools). If you need to remove seams between the pieces then you can merge the models (e.g., use append polydata filter to put all pieces into one data object, and then use clean polydata filter to merge coincident points). All these steps can be Python scripted, which allows you to partition the data into many pieces (not just cut into 2, but for example cut into 3x3x3 = 27 pieces).</p>

---

## Post #11 by @Tyler (2024-09-23 06:34 UTC)

<p>Thats exactly what I did/tried, the excessive overlap deleted but still the remainders wouldnt perfectly align in topology.</p>
<p>Ill prepare more info and let you know.</p>

---

## Post #12 by @Tyler (2024-09-26 11:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f81af5c37be366aee4a1d9341558c36c70087a40.png" data-download-href="/uploads/short-url/zoQaNL7w8otCDCYjMhBAQDAPOjm.png?dl=1" title="690d1dcf87295638d44995f0eec98ba0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81af5c37be366aee4a1d9341558c36c70087a40_2_531x500.png" alt="690d1dcf87295638d44995f0eec98ba0" data-base62-sha1="zoQaNL7w8otCDCYjMhBAQDAPOjm" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81af5c37be366aee4a1d9341558c36c70087a40_2_531x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81af5c37be366aee4a1d9341558c36c70087a40_2_796x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81af5c37be366aee4a1d9341558c36c70087a40_2_1062x1000.png 2x" data-dominant-color="7C7C7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">690d1dcf87295638d44995f0eec98ba0</span><span class="informations">1214×1143 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So this  is what I get when  I use the segmentation to 3d model workflow. Theres lots of memory left in the process. (Yes, other processes use more ram fine, so I dont assume its a faulty memory issue.)</p>
<p>I tried the labelmap to model maker workflow, different error but seems also memory related.</p>
<p>So far I didnt succeed to to create just pieces of the whole model and merge it later on.</p>
<p>More screens and reports soon.</p>

---

## Post #13 by @muratmaga (2024-09-26 16:04 UTC)

<p>I don’t think it is a faulty memory issue, but possibly a memory fragmentation problem. My understanding you can hit OOM error for the array, if there is no contiguous memory address space for the size of the array you are creating. So you might have 300GB of RAM available but if these are split in 100GB chunks, you cannot create an array of 101GB in size. Or so my basic understanding goes.</p>
<p>This is something operating system supposed to do it for you, and I think a simple test is to reduce your data a little bit (like 10-15% in axes) and retry. That will reduce the memory consumption almost 50%. If it works, you are really hitting a memory problem. If not, then there is something else is going on.</p>
<p>To try that you need to use the ResampleScalarVolume module (since crop volume only resamples in integer factors).</p>

---

## Post #14 by @lassoan (2024-09-27 12:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>To try that you need to use the ResampleScalarVolume module (since crop volume only resamples in integer factors).</p>
</blockquote>
</aside>
<p>“Crop volume” module uses “Resample Scalar/Vector/DWI Volume” module under the hood and supports scaling by any factor (not only integer). The main advantage of using “Crop volume” module is that it performs the two most common methods for reducing image size (cut off irrelevant parts of the image + lower the resolution) in one step.</p>

---

## Post #15 by @muratmaga (2024-09-27 14:34 UTC)

<p>True. I keep forgetting about that.<br>
<a class="mention" href="/u/tyler">@Tyler</a> if you want to downsample 15% you can put factor of 1.15 in CropVolume. It is easier to use…</p>

---

## Post #16 by @Tyler (2024-09-30 05:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07fb90252d1188d13af8a007480dfc32ef1c63bd.jpeg" data-download-href="/uploads/short-url/18CjrMuURa2XphPGg0TIoyIWYl7.jpeg?dl=1" title="6dd0e5ca24d440dad6c3a32b5126259d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07fb90252d1188d13af8a007480dfc32ef1c63bd_2_690x424.jpeg" alt="6dd0e5ca24d440dad6c3a32b5126259d" data-base62-sha1="18CjrMuURa2XphPGg0TIoyIWYl7" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07fb90252d1188d13af8a007480dfc32ef1c63bd_2_690x424.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07fb90252d1188d13af8a007480dfc32ef1c63bd_2_1035x636.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07fb90252d1188d13af8a007480dfc32ef1c63bd_2_1380x848.jpeg 2x" data-dominant-color="CF905F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6dd0e5ca24d440dad6c3a32b5126259d</span><span class="informations">1920×1182 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So this is the result of using label maps to model maker workflow for both halves with same exact settings.<br>
I assume the smoothing is causing the difference again.</p>
<p>I am now testing the downsampling again, although I fear I will loose surface definition…</p>

---

## Post #17 by @Tyler (2024-09-30 09:02 UTC)

<p>…and Resample Scalar/Vector/DWI Volume terminated with an unknown exception…</p>

---

## Post #18 by @muratmaga (2024-09-30 15:46 UTC)

<p>Well all I can say, if you share your scene with the data, and the specific steps you are doing, I can try to run it on a larger memory computer.</p>

---

## Post #19 by @muratmaga (2024-10-01 20:22 UTC)

<p>OK, I can replicate this crash in a system with 1TB RAM. While it is throwing a memory error, probably something else causing this. I am not sure if anyone will be able to debug this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5c34401f58e9e1e60d2a749fb22c11233e7cf73.jpeg" data-download-href="/uploads/short-url/uv23t2vgUt1bHntyIicm9fNdCEz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5c34401f58e9e1e60d2a749fb22c11233e7cf73_2_690x399.jpeg" alt="image" data-base62-sha1="uv23t2vgUt1bHntyIicm9fNdCEz" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5c34401f58e9e1e60d2a749fb22c11233e7cf73_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5c34401f58e9e1e60d2a749fb22c11233e7cf73_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5c34401f58e9e1e60d2a749fb22c11233e7cf73_2_1380x798.jpeg 2x" data-dominant-color="786974"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1113 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However your other memory crashes are probably indeed out of memory errors.</p>
<ol>
<li>I took your data (~2.5GB) and designate is as the master volume.</li>
<li>Over sampled the segmentation geometry by factor of 4. (during this time memory usage of Slicer reached as high as 300GB).</li>
<li>Created a segment using threshold range of 12750-Max. During this memory usage of Slicer reached 420-460GB range transiently. When the task was finished Slicer’s memory usage was around 350GB range.</li>
<li>I went to Segmentation module, and choose to export the model to scene. It worked for while with memory usage hovering between 350-450GB, and then Slicer crashed with this error.</li>
</ol>
<p>As you can see at times you are coming already close to the physical limits of the memory on your system. So resampling and other may be indeed crashing due to OOM. However, this (crash during model export) does seem like a real issue.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #20 by @pieper (2024-10-04 14:00 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="19" data-topic="38483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>1TB RAM. While it is throwing a memory error, probably</p>
</blockquote>
</aside>
<p>Probably this is still an out of memory issue.  Even with 1TB of memory some allocations may fail due to fragmentation.  You can try with an even bigger memory machine (google and amazon have machines with like 11 TB or so) or you can just add a bunch of swap space.</p>
<p>If it still fails I suggest building in debug and getting a stack trace of the failed allocation.</p>

---

## Post #21 by @muratmaga (2024-10-04 15:32 UTC)

<p>I don’t have acccess to commercial cloud, but will add 1TB swap and see if this replicates.</p>

---

## Post #23 by @muratmaga (2024-10-04 18:54 UTC)

<p>Actually I tried with the new surface nets/smoothing option enabled, and everything worked fine, up to a point. Model is supposedly generated and saved into the scene, I can look up it is properties. It is over 600M polygons.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc81e801203491d3e2eb299e56a013f178c1605.png" data-download-href="/uploads/short-url/t4JG95Ltg1bIB7yL4qkWgmCFt9b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbc81e801203491d3e2eb299e56a013f178c1605_2_389x500.png" alt="image" data-base62-sha1="t4JG95Ltg1bIB7yL4qkWgmCFt9b" width="389" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbc81e801203491d3e2eb299e56a013f178c1605_2_389x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc81e801203491d3e2eb299e56a013f178c1605.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc81e801203491d3e2eb299e56a013f178c1605.png 2x" data-dominant-color="EFF1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">517×663 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But no model is being displayed in 3D viewer.  There is an error about display properties:</p>
<pre><code class="lang-auto">Switch to module:  "ImageStacks"
Switch to module:  "Data"
GetItemName: Failed to find subject hierarchy item by ID 27


Switch to module:  "SegmentEditor"
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1
void qMRMLSegmentationGeometryWidget::setReferenceImageGeometryForSegmentationNode() : Reference image geometry of Affenschaedel_0000_Segmentation is set to ' -0.0086287;0;0;0.01294305;0;-0.0086287;0;0.01294305;0;0;0.0086287;-0.01294305;0;0;0;1;176;3655;600;3671;312;5811; '
Switch to module:  "Segmentations"
Warning: In vtkMRMLSegmentationDisplayNode.cxx, line 302
vtkMRMLSegmentationDisplayNode (0x5f51020): vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=2.25.166211090335523915802933448538484626475, return default


void qMRMLSegmentationDisplayNodeWidget::updateSelectedSegmentSection() : No display properties found for segment ID  "2.25.166211090335523915802933448538484626475"
Warning: In vtkMRMLSegmentationDisplayNode.cxx, line 302
vtkMRMLSegmentationDisplayNode (0x5f51020): vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=2.25.166211090335523915802933448538484626475, return default


void qMRMLSegmentationDisplayNodeWidget::updateSelectedSegmentSection() : No display properties found for segment ID  "2.25.166211090335523915802933448538484626475"
virtual double qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(vtkIdType) const : Input item is invalid
Warning: In vtkMRMLSubjectHierarchyNode.cxx, line 2156
vtkMRMLSubjectHierarchyNode (0xb85a3c0): GetItemDataNode: Invalid item ID given


Switch to module:  "Data"
</code></pre>
<p>Right now I am saving it as PLY, it has been over 30GB and still going on.</p>
<p><a class="mention" href="/u/tyler">@Tyler</a> so things are working, but the resultant model will be so big am not sure what you can do with it.</p>

---

## Post #24 by @Tyler (2024-10-04 19:58 UTC)

<p>Ill try that, I assumed the new surface nets option is less accurate though?</p>

---

## Post #25 by @muratmaga (2024-10-04 19:59 UTC)

<p>I have not noticed any issues with it to make me thing it is any less accurate.</p>

---

## Post #26 by @Tyler (2024-10-04 20:01 UTC)

<p>ill make a comparison then with the halved part too</p>

---

## Post #27 by @Tyler (2024-10-06 16:24 UTC)

<p>tried with the surface nets option (not smoothing) and same error.</p>

---
