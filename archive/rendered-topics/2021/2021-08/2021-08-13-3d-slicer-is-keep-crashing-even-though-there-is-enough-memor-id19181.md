---
topic_id: 19181
title: "3D Slicer Is Keep Crashing Even Though There Is Enough Memor"
date: 2021-08-13
url: https://discourse.slicer.org/t/19181
---

# 3D slicer is keep crashing even though there is enough memory

**Topic ID**: 19181
**Date**: 2021-08-13
**URL**: https://discourse.slicer.org/t/3d-slicer-is-keep-crashing-even-though-there-is-enough-memory/19181

---

## Post #1 by @hourglassnam (2021-08-13 07:30 UTC)

<p>Hello,<br>
My computer has been keep crashing while using the 3D slicer program.<br>
During segmentation process, the program suddenly stops then my laptop turns off.<br>
I could not figure out why until I got this error message today.</p>
<blockquote>
<p>Slicer has caught an application error, please save your work and restart.</p>
<p>The application has run out of memory. Increasing virtual memory size in system settings or adding more RAM may fix this issue.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a></p>
<p>The message detail is:<br>
Exception thrown in event: bad allocation</p>
</blockquote>
<p>So my guess is that the program is not happy with my RAM.<br>
However, I can’t understand why this would happen because I do have enough space on my RAM and SSD.<br>
My dataset is about 4GB and my RAM is 64GB.<br>
I also have 860GB available on my SSD and my CPU is 11th Gen Intel(R) Core™ i7-11800H and GPU is RTX 3070.<br>
I also tried cropping the volume so I would have smaller file size but the program still crashed.</p>
<p>It seems to happen more often when I am using SkyscanReconImport to bring the files.<br>
This did not happened when I loaded files using the ImageStacks module.<br>
But because I can’t properly bring scale information with ImageStacks, I would like to use the SkyscanReconImport</p>
<p>Does anyone have any idea why this might have happened?<br>
Any help should be appreciated.<br>
Thank you.</p>

---

## Post #2 by @pieper (2021-08-13 12:33 UTC)

<p>Someone can probably help with this if you can provide a sample data file that reproducibly leads to a crash.</p>

---

## Post #3 by @muratmaga (2021-08-13 15:48 UTC)

<p>We will need the offending dataset to figure out the problem. However, you should know that SkyscanReconImport is less optimized than the ImageStacks in terms of memory usage.</p>
<p>Why do you think you cannot load the same files with ImageStacks with the correct scale information? All you have to do is to open the <strong>_rec.log</strong> file from find the image spacing (if you don’t already know) and enter that information prior to importing the dataset.</p>

---

## Post #4 by @lassoan (2021-08-13 19:53 UTC)

<p>What operating system do you use?</p>

---

## Post #5 by @hourglassnam (2021-08-16 08:05 UTC)

<p>Thank you always for your help!<br>
I didn’t realized I could find the image spacing from the log file.<br>
Thanks to you now I know how!</p>
<p>It does seems to work better with the ImageStack, since my computer doesn’t freeze anymore. However, the program still crash and turns off unexpectedly.</p>
<p>This actually happens with all my datasets.<br>
Here is one of my data sets which gave me the problem.<br>
<a href="https://drive.google.com/drive/folders/1_1pCp2UbC3NgNotUPGHCW_d6es3unP1M?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1_1pCp2UbC3NgNotUPGHCW_d6es3unP1M?usp=sharing</a></p>
<p>If this the program’s fault, then maybe there is something wrong with my computer.</p>

---

## Post #6 by @hourglassnam (2021-08-16 08:05 UTC)

<p>I am using Window 10!</p>

---

## Post #7 by @hourglassnam (2021-08-16 08:08 UTC)

<p>Thank you for your suggestion!<br>
I’ve attached dataset to the Mr. Muratmaga’s post now!</p>

---

## Post #8 by @muratmaga (2021-08-16 18:45 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="7" data-topic="19181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>I’ve attached dataset to the Mr. Muratmaga’s post now!</p>
</blockquote>
</aside>
<p>I have tried the provided dataset with SkyScanReconImport, and have no crash on my windows 10 laptop. It has got 32GB of ram and is running the stable version of Slicer. There are a whole bunch of log files in that folder, make sure to choose the correct one output by the Nrecon, <strong>hopum10__rec.log</strong>.</p>
<p>I also tried with ImageStacks and load the data successfully. Dataset is also not that big. I takes a about 20 seconds with ImageStacks to load the data and about 1min with SkyScanImport on a nvme disk. So the crashes you are facing are not related to SlicerMorph or the size of the dataset.</p>
<p>I would make sure:</p>
<ol>
<li>You are not loading data from a network share, where access speed can be variable.</li>
<li>You are choosing the correct log file when you are using the SkyscanReconImport</li>
</ol>
<p>If the issues persist, we will need the exact steps of where the crash is happening.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b53e7d43f615c47e225c5a60bab8af61a8e2b500.jpeg" data-download-href="/uploads/short-url/pRmiU1LZLJA12UMlKQg2oAfUA36.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b53e7d43f615c47e225c5a60bab8af61a8e2b500_2_690x434.jpeg" alt="image" data-base62-sha1="pRmiU1LZLJA12UMlKQg2oAfUA36" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b53e7d43f615c47e225c5a60bab8af61a8e2b500_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b53e7d43f615c47e225c5a60bab8af61a8e2b500_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b53e7d43f615c47e225c5a60bab8af61a8e2b500_2_1380x868.jpeg 2x" data-dominant-color="B0B3B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1800×1133 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note. I just noticed you have a VOI folder. Just to clarify, I only tested with the top level folder, which is the untouched output from the Nrecon software. SkyscanReconImport requires you to provide the unedited output. If you do want to use the VOI folder contents in Slicer, you definitely need to use the ImageStacks.</p>

---

## Post #9 by @hourglassnam (2021-08-26 09:46 UTC)

<p>Thank you so much for checking on my dataset.<br>
Without this community’s help, I probably won’t be able to continue my study.<br>
After your response, I called the store where I bought my new laptop, and they told me that I needed to download proper drivers for my CPU and GPU!<br>
So I did and tried using it for a week.<br>
I think I can say that solved the problem.<br>
My computer no longer turns off.<br>
The program does freeze from time to time, but it is usually when I connect my iPad to use as a tablet or when I mistakenly put in a large number for the smoothing tool.<br>
So as long as I am careful with these, I don’t have a big problem using the program.<br>
Again, thank you for your help!<br>
Have a great day!</p>

---
