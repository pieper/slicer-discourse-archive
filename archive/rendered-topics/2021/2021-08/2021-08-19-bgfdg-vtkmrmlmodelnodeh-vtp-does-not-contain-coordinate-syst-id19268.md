---
topic_id: 19268
title: "Bgfdg Vtkmrmlmodelnodeh Vtp Does Not Contain Coordinate Syst"
date: 2021-08-19
url: https://discourse.slicer.org/t/19268
---

# BGFDG_vtkMRMLModelNodeH.vtp does not contain coordinate system information. Assuming LPS

**Topic ID**: 19268
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/bgfdg-vtkmrmlmodelnodeh-vtp-does-not-contain-coordinate-system-information-assuming-lps/19268

---

## Post #1 by @Mahesh_Timmanagoudar (2021-08-19 07:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3337bd5b8a6101772a1475fe25db658d2d29b8ef.png" data-download-href="/uploads/short-url/7j5LUgBAb61dXwMKRTYjpyWjxIX.png?dl=1" title="vtp no points" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3337bd5b8a6101772a1475fe25db658d2d29b8ef.png" alt="vtp no points" data-base62-sha1="7j5LUgBAb61dXwMKRTYjpyWjxIX" width="690" height="308" data-dominant-color="F9F9F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vtp no points</span><span class="informations">1859×832 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Centerline.tre file created correctly. But there is no points in BranchCenterline_0.fcsv file. We got  message in log that is “BGFDG_vtkMRMLModelNodeH.vtp does not contain coordinate system information” .</p>
<p>I have attached centerline.tre and branchcenterline.fcsv file for more information.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f9f8d56e32e45f59af08a6f9af17968d8966548.png" data-download-href="/uploads/short-url/mM5KUqlH8ZhmCgal9nVheBvqTc4.png?dl=1" title="BranchCenterline" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f9f8d56e32e45f59af08a6f9af17968d8966548.png" alt="BranchCenterline" data-base62-sha1="mM5KUqlH8ZhmCgal9nVheBvqTc4" width="690" height="227" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BranchCenterline</span><span class="informations">945×312 7.12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ad2694411822f6926d45db50faf87328855038.png" data-download-href="/uploads/short-url/evtchNudQ91HqqbjJMOmctF2vws.png?dl=1" title="CenterlinePonts" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ad2694411822f6926d45db50faf87328855038.png" alt="CenterlinePonts" data-base62-sha1="evtchNudQ91HqqbjJMOmctF2vws" width="649" height="500" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CenterlinePonts</span><span class="informations">945×727 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-08-19 12:11 UTC)

<p>The coordinate system message is probably not important.  If you aren’t getting any results from the module probably your model is not a compatible with the filter so your core issue is something in TubeTK.  Try TubeTK outside of Slicer to debug.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITKTubeTK">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/InsightSoftwareConsortium/ITKTubeTK" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0e63bb950a63c6b628faa64e9b1a7374e16ab86fc792883bc938b952f7b98377/InsightSoftwareConsortium/ITKTubeTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/InsightSoftwareConsortium/ITKTubeTK" target="_blank" rel="noopener">GitHub - InsightSoftwareConsortium/ITKTubeTK</a></h3>

  <p>Contribute to InsightSoftwareConsortium/ITKTubeTK development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-08-20 18:43 UTC)

<p>It would be nice to make TubeTK work nicely with Slicer again, though. I don’t think it had been recently tested with Slicer, so there could be some API changes that require small adjustments.<br>
Do you run TubeTK CLI modules inn Slicer?<br>
What are you trying to achieve?</p>
<p>Note that you can also use <a href="https://github.com/vmtk/SlicerExtension-VMTK">VMTK extension</a> for extracting, visualizing, processing, quantifying centerlines in Slicer.</p>

---

## Post #4 by @Mahesh_Timmanagoudar (2021-08-23 08:17 UTC)

<p>I am extracting branch centerline points using TubeTK models in Slicer.</p>
<p>May I know which APIs required small adjustments for proper working?</p>
<p>I have already integrated <a href="https://github.com/LucasGandel/TubeTK" rel="noopener nofollow ugc">TubeTK</a> with Slicer.</p>
<p>Is there any way to make TubeTK work with new slicer version?</p>

---

## Post #5 by @Mahesh_Timmanagoudar (2021-08-23 09:30 UTC)

<p>I have changed TubeTK by using the link of <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/55e276d8381947d2a38409abb57f93ab3f346445/Documentation/ITK5MigrationGuide.md#spatial-objects-refactoring" rel="noopener nofollow ugc">Spatial Objects Refactoring section of the ITK 5 Migration Guide</a>. But still no luck. Its not working.</p>

---
