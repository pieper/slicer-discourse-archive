---
topic_id: 37556
title: "Elastix Registration With Masking"
date: 2024-07-25
url: https://discourse.slicer.org/t/37556
---

# Elastix registration with Masking

**Topic ID**: 37556
**Date**: 2024-07-25
**URL**: https://discourse.slicer.org/t/elastix-registration-with-masking/37556

---

## Post #1 by @khajta (2024-07-25 09:54 UTC)

<p>Dear experts,<br>
I would like to register 2 images, CT and CT. Actually, my final goal is to register SPECT and SPECT with different timepoint.</p>
<p>Firstly, I used rigid registration followed by elastix between CT1 and CT2 at different timepoint. Then I use these transformation matrices to SPECT2. The result looked well for organ but not tumor. I would like to use masking in elastix. I apply segmented tumor. The result showed error.</p>
<p>Failed to compute results.</p>
<p>Command ‘elastix’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):<br>
File “D:\slicer\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “D:/slicer/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Elastix.py”, line 314, in onApplyButton<br>
self.logic.registerVolumesUsingParameterNode(self._parameterNode)<br>
File “D:/slicer/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Elastix.py”, line 591, in registerVolumesUsingParameterNode<br>
self.registerVolumes(<br>
File “D:/slicer/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Elastix.py”, line 637, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “D:/slicer/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules/Elastix.py”, line 572, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #2 by @Matteboo (2024-07-25 10:01 UTC)

<p>This means that the error is inside elastix<br>
To get a better understanding of the error, you need to read the elastix log.<br>
To do that, tick the “keep temporary files” box, launch your regisrtration then click on “show temp folder”<br>
There’s a text file called elastix, if you go to the bottom of the file, you should get a more helpfull error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134c6a1999e3cbb32aa06b21fa68ed5ef836671a.png" data-download-href="/uploads/short-url/2KIMVunHUApGyzVrKhQRuRCcoP0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/134c6a1999e3cbb32aa06b21fa68ed5ef836671a_2_412x500.png" alt="image" data-base62-sha1="2KIMVunHUApGyzVrKhQRuRCcoP0" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/134c6a1999e3cbb32aa06b21fa68ed5ef836671a_2_412x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134c6a1999e3cbb32aa06b21fa68ed5ef836671a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134c6a1999e3cbb32aa06b21fa68ed5ef836671a.png 2x" data-dominant-color="403F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">434×526 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @khajta (2024-07-26 03:31 UTC)

<p>Thank you for your reply.</p>
<p>The text file showed</p>
<p>itk::ExceptionObject (0000003B772FC9B0)<br>
Location: “ElastixTemplate - Run()”<br>
File: D:\D\S\S-0-E-b\SlicerElastix-build\elastix\Common\CostFunctions\itkAdvancedImageToImageMetric.hxx<br>
Line: 916<br>
Description: ITK ERROR: AdvancedMattesMutualInformationMetric(0000020314FC7190): Too many samples map outside moving image buffer: 510 / 2048</p>
<p>Error occurred during actual registration.</p>
<p>Errors occurred!</p>

---

## Post #4 by @Matteboo (2024-07-29 12:37 UTC)

<p>It’s hard to help you without example, but you can try these:</p>
<ul>
<li>Center both of your volume (giving them the same origin)</li>
<li>Make sure that your volumes are of similar sizes</li>
</ul>

---
