---
topic_id: 18951
title: "Additional Code With Functions"
date: 2021-07-27
url: https://discourse.slicer.org/t/18951
---

# Additional code with functions

**Topic ID**: 18951
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/additional-code-with-functions/18951

---

## Post #1 by @rohan_n (2021-07-27 18:59 UTC)

<p>Hello,</p>
<p>I want to submit my extension to the Extension Manager this week.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37a5f91478b9f78fb27e91358e92610842473f0f.png" data-download-href="/uploads/short-url/7WhR5H1LrQDW8y7C9kchU4jYeiH.png?dl=1" title="module1codescreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37a5f91478b9f78fb27e91358e92610842473f0f_2_689x321.png" alt="module1codescreenshot" data-base62-sha1="7WhR5H1LrQDW8y7C9kchU4jYeiH" width="689" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37a5f91478b9f78fb27e91358e92610842473f0f_2_689x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37a5f91478b9f78fb27e91358e92610842473f0f_2_1033x481.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37a5f91478b9f78fb27e91358e92610842473f0f_2_1378x642.png 2x" data-dominant-color="F8F9FA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">module1codescreenshot</span><span class="informations">2437×1137 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
As you can see in the attached image, each module folder has the main .py file that has same name as the module, but also several other .py files that the main module file imports so that it can call the functions in those other .py files.</p>
<p>Is this ok, or does each module folder have to have only the one .py file with same name as the module? If it’s ok to have multiple .py files in the module folder, how do I make sure that an error like this:</p>
<p><code>RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class chooseEarly_LateByManufacturer was not found in file C:/Users/rnadkarni/SlcExt/Breast_DCEMRI_FTV/DCE_IDandPhaseSelect/chooseEarly_LateByManufacturer.py</code></p>
<p>doesn’t prevent the user from being able to use my extension?<br>
On the main Windows computer I’m developing this extension on, I am able to ignore this error message and run the modules without issue. But I tried on my Mac laptop and this error appears to be the reason that module 1 of my extension is unavailable to use.</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #2 by @pieper (2021-07-27 19:05 UTC)

<p>You can place those other python files in a Lib folder that you import into your module.  Slicer looks at all .py files in the module path and tries to load them but won’t look inside subfolders.  There are lots of examples of this, but here’s a good one:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/SegmentStatistics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/SegmentStatistics" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/SegmentStatistics" target="_blank" rel="noopener">Slicer/Modules/Scripted/SegmentStatistics at master · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/SegmentStatistics" target="_blank" rel="noopener">master/Modules/Scripted/SegmentStatistics</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
