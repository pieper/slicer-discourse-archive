# Does importing .jpg sequence instead of .png reduce ram requirements?

**Topic ID**: 9173
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/does-importing-jpg-sequence-instead-of-png-reduce-ram-requirements/9173

---

## Post #1 by @NoobForSlicer (2019-11-15 22:54 UTC)

<p>In other words, does Slicer 3D dismantle those images and insert them pixel by pixel with 8 bit channels (24 bits total) irrelevant of what format was used? Or does Slicer somehow preserve the format and thus Jpg sequence imported would require less ram?</p>

---

## Post #2 by @pieper (2019-11-16 13:24 UTC)

<p>No, png vs jpg compression only matters for storage to disk.  If the images are the same resolution they will take the same amount of memory once uncompressed.</p>

---
