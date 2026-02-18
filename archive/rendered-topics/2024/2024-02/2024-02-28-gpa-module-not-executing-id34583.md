# GPA module not executing 

**Topic ID**: 34583
**Date**: 2024-02-28
**URL**: https://discourse.slicer.org/t/gpa-module-not-executing/34583

---

## Post #1 by @megvdb (2024-02-28 04:35 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 5.6.0<br>
Expected behavior: Trying to execute GPA+PCA<br>
Actual behavior: wont run!</p>
<p>Hi! I have used ALPACA to get landmarks for 9 species and I selected these files in the GPA module as mark.json files. I selected my output folder. However when I hit execute nothing is happening, any thoughts?</p>

---

## Post #2 by @muratmaga (2024-02-28 04:47 UTC)

<p>Please open the log file (CTRL/CMD + 0), and copy and paste the full log file.</p>

---

## Post #3 by @muratmaga (2024-02-28 22:59 UTC)

<p>Also you are using an older version of the SLicer. Please install the current stable (5.6.1) and retry.</p>

---

## Post #4 by @coco (2024-06-12 13:18 UTC)

<p>Hello,<br>
I encountered similar issues whilst using .mrk.json files but resolved the issues after changing format (saving new files as fcsv)<br>
Isn’t supposed to work with both file formats though ?<br>
Thanks and having a great time with slicermorph thus far !</p>

---

## Post #5 by @maryam_shakeri (2024-10-09 22:10 UTC)

<p>I am having this issue as well. I’m using a newer version of Slicer and have about 38 landmarks saved as .json files. When I click execute, nothing happens.<br>
I’m wondering - do I need to have two sets of landmarks (from the shapes I am comparing) from the get-go? Or can I set one as the ‘standard’ somehow and compare the rest of my samples to this one?</p>

---

## Post #6 by @muratmaga (2024-10-09 22:31 UTC)

<p>Can you provide the log file? You can get to it by hitting ctrl+0</p>
<aside class="quote no-group" data-username="maryam_shakeri" data-post="5" data-topic="34583">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maryam_shakeri/48/78189_2.png" class="avatar"> maryam_shakeri:</div>
<blockquote>
<p>do I need to have two sets of landmarks (from the shapes I am comparing) from the get-go?</p>
</blockquote>
</aside>
<p>No, you don’t need to set of landmark. You just need all the samples to have exactly the same number of landmarks as others. Please provide the log file, without that we can’t know why this is not working.</p>

---

## Post #7 by @maryam_shakeri (2024-10-10 00:42 UTC)

<p>Hi,<br>
Thanks for your reply! The log file is :</p>
<p>Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
Operating system …: Windows /  Professional / (Build 22621, Code Page 65001) - 64-bit<br>
Memory …: 32491 MB physical, 37355 MB virtual<br>
CPU …: GenuineIntel , 20 cores, 20 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
Internationalization …: disabled, language=<br>
Developer mode …: disabled<br>
Application path …: C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin<br>
libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
libpng warning: iCCP: known incorrect sRGB profile</p>
<p>ModuleType: CommandLineModule</p>
<p>Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.025000000372529,0.025000000372529,0.025000000372529 --size 140,194,339 --origin 5.90012,-1.55799,19.2427 --direction_matrix -0.99802077918573,0.0348755839426684,-0.0523279829524778,-0.0348755837543809,-0.999391244391407,-0.00091338841198455,-0.0523279845904687,0.000913388445507022,0.998629534873536 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeC.nrrd C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeE.nrrd</p>
<p>Resample Scalar/Vector/DWI Volume completed without errors</p>
<p>Switch to module:  “VolumeRendering”<br>
Switch to module:  “Segmentations”<br>
Switch to module:  “SegmentEditor”<br>
QLayout::addChildLayout: layout “” already has a parent<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
Switch to module:  “CropVolume”<br>
Found CommandLine Module, target is C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe</p>
<p>ModuleType: CommandLineModule</p>
<p>Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.025000000372529,0.025000000372529,0.025000000372529 --size 149,245,366 --origin 6.15869,-1.55289,18.5764 --direction_matrix -0.99802077918573,0.0348755839426684,-0.0523279829524778,-0.0348755837543809,-0.999391244391407,-0.00091338841198455,-0.0523279845904687,0.000913388445507022,0.998629534873536 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeE.nrrd C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeE.nrrd</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageThreshold (0000017A5C703740) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageReslice (0000017A56A43210) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageThreshold (0000017A5C703740) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageReslice (0000017A56A43210) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageThreshold (0000017A5C703740) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors (0000017A5CC24E90) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageReslice (0000017A58A04880) has 0 connections but is not optional.<br>
Switch to module:  “SegmentEditor”<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
Switch to module:  “CropVolume”<br>
Switch to module:  “Markups”<br>
Switch to module:  “CropVolume”<br>
Switch to module:  “Data”<br>
ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds<br>
Switch to module:  “VolumeRendering”<br>
Switch to module:  “CropVolume”<br>
Found CommandLine Module, target is C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe</p>
<p>Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.025000000372529,0.025000000372529,0.025000000372529 --size 150,263,388 --origin 6.20134,-1.07981,18.0242 --direction_matrix -0.99802077918573,0.0348755839426684,-0.0523279829524778,-0.0348755837543809,-0.999391244391407,-0.00091338841198455,-0.0523279845904687,0.000913388445507022,0.998629534873536 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeC.nrrd C:/Users/GrafLab/AppData/Local/Temp/Slicer/BAGAE_vtkMRMLScalarVolumeNodeF.nrrd</p>
<p>Resample Scalar/Vector/DWI Volume completed without errors</p>
<p>Switch to module:  “VolumeRendering”<br>
Switch to module:  “SegmentEditor”<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
Switch to module:  “Data”<br>
Switch to module:  “SegmentEditor”<br>
Switch to module:  “Segmentations”<br>
“Model” Reader has successfully read the file<br>
Switch to module:  “Markups”<br>
Switch to module:  “Data”<br>
Switch to module:  “Markups”<br>
Switch to module:  “GPA”<br>
Collecting pandas<br>
Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl.metadata (19 kB)<br>
Requirement already satisfied: numpy&gt;=1.22.4 in c:\users\graflab\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from pandas) (1.26.1)<br>
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\graflab\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from pandas) (2.8.2)<br>
Collecting pytz&gt;=2020.1 (from pandas)<br>
Downloading pytz-2024.2-py2.py3-none-any.whl.metadata (22 kB)<br>
Collecting tzdata&gt;=2022.7 (from pandas)<br>
Downloading tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)<br>
Requirement already satisfied: six&gt;=1.5 in c:\users\graflab\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.16.0)<br>
Downloading pandas-2.2.3-cp39-cp39-win_amd64.whl (11.6 MB)<br>
---------------------------------------- 11.6/11.6 MB 81.8 MB/s eta 0:00:00<br>
Downloading pytz-2024.2-py2.py3-none-any.whl (508 kB)<br>
---------------------------------------- 508.0/508.0 kB ? eta 0:00:00<br>
Downloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)<br>
--------------------------------------- 346.6/346.6 kB 22.4 MB/s eta 0:00:00<br>
Installing collected packages: pytz, tzdata, pandas<br>
Successfully installed pandas-2.2.3 pytz-2024.2 tzdata-2024.2<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1022, in onSelectLandmarkFiles<br>
self.LM_dir_name = os.path.dirname(self.inputFilePaths[0])<br>
IndexError: tuple index out of range<br>
Switch to module:  “Markups”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: “”<br>
Switch to module:  “GPA”<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Result import failed: Missing file<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Result import failed: Missing file<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Excluded landmarks:  [‘f.mark’]<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1195, in onLoad<br>
self.LMExclusionList=[int(x) for x in self.LMExclusionList]<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1195, in <br>
self.LMExclusionList=[int(x) for x in self.LMExclusionList]<br>
ValueError: invalid literal for int() with base 10: ‘f.mark’<br>
Excluded landmarks:  [‘f.mark’]<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1195, in onLoad<br>
self.LMExclusionList=[int(x) for x in self.LMExclusionList]<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1195, in <br>
self.LMExclusionList=[int(x) for x in self.LMExclusionList]<br>
ValueError: invalid literal for int() with base 10: ‘f.mark’<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs<br>
Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 240, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 630, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs</p>

---

## Post #8 by @maryam_shakeri (2024-10-10 00:45 UTC)

<p>I see - so I must enter both landmark file sets at once? That may be the issue as I currently have been trying only one sample’s landmarks. Apologies for the naive question; I’m very new to slicer!</p>

---

## Post #9 by @muratmaga (2024-10-10 01:20 UTC)

<aside class="quote no-group" data-username="maryam_shakeri" data-post="7" data-topic="34583">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maryam_shakeri/48/78189_2.png" class="avatar"> maryam_shakeri:</div>
<blockquote>
<p>Loaded 39 subjects with 1 landmark points.<br>
C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1209, in onLoad<br>
self.LM.doGpa(self.BoasOption)<br>
File “C:/Users/GrafLab/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 229, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\SlicerMorph\lib\Slicer-5.6\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\GrafLab\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)</p>
</blockquote>
</aside>
<p>This is the issue. There is only 1 landmark point in 39 files. The covariance matrix is singular and everything breaks apart. You can’t do a shape analysis with a single landmark.</p>
<p>If this is not what you are trying to do (i.e., work with a single landmark), then please share your dataset. Otherwise perhaps review our GPA module tutorials to understand how it works: <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a>.</p>

---

## Post #10 by @maryam_shakeri (2024-10-10 17:05 UTC)

<p>I was under the impression that each point placed (ie each .json file) was a landmark. How can I place landmarks if not in the markups module?</p>
<p>Thanks!</p>

---

## Post #11 by @muratmaga (2024-10-10 19:07 UTC)

<p>A pointList markup type can store many control points (aka landmarks). Please read our tutorials. Including the ones for Markups from the link I shared above.</p>

---
