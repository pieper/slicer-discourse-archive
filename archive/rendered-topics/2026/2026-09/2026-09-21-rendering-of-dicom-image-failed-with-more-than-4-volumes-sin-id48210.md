---
topic_id: 48210
title: "Rendering of DICOM image failed with more than 4 volumes since version 12"
date: 2026-09-21
url: https://discourse.slicer.org/t/48210
last_bumped: 2026-09-22T04:14:26.110Z
---

# Rendering of DICOM image failed with more than 4 volumes since version 12

**Topic ID**: 48210
**Date**: 2026-09-21
**URL**: https://discourse.slicer.org/t/rendering-of-dicom-image-failed-with-more-than-4-volumes-since-version-12/48210

---

## Post #1 by @mhouse (2026-09-21 13:58 UTC)

<p>Since version 12 (also with version 13) 3D Slicer crashes, because it cannot render an image with more than 4 volumes. At least with the version Slicer-5.11.0-2026-03-20-linux-amd64 it is working with 9 volumes, for e.g. a GE Multiphase volume.</p>
<blockquote>
<p>Slicer-5.12.4-linux-amd64$ ./Slicer<br>
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.<br>
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.</p>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “DICOM”<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
E: invalid value for ‘PhotometricInterpretation’ (YBR_RCT)<br>
W: Rendering of DICOM image failed for thumbnail failed: Invalid element value<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).<br>
error: [/home/Slicer-5.12.4-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>

---

## Post #2 by @pieper (2026-09-21 14:07 UTC)

<p>Thanks for the report.  Are you able to share data to replicate the issue?</p>

---

## Post #3 by @mhouse (2026-09-21 14:17 UTC)

<p>Hello,</p>
<p>yes if it would help. Do you need the sequence or the log from version 11, if the log contains any information about the loading of the 9 volume sequence. So long I use the version 11, but the component display, either as RGBA or separate, is only available in further versions.</p>
<p>If you need the sequence then I need to remove the personal data. It’s my heart issue, it’s from the last Hi-Res CCTA.</p>
<p>Kindest regards</p>

---

## Post #4 by @fedorov (2026-09-21 14:31 UTC)

<p><a class="mention" href="/u/mhouse">@mhouse</a> you can check DICOM conformance of the files using the <code>dciodvfy</code> validator, which is available via this web page: <a href="https://imagingdatacommons.github.io/dicom3tools-web-distributions/">https://imagingdatacommons.github.io/dicom3tools-web-distributions/</a> and send back the output to help with debugging this issue.</p>
<p><em>If you send back the output, please look over it first to make sure no sensitive information is included!</em></p>
<p>That validation is done in the browser, and no files are uploaded anywhere. The source code is available here: <a href="https://github.com/ImagingDataCommons/dicom3tools-web-distributions">https://github.com/ImagingDataCommons/dicom3tools-web-distributions</a>.</p>

---

## Post #5 by @mhouse (2026-09-21 15:31 UTC)

<p>it will take some time, because the dataset is about 1,6Gb and consists of more than 8500 files. I have not done so much with the DICOM files in the past, I was just loading them into 3D Slicer.</p>
<p>I think after version 11 someone has limited the max. of data size. Therefore this error message. The messages before are maybe not related to this issue.</p>
<p>Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s)</p>

---

## Post #6 by @pieper (2026-09-21 16:06 UTC)

<p><a class="mention" href="/u/mhouse">@mhouse</a> It would be great if you could share the data, but no pressure since it’s private.</p>
<p>There are several de-identification tools available. None of them are guaranteed to be 100% effective at removing all identifiers, but <a href="https://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html">David Clunie’s DicomCleaner</a> is probably as good as you can find.</p>
<p>It would be good if you could confirm the behavior is the same after deidentification, since changing the tags may change how Slicer interprets the data.</p>
<p>Or if you decide not to share the data then the full logs from both versions of Slicer may be enough to help diagnose (maybe do that first if it’s easier).</p>

---

## Post #7 by @mhouse (2026-09-22 04:06 UTC)

<p>I don’t know how you want to get the logfiles, because I cannot attach them here directly. Please find the last lines of version 5.13 below.</p>
<p>I have only started the app and loaded the DICOM sequence from the DICOM database (w/o Advanced checked). After dragging the Multiphase sequence into the VR window 3D Slicer crashed with version 5.13. With version 5.11 it’s loading and displaying fine.</p>
<pre><code class="lang-auto">...

DICOMScalarVolumePlugin.py:441) - Loading with imageIOName: GDCM
[DEBUG][Python] 21.09.2026 19:33:56 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:563) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_7' from SOP instance 1.2.840.113619.2.416.8924333666940351969290340049978143130.1921.
[INFO][Python] 21.09.2026 19:33:57 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:441) - Loading with imageIOName: GDCM
[DEBUG][Python] 21.09.2026 19:34:04 [Python] (/home/m/install/Slicer-5.13.0-2026-08-05-linux-amd64/bin/../lib/Slicer-5.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:563) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_8' from SOP instance 1.2.840.113619.2.416.7813687437206210351250794399055596848.2177.
[DEBUG][Qt] 21.09.2026 19:34:42 [] (unknown:0) - Switch to module:  "Data"
[ERROR][VTK] 21.09.2026 19:35:15 [vtkOpenGLGPUVolumeRayCastMapper (0x46a56d50)] (vtkGPUVolumeRayCastMapper.cxx:424) - Only 1 - 4 component scalars are supported by this mapper.The input data has 9 component(s).
</code></pre>

---

## Post #8 by @mhouse (2026-09-22 04:14 UTC)

<p>with version 5.11 it looks similar in the logfile before the crash.</p>
<pre><code class="lang-auto">...

[INFO][Python] 22.09.2026 05:22:48 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM
[DEBUG][Python] 22.09.2026 05:22:53 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_7' from SOP instance 1.2.840.113619.2.416.8924333666940351969290340049978143130.1921.
[INFO][Python] 22.09.2026 05:22:53 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:445) - Loading with imageIOName: GDCM
[DEBUG][Python] 22.09.2026 05:22:59 [Python] (/home/m/install/Slicer-5.11.0-2025-11-19-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:567) - DICOM window/level (105.0/860.0) set to volume '315: Multiphase_8' from SOP instance 1.2.840.113619.2.416.7813687437206210351250794399055596848.2177.
[DEBUG][Qt] 22.09.2026 05:34:20 [] (unknown:0) - Switch to module:  ""
</code></pre>

---
