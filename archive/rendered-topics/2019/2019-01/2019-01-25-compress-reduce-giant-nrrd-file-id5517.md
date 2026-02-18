# Compress/reduce giant nrrd file

**Topic ID**: 5517
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/compress-reduce-giant-nrrd-file/5517

---

## Post #1 by @jxg (2019-01-25 17:24 UTC)

<p>Hello,<br>
First of all apologies if I’m posting this in the wrong place - let me know and I’m happy to change it. I’m very inexperienced with this software and radiological scans in general!<br>
I’m trying to render a volume from a very large .nrrd file (9GB) from a MicroCT. I’m having a lot of difficulty dealing with such a large file, and it’s proving difficult to manage. Is there any way to compress/reduce the file size? I’ve had the idea of converting it to a DICOM using the relevant module, and transferring it into a separate program to reduce it, but apparently an exception keeps being thrown whatever that means.<br>
Thanks for your help! And it’s great software to use for a broke student <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @muratmaga (2019-01-25 18:34 UTC)

<p>Compressing the file have no use for you in terms of 3D rendering performance. Reducing the resolution would help.</p>
<p>If you managed to get your scan successfully into Slicer, you can you use the crop volume to cut out the your region of interest and only render that part, which may help with rendering speed.</p>
<p>Or you can use the resampleScalarVolume module to reduce the size of your dataset.</p>
<p>How much memory our computer? Exceptions might be related to lack of memory to deal with such big dataset</p>

---

## Post #3 by @jxg (2019-01-25 19:00 UTC)

<p>Thanks for your response!</p>
<p>My computer has 8gb of RAM. So I think you’re right about the lack of memory. I’ve tried the Crop Volume function, but it’s not rendering anything in the 3d viewer, but I can explore that a bit more.</p>
<p>Could you explain how to use the resampleScalarVolume function? How would I halve the resolution using that?</p>

---

## Post #4 by @lassoan (2019-01-25 20:29 UTC)

<p>In general, you need 10x more memory space than size of your data set. Physical RAM is best, but if you cannot get 90GB physical RAM then configure 90 GB virtual memory in your system settings on Windows / swap space on Linux / simple free disk storage space on MacOS. Since disk is much slower (potentially hundreds of times slower) than RAM, everything will be very slow, but should eventually work.</p>

---

## Post #5 by @muratmaga (2019-01-28 05:45 UTC)

<p>You don’t need to turn on the 3D rendering for crop volume to work. You can define your region of interest using slice viewers, and then crop. To reduce the size of your of your volume, enable the interpolated cropping option and set the spacing scale something bigger than 1.00X (e.g., 2X will reduce each dimension by 2, resulting in a dataset 1/8th of the original).</p>
<p>Resamplescalarvolume does the same thing, but without the possibility of setting a ROI (whole volume will be reduced). Keep in mind in the resamplescalarVolume you type in the voxel spacing you want to achieve after resampling (e.g., if your original volume had voxel spacing of 0.010x0.010x0.010mm, you need to type in 0.02,0.02,0.02 in the spacing field, which will result in 50% reduction in each axis).</p>

---

## Post #6 by @tsehrhardt (2019-01-28 13:11 UTC)

<p>You could open the nrrd in Fiji/ImageJ to:</p>
<ol>
<li>remove unnecessary slices and/or</li>
<li>convert to 8-bit if that would still work for you.</li>
</ol>
<p>Since the file is so big, it’s might be more than 8-bit.</p>

---
