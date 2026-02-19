---
topic_id: 23761
title: "Can Vertex Colored Models Be Imported As Segmentations"
date: 2022-06-08
url: https://discourse.slicer.org/t/23761
---

# Can vertex colored models be imported as segmentations?

**Topic ID**: 23761
**Date**: 2022-06-08
**URL**: https://discourse.slicer.org/t/can-vertex-colored-models-be-imported-as-segmentations/23761

---

## Post #1 by @muratmaga (2022-06-08 04:09 UTC)

<p>See an example of vertex colored skull from MorphoSource. <a href="https://www.morphosource.org/concern/parent/000101191/media/000358488" rel="noopener nofollow ugc">https://www.morphosource.org/concern/parent/000101191/media/000358488</a></p>
<p>These were derived from CT scans, which are also available on M/S, but the segmentations are not. Would it be possible to import this model in a way that each color is a separate segment? Right now, it is importing everything as one element.</p>

---

## Post #2 by @pieper (2022-06-08 13:20 UTC)

<p>Some coding would be required, but the mesh could be split based on vertex colors and if they are closed surfaces they could be converted back to filled regions in a volume.</p>

---

## Post #3 by @mau_igna_06 (2022-06-08 14:47 UTC)

<p>Inthimk you cannuse vtkPolydataConnectivityFilter for that using your color scalar as one of the arguments.<br>
Then do a for loop of all componnents and use a vtkthreshold, wirh the geometry filter at the end.of the pipeline</p>
<p>Hope it helps</p>

---
