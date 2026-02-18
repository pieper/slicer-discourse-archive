# MRI to US contour propagation module

**Topic ID**: 15122
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/mri-to-us-contour-propagation-module/15122

---

## Post #1 by @erpoul (2020-12-17 21:19 UTC)

<p>Hi,<br>
I am trying to install the new version of 3D slicer with the Mri to US contour proagation module, but it seems the module doesn’t work well in the new version 4.11.20200930. I have installed Slicer RT and the Segment registration module as well as the Slicer prostate module (manually). I am able to register the volume but I get errors when I want to export the Dicom or calculate de similarity. It seems its not showing the hierarchy name of the patients. I have joinded the error logs. I also used the same data as we first validated it. My 2017 version is still working very well.</p>
<p>Here are the log files :</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Ffile%2Fd%2F1PusLN520AcmPCwF0h00m6836vGQDJwwD%2Fview?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Ffile%2Fd%2F1PusLN520AcmPCwF0h00m6836vGQDJwwD%2Fview?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Ffile%2Fd%2F1PusLN520AcmPCwF0h00m6836vGQDJwwD%2Fview?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Ffile%2Fd%2F1PusLN520AcmPCwF0h00m6836vGQDJwwD%2Fview?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thank you</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2020-12-17 21:20 UTC)

<p>Could you please try with latest Slicer Preview Release, too?</p>

---

## Post #3 by @erpoul (2020-12-18 13:04 UTC)

<p>It is worst with 4.13.0-2020-12-17, this time when loading the US volume it actually split the volume in multiple volume of 1 slice.<br>
[CRITICAL][Stream] 18.12.2020 07:58:39 [] (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)</p>
<p>[CRITICAL][Stream] 18.12.2020 07:58:40 [] (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)</p>
<p>[WARNING][Python] 18.12.2020 07:59:06 [Python] (C:\Users\erpoul\AppData\Local\NA-MIC\Slicer 4.13.0-2020-12-17\lib\Slicer-4.13\qt-scripted-modules\DICOMLib\DICOMBrowser.py:602) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [0]: Image spacing may need to be calibrated for accurate size measurements.</p>

---

## Post #4 by @lassoan (2020-12-18 18:51 UTC)

<p>Could you share a 3D ultrasound volume in DICOM format (anonymized or image of a phantom) so that we can create a rule that allows loading as 3D volume?</p>
<p>The other issue is probably due to a recent Slicer API update. We’ll fix this soon.</p>

---

## Post #5 by @erpoul (2020-12-21 15:00 UTC)

<p>Data sent to you privately, however I think a reference dataset was left with the module to test, I sent you the exact data that were used for the initial release.</p>

---

## Post #6 by @erpoul (2021-06-11 21:14 UTC)

<p>Is the bug resolve in a specific version ?</p>

---

## Post #7 by @lassoan (2021-06-11 21:37 UTC)

<p>Please test with the latest Slicer Preview Release an let us know if you find any issues.</p>

---

## Post #8 by @erpoul (2021-06-16 13:21 UTC)

<p>This time no major bug that prevent from actually using the registration button, however the registration is not performed, only the prealignement is performed … There is no affine nor deformable transform after the registration. 4.13.0-2021-06-14 r29960 / f3899b2 was installed. Just for fun I have calculated also similarity indices from the button and only the Dice table appear, the Hausdorff is not possible to get … The testing was done with the testing data I sent you.</p>

---

## Post #9 by @erpoul (2021-06-16 15:34 UTC)

<p>Finally it still create a problem as I did a mistake and used an older version with 4.13.0-2021-06-14 r29960 / f3899b2 it doesn’t work…</p>
<p>log file sent to you</p>

---
