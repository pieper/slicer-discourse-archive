# Error when saving labelmap to jpg

**Topic ID**: 11630
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/error-when-saving-labelmap-to-jpg/11630

---

## Post #1 by @Emmanuel_Salinas_Mir (2020-05-20 04:35 UTC)

<p>Hi.<br>
I am working with JPG images:<br>
When I try to save a labelmap to any of the JPG or PNG formats I get this error:<br>
“Cannot write data file: /Users/xx/Documents/Segmentation-labe.jpg.<br>
Do you want to continue saving?”</p>
<p>I am in MAC. Slicer 4.10.</p>
<p>Slicer 4.11 preview crashes</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2020-05-22 15:16 UTC)

<p>Volumes cannot be saved into JPEG without information loss (JPEG can only store a single slice, cannot store spacing between slices, etc.). You can easily export a labelmap to JPEG as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files">example in script repository</a>.</p>
<p>If you ask this because you want to use these images for deep learning: do not use JPEG for temporarily storing image slices. Many people find some deep learning examples on the web that use JPEG (e.g., because they are originally developed by computer vision people, working on camera images), and assume that it is the right thing to do for medical images, but this is just very wrong. JPEG can only store 8-bit images (while many medical images becomes barely usable if you reduce their dynamic range to 8 bits), may introduce compression artifacts, slower to compress/decompress than plain numpy array npy files, and your machine learning library needs numpy arrays as inputs anyway. So, instead of compromising data by writing to disk as JPEG, write it directly as numpy array. You can get voxels of a volume as numpy array by calling <code>slicer.util.arrayFromVolume()</code> from Slicer’s Python console.</p>

---
