---
topic_id: 21787
title: "Example Data For Film Dosimetry Analysis"
date: 2022-02-03
url: https://discourse.slicer.org/t/21787
---

# Example data for Film Dosimetry Analysis

**Topic ID**: 21787
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/example-data-for-film-dosimetry-analysis/21787

---

## Post #1 by @johenn66 (2022-02-03 17:41 UTC)

<p>I am trying to locate a downloadable example dataset  for the “Film Dosimetry Analysis” workflow.  Can someone direct me to a downloadable dataset?</p>

---

## Post #2 by @cpinter (2022-02-04 09:41 UTC)

<p>I just uploaded a dataset for you, please find it here: <a href="https://github.com/SlicerRt/SlicerRtData/tree/master/film-dosimetry-01">https://github.com/SlicerRt/SlicerRtData/tree/master/film-dosimetry-01</a></p>

---

## Post #4 by @Thomas_LeDorze (2025-05-13 10:06 UTC)

<p>Hello,<br>
we are trying to use the FilmDosimetryAnalysis module in order to eventually perform a gamma comparison between EBT4 radiochromic films (in .tif or .png format) and an RTDose file in .dcm format. However, when we try to perform the calibration in version 4.10 of Slicer, nothing happens.<br>
Does anyone have a solution?<br>
Thank you.</p>

---

## Post #5 by @cpinter (2025-05-13 14:43 UTC)

<aside class="quote no-group" data-username="Thomas_LeDorze" data-post="4" data-topic="21787">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/d07c76/48.png" class="avatar"> Thomas_LeDorze:</div>
<blockquote>
<p>when we try to perform the calibration in version 4.10 of Slicer, nothing happens.</p>
</blockquote>
</aside>
<p>The module is not supported for several years now, but if you can provide me more information of what does not happen, and if there are any errors in the Python console, what they are, I may be able to help.</p>

---

## Post #6 by @Thomas_LeDorze (2025-05-14 12:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e8bea4e97a01e2bafd402fbc350a826fb4f188.png" data-download-href="/uploads/short-url/gXUZFMGMHKl8uxRe20s66BMLKXu.png?dl=1" title="Pb_Slicer_calibration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e8bea4e97a01e2bafd402fbc350a826fb4f188_2_690x388.png" alt="Pb_Slicer_calibration" data-base62-sha1="gXUZFMGMHKl8uxRe20s66BMLKXu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e8bea4e97a01e2bafd402fbc350a826fb4f188_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e8bea4e97a01e2bafd402fbc350a826fb4f188_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e8bea4e97a01e2bafd402fbc350a826fb4f188_2_1380x776.png 2x" data-dominant-color="A6A4AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pb_Slicer_calibration</span><span class="informations">1920×1080 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello,<br>
Thank you for your response.</p>
<p>We import our film scans (in PNG or TIF format), then in “Load calibration dose” we enter the corresponding doses. However, when we click on “Perform calibration”, we never obtain a calibration curve or its coefficients.</p>
<p>Below you will find the errors returned by the program or as an attachment :</p>
<p>Python 2.7.13 (default, May 16 2019, 14:27:45) [MSC v.1900 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “\s-dds\dds\Soins\Medico-technique\Physique Medicale\NOUVELLE ARBORESENCE\Radiotherapie\Logiciels\3DSlicer\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SegmentEditorEffects_<em>init</em>_.py”, line 5, in <br>
from SegmentEditorDrawEffect import *<br>
File “\s-dds\dds\Soins\Medico-technique\Physique Medicale\NOUVELLE ARBORESENCE\Radiotherapie\Logiciels\3DSlicer\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SegmentEditorEffects\SegmentEditorDrawEffect.py”, line 4, in <br>
from SegmentEditorEffects import *<br>
File “\s-dds\dds\Soins\Medico-technique\Physique Medicale\NOUVELLE ARBORESENCE\Radiotherapie\Logiciels\3DSlicer\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SegmentEditorEffects\SegmentEditorEffects_<em>init</em>_.py”, line 3, in <br>
from AbstractScriptedSegmentEditorAutoCompleteEffect import *<br>
ImportError: No module named AbstractScriptedSegmentEditorAutoCompleteEffect<br>
Calibration: Mean value for flood field image in ROI = 166.2898<br>
Calibration: Mean value for calibration image for 4499.0 cGy in ROI = 19.1761, OD = 0.9381<br>
Calibration: Mean value for calibration image for 3001.0 cGy in ROI = 24.5731, OD = 0.8304<br>
Calibration: Mean value for calibration image for 1720.0 cGy in ROI = 36.3917, OD = 0.6599<br>
Calibration: Mean value for calibration image for 1000.0 cGy in ROI = 52.3595, OD = 0.5019<br>
Calibration: Mean value for calibration image for 500.0 cGy in ROI = 74.3727, OD = 0.3495<br>
Calibration: Mean value for calibration image for 220.0 cGy in ROI = 105.1962, OD = 0.1989<br>
Traceback (most recent call last):<br>
File “C:/Users/M1081468/AppData/Roaming/NA-MIC/Extensions-28257/FilmDosimetryAnalysis/lib/Slicer-4.10/qt-scripted-modules/FilmDosimetryAnalysis.py”, line 1272, in onPerformCalibrationButton<br>
message = self.logic.performCalibration(floodFieldImageVolumeNode, calibrationDoseToVolumeNodeMap)<br>
File “C:\Users\M1081468\AppData\Roaming\NA-MIC\Extensions-28257\FilmDosimetryAnalysis\lib\Slicer-4.10\qt-scripted-modules\FilmDosimetryAnalysisLogic\FilmDosimetryAnalysisLogic.py”, line 350, in performCalibration<br>
self.findBestFittingCalibrationFunctionCoefficients()<br>
File “C:\Users\M1081468\AppData\Roaming\NA-MIC\Extensions-28257\FilmDosimetryAnalysis\lib\Slicer-4.10\qt-scripted-modules\FilmDosimetryAnalysisLogic\FilmDosimetryAnalysisLogic.py”, line 238, in findBestFittingCalibrationFunctionCoefficients<br>
coeffs = self.findCoefficientsForExponent(n)<br>
File “C:\Users\M1081468\AppData\Roaming\NA-MIC\Extensions-28257\FilmDosimetryAnalysis\lib\Slicer-4.10\qt-scripted-modules\FilmDosimetryAnalysisLogic\FilmDosimetryAnalysisLogic.py”, line 261, in findCoefficientsForExponent<br>
functionConstantTerms = numpy.linalg.lstsq(functionTermsMatrix,functionDoseTerms,rcond=None)<br>
File “\s-dds\dds\Soins\Medico-technique\Physique Medicale\NOUVELLE ARBORESENCE\Radiotherapie\Logiciels\3DSlicer\Slicer 4.10.2\lib\Python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg\numpy\linalg\linalg.py”, line 1953, in lstsq<br>
0, work, -1, iwork, 0)<br>
TypeError: a float is required<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66522b2c16bc9334770c338d741ab3c8c21b4759.png" data-download-href="/uploads/short-url/eBaKllo4YTXSlPxwEJVm9QzKOp3.png?dl=1" title="error_script_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66522b2c16bc9334770c338d741ab3c8c21b4759.png" alt="error_script_slicer" data-base62-sha1="eBaKllo4YTXSlPxwEJVm9QzKOp3" width="690" height="190" data-dominant-color="FDF5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_script_slicer</span><span class="informations">1897×524 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2025-05-28 10:01 UTC)

<p>Sorry for the delay. I looked at the code, but it is impossible to tell the cause of the error without debugging that version of Slicer with the data you use.</p>
<p>Does it work if you try the test data?</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRtData/tree/master/film-dosimetry-01">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRtData/tree/master/film-dosimetry-01" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRtData/tree/master/film-dosimetry-01" target="_blank" rel="noopener">SlicerRtData/film-dosimetry-01 at master · SlicerRt/SlicerRtData</a></h3>


  <p><span class="label1">Sample DICOM-RT datasets for demonstration and testing purposes - SlicerRt/SlicerRtData</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
