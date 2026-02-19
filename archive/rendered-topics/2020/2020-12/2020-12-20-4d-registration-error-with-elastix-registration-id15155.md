---
topic_id: 15155
title: "4D Registration Error With Elastix Registration"
date: 2020-12-20
url: https://discourse.slicer.org/t/15155
---

# 4D registration error with Elastix Registration

**Topic ID**: 15155
**Date**: 2020-12-20
**URL**: https://discourse.slicer.org/t/4d-registration-error-with-elastix-registration/15155

---

## Post #1 by @marianaslicer (2020-12-20 16:00 UTC)

<p>Hi everyone,</p>
<p>I’m on the preview release version (4.13) and I’m using the Slicer Elastix module to perform non-rigid registration in the 4D CT dataset of lungs. Firstly, I tried to use the default preset (rigid + bspline parameters) with success since the warped volume was correctly aligned with the reference volume.</p>
<p>Even so, since the patient’s anatomy is nearly the same over the breathing phases (the movement is predominantly in the lungs and diaphragm), I just want to use b-spline parameters. To do so, I added the ‘par0007’ preset to the parameter file database (<a href="http://elastix.bigr.nl/wiki/index.php/Par0007" rel="noopener nofollow ugc">http://elastix.bigr.nl/wiki/index.php/Par0007</a>) which seems to be more suitable for my data type. However, when I tried to run the registration, I got the following message regarding the last parameter file (Parameters.MI.RP.Bspline_tuned.txt):</p>
<blockquote>
<p>Running elastix with parameter file 2: “C:\Users\MIM\AppData\Roaming\NA-MIC\Extensions-29506\SlicerElastix\lib\Slicer-4.13\qt-scripted-modules\Resources\RegistrationParameters\Parameters.MI.RP.Bspline_tuned.txt”.</p>
<p>Current time: Sun Dec 20 15:13:23 2020.<br>
Reading the elastix parameters from file …</p>
<p>Error:<br>
MattesMutualInformationWithRigidityPenalty(index 3) - This component is not installed!<br>
ERROR: error occurred while creating Metric 0.</p>
<p>itk::ExceptionObject (000000000024F710)<br>
Location: “unknown”<br>
File: D:\D\P\S-0-E-b\SlicerElastix-build\elastix\Core\Kernel\elxElastixMain.cxx<br>
Line: 827<br>
Description: itk::ERROR: itk::ERROR: ElastixMain(00000000022942B0): The following component could not be created: MattesMutualInformationWithRigidityPenalty</p>
<p>ERROR:<br>
One or more components could not be created.<br>
Errors occurred!<br>
vtkDebugLeaks has found no leaks.</p>
<p>Command ‘elastix’ returned non-zero exit status 1.<br>
Traceback (most recent call last):<br>
File “C:/Users/MIM/AppData/Roaming/NA-MIC/Extensions-29506/SlicerElastix/lib/Slicer-4.13/qt-scripted-modules/Elastix.py”, line 335, in onApplyButton<br>
forceDisplacementFieldOutputTransform = self.forceDisplacementFieldOutputChecbox.checked)<br>
File “C:/Users/MIM/AppData/Roaming/NA-MIC/Extensions-29506/SlicerElastix/lib/Slicer-4.13/qt-scripted-modules/Elastix.py”, line 807, in registerVolumes<br>
self.logProcessOutput(ep)<br>
File “C:/Users/MIM/AppData/Roaming/NA-MIC/Extensions-29506/SlicerElastix/lib/Slicer-4.13/qt-scripted-modules/Elastix.py”, line 728, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>
</blockquote>
<p>Does anyone know why this is happening? and how to fix it?</p>
<p>Thank you!</p>

---
