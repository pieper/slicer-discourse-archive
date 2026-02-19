---
topic_id: 41135
title: "Opendose3D Youtube Channel"
date: 2025-01-17
url: https://discourse.slicer.org/t/41135
---

# OpenDose3D YouTube channel

**Topic ID**: 41135
**Date**: 2025-01-17
**URL**: https://discourse.slicer.org/t/opendose3d-youtube-channel/41135

---

## Post #1 by @Alex_Vergara (2025-01-17 20:35 UTC)

<p>Hello</p>
<p>I want to announce the start of <a href="https://www.youtube.com/@OpenDose3D" rel="noopener nofollow ugc">OpenDose3D YouTube channel</a>.</p>
<p>OpenDose3D is a 3DSlicer extension for Patient dosimetry in internal radiotherapy. Please subscribe and leave us your comments.</p>

---

## Post #2 by @imbeatriz (2025-01-22 13:39 UTC)

<p>Hi!</p>
<p>I was following the video tutorial 02 Testing OD3D and am facing a weird issue when I select the Utilities → Run Test. I receive the following message on the Python console:</p>
<p>[Python] DICOM test data dir: /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57<br>
[Python] Successfully loaded patient 1 with StudyInstanceUID: 1.2.752.37.5.626934496.20171125.26473.4.1934 and SeriesInstanceUID: 1.3.6.1.4.1.33868.20191002120418.51247<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 48HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 4HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 1HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 24HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 1HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 96HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 24HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 48HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 4HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 96HR<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 48HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 4HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 1HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 24HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 96HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
Traceback (most recent call last):<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/OpenDose3D.py”, line 1228, in onRunTestButton<br>
self.test.FullTest_positive()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Logic/OpenDose3DTest.py”, line 542, in FullTest_positive<br>
self.logic.createTransforms(referenceNode.data)<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Logic/OpenDose3DLogic.py”, line 919, in createTransforms<br>
Elastix.RegistrationPresets_ParameterFilenames<br>
AttributeError: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’<br>
[Python] Cannot load preset. Loading failed with error: [Errno 2] No such file or directory: ‘/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/par0013Powell_NGC_singleImage.txt’<br>
[Qt] An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png</a>’. This content should also be served over HTTPS.<br>
[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[Qt] A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>.</p>
<p>Could you help me with what could be causing this?</p>
<p>Thank you!</p>
<p>Greetings,<br>
Beatriz</p>

---

## Post #3 by @muratmaga (2025-01-22 16:25 UTC)

<aside class="quote no-group" data-username="imbeatriz" data-post="2" data-topic="41135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e8c25b/48.png" class="avatar"> imbeatriz:</div>
<blockquote>
<p>Elastix.RegistrationPresets_ParameterFilenames<br>
AttributeError: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’<br>
[Python] Cannot load preset. Loading failed with error: [Errno 2] No such file or directory: ‘/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/</p>
</blockquote>
</aside>
<p>Is the Elastix extension installed? There is an error about not finding the directory:</p>
<pre><code class="lang-auto">AttributeError: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’
[Python] Cannot load preset. Loading failed with error: [Errno 2] No such file or directory: ‘/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/</code></pre>

---

## Post #4 by @imbeatriz (2025-01-22 16:28 UTC)

<p>Hi,</p>
<p>I checked and it is installed. The name of the module tho that appears to me is SlicerElastix.</p>

---

## Post #5 by @muratmaga (2025-01-22 16:45 UTC)

<p>It is not finding the registration presets. That looks like an issue with Elastix to me. Perhaps try running the Elastix by itself to register a dataset and see if it is correctly installed?</p>

---

## Post #6 by @imbeatriz (2025-01-22 16:55 UTC)

<p>Hi,</p>
<p>I tried running Elastix by itself and it shows me this message on the python console:</p>
<p>[Python] Cannot load preset. Loading failed with error: [Errno 2] No such file or directory: ‘/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/par0013Powell_NGC_singleImage.txt’</p>
<p>I am confused because the file exists and it’s present in that directory.</p>

---

## Post #7 by @muratmaga (2025-01-22 16:57 UTC)

<p>At least you know the issue with Elastix. I am not familiar with unfortunately.<br>
So in the shell window if you do</p>
<p><code>ls -l  /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/par0013Powell_NGC_singleImage.txt</code></p>
<p>you see a file?</p>

---

## Post #8 by @imbeatriz (2025-01-22 17:09 UTC)

<p>Yes I see. I even went to the directory itself and opened it.</p>
<p>administrator@Pacheca-IBEB:~$ ls -l /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/Par0013Powell_NGC_singleImage.txt<br>
-rw-r–r-- 1 administrator administrator 1796 Jan 22 16:39 /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Resources/RegistrationParameters/Par0013Powell_NGC_singleImage.txt</p>
<p>I think I see what is wrong. My file is called Par0013Powell_NGC_singleImage.txt while the one 3d Slicer is trying to find is par0013Powell_NGC_singleImage.txt. it’s all because of the letter P.<br>
I just changed to a small letter p the name of the file and I don’t get the error for Elastix.</p>

---

## Post #9 by @imbeatriz (2025-01-22 17:19 UTC)

<p>I still get this extensive error when I try to do the run test of OpenDose3D tho.</p>
<p>[Python] DICOM test data dir: /home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57<br>
[Python] Successfully loaded patient 1 with StudyInstanceUID: 1.2.752.37.5.626934496.20171125.26473.4.1934 and SeriesInstanceUID: 1.3.6.1.4.1.33868.20191002120418.51247<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 48HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 4HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 1HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 24HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 1HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 96HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 24HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 48HR<br>
[Python] Cannot get DICOM slice positions for volume 1: CT SPECT-CT 4HR<br>
[Python] Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 96HR<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 48HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 4HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 1HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 24HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’<br>
[Python] Attribute ‘DICOM.Acquisition.Duration’ is empty<br>
[Python] No injection time and no timestamp in name for node 1: ACSC SPECT-CT 96HR<br>
[Python] Failed to retrieve DICOM attribute: DICOM.Injection.Date<br>
Traceback (most recent call last):<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/OpenDose3D.py”, line 1228, in onRunTestButton<br>
self.test.FullTest_positive()<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Logic/OpenDose3DTest.py”, line 542, in FullTest_positive<br>
self.logic.createTransforms(referenceNode.data)<br>
File “/home/administrator/Software/Slicer-5.6.2-linux-amd64/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Logic/OpenDose3DLogic.py”, line 919, in createTransforms<br>
Elastix.RegistrationPresets_ParameterFilenames<br>
AttributeError: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’</p>

---

## Post #10 by @fragosoj (2025-01-31 14:29 UTC)

<p>This has already been fixed in the latest update of OpenDose3D (2025-01-24).</p>

---

## Post #11 by @akmal871026 (2025-02-09 07:52 UTC)

<p>Dear <a class="mention" href="/u/imbeatriz">@imbeatriz</a> ,</p>
<p>For version 5.8.0, its more better for OpenDose3D. Perhaps you try it. Especially in OAR segmentation, very nice.</p>

---

## Post #12 by @imbeatriz (2025-02-09 13:13 UTC)

<p>Hi,</p>
<p>I tried and it’s working perfectly!</p>
<p>Thank you!</p>

---
