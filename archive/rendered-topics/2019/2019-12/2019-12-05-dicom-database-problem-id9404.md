# DICOM database problem

**Topic ID**: 9404
**Date**: 2019-12-05
**URL**: https://discourse.slicer.org/t/dicom-database-problem/9404

---

## Post #1 by @opetne (2019-12-05 21:14 UTC)

<p>Slicer 4.11.0 version<br>
T<br>
If I want to see series in the DICOM module, I see the patient name but there is nothing listed in the advanced part of it, I can’t see what kind of series does a patient have. If I want to load any series sometimes nothing happens after I clicked on it. I have to click on a series many, many times till it opens.</p>

---

## Post #2 by @lassoan (2019-12-05 22:01 UTC)

<p>If you use latest preview release and create the database from scratch (choose an empty folder as database location in “DICOM database settings”) then it should all work well. If not, then let us know.</p>
<p>It is normal that clicking on a series has no effect. You can either double-click on a patient/study/series to load it or click “Load” button to load the selected items.</p>

---

## Post #3 by @opetne (2019-12-05 22:22 UTC)

<p>Thank you Andras but nothing happens since I can’t click on creating new database option since it is not active…</p>

---

## Post #4 by @opetne (2019-12-05 22:25 UTC)

<p>This is what I’ve found in the python module:</p>
<details>
<summary>
Logs</summary>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/EasyClip/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py”, line 41<br>
print “-------Easy Clip Widget Setup---------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Easy Clip Widget Setup---------")?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerProstateAblation/lib/Slicer-4.11/qt-scripted-modules/ProstateAblation.py”, line 259<br>
print slicer.dicomDatabase<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(slicer.dicomDatabase)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ResectionPlanner/lib/Slicer-4.11/qt-scripted-modules/ResectionVolume.py”, line 229<br>
except Exception, e:<br>
^<br>
SyntaxError: invalid syntax<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ZFrameRegistration/lib/Slicer-4.11/qt-scripted-modules/ZFrameRegistrationWithROI.py”, line 8, in <br>
from SlicerDevelopmentToolboxUtils.mixins import ModuleLogicMixin, ModuleWidgetMixin<br>
File “C:\Users\petnehazyors\AppData\Roaming\NA-MIC\Extensions-28659\SlicerDevelopmentToolbox\lib\Slicer-4.11\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py”, line 6, in <br>
from packaging import version<br>
ModuleNotFoundError: No module named ‘packaging’<br>
TypeError: module.<strong>init</strong>() argument 1 must be str, not qSlicerScriptedLoadableModule</p>
</details>

---

## Post #5 by @lassoan (2019-12-05 22:36 UTC)

<aside class="quote no-group" data-username="opetne" data-post="3" data-topic="9404">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/71e660/48.png" class="avatar"> opetne:</div>
<blockquote>
<p>can’t click on creating new database option since it is not active…</p>
</blockquote>
</aside>
<p>Could you please post a screenshot?</p>

---

## Post #6 by @jamesobutler (2019-12-06 00:44 UTC)

<p>If you uninstall the SlicerProstateAblation extension which is having problems and restart Slicer, can you then create a new Slicer database?</p>

---

## Post #7 by @opetne (2019-12-06 08:41 UTC)

<p>Dear Andras and James,</p>
<p>I uninstalled a lot of the extensions, I kept only what I think could be usefull for segmentation.<br>
After a restart here are the erros logs:</p>
<details>
<summary>
Logs</summary>
<p>Session start time …: 2019-12-06 09:38:40<br>
Slicer version …: 4.11.0-2019-12-02 (revision 28659) win-amd64 - installed release<br>
Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
Memory …: 40840 MB physical, 46728 MB virtual<br>
CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Application path …: C:/Users/petnehazyors/AppData/Local/NA-MIC/Slicer 4.11.0-2019-12-02/bin<br>
Additional module paths …: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/Slicer-AirwaySegmentation/lib/Slicer-4.11/cli-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/Slicer-AirwaySegmentation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ModelCropper/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py”, line 72<br>
print “-------Angle Planes Widget Setup-------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Angle Planes Widget Setup-------”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py”  as module “AnglePlanes” !<br>
Fail to instantiate module  “AnglePlanes”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py”, line 42<br>
print “-------Easy Clip Widget Setup---------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Easy Clip Widget Setup---------”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py”  as module “EasyClip” !<br>
Fail to instantiate module  “EasyClip”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/MeshStatistics.py”, line 35<br>
print “-------Mesh Statistic Widget Setup-------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Mesh Statistic Widget Setup-------”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/MeshStatistics.py”  as module “MeshStatistics” !<br>
Fail to instantiate module  “MeshStatistics”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/PickAndPaint.py”, line 27<br>
print “-------Pick And Paint Widget Setup--------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Pick And Paint Widget Setup--------”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/PickAndPaint.py”  as module “PickAndPaint” !<br>
Fail to instantiate module  “PickAndPaint”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/Q3DC.py”, line 40<br>
print “-------Q3DC Widget Setup------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Q3DC Widget Setup------”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/Q3DC.py”  as module “Q3DC” !<br>
Fail to instantiate module  “Q3DC”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifier.py”, line 89<br>
print “----- Shape Quantifier widget setup -----”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“----- Shape Quantifier widget setup -----”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifier.py”  as module “ShapeQuantifier” !<br>
Fail to instantiate module  “ShapeQuantifier”<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifierCore.py”, line 43<br>
print “UpdateThreeDView”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“UpdateThreeDView”)?<br>
loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifierCore.py”  as module “ShapeQuantifierCore” !<br>
Fail to instantiate module  “ShapeQuantifierCore”<br>
Error(s):<br>
CLI executable: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
Fail to instantiate module  “vtkvmtk”<br>
The following modules failed to be instantiated:<br>
EasyClip<br>
MeshStatistics<br>
PickAndPaint<br>
vtkvmtk<br>
ShapeQuantifierCore<br>
Q3DC<br>
AnglePlanes<br>
ShapeQuantifier<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module:  “Welcome”<br>
Loaded volume from file: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.</p>
<p>And here is everything I’ve found in the python interactor:</p>
<p>Python 3.6.7 (default, Dec  3 2019, 23:21:59) [MSC v.1900 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py”, line 72<br>
print “-------Angle Planes Widget Setup-------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Angle Planes Widget Setup-------”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py”, line 42<br>
print “-------Easy Clip Widget Setup---------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Easy Clip Widget Setup---------”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/MeshStatistics.py”, line 35<br>
print “-------Mesh Statistic Widget Setup-------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Mesh Statistic Widget Setup-------”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/PickAndPaint.py”, line 27<br>
print “-------Pick And Paint Widget Setup--------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Pick And Paint Widget Setup--------”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/Q3DC.py”, line 40<br>
print “-------Q3DC Widget Setup------”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“-------Q3DC Widget Setup------”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifier.py”, line 89<br>
print “----- Shape Quantifier widget setup -----”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“----- Shape Quantifier widget setup -----”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifierCore.py”, line 43<br>
print “UpdateThreeDView”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“UpdateThreeDView”)?</p>
</details>

---

## Post #8 by @cpinter (2019-12-06 10:56 UTC)

<p>Based on the error messages it seems that the extension ShapeQuantifier is not compatible with the current Slicer (it would need to be updated to support Python 3).</p>
<p>Not sure what it has to do with the DICOM browser though. We’d need to see exactly what happens there. Can you post a screenshot about it when you cannot select a new DICOM database?</p>

---

## Post #9 by @opetne (2019-12-06 20:28 UTC)

<p>Dear Csaba,</p>
<p>After I uninstalled a lot of extensions I can’t reconstruct the database problem.</p>
<p>Ors</p>
<p>Csaba Pinter via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> ezt írta (időpont: 2019. dec. 6., Pén 12:06):</p>

---

## Post #10 by @lassoan (2019-12-07 00:23 UTC)

<p>Do you mean that after uninstalling the extensions that caused the problems during startup, everything works well?</p>

---

## Post #11 by @cpinter (2019-12-07 15:20 UTC)

<p>Unfortunately there are still some extensions that have not been updated to work with the current Slicer. For example the ShapeQuantifier extension (<a href="https://github.com/jbvimort/ShapeQuantifierExtension">GitHub</a>) has not changed in four years.</p>
<p>The good news is that Python3 migration is quite easy and usually it’s about 3-4 types of typical problems that can be fixed mechanically.</p>

---

## Post #12 by @opetne (2019-12-07 15:46 UTC)

<p>Dear Andras,</p>
<p>yes, it seems now working ok.</p>
<p>Ors</p>
<p>Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> ezt írta (időpont: 2019. dec. 7., Szo, 1:33):</p>

---

## Post #13 by @opetne (2019-12-08 11:35 UTC)

<p>Dear Andras,</p>
<p>I might be a bit too fast by saying that the problem is solved. This is the screen I see since 2 hours. Somehow the database still causes problems and there is not smooth load of the series.</p>
<p>If I have a series loaded I can’t see the details, because if I click on it I don’t know if anything happens, no window pops up, no changes can be seen, the software doesn’t says NOt responding just nothing happens. Or maybe some minutes later crashes the whole software.</p>
<p>Ors</p>
<p>Ors Petnehazy <a href="mailto:ors.petne@gmail.com">ors.petne@gmail.com</a> ezt írta (időpont: 2019. dec. 7., Szo, 16:46):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e31bce6cacdb8d600f88ec3a3929c990eabf339d.png" data-download-href="/uploads/short-url/wp5XyAXLjQ9e3UTw5XNV70XAE0J.png?dl=1" title="dicom database.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31bce6cacdb8d600f88ec3a3929c990eabf339d_2_690x370.png" alt="dicom database.PNG" data-base62-sha1="wp5XyAXLjQ9e3UTw5XNV70XAE0J" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31bce6cacdb8d600f88ec3a3929c990eabf339d_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31bce6cacdb8d600f88ec3a3929c990eabf339d_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31bce6cacdb8d600f88ec3a3929c990eabf339d_2_1380x740.png 2x" data-dominant-color="D8E7F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicom database.PNG</span><span class="informations">1916×1029 78.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @lassoan (2019-12-08 14:37 UTC)

<p>It seems that the path you are importing data from is extremely long. Do you actually store data in so deep folder structure with so long names? Is it possible that you chose to import files from the DICOM database folder (maybe this can create an infinite loop)?</p>
<p>Are there any errors in the log?<br>
Do you have multiple Slicer instances runnning at the same time?<br>
Do you have the imported files on your local computer or loading them from a network drive?</p>

---

## Post #15 by @opetne (2019-12-09 13:29 UTC)

<p>Dear Andras,</p>
<p>The files are stored on my computer, locally. I think the reason could be the someone (who installed it) named it “Ez a számítógép”… what was contained in the name of the path causing the problem</p>
<p>Ors</p>
<p>Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> ezt írta (időpont: 2019. dec. 8., V, 15:47):</p>

---

## Post #16 by @opetne (2019-12-09 13:37 UTC)

<p>I changed the name to my computer, not using special characters but still no changes in loading the DICOM files.</p>
<p>Ors Petnehazy <a href="mailto:ors.petne@gmail.com">ors.petne@gmail.com</a> ezt írta (időpont: 2019. dec. 9., H, 14:29):</p>

---

## Post #17 by @opetne (2019-12-09 13:39 UTC)

<p>Here is the complete error log:</p>
<details>
<summary>
Logs</summary>
<p>Session start time …: 2019-12-09 14:25:10</p>
<p>Slicer version …: 4.11.0-2019-12-02 (revision 28659) win-amd64 - installed release</p>
<p>Operating system …: Windows / Professional / (Build 9200) - 64-bit</p>
<p>Memory …: 40840 MB physical, 46728 MB virtual</p>
<p>CPU …: GenuineIntel , 8 cores, 8 logical processors</p>
<p>VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>Developer mode enabled …: no</p>
<p>Prefer executable CLI …: yes</p>
<p>Application path …: C:/Users/petnehazyors/AppData/Local/NA-MIC/Slicer 4.11.0-2019-12-02/bin</p>
<p>Additional module paths …: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/Slicer-AirwaySegmentation/lib/Slicer-4.11/cli-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/Slicer-AirwaySegmentation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ModelCropper/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/PETDICOMExtension/lib/Slicer-4.11/cli-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py”, line 72</p>
<p>print “-------Angle Planes Widget Setup-------”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Angle Planes Widget Setup-------")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/AnglePlanes.py” as module “AnglePlanes” !</p>
<p>Fail to instantiate module “AnglePlanes”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 678, in exec_module</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 14, in </p>
<p>from SlicerDevelopmentToolboxUtils.mixins import ModuleLogicMixin</p>
<p>File “C:\Users\petnehazyors\AppData\Roaming\NA-MIC\Extensions-28659\SlicerDevelopmentToolbox\lib\Slicer-4.11\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py”, line 6, in </p>
<p>from packaging import version</p>
<p>ModuleNotFoundError: No module named ‘packaging’</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py” as module “DICOMSegmentationPlugin” !</p>
<p>Fail to instantiate module “DICOMSegmentationPlugin”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 678, in exec_module</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMTID1500Plugin.py”, line 12, in </p>
<p>from SlicerDevelopmentToolboxUtils.mixins import ModuleLogicMixin</p>
<p>File “C:\Users\petnehazyors\AppData\Roaming\NA-MIC\Extensions-28659\SlicerDevelopmentToolbox\lib\Slicer-4.11\qt-scripted-modules\SlicerDevelopmentToolboxUtils\mixins.py”, line 6, in </p>
<p>from packaging import version</p>
<p>ModuleNotFoundError: No module named ‘packaging’</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMTID1500Plugin.py” as module “DICOMTID1500Plugin” !</p>
<p>Fail to instantiate module “DICOMTID1500Plugin”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py”, line 42</p>
<p>print “-------Easy Clip Widget Setup---------”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Easy Clip Widget Setup---------")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/EasyClip.py” as module “EasyClip” !</p>
<p>Fail to instantiate module “EasyClip”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/MeshStatistics.py”, line 35</p>
<p>print “-------Mesh Statistic Widget Setup-------”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Mesh Statistic Widget Setup-------")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/MeshStatistics.py” as module “MeshStatistics” !</p>
<p>Fail to instantiate module “MeshStatistics”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/PickAndPaint.py”, line 27</p>
<p>print “-------Pick And Paint Widget Setup--------”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Pick And Paint Widget Setup--------")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/PickAndPaint.py” as module “PickAndPaint” !</p>
<p>Fail to instantiate module “PickAndPaint”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/Q3DC.py”, line 40</p>
<p>print “-------Q3DC Widget Setup------”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("-------Q3DC Widget Setup------")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/Q3DC.py” as module “Q3DC” !</p>
<p>Fail to instantiate module “Q3DC”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 678, in exec_module</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/QuantitativeReporting.py”, line 12, in </p>
<p>from DICOMSegmentationPlugin import DICOMSegmentationExporter</p>
<p>ImportError: cannot import name ‘DICOMSegmentationExporter’</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/QuantitativeReporting.py” as module “QuantitativeReporting” !</p>
<p>Fail to instantiate module “QuantitativeReporting”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifier.py”, line 89</p>
<p>print “----- Shape Quantifier widget setup -----”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print("----- Shape Quantifier widget setup -----")?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifier.py” as module “ShapeQuantifier” !</p>
<p>Fail to instantiate module “ShapeQuantifier”</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Users\petnehazyors\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-02\lib\Python\Lib\imp.py”, line 170, in load_source</p>
<p>module = _exec(spec, sys.modules[name])</p>
<p>File “”, line 618, in _exec</p>
<p>File “”, line 674, in exec_module</p>
<p>File “”, line 781, in get_code</p>
<p>File “”, line 741, in source_to_code</p>
<p>File “”, line 219, in _call_with_frames_removed</p>
<p>File “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifierCore.py”, line 43</p>
<p>print “UpdateThreeDView”</p>
<p>^</p>
<p>SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“UpdateThreeDView”)?</p>
<p>loadSourceAsModule - Failed to load file “C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/ShapeQuantifier/lib/Slicer-4.11/qt-scripted-modules/ShapeQuantifierCore.py” as module “ShapeQuantifierCore” !</p>
<p>Fail to instantiate module “ShapeQuantifierCore”</p>
<p>Error(s):</p>
<p>CLI executable: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py</p>
<p>The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.</p>
<p>Fail to instantiate module “vtkvmtk”</p>
<p>The following modules failed to be instantiated:</p>
<p>vtkvmtk</p>
<p>AnglePlanes</p>
<p>EasyClip</p>
<p>Q3DC</p>
<p>ShapeQuantifierCore</p>
<p>MeshStatistics</p>
<p>ShapeQuantifier</p>
<p>PickAndPaint</p>
<p>DICOMSegmentationPlugin</p>
<p>QuantitativeReporting</p>
<p>DICOMTID1500Plugin</p>
<p>Scripted subject hierarchy plugin registered: Annotations</p>
<p>When loading module “QuantitativeReportingTests” , the dependency “QuantitativeReporting” failed to be loaded.</p>
<p>Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>Switch to module: “Welcome”</p>
<p>Loaded volume from file: C:/Users/petnehazyors/AppData/Roaming/NA-MIC/Extensions-28659/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.</p>
<p>Switch to module: “DICOM”</p>
<p>DICOMParametricMapPluginClass : Caching files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>DICOMParametricMapPluginClass : Using cached files</p>
<p>MultiVolumeImportPlugin::examine</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
<p>MultiVolumeImportPlugin:examineMultiseries</p>
<p>DICOMMultiVolumePlugin found 0 multivolumes!</p>
</details>

---

## Post #18 by @lassoan (2019-12-09 18:10 UTC)

<p>We did remote debugging on the computer and it turns out that it was a display issue (the application did not react to most button clicks when the DICOM browser was displayed).</p>
<p><strong>Updating the video card driver solved the problem</strong> (it was a laptop with Intel+NVidia graphics card and the video card driver was several years old).</p>

---

## Post #19 by @opetne (2019-12-11 09:00 UTC)

<p>Indeed as Andras said, I have a HP Zbook 15 with an Intel HD Graohics 530 and and NVIDIA Quadro M1000M graphic card with 2 GB memory. I have a HP Assistant software on my computer what notified me several times to refresh the driver for the video card. I made it many times but it was only a “fake” refreshment since the files, available form the official sources didn’t worked. Andras found the way how we can get files what are working for refreshing the driver for the integrated graphic card. After refreshing the NVidia driver the problem disappeared.</p>
<p>What we learned form it, check it twice or more if the official refreshing procedures realy works:)</p>

---
