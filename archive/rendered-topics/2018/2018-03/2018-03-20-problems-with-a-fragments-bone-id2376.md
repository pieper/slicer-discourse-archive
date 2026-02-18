# Problems with a fragments bone

**Topic ID**: 2376
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/problems-with-a-fragments-bone/2376

---

## Post #1 by @Patrycja_Grygny (2018-03-20 13:32 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
I have a cremation material which is located in the Popiel during the Pomeranian culture period. Itry to crop a fragments and do 3D. The program doesn’t see a single bones. Ceramics ashtray treats as bones. In small fragments he doesn’t read at all.<br>
How can I deal with it? Anyone have an idea?<br>
Please help.</p>

---

## Post #2 by @lassoan (2018-03-20 16:02 UTC)

<p>You can adjust brightness/contrast of the image by holding down the mouse left button and dragging it on the image up/down and left/right.</p>
<p>For volume visualization, go to Volume rendering module, select a volume rendering preset, and adjust the “Shift” slider.</p>
<p>For high-quality 3D visualization you may need to segment your volume using Segment Editor. See tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a>.</p>

---
