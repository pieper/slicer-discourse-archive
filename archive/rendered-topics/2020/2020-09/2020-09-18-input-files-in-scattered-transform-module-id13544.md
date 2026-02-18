# Input files in Scattered Transform module

**Topic ID**: 13544
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/input-files-in-scattered-transform-module/13544

---

## Post #1 by @aseman (2020-09-18 12:47 UTC)

<p>Hi 3D Slicer experts and all<br>
I have 2 images (CT and MRI), which MRI  image is with distortion. I want to calculate the B-Spline Transform, using Scattered Transform module. which one do I insert for “file with initial point positions” of input files panel, (CT or MRI)?<br>
Thanks a lot</p>

---

## Post #2 by @aseman (2020-10-03 18:58 UTC)

<p>HI 3D Slicer experts<br>
Unfortunately, I did not receive any feedback on my question. I think that CT image, which is without distortion, should be inserted for “file with initial point positions”. is this true? can you help me with this question?<br>
Thanks a lot</p>

---

## Post #3 by @lassoan (2020-10-03 22:22 UTC)

<p>Scattered transform module converts a set of landmark displacements to a regular bspline grid. No images are used. If you want to register images to compute a transform then you can use “General registration (BRAINS)” module or “General registration (Elastix)” module (provided by SlicerElastix extension).</p>

---

## Post #4 by @aseman (2020-10-21 20:08 UTC)

<p>Hi<br>
I’ve been using the scattered Transform module in Slicer 4.7.0-2017-09-13 to create B- Spline matrix for a while, but recently it seems broken. I have 2 .txt files of more than 20 thousand points and every time I insert them in the Input files section, the process ends up with an error like  " the scattered transform module encountered with the serious problem". I want to know is there sth wrong with it? and how can I fix this problem?  can you help me?<br>
By the way, I tried this module in some other version of Slicer, but the outcome was the same.<br>
Thanks a lot</p>

---

## Post #5 by @lassoan (2020-10-21 20:12 UTC)

<p>Can you provide an example data set that reproduces the issue?</p>

---

## Post #6 by @aseman (2020-10-22 19:36 UTC)

<p>Hi<br>
This is an example of two sets of points in CT  and MRI that I expect scattered transform to create BSpline matrix of them.<br>
Thanks a lot</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e76f68f1eb3c072cf2423345635ba60c9ffede1.jpeg" alt="MR and CT points" data-base62-sha1="8UAtMXNjLOEhLcwI9seDhNAvDTb" width="441" height="366"></p>

---

## Post #7 by @lassoan (2020-10-22 21:10 UTC)

<p>Please upload the files somewhere and post the link here. Use a file format that Slicer can directly load.</p>

---

## Post #8 by @aseman (2020-10-24 19:27 UTC)

<p>Hi<br>
These are the CT and MR data links that have been uploaded.</p>
<p><a href="https://uupload.ir/filelink/RjrHINoGt5Gg/1u1r_pointsintersectionct.txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://uupload.ir/filelink/RjrHINoGt5Gg/1u1r_pointsintersectionct.txt</a><br>
<a href="https://uupload.ir/filelink/wx9AHwCeijql/7bsw_pointsintersectionmr.txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://uupload.ir/filelink/wx9AHwCeijql/7bsw_pointsintersectionmr.txt</a><br>
Also, I have another question. Formerly when I used slicer 4.7, the residual number at the end of the process was not the same in different versions of slicer(4.8 or 4.10 for instance). why this happens and which residual number is correct? higher or lower?<br>
Thanks a lot</p>

---

## Post #9 by @aseman (2020-11-02 19:34 UTC)

<p>Hi 3D Slicer experts and all<br>
Unfortunately, I didn’t receive any feedback. Previously, as I mentioned, I use Scattered Transforms module to Creat Bspline matrix in Slicer 4.7 . I have 2 .txt files of mere than 20 thousand points and every time I insert them in the Input files section, the process ends up with an error.<br>
1- can you help me about the reason of this problem?<br>
Also, the residual number at the end of the process is not the  same in different versions of slicer.<br>
2- Can you tell me what is the reason of this difference?<br>
Finally, I put the link of my CT and MRI data here again.</p>
<p><a href="https://uupload.ir/filelink/w8SKqrRr4wWd/1u1r_pointsintersectionct.txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://uupload.ir/filelink/w8SKqrRr4wWd/1u1r_pointsintersectionct.txt</a><br>
<a href="https://uupload.ir/filelink/etcljQ20qsDc/7bsw_pointsintersectionmr.txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://uupload.ir/filelink/etcljQ20qsDc/7bsw_pointsintersectionmr.txt</a></p>
<p>Thanks a lot</p>

---

## Post #10 by @lassoan (2020-11-02 20:15 UTC)

<p>I ran the module with default parameters (latest stable, Slicer-4.11.20200930, Windows 10) and got 0.00414063 residual error. The displacement field qualitatively looked good. I haven’t checked how well the field matches the two pointsets, you can do that to confirm that everything works well.</p>
<p>The residual error is typically computed as the mean distance between fixed points and transformed moving points. Smaller value is the better, if it is a magnitude lower than your total system error then you can consider it as negligible.</p>
<p>Since the method performs floating point computations, so small differences are expected depending on compiler versions, runtime libraries, etc., but these differences should not be significant.</p>

---
