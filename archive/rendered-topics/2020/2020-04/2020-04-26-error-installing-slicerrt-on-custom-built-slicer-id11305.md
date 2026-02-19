---
topic_id: 11305
title: "Error Installing Slicerrt On Custom Built Slicer"
date: 2020-04-26
url: https://discourse.slicer.org/t/11305
---

# Error installing SlicerRT on custom built Slicer

**Topic ID**: 11305
**Date**: 2020-04-26
**URL**: https://discourse.slicer.org/t/error-installing-slicerrt-on-custom-built-slicer/11305

---

## Post #1 by @cacalsonari (2020-04-26 07:06 UTC)

<p>Hi!<br>
I builded 3DSlicer in my computer, and tried to install the SlicerRT extension on Extension Manager, but when I tried to open my DICOM images I had this issue:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/carla/MyProjects/Slicer/build/python-install/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/carla/.config/NA-MIC/Extensions-29011/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/PlmRegister.py", line 4, in &lt;module&gt;
    import RegistrationLib
ModuleNotFoundError: No module named 'RegistrationLib'
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
libitkhdf5_cpp.so.1: cannot open shared object file: No such file or directory
Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects
Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects
Traceback (most recent call last):
  File "/home/carla/MyProjects/Slicer/build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 671, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)
  File "/home/carla/.config/NA-MIC/Extensions-29011/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DicomRtImportExportPlugin.py", line 41, in examineForImport
    slicer.modules.dicomrtimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)
AttributeError: module 'modules' has no attribute 'dicomrtimportexport'
DICOM Plugin failed: module 'modules' has no attribute 'dicomrtimportexport'
Traceback (most recent call last):
  File "/home/carla/MyProjects/Slicer/build/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 671, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)
  File "/home/carla/.config/NA-MIC/Extensions-29011/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DicomSroImportExportPlugin.py", line 40, in examineForImport
    slicer.modules.dicomsroimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)
AttributeError: module 'modules' has no attribute 'dicomsroimportexport'
DICOM Plugin failed: module 'modules' has no attribute 'dicomsroimportexport'
</code></pre>
<p>Anyone had this issue too? Or anyone know how to fix it?<br>
I builded 3D Slicer 4.11.0-2020-04-25 on Ubuntu 18.04.4 LTS</p>
<p>Thanks.</p>

---

## Post #2 by @cpinter (2020-04-26 08:52 UTC)

<p>Extension manager downloads only work for factory built Slicer releases. If you build your own Slicer, you will need to build your own SlicerRT too.</p>

---

## Post #3 by @cacalsonari (2020-04-27 14:40 UTC)

<p>Thanks, it worked for me! However, I had to build another extension, as it is not available in the extension manager, and I need SlicerRT to be able to use my images. Would you know how I could put the two extensions together in a Slicer?</p>

---

## Post #4 by @cpinter (2020-04-27 15:25 UTC)

<p>If you ask this because you use SlicerRT with the SlicerWithSlicerRT executable, then you need to add the binary folders as additional module directories. You can find all the information in the documentation <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F</a></p>

---
