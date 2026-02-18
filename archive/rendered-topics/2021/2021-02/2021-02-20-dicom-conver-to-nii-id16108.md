# Dicom conver to Nii

**Topic ID**: 16108
**Date**: 2021-02-20
**URL**: https://discourse.slicer.org/t/dicom-conver-to-nii/16108

---

## Post #1 by @samsonaie (2021-02-20 08:36 UTC)

<p>Hi, There,</p>
<p>I have a challenge that when I use 3D slicer to convert a ultrason DICOM files to nii files. I lost the quality of image by a new ultrason probe ( comparing to a probe we used before).</p>
<p>In the past, we have been using a GE probe in GE Voluson E10 :</p>
<p>Model: "RIC5-9-D,<br>
Acquisition parameters: <strong>B177 degrees, V120 degrees, depth 7.7cm,</strong><br>
The obtained dicom document size is <strong>54Mb</strong>, ( see attached link to download )<br>
Then, the converted nii file size is <strong>63Mb</strong><br>
The image is clear and has sufficient resolution.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="15" height="15">
      <a href="https://www.dropbox.com/sh/525mdcpe35ei57e/AAAggMpGgJqjqlEJLUxXXPMJa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/525mdcpe35ei57e/AAAggMpGgJqjqlEJLUxXXPMJa?dl=0" target="_blank" rel="noopener nofollow ugc">DCM Nii files</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>However, we recently have a new GE probe,</p>
<p>Model: "RSP6-16-D,<br>
Acquisition parameters: <strong>B50 degrees, V29 degrees, depth 4.2cm</strong><br>
Dicom document size <strong>37Mb</strong><br>
The converted nii file size is  <strong><strong>2.6Mb  &lt;= this is the problem, it become very small !!</strong></strong><br>
The resolution of the picture is very low and very blurry.</p>
<p>you can find that the acquisition angle (B, V) of the original equipment (RIC5-9-D )  is relatively wide, and the acquisition angle of the new equipment (RSP6-16-D)  is much narrow.</p>
<p>The problem we encountered is: Why does the DICOM document of the new device become very small when it is converted. <strong>The resolution Is poor.</strong><br>
Is there any parameter or setting I need to modify for smaller angle dicom file which I acquired by the new probe? or anything thing I can do to keep the same quality?</p>
<p>Hope it can be resolved, thank you.</p>

---

## Post #2 by @samsonaie (2021-02-26 07:29 UTC)

<p>After some analysis，, I assume the challenge is NOT in the process of converting from DCM to Nii, it is, most likely,  the data acquisition process of DCM file in 3D slicer. The DCM can not be read in a proper way or in full resolution thus it lost the resolution of the image.<br>
If anyway have any tips to modify the parameter and share them with me, It will be highly appreciated!</p>
<p>Thank you for all the attention and consideration! <img src="https://emoji.discourse-cdn.com/twitter/love_you_gesture.png?v=9" title=":love_you_gesture:" class="emoji" alt=":love_you_gesture:"></p>

---
