# Uploading .VOX image

**Topic ID**: 12371
**Date**: 2020-07-04
**URL**: https://discourse.slicer.org/t/uploading-vox-image/12371

---

## Post #1 by @Angel (2020-07-04 06:47 UTC)

<p>Hello,</p>
<p>I have a .VOX image that I want to upload. Normally, I would convert the .VOX image into a stack of JPEGs, but it would be much more convenient to just upload it in the original format. Can I use the RawImageGuess Extension? What settings should I use in the extension? The image details are as follows:</p>
<p>VolumeSize 512 512 512</p>
<p>VoxelSize 16 microns</p>
<p>VolumePosition 0 0 0</p>
<p>VolumeScale 0.020 0.020 0.020</p>
<p>Thanks!!</p>

---

## Post #2 by @lassoan (2020-07-04 12:43 UTC)

<p>If the image is not compressed then you can load it with RawImageGuess. Do you have only a single image or you have a software that creates such files and you regularly want to open new files? What software creates Vox volume files? Do you have a reader in Python or C++ or specification of the format?</p>

---

## Post #3 by @Angel (2020-07-07 07:34 UTC)

<p>Hello,</p>
<p>I actually ended up figuring things out with the person I work with.</p>
<p>Thank you for your response!</p>

---

## Post #4 by @lassoan (2020-07-08 12:12 UTC)

<p>Would you mind letting us know what the solution was?</p>

---

## Post #5 by @Angel (2020-09-01 07:47 UTC)

<p>Sorry…I must have missed this message…but we stuck with using the JPEG stack for simplicity.</p>

---

## Post #6 by @Ishika_Ringania (2025-02-10 20:48 UTC)

<p>hey, could you elaborate on how you uploaded .vox file to the software</p>

---

## Post #7 by @Ishika_Ringania (2025-02-10 21:26 UTC)

<p>analyse 14 is the software provided along with perkin ehlmer quantumgx MicroCTscanner  which provides .vox ,</p>

---
