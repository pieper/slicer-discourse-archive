# Showing real-time thermography images as overlay

**Topic ID**: 1610
**Date**: 2017-12-07
**URL**: https://discourse.slicer.org/t/showing-real-time-thermography-images-as-overlay/1610

---

## Post #1 by @thaenel (2017-12-07 15:32 UTC)

<p>I’m working on a combined visualization of an preoperative MRI image and intraoperative thermography images. The intraoperative thermography image (2D) is registered to the MRI image with a tracking system that utilises OpenIGTLink (the reason for this thread). Afterwards I create a visualisation of the thermography images by re-projecting them onto a surface that is reconstructed from the MRI image. This resulting 3D visualisation of the thermography image should be combined with an arbitrary visualisation of the MRI image. I plan to do this using image fusion.</p>
<p>I split up the whole visualisation pipeline into the following modules:</p>
<ul>
<li>
<em>Streaming</em> module that takes care of receiving the intraoperative thermography images and the tracking data (done)</li>
<li>
<em>Re-projection visualisation</em> module that creates the 3D visualisation of the thermography images</li>
<li>
<em>Image fusion</em> module that creates a single visualisation out of to the thermography visualisation and an arbitrary MRI visualisation (e.g. Direct Volume Rendering)</li>
</ul>
<p>I’ll create different threads for the <em>Re-projection</em> and the <em>Image fusion</em> module</p>

---

## Post #2 by @lassoan (2017-12-07 15:36 UTC)

<p>These features are all readily available in Slicer.</p>
<p>Streaming module = OpenIGTLinkIF.</p>
<p>Re-projection visualization module = VolumeResliceDriver module</p>
<p>Image fusion module = you set MR image as background and thermography visualization image as foreground image; you can tune colormap and thresholding setings in Volumes module</p>
<p>I would strongly recommend to complete all SlicerIGT user tutorials at <a href="http://www.slicerigt.org/wp/user-tutorial/">http://www.slicerigt.org/wp/user-tutorial/</a> to get an idea what Slicer/SlicerIGT can already do, but of course we are happy to answer any specific questions here.</p>

---

## Post #3 by @thaenel (2017-12-07 21:28 UTC)

<p>Thanks for your suggestions and creating a thread for me!</p>
<p>I looked at the tutorials and they don’t describe what I plan to do.</p>
<p>As I understand <em>Volume Reslice Driver</em> module positions a 2D image in the 3D scene given a continously updated transformation. That is not what I am trying to do.</p>
<p>The <em>Re/Back-projection visualisation</em> module should project (maybe re-projection is a translation error) the 2D image back onto a given 3D surface. Imagine a beamer that projects the 2D thermography image onto the surface that it depicts. As a result, each surface point should be colored according to its temperature. Slicer is able to create such a surface from the MRI image. E.g. for neuro surgery there are skull stripping extensions and surface models can be created from label maps / volumes.</p>
<p>vtkProjectedTexture achieves the same effect, but on vertices (not fragments). That is why, after implementing a prototype using only VTK, I decided to create a custom mapper. This mapper takes a model, an image and camera parameters and creates this desired visualisation (easy and fast GPU based implementation). As far as I understand Slicer and VTK I propapbly need to create my own display node type and a matching displayable manager.</p>
<p>For the <em>image fusion</em> module I was a bit short on description as well. I want to fuse two different 2D images / image sources that are based both on a visualisiation similar to the 3D view. I want to perform an off screen rendering of both 3D visualisations into 2D images. These images should then be fused using an algorithm similar to the one described in this paper <a href="http://ieeexplore.ieee.org/document/6423909" rel="nofollow noopener">http://ieeexplore.ieee.org/document/6423909</a>. The result should then be displayed on a camera aligned plane in the 3D view.</p>
<p>Some more information about me: I have a computer science background and I am mostly new to the medical imaging domain. The whole project I described is part of a minor thesis, that I am currently working on. The focus is more one the theoratical background and less on practical day-to-day usability.</p>

---

## Post #4 by @lassoan (2017-12-07 22:10 UTC)

<p>Thanks for the clarification. I assumed that you use MR thermometry and use slice visualization. Volume reslice driver module just reslices volumes, so it is not what you need.</p>
<aside class="quote no-group" data-username="thaenel" data-post="3" data-topic="1610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9fc348/48.png" class="avatar"> thaenel:</div>
<blockquote>
<p>I understand Slicer and VTK I propapbly need to create my own display node type and a matching displayable manager.</p>
</blockquote>
</aside>
<p>That’s correct.</p>

---

## Post #5 by @lassoan (2017-12-08 04:26 UTC)

<p>Your project sounds very exciting. There will be a project on medical infrared imaging on the <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW27_2018_Boston/README.md">upcoming Slicer Project Week at MIT in January</a> by <a class="mention" href="/u/carlos-luque">@carlos-luque</a> and others. It would be great if you could update us about your progress, or even come to the project week - you could accomplish a lot during a week there.</p>

---
