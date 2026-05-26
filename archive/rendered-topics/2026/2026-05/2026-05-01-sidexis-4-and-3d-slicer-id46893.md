---
topic_id: 46893
title: "Sidexis 4 and 3D Slicer?"
date: 2026-05-01
url: https://discourse.slicer.org/t/46893
last_bumped: 2026-05-04T19:46:02.218Z
---

# Sidexis 4 and 3D Slicer?

**Topic ID**: 46893
**Date**: 2026-05-01
**URL**: https://discourse.slicer.org/t/sidexis-4-and-3d-slicer/46893

---

## Post #1 by @drychen (2026-05-01 17:07 UTC)

<p>I can’t import the exported DICOM files from Sidexis 4 into my 3D slicer. I keep getting the following error message: 902: RawBlobs [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.</p>
<p>Does anyone have a solution?</p>

---

## Post #2 by @lassoan (2026-05-04 19:46 UTC)

<p>This means that there is no 3D information in the image. The series number (902) suggests that it is a post-processing result (original image series usually have series number below 100). Similarly, the <code>RawBlobs</code> series description indicates that it is a raw data dump that is only intended for the software that generated it (most likely Sidexis). The error message just indicates that Slicer could not confirm that the 3D geometry of the image it managed to load from this series is correct.</p>

---
