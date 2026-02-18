# HDR brachytherapy plan loading

**Topic ID**: 9383
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/hdr-brachytherapy-plan-loading/9383

---

## Post #1 by @agv (2019-12-04 12:37 UTC)

<p>Hello everyone,</p>
<p>I am not sure if this is the right topic, but it looks similar to the error I get.</p>
<p>I am trying to import an HDR brachytherapy treatment planning in DICOM format, previously exported from Oncentra Brachy. I have the SlicerRT extension already installed, but when trying to load the files from DICOM Browser I get the following error:</p>
<p>“Could not load RTDOSE as a RT”<br>
“Could not load RTPLAN as a RT”</p>
<p>And when going to Data module, only the volume and RTSTRUCT are available.</p>
<p>Are brachytherapy plannings supported in SlicerRT?</p>
<p>If they are, I can share the DICOM files if that could help.</p>
<p>Thank you very much in advance,</p>
<p>Alessandro</p>

---

## Post #2 by @cpinter (2019-12-04 13:50 UTC)

<p>We implemented brachy plan import in SlicerRT a few months ago. It means that it is not available in 4.10.1, but it is in recent preview versions. If you haven’t then please try a preview release.</p>

---

## Post #3 by @agv (2019-12-04 15:37 UTC)

<p>Thanks for the quick answer!</p>
<p>Unfortunately, I am working in 3D Slicer 4.10.2 and I got that error.</p>
<p>Do I have to do something differently or extra in order to import a brachytherapy planning?</p>

---

## Post #4 by @Mik (2019-12-05 12:49 UTC)

<p>Preview release is a 3D Slicer 4.11.0, version 4.10.2 is a stable one.</p>

---

## Post #5 by @agv (2019-12-05 15:36 UTC)

<p>Hello Mikhail, thank you very much for the clarification!</p>
<p>I tried with the 4.11.0 version and it managed to load the RTPLAN, although same error appeared regarding the RTDOSE. However, I just wanted to reconstruct the catheters, so I did not need the dose at all.</p>
<p>Thanks again!</p>

---

## Post #6 by @cpinter (2019-12-05 16:51 UTC)

<p>If you give us access to the dose file we can check to see what’s the problem with loading it.</p>

---

## Post #7 by @agv (2019-12-10 09:10 UTC)

<p>I’ve uploaded a .zip file with the DICOM files to Google Drive:</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/12NMhdl4kI01Epfs6WjNDBQQUPUjcTfwC/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/12NMhdl4kI01Epfs6WjNDBQQUPUjcTfwC/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/12NMhdl4kI01Epfs6WjNDBQQUPUjcTfwC/view?usp=sharing" target="_blank" rel="nofollow noopener">HULP_0000OR3.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Is it ok for you? Thanks in advance!</p>

---

## Post #8 by @cpinter (2019-12-10 19:59 UTC)

<p>Got the file, thank you! I will take a look at it hopefully soon.</p>

---

## Post #9 by @anhthu (2023-12-07 04:45 UTC)

<p>Hello everyone,</p>
<p>I also installed the Slicer RT extension for 3D Slicer 5.4.0. However, I tried to load the files from the DICOM Browser and I got an error:</p>
<p>“Could not load: 1: RTDOSE: Dose for Brachy plan as an RT”</p>
<p>My screenshot file is attached.</p>
<p>Thank you very much in advance</p>
<p>Thu<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/def0b2109a7ddcc541ec1d6a355e5ebb329f34dd.png" data-download-href="/uploads/short-url/vOdGybaO8nnQqfRPAPROFTjl13T.png?dl=1" title="Screenshot (112)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def0b2109a7ddcc541ec1d6a355e5ebb329f34dd_2_690x388.png" alt="Screenshot (112)" data-base62-sha1="vOdGybaO8nnQqfRPAPROFTjl13T" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def0b2109a7ddcc541ec1d6a355e5ebb329f34dd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def0b2109a7ddcc541ec1d6a355e5ebb329f34dd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def0b2109a7ddcc541ec1d6a355e5ebb329f34dd_2_1380x776.png 2x" data-dominant-color="313A41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (112)</span><span class="informations">1920×1080 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
