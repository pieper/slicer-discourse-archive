# Automatic c-MRI heart segmentation

**Topic ID**: 15047
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/automatic-c-mri-heart-segmentation/15047

---

## Post #1 by @Jonathan (2020-12-14 13:29 UTC)

<p>Hello,</p>
<p>I have cardiac short axis scans which I would like to segment at specific phases of the cardiac cycle : at peak-systole and at peak-diatole.</p>
<p>So far, I manually detected the relevant slices and then copied the IMA file to a new folder [one for the systole and one for the diastole] , and then used the DICOM patcher for volumetric segmentation.</p>
<p>*Is there an automatic feature to extract the slices?<br>
*How can I group all the relevant slices to one nrrd flie?<br>
*Sometimes I get the following error : Unexpected error after executing the patch command: ‘ForceSamePatientNameIdInEachDirectory’ object has no attribute ‘patientName’<br>
I tried to change the metadata accordingly - didn’t work.</p>
<p>Thank you for your help,</p>
<p>J</p>

---

## Post #2 by @lassoan (2020-12-14 14:46 UTC)

<p>Latest Slicer version should be able to automatically load 4D cardiac MRI sequence as a volume sequence. If it does not seem to work then you can share an anonymized data set (upload somewhere and post the link here) and we can investigate.</p>

---

## Post #3 by @Jonathan (2020-12-15 05:59 UTC)

<p>Thank you for the quick reply.<br>
I downloaded and installed the latest version. The 4D cardiac MRI sequence was indeed loaded automatically as a volume sequence, and I was able to segment the whole heart at once. However, I wasn’t able to nevigate through time periods. [I was able to segment only the specific loaded time frame].<br>
Up  till now I have uploaded the data without using the DICOM utility and used the scroll bar to choose the desired time period.<br>
I am newbie to this module and I would appriciate your assistance in the matter.</p>
<p>The entire data is available at the following link:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f-p8-IOdfVX7YE1pYLy_pNuILdHLGZ49?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f-p8-IOdfVX7YE1pYLy_pNuILdHLGZ49?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f-p8-IOdfVX7YE1pYLy_pNuILdHLGZ49?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1f-p8-IOdfVX7YE1pYLy_pNuILdHLGZ49?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>J</p>

---
