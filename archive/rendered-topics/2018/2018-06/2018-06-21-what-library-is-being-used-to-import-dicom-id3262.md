---
topic_id: 3262
title: "What Library Is Being Used To Import Dicom"
date: 2018-06-21
url: https://discourse.slicer.org/t/3262
---

# What library is being used to import dicom?

**Topic ID**: 3262
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/what-library-is-being-used-to-import-dicom/3262

---

## Post #1 by @kayarre (2018-06-21 21:48 UTC)

<p>What library is being used on the backend to import dicom images?</p>
<p>The other libraries out there (gdcm, pydicom) don’t consistently work with jpg2000 formats.</p>
<p>What does 3D Slicer use?</p>

---

## Post #2 by @pieper (2018-06-21 22:29 UTC)

<p>Because DICOM is complex and not all types are supported by various libraries we actually include three main implementations.  ITK adds the jpeg2000 library for GDCM.  Through ITK we can use either GDCM or DCMTK (there’s an option to select that I realized was not <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#Advanced_options">on the wiki so I added it here</a>).  Some DICOM objects are read with pydicom.</p>
<p>There’s also a VTK DICOM reader that we don’t use bundled with VTK and another <a href="https://github.com/dgobbi/vtk-dicom">implementation by David Gobbi</a> that we don’t currently bundle but easily could if it solves any problems not addressed by the others.</p>

---
