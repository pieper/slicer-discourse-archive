# Extract systematic volumes, quantify their and export their stl models

**Topic ID**: 19302
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/extract-systematic-volumes-quantify-their-and-export-their-stl-models/19302

---

## Post #1 by @qubalee (2021-08-23 01:00 UTC)

<p>Hi there!</p>
<p>I am currently working on a volume and need to slice it into subvolumes (smaller, i.e., Rubik’s Cube), quantify each subvolume, and export it as a .stl model. I need also to increase/decrease the number of subvolumes each time. Is there any way to do this on 3D Slicer with less time and effort?</p>
<p>Thank you in advance</p>
<p>Abdullah</p>

---

## Post #2 by @qubalee (2021-08-24 08:24 UTC)

<p>I managed to slice my volume into 623 stacked tiffs (cubes). I need to know how to automatically segment each file and export it as .obj file. This is going to help in reducing the time and effort. I appreciate any help from you.</p>
<p>I will share everything related to this topic later on.</p>
<p>Thanks in advance<br>
AA</p>

---

## Post #3 by @pieper (2021-08-24 13:35 UTC)

<p>Sure, you can do that if you piece together examples from the Script Repository.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node</a></p>

---

## Post #4 by @qubalee (2021-08-24 15:43 UTC)

<p>Many thanks, <a class="mention" href="/u/pieper">@pieper</a><br>
I think that I have a problem with the scripts. I need to know how to load my multiple-stack tiff files (as a batch) and how to use these scripts <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=10" title=":sweat_smile:" class="emoji" alt=":sweat_smile:">.</p>
<p>Any advice is highly appreciated!</p>

---

## Post #5 by @pieper (2021-08-24 22:59 UTC)

<aside class="quote no-group" data-username="qubalee" data-post="4" data-topic="19302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qubalee/48/9314_2.png" class="avatar"> qubalee:</div>
<blockquote>
<p>how to use these scripts <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">.</p>
</blockquote>
</aside>
<p>I think the best advice would be to try some of the programming tutorials.  It takes some practice to learn how the scripts work but once you have the hang of it they script repository is a goldmine of useful tricks to automate everything in the application.  For tiff stacks you might look at the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/ImageStacks">ImageStacks</a> module and code in the SlicerMorph extension.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>

---

## Post #6 by @qubalee (2021-08-25 01:25 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a><br>
Thank you so much for your reply.<br>
I tried to go through the documentation before posting this topic, but I realized that is so long way to do. Running the files one by one would be faster than learning without a guide. What I really need is just to repeat the steps giving below on all the samples showing in the picture.</p>
<p>The steps include:<br>
1- segmenting white and black features<br>
2- exploring STL files<br>
3- taking the volume data of each segment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dfdbab5da695b180196479be900043e9127331.jpeg" data-download-href="/uploads/short-url/axwt57GqNCLZLjPCvnYnkQNwIuJ.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49dfdbab5da695b180196479be900043e9127331_2_381x500.jpeg" alt="slicer" data-base62-sha1="axwt57GqNCLZLjPCvnYnkQNwIuJ" width="381" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49dfdbab5da695b180196479be900043e9127331_2_381x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dfdbab5da695b180196479be900043e9127331.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dfdbab5da695b180196479be900043e9127331.jpeg 2x" data-dominant-color="EAECED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">551×722 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-08-25 02:18 UTC)

<p>Do you want really want to split the volume to slices and export each slice into a separate STL file? That does not sound right. What is your end goal? What images are you working with? What analysis would you like to do? What do you plan to do with the hundreds of STL files?</p>
<p>If you just want to compute cross-sectional areas along a vessel then you can find several modules for that in VMTK extension.</p>

---

## Post #8 by @qubalee (2021-08-25 02:33 UTC)

<blockquote>
<p>Do you want really want to split the volume to slices and export each slice into a separate STL file? That does not sound right.</p>
</blockquote>
<p>I have already separated volumes and would like to quantify and export STL files.</p>
<blockquote>
<p>What is your end goal? What images are you working with? What analysis would you like to do? What do you plan to do with the hundreds of STL files?</p>
</blockquote>
<p>We are conducting qualitative and quantitative analyses of burrows on 632 cubes. Burrows have already been segmented in another software (binary tiff files) and we need to segment and quantify burrows and the surrounding materials in the 3D slicer. For the STL, we need to for qualitative analysis. The whole thing is a part of the research we are doing to investigate burrow quantification.</p>
<p>Thank you</p>

---

## Post #9 by @lassoan (2021-08-25 02:56 UTC)

<aside class="quote no-group" data-username="qubalee" data-post="8" data-topic="19302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qubalee/48/9314_2.png" class="avatar"> qubalee:</div>
<blockquote>
<p>We are conducting qualitative and quantitative analyses of burrows on 632 cubes</p>
</blockquote>
</aside>
<p>Could you tell a bit more about what kind of burrows are you analyzing? Could you post a few typical images? It is important for us to understand your end goal, because without that we can only offer help to solve small subproblems that you identify, which often end up being irrelevant because it turns out there is a different, better overall approach.</p>
<blockquote>
<p>I have already separated volumes and would like to quantify and export STL files.</p>
</blockquote>
<p>Do you have many small 3D cubic structures and you want to export each as a separate STL file? Or you want to export slice by slice?</p>
<aside class="quote no-group" data-username="qubalee" data-post="8" data-topic="19302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qubalee/48/9314_2.png" class="avatar"> qubalee:</div>
<blockquote>
<p>For the STL, we need to for qualitative analysis.</p>
</blockquote>
</aside>
<p>Doing quantitative analysis on surface meshes is generally much more difficult than on labelmaps. What kind of analysis would you like to do? Is there any metric that you need to compute and not already provided by Segment Statistics module? What software do you plan to use for analyzing the segmented structures?</p>

---

## Post #10 by @qubalee (2021-08-25 03:51 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you so much for your reply. Please check the attached image to see what I am talking about.<br>
We know exactly what we are doing, but we need to accelerate the process of volume quantification. In other words, how to repeat the steps given below to be automatically applied on all the other samples? if that is not possible in the 3D slicer, I have to find another software or do it one by one in the 3D slicer<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b237bccdaeeeb2e3bbd2a754d12cba3de8db2393.jpeg" data-download-href="/uploads/short-url/pqApdME2QCQOLiiNh2ja7RqP6KL.jpeg?dl=1" title="burrows" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b237bccdaeeeb2e3bbd2a754d12cba3de8db2393_2_564x500.jpeg" alt="burrows" data-base62-sha1="pqApdME2QCQOLiiNh2ja7RqP6KL" width="564" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b237bccdaeeeb2e3bbd2a754d12cba3de8db2393_2_564x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b237bccdaeeeb2e3bbd2a754d12cba3de8db2393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b237bccdaeeeb2e3bbd2a754d12cba3de8db2393.jpeg 2x" data-dominant-color="767676"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">burrows</span><span class="informations">766×679 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
.</p>
<blockquote>
<p>The steps include:<br>
1- segmenting white and black features<br>
2- exploring STL files<br>
3- taking the volume data of each segment</p>
</blockquote>
<p>Thank you</p>

---

## Post #11 by @lassoan (2021-08-25 04:09 UTC)

<p>Is this a picture of one cube? Do you have a large volume that contains 632 of these cubes? Or does this cube contain 632 small islands?</p>
<p>Are the STL files that you want to export flat (each one is created from a single slice) or a 3D blob, or a tree structure?</p>
<p>How do you plan to quantify the STL files? What metrics do you need to compute?</p>
<aside class="quote no-group" data-username="qubalee" data-post="10" data-topic="19302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qubalee/48/9314_2.png" class="avatar"> qubalee:</div>
<blockquote>
<p>if that is not possible in the 3D slicer, I have to find another software or do it one by one in the 3D slicer</p>
</blockquote>
</aside>
<p>Slicer is designed to be extremely flexible, it bundles a couple of very powerful libraries, and you can install any of the hundreds of thousands of Python packages from PyPI, so it is very likely that you can implement your entire analysis in Slicer/Python.</p>

---

## Post #12 by @qubalee (2021-08-25 04:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is this a picture of one cube? Do you have a large volume that contains 632 of these cubes? Or does this cube contain 632 small islands?</p>
<p>Are the STL files that you want to export flat (each one is created from a single slice) or a 3D blob, or a tree structure?</p>
<p>How do you plan to quantify the STL files? What metrics do you need to compute?</p>
</blockquote>
</aside>
<p>The picture is for one cube (one sample) after I segmented, and generated it through the 3D slicer. Therefore, it was a tiff stack file and it was generated to STL from each cube (tiff stacked file) after running the Segment Statistics module.</p>
<blockquote>
<p>so it is very likely that you can implement your entire analysis in Slicer/Python.</p>
</blockquote>
<p>Yes, exactly! This is why I am here.</p>
<p>Although I read many ppt files in the documentation, still I don’t know how to load the stack tiff files, process them and export the data.</p>

---

## Post #13 by @lassoan (2021-08-25 14:53 UTC)

<ul>
<li>You can load a TIFF stack the same way as the PNG stack is loaded in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-file">this example</a>. If the TIFF stack contains a binary labelmap then set <code>{"singleFile": False, "labelmap": True}</code> options.</li>
<li>Set spacing (voxel size) of the volume using <code>SetSpacing</code>
</li>
<li>Import the labelmap volume to segmentation as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-segmentation-from-a-labelmap-volume-and-display-in-3d">here</a>.</li>
<li>Quantify segmentation as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#quantifying-segments">here</a>.</li>
<li>Export model segmentation to model node should not be necessary because you can do all quantifications in using existing Slicer modules and Python scripting. If you want to export STL files anyway then:
<ul>
<li>Export segmentation to model node as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node">this example</a>.</li>
<li>Save model node to file as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-node-to-file">here</a>.</li>
</ul>
</li>
</ul>

---
