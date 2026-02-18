# How to save MRMLCore.vtkMRMLSequenceNode to a number of images

**Topic ID**: 20559
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/how-to-save-mrmlcore-vtkmrmlsequencenode-to-a-number-of-images/20559

---

## Post #1 by @Illusion (2021-11-10 03:33 UTC)

<p>Operating system:         Windows 10<br>
Slicer version:               4.13.0</p>
<p>Hello,</p>
<p>I am trying to write codes in Jupyter to convert a sequence of images to numpy array, in order to save the sequence to images.</p>
<p>Currently, I can get the MRMLCore.vtkMRMLSequenceNode using</p>
<pre><code class="lang-auto">im_seq_1 = slicer.util.getNode('Sequence_1_Im')
</code></pre>
<p>however, could not move forward.</p>
<p>Could anyone please let me know how should I convert <code>im_seq_1</code> or save it to images?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @lassoan (2021-11-10 03:59 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-voxels-of-a-4d-volume-as-a-single-numpy-array">This example</a> in the script repository should help.</p>
<p>What format would you like to write the image sequence to?</p>

---

## Post #3 by @Illusion (2021-11-10 04:09 UTC)

<p>Thank you so much, Andras! That example helps a lot!<br>
I would like to save as an uncompressed data format or raw data. Not sure which is better for viewing and editing yet.</p>

---

## Post #4 by @lassoan (2021-11-10 04:13 UTC)

<p>You can save the image sequence as an uncompressed raw file and a separate header file (you must have that to be able to interpret the data correctly) using File / Save. Choose “.seq.nhdr” file format, enable “Show options” and uncheck “Compress” option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/211e9b405f23277f492bed8c0b93a1e06dd400b7.png" data-download-href="/uploads/short-url/4IZkuBNG9uSRbqcYqI65iTRzuVp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/211e9b405f23277f492bed8c0b93a1e06dd400b7_2_690x241.png" alt="image" data-base62-sha1="4IZkuBNG9uSRbqcYqI65iTRzuVp" width="690" height="241" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/211e9b405f23277f492bed8c0b93a1e06dd400b7_2_690x241.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/211e9b405f23277f492bed8c0b93a1e06dd400b7_2_1035x361.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/211e9b405f23277f492bed8c0b93a1e06dd400b7_2_1380x482.png 2x" data-dominant-color="F6F6F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×668 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Illusion (2021-11-10 04:32 UTC)

<p>Thank you so much!</p>
<p>Just wondering is it possible to save to *.npy file, which is convenient for further processing?</p>

---

## Post #6 by @lassoan (2021-11-10 04:35 UTC)

<p>A numpy file does not store all metadata that must be preserved (such as image origin, spacing, axis directions, axis kinds, sequence axis type, name, unit, values), therefore I would recommend to use nrrd format. If you don’t need any metadata just the voxels as a numpy array then you can read the nrrd file using pynrrd.</p>
<p>What further processing would you like to do in what software?</p>

---

## Post #7 by @Illusion (2021-11-11 14:37 UTC)

<p>Thank you, Andras! The pynrrd can help a lot.</p>
<p>I would like to label two pixels for every single 2D image in the sequence, probably manually, not sure how to do it in an efficient way.</p>

---

## Post #8 by @lassoan (2021-11-11 14:56 UTC)

<p>Do you want to define two trajectories (nerves, vessels, etc.) running across the volume? If yes, then it is much faster to define that using a curve and then set the voxels from the curve points.</p>
<p>If you tell us about your overall goal then we can give advice on how to achieve that. It is important to make sure that the high-level workflow is good before discussing minor implementation details.</p>

---
