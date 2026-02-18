# Simulated Lightning

**Topic ID**: 22936
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/simulated-lightning/22936

---

## Post #1 by @ZUSV5EHlK7 (2022-04-13 12:23 UTC)

<p>Hello,<br>
actually I am working on my master thesis about “Direct Volume Rendering in Medicine”. For this I am comparing different OpenSource Software products. Now I am researching about simulated lightning/ many light source methods in DVR. Perhaps the 3D-Slicer inlcudes such tools for a more detailed representation of volume data.</p>
<p>Unfortunately I can not find some information about this.</p>
<p>Maybe You have some interest information.</p>
<p>Thank You.</p>

---

## Post #2 by @lassoan (2022-04-13 13:27 UTC)

<p>Slicer uses VTK for rendering. VTK has tons of lighting and volume rendering options in several rendering backends. In Slicer you can use most of these features. Most commonly needed features are exposed on the graphical user interface in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html"><code>Volume Rendering</code> module</a> in Slicer core and in <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/README.md#lights"><code>Lights</code> module</a> in <code>Sandbox</code> extension; and you can access all other options via Python scripting using <a href="https://vtk.org/doc/nightly/html/index.html">VTK API</a>.</p>
<p>Let us know if you are not sure if a specific lighting method is available in Slicer or not.</p>

---

## Post #3 by @pieper (2022-04-13 13:29 UTC)

<p><a class="mention" href="/u/zusv5ehlk7">@ZUSV5EHlK7</a> have a look at this thread to get ideas for work that is still needed:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/adding-secondary-rays-and-complex-illumination-methods-to-volumetric-rendering/8214">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/adding-secondary-rays-and-complex-illumination-methods-to-volumetric-rendering/8214" target="_blank" rel="noopener" title="07:21AM - 05 April 2022">VTK – 5 Apr 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/431;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/0/04aeefa53b921147a1b6a17ba81679534f28b2b7_2_1024x640.jpeg" class="thumbnail" width="690" height="431"></div>

<h3><a href="https://discourse.vtk.org/t/adding-secondary-rays-and-complex-illumination-methods-to-volumetric-rendering/8214" target="_blank" rel="noopener">Adding secondary rays and complex illumination methods to volumetric rendering</a></h3>

  <p>Hi all,  With Timothée Chabat and Francois Mazen, we’re currently working on developing new shaders for the vtkGPUVolumeRayCastMapper class in order to have a more realistic volumetric rendering. We are trying to integrate multiple-scattering effects...</p>

  <p>
    <span class="label1">Reading time: 4 mins 🕑</span>
      <span class="label2">Likes: 7 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @ZUSV5EHlK7 (2022-04-14 07:09 UTC)

<p>Great, this is going in the right direction.</p>
<p>DVR is a very complex issue. Until now I only used the Slicer. Now I have to question how it works.</p>
<p>Thank you very much.</p>
<p>If you have more information, send it to me. It is a great help.</p>

---

## Post #5 by @Chris_Rorden (2022-04-14 15:23 UTC)

<p><a class="mention" href="/u/zusv5ehlk7">@ZUSV5EHlK7</a> you may also want to look at <a href="https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage" rel="noopener nofollow ugc">MRIcroGL</a>. which blends Matcaps based on the <a href="https://github.com/neurolabusc/blog/blob/main/GL-gradients/README.md" rel="noopener nofollow ugc">gradients</a>. I also strongly recommend the book <a href="http://www.real-time-volume-graphics.org" rel="noopener nofollow ugc">real time volume graphics</a>.</p>

---
