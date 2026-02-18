# VMTK centrelines - stl format in ascii mode

**Topic ID**: 16058
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/vmtk-centrelines-stl-format-in-ascii-mode/16058

---

## Post #1 by @Dhaya (2021-02-18 12:09 UTC)

<p>I am new to VTMK software nad  have generated the centrelines in vtp format.</p>
<p>vmtksurfacereader -ifile “E:/geometry/v3_shortIliacExtendIMACAP_V2_vtmk.stl” --pipe vmtkcenterlines -seedselector openprofiles -ofile “C:/Users/Dhaya/surface_centerlines.vtp”</p>
<p>But I want the file in .stl format (ascii). Would any one help me to solve the problem?</p>

---

## Post #2 by @Dhaya (2021-02-18 12:11 UTC)

<p>I want to create a centerline for my patient specific geometry. I have successfully created in .vtp format using VMTK sotware.</p>
<p>code:</p>
<p>vmtksurfacereader -ifile “E:/geometry/v3_shortIliacExtendIMACAP_V2_vtmk.stl” --pipe vmtkcenterlines -seedselector openprofiles -ofile “C:/Users/Dhaya/surface_centerlines.vtp”</p>
<p>will it possible to create or convert to .stl format in ascii mode?</p>
<p>Note: The above generated .stl file is imported into the Ansys CFD Post.</p>
<p>Operating system: Windows 10<br>
Slicer version: VMTK 1.4.0 software<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #3 by @lassoan (2021-02-18 12:16 UTC)

<p>STL cannot store lines, only triangles. I would recommend to process the centerline data (extract data, write in any format you need) in Python - either by writing separate scripts or modifying existing PypeS scripts.</p>

---

## Post #4 by @chir.set (2021-02-18 12:33 UTC)

<p>Shouldn’t this request go to the VMTK mailing list ? It does not imply Slicer anywhere.</p>

---

## Post #5 by @lassoan (2021-02-18 12:37 UTC)

<p>Slicer forum hosts several other communities, such as pyRadiomics and VMTK. The author accidentally wrote to the Slicer category as well, probably because the post did not appear immediately due to moderation requirements for new users.</p>

---
