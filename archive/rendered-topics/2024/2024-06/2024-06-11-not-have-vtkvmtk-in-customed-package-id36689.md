# Not have vtkvmtk in customed package

**Topic ID**: 36689
**Date**: 2024-06-11
**URL**: https://discourse.slicer.org/t/not-have-vtkvmtk-in-customed-package/36689

---

## Post #1 by @schcat (2024-06-11 02:43 UTC)

<p>I use SlicerCustomAppTemplate to customize Slicer, when I  run “make” and “make package” and test the software, everything is OK, exept that there is not vtkvmtk module in package.</p>
<p>I can import vtkvmtk*** in Slicer-build/SlicerCustomAppTemplate, but cant’t in package file. I notice that there are no vtkvmtk .so files in package root: Slicer-build/SlicerCustomAppTemplate-0.1.0-linux-amd64/lib/SlicerCustomAppTemplate-5.3/qt-scripted-modules, but there exist in make root: Slicer-build//lib/SlicerCustomAppTemplate-5.3/qt-scripted-modules.</p>
<p>I can’t find how to add vtkvmtk to package by CPack. My CPack outcome is:</p>
<pre><code class="lang-auto">Run CPack packaging tool...
CPack: Create package using TGZ
CPack: Install projects
CPack: - Run preinstall target for: IGSIO
CPack: - Install project: IGSIO []
CPack: - Run preinstall target for: OpenIGTLink
CPack: - Install project: OpenIGTLink []
CPack: - Run preinstall target for: OpenIGTLinkIO
CPack: - Install project: OpenIGTLinkIO []
CPack: - Run preinstall target for: VMTK
CPack: - Install project: VMTK []
CPack: - Run preinstall target for: VMTK
CPack: - Install project: VMTK []
CPack: - Run preinstall target for: VMTK
CPack: - Install project: VMTK []
CPack: - Run preinstall target for: CTK
CPack: - Install project: CTK []
CPack: - Run preinstall target for: CTK
CPack: - Install project: CTK []
CPack: - Run preinstall target for: VTK
CPack: - Install project: VTK []
CPack: - Run preinstall target for: VTK
CPack: - Install project: VTK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: ITK
CPack: - Install project: ITK []
CPack: - Run preinstall target for: JsonCpp
CPack: - Install project: JsonCpp []
CPack: - Run preinstall target for: SlicerExecutionModel
CPack: - Install project: SlicerExecutionModel []
CPack: - Run preinstall target for: teem
CPack: - Install project: teem []
CPack: - Run preinstall target for: CTK
CPack: - Install project: CTK []
CPack: - Run preinstall target for: Slicer
CPack: - Install project: Slicer []
CPack: - Run preinstall target for: Slicer
CPack: - Install project: Slicer []
CPack: Create package
</code></pre>

---

## Post #2 by @schcat (2024-06-16 02:07 UTC)

<p>Administrators can close this question. I fond that this due to the revise of my External_VMTK.cmake file in SlicerVMTK.</p>

---
