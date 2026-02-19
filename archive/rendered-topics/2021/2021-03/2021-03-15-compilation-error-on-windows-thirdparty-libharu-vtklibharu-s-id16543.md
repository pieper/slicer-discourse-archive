---
topic_id: 16543
title: "Compilation Error On Windows Thirdparty Libharu Vtklibharu S"
date: 2021-03-15
url: https://discourse.slicer.org/t/16543
---

# Compilation error on windows - ThirdParty/libharu/vtklibharu/src/hpdf_doc.c: No such file or directory

**Topic ID**: 16543
**Date**: 2021-03-15
**URL**: https://discourse.slicer.org/t/compilation-error-on-windows-thirdparty-libharu-vtklibharu-src-hpdf-doc-c-no-such-file-or-directory/16543

---

## Post #1 by @oren (2021-03-15 06:38 UTC)

<p>Operating system:windows 10 pro<br>
Slicer version:latest of 14.03.2021  <a href="https://github.com/Slicer/Slicer.git" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer.git</a><br>
Expected behavior:build successful on Release mode<br>
Actual behavior:compilation error</p>
<p>|Error||VTK was not configured to use Qt, you probably need to recompile it|Slicer|D:\SlicerCAT\S4R\CUSTOMBUILD|1||</p>
<p>|Error||unable to stat just-written file ThirdParty/libharu/vtklibharu/src/hpdf_doc.c: No such file or directory|VTK|D:\SlicerCAT\S4R\CUSTOMBUILD|1||</p>
<p>|Error|LNK1181|cannot open input file ‘vtkViewsContext2D.lib’ [D:\SlicerCAT\S4R\CTK-build\CTK-build\Libs\Visualization\VTK\Core\CTKVisualizationVTKCore.vcxproj] [D:\SlicerCAT\S4R\CTK-build\CTK.vcxproj]|CTK|D:\SlicerCAT\S4R\LINK|1||</p>

---

## Post #2 by @oren (2021-03-15 07:42 UTC)

<p>Update:<br>
It looks like the malware protection software have identify ‘hpdf_doc.c’ as malicious and removed it.</p>
<p>issue solved</p>

---

## Post #3 by @lassoan (2021-03-17 02:21 UTC)

<p>Thanks for the update. Was it avast?</p>

---

## Post #4 by @oren (2021-03-17 05:35 UTC)

<p>It was HP Sure Sense (detect malicious files and prevent malware)</p>

---
