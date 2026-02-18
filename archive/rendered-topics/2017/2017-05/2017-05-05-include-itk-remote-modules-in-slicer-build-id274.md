# Include itk remote modules in Slicer build

**Topic ID**: 274
**Date**: 2017-05-05
**URL**: https://discourse.slicer.org/t/include-itk-remote-modules-in-slicer-build/274

---

## Post #1 by @emckenzi123 (2017-05-05 19:02 UTC)

<p>Hello,<br>
I successfully built Slicer from source (4.7) for the first time and I would like to include some remote itk modules.  I see them in the …\ITKv4\Modules\Remote directory, but how do I incorporate them into my build?  Is there a CMake option I can use?  I have tried “SLICER_BUILD_” and “MODULE_” as Bool ON options and that doesn’t work (in fact they break my Slicer build).  I’d appreciate anyone who could point me in the right direction for this question.</p>
<p>Thank you</p>

---

## Post #2 by @jcfr (2017-05-06 03:21 UTC)

<p>Hi <a class="mention" href="/u/emckenzi123">@emckenzi123</a>,</p>
<p>There are currently no way to enable ITK options without having to explicitly editing <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_ITKv4.cmake">SuperBuild/External_ITKv4.cmake</a>.</p>
<p>An alternative approach could be to create a Slicer extension bundling the remote mode.</p>
<p>For example, see</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/KitwareMedical/SlicerITKUltrasound" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2717525?s=400&amp;v=4" class="thumbnail onebox-avatar" width="59" height="59">

<h3><a href="https://github.com/KitwareMedical/SlicerITKUltrasound" target="_blank">KitwareMedical/SlicerITKUltrasound</a></h3>

<p>Ultrasound image formation, processing, and analysis. Interfaces built off the ITKUltrasound library. - KitwareMedical/SlicerITKUltrasound</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
