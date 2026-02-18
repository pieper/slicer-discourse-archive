# RuntimeError: Exception thrown in SimpleITK ImageSeriesReader_Execute: D:\D\P\S-0-build\ITK\Modules\IO\GDCM\src\itkGDCMImageIO.cxx:462: ITK ERROR: GDCMImageIO(00000285738E9DB0): Cannot read requested file

**Topic ID**: 29658
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/runtimeerror-exception-thrown-in-simpleitk-imageseriesreader-execute-d-d-p-s-0-build-itk-modules-io-gdcm-src-itkgdcmimageio-cxx-itk-error-gdcmimageio-00000285738e9db0-cannot-read-requested-file/29658

---

## Post #1 by @Dex2046 (2023-05-26 00:47 UTC)

<p>call for help. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>I’m trying to use pet-must-segmenter, when I click perform segmentation, I got  errors like below</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/DEX/AppData/Local/slicer.org/Slicer/slicer.org/Extensions-31757/PET-MUST-Segmenter/lib/Slicer-5.3/qt-scripted-modules/MUSTsegmenter.py”, line 236, in onSegmentationButton<br>
self.segmentationLogic.performSegmentation(self.organSegments, self.segmentationMethods, self.suvPerRoi,<br>
File “C:/Users/DEX/AppData/Local/slicer.org/Slicer/slicer.org/Extensions-31757/PET-MUST-Segmenter/lib/Slicer-5.3/qt-scripted-modules/MUSTsegmenter.py”, line 474, in performSegmentation<br>
suvMap, isEstimated = self.computeSuvMap(petImageFileList)<br>
File “C:/Users/DEX/AppData/Local/slicer.org/Slicer/slicer.org/Extensions-31757/PET-MUST-Segmenter/lib/Slicer-5.3/qt-scripted-modules/MUSTsegmenter.py”, line 1079, in computeSuvMap<br>
image, imageArray = self.readDicomSeriesFiles(imageFileList)<br>
File “C:/Users/DEX/AppData/Local/slicer.org/Slicer/slicer.org/Extensions-31757/PET-MUST-Segmenter/lib/Slicer-5.3/qt-scripted-modules/MUSTsegmenter.py”, line 1067, in readDicomSeriesFiles<br>
image = reader.Execute()<br>
File “C:\Users\DEX\AppData\Local\slicer.org\Slicer\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py”, line 6195, in Execute<br>
return _SimpleITK.ImageSeriesReader_Execute(self)<br>
RuntimeError: Exception thrown in SimpleITK ImageSeriesReader_Execute: D:\D\P\S-0-build\ITK\Modules\IO\GDCM\src\itkGDCMImageIO.cxx:462:<br>
ITK ERROR: GDCMImageIO(00000285738E9DB0): Cannot read requested file</p>
<p>how does this happen?  I even cannot find the path and file  “D:\D\P\S-0-build\ITK\Modules\IO\GDCM\src\itkGDCMImageIO.cxx”</p>
<p>I have tried to reinstall the software and modules, replace computers, it will be ok on my mate’s computer.</p>

---

## Post #2 by @ATAKAN_Isik (2023-05-29 16:54 UTC)

<p>try disable anti-virus if u have any. reinstall ITK using pip. Libararies and your pyhton requisites may not be match please check them.<br>
Good Luck</p>

---

## Post #3 by @Dex2046 (2023-06-01 06:45 UTC)

<p>thank you for your help.</p>
<p>I used the sample data downloaded from github, after trying for one week, finally, I found the sample date does not work on my computer <img src="https://emoji.discourse-cdn.com/twitter/skull.png?v=12" title=":skull:" class="emoji" alt=":skull:" loading="lazy" width="20" height="20">. I try some other data, the module works well and I do not want to tangle with  the sample data any more.</p>

---
