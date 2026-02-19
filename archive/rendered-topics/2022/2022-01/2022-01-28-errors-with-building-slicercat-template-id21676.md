---
topic_id: 21676
title: "Errors With Building Slicercat Template"
date: 2022-01-28
url: https://discourse.slicer.org/t/21676
---

# Errors with building slicercat template

**Topic ID**: 21676
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/errors-with-building-slicercat-template/21676

---

## Post #1 by @Mrwa_Awoda (2022-01-28 11:35 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
I am trying to build the SlicerCAT as explained in <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> by following the exact instructions here <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a></p>
<p>I have got error and warnings about CTK, VTK and simpleITK projects in the last step of the build process in VS while I haven’t change anything in <code>CMakeLists.txt</code>. would you please tell me how to fix it?</p>
<details>
<summary>Details about error and warnings related to CTK, VTK and simpleITK projects</summary>
<pre><code class="lang-auto">|Error|MSB8066|Custom build for 'E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-mkdir.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-download.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-update.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-patch.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-configure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-build.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-forceconfigure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\Slicer-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\Slicer.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.|Slicer|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
|Error|MSB8066|Custom build for 'E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-mkdir.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-download.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-update.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-patch.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-configure.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-build.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\SimpleITK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\SimpleITK.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.|SimpleITK|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
|Error|MSB8066|Custom build for 'E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-mkdir.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-download.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-update.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-patch.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-configure.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-forcebuild.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-build.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-install.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\9be4e433cd02aef5b6487fefef7ada35\SimpleITK-complete.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\bb9f6672bdc8a30b78dccc82e0a89b19\SimpleITK.rule;E:\D\S4R\SimpleITK\SuperBuild\CMakeLists.txt' exited with code 1. [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]|SimpleITK|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
|Error|LNK1181|cannot open input file 'E:\D\S4R\ITK-build\lib\Release\itksys-5.2.lib' [E:\D\S4R\SimpleITK-build\SimpleITK-build\Code\Common\src\SimpleITKCommon.vcxproj] [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]|SimpleITK|E:\D\S4R\LINK|1||
|Error|MSB8066|Custom build for 'E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-mkdir.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-download.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-update.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-patch.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-configure.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-build.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-generate_project_description.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\SlicerExecutionModel-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\SlicerExecutionModel.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.|SlicerExecutionModel|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
|Error|LNK1181|cannot open input file 'E:\D\S4R\ITK-build\lib\Release\itksys-5.2.lib' [E:\D\S4R\SlicerExecutionModel-build\ModuleDescriptionParser\ModuleDescriptionParser.vcxproj]|SlicerExecutionModel|E:\D\S4R\LINK|1||
|Error|MSB8066|Custom build for 'E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-mkdir.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-download.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-update.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-patch.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-configure.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-build.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-generate_project_description.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\CTK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\CTK.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.|CTK|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
|Error|MSB8066|Custom build for 'E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-mkdir.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-download.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-update.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-patch.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-configure.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-build.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-forceconfigure.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-install.rule;E:\D\S4R\CTK-build\CMakeFiles\5ecc0909b7e629936336667a3198cb7f\CTK-complete.rule;E:\D\S4R\CTK-build\CMakeFiles\133301bfd8d7306c1cff6360a6c6b40c\CTK.rule;E:\D\S4R\CTK\CMakeLists.txt' exited with code 1. [E:\D\S4R\CTK-build\CTK.vcxproj]|CTK|C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets|242||
</code></pre>
<div class="md-table">
<table>
<thead>
<tr>
<th>Severity</th>
<th>Code</th>
<th>Description</th>
<th>Project</th>
<th>File</th>
<th>Line</th>
<th>Suppression State</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-mkdir.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-download.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-update.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-patch.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-configure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-build.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-forceconfigure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\Slicer-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\Slicer.rule;E:\D\S4\Slicer\CMakeLists.txt’ exited with code 1.</td>
<td>Slicer</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-mkdir.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-download.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-update.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-patch.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-configure.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-build.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\SimpleITK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\SimpleITK.rule;E:\D\S4\Slicer\CMakeLists.txt’ exited with code 1.</td>
<td>SimpleITK</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-mkdir.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-download.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-update.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-patch.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-configure.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-forcebuild.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-build.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-install.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\9be4e433cd02aef5b6487fefef7ada35\SimpleITK-complete.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\bb9f6672bdc8a30b78dccc82e0a89b19\SimpleITK.rule;E:\D\S4R\SimpleITK\SuperBuild\CMakeLists.txt’ exited with code 1. [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]</td>
<td>SimpleITK</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>LNK1181</td>
<td>cannot open input file ‘E:\D\S4R\ITK-build\lib\Release\itksys-5.2.lib’ [E:\D\S4R\SimpleITK-build\SimpleITK-build\Code\Common\src\SimpleITKCommon.vcxproj] [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]</td>
<td>SimpleITK</td>
<td>E:\D\S4R\LINK</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-mkdir.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-download.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-update.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-patch.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-configure.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-build.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-generate_project_description.rule;E:\D\S4R\CMakeFiles\99511604aac5c76d372eaa262a119621\SlicerExecutionModel-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\SlicerExecutionModel-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\SlicerExecutionModel.rule;E:\D\S4\Slicer\CMakeLists.txt’ exited with code 1.</td>
<td>SlicerExecutionModel</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>LNK1181</td>
<td>cannot open input file ‘E:\D\S4R\ITK-build\lib\Release\itksys-5.2.lib’ [E:\D\S4R\SlicerExecutionModel-build\ModuleDescriptionParser\ModuleDescriptionParser.vcxproj]</td>
<td>SlicerExecutionModel</td>
<td>E:\D\S4R\LINK</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-mkdir.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-download.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-update.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-patch.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-configure.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-build.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-generate_project_description.rule;E:\D\S4R\CMakeFiles\9bad8873f29c688a199c24d814eb83b7\CTK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\CTK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\CTK.rule;E:\D\S4\Slicer\CMakeLists.txt’ exited with code 1.</td>
<td>CTK</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>MSB8066</td>
<td>Custom build for ‘E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-mkdir.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-download.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-update.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-patch.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-configure.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-build.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-forceconfigure.rule;E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-install.rule;E:\D\S4R\CTK-build\CMakeFiles\5ecc0909b7e629936336667a3198cb7f\CTK-complete.rule;E:\D\S4R\CTK-build\CMakeFiles\133301bfd8d7306c1cff6360a6c6b40c\CTK.rule;E:\D\S4R\CTK\CMakeLists.txt’ exited with code 1. [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets</td>
<td>242</td>
<td></td>
</tr>
<tr>
<td>Warning</td>
<td>C4996</td>
<td>‘QTime::start’: Use QElapsedTimer instead [E:\D\S4R\CTK-build\CTK-build\Libs\Visualization\VTK\Widgets\CTKVisualizationVTKWidgets.vcxproj] [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>E:\D\S4R\CTK\Libs\Visualization\VTK\Widgets\ctkVTKAbstractView.cpp</td>
<td>206</td>
<td></td>
</tr>
<tr>
<td>Warning</td>
<td>C4302</td>
<td>‘reinterpret_cast’: truncation from ‘void *’ to ‘long’ [E:\D\S4R\CTK-build\CTK-build\Libs\Visualization\VTK\Widgets\CTKVisualizationVTKWidgets.vcxproj] [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>E:\D\S4R\CTK\Libs\Visualization\VTK\Widgets\ctkVTKScalarsToColorsWidget.cpp</td>
<td>299</td>
<td></td>
</tr>
<tr>
<td>Warning</td>
<td>C4302</td>
<td>‘reinterpret_cast’: truncation from ‘void *’ to ‘unsigned long’ [E:\D\S4R\CTK-build\CTK-build\Libs\Visualization\VTK\Widgets\CTKVisualizationVTKWidgets.vcxproj] [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>E:\D\S4R\CTK\Libs\Visualization\VTK\Widgets\ctkVTKScalarsToColorsView.cpp</td>
<td>559</td>
<td></td>
</tr>
<tr>
<td>Warning</td>
<td>C4996</td>
<td>‘Qt::MidButton’: MidButton is deprecated. Use MiddleButton instead [E:\D\S4R\CTK-build\CTK-build\Libs\Visualization\VTK\Widgets\CTKVisualizationVTKWidgets.vcxproj] [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>E:\D\S4R\CTK\Libs\Visualization\VTK\Widgets\ctkVTKChartView.cpp</td>
<td>428</td>
<td></td>
</tr>
<tr>
<td>Error</td>
<td>LNK1181</td>
<td>cannot open input file ‘E:\D\S4R\ITK-build\lib\Release\ITKCommon-5.2.lib’ [E:\D\S4R\CTK-build\CTK-build\Libs\ImageProcessing\ITK\Core\CTKImageProcessingITKCore.vcxproj] [E:\D\S4R\CTK-build\CTK.vcxproj]</td>
<td>CTK</td>
<td>E:\D\S4R\LINK</td>
<td>1</td>
<td></td>
</tr>
</tbody>
</table>
</div></details>

---

## Post #2 by @lassoan (2022-01-28 17:11 UTC)

<p>Please use the latest master version of the custom application template with the latest master version of Slicer and let us know if you run into any issues.</p>

---

## Post #3 by @Marwa_Awoda (2022-02-03 15:10 UTC)

<p>Hello Andras,<br>
Here is the steps of the build process  that I’ve followed … (in a screen record)</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1zo3XGNRrzAb0IQp_rOji0yjjpF5xv5Q8/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1zo3XGNRrzAb0IQp_rOji0yjjpF5xv5Q8/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/BuwMUlKptPIpisIeCQsmY8ID-SwDto8AeGBluQ6UBrqSYsiZ4Uf3KfCgDwvyIk54jus=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1zo3XGNRrzAb0IQp_rOji0yjjpF5xv5Q8/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">tut.webm</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Still getting these errors and warnings:</p>
<pre><code class="lang-auto">Warning	MSB8064	Custom build for item "E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-build.rule" succeeded, but specified dependency "e:\d\s4r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure" does not exist. This may cause incremental build to work incorrectly. [E:\D\S4R\CTK-build\CTK.vcxproj]	CTK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	242	
Warning	C4996	'PyEval_CallObjectWithKeywords': deprecated in 3.9 [E:\D\S4R\VTK-build\Wrapping\PythonCore\WrappingPythonCore.vcxproj]	VTK	E:\D\S4R\VTK\Wrapping\PythonCore\vtkPythonUtil.cxx	567	
Warning	C4100	'globals': unreferenced formal parameter [E:\D\S4R\VTK-build\Wrapping\PythonCore\WrappingPythonCore.vcxproj]	VTK	E:\D\S4R\VTK\Wrapping\PythonCore\vtkPythonUtil.cxx	893	
Warning	C4996	'PyEval_CallObjectWithKeywords': deprecated in 3.9 [E:\D\S4R\VTK-build\Wrapping\PythonCore\WrappingPythonCore.vcxproj]	VTK	E:\D\S4R\VTK\Wrapping\PythonCore\vtkPythonUtil.cxx	1086	
Warning	MSB8065	Custom build for item "E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-configure.rule" succeeded, but specified output "e:\d\s4r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure" has not been created. This may cause incremental build to work incorrectly. [E:\D\S4R\CTK-build\CTK.vcxproj]	CTK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	242	
Warning	C4293	'&lt;&lt;': shift count negative or too big, undefined behavior [E:\D\S4R\SimpleITK-build\SimpleITK-build\Code\BasicFilters\src\SimpleITK_ITKLabelMap.vcxproj] [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]	SimpleITK	E:\D\S4R\ITK\Modules\Filtering\LabelMap\include\itkStatisticsLabelMapFilter.h	142	
Warning	C4293	'&lt;&lt;': shift count negative or too big, undefined behavior [E:\D\S4R\SimpleITK-build\SimpleITK-build\Code\BasicFilters\src\SimpleITK_ITKLabelMap.vcxproj] [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]	SimpleITK	E:\D\S4R\ITK\Modules\Filtering\LabelMap\include\itkStatisticsLabelMapFilter.hxx	77	
Error	LNK1181	cannot open input file 'optimized.lib' [E:\D\S4R\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK_PYTHON.vcxproj] [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]	SimpleITK	E:\D\S4R\LINK	1	
Error	MSB8066	Custom build for 'E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-forcebuild.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-build.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\e434fb47607d62ac9904788467fcbb5e\SimpleITK-install.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\9be4e433cd02aef5b6487fefef7ada35\SimpleITK-complete.rule;E:\D\S4R\SimpleITK-build\CMakeFiles\bb9f6672bdc8a30b78dccc82e0a89b19\SimpleITK.rule;E:\D\S4R\SimpleITK\SuperBuild\CMakeLists.txt' exited with code 1. [E:\D\S4R\SimpleITK-build\SimpleITK.vcxproj]	SimpleITK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	242	
Error	MSB8066	Custom build for 'E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-configure.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-build.rule;E:\D\S4R\CMakeFiles\eec0fafea484c1c9bf8d0dbc735ed3d8\SimpleITK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\SimpleITK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\SimpleITK.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.	SimpleITK	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	242	
Error	MSB8066	Custom build for 'E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-configure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-build.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-forceconfigure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\Slicer-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\Slicer.rule;E:\D\S4\Slicer\CMakeLists.txt' exited with code 1.	Slicer	C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets	242
</code></pre>

---

## Post #4 by @jcfr (2022-02-03 18:53 UTC)

<p>There are two issues being discussed here:</p>
<ol>
<li>
<p>Build error when creating, and then building a custom application following instruction outline in <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>
</li>
<li>
<p>Build errors when building Slicer following instructions described on <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox">Windows — 3D Slicer documentation</a></p>
</li>
</ol>
<p><a class="mention" href="/u/mrwa_awoda">@Mrwa_Awoda</a></p>
<p>If you would like to create custom Slicer-based application, successfully building Slicer itself will allow to confirm your development environment is valid.</p>
<p>I suggest we focus on  building Slicer first.</p>
<p>In your last post, you copied some error messages. That said, we are missing the actual errors … which is probably reported earlier in the output.</p>
<p>It looks like <code>SimpleITK</code> failed to build … after opening the top-level solution file (<code>C:\D\S4R\Slicer.sln</code>) and selecting <code>Release</code>, I suggest you right click on <code>SimpleITK</code> and select <code>Project Only</code> then <code>Build Only SimpleITK</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/849d4b169ea6c826bed8e8f2101881863ddad56e.png" data-download-href="/uploads/short-url/iVa1zUetbflNHcJ17Lq8326CZMG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/849d4b169ea6c826bed8e8f2101881863ddad56e.png" alt="image" data-base62-sha1="iVa1zUetbflNHcJ17Lq8326CZMG" width="690" height="403" data-dominant-color="30292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">738×432 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This should help identify the SimpleITK specific errors.</p>

---

## Post #5 by @Mrwa_Awoda (2022-02-03 20:11 UTC)

<p>Hi jcfr,<br>
thanks for your response…<br>
here what i get …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af18cc6c613d8f335f274b97b7208503c48d10b.png" data-download-href="/uploads/short-url/3QlVOCjDZWBGMBesKDBIfqqWrOP.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af18cc6c613d8f335f274b97b7208503c48d10b.png" alt="Capture" data-base62-sha1="3QlVOCjDZWBGMBesKDBIfqqWrOP" width="690" height="369" data-dominant-color="303031"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1365×730 61.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jcfr (2022-02-03 21:27 UTC)

<p>The relevant message seems to be:</p>
<pre><code class="lang-auto">LINK : falal error LNK1181:  cannot open input file 'optimized.lib'
</code></pre>
<p><em>Note: While screenshot helps understand the context. In addition, it is a good practice to copy the error message as text. This allow to easy copy/past the message (or part of it), and also ensure the error will be indexed by the forum search  engine)</em></p>
<p><strong>Question 1:</strong> Could you also check if <code>ITK</code> build successfully following the same approach ?</p>
<p><strong>Question 2</strong>: Did you customize the <code>PATH</code> environment variable on  your workstation  ?</p>
<p><strong>Question 3:</strong> Is there any registry entries associated with  one of these key ?  (see details and screenshot below)</p>
<ul>
<li><code>HKEY_LOCAL_MACHINE\Software\Kitware\CMake\Packages\&lt;PackageName&gt;</code></li>
<li><code>HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\&lt;PackageName&gt;</code></li>
</ul>
<h4><a name="p-73496-cmake-user-and-system-package-registry-1" class="anchor" href="#p-73496-cmake-user-and-system-package-registry-1" aria-label="Heading link"></a>CMake User and system package registry</h4>
<p>I am wondering if some other package built and exported on your system are interfering with one of the build-system.</p>
<p>We usually make sure no packages built by Slicer are exported to the CMake registry but it is possible we missed something with the recent updates.</p>
<p>More details can be found here: <a href="https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#system-package-registry" class="inline-onebox">cmake-packages(7) — CMake 4.2.0 Documentation</a></p>
<p>Registry editor is found on windows typing <code>regedit</code> in the windows menu</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec302a4401d50135d383ccbaee327fdccbfeea5c.png" data-download-href="/uploads/short-url/xHpSkpp2mzAgT6qiGwftOjizw96.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec302a4401d50135d383ccbaee327fdccbfeea5c.png" alt="image" data-base62-sha1="xHpSkpp2mzAgT6qiGwftOjizw96" width="606" height="450"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">606×450 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Mrwa_Awoda (2022-02-03 22:16 UTC)

<p>thanks for your patience…<br>
here what i get after building the ITK…</p>
<pre><code class="lang-auto">Build started...
1&gt;------ Build started: Project: ITK, Configuration: Release x64 ------
1&gt;Performing update step for 'ITK'
1&gt;No patch step for 'ITK'
1&gt;Performing configure step for 'ITK'
1&gt;loading initial cache file E:/D/S4R/ITK-prefix/tmp/ITK-cache-Release.cmake
1&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
1&gt;error launching git: The process cannot access the file because it is being used by another process.
1&gt;
1&gt;CMake Error at CMake/ITKModuleRemote.cmake:91 (message):
1&gt;  Failed to get the hash for
1&gt;  https://github.com/ntustison/ITKAdaptiveDenoising.git HEAD
1&gt;Call Stack (most recent call first):
1&gt;  CMake/ITKModuleRemote.cmake:137 (_git_update)
1&gt;  CMake/ITKModuleRemote.cmake:236 (_fetch_with_git)
1&gt;  Modules/Remote/AdaptiveDenoising.remote.cmake:44 (itk_fetch_module)
1&gt;  Modules/Remote/CMakeLists.txt:10 (include)
1&gt;
1&gt;
1&gt;-- Configuring incomplete, errors occurred!
1&gt;See also "E:/D/S4R/ITK-build/CMakeFiles/CMakeOutput.log".
1&gt;See also "E:/D/S4R/ITK-build/CMakeFiles/CMakeError.log".
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(242,5): error MSB8066: Custom build for 'E:\D\S4R\CMakeFiles\5192aa6b129195b05a27c64828fbcc8c\ITK-update.rule;E:\D\S4R\CMakeFiles\5192aa6b129195b05a27c64828fbcc8c\ITK-patch.rule;E:\D\S4R\CMakeFiles\5192aa6b129195b05a27c64828fbcc8c\ITK-configure.rule;E:\D\S4R\CMakeFiles\5192aa6b129195b05a27c64828fbcc8c\ITK-build.rule;E:\D\S4R\CMakeFiles\5192aa6b129195b05a27c64828fbcc8c\ITK-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\ITK-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\ITK.rule' exited with code 1.
1&gt;Done building project "ITK.vcxproj" -- FAILED.
========== Build: 0 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========
</code></pre>
<p>there are no other packages have biult or exported in the CMake registry :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e3eed0e3a4af9a08c88f44b89ac79ff101af821.png" data-download-href="/uploads/short-url/221vbcXmIYbajdQbLGKTSf41D4R.png?dl=1" title="Capturej" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e3eed0e3a4af9a08c88f44b89ac79ff101af821_2_690x352.png" alt="Capturej" data-base62-sha1="221vbcXmIYbajdQbLGKTSf41D4R" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e3eed0e3a4af9a08c88f44b89ac79ff101af821_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e3eed0e3a4af9a08c88f44b89ac79ff101af821.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e3eed0e3a4af9a08c88f44b89ac79ff101af821.png 2x" data-dominant-color="F3F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capturej</span><span class="informations">1009×516 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d09adeccd1cb728e50b6187a491ab495a688aa0.png" data-download-href="/uploads/short-url/fyAMv6GF7bOHvCuE9CxBHgsLHyM.png?dl=1" title="Captureh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d09adeccd1cb728e50b6187a491ab495a688aa0.png" alt="Captureh" data-base62-sha1="fyAMv6GF7bOHvCuE9CxBHgsLHyM" width="529" height="500" data-dominant-color="E4E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captureh</span><span class="informations">619×584 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @jcfr (2022-02-03 22:57 UTC)

<aside class="quote no-group" data-username="Mrwa_Awoda" data-post="7" data-topic="21676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrwa_awoda/48/10236_2.png" class="avatar"> Mrwa_Awoda:</div>
<blockquote>
<p><code>error launching git: The process cannot access the file because it is being used by another process.</code></p>
</blockquote>
</aside>
<p>This seems to indicate you have either another instance of Visual Studio, a text editor or a terminal open in the directory … I suggest you close the applications and try again.</p>

---

## Post #9 by @Mrwa_Awoda (2022-02-04 00:34 UTC)

<p>Right, ItK build completed successfully!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7166162c71352548ef1b13648900d1ac65279a58.png" data-download-href="/uploads/short-url/gbaFLNLYWmNGlB7hXDj8cJbqSdq.png?dl=1" title="Capture ITK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7166162c71352548ef1b13648900d1ac65279a58.png" alt="Capture ITK" data-base62-sha1="gbaFLNLYWmNGlB7hXDj8cJbqSdq" width="690" height="363" data-dominant-color="313132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture ITK</span><span class="informations">1184×624 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>unfortunately, still having warnings after building CTK:</p>
<p>.</p>
<p>.</p>
<p>Completed ‘CTK’</p>
<p>1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(242,5): warning MSB8065: Custom build for item “E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-configure.rule” succeeded, but specified output “e:\d\s4r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” has not been created. This may cause incremental build to work incorrectly. [E:\D\S4R\CTK-build\CTK.vcxproj]</p>
<p>1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(242,5): warning MSB8064: Custom build for item “E:\D\S4R\CTK-build\CMakeFiles\6897e4f0eca62e72c3a61e1ea7f571d2\CTK-build.rule” succeeded, but specified dependency “e:\d\s4r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” does not exist. This may cause incremental build to work incorrectly. [E:\D\S4R\CTK-build\CTK.vcxproj]</p>
<p>1&gt;No install step for ‘CTK’</p>
<p>1&gt;Completed ‘CTK’</p>
<p>1&gt;Done building project “CTK.vcxproj”.</p>
<p>========== Build: 1 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========</p>
<p>and with building Slicer as well:</p>
<p>.</p>
<p>.</p>
<p>1&gt;-- --------------------------------------------------</p>
<p>1&gt;-- Configuring Slicer application library: qSlicerApp</p>
<p>1&gt;-- --------------------------------------------------</p>
<p>1&gt;-- Setting Slicer DESCRIPTION_SUMMARY to ‘Medical Visualization and Processing Environment for Research’</p>
<p>1&gt;-- Setting Slicer DESCRIPTION_FILE to ‘E:/D/S4/Slicer/README.txt’</p>
<p>1&gt;-- --------------------------------------------------</p>
<p>1&gt;-- Configuring Slicer application: SlicerApp</p>
<p>1&gt;-- --------------------------------------------------</p>
<p>1&gt;-- Setting Slicer APPLICATION_NAME to ‘Slicer’</p>
<p>1&gt;-- Setting Slicer LAUNCHER_SPLASHSCREEN_FILE to ‘E:/D/S4/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png’</p>
<p>1&gt;-- Setting Slicer APPLE_ICON_FILE to ‘E:/D/S4/Slicer/Applications/SlicerApp/Resources/Slicer.icns’</p>
<p>1&gt;-- Setting Slicer WIN_ICON_FILE to ‘E:/D/S4/Slicer/Applications/SlicerApp/Resources/Slicer.ico’</p>
<p>1&gt;-- Setting Slicer LICENSE_FILE to ‘E:/D/S4/Slicer/License.txt’</p>
<p>1&gt;-- Setting Slicer executable name to ‘SlicerApp-real.exe’</p>
<p>1&gt;-- Setting Slicer EXECUTABLE to ‘E:/D/S4R/Slicer-build/bin/SlicerApp-real.exe’</p>
<p>1&gt;CMake Error at CMake/SlicerMacroBuildApplication.cmake:479 (get_filename_component):</p>
<p>1&gt; get_filename_component unknown component optimized</p>
<p>1&gt;Call Stack (most recent call first):</p>
<p>1&gt; Applications/SlicerApp/CMakeLists.txt:66 (slicerMacroBuildApplication)</p>
<p>1&gt;</p>
<p>1&gt;</p>
<p>1&gt;-- Configuring incomplete, errors occurred!</p>
<p>1&gt;See also “E:/D/S4R/Slicer-build/CMakeFiles/CMakeOutput.log”.</p>
<p>1&gt;See also “E:/D/S4R/Slicer-build/CMakeFiles/CMakeError.log”.</p>
<p>1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(242,5): error MSB8066: Custom build for ‘E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-configure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-build.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-forceconfigure.rule;E:\D\S4R\CMakeFiles\edbed8a7c8f5e3496e69de9e4425bff5\Slicer-install.rule;E:\D\S4R\CMakeFiles\a292924acdc90ab5003f524bcf7a9fa8\Slicer-complete.rule;E:\D\S4R\CMakeFiles\18dd41b82dccc87fa779d30114192df1\Slicer.rule’ exited with code 1.</p>
<p>1&gt;Done building project “Slicer.vcxproj” – FAILED.</p>
<p>========== Build: 0 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========</p>

---
