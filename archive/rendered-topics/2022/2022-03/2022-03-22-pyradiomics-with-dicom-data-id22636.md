#  pyradiomics with DICOM data

**Topic ID**: 22636
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/pyradiomics-with-dicom-data/22636

---

## Post #1 by @Geor_F (2022-03-22 14:01 UTC)

<p>Hello,</p>
<p>I would like to use  pyradiomics with DICOM data, in the guideline it says “The script will accept as input a directory with a single DICOM image study for the input image, and the file name pointing to a DICOM Segmentation Image (DICOM SEG) object.”</p>
<p>but I am not sure what are the DICOM Segmentation Images and how to get these? I only have DICOM image files.</p>
<p>Thank you<br>
Gorge</p>

---

## Post #2 by @JonasB (2022-03-23 14:56 UTC)

<p>Hi,</p>
<p>I am not sure what you mean but maybe this helps: <a href="https://www.youtube.com/watch?v=nzWf4xHy1BM" class="inline-onebox" rel="noopener nofollow ugc">Create DICOM files from CT volume and segmentation - YouTube</a><br>
With 3D-slicer, you can generate DICOM segmentation files.</p>
<p>But I would rather work with nifiti where you only have one file per scan.<br>
It is pretty easy to convert DICOM to nifti: <a href="https://pypi.org/project/dicom2nifti/" class="inline-onebox" rel="noopener nofollow ugc">dicom2nifti · PyPI</a></p>
<p>Best,<br>
Jonas</p>

---

## Post #3 by @Geor_F (2022-03-23 16:19 UTC)

<p>Hi Jonas,</p>
<p>Thank you for your response. I am not a radiologist and not familiar with the images format, I am trying to figure out what kind of data I will be working with (to run pyradiomics) I know that we have DICOM files but not sure if they also have segmentation files as well,I know that veloity software is used. Does all DICOM files come with the segmentation files?<br>
Thanks.</p>

---

## Post #4 by @JonasB (2022-03-24 09:52 UTC)

<p>Hi Gorge,</p>
<p>You are welcome. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I am also not a radiologist. I know that DICOM is the raw data format containing metadata from the device (e.g. CT scanners). A CT scan contains several (mostly axial) slices which together make the 3D scan. To run Pyradiomics you need to have a region of interest where you extract the features. Segmentations are annotations and do not necessarily come with the image file itself. Normally, it is an extra file that separates the region of interest from the background (a mask for the original scan). If this file is not present you are probably missing the annotations and need to segment the region. Depending on what is your object of interest (e.g. cancer, metastasis, etc.) it can be very time-consuming to do this segmentation. Maybe ask some radiologists if they have segmentations for your purpose.</p>
<p>I hope that helps somehow.</p>
<p>Best,<br>
Jonas</p>

---

## Post #5 by @JoostJM (2022-03-25 07:02 UTC)

<p>Hello George,</p>
<p>In general, DICOMS acquired in a radiology workflow will not have been segmented, this is indeed a required and time consuming step. In case of images from radiotherapy, these will generally have segmentations in the form of RTSTRUCT, which need to be converted before they are usable for PyRadiomics. This can be done in 3D Slicer, or via commandline tool plastimatch.</p>
<p>Generally, most studies using PyRadiomics start out with DICOMS, but first convert them to another (easier-to-use) image format like NIFTII or NRRD, followed by segmentation and radiomics feature extraction. PyRadiomics does allow you to use DICOM files directly, but this uses the pyradiomics-dcm labs script and requires you to provide the segmentation in DICOM SEG format (which is a newer type of segmentation annotation that is easier to use than RTSTRUCT when extracting features). Furthermore, the output of that script is DICOM SR, making it a DICOM to DICOM workflow, which is generally not required for research in a big dataset and can make it more complicated than necessary.</p>
<p>Regards,</p>
<p>Joost</p>

---

## Post #6 by @Geor_F (2022-04-13 16:16 UTC)

<p>Great, thank you both for your explanations. So of I get you right I need DICOM file (or series of files?) +segmentation file to run pyradiomics. Without segmentation I will not be able to run radiomics feature extraction as the ROI is not defined.<br>
I can get this if there are DICOM SEG files already, or I can convert DICOM to NIFTII (or NRRD) and next on this file ask radiologist to do segmentation. Is this correct?<br>
Is there any example of data that I can send to show what I need for pyradiomics?I am interested in lung cancer nodules. Can you advise what exactly to ask to send me, possible formats etc how big are files, can they be easily transferred-send by email. Any suggestions will be highly appreciated!</p>

---

## Post #7 by @lassoan (2022-04-13 21:15 UTC)

<p>It is simpler than this. You can load your DICOM images into Slicer. If you have DICOM segmentations (because the radiologist already segmented the region of interests in his clinical software and stored in the DICOM archive in DICOM RT Structure Set or DICOM Segmentation Object format), then you can load them into Slicer, too. If you don’t have segmentation then you can load the DICOM image into Slicer and then segment it in the Segment Editor.</p>
<p>You can then compute radiomics features in Slicer or save the image and segmentation in nrrd format and compute radiomics features later.</p>

---

## Post #8 by @rbumm (2022-04-13 21:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Do I have to convert the segmentation with a couple of segments to a labelmap before I feed it into Radiomics? I tested some datasets today and always get identical feature columns in SlicerRadiomics.</p>

---

## Post #9 by @lassoan (2022-04-13 22:03 UTC)

<p>I’ve just tested and it works well (in a few-day-old Slicer Preview Release). I’ve just submitted a fix for an issue that might cause the problem you experienced:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/pull/69">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/69" target="_blank" rel="noopener">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/69" target="_blank" rel="noopener">BUG: Fix some segment missing in output</a>
    </h4>

    <div class="branches">
      <code>AIM-Harvard:master</code> ← <code>lassoan:fix-missing-segment</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-13" data-time="22:01:42" data-timezone="UTC">10:01PM - 13 Apr 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 7 additions and 6 deletions">
        <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/69/files" target="_blank" rel="noopener">
          <span class="added">+7</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When input regions were provided as a segmentation node, segments were missed wh<span class="show-more-container"><a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/69" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">en segment name was not the same as the segment ID (e.g., the user renamed the segment).

The problem was that ExportSegmentsToLabelmapNode requires segment ID, but it was provided segment name instead. Fixed the issue by providing segment ID.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can try to apply this change manually on your SlicerRadiomics.py file and see if it fixes the issue.</p>

---

## Post #10 by @Geor_F (2022-04-14 10:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="22636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOM images into Slicer. If you have DICOM segmentations (because the radiologist already segmented the region of interests in his clinical software and stored in the DICOM archive in DICOM RT Structure Set or DICOM Segmentation Object format), then you can load them into Slicer, too. If you don’t have segmentation then you can load the DICOM image into Slicer and then segment it in the Segment Editor.</p>
</blockquote>
</aside>
<p>Thanks so much Andras! Can I also ask if the segmentation file has a DICOM SEG ending? How to recognise the segmentation file (either DICOM RT or Segmentation Object). I am asking as a clinician is not sure if there are any segmentations files associated with CT, and he is not sure how to spot one. Thanks again!</p>

---

## Post #11 by @rbumm (2022-04-14 10:21 UTC)

<p>Thanks a lot. This now works.</p>

---

## Post #12 by @lassoan (2022-04-14 11:38 UTC)

<aside class="quote no-group" data-username="Geor_F" data-post="10" data-topic="22636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/geor_f/48/14756_2.png" class="avatar"> Geor_F:</div>
<blockquote>
<p>Can I also ask if the segmentation file has a DICOM SEG ending? How to recognise the segmentation file (either DICOM RT or Segmentation Object).</p>
</blockquote>
</aside>
<p>DICOM does not rely on specific filenames or extensions, so you can only tell what a set of DICOM files contain by parsing them with a compatible software application. Segmentation may show up in the series list as “Segmentation”, “SEG”, “Structure Set”, “RTSTRUCT”.</p>
<aside class="quote no-group" data-username="Geor_F" data-post="10" data-topic="22636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/geor_f/48/14756_2.png" class="avatar"> Geor_F:</div>
<blockquote>
<p>I am asking as a clinician is not sure if there are any segmentations files associated with CT, and he is not sure how to spot one.</p>
</blockquote>
</aside>
<p>Segmenting an image in clinical software usually requires significant effort. Therefore, if the clinician is not sure if he segmented the image or not then most likely the image was not segmented.</p>

---

## Post #13 by @Ella1 (2022-06-10 19:10 UTC)

<p>Hi Andras<br>
My research project is about Brain Mets. My question is can I use this method for MRI scans as well?<br>
Because I am not sure if those MRI scans have segmentations.</p>

---

## Post #14 by @lassoan (2022-06-12 02:08 UTC)

<p>Yes, the same method works. You need segmentation to designate a region of interest. You don’t want irrelevant regions of the image affect your results.</p>

---

## Post #15 by @Ella1 (2022-06-13 14:27 UTC)

<p>Thanks for your response!!!</p>

---
