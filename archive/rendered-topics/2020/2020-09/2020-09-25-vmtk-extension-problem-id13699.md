# VMTK Extension Problem

**Topic ID**: 13699
**Date**: 2020-09-25
**URL**: https://discourse.slicer.org/t/vmtk-extension-problem/13699

---

## Post #1 by @hannah_e (2020-09-25 15:35 UTC)

<p>Hello!</p>
<p>I’m trying to use the VMTK extension in 3D slicer but can’t seem to load the qt-loadable-modules. As far as I can tell the qt-scriptable modules load fine, at least I can see them in the modules in Slicer.<br>
–I am using a Windows 10 machine and have the 9/22/2020 nightly version of Slicer (though I’ve tried many other builds, including the stable release, and don’t see a difference). I’ve also tried the nightly release on another windows 10 machine and get the same errors installing VMTK extension.<br>
–My error log shows:<br>
Error(s):<br>
CLI executable: C:/Users/E/AppData/Roaming/NA-MIC/Extensions-29387/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
Fail to instantiate module  “vtkvmtk”<br>
The following modules failed to be instantiated:<br>
vtkvmtk<br>
–After reading up, I’ve tried removing the “shebang” line and then I get a relative import error. After removing all relative import references in the vtkvmtk.py script, the imports in vtkvmtk.py seem to work (I don’t see errors in the python console due to imports), but I get a new error below in the python console:<br>
RuntimeError: qSlicerScriptedLoadableModule::setPythonSource - Failed to load scripted loadable module: class vtkvmtk was not found in file C:/Users/E/AppData/Roaming/NA-MIC/Extensions-29387/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py</p>
<p>With this as well in the error log:<br>
Fail to instantiate module  “vtkvmtk”<br>
The following modules failed to be instantiated:<br>
vtkvmtk</p>
<p>I’m not sure what I can try next and I’m worried I’m missing some step early on. Any help you could give would be very appreciated!</p>

---

## Post #2 by @lassoan (2020-09-25 15:39 UTC)

<p>You can safely ignore this error message. We’ll fix it probably within a couple of weeks (you can monitor the progress here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22">https://github.com/vmtk/SlicerExtension-VMTK/issues/22</a>).</p>

---
