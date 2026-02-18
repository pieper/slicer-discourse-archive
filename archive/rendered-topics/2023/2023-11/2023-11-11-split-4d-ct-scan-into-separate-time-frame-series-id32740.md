# Split 4D CT scan into separate time frame series

**Topic ID**: 32740
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/split-4d-ct-scan-into-separate-time-frame-series/32740

---

## Post #1 by @LindaV (2023-11-11 13:27 UTC)

<p>Hello,</p>
<p>First I would like to say that I am very impressed with all the functionalities of 3D Slicer. I am new to Slicer, so I hope I get the terminology right. For my project I am working with a 4D CT scan. Slicer can read in these files and I can see al the different timesteps. For my project, I would like to split the folder with all the DICOM files into separate folders with a folder per timestep. Up till now I am unable to find which metadata is used to split the files to know which file belongs to which timestep. Since Slicer knows this (as it can read in the files perfectly), I was wondering how this is achieved?<br>
Or is it possible in 3D Slicer to save one timestep for further processing?<br>
Thank you for your help.</p>

---

## Post #2 by @pieper (2023-11-11 14:45 UTC)

<p>You might try going into Advanced mode in the DICOM module.  After clicking Examine you can look at the list of loadable items and probably you will see the way they are broken down by tags.  Once you know the tag you could use a tool like <a href="https://github.com/pieper/dicomsort">dicomsort</a> to organize your files into folders according to the tags.</p>

---

## Post #3 by @LindaV (2023-11-16 14:45 UTC)

<p>Thank you for your reply. In advanced mode I get a list with my CT - 11 frames Multivolume by CardiacCycle and  my CT - 11 frames Volume sequence by CardiacCycle. But clicking “examine” does not seem to do anything. It gives a pop up that it is processing, but after that it just disappears. Where can I see the way they are broken down by tags?</p>

---

## Post #4 by @pieper (2023-11-16 15:03 UTC)

<p>The Examine button gives you a list of options for loading the data.  You can check the boxes by the version of loading you want to use.</p>
<aside class="quote no-group" data-username="LindaV" data-post="3" data-topic="32740">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/ccd318/48.png" class="avatar"> LindaV:</div>
<blockquote>
<p>Where can I see the way they are broken down by tags?</p>
</blockquote>
</aside>
<p>I’m sure I understand what you are asking.  That is exactly the information that should be in the advanced panel.</p>

---

## Post #5 by @LindaV (2023-11-16 15:11 UTC)

<p>Then I don’t understand what the tags are that I can see in the advanced mode. I have an 11 frames volume sequence and an 11 frames multivolume. But I don’t understand how this gives me information to sort the files.</p>

---

## Post #6 by @pieper (2023-11-16 19:58 UTC)

<p>I don’t have any time series dicom data in front of me at the moment, but as I recall the multivolume and sequence plugins tell you what they split the series by.  Also the scalar volumes offered in advanced mode it should offer one volume for each tag it’s split on as part of the name.</p>
<p>Also if you go to the Application Settings and enable “Allow loading subseries by time” maybe you will get the information you are looking for.  Maybe that’s what you are looking for:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3314fbcb2672c7eb9e2cc62039d96b18b23c90ba.png" data-download-href="/uploads/short-url/7hTj6gnQU9LY7OJRwpvR3PO8SFQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3314fbcb2672c7eb9e2cc62039d96b18b23c90ba_2_690x195.png" alt="image" data-base62-sha1="7hTj6gnQU9LY7OJRwpvR3PO8SFQ" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3314fbcb2672c7eb9e2cc62039d96b18b23c90ba_2_690x195.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3314fbcb2672c7eb9e2cc62039d96b18b23c90ba.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3314fbcb2672c7eb9e2cc62039d96b18b23c90ba.png 2x" data-dominant-color="D5D9DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">972×276 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @LindaV (2023-11-19 10:42 UTC)

<p>Thank you again for your reply. I’ll try using the plug-ins and the “allow loading subseries by time”.</p>

---
