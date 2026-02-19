---
topic_id: 28923
title: "Help Fill Between Slices Function Not Working Properly"
date: 2023-04-14
url: https://discourse.slicer.org/t/28923
---

# Help - "Fill between slices" - function not working properly

**Topic ID**: 28923
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/help-fill-between-slices-function-not-working-properly/28923

---

## Post #1 by @FPRO (2023-04-14 18:36 UTC)

<p>Since I am working with the 3D-Slicer there is a problem with the function “fill between slices”. I am marking muscle frames (not the whole muscle, only the frame around) and using the “fill between slices”, so i do not have to mark it in every segment, but the longer i am using the function, the bigger the frames are getting. I think it is related to the number of fillings the function is doing on it´s own, in the beginning it was fine but after round about 50 slices, the frames became bigger and bigger, so the frame is not very useful anymore.</p>
<p>Maybe there is someone who had a similar problem and found a solution to it.</p>
<p>Best regards</p>
<p>Operating system: Windows 11<br>
Slicer version: 5.2.2.<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2023-04-15 03:04 UTC)

<p>Can you attach a screenshot that shows what you mean by muscle frames?</p>
<p>Do you press “Apply” in</p>
<aside class="quote no-group" data-username="FPRO" data-post="1" data-topic="28923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fpro/48/65623_2.png" class="avatar"> FPRO:</div>
<blockquote>
<p>frames became bigger and bigger,</p>
</blockquote>
</aside>
<p>Getting bigger in what sense? Can you attach a few screenshots?</p>

---

## Post #3 by @FPRO (2023-04-15 10:55 UTC)

<p>Thank you for the quick reply!</p>
<p>I was pressing “initialize” and then apply. Maybe about 5-10 times while segmentating the data. In the attachment are the screenshots, I hope it becomes clear what I meant by “muscleframes”.<br>
these enlarged outlines came especially when I marked other structures. I suspect that with each use of the function, the outlines of the muscle have become slightly larger.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a270c52318bd13f00cfb06b454f67eeb59743df.png" alt="3D - before" data-base62-sha1="8irlUUZqICODsyhzJodPFSnOQWz" width="512" height="128"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab77a36ab6a51f3456fb3978ca42adb718b75954.png" alt="3D - after" data-base62-sha1="osRYe9m0Xbv8mioeGVJeSgXtP9i" width="612" height="155"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b03863f2ef5737878939a9e4bd03579dd41ed07.png" alt="axial - before" data-base62-sha1="3QYrrJgsa0ymB6dYGD99g5SPTan" width="346" height="70"></p>
<p>I send the last screenshot in an extra post, because as a new member I am only allowed to attach a maximum of three pictures.</p>
<p>Best regards</p>

---

## Post #4 by @FPRO (2023-04-15 10:57 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aac424fdfa8d4972937a63f217cb249f1501efc3.png" alt="axial - after" data-base62-sha1="omFpgVIYocIKGoUVlhH0I5yDRHZ" width="404" height="90"></p>
<p>The first two images are of the 3D model at an earlier and later stage of the work. The 3rd and 4th images are the corresponding axial sections.</p>

---

## Post #5 by @lassoan (2023-04-16 12:52 UTC)

<p>Fill between slices needs to find correspondence between points on different slices, which is very hard if you have thin, hollow structures.</p>
<p>However, you may not need to segment hollow structures. Instead, you can segment the muscle using <code>Fill between slices</code> and then use <code>Hollow</code> effect to get its “frame”.</p>

---

## Post #6 by @FPRO (2023-04-17 06:54 UTC)

<p>Thank you very much for your advice, i will try it as you recommended!</p>

---

## Post #7 by @Mehran (2023-04-17 08:58 UTC)

<p>Hi, recently we provided new method for filling between slices which works for thigh muscles. you may try and be useful for you.<br>
<a href="https://github.com/latimagine/SlicerSpline" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/latimagine/SlicerSpline</a></p>

---

## Post #8 by @FPRO (2023-04-17 11:50 UTC)

<p>hello, thank you very much for the feedback, unfortunately the link is not available. Is it an add-on?<br>
Best regards</p>

---

## Post #9 by @philippepellerin (2025-02-28 08:50 UTC)

<p>Hi Mehran, I followed your link to Github; your module looks great; congratulations.<br>
I am working on a Mac as a “final user” without much computer science skills.<br>
I saw that you ran it on Unbutu. I downloaded the package from GitHub, but I do not know what to do with it. Is there a way to run it on my Mac?<br>
If so, how can I do that?<br>
It would be great if we could find it in the extension manager.<br>
Thanks for any help</p>

---

## Post #10 by @philippepellerin (2025-03-02 15:43 UTC)

<p>Hi. I have contacted Mehran, who kindly helped me install the module, which I did succesfully.<br>
Unfortunately, I still have an issue. I get an error when I try to run the module (see the screen capture). It seems to be related to the “read-only” quality of the temporary folder, which is needed. It is an issue specific to macOS. I have allowed full drive access to the Slicer application, but it is still the same. I do not know where to look for the temporary folder, which I need to set to write and read.<br>
Could anyone help me with this one?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aff984b45c8ed53a6a870dd3344ea2522bea844.jpeg" data-download-href="/uploads/short-url/1zinP3kbPaMgtJg2xkhVNPcSPt2.jpeg?dl=1" title="Screenshot 2025-03-02 at 16.28.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0aff984b45c8ed53a6a870dd3344ea2522bea844_2_690x388.jpeg" alt="Screenshot 2025-03-02 at 16.28.17" data-base62-sha1="1zinP3kbPaMgtJg2xkhVNPcSPt2" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0aff984b45c8ed53a6a870dd3344ea2522bea844_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0aff984b45c8ed53a6a870dd3344ea2522bea844_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0aff984b45c8ed53a6a870dd3344ea2522bea844_2_1380x776.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-02 at 16.28.17</span><span class="informations">1920×1082 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
