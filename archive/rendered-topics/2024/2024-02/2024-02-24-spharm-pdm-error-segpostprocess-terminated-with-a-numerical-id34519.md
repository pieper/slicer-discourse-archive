# SPHARM-PDM Error: 'SegPostProcess terminated with a numerical fault'

**Topic ID**: 34519
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/spharm-pdm-error-segpostprocess-terminated-with-a-numerical-fault/34519

---

## Post #1 by @etour (2024-02-24 15:14 UTC)

<p>Hello! I’ve been attempting to use SlicerSALT SPHARM-PDM to compare the shape of some archaeological artefacts that I’m analysing (clay documents, to be more specific). My original 3D mesh files are .ply, and I’ve been able to convert them to both .vtk and .nrrd formats using the capabilities within Slicer, but no matter which I use as the input file type for the ‘Shape Analysis Module’, I am consistently getting the error ‘SegPostProcess terminated with a numerical fault’. I have generally just been using the default settings in SlicerSALT. I am very new to these types of files, so I am probably doing something very basic wrong, but would appreciate some guidance! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> (Note that I downloaded the SlicerSALT sample data, and was able to get those files to process correctly, so it’s definitely something wrong with my files.)</p>

---

## Post #2 by @etour (2024-02-25 08:28 UTC)

<p>An update: I managed to get past this initial error (it was an issue of scaling with the .ply files) and now my process is failing at this point:</p>
<p><em>ParaToSPHARMMesh standard error:</em></p>
<p><em>Error: open of file “[FilePath]-[OriginalFileName]-label_pp_surf_paraPhi.txt” failed.</em></p>
<p>As before, any guidance about what might be causing this error would be much appreciated! When looking in the log file, there are quite a few other errors are reported, so not sure if there’s multiple problems…</p>

---

## Post #3 by @bpaniagua (2024-02-26 13:50 UTC)

<p>Dear Emily</p>
<p>Do you have an output from GenParaMesh? it should be something like *_para.vtk or *_surf.vtk</p>
<p>Thanks!<br>
Bea</p>

---

## Post #4 by @etour (2024-02-26 23:11 UTC)

<p>Hi Beatriz,</p>
<p>I have the below outputs in the GenParaMesh folder:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7f6a6b8754e0483679d54107e34b8049c9dec1.png" data-download-href="/uploads/short-url/i339bx6DhxsYaYWMXs25liFA3UR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7f6a6b8754e0483679d54107e34b8049c9dec1.png" alt="image" data-base62-sha1="i339bx6DhxsYaYWMXs25liFA3UR" width="690" height="93" data-dominant-color="F2F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1450×197 13.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @styner (2024-02-28 21:43 UTC)

<p>Hi Emily<br>
The vtk files are all very small, likely near empty with exception of the header.<br>
The issue is likely with the first step of the SPHARM-PDM workflow, i.e. in the SegPostProcess step. If you load the post-processed label/segmentation file into Slicer, is it all empty? or does it contain the structure that you expected?</p>
<p>In the parameters for the SPHARM-PDM module, under Post Processed Segmentation, you can/have to set the label number of the structure in the segmentation input. Is it possible that this label number is not correctly set (I think the default is 1) then the post processing will yield an empty image and thus processing will fail.</p>
<p>Martin</p>

---

## Post #6 by @bpaniagua (2024-02-29 12:52 UTC)

<blockquote>
<p>under Post Processed Segmentation, you can/have to set the label number of the structure in the segmentation input. Is it possible that this label number is not correctly set (I think the default is 1) then the post processing will yield an empty image and thus processing will fail.</p>
</blockquote>
<p>Very good point. You should be able if your SegPostProcessed segmentation is empty by looking at the content of your *pp.nrrd file.</p>

---

## Post #7 by @etour (2024-03-03 00:31 UTC)

<p>Hi Beatriz and Martin,</p>
<p>Thank you so much for your responses! You are correct, there was an issue with the SegPostProcess step. Rather than being to do with the label number, it seems that there was an problem writing to the particular Output folder I’d selected in my OneDrive, so the _pp.nrrd files weren’t being generated at all (I could only see some temp folders). I instead chose a different output folder in my local ‘Documents’, and everything ran smoothly <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best,</p>
<p>Emily</p>

---
