---
topic_id: 44800
title: "Segmentwithsam Module Not Working"
date: 2025-10-17
url: https://discourse.slicer.org/t/44800
---

# SegmentWithSAM module not working

**Topic ID**: 44800
**Date**: 2025-10-17
**URL**: https://discourse.slicer.org/t/segmentwithsam-module-not-working/44800

---

## Post #1 by @Jessica_de_Kort (2025-10-17 18:00 UTC)

<p>Hello! I am trying to use SegmentWithSAM module. I downloaded it through Extension Wizard, restarted Slicer a few times, and the module has no prompts or buttons on the left hand side of the screen. I looked at the error code and it mentions something about a bad git. I am not quite sure what that means or if that is the problem. Does anyone have any ideas on what to do?</p>
<p>Here is a photo of the interface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da2e111a0625d607d0cf432e01ccbdbf56da3e5c.png" data-download-href="/uploads/short-url/v86MKglYtqYkpphIsSStkjdj2kA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2e111a0625d607d0cf432e01ccbdbf56da3e5c_2_690x367.png" alt="image" data-base62-sha1="v86MKglYtqYkpphIsSStkjdj2kA" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2e111a0625d607d0cf432e01ccbdbf56da3e5c_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2e111a0625d607d0cf432e01ccbdbf56da3e5c_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da2e111a0625d607d0cf432e01ccbdbf56da3e5c_2_1380x734.png 2x" data-dominant-color="F8F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1676×893 61.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-10-17 18:39 UTC)

<p>I haven’t seen any SAM variant outperforming classic interactive segmentation tools for medical image segmentation. Therefore, I would not spend time with trying to figure out why this this extension fails.</p>
<p>In contrast, NNInteractive model is an AI-based interactive segmentation tool that actually works, and it works really well. For many segmentation tasks it performs much better than classic tools. You can often get a perfect segmentation of a bone from a single click. I would recommend to use it instead of any SAM-based tools. It is available in the Extensions Manager.</p>

---

## Post #3 by @Jessica_de_Kort (2025-10-22 15:49 UTC)

<p>The NNInteractive model needs a Nvidia GPU which we do not have yet. I will try NNInteractive once we have a Nvidia GPU. Thank you for your help.</p>

---

## Post #4 by @muratmaga (2025-10-22 16:17 UTC)

<aside class="quote no-group" data-username="Jessica_de_Kort" data-post="3" data-topic="44800">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jessica_de_kort/48/70344_2.png" class="avatar"> Jessica_de_Kort:</div>
<blockquote>
<p>I will try NNInteractive once we have a Nvidia GPU.</p>
</blockquote>
</aside>
<p>You can always give it a try on [MorphoCloud](<a href="https://morphocloud.org" rel="noopener nofollow ugc">https://morphocloud.org</a>). Brief instructions are here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/MorphoCloud/MorphoCloud/NNInteractive.MD">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/MorphoCloud/MorphoCloud/NNInteractive.MD" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/MorphoCloud/MorphoCloud/NNInteractive.MD" target="_blank" rel="noopener nofollow ugc">MorphoCloud/NNInteractive.MD</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/MorphoCloud/MorphoCloud/NNInteractive.MD" rel="noopener nofollow ugc"><code>MorphoCloud</code></a>
</div>


      <pre><code class="lang-md"># Setting &amp; Using NNInteractive extension on the MorphoCloud instances
nnInteractive is a deep learning-based framework for interactive segmentation of 3D images, allowing for fast voxel-wise segmentation using prompts like points, scribbles, bounding boxes, and lasso. It is a very useful and effective tool for rapid 3D segmentation with few clicks. It is a little different from the typical Slicer extensions, because it is a client and server application. While Slicer installation on the MOrphoCloud instances come with SlicerNNInteractive, that's only the **client**; you still have to install and then run the server each time you are planning to use NNInteractive. 

The official repository and most up-to-date instructions on how to install NNInteractive can be found at https://github.com/coendevente/SlicerNNInteractive/blob/main/README.md. This guide covers specific steps specific known to work with on MorphoCloud.

## Installing the server and running it.
There are multiple ways of running the server. On MorphoCloud we suggest you use the [**pip install** option as documented in the official documentation](https://github.com/coendevente/SlicerNNInteractive?tab=readme-ov-file#option-2-using-pip). 

1. Open a terminal window 
2. To create a python virtual environment specific to NNinteractive copy and paste this command to the terminal window (one-time only)
```
python3 -m venv /media/volume/MyData/nninteractive
```
3. To activate this python virtual enviroment copy and paste this command to the terminal window (everytime you want to run the server)
```
source /media/volume/MyData/nninteractive/bin/activate
```
4. To install the NNinteractive server copy and paste this command to the terminal window (one-time only)
```
pip install nninteractive-slicer-server
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/MorphoCloud/MorphoCloud/NNInteractive.MD" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @muratmaga (2025-10-23 02:30 UTC)

<p>Actually this is the correct link for the short tutorial: <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive.MD" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MorphoCloud/NNInteractive.MD at main · SlicerMorph/Tutorials · GitHub</a></p>

---
