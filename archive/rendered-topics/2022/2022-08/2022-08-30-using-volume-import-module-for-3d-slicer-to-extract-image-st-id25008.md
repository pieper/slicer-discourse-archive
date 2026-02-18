# Using volume import module for 3D Slicer to extract image stacks from .vol files

**Topic ID**: 25008
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/using-volume-import-module-for-3d-slicer-to-extract-image-stacks-from-vol-files/25008

---

## Post #1 by @Lastom (2022-08-30 17:50 UTC)

<p>Hello everyone,</p>
<p>I’m pretty new to using the 3D slicer software and recently downloaded it to convert .vol files to image stacks using this plugin by <a class="mention" href="/u/muratmaga">@muratmaga</a>:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chz31/VolImportModule">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chz31/VolImportModule" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/477341805ac1868788857900d9648c9fb1c3a4296a1fbd91599f406964fa5cc7/chz31/VolImportModule" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/chz31/VolImportModule" target="_blank" rel="noopener nofollow ugc">GitHub - chz31/VolImportModule</a></h3>

  <p>Contribute to chz31/VolImportModule development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I managed to already visualize my data in the program after generating an NHDR file. However, I still don’t quite know how to extract image stacks using this plugin. I tried to then save the scene in the .TIFF format, but when I do so, I only get one single image file that I can’t open containing all the data.</p>
<p>Unfortunately, I don’t have any programming experience with Python and many previous posts I saw related to my issue discussed some Python scripts to solve this. So if anyone knows a different and more simple solution to this issue, I’d appreciate your input!</p>

---

## Post #2 by @lassoan (2022-08-30 18:11 UTC)

<p>NRRD (or NHDR) file format can store an image stack in a convenient single-file format, preserving essential 3D geometry information. Therefore, in general you don’t want to downgrade to storing the image in a stack of TIFF files.</p>
<p>Can you describe your overall goal? What software are you planning to use for analyzing a TIFF stack?</p>

---

## Post #3 by @Lastom (2022-08-31 14:20 UTC)

<p>I’m planning to segment the data using the Dragonfly software and previously, with other data sets, I’ve always used TIFF image stacks for that. I have not seen the option to load NHDR files into Dragonfly.</p>

---

## Post #4 by @lassoan (2022-08-31 19:27 UTC)

<p>You can load NIFTI images (saved in Slicer as .hdr file) into Dragonfly. I would suggest to submit a feature request for Dragonfly for NRRD loading, as it is very easy to implement and a basic requirement for an image computing research software.</p>
<p>In general Slicer is much more capable software than Dragonfly: it has much more features and it is free and customizable and extensible. Is there any specific feature of Drafonfly that you don’t find in Slicer?</p>

---

## Post #5 by @Lastom (2022-09-01 13:35 UTC)

<p>Thank you, I’ll try that out.</p>
<p>Regarding the softwares, I’ve just always worked with Dragonfly in the past and the video editing in Dragonfly is very smooth. In Slicer, I have yet to get acquainted with all the different features and the segmentation options.</p>

---
