# Does Slicer support the batch processing?

**Topic ID**: 2529
**Date**: 2018-04-06
**URL**: https://discourse.slicer.org/t/does-slicer-support-the-batch-processing/2529

---

## Post #1 by @glhfgg1024 (2018-04-06 17:40 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.0<br>
Expected behavior: batch processing<br>
Actual behavior: Not sure</p>
<p>Hi there,</p>
<p>I’m on these things: first import the DICOM files into Slicer, then for each patient, I need to save the PET/CT and the RT Structure Set to Nifti format for subsequent processing. Current I need to handle this data case by case. I was wondering if the Slicer can support the batch processing. After we defined a pipeline based on Slicer and the extensions, the batch processing module could repeat the processing automatically and also could record the cases with failure.</p>
<p>Thanks.</p>

---

## Post #2 by @cpinter (2018-04-06 18:08 UTC)

<p>Hello,</p>
<p>This question has been asked many times in the mailing list, for example</p><aside class="quote" data-post="1" data-topic="2437">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a183cd/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rtstruct-to-label-map/2437">RTstruct to Label map</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I have 200 dicom datapoints that contain a image and a RTstruct for the segmentations. I need to convert all RTstructs to Label volumes (maps) and can do this with the segmentations module. However, I have to perform every step manually and I am thus looking for a way to do it batch-wise. Since the segmentations module does not have a CLI, I was wondering if there is another solution that would allow me to access the module without the GUI. 
Best regards, 
Alain
  </blockquote>
</aside>
<p>
and</p><aside class="quote quote-modified" data-post="1" data-topic="1863">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/naglisr/48/16280_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-batch-processing-question-no-main-window-python-script/1863">Slicer batch processing question (--no-main-window --python-script)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
I am trying to find the best way to quickly batch process a number of folders containing head MRI dicom files to .nii files. Basically the pipeline should work like this: import the dicom files &gt; load them as a volume &gt; save the volume as a .nii file. 
I am trying to do this using the slicer from terminal: Slicer --no-main-window --python-script (as is described in here <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_access_a_scripted_module_from_python_scripts" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_access_a_scripted_module_fro…</a>
  </blockquote>
</aside>

<p>I hope this helps.</p>

---

## Post #3 by @pieper (2018-04-06 18:15 UTC)

<p>Also you can have a look at the CaseIterator extension.  It is currently geared for interactive work, but it would be great to see it extended to also work with batch pipelines.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/JoostJM/SlicerCaseIterator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/JoostJM/SlicerCaseIterator" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/7fecde44edbc67223150e8dd942ca5ab390e5c002e8365915c21bfb0f3c354a6/JoostJM/SlicerCaseIterator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/JoostJM/SlicerCaseIterator" target="_blank" rel="noopener">GitHub - JoostJM/SlicerCaseIterator: Simple Scripted Module to batch process...</a></h3>

  <p>Simple Scripted Module to batch process patients in 3D Slicer - GitHub - JoostJM/SlicerCaseIterator: Simple Scripted Module to batch process patients in 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator</a></p>

---

## Post #4 by @glhfgg1024 (2018-04-06 18:36 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/pieper">@pieper</a>, thank you very much for your kind reply and suggestions! Very helpful!</p>

---

## Post #5 by @timeanddoctor (2019-12-24 11:50 UTC)

<p>I installed SlicerCaseIterator and was confused by this wiki. The .csv table should be created including the dir of all volume and segment before load them?  Can I save/write a loaded volume  and mask segmentation in slicer by this module? I tried to do that  but nothing happen even clicking the batch buttom for an empty table.</p>

---
