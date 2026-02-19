---
topic_id: 15378
title: "Error In Exporting Tiff Images To Dicom"
date: 2021-01-06
url: https://discourse.slicer.org/t/15378
---

# Error in exporting .tiff images to DICOM

**Topic ID**: 15378
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/error-in-exporting-tiff-images-to-dicom/15378

---

## Post #1 by @marianaslicer (2021-01-06 18:14 UTC)

<p>Hello,</p>
<p>I have .tiff files of a lung phantom that I want to export to DICOM files using 3D Slicer (4.11.20200930 or 4.13.0). I was able to import the .tiff files into 3D Slicer and export them to DICOM. But when I tried to import the files from the DICOM database into the scene, the scene turns out all black. I do not understand why.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2021-01-06 18:59 UTC)

<p>Are there any warnings or errors in the application log?<br>
Can you upload the exported data set somewhere and post the link here so that we can have a look?</p>

---

## Post #3 by @marianaslicer (2021-01-06 21:14 UTC)

<p>Hi Andras,</p>
<p>Thank you for your prompt reply.<br>
No, there is a message saying ‘create a DICOM Series completed without errors’.</p>
<p>Here is the link for the .tiff files:</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f32GzyiLeMN2Iuly7HvIqWgplWkqdlMN?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f32GzyiLeMN2Iuly7HvIqWgplWkqdlMN?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f32GzyiLeMN2Iuly7HvIqWgplWkqdlMN?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f32GzyiLeMN2Iuly7HvIqWgplWkqdlMN?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>And for the exported DICOM data:</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1ujcs2GhS1ii0mDWMny9xva6EniuU3XQg?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1ujcs2GhS1ii0mDWMny9xva6EniuU3XQg?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1ujcs2GhS1ii0mDWMny9xva6EniuU3XQg?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1ujcs2GhS1ii0mDWMny9xva6EniuU3XQg?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I am sorry for not making the link public. They are part of a research project. So, I just shared the link with your email.</p>

---

## Post #4 by @lassoan (2021-01-07 00:29 UTC)

<p>The problem is that values in these TIFF files are stored very poorly:</p>
<ul>
<li>it has floating-point values, while voxels have 15-20 discrete values, which makes it hard to assign any meaning to voxel values</li>
<li>range of values is between -0.0048 and 0.0531 (until very recently DICOM only supported storage of integer values, and for compatibility reasons we still use only integers; since all input voxels are approximately 0, all voxels in the exported DICOM volume are set to 0, too)</li>
</ul>
<p>You can fix everything by using Simple Filters module -&gt; RescaleIntensityImageFilter or ShiftScaleImageFilter. CT volumes typically scaled between -1000 and 1000. If you set this output range then everything will work well</p>
<p>I would recommend to notify the group that created the volumes to switch to using standard 3D volume file formats, such as NRRD, instead of multi-frame 2D TIFF image.</p>

---
