---
topic_id: 43540
title: "Help Integrating Vtku3Dexporter Module In Slicer"
date: 2025-06-30
url: https://discourse.slicer.org/t/43540
---

# Help integrating vtkU3DExporter module in Slicer

**Topic ID**: 43540
**Date**: 2025-06-30
**URL**: https://discourse.slicer.org/t/help-integrating-vtku3dexporter-module-in-slicer/43540

---

## Post #1 by @alientex (2025-06-30 04:26 UTC)

<p>Hello,</p>
<p>I came across the <a href="https://github.com/Korijn/VTKU3DExporter" rel="noopener nofollow ugc">VTKU3DExporter</a> module, which allows exporting a VTK scene to the U3D file format. I would like to use the generated U3D file for including in 3D PDFs.</p>
<p>I have successfully built this module independently and tested it with a demo scene—it worked as expected. I’m now looking for an official way to integrate this module into Slicer.</p>
<p>I’m happy to provide more details about how I built the module independently.</p>
<p>Any help would be greatly appreciated.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2025-06-30 12:27 UTC)

<p>You could do this by making a SuperBuild extension so the C++ code and python wrappings are build and packaged for all platforms.  If this is a well-implemented VTK module that should be fairly straightforward.  You can look at other extensions to get ideas.</p>

---

## Post #3 by @jcfr (2025-06-30 15:17 UTC)

<p><a class="mention" href="/u/alientex">@alientex</a>  To follow-up, you should be able to integrate the module into your extension and/or custom application following an approach like the on used in <a href="https://github.com/KitwareMedical/SlicerVirtualReality">SlicerVirtualReality</a>.</p>

---

## Post #4 by @lassoan (2025-07-01 13:23 UTC)

<p>How do you create 3D PDF from this file?<br>
Can you post a link to an example 3D PDF that you generate from a segmentation?</p>
<p>Can the VTK exporter preserves colors, opacities, material properties, and scene lights?</p>
<p>Can you specify segment names that appear in the PDF viewer (similar to <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/README.md">OpenAnatomy glTF exports</a>)?</p>
<p>Does the exporter support multiple time points? Can your step through the time points one by one in the PDF viewer?</p>
<p>Can you specify clipping planes and edit them in the PDF viewer?</p>
<p>I’m mainly asking these to see how the PDF solution compares to existing solutions, such as <a href="http://3dviewer.net">3dviewer.net</a>, and how could it compete in the long term with a VTK-based viewer apps. Based on my limited experience and little reading on 3D PDF it seems to me that it is very limited, legacy technology (just barely hanging on, maintained but not improved for many years) and so a modern VTK-based viewer could work much better (it would work with open file formats, it would be extensible and customizable, it could reslice 3D images, do volume rendering, etc). Even just packaging <a href="http://3dviewer.net">3dviewer.net</a> as a mobile app would probably be a better 3D viewer than 3D PDF.</p>

---

## Post #5 by @pieper (2025-07-01 13:43 UTC)

<p>Also see this discussion: <a href="https://discourse.slicer.org/t/lighweight-zero-footprint-3d-slicer-viewer-wanted/29202" class="inline-onebox">Lighweight "zero footprint" 3D Slicer viewer wanted</a></p>

---
