# 2018-10-15 Windows nightly build "unable to import VTK"

**Topic ID**: 4403
**Date**: 2018-10-15
**URL**: https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403

---

## Post #1 by @jamesobutler (2018-10-15 17:12 UTC)

<p>Today’s 2018-10-15 Windows nightly build shows a bunch of errors after launch because it is unable to import VTK in python. This hasn’t been an issue for recent nightly builds so I assume it is something to do with a recent VTK commit as the Slicer release is getting prepped. The Windows build didn’t appear to show build errors indicating that there would be a problem with this nightly. Can anyone replicate this?</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - NameError: name 'getSlicerRCFileName' is not defined
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AddManyMarkupsFiducialTest.py", line 4, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -     import vtk, qt, ctk, slicer
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - ImportError: No module named vtk
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AddManyMarkupsFiducialTest.py"  as module "AddManyMarkupsFiducialTest" !
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - Fail to instantiate module  "AddManyMarkupsFiducialTest"
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AddStorableDataAfterSceneViewTest.py", line 3, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -     import vtk, qt, ctk, slicer
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - ImportError: No module named vtk
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AddStorableDataAfterSceneViewTest.py"  as module "AddStorableDataAfterSceneViewTest" !
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - Fail to instantiate module  "AddStorableDataAfterSceneViewTest"
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -   File "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AtlasTests.py", line 3, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) -     import vtk, qt, ctk, slicer
[CRITICAL][Stream] 15.10.2018 13:03:33 [] (unknown:0) - ImportError: No module named vtk
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Program Files/Slicer 4.9.0-2018-10-15/bin/../lib/Slicer-4.9/qt-scripted-modules/AtlasTests.py"  as module "AtlasTests" !
[CRITICAL][Qt] 15.10.2018 13:03:33 [] (unknown:0) - Fail to instantiate module  "AtlasTests"
...[Other messages hidden]
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -   File "C:\Program Files\Slicer 4.9.0-2018-10-15\bin\Python\slicer\util.py", line 100, in importVTKClassesFromDirectory
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -     from vtk import vtkObjectBase
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) - ImportError: No module named vtk
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -   File "C:\Program Files\Slicer 4.9.0-2018-10-15\bin\Python\slicer\util.py", line 100, in importVTKClassesFromDirectory
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) -     from vtk import vtkObjectBase
[CRITICAL][Stream] 15.10.2018 13:03:36 [] (unknown:0) - ImportError: No module named vtk
[DEBUG][Qt] 15.10.2018 13:03:37 [] (unknown:0) - Switch to module:  "Welcome"
[CRITICAL][Stream] 15.10.2018 13:03:38 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.10.2018 13:03:38 [] (unknown:0) -   File "&lt;string&gt;", line 1, in &lt;module&gt;
[CRITICAL][Stream] 15.10.2018 13:03:38 [] (unknown:0) - NameError: name 'loadSlicerRCFile' is not defined
</code></pre>

---

## Post #2 by @jcfr (2018-10-16 08:16 UTC)

<p>Thanks for the report <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I confirm this is an issue. It is now tracked by  <a href="https://issues.slicer.org/view.php?id=4636">https://issues.slicer.org/view.php?id=4636</a></p>

---

## Post #3 by @jcfr (2018-10-16 14:01 UTC)

<p>This has been fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27491">r27491</a>, a regression due to the change of VTK version from 9.0 to 8.2 …</p>
<p>I will delete the Windows nightly CDash entry and re-trigger a “nightly” build with that change, that way we will have a working windows package.</p>

---
