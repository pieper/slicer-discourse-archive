---
topic_id: 2714
title: "3D Model Of Only The Outer Surface Of A Bone 3D Model Of A B"
date: 2018-04-27
url: https://discourse.slicer.org/t/2714
---

# 3D model of only the outer surface of a bone+ 3D model of a bone

**Topic ID**: 2714
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/3d-model-of-only-the-outer-surface-of-a-bone-3d-model-of-a-bone/2714

---

## Post #1 by @saeed_mouloodi (2018-04-27 02:08 UTC)

<p>Hi,</p>
<p>I am very new with the 3D slicer, so my question might be so simple. Still, it is really appreciated if you could help me with it.</p>
<p>I have a DCOM data from CT of a bone (to say like femur). I am wondering how can I do the followings:</p>
<p><span class="hashtag">#1</span> I want a surface model of the bone to be created just only from the outer surface (without the inside of the bone to be considered). ONLY the outer surface</p>
<p><span class="hashtag">#2</span> How can I export a 3D model of that bone, representing the actual model of the bone? I don’t mind about the marrow inside the bone. just a solid model of the bone with the hollow inside will be great!</p>
<p>Many thanks,<br>
Saeed</p>

---

## Post #2 by @lassoan (2018-04-27 03:41 UTC)

<p>If the image quality is good enough then thresholding, smoothing, and inverted island removal may produce good enough results. See detailed description here: <a href="https://discourse.slicer.org/t/2d-3d-fill-tool/2682">2D/3D fill tool</a></p>
<p>If image quality is very low and/or bone density is low then you may need to use Grow from seeds effect (growing bone from seed regions), as described here: <a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960/15">Bone segmentation to create 3D-printable STL</a></p>
<p>Exporting to 3D-printable STL file and many other tips are described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials</a>.</p>

---

## Post #3 by @saeed_mouloodi (2018-04-27 04:29 UTC)

<p>Dear Andras,</p>
<p>Thank you very much for your prompt reply! I will follow the instruction and information provided, and if I face any concerns, I will come back to you again.</p>
<p>Really appreciated!<br>
Saeed</p>

---

## Post #4 by @lassoan (2018-05-23 04:49 UTC)

<p>A post was split to a new topic: <a href="/t/export-segmentation-to-fea-software/2893">Export segmentation to FEA software</a></p>

---

## Post #5 by @saeed_mouloodi (2018-05-25 05:39 UTC)

<p>Dear Andras,</p>
<p>I followed all the discussions you have had with the other regarding creating a 3D model of a bone, generating 3D mesh, and eventually importing into FEA.</p>
<p>I should, however, say that I am still a bit confused about the process for making the model. Actually it is very hard to do so and it leads to inaccurate results. For example, segment mesher extension generates inaccurate meshes. I need a 3D model of the long bone, however the segment mesher creates a block of meshes, NOT to create the meshes on the segment of the bone.</p>
<p>Can you please help me with this, or if there is any tutorial video for this? As I concluded from the discussion in that specific forum, it is a incapability of 3D slicer? Is it? In case I need to use other software such as Mimics (even though I need to pay for it) please advise.</p>
<p>Many thanks,<br>
Saeed</p>

---

## Post #6 by @lassoan (2018-05-25 11:51 UTC)

<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>Actually it is very hard to do so and it leads to inaccurate results.</p>
</blockquote>
</aside>
<p>Development of a new segmentation workflow for a certain bone image, acquired with a specific imaging protocol, for a specific application always takes some time and practice. If the generated mesh surface looks good then segmentation task has been successfully completed. You may post an screenshot of your segmentation if you are not sure if the quality is good enough and we may give advice on how to improve it.</p>
<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>segment mesher extension generates inaccurate meshes</p>
</blockquote>
</aside>
<p>By default a coarse mesh is generated so that you get result quickly. Increase <code>--scale</code> parameter value in Advanced settings section to genereate a finer resolution mesh.</p>
<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>segment mesher creates a block of meshes, NOT to create the meshes on the segment of the bone.</p>
</blockquote>
</aside>
<p>Cleaver generates a “background” mesh so that you can simulate embedding your structures in some material (soft tissue, etc). If you don’t need these mesh elements, then don’t use them. Each cell is assigned to a segment, specified by <code>labels</code> cell attribute. You can use this attribute to assign material properties or remove parts of the mesh, etc.</p>
<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>Can you please help me with this, or if there is any tutorial video for this?</p>
</blockquote>
</aside>
<p>There is no video tutorial for Segment Mesher, but it would be greatly appreciated if you created one about your workflow, once you’ve figured out everything. You can of course post any specific questions here.</p>
<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>it is a incapability of 3D slicer? Is it?</p>
</blockquote>
</aside>
<p>It is not. 3D Slicer is very capable.</p>
<aside class="quote no-group" data-username="saeed_mouloodi" data-post="5" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>I need to use other software such as Mimics</p>
</blockquote>
</aside>
<p>Use any tool that work for you. Probably segmentation tools of Slicer are better than of Mimics, but Mimics has probably more meshing options and direct exporters for FEA software. So, if you and all your users can afford to buy Mimics then of course, give it a try. You may also try to export surface meshes (in STL, PLY, etc. format) and let your FEA software generate the volumetric mesh.</p>

---

## Post #7 by @saeed_mouloodi (2018-05-28 03:37 UTC)

<p>Your detailed and one-by-one replies are greatly appreciated.<br>
By the information provided, it seems a bit more understandable what steps I should follow right now.</p>
<p>I will proceed and have a try and hopefully after generating a successful result, I will make a video of it and will share it with you for further training program.</p>
<p>As I have been working with CAD+FEA for a long time, it seems that 3D slicer does not generate a 3D geometry (I mean a format file like STP or STEP) to be just a 3D model (not meshes). If it was a 3D model it could be imported into CAD for further modification. Therefore as I understand from your comments, 3D slicer generates meshes on the parts (such as bone for my case), and from the meshes I will be able to start my simulation in FEA.</p>
<p>Many thanks,<br>
Saeed</p>

---

## Post #8 by @lassoan (2018-05-28 04:15 UTC)

<aside class="quote no-group" data-username="saeed_mouloodi" data-post="7" data-topic="2714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> saeed_mouloodi:</div>
<blockquote>
<p>it seems that 3D slicer does not generate a 3D geometry (I mean a format file like STP or STEP) to be just a 3D model (not meshes)</p>
</blockquote>
</aside>
<p>Since 3D geometry, 3D model, mesh, part, solid are used for completely different things in different domains (3D modeling, FEA, medical image computing), and even in different software, but probably your understanding is correct.</p>
<p>Slicer’s Segment Mesher extension creates a volumetric mesh consisting of tetrahedral and wedge elements, ready for FEA analysis.</p>
<p>Mesh editing of surface or volumetric meshes in CAD software is of course a very common need, too. However, most software cannot easily reverse engineer arbitrary meshes into editable representations - there are significant limitations, such as maximum number of points, complexity of the surface, quality of the mesh.</p>
<p>It would be great to hear from you if you were able to use the volumetric mesh that Segment Mesher extension generated.</p>

---

## Post #9 by @saeed_mouloodi (2018-05-28 23:48 UTC)

<p>Thanks again dear Andras. I will start again to generate the meshes from the comments you have mentioned so far, and I let you know then. Probably it takes a bit of time, since I would like to try everything with enough details and with importing the model into FEA and running some simulation.</p>
<p>I hope that I will be able to produce good results as I expected.</p>

---

## Post #10 by @saeed_mouloodi (2018-06-05 02:46 UTC)

<p>Hi again,</p>
<p>As you mentioned I tried to generate the meshes on the long bone. Since my region of interest is ONLY the bone, I merely used TetGen in the “Meshing method” appeared in the inputs of segment mesher extension. Because as you highlighted Cleaver generates a mesh for background, which I am not interested in.<br>
However, when I click on the TetGen and then apply, it comes to an error.<br>
This is the step-by-step workflow I am doing:</p>
<ol>
<li>Loading the DICOM Files</li>
<li>Volume Rendering for selecting the boundaries of ROI</li>
<li>Cropp Volume and then apply</li>
<li>Segment Editor, add, selecting a threshold and apply, Using Scissors for removing some regions on the 3D view</li>
<li>Segment Mesher Extension, Input segmentation: Segmentation, Meshing method: TetGen, Output Model: create a new model, and then apply</li>
</ol>
<p>However, as I said it comes to an error. It says A self-intersection was detected. Program stopped.<br>
Hint: use -d option to detect all self-intersections.</p>
<p>I have uploaded a screenshot of the segmentation. Can you please help me through this and hopefully once it comes to a successful model, I will create a video tutorial-based for this forum future use.<br>
Additionally, how I am able to remove/delete the background meshes? And also, do I need to use label in the Editor module for labeling a bone? (using the yellow one?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21d3fbde4313032ad1a4003229efc9f717b50f36.jpeg" data-download-href="/uploads/short-url/4PfVElrW2LYOWUzAQ0t0Ir9FEfc.jpg?dl=1" title="3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3fbde4313032ad1a4003229efc9f717b50f36_2_690x366.jpg" alt="3D" data-base62-sha1="4PfVElrW2LYOWUzAQ0t0Ir9FEfc" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3fbde4313032ad1a4003229efc9f717b50f36_2_690x366.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3fbde4313032ad1a4003229efc9f717b50f36_2_1035x549.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3fbde4313032ad1a4003229efc9f717b50f36_2_1380x732.jpg 2x" data-dominant-color="7D7F84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D</span><span class="informations">1913×1016 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2018-06-05 04:05 UTC)

<p>TetGen: Unfortunately, TetGen is known not to be very robust. You may try to adjust meshing parameters.</p>
<p>Cleaver2: The background mesh should not be a problem. Each cell contains ID of the segment, so you can use vtkThreshold filter to extract cells corresponding to a specific material (see <a href="https://www.vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/Graphics/Python/SingleYoungsMaterialInterface.py">this example</a>).</p>

---

## Post #12 by @saeed_mouloodi (2018-06-08 06:26 UTC)

<p>Dear Andras,</p>
<p>Following a great deal of time and put significant effort along with several trial and error, eventually I have generated a 3D model from the DICOM files, which can be imported into any CAD software as I eventually end up with a STP file format. This facilitates importing the 3D model into any sort of FEA packages as well. I would like to mention that it requires using other software such as spacecliam simultaneously with 3D slicer. I am going to make a video from it and share with you and your team, since this has been asked numerous times and it might add value to the forum.</p>
<p>Saeed</p>

---

## Post #13 by @lassoan (2018-06-08 14:54 UTC)

<p>Sounds great, thank you! Looking forward to seeing your tutorial.</p>

---

## Post #14 by @Lorensen (2018-06-08 21:30 UTC)

<p>Gg v  <img src="https://emoji.discourse-cdn.com/twitter/saxophone.png?v=5" title=":saxophone:" class="emoji" alt=":saxophone:"><img src="https://emoji.discourse-cdn.com/twitter/saxophone.png?v=5" title=":saxophone:" class="emoji" alt=":saxophone:"><img src="https://emoji.discourse-cdn.com/twitter/saxophone.png?v=5" title=":saxophone:" class="emoji" alt=":saxophone:"> <img src="https://emoji.discourse-cdn.com/twitter/musical_note.png?v=5" title=":musical_note:" class="emoji" alt=":musical_note:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/headphones.png?v=5" title=":headphones:" class="emoji" alt=":headphones:"><img src="https://emoji.discourse-cdn.com/twitter/musical_note.png?v=5" title=":musical_note:" class="emoji" alt=":musical_note:"> Z</p>

---

## Post #15 by @cpinter (2018-06-11 13:50 UTC)

<p>Thank you Saeed for the effort! The video tutorial will indeed be much appreciated!</p>

---

## Post #16 by @timeanddoctor (2018-06-11 15:04 UTC)

<p>Thank you very much.</p>

---

## Post #17 by @doc-xie (2018-06-11 17:24 UTC)

<p>Looking forward to your exellent video!</p>

---

## Post #19 by @studia_ibm (2022-01-08 01:29 UTC)

<p>Where  can I find this video ?</p>

---
