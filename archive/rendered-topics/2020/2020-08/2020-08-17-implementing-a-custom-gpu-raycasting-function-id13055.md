# Implementing a custom GPU raycasting function

**Topic ID**: 13055
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/implementing-a-custom-gpu-raycasting-function/13055

---

## Post #1 by @Zerfox (2020-08-17 20:04 UTC)

<p>Dear all,</p>
<p>Currently I am working on a 3D Slicer module in which I need to render isosurfaces and silhouettes.<br>
Right now I am using <code>vtkOpenGLGPUVolumeRayCastMapper</code> and setting a <code>vtkImageData</code> object as input data. The voxel values are modified continuously.</p>
<p>The isosurfaces generated using <code>vtkOpenGLGPUVolumeRayCastMapper</code> are nice, but I need to have more control over the render results. Especially when I want to combine the isosurfaces with silhouettes. I think I need to define my own ray-casting function that can be called by <code>vtkOpenGLGPUVolumeRayCastMapper</code> / <code>vtkGPUVolumeRaycastMapper</code>. Is something like this possible at this point in time? If so, what would be the best way to approach this or can someone point me to some good resources?</p>
<p>From what I understand, 3D Slicer is using a slightly modified version of VTK version 8.2.0. VTK 9.0 <a href="https://vtk.org/Wiki/VTK/ProgrammableMultiVolumeRendering" rel="nofollow noopener">was supposed to introduce</a> shader replacement functionality in <code>vtkGPUVolumeRaycastMapper</code>. I am getting a bit lost as the raycasting functionality has received a major overhaul in the past and I still encounter some older documentation while trying to search for an approach to my problem. For instance, for the CPU-based <code>vtkVolumeRayCastMapper</code> there appears to have been a <code>vtkVolumeRayCastFunction</code> superclass that could have been inherited.</p>
<p>My apologies if this has been asked numerous times or is supposed to be trivial. Getting to know the 3D Slicer and VTK ecosystem is quite overwhelming for me at the moment. It seems that I have difficulties finding the right search keywords.</p>
<p>Thanks in advance.</p>
<p>Kind regards,<br>
Rutger</p>

---

## Post #2 by @pieper (2020-08-17 20:22 UTC)

<p>Yes, you should be able to do that now using the PRISMRendering extension which gives you an easy way to work with custom shaders.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/61759657?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering" target="_blank" rel="noopener">ETS-vis-interactive/SlicerPRISMRendering</a></h3>

<p>Implementation of the PRISM customizable volume rendering framework as a 3D Slicer module - ETS-vis-interactive/SlicerPRISMRendering</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://journals.plos.org/plosone/resource/img/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0193636" target="_blank" rel="noopener">journals.plos.org</a>
  </header>
  <article class="onebox-body">
    <img src="https://journals.plos.org/plosone/article/figure/image?id=10.1371/journal.pone.0193636.strk&amp;size=inline" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0193636" target="_blank" rel="noopener">PRISM: An open source framework for the interactive design of GPU volume...</a></h3>

<p>Direct volume rendering has become an essential tool to explore and analyse 3D medical images. Despite several advances in the field, it remains a challenge to produce an image that highlights the anatomy of interest, avoids occlusion of important...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Let us know how it goes for you.</p>

---

## Post #3 by @lassoan (2020-08-17 21:05 UTC)

<p>Prism contains nice examples and infrastructure for getting additional inputs from other nodes, but if you just need a custom shader replacements then you can simply set those in the volume rendering node, as shown in these simpler examples: <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/VolumeRenderingSpecialEffects">https://github.com/PerkLab/SlicerSandbox/tree/master/VolumeRenderingSpecialEffects</a></p>

---

## Post #4 by @Zerfox (2020-08-17 21:15 UTC)

<p>Thanks to both for your fast response! I’ll have a good look and get back to you.</p>

---

## Post #5 by @Zerfox (2020-08-19 07:46 UTC)

<p>I have looked at both provided sources and googled around a bit, but I got stuck again as I am using C++ instead of Python.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> For PRISM I was able to find <a href="https://github.com/drouin-simon/PRISM" rel="nofollow noopener">the original C++ implementation</a>, which was targeted at VTK 6.3.0. Certain VTK-specific functions are not present in Slicer’s VTK and I am wondering whether it would have worked otherwise. Is there a C++ version of PRISM for Slicer? I was not able to find one. Or should I try to migrate the original PRISM implementation?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Similarly, I tried to convert the provided Python example into C++. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering" rel="nofollow noopener">On the wiki</a> I found a piece of code under “How to programmatically volume render your volume node” which was the following:</p>
<pre><code>qSlicerAbstractCoreModule* volumeRenderingModule =
  qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module("VolumeRendering");
vtkSlicerVolumeRenderingLogic* volumeRenderingLogic = 
  volumeRenderingModule ? vtkSlicerVolumeRenderingLogic::SafeDownCast(volumeRenderingModule-&gt;logic()) : 0;
vtkMRMLVolumeNode* volumeNode = mrmlScene-&gt;GetNodeByID('vtkMRMLScalarVolumeNode1');
if (volumeRenderingLogic)
  {
  vtkSmartPointer&lt;vtkMRMLVolumeRenderingDisplayNode&gt; displayNode =
    vtkSmartPointer&lt;vtkMRMLVolumeRenderingDisplayNode&gt;::Take(volumeRenderingLogic-&gt;CreateVolumeRenderingDisplayNode());
  mrmlScene-&gt;AddNode(displayNode);
  volumeNode-&gt;AddAndObserveDisplayNodeID(displayNode-&gt;GetID());
  volumeRenderingLogic-&gt;UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode);
  }
</code></pre>
<p>Is this outdated code? Because it tries to pass a <code>vtkMRMLNode*</code> into a <code>vtkMRMLVolumeNode*</code> and a <code>vtkSmartPointer&lt;vtkMRMLVolumeRenderingDisplayNode&gt;</code> into <code>vtkMRMLNode*</code>, which is not working out of the box. Can I safely cast these? Or do you perhaps have a C++ resources available on custom shader replacements?</p>
<p>Thanks again.</p>

---

## Post #6 by @lassoan (2020-08-19 12:05 UTC)

<p>You can safely downcast a vtkMRMLNode to any derived class (search for downcast in Slicer source).</p>
<p>You can convert between Python and C++ code by following a few rules (maybe we have already povided such rules in some previous topic). Therefore, I would recommend to implement a working code snippet in Python first, even if final implentation will be C++, just because it is so much easier to change the code and rerun in Python. You can copy-paste code into the console, create/modify a Python scripted module, or use Jupyter notebook.</p>

---

## Post #7 by @Zerfox (2020-08-20 10:43 UTC)

<p>Thank you for your suggestion to first implement a working code snippet in Python first. I have tried to get the SlicerSandbox module to work properly, after fixing two minor bugs I am running into an error when updating the custom shader (line 288 in VolumeRenderingSpecialEffects.py):</p>
<pre><code>AttributeError: 'vtkSlicerVolumeRenderingModuleMRMLPython.vtkMRMLCP' object has no attribute 'GetOrCreateShaderPropertyNode'
</code></pre>
<p>This error occurs when trying to copy-paste the code into the console, but also when trying to run the module from the GUI. I tried this using the Slicer v4.10.2 binary. When using Slicer built from source (4.11.0-2020-07-09) I do not get this error message, and the volume is raycasted. However, changing the radius for a certain MarkupsFiducial for both sphere and wedge crop doesn’t do anything.</p>
<p>What am I doing wrong?</p>

---

## Post #8 by @lassoan (2020-08-20 20:44 UTC)

<aside class="quote no-group" data-username="Zerfox" data-post="7" data-topic="13055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/eb8c5e/48.png" class="avatar"> Zerfox:</div>
<blockquote>
<p>I tried this using the Slicer v4.10.2 binary</p>
</blockquote>
</aside>
<p>For any developments, use latest Slicer Preview Release.</p>
<aside class="quote no-group" data-username="Zerfox" data-post="7" data-topic="13055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/eb8c5e/48.png" class="avatar"> Zerfox:</div>
<blockquote>
<p>changing the radius for a certain MarkupsFiducial for both sphere and wedge crop doesn’t do anything</p>
</blockquote>
</aside>
<p>Markups control point size is not related to volume rendering. VolumeRenderingSpecialEffects module serves as an example of how to get additional rendering parameters using a custom module. By using PRISM volume rendering extension, you can create custom shading effects and get GUI widgets to control additional parameters without any Python coding.</p>

---

## Post #9 by @Zerfox (2020-08-21 20:15 UTC)

<p>Pardon me for my prior confusion. I finally realise what the purpose for both options are.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For any developments, use latest Slicer Preview Release.</p>
</blockquote>
</aside>
<p>Thanks for the remark! As I am normally working in C++ I was using the nightly version of Slicer. I assumed (apparently wrongly) that for Python-related development all binary versions would work.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="13055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Markups control point size is not related to volume rendering. VolumeRenderingSpecialEffects module serves as an example of how to get additional rendering parameters using a custom module. By using PRISM volume rendering extension, you can create custom shading effects and get GUI widgets to control additional parameters without any Python coding.</p>
</blockquote>
</aside>
<p>Gotcha. I have successfully played around with the code in VolumeRenderingSpecialEffects now too. Thank you for your time and keep up the good work <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @lassoan (2020-08-21 21:20 UTC)

<p>Keep us posted if you get something working. It would be nice to see what special visualizations you could achieve.</p>

---
