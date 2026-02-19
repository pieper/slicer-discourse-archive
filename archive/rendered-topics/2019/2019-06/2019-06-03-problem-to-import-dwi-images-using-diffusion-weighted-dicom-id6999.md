---
topic_id: 6999
title: "Problem To Import Dwi Images Using Diffusion Weighted Dicom"
date: 2019-06-03
url: https://discourse.slicer.org/t/6999
---

# Problem to import DWI images using Diffusion-weighted DICOM Import (DWIConvert)

**Topic ID**: 6999
**Date**: 2019-06-03
**URL**: https://discourse.slicer.org/t/problem-to-import-dwi-images-using-diffusion-weighted-dicom-import-dwiconvert/6999

---

## Post #1 by @shahrokh (2019-06-03 04:16 UTC)

<p>Dears 3DSlicer developers:</p>
<pre><code>Specification:
Fedora Core 25 (Linux localhost.localdomain 4.8.6-300.fc25.x86_64)
3DSlicer versions 4.8.1
3DSlicer versions 4.9.0
3DSlicer versions 4.10.0
</code></pre>
<p>I have 1768 DWI images (<strong>from</strong> ep2d__FOV256_ISO2mm_i1.dcm <strong>to</strong> ep2d__FOV256_ISO2mm_i1768.dcm), 68 slices per volume and 26 volumes</p>
<p>I want to use “UKF Tractogrpahy” module to analyze these image. To do this and import images, I think that I should use the module of “Diffusion-weighted DICOM Import (DWIConvert)” with the following setup.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d256524e68efbd7123a3b18c9bd5d2d5703255d1.png" data-download-href="/uploads/short-url/u0Jd83JAsLfqg30gKPzL2344TpD.png?dl=1" title="ScreenshotDWIConvert" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d256524e68efbd7123a3b18c9bd5d2d5703255d1_2_404x500.png" alt="ScreenshotDWIConvert" data-base62-sha1="u0Jd83JAsLfqg30gKPzL2344TpD" width="404" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d256524e68efbd7123a3b18c9bd5d2d5703255d1_2_404x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d256524e68efbd7123a3b18c9bd5d2d5703255d1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d256524e68efbd7123a3b18c9bd5d2d5703255d1.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotDWIConvert</span><span class="informations">600×741 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I execute this module, I get the following error message:</p>
<blockquote>
<p>/home/sn/Slicer-4.8.1-linux-amd64/lib/Slicer-4.8/cli-modules/DWIConvert --conversionMode DicomToNrrd --inputDicomDirectory /home/sn/Diffusion --outputNiftiFile /home/sn/Diffusion/test --outputBValues /home/sn/Diffusion/test --outputBVectors /home/sn/Diffusion/test --outputDirectory . --smallGradientThreshold 0.2 --transposeInputBVectors</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard output:</p>
<p>======= DWI Convert Public Lib Ctest =========<br>
=================== this-&gt;m_SlicesPerVolume:68<br>
Dicom images are ordered in a volume interleaving way.<br>
ImageOrientationPatient (0020:0037): LPS Orientation Matrix<br>
0.999997 3.3575e-08 0.00238174<br>
-0.000420449 0.984298 0.176516<br>
-0.00234433 -0.176516 0.984295</p>
<p>this-&gt;m_SpacingMatrix<br>
2 0 0<br>
0 2 0<br>
0 0 2</p>
<p>NRRDSpaceDirection<br>
1.99999 6.71501e-08 0.00476347<br>
-0.000840897 1.9686 0.353032<br>
-0.00468866 -0.353033 1.96859</p>
<p>Slice 0: -136.139 -145.778 33.773<br>
Slice 1: -136.135 -145.425 35.7416<br>
Slice order is IS<br>
Image#: 0 BV: 0 GD: 0,0,0<br>
Number of Directions : 3<br>
Directions 0: 0.86221<br>
Directions 1: -0.362712<br>
Directions 2: 0.353602<br>
DiffusionVector_magnitude 1<br>
Image#: 68 BV: 1000 GD: 0.86220956,-0.36271203,0.35360244<br>
Number of Directions : 3<br>
Directions 0: 0.863006<br>
Directions 1: 0.36176<br>
Directions 2: 0.352634<br>
DiffusionVector_magnitude 1<br>
Image#: 136 BV: 1000 GD: 0.86300552,0.36176044,0.35263431<br>
Number of Directions : 3<br>
Directions 0: 0.862383<br>
Directions 1: 0.362935<br>
Directions 2: -0.352951<br>
DiffusionVector_magnitude 1<br>
Image#: 204 BV: 1000 GD: 0.86238289,0.36293468,-0.35295057<br>
Number of Directions : 3<br>
Directions 0: 0.863359<br>
Directions 1: -0.361339<br>
Directions 2: -0.352202<br>
DiffusionVector_magnitude 1<br>
Image#: 272 BV: 1000 GD: 0.8633585,-0.36133933,-0.35220158<br>
Number of Directions : 3<br>
Directions 0: 0.357315<br>
Directions 1: -0.361901<br>
Directions 2: -0.861019<br>
DiffusionVector_magnitude 1<br>
Image#: 340 BV: 1000 GD: 0.35731497,-0.3619009,-0.86101902<br>
Number of Directions : 3<br>
Directions 0: 0.356462<br>
Directions 1: -0.865857<br>
Directions 2: -0.351035<br>
DiffusionVector_magnitude 1<br>
Image#: 408 BV: 1000 GD: 0.35646203,-0.86585736,-0.35103545<br>
Number of Directions : 3<br>
Directions 0: 0.355873<br>
Directions 1: -0.865479<br>
Directions 2: 0.352564<br>
DiffusionVector_magnitude 1<br>
Image#: 476 BV: 1000 GD: 0.35587266,-0.86547863,0.35256404<br>
Number of Directions : 3<br>
Directions 0: 0.356936<br>
Directions 1: -0.36273<br>
Directions 2: 0.860828<br>
DiffusionVector_magnitude 1<br>
Image#: 544 BV: 1000 GD: 0.35693565,-0.36272988,0.86082757<br>
Number of Directions : 3<br>
Directions 0: 0.357965<br>
Directions 1: 0.361675<br>
Directions 2: 0.860844<br>
DiffusionVector_magnitude 1<br>
Image#: 612 BV: 1000 GD: 0.35796461,0.36167514,0.86084408<br>
Number of Directions : 3<br>
Directions 0: 0.356507<br>
Directions 1: 0.865463<br>
Directions 2: 0.351961<br>
DiffusionVector_magnitude 1<br>
Image#: 680 BV: 1000 GD: 0.35650745,0.8654629,0.35196099<br>
Number of Directions : 3<br>
Directions 0: 0.35609<br>
Directions 1: 0.865654<br>
Directions 2: -0.351912<br>
DiffusionVector_magnitude 1<br>
Image#: 748 BV: 1000 GD: 0.35609004,0.86565441,-0.35191223<br>
Number of Directions : 3<br>
Directions 0: 0.357203<br>
Directions 1: 0.363002<br>
Directions 2: -0.860602<br>
DiffusionVector_magnitude 1<br>
Image#: 816 BV: 1000 GD: 0.3572031,0.36300167,-0.86060208<br>
Image#: 884 BV: 0 GD: 0,0,0<br>
Number of Directions : 3<br>
Directions 0: 0.86221<br>
Directions 1: -0.362712<br>
Directions 2: 0.353602<br>
DiffusionVector_magnitude 1<br>
Image#: 952 BV: 1000 GD: 0.86220956,-0.36271203,0.35360244<br>
Number of Directions : 3<br>
Directions 0: 0.863006<br>
Directions 1: 0.36176<br>
Directions 2: 0.352634<br>
DiffusionVector_magnitude 1<br>
Image#: 1020 BV: 1000 GD: 0.86300552,0.36176044,0.35263431<br>
Number of Directions : 3<br>
Directions 0: 0.862383<br>
Directions 1: 0.362935<br>
Directions 2: -0.352951<br>
DiffusionVector_magnitude 1<br>
Image#: 1088 BV: 1000 GD: 0.86238289,0.36293468,-0.35295057<br>
Number of Directions : 3<br>
Directions 0: 0.863359<br>
Directions 1: -0.361339<br>
Directions 2: -0.352202<br>
DiffusionVector_magnitude 1<br>
Image#: 1156 BV: 1000 GD: 0.8633585,-0.36133933,-0.35220158<br>
Number of Directions : 3<br>
Directions 0: 0.357315<br>
Directions 1: -0.361901<br>
Directions 2: -0.861019<br>
DiffusionVector_magnitude 1<br>
Image#: 1224 BV: 1000 GD: 0.35731497,-0.3619009,-0.86101902<br>
Number of Directions : 3<br>
Directions 0: 0.356462<br>
Directions 1: -0.865857<br>
Directions 2: -0.351035<br>
DiffusionVector_magnitude 1<br>
Image#: 1292 BV: 1000 GD: 0.35646203,-0.86585736,-0.35103545<br>
Number of Directions : 3<br>
Directions 0: 0.355873<br>
Directions 1: -0.865479<br>
Directions 2: 0.352564<br>
DiffusionVector_magnitude 1<br>
Image#: 1360 BV: 1000 GD: 0.35587266,-0.86547863,0.35256404<br>
Number of Directions : 3<br>
Directions 0: 0.356936<br>
Directions 1: -0.36273<br>
Directions 2: 0.860828<br>
DiffusionVector_magnitude 1<br>
Image#: 1428 BV: 1000 GD: 0.35693565,-0.36272988,0.86082757<br>
Number of Directions : 3<br>
Directions 0: 0.357965<br>
Directions 1: 0.361675<br>
Directions 2: 0.860844<br>
DiffusionVector_magnitude 1<br>
Image#: 1496 BV: 1000 GD: 0.35796461,0.36167514,0.86084408<br>
Number of Directions : 3<br>
Directions 0: 0.356507<br>
Directions 1: 0.865463<br>
Directions 2: 0.351961<br>
DiffusionVector_magnitude 1<br>
Image#: 1564 BV: 1000 GD: 0.35650745,0.8654629,0.35196099<br>
Number of Directions : 3<br>
Directions 0: 0.35609<br>
Directions 1: 0.865654<br>
Directions 2: -0.351912<br>
DiffusionVector_magnitude 1<br>
Image#: 1632 BV: 1000 GD: 0.35609004,0.86565441,-0.35191223<br>
Number of Directions : 3<br>
Directions 0: 0.357203<br>
Directions 1: 0.363002<br>
Directions 2: -0.860602<br>
DiffusionVector_magnitude 1<br>
Image#: 1700 BV: 1000 GD: 0.3572031,0.36300167,-0.86060208</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>Error: the output file type is not supported currently<br>
Error: the output file type is not supported currently<br>
Invalidate conversion mode<br>
Diffusion-weighted DICOM Import (DWIConvert) completed with errors</p>
</blockquote>
<p>I must mention that I get the same error in 3DSlicer versions 4.8.1, 4.9.0 and 4.10.0.<br>
Please guide me.</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @ljod (2019-06-03 11:19 UTC)

<p>Please use the new release 4.10.2 and the new module dcm2niix GUI. This should load a much more comprehensive set of recent DICOM DWI.</p>
<p>Let us know if this works for you.</p>

---

## Post #3 by @shahrokh (2019-06-03 13:00 UTC)

<p>Dear Lauren</p>
<p>Thank you very very much. This is an excellent version. My problem was solved.<br>
Best regards.</p>

---

## Post #4 by @ljod (2019-06-03 13:55 UTC)

<p>Great!! Thanks for letting us know that the new release solves this issue.</p>

---
