---
topic_id: 17941
title: "Resample Dwi Volume"
date: 2021-06-03
url: https://discourse.slicer.org/t/17941
---

# Resample DWI Volume

**Topic ID**: 17941
**Date**: 2021-06-03
**URL**: https://discourse.slicer.org/t/resample-dwi-volume/17941

---

## Post #1 by @Nadya_Shusharina (2021-06-03 21:49 UTC)

<p>I am using Resample Scalar/Vector/DWI Volume module to simply upsample the image. The Apply button runs the process of resampling with the status “Completed” after about 25 sec. However, the output resampled volume is not being written/displayed.</p>
<p>I am using nrrd input and Manual Output Parameters.</p>
<p>What am I missing?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-06-04 01:57 UTC)

<p>What do you see in the application log?</p>
<p>Does it make a difference if you enable “Prefer executable CLI” in application settings / modules?</p>

---

## Post #3 by @Nadya_Shusharina (2021-06-07 13:43 UTC)

<p>“Prefer executable CLI” is ON.</p>
<p>The message is “Unsupported number of components (only 1 allowed): 168”</p>

---

## Post #4 by @pieper (2021-06-07 14:55 UTC)

<p>In Slicer is the input volume loaded as a diffusion volume?  (check in the Volumes module if you can scroll through the gradient images).  Otherwise maybe you can share a dataset with steps for reproducing.</p>

---

## Post #5 by @Nadya_Shusharina (2021-06-07 14:58 UTC)

<p>Yes, I can see all components. How do I share?</p>

---

## Post #6 by @pieper (2021-06-07 18:08 UTC)

<p>You can put it on google drive, dropbox, or similar and share the link here.</p>

---

## Post #7 by @Nadya_Shusharina (2021-06-08 02:46 UTC)

<p>Here is the link.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/sh/b7odxcgdv89fwsy/AAAS7eKnFI04nvzHykaameuea?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/b7odxcgdv89fwsy/AAAS7eKnFI04nvzHykaameuea?dl=0" target="_blank" rel="noopener nofollow ugc">DTI_legs</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @pieper (2021-06-09 02:42 UTC)

<p>Thanks for reporting this and providing the data to replicate it <a class="mention" href="/u/nadya_shusharina">@Nadya_Shusharina</a>.</p>
<p>It appears the problem is that the CLI read-back mechanism is not detecting the resampled data as DWI and so it fails to load.  As I recall this used to work but I haven’t seen it used in a while.</p>
<pre><code class="lang-auto">
Found CommandLine Module, target is  /Applications/Slicer-4.11.20210226.app/Contents/lib/Slicer-4.11/cli-modules/ResampleScalarVectorDWIVolume
ModuleType: CommandLineModule
Resample Scalar/Vector/DWI Volume command line: 

/Applications/Slicer-4.11.20210226.app/Contents/lib/Slicer-4.11/cli-modules/ResampleScalarVectorDWIVolume --transformationFile /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLLinearTransformNodeE.h5 --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0,0,0 --size 0,0,0 --direction_matrix 0,0,0,0,0,0,0,0,0 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd 

Resample Scalar/Vector/DWI Volume completed without errors

UpdateFromFile: Unsupported number of components (only 1 allowed): 168


ReadDataInternal: Cannot read file as a volume of type Volume[fullName = /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd]
	Number of files listed in the node = 0.
	File reader says it was able to read 1 files.
	File reader used the archetype file name of /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd [reader 0th file name = /private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd]
FileFormatError



vtkMRMLStorageNode::ReadData: Failed to read node Output Volume (vtkMRMLScalarVolumeNode1) from filename='/private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd'


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x7ff9223662f0) has 0 connections but is not optional.

</code></pre>
<p>This is a bug so I <a href="https://github.com/Slicer/Slicer/issues/5684">reported an issue</a> to track it.</p>
<p>As a workaround you can enable the “Preserve CLII module data files” flag in the Application Settings → Developer panel and then open the result of the CLI using the regular Add Data dialog.  The output is the last filename on the CLI command line (/private/var/folders/0y/yzydqvk90f9_kx1sqd3k110h0000gn/T/Slicer-pieper/GJHED_vtkMRMLScalarVolumeNodeB.nrrd<br>
in this case),</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4a902b62de6c4ad606e6bc4702048ab8db1e95.png" data-download-href="/uploads/short-url/fSwKvdKLIdNhZJlW0ChYRAEVjo1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4a902b62de6c4ad606e6bc4702048ab8db1e95_2_345x94.png" alt="image" data-base62-sha1="fSwKvdKLIdNhZJlW0ChYRAEVjo1" width="345" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4a902b62de6c4ad606e6bc4702048ab8db1e95_2_345x94.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4a902b62de6c4ad606e6bc4702048ab8db1e95_2_517x141.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4a902b62de6c4ad606e6bc4702048ab8db1e95_2_690x188.png 2x" data-dominant-color="383B3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">992×272 31.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Nadya_Shusharina (2021-06-09 13:44 UTC)

<p>Thank you, Steve. I recall some other cases in DMRI where the output volume does not load if I specify “Create new Volume as …”.</p>

---

## Post #10 by @pieper (2021-06-09 13:56 UTC)

<p>Ah, yes, thanks for the reminder.  I really haven’t used this in a long time.</p>
<p>You do need to select the correct node type for the output in order for it to load correctly.  This is different from the Add Data path which tries many different types to figure out what type of file is being read back.</p>
<p>So in this case if I create a DiffusionWeightedVolume the result loads back correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2206ac90f771a286c0e4757e89debcb0e94ec48.png" data-download-href="/uploads/short-url/ppMrtmhm7xqgOTyGBbHSLjYWuqQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2206ac90f771a286c0e4757e89debcb0e94ec48_2_689x171.png" alt="image" data-base62-sha1="ppMrtmhm7xqgOTyGBbHSLjYWuqQ" width="689" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2206ac90f771a286c0e4757e89debcb0e94ec48_2_689x171.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2206ac90f771a286c0e4757e89debcb0e94ec48_2_1033x256.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2206ac90f771a286c0e4757e89debcb0e94ec48.png 2x" data-dominant-color="424950"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1212×302 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is an odd usability issue, but maybe not technically a bug given the design of the CLI intertace.  Probably a small scripted module on top of the CLI could automated some of these data dependencies.</p>

---
