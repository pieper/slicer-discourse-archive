---
topic_id: 31921
title: "Convert Ct Nifti File To Dicom Using Slicer Modules Createdi"
date: 2023-09-26
url: https://discourse.slicer.org/t/31921
---

# Convert CT nifti file to DICOM using slicer.modules/createdicomseries

**Topic ID**: 31921
**Date**: 2023-09-26
**URL**: https://discourse.slicer.org/t/convert-ct-nifti-file-to-dicom-using-slicer-modules-createdicomseries/31921

---

## Post #1 by @DeepaKrishnaswamy (2023-09-26 23:45 UTC)

<p>Hi,</p>
<p>I am interested in converting the TotalSegmentator training dataset from NifTi to DICOM.</p>
<p>I’ve converted each CT NifTi file to a DICOM series using <code>slicer.modules.createdicomseries</code>, where I specified parameters including the inputVolume, dicomDirectory, patientID, studyID, seriesNumber, seriesDescription, and modality.</p>
<p>The converted DICOM files load successfully in Slicer. However, I then used <code>dciodvfy</code> from <code>dicom3tools</code> to verify that these converted DICOM files are valid. It displayed the following warnings/errors:</p>
<pre><code class="lang-auto">Warning - Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [1] = &lt;Anonymous&gt; - Retired Person Name form
CTImage
Error - Missing attribute Type 2C Conditional Element=&lt;Laterality&gt; Module=&lt;GeneralSeries&gt;
Error - Missing attribute Type 2 Required Element=&lt;KVP&gt; Module=&lt;CTImage&gt;
Error - Missing attribute Type 2 Required Element=&lt;AcquisitionNumber&gt; Module=&lt;CTImage&gt;
</code></pre>
<p>Using the <code>slicer.modules.createdicomseries</code>, how do I specify these particular fields to create a valid DICOM file?</p>
<p>Thank you!</p>
<p>Deepa</p>

---

## Post #2 by @pieper (2023-09-27 00:44 UTC)

<p>Hi <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> - this module was developed by some of our good friends at GE many years ago and I recall they only did the bare minimum to get their company’s workstation to recognize and show data generated from ITK/Slicer, so It’s not a surprise that the data isn’t perfect.  The <a href="https://github.com/Slicer/Slicer/tree/main/Modules/CLI/CreateDICOMSeries">code is here</a> if you want to have a look.  It’s pretty hard coded but wouldn’t be hard to extend to fix these issues.  It would just be exposing these tags as command line options following the existing pattern.  It would be great if you or someone could try this.</p>
<p>Of course another, probably a bit easier but hacky, solution would be to write a pydicom script to patch the generated files to add these fields.  Basically like the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html">DICOMPatcher</a>.</p>
<p>I’ll bet you don’t know KVP for this data so there’s no way to make them perfect, but I guess you can make them as close as possible.</p>

---

## Post #3 by @fedorov (2023-09-28 00:37 UTC)

<p>For the sake of completeness, this is the same CT series that is in question for the OHIF issue here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/OHIF/Viewers/issues/3682">
  <header class="source">

      <a href="https://github.com/OHIF/Viewers/issues/3682" target="_blank" rel="noopener">github.com/OHIF/Viewers</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/OHIF/Viewers/issues/3682" target="_blank" rel="noopener">[Bug] Viewing CT and SEG DICOM files in OHIF converted from nifti </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-27" data-time="22:55:24" data-timezone="UTC">10:55PM - 27 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/deepakri201" target="_blank" rel="noopener">
          <img alt="deepakri201" src="https://avatars.githubusercontent.com/u/59979551?v=4" class="onebox-avatar-inline" width="20" height="20">
          deepakri201
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Awaiting Reproduction
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hi, 

I have deployed my own viewer app using the https://github.com/ImagingDa<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">taCommons/Viewers master branch here. It has been working with no issues -- however now I have been working with a different set of files, and have encountered an issue. 

I have a nifti CT file that I converted to a DICOM series using the `slicer.modules.createdicomseries` module. I then converted the associated label nifti file to a DICOM SEG file using `dcmqi`. When I load these converted DICOM files into Slicer, they load with no visible issues: 

![image](https://github.com/OHIF/Viewers/assets/59979551/d098a635-d21e-4c9a-aa31-7ad513b821a8)

However, when I view the same DICOM files in OHIF, the following occurs: 

https://github.com/OHIF/Viewers/assets/59979551/030a3aa7-4b3c-4663-8edf-aa9f381314ce

Here are the DICOM CT and SEG files in [dropbox](https://www.dropbox.com/scl/fi/0abgbrcbnijjr33hhud3l/OHIF_converted_ct_and_seg_issue_09_27_23.zip?rlkey=266d3fqxra1npvq6dpmcfz5am&amp;dl=0). 

Thank you, 

Deepa

### Steps to Reproduce

1. Deployed my own viewer app using the https://github.com/ImagingDataCommons/Viewers master branch
2. Converted the CT nifti file to DICOM series using `slicer.modules.createdicomseries`
3. Converted the label nifti file to DICOM using `dcmqi`
4. Added DICOM files to a dataset and DICOM datastore and accessed in the deployed viewer

### The current behavior

Currently, both the CT and SEG do not load properly: 

https://github.com/OHIF/Viewers/assets/59979551/030a3aa7-4b3c-4663-8edf-aa9f381314ce

### The expected behavior

It should look something like this: 

![image](https://github.com/OHIF/Viewers/assets/59979551/d098a635-d21e-4c9a-aa31-7ad513b821a8)

### OS

Windows 10 

### Node version

I'm not sure 

### Browser

Chrome 116.0.5845.188</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2023-09-28 02:37 UTC)

<p>None of the validation errors explain the completely garbled output in OHIF viewer. Is there any other DICOM viewer that has trouble loading and displaying this CT properly?</p>

---

## Post #5 by @DeepaKrishnaswamy (2023-09-29 20:21 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I tried viewing these DICOM files in ITK-Snap, ImageJ, and the Mango viewer. I didn’t encounter any issues with these packages.</p>

---

## Post #6 by @lassoan (2023-09-30 04:19 UTC)

<p>If none of those software had any issues with the image then most likely the problem is in OHIF. Report the error to them and attach the image that OHIF does not load correctly.</p>

---

## Post #7 by @fedorov (2023-10-01 03:01 UTC)

<p>We reviewed this example with <a class="mention" href="/u/david_clunie">@David_Clunie</a>, and he noticed that the slices have rather unusual for a typical DICOM resolution (since the original DICOM data was resampled and cropped prior to creating the source NIfTIs), resulting in an odd number of pixels in a frame, which may trigger a bug in OHIF v2. We will investigate this further with the OHIF team, and will try to make sure this is fixed for OHIF v3.</p>

---

## Post #8 by @joshy (2024-05-08 15:47 UTC)

<p>Hi <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a>,<br>
can you share how you converted the NifTi to DICOM?<br>
Thx and with best regards,<br>
Joshy</p>

---
