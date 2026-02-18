# How can I convert NIFTI files to NRRD files in batch mode?

**Topic ID**: 11841
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/how-can-i-convert-nifti-files-to-nrrd-files-in-batch-mode/11841

---

## Post #1 by @AT3432984 (2020-06-03 02:30 UTC)

<p>Hello,</p>
<p>I have approximately 300 MRI images in the NIfTI format which I need to convert to NRRD files so that I can analyse them. I can open each file in 3D-Slicer and save as NRRD, but I am wondering if there is an easier way to do this as I have so many images.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-06-03 02:32 UTC)

<p>You can write a few-line Python script that iterates through all the nifti files in that folder, loads the volume, then saves it as nrrd.</p>
<p>You can find examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">script repository</a> for loading and saving volume. This post can also help (and there were other similar questions here before that you may be able to find):</p>
<aside class="quote quote-modified" data-post="1" data-topic="6169">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/85e7bf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-load-mrb-file-and-save-all-nodes-in-nii-format-using-script/6169">how to load mrb file and save all nodes in nii format using script</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: windows 10 
Slicer version:4.8.1 
Expected behavior: save nodes in nii format using script 
Actual behavior: only can save in nrrd format 
Hi, 
I want to export image and labelmap node in nii format to a directory using python script. 
My script is: 
mrbfile=r’D:\sample.mrb’ 
outdir = r’D:\output_dir’ 
loadScene(infilename) 
saveScene(outfilename[:-4]) 
slicer.mrmlScene.Clear(0); 
However, this could only save node in nrrd format, the 3D Slicer default format. How could I save …
  </blockquote>
</aside>


---
