---
topic_id: 22320
title: "Errors In Windows Build Of Preview Version"
date: 2022-03-04
url: https://discourse.slicer.org/t/22320
---

# Errors in Windows build of preview version

**Topic ID**: 22320
**Date**: 2022-03-04
**URL**: https://discourse.slicer.org/t/errors-in-windows-build-of-preview-version/22320

---

## Post #1 by @smrolfe (2022-03-04 23:39 UTC)

<p>I’m getting the following VTK-related errors while trying to build the Preview version of Slicer for Windows 10. I just updated to CMake 3.23.0-rc2, although I believe this should be fine?</p>
<p>I’m not able to find the lib file that can’t be opened: “vtkViewsQt-9.1d.lib”. Any advice on how to resolve this?</p>
<pre><code class="lang-auto">Severity	Code	Description	Project	File	Line	Suppression State
Error	C2039	'max': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2039	'max': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2065	'max': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2039	'min': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2065	'min': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	328	
Error	C2039	'max': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	331	
Error	C2065	'max': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	331	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	331	
Error	C2065	'max': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2039	'min': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2065	'min': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	425	
Error	C2039	'max': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	426	
Error	C2065	'max': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	426	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	426	
Error	C2039	'max': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	C2065	'max': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	C2039	'min': is not a member of 'std' [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	C2065	'min': undeclared identifier [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	C2275	'vtkIdType': illegal use of this type as an expression [C:\S_B\VTK-build\Common\DataModel\CommonDataModel-objects.vcxproj]	VTK	C:\S_B\VTK\Common\DataModel\vtkTable.cxx	491	
Error	LNK1104	cannot open file 'C:\S_B\VTK-build\lib\Debug\vtkViewsInfovis-9.1d.lib' [C:\S_B\CTK-build\CTK-build\Libs\Visualization\VTK\Core\CTKVisualizationVTKCore.vcxproj] [C:\S_B\CTK-build\CTK.vcxproj]	CTK	C:\S_B\LINK	1	
Error	LNK1104	cannot open file 'C:\S_B\VTK-build\lib\Debug\vtkViewsQt-9.1d.lib' [C:\S_B\Slicer-build\Libs\vtkAddon\vtkAddon.vcxproj]	Slicer	C:\S_B\LINK	1	
Error	LNK1104	cannot open file 'C:\S_B\VTK-build\lib\Debug\vtkViewsQt-9.1d.lib' [C:\S_B\Slicer-build\Libs\vtkITK\vtkITK.vcxproj]	Slicer	C:\S_B\LINK	1	
Error	LNK1104	cannot open file 'C:\S_B\VTK-build\lib\Debug\vtkViewsQt-9.1d.lib' [C:\S_B\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj]	Slicer	C:\S_B\LINK	1	
Error	LNK1104	cannot open file 'C:\S_B\VTK-build\lib\Debug\vtkViewsQt-9.1d.lib' [C:\S_B\Slicer-build\Libs\vtkTeem\vtkTeem.vcxproj]	Slicer	C:\S_B\LINK	1	
</code></pre>

---

## Post #2 by @smrolfe (2022-03-08 22:14 UTC)

<p>This issue was resolved when I updated from Visual Studio 2019 to 2022.</p>

---

## Post #3 by @lassoan (2022-03-08 23:36 UTC)

<p>Have you rebuilt entire Slicer (the top-level build, including VTK, ITK, etc.) from scratch after updating CMake?</p>
<p>I use CMake-3.22.0, Slicer factory computers use CMake-3.22.1, so these versions should work. Regressions in CMake are quite common, so in general I would recommend to use well-proven versions and not experiment with release candidates (unless there is a fix that you need and it is only available in the most recent version).</p>

---

## Post #4 by @smrolfe (2022-03-08 23:42 UTC)

<p>Yes, I rebuilt from scratch after the CMake update, so I’m not sure what resolved the issue.</p>
<p>I’ll stick to a more stable CMake version going forward, thanks!</p>

---
