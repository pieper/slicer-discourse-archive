---
topic_id: 4590
title: "Slicer 4 10 0 Starts Up No More After Closing Unexpectedly"
date: 2018-10-30
url: https://discourse.slicer.org/t/4590
---

# Slicer 4.10.0 starts up no more after closing unexpectedly

**Topic ID**: 4590
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/slicer-4-10-0-starts-up-no-more-after-closing-unexpectedly/4590

---

## Post #1 by @stephan (2018-10-30 15:08 UTC)

<p>Slicer 4.10.0<br>
Windows 7, 64 bit</p>
<p>Hi everybody,</p>
<p>this morning I run into the same issue twice, but I still have to figure out how to reproduce it exactly. As of now, I just wanted to ask if anybody has experienced something similar:</p>
<p>When saving a rather large scene in Slicer 4.10.0, Slicer closes unexpectedly while (or rather immediately after) saving the scene. Of note, no log file items are written for this saving, but the scene was saved correctly (and could be opened correctly later).<br>
After the unexpected shutdown (the window simply disappears), there is no way to restart Slicer 4.10.0. (an old installation of 4.8.0 on my machine continues to work).<br>
When trying to start Slicer 4.10.0, the cursor becomes the “working” icon for a few moments, but nothing happens: No splash screen, no new log file in the slicer log folder.<br>
Restarting Windows does not solve the issue. I had to re-install Slicer 4.10.0, which worked fine then. I was able to continue working on the scene and even save it a couple time, but roughly 1 hour later the same happened again (Slicer closes during saving, can’t be started up again, had to be re-installed).</p>
<p>I will now try to investigate further if I can reproduce this issue more reliably and will get back if I can. The fact that no log files are produced during the startup attempt makes things a little hard to debug, I suppose.<br>
For the time being, if anyone else has experienced this weird behavior, please add to this post.</p>
<p>Stephan</p>

---

## Post #2 by @stephan (2018-10-30 15:40 UTC)

<p>It happened again when trying to save.<br>
Here is the log file of the session:</p>
<pre><code>[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Session start time .......: 2018-10-30 09:53:51
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Slicer version ...........: 4.10.0 (revision 27501) win-amd64 - installed release
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Memory ...................: 8072 MB physical, 16143 MB virtual
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 30.10.2018 09:53:51 [] (unknown:0) - Additional module paths ..: C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/CMFreg/lib/Slicer-4.10/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/CMFreg/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/PETDICOMExtension/lib/Slicer-4.10/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/PETDICOMExtension/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/DCMQI/lib/Slicer-4.10/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/QuantitativeReporting/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/SlicerDevelopmentToolbox/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/Sequences/lib/Slicer-4.10/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/Sequences/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/SlicerElastix/lib/Slicer-4.10/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/SlicerRT/lib/Slicer-4.10/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-27501/SlicerRT/lib/Slicer-4.10/qt-scripted-modules
[DEBUG][Python] 30.10.2018 09:54:05 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)
[DEBUG][Python] 30.10.2018 09:54:06 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)
[DEBUG][Python] 30.10.2018 09:54:11 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 30.10.2018 09:54:17 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 30.10.2018 09:54:17 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 30.10.2018 09:54:18 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 30.10.2018 09:54:45 [] (unknown:0) - Unpacking bundle  "H:/[...]/P860-scar and planning.mrb"  to  "C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589"
[WARNING][VTK] 30.10.2018 09:54:50 [vtkMRMLModelDisplayNode (000000004EA79410)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:
[WARNING][VTK] 30.10.2018 09:54:50 [vtkMRMLModelDisplayNode (000000004EA79680)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:
[WARNING][VTK] 30.10.2018 09:54:50 [vtkMRMLModelDisplayNode (000000004EA798F0)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:
[WARNING][VTK] 30.10.2018 09:54:50 [vtkMRMLModelDisplayNode (000000004EA79B60)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:
[INFO][VTK] 30.10.2018 09:54:50 [vtkMRMLVolumeArchetypeStorageNode (0000000052239360)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589/P860-scar and planning/Data/11 3D MDE sax 3mm asset.nrrd. Dimensions: 256x256x72. Number of components: 1. Pixel type: short.
[INFO][VTK] 30.10.2018 09:54:50 [vtkMRMLVolumeArchetypeStorageNode (00000000522391C0)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589/P860-scar and planning/Data/15 3d fiesta cai.nrrd. Dimensions: 512x512x72. Number of components: 1. Pixel type: short.
[INFO][VTK] 30.10.2018 09:54:51 [vtkMRMLVolumeArchetypeStorageNode (0000000055EC3AE0)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589/P860-scar and planning/Data/623 RTDOSE Mr. Spock Dose 4D Accumulated 4DGPUCalc Accumulate 70.nrrd. Dimensions: 473x476x192. Number of components: 1. Pixel type: float.
[WARNING][VTK] 30.10.2018 09:55:56 [vtkPolyData (0000000066C40090)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:55:56 [vtkPolyData (0000000066C40090)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:21 [vtkPolyData (0000000066E5FB80)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:21 [vtkPolyData (0000000066E5FB80)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:21 [vtkPolyData (0000000066E5FA00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:21 [vtkPolyData (0000000066E5FA00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:21 [vtkPolyData (0000000066E5FD00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:22 [vtkPolyData (0000000066E5FD00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:22 [vtkPolyData (0000000066E5FD00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 09:56:22 [vtkPolyData (0000000066E5FD00)] (D:\D\S\Slicer-4100-build\VTK\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[INFO][VTK] 30.10.2018 09:56:25 [vtkMRMLVolumeArchetypeStorageNode (0000000055EC3C80)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589/P860-scar and planning/Data/11 With contrast 1.0 I26f 3 0 - 95  TRIGGER_DELAY 70%.nrrd. Dimensions: 512x512x192. Number of components: 1. Pixel type: short.
[INFO][VTK] 30.10.2018 09:56:28 [vtkMRMLVolumeArchetypeStorageNode (0000000055EC3940)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589/P860-scar and planning/Data/602 Private^Packer_Heart_Spiral (Adult) 0.nrrd. Dimensions: 512x512x192. Number of components: 1. Pixel type: short.
[INFO][Stream] 30.10.2018 09:56:28 [] (unknown:0) - CreateVTKTransformFromITK - SetVTKLinearTransformFromITK conversionSuccess:1
[DEBUG][Qt] 30.10.2018 09:56:28 [] (unknown:0) - Loaded bundle from  "C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_09+54+45.589"
[DEBUG][Qt] 30.10.2018 09:56:28 [] (unknown:0) - Reset scene to point to the MRB directory  H:/[...]/P860-scar and planning.mrml
[DEBUG][Qt] 30.10.2018 09:56:28 [] (unknown:0) - "MRB Slicer Data Bundle" Reader has successfully read the file "H:/[...]/P860-scar and planning.mrb" "[103.20s]"
</code></pre>
<p>At 10:09 I started saving the scene, which it did successfully (a .mrb file was created which has the same size as the original), but immediately after that Slicer closed. As you see, the entire save process has not been logged. I tried to start slicer.exe several times to no avail. I my desperation, I also gave the “Recommended Windows compatibility settings” a try, but that did not help either, of course (well, there were no compatibility issues before, so I did not expect this to do much).<br>
As before, no new log file is started during these startup attempts, and the one I pasted above is not appended, either.</p>
<p>The scene in question contains an MRI, two CTs and radiotherapy dose data as well as a radiotherapy structure set. I use SlicerRT for these.<br>
I am happy to share the scene via private message if one of the developers would like to give it a try.</p>
<p>I briefly though that there might be some interference with other software, because one of the sudden crashes coincided with me opening R Studio, but since I have re-started my computer in the meantime and only had Slicer open this time, this can probably be ruled out.</p>
<p>I also loaded the scene in the old 4.8.0 installation was able to successfully save it from there without crashing. Log file: [was over the character limit for a single post, follows below]</p>
<p>Gonna re-install Slicer 4.10.0 now again.</p>
<p>Please let me know if there is anything specific you would like me try out.<br>
Thanks</p>
<p>Stephan</p>

---

## Post #3 by @stephan (2018-10-30 15:41 UTC)

<p>The log file for the succesful load and save in Slicer 4.8. (part 1/2):</p>
<pre><code>[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Session start time .......: 2018-10-30 10:30:01
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Slicer version ...........: 4.8.0 (revision 26489) win-amd64 - installed
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Operating system .........: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Memory ...................: 8072 MB physical, 16143 MB virtual
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 16 logical processors
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 30.10.2018 10:30:01 [] (unknown:0) - Additional module paths ..: C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/SlicerRT/lib/Slicer-4.8/cli-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/SlicerRT/lib/Slicer-4.8/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/SlicerRT/lib/Slicer-4.8/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/Sequences/lib/Slicer-4.8/qt-loadable-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/Sequences/lib/Slicer-4.8/qt-scripted-modules, C:/Users/M171189/AppData/Roaming/NA-MIC/Extensions-26489/SlicerOpenCV/lib/Slicer-4.8/qt-loadable-modules
[DEBUG][Python] 30.10.2018 10:30:09 [Python] (C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 30.10.2018 10:30:10 [Python] (C:\Program Files\Slicer 4.8.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 30.10.2018 10:30:14 [Python] (C:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 30.10.2018 10:30:19 [Python] (C:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 30.10.2018 10:30:19 [Python] (C:\Program Files\Slicer 4.8.0\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 30.10.2018 10:30:04 [] (unknown:0) - Number of registered modules: 162
[DEBUG][Qt] 30.10.2018 10:30:11 [] (unknown:0) - Number of instantiated modules: 162
[DEBUG][Qt] 30.10.2018 10:30:20 [] (unknown:0) - Number of loaded modules: 162
[DEBUG][Qt] 30.10.2018 10:30:20 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 30.10.2018 10:30:37 [] (unknown:0) - Unpacking bundle  "H:/[...]/P860-scar and planning.mrb"  to  "C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869"
[WARNING][Qt] 30.10.2018 10:30:42 [] (unknown:0) - QColor::fromRgbF: RGB parameters out of range
[INFO][VTK] 30.10.2018 10:30:42 [vtkMRMLVolumeArchetypeStorageNode (0000000009FEFC60)] (D:\D\P\Slicer-480\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869/P860-scar and planning/Data/11 3D MDE sax 3mm asset.nrrd. Dimensions: 256x256x72. Number of components: 1. Pixel type: short.
[INFO][VTK] 30.10.2018 10:30:42 [vtkMRMLVolumeArchetypeStorageNode (0000000009FEFE00)] (D:\D\P\Slicer-480\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869/P860-scar and planning/Data/15 3d fiesta cai.nrrd. Dimensions: 512x512x72. Number of components: 1. Pixel type: short.
[ERROR][VTK] 30.10.2018 10:30:42 [vtkSegmentationConverter (0000000051E50720)] (D:\D\P\Slicer-480\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:267) - SetConversionParameter: Conversion parameter 'Default slice thickness' not found in converter rules!
[ERROR][VTK] 30.10.2018 10:30:42 [vtkSegmentationConverter (00000000525B7C20)] (D:\D\P\Slicer-480\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:267) - SetConversionParameter: Conversion parameter 'Default slice thickness' not found in converter rules!
[INFO][VTK] 30.10.2018 10:30:43 [vtkMRMLVolumeArchetypeStorageNode (0000000052890A00)] (D:\D\P\Slicer-480\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869/P860-scar and planning/Data/623 RTDOSE Mr. Spock Dose 4D Accumulated 4DGPUCalc Accumulate 70.nrrd. Dimensions: 473x476x192. Number of components: 1. Pixel type: float.
[ERROR][VTK] 30.10.2018 10:30:43 [vtkSegmentationConverter (00000000525CB180)] (D:\D\P\Slicer-480\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:267) - SetConversionParameter: Conversion parameter 'Default slice thickness' not found in converter rules!
[WARNING][VTK] 30.10.2018 10:32:11 [vtkPolyData (000000005E750D10)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:11 [vtkPolyData (000000005E750D10)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:44 [vtkPolyData (000000005EB99280)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:44 [vtkPolyData (000000005EB99280)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:45 [vtkPolyData (000000005EB99100)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:45 [vtkPolyData (000000005EB99100)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:45 [vtkPolyData (000000005EB99400)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:46 [vtkPolyData (000000005EB99400)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:46 [vtkPolyData (000000005EB99400)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[WARNING][VTK] 30.10.2018 10:32:46 [vtkPolyData (000000005EB99400)] (D:\D\P\Slicer-480-package\VTKv8\Common\DataModel\vtkPolyData.cxx:993) - Building VTK_LINE 1 with only one point, but VTK_LINE needs at least two points. Check the input.
[INFO][VTK] 30.10.2018 10:32:51 [vtkMRMLVolumeArchetypeStorageNode (0000000052890BA0)] (D:\D\P\Slicer-480\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869/P860-scar and planning/Data/11 With contrast 1.0 I26f 3 0 - 95  TRIGGER_DELAY 70%.nrrd. Dimensions: 512x512x192. Number of components: 1. Pixel type: short.
[INFO][VTK] 30.10.2018 10:32:53 [vtkMRMLVolumeArchetypeStorageNode (00000000528906C0)] (D:\D\P\Slicer-480\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869/P860-scar and planning/Data/602 Private^Packer_Heart_Spiral (Adult) 0.nrrd. Dimensions: 512x512x192. Number of components: 1. Pixel type: short.
[INFO][Stream] 30.10.2018 10:32:53 [] (unknown:0) - CreateVTKTransformFromITK - SetVTKLinearTransformFromITK conversionSuccess:1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000052890EE0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000052890EE0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000052890EE0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567365B0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567365B0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567365B0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000056736750)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000056736750)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (0000000056736750)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567368F0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567368F0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][VTK] 30.10.2018 10:32:53 [vtkPolyDataReader (00000000567368F0)] (D:\D\P\Slicer-480-package\VTKv8\IO\Legacy\vtkDataReader.cxx:490) - Reading file version: 4.2 with older reader version 4.1
[WARNING][Qt] 30.10.2018 10:32:53 [] (unknown:0) - QColor::fromRgbF: RGB parameters out of range
[WARNING][Qt] 30.10.2018 10:32:53 [] (unknown:0) - QColor::fromRgbF: RGB parameters out of range
[WARNING][Qt] 30.10.2018 10:32:53 [] (unknown:0) - QColor::fromRgbF: RGB parameters out of range
[DEBUG][Qt] 30.10.2018 10:32:54 [] (unknown:0) - Loaded bundle from  "C:/Users/M171189/AppData/Local/Temp/__BundleLoadTemp2018-10-30_10+30+37.869"
[DEBUG][Qt] 30.10.2018 10:32:54 [] (unknown:0) - Reset scene to point to the MRB directory  H:/[...]/P860-scar and planning.mrml
[DEBUG][Qt] 30.10.2018 10:32:54 [] (unknown:0) - "MRB Slicer Data Bundle" Reader has successfully read the file "H:/[...]/P860-scar and planning.mrb" "[136.26s]"
[WARNING][Qt] 30.10.2018 10:33:19 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 30.10.2018 10:33:19 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Qt] 30.10.2018 10:33:20 [] (unknown:0) - packing to  "C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114"
[DEBUG][Qt] 30.10.2018 10:34:06 [] (unknown:0) - zipping to  "H:/[...]/P860-scar and planning_from4.8.mrb"
[INFO][VTK] 30.10.2018 10:34:06 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/11%203D%20MDE%20sax%203mm%20asset.nrrd
[INFO][VTK] 30.10.2018 10:34:06 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/11%203D%20MDE%20sax%203mm%20asset.nrrd
[INFO][VTK] 30.10.2018 10:34:06 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/11%20With%20contrast%201.0%20I26f%203%200%20-%2095%20%20TRIGGER_DELAY%2070%.nrrd
[INFO][VTK] 30.10.2018 10:34:06 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/11%20With%20contrast%201.0%20I26f%203%200%20-%2095%20%20TRIGGER_DELAY%2070%.nrrd
[INFO][VTK] 30.10.2018 10:34:17 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/15%203d%20fiesta%20cai.nrrd
[INFO][VTK] 30.10.2018 10:34:17 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/15%203d%20fiesta%20cai.nrrd
[INFO][VTK] 30.10.2018 10:34:20 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/602%20Private^Packer_Heart_Spiral%20(Adult)%200.nrrd
[INFO][VTK] 30.10.2018 10:34:20 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/602%20Private^Packer_Heart_Spiral%20(Adult)%200.nrrd
[INFO][VTK] 30.10.2018 10:34:29 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/602%20Private^Packer_Heart_Spiral%20(Adult).seq.nrrd
[INFO][VTK] 30.10.2018 10:34:29 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/602%20Private^Packer_Heart_Spiral%20(Adult).seq.nrrd
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_0.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_0.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_1.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_1.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_10.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_10.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_11.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_11.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_12.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_12.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_13.vtp
[INFO][VTK] 30.10.2018 10:34:48 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_13.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_14.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_14.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_15.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_15.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_16.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_16.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_17.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_17.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_18.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_18.vtp</code></pre>

---

## Post #4 by @stephan (2018-10-30 15:42 UTC)

<p>(part 2/2):</p>
<pre><code>[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_19.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_19.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_2.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_2.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_20.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_20.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_21.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_21.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_22.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_22.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_23.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_23.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_24.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_24.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_25.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_25.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_26.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_26.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_27.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_27.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_28.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_28.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_29.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_29.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_3.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_3.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_4.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_4.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_5.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_5.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_6.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_6.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_7.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_7.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_8.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_8.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_9.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg/612%20RTSTRUCT%20Planning.seg_9.vtp
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg.vtm
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/612%20RTSTRUCT%20Planning.seg.vtm
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/623%20RTDOSE%20Mr.%20Spock%20Dose%204D%20Accumulated%204DGPUCalc%20Accumulate%2070.nrrd
[INFO][VTK] 30.10.2018 10:34:49 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/623%20RTDOSE%20Mr.%20Spock%20Dose%204D%20Accumulated%204DGPUCalc%20Accumulate%2070.nrrd
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/CTtoMRI.h5
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/CTtoMRI.h5
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/IsodoseLevel_10GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/IsodoseLevel_10GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/IsodoseLevel_20GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/IsodoseLevel_20GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/IsodoseLevel_30GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/IsodoseLevel_30GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/IsodoseLevel_40GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/IsodoseLevel_40GY.vtk
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual%20statistics.schema.tsv
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual%20statistics.schema.tsv
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual%20statistics.tsv
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual%20statistics.tsv
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual.seg.nrrd
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/P860_MDE_LV_BP_scar_manual.seg.nrrd
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/P860_SE11.seg.nrrd
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/P860_SE11.seg.nrrd
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_2.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_2.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_3.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_3.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_7.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Data/Slicer%20Data%20Bundle%20Scene%20View_7.png
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/P860-scar and planning_from4.mrml
[INFO][VTK] 30.10.2018 10:34:54 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/P860-scar and planning_from4.mrml
[INFO][VTK] 30.10.2018 10:34:55 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding: C:/Users/M171189/AppData/Local/Temp/Slicer/__BundleSaveTemp-2018-10-30_10+33+20.114/P860-scar and planning_from4.8/Slicer Data Bundle Scene View_1.png
[INFO][VTK] 30.10.2018 10:34:55 [] (unknown:0) - Info: In D:\D\P\Slicer-480\Libs\MRML\Logic\vtkArchive.cxx, line 35
Zip: adding rel: P860-scar and planning_from4.8/Slicer Data Bundle Scene View_1.png
[DEBUG][Qt] 30.10.2018 10:34:55 [] (unknown:0) - saved  "H:/[...]/P860-scar and planning_from4.8.mrb"</code></pre>

---

## Post #5 by @lassoan (2018-10-30 15:45 UTC)

<p>See instructions for debugging Slicer startup issues here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Instruction_for_Windows</a></p>
<p>If you send me the scene in private message then I’ll have a look.</p>

---

## Post #6 by @stephan (2018-10-30 15:59 UTC)

<p>Thank you for the guidance…<br>
I went through the startup debugging instructions step by step.</p>
<ol>
<li>slicer.exe --disable-settings : Slicer still does not start.</li>
<li>event viewer: No entries relating to Slicer</li>
<li>process loading logging: Access is denied on my (work) machine, unfortunately.</li>
</ol>
<p>I’ll share the scene with you in a moment.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #7 by @lassoan (2018-10-31 04:25 UTC)

<p>I could not reproduce the issue. Scene is saved and loaded successfully.</p>
<p>During saving, additional temporary memory is allocated, so the crash may be due to running out of memory. You could try to increase virtual memory size to 32GB and see if you can ever reproduce the crash.</p>
<p>Not being able to start the application after crash might be due to Windows trying to apply compatibility settings, but I’m not sure if that was already there in Windows 7. Anyway, if the application is crashing then please check again if there is any non-default compatibility settings specified for <em>c:\Program Files\Slicer 4.10.0\bin\SlicerApp-real.exe</em>. The executable <em>c:\Program Files\Slicer 4.10.0\Slicer.exe</em> is just a launcher, so its compatibility settings may not matter. Check both application properties and in registry as described <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=155371923">here</a>.</p>
<p>It may also be possible that graphics card driver bugs cause the crash. What computer is this (desktop/laptop)? What graphics cards does it have?</p>
<p>Windows 7 mainstream support ended almost 4 years ago and <a href="https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet">all extended support will end in about a year</a>. We don’t have access to Windows 7 computers anymore. It is hard to do anything if we cannot reproduce the problem on a current operating system. If you get to a state when the application is not crashing then we could set up a remote desktop sharing session and debug it on your computer (write me a private message if you would like to do this).</p>

---

## Post #8 by @stephan (2018-10-31 13:33 UTC)

<p>Thank you Andras.<br>
Well, as you were not able to reproduce this, I think we can give up on this issue. After all, it only happens with this scene for me, and so I might just use 4.8.0 for this.</p>
<p>Just as an update: I first increased the page file size (which was “automatic”) to maximum 32000 MB, but it does not solve the issue. Also, when observing the Windows resource monitor during the saving, there seems to be plenty of available memory all the time.</p>
<p>One more mystery, though: Upon the sudden crash of Slicer, the /bin/SlicerApp-real.exe “disappears”. I noticed that because I wanted to check the compatibility settings. None were applied before the crash (after a clean install), but after Slicer crashing, the entire file was gone. So for after the next re-install I created a copy of SlicerApp-real.exe on my desktop. After another crash, and Slicer no longer starting up, I could simply copy this into /bin/ and everything worked again. I have no clue if this deleting the executable from the program folder is done by the virus protection software or if it is some weird Windows “feature”.</p>
<p>Anyway, I feel we might have reached a dead end here. I will use 4.8.0. as a work-around when necessary, and I have a crude method to make 4.10.0 work again after these crashes. And after all, the scene is actually saved correctly, so no real harm is done.</p>
<p>Andras, thank you again for your help and your investigations into this issue.</p>
<p>Best regards<br>
Stephan</p>

---

## Post #9 by @lassoan (2018-10-31 14:03 UTC)

<aside class="quote no-group" data-username="stephan" data-post="8" data-topic="4590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>Upon the sudden crash of Slicer, the /bin/SlicerApp-real.exe “disappears”.</p>
</blockquote>
</aside>
<p>It is not a Windows feature, but most likely your anti-virus software decides that the executable file must be quarantined.</p>

---

## Post #10 by @stephan (2018-10-31 14:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="4590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>most likely your anti-virus software decides that the executable file must be quarantined.</p>
</blockquote>
</aside>
<p>You are right. So it looks like all this was just the AV software’s fault.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d9f5f4dde40ff25836402ba83a0ad5ee994ef2f.png" data-download-href="/uploads/short-url/muopODIIxtS79KEuUK80jKQl9ef.png?dl=1" title="quarantine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d9f5f4dde40ff25836402ba83a0ad5ee994ef2f.png" alt="quarantine" data-base62-sha1="muopODIIxtS79KEuUK80jKQl9ef" width="690" height="367" data-dominant-color="F3E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">quarantine</span><span class="informations">944×503 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I consider this issue solved, because it is actually not Slicer related.</p>
<p>EDIT:<br>
For the record: The antivirus software is Trend Micro OfficeScan and the issue seems to be known. <a href="https://community.spiceworks.com/topic/2007417-trend-micro-false-positive" class="inline-onebox" rel="noopener nofollow ugc">Trend Micro false positive - Security - Spiceworks Community</a></p>

---

## Post #11 by @lassoan (2018-10-31 14:18 UTC)

<aside class="quote no-group quote-modified" data-username="stephan" data-post="10" data-topic="4590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>The antivirus software is Trend Micro OfficeScan.</p>
</blockquote>
</aside>
<p>This faulty OfficeScan behavior has been widely reported for many software. To prevent this from happening again, you can add an exception for this file (or better yet, for the entire Slicer folder). Antivirus is not really needed for current Windows versions, but for Windows7 it is probably better to keep it.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> It could be useful to sign executables for Windows, too, to reduce the chance of overly aggressive AV heuristics flagging Slicer executables.</p>

---

## Post #12 by @stephan (2018-10-31 14:23 UTC)

<p>I just now try to set up an exception.<br>
In a corporate environment where all IT security is managed by someone else (i.e. the IT department), this is harder than one might think… <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"></p>

---
