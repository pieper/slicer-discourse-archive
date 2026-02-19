---
topic_id: 26859
title: "Vol File From Ultrasound To Stl File"
date: 2022-12-20
url: https://discourse.slicer.org/t/26859
---

# .VOL file from ultrasound to STL file?

**Topic ID**: 26859
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/vol-file-from-ultrasound-to-stl-file/26859

---

## Post #1 by @Edwin_Notebomer (2022-12-20 20:23 UTC)

<p>Hi everyone,</p>
<p>I’m really new to all this and I’m looking for a way to make an STL file from the .VOL file I got from my sister’s baby ultrasound.</p>
<p>I asked for a dicom file, but for some reason it was not possible.</p>
<p>My technical knowledge isn’t really great, but I hope someone here can help me.</p>
<p>Thanks for anyone willing to help.</p>

---

## Post #2 by @cpinter (2023-01-04 09:44 UTC)

<p>The problem with such proprietary formats is that they have their custom headers and it is not too straightforward to load it. Do you happen to know the manufacturer of the ultrasound that produced the file?</p>
<p>In any case you could try with this module: <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219" class="inline-onebox">New extension: RawImageGuess - for loading of images from unrecognized file format</a></p>
<p>Let us know how it goes.</p>

---

## Post #3 by @lassoan (2023-01-05 14:15 UTC)

<p>You can also try the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#loading-ge-kretz-ultrasound-images">.vol file reader in SlicerHeart extension</a>.</p>

---
