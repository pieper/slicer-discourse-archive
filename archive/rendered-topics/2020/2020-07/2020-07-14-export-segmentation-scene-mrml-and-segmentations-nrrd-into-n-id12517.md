---
topic_id: 12517
title: "Export Segmentation Scene Mrml And Segmentations Nrrd Into N"
date: 2020-07-14
url: https://discourse.slicer.org/t/12517
---

# Export segmentation scene (mrml) and segmentations (nrrd) into Nifti format for dropbox viewing

**Topic ID**: 12517
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/export-segmentation-scene-mrml-and-segmentations-nrrd-into-nifti-format-for-dropbox-viewing/12517

---

## Post #1 by @Bo_Lan (2020-07-14 03:38 UTC)

<p>Hi! I am trying to export my segmentation scene and its segmentations as a nifti file for my PI to be shared and downloaded from dropbox. However, the entire scene can only be saved as a mrml file and the segmentations can only be saved in nrrd format with only the original unsegmented template able to be saved in Nifti format (See attached photo). My PI says that they can only access nifti files and since my entire scene and segmentations cannot be saved in the nifti format as nifti format is not an option in their menu (first two files), how can I save them both in nifti format so that my PI can view them properly? Thank You! <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec8bc7287dde4cfeb9f0c89bcdd194866f507a44.jpeg" data-download-href="/uploads/short-url/xKA9FnTZSskjfpOT2QboPsHKcaE.jpeg?dl=1" title="InkedFiles_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec8bc7287dde4cfeb9f0c89bcdd194866f507a44_2_690x225.jpeg" alt="InkedFiles_LI" data-base62-sha1="xKA9FnTZSskjfpOT2QboPsHKcaE" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec8bc7287dde4cfeb9f0c89bcdd194866f507a44_2_690x225.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec8bc7287dde4cfeb9f0c89bcdd194866f507a44.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec8bc7287dde4cfeb9f0c89bcdd194866f507a44.jpeg 2x" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">InkedFiles_LI</span><span class="informations">944×308 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-07-14 03:48 UTC)

<p>Are you working with brain images? If yes, then using nifti file format may make sense (otherwise I would recommend nrrd). To save segmentation result as nifti, right-click on the segmentation node in Data module to export to labelmap node.</p>

---

## Post #3 by @Bo_Lan (2020-07-14 20:06 UTC)

<p>Thank you! I am working with segmenting and entire brain so it does make sense for nifti. I have gone to the Segmentations module where export and export to labelmap is located and cannot seem to find the nodes that you are talking about. Right clicking on segmentations in save also does not do anything. Can you show me how to get there?</p>

---

## Post #4 by @lassoan (2020-07-14 20:20 UTC)

<p>To convert segmentation to labelmap: right-click on segmentation node in Data module and choose “Export visible segments to binary labelmap” (or use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">Segmentations module</a>).</p>

---

## Post #5 by @Bo_Lan (2020-07-15 21:55 UTC)

<p>Thank you for the advice! I was able to get my file into nifti format. However, as I am performing an entire brain segmentation (both hemispheres), it appears that the new nifti file (after exported to binary labelmap) when opened in a new slicer tab has its spatial position slightly altered and the right hemisphere is completely dark with only left hemisphere segmentations visible. How can I go about correcting this?</p>

---

## Post #6 by @Bo_Lan (2020-07-15 22:12 UTC)

<p>Here are my original (with Freesurfer label colors) and nifti. The nifti appears to be spatially disoriented (acccording to my PI) as well as missing the right hemisphere even though I created it by simply right clicking on segmentation node and choosing exporting to binary labelmap. Hope you can let me know what is wrong, thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0558eae4fe603332b715801602388ec4c8b6a850.png" data-download-href="/uploads/short-url/LiTk9jY6mobgtZpqZgoIdWira8.png?dl=1" title="Nifti" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0558eae4fe603332b715801602388ec4c8b6a850.png" alt="Nifti" data-base62-sha1="LiTk9jY6mobgtZpqZgoIdWira8" width="560" height="500" data-dominant-color="1C1B1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Nifti</span><span class="informations">927×827 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2020-07-16 02:25 UTC)

<p>When you load the nifti file, you need to indicate in “Add data” window that the nifti file contains a segmentation or labelmap volume, by selecting “Segmentation” in the description column; or selecting “Volume” in the description and check “Show options” and check “LabelMap”.</p>

---

## Post #8 by @Bo_Lan (2020-07-17 17:46 UTC)

<p>Thank you for the information! I have been able to get colors now by selecting “volume” in the description. However, my colors are in Freesurfer labels as needed for my project and when I upload the new nifti, I also do select Freesurfer labels in the description after checking “Show options” and my segmentations end up an entirely different color (bottom) as the original (top). I am wondering how I can fix this. Going to volumes and changing to freesurfer or just generic colors also does not seem to help. Thank you so far! <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78ff7b365823326ae9ec454b5f63cce044fd83db.png" data-download-href="/uploads/short-url/hgoF54BAFFZzGbYMzjCFqlNbciT.png?dl=1" title="Original" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78ff7b365823326ae9ec454b5f63cce044fd83db_2_528x500.png" alt="Original" data-base62-sha1="hgoF54BAFFZzGbYMzjCFqlNbciT" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78ff7b365823326ae9ec454b5f63cce044fd83db_2_528x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78ff7b365823326ae9ec454b5f63cce044fd83db_2_792x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78ff7b365823326ae9ec454b5f63cce044fd83db.png 2x" data-dominant-color="484345"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Original</span><span class="informations">914×864 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2020-07-17 18:04 UTC)

<p>To identify segments, FreeSurfer relies on hardcoded label values, while segmentation relies on names (or standard DICOM terminology).</p>
<p>Could you please describe your data processing workflow? Would you like to fix automatic FreeSurfer segmentation in Slicer’s Segment Editor?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Can you help here? Maybe we would need a FreeSurfer export, which would create labelmap with FreeSurfer label values, with a similar script to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header">this</a>.</p>

---

## Post #10 by @pieper (2020-07-17 18:36 UTC)

<p>Also there is this project that may help:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/corticometrics/fs2dicom" target="_blank" rel="noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/25853744?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/corticometrics/fs2dicom" target="_blank" rel="noopener">corticometrics/fs2dicom</a></h3>

<p>Convert FreeSurfer outputs to DICOM. Contribute to corticometrics/fs2dicom development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Sunderlandkyl (2020-07-17 19:07 UTC)

<p>We could add the functionality in SlicerFreeSurfer to export the Segmentations with the correct label values directly to nifti.<br>
Exporting the segmentations to labelmap <a href="https://github.com/Slicer/Slicer/issues/5044" rel="nofollow noopener">using the color node</a> would also solve this issue.</p>

---

## Post #12 by @lassoan (2020-07-17 19:20 UTC)

<p>Sounds good. For now maybe just add an issue to SlicerFreeSurfer so that we remember this.</p>

---

## Post #13 by @Bo_Lan (2020-07-18 02:48 UTC)

<p>Thank you for all the feedback. I will indeed try it. In response to Dr. Lasso <a class="mention" href="/u/lassoan">@lassoan</a> , my processing workflow has simply been to use the segmentations editor and manually color them in, using automated tools such as thresholding only occasionally, as my project requires manual segmentation. I also label my segmentations simply with freesurfer colors. How would I export using color node? The link does not seem to inform me how to do so but I would appreciate it!</p>

---

## Post #14 by @lassoan (2020-07-18 14:34 UTC)

<p>We haven’t implemented export with label values taken from color table. The idea is tracked in <a href="https://github.com/Slicer/Slicer/issues/5044">this issue</a>. We don’t plan to work on it before releasing Slicer5, but if many people request it and/or Slicer5 release is delayed then it might fit in.</p>
<p>Until then, you can use this code snippet to relabel a segmentation:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header</a></p>

---
