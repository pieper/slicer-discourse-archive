---
topic_id: 5260
title: "How To Import All Dicom Files Into One Volume"
date: 2019-01-03
url: https://discourse.slicer.org/t/5260
---

# How to import all dicom files into one volume

**Topic ID**: 5260
**Date**: 2019-01-03
**URL**: https://discourse.slicer.org/t/how-to-import-all-dicom-files-into-one-volume/5260

---

## Post #1 by @TingtingYu (2019-01-03 08:13 UTC)

<p>Hi,</p>
<p>I have a binary file contains volumetric information and its format was converted into DICOM format. Each .dcm  file contains one-slide information. Then I imported all these dicom files, however, each slide was shown as a volume. Could you please show me how to import these DICOM files and form only one 3D volume? Thanks in advanced.</p>
<p>Best wishes,<br>
Tingting</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0da4104db85a464379521d2c601e44de0f14bd60.png" alt="image" data-base62-sha1="1WFI8HF4g5sUsLKsRNUP5XV2MjC" width="518" height="394"></p>

---

## Post #2 by @pieper (2019-01-03 14:33 UTC)

<p>Creating valid dicom data can be tricky - you may be better off trying to load the original volume data.  If you can share the data or provide more information about it we might be able to help.</p>

---

## Post #3 by @lassoan (2019-01-03 15:45 UTC)

<p>It seems that you have selected multiple files. When you load DICOM data, drag-and-drop the containing <em>folder</em> to the Slicer application screen and not individual files. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" rel="nofollow noopener">DICOM module documentation</a> for detailed instructions.</p>

---

## Post #4 by @TingtingYu (2019-01-04 14:21 UTC)

<p>Hi Steve,</p>
<p>Thank you for your quick reply. Below is the link that shares binary file. The grid size is 256x256x152.</p>
<p><a href="https://drive.google.com/file/d/1kiWJX9rBdzH00v_Sa27b10HOOVTgWHjG/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/1kiWJX9rBdzH00v_Sa27b10HOOVTgWHjG/view?usp=sharing</a></p>
<p>Best,<br>
Tingting</p>

---

## Post #5 by @TingtingYu (2019-01-04 14:32 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. I dragged and dropped the folder to the Slicer application screen. But it still show the same problem.</p>
<p>Best,<br>
Tingting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d397ba8f8d9c62088804e4581e3b57a3d704f73.png" data-download-href="/uploads/short-url/6s4DRObidrkzcda55P6Er8a6gZZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d397ba8f8d9c62088804e4581e3b57a3d704f73_2_690x372.png" alt="image" data-base62-sha1="6s4DRObidrkzcda55P6Er8a6gZZ" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d397ba8f8d9c62088804e4581e3b57a3d704f73_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d397ba8f8d9c62088804e4581e3b57a3d704f73_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d397ba8f8d9c62088804e4581e3b57a3d704f73.png 2x" data-dominant-color="EFF1F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×737 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2019-01-04 14:49 UTC)

<p>Hi <a class="mention" href="/u/tingtingyu">@TingtingYu</a> -</p>
<p>It does appear that the dicom files haven’t been converted properly.  To load as a volume they would need to all be in the same study and series.</p>
<p>I would have a look, but the .bin file you posted won’t open for me.  Can you post a .zip instead?</p>
<p>-Steve</p>

---

## Post #7 by @lassoan (2019-01-04 15:36 UTC)

<p>You might be able to fix these invalid files using DICOM Patcher module, by enabling “Force same patient name and ID in each directory” option.</p>

---

## Post #8 by @TingtingYu (2019-01-07 02:42 UTC)

<p>Hi Steve,</p>
<p>Thank you for your help. No problem. Below is the .zip file.</p>
<p><a href="https://drive.google.com/file/d/1wmWkbIqVuBBTiXpX6z3pNVmWYJAJ863E/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/1wmWkbIqVuBBTiXpX6z3pNVmWYJAJ863E/view?usp=sharing</a></p>
<p>Best,<br>
Tingting</p>

---

## Post #9 by @TingtingYu (2019-01-07 02:51 UTC)

<p>Hi Andras,</p>
<p>Thank you for helping me.<br>
I tried the DICOM Patcher Module, but it still did not work. It gave me the warning below.</p>
<p>Best,<br>
Tingting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9aafb6ae71bcb9a0c5c7fbadc65e6d275945c84.png" data-download-href="/uploads/short-url/zCFduswGXf7TEFzaWe8mlZDVLPC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9aafb6ae71bcb9a0c5c7fbadc65e6d275945c84.png" alt="image" data-base62-sha1="zCFduswGXf7TEFzaWe8mlZDVLPC" width="479" height="500" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">565×589 17.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2019-01-07 03:03 UTC)

<p>The yip file contains a single “xcat-TrunPhanLesn-atn.bin” file in a file format that I don’t recognize. Please zip the folder that contains the DICOM files and send that.</p>

---

## Post #11 by @TingtingYu (2019-01-07 03:45 UTC)

<p>Hi Andras,</p>
<p>Below is the link that shares zipped folder containing DICOM files.</p>
<p><a href="https://drive.google.com/file/d/1PCokDgtJUViGLLEw5Z4QCIURvia0qP0R/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1PCokDgtJUViGLLEw5Z4QCIURvia0qP0R/view?usp=sharing</a></p>
<p>I also share how I converted the format, it might help you read the .bin file.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c72d6137d4614ac2a0faae2e2fe58cc8582d6075.png" alt="image" data-base62-sha1="sq0f1pxj9UOwmZFqEgL3c8Bn6y9" width="483" height="315"></p>
<p>Best,<br>
Tingting</p>

---

## Post #12 by @lassoan (2019-01-07 04:01 UTC)

<p>You cannot create valid DICOM files like this. There are a number of required DICOM fields that you must set correctly (patient name, patient ID, series instance UID, image position patient, image orientation patient, etc). If you don’t want to learn how to create valid DICOM files then you can use using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" rel="nofollow noopener">nrrdwrite.m</a> to save the voxel array as .nrrd file that you can directly load into Slicer.</p>

---

## Post #13 by @TingtingYu (2019-01-07 11:34 UTC)

<p>Hi Andras,</p>
<p>Thank you very much! It works.</p>
<p>Best wishes,<br>
Tingting</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59cfa29e85fdc49693d19330b6d231f815fc3cad.png" alt="image" data-base62-sha1="cOvlMoZsDzaZFr75waQfeaiUbmd" width="286" height="89"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b241674096e3dcf52f3584a29d8a751ee318b2f.png" data-download-href="/uploads/short-url/aIJ7VqfjdYp1qoiAVx3lcwue4G3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b241674096e3dcf52f3584a29d8a751ee318b2f_2_669x500.png" alt="image" data-base62-sha1="aIJ7VqfjdYp1qoiAVx3lcwue4G3" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b241674096e3dcf52f3584a29d8a751ee318b2f_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b241674096e3dcf52f3584a29d8a751ee318b2f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b241674096e3dcf52f3584a29d8a751ee318b2f.png 2x" data-dominant-color="58575D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">873×652 82.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
