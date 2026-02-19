---
topic_id: 1175
title: "Create And Export 3D 4D Metadata"
date: 2017-10-05
url: https://discourse.slicer.org/t/1175
---

# Create and export 3D/4D metadata

**Topic ID**: 1175
**Date**: 2017-10-05
**URL**: https://discourse.slicer.org/t/create-and-export-3d-4d-metadata/1175

---

## Post #1 by @John_D (2017-10-05 01:35 UTC)

<p>Not sure if title is too clear, but imagine I want to mark specific locations in a 3D/4D dataset e.g. click on a tumour to mark it in 3D space (not segment it, just put a 3D marker on it). Then, I want to export this data which might be simply a list of name-XYZ pairs. Maybe in an ancillary file like an XML or JSON, to be consumed by some bespoke application that is nothing to do with DICOM.</p>
<p>Is this something Slicer can do with common modules/extensions? It seems like pretty basic application-development  stuff, but how the internals of Slicer fit together I don’t know!</p>

---

## Post #2 by @ihnorton (2017-10-05 02:23 UTC)

<p>Use the Markups module to place points. The list(s) may be exported as CSV (via ‘Save Data’); see module overview and format description here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#File_Format" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#File_Format</a></p>

---
