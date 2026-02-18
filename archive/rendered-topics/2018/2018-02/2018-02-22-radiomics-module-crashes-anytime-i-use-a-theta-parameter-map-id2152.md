# Radiomics module crashes anytime I use a "Theta parameter map"

**Topic ID**: 2152
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/radiomics-module-crashes-anytime-i-use-a-theta-parameter-map/2152

---

## Post #1 by @Andrea_Barucci1 (2018-02-22 18:57 UTC)

<p>Hi,<br>
good morning to everyone and sorry if my question has a solution in thread I have not found.</p>
<p>My problem is simple:<br>
Eveytime I’m trying to evaluate radionics features using a diffusion map obtained by the DWModeling, using the model “Gamma distribution”, “Theta parameter map”, 3D Slicer crash.</p>
<p>I have tried many times, closing all other maps, loading just the data necessary for this analysis, but I’m always encountering the same problem.</p>
<p>This sounds very strange because Radiomics module has been able to evaluate features with any diffusion model I’ve used, just with this map it crashes.</p>
<p>My operating system tell me that there is a memory problem.<br>
It’s very strange because the “Input Label Map” is always the same, and it comprise just a few points.</p>
<p>This is my version: 4.9.0-2018-01-14 r26833<br>
My computer is Apple Mac Book Pro.</p>
<p>Thank you very much for your support and thank you for developing this amazing software</p>

---

## Post #2 by @fedorov (2018-02-22 22:03 UTC)

<p>What is the scalar range that you see in the theta map? You can find it in the Volumes module as shown below. It might be that the output map contains NaN pixels which may not be handled properly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f5b98e5b4ec788ef76f588630acb6b1af5488b.png" data-download-href="/uploads/short-url/77XRggaWI4u68sZw7oaSSjRRXwn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f5b98e5b4ec788ef76f588630acb6b1af5488b_2_565x500.png" alt="image" data-base62-sha1="77XRggaWI4u68sZw7oaSSjRRXwn" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f5b98e5b4ec788ef76f588630acb6b1af5488b_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f5b98e5b4ec788ef76f588630acb6b1af5488b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f5b98e5b4ec788ef76f588630acb6b1af5488b.png 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×569 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Andrea_Barucci1 (2018-02-22 23:01 UTC)

<p>The range is very large.</p>
<p>Maybe this can be the problem?</p>
<p>There is a way to insert a threshold?</p>
<p>Thanks</p>
<p><img></p>

---

## Post #4 by @fedorov (2018-02-22 23:35 UTC)

<p>The range in my screenshot is the range for a different image. What is the reported range for your example? Can you share the theta map?</p>

---

## Post #5 by @Andrea_Barucci1 (2018-02-22 23:48 UTC)

<p>This is my map.<br>
The range in the screenshot I have sent before should be right.</p>

---

## Post #6 by @Andrea_Barucci1 (2018-02-23 09:59 UTC)

<p>Hi,<br>
Did you receive my email with data?</p>
<p>I can send you again my image with the label-map (Diffusion map-label.nrrd) I use to extract features.</p>
<p>Thank you very much</p>
<p>Andrea</p>

---

## Post #7 by @fedorov (2018-02-23 19:01 UTC)

<p><a class="mention" href="/u/andrea_barucci1">@Andrea_Barucci1</a> no, I did not receive any images or screenshots from you.</p>

---

## Post #8 by @Andrea_Barucci1 (2018-02-24 09:10 UTC)

<p>I have sent you two times…<br>
Can I send using your private email or another method?</p>
<p>However yesterday I did some other data elaboration, and I discovered that the same crash problem I can encounter with other map, e.g. DDC map.</p>
<p>My opinion that the problem can come from the memory of my computer.</p>
<p>What do you think?</p>
<p>On Monday I will try these elaborations with a different computer.</p>
<p>Let me know what you think and how I can send you the data.</p>
<p>Thank you very much for your support</p>
<p>Best</p>
<p>Andrea</p>
<p>Andrea Barucci</p>

---

## Post #9 by @Andrea_Barucci1 (2018-02-25 16:55 UTC)

<p>Dear Andrey,</p>
<p>I have tried to send you .nrrd files but it’s impossible.<br>
I just insert here two screenshot of maps informations using the Volume Module.</p>
<p>K map in this case doesn’t crash when I use Radiomics module.<br>
However when I try to analyse  DDC map using Radiomics, 3DSlicer crashes.</p>
<p>Do you think that this problem can be due to the range of the map?<br>
Or is a problem of my hardware (not enough memory)?</p>
<p>Using the Radiomics Module I’m encountering this problem many times, often with DDC map, Theta parameter map, etc.<br>
All these maps have been evaluated using the DWI module.</p>
<p>Thank you very much for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd3c8b086aef78512369a386b6f646b8848cac6.png" data-download-href="/uploads/short-url/oETRVZaPshFAA1QaPM6vrwcPpoG.png?dl=1" title="DDC_map_Radiomics_Crash" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd3c8b086aef78512369a386b6f646b8848cac6_2_690x332.png" alt="DDC_map_Radiomics_Crash" data-base62-sha1="oETRVZaPshFAA1QaPM6vrwcPpoG" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd3c8b086aef78512369a386b6f646b8848cac6_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd3c8b086aef78512369a386b6f646b8848cac6_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd3c8b086aef78512369a386b6f646b8848cac6.png 2x" data-dominant-color="9B9A9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DDC_map_Radiomics_Crash</span><span class="informations">1257×605 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @JoostJM (2018-02-26 09:30 UTC)

<p><a class="mention" href="/u/andrea_barucci1">@Andrea_Barucci1</a>, PyRadiomics (which is the back end of the SlicerRadiomics extension) supports resegmentation. If so specified, it will exclude voxels outside a given range. The extension does not have GUI elements to set this though, so you’ll have to make a parameter file and supply that (if that is not possible on you version of slicer, you’ll need to install the latest stable release and re-install the SlicerRadiomics extension).<br>
See <a href="http://pyradiomics.readthedocs.io/en/latest/customization.html#feature-extractor-level" rel="nofollow noopener">here</a> (look for parameter <code>resegmentRange</code>) for the setting of resegmentation and <a href="http://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file" rel="nofollow noopener">here</a> for information on making a parameter file.</p>
<p>Alternatively, what you can also try is to extract features using the stand-alone version of PyRadiomics. If there is an error in PyRadiomics, it will also be displayed. See <a href="http://pyradiomics.readthedocs.io/en/latest/installation.html" rel="nofollow noopener">here</a> for instructions on how to install the stand-alone version of PyRadiomics and <a href="http://pyradiomics.readthedocs.io/en/latest/usage.html" rel="nofollow noopener">here</a> on how to use it.</p>

---

## Post #11 by @fedorov (2018-02-26 20:41 UTC)

<aside class="quote no-group" data-username="Andrea_Barucci1" data-post="9" data-topic="2152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andrea_barucci1/48/4105_2.png" class="avatar"> Andrea_Barucci1:</div>
<blockquote>
<p>I have tried to send you .nrrd files but it’s impossible.</p>
</blockquote>
</aside>
<p>You probably replied to the forum posts by email with attachments, and I don’t know if that works. The most reliable way to share sample datasets is to upload to Dropbox or similar, and include the link in the forum post.</p>

---

## Post #12 by @Andrea_Barucci1 (2018-03-01 13:57 UTC)

<p>Thank you very much for your kindness and help.</p>
<p>I will share here my dataset, just to let you check if you encounter the same problems in data analysis.</p>
<p>Dataset: <a href="https://drive.google.com/file/d/1P-5UKdr2YSlo3k5EX4nJkJRSdPhlxKxK/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1P-5UKdr2YSlo3k5EX4nJkJRSdPhlxKxK/view?usp=sharing</a></p>
<p>Thank you very much</p>

---

## Post #13 by @fedorov (2018-03-01 16:10 UTC)

<p>When I click the link I get the error below.</p>
<p>Make sure you do not have any patient information in your dataset before sharing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8a7d5040263d38e7937bc15837f7700b68f67a.png" data-download-href="/uploads/short-url/fllNHS4RmjmMzbxCZsedydVRAaS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8a7d5040263d38e7937bc15837f7700b68f67a_2_690x335.png" alt="image" data-base62-sha1="fllNHS4RmjmMzbxCZsedydVRAaS" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8a7d5040263d38e7937bc15837f7700b68f67a_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8a7d5040263d38e7937bc15837f7700b68f67a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8a7d5040263d38e7937bc15837f7700b68f67a.png 2x" data-dominant-color="F5F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">749×364 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @Andrea_Barucci1 (2018-03-01 16:32 UTC)

<p>Now the dataset should be available.</p>
<p>There are no patient information in the dataset shared.<br>
The name of the folders are just “fictitious names” that I use to remember who is who.</p>
<p>Thank you very much</p>

---

## Post #15 by @fedorov (2018-03-01 17:42 UTC)

<p><a class="mention" href="/u/andrea_barucci1">@Andrea_Barucci1</a> I downloaded your dataset, but I am unable to move forward, since I discovered other related issues, and I cannot install Radiomics extension in either stable or nightly release… I will look into that when I have the setup.</p>

---

## Post #16 by @Andrea_Barucci1 (2018-03-02 18:25 UTC)

<p>Thank you very much.</p>
<p>In the last week I have encountered the same problems.<br>
Instead I’m using a Nightly version of January.</p>
<p>With the last versions of Slicer I’ve many troubles with all Slicer modules in general.<br>
I don’t know why.</p>
<p>I was wondering that was a problem of my computer.</p>

---

## Post #17 by @JoostJM (2018-03-07 09:44 UTC)

<p><a class="mention" href="/u/andrea_barucci1">@Andrea_Barucci1</a>, we created an <a href="https://github.com/Radiomics/pyradiomics/issues/354" rel="nofollow noopener">issue</a> on the PyRadiomics repository. I posted the cause and solution there.</p>

---

## Post #18 by @Andrea_Barucci1 (2018-03-07 16:13 UTC)

<p>Thank you very much for your help.</p>
<p>I have to download a new version of the Radiomics module?</p>

---

## Post #19 by @fedorov (2018-03-07 16:25 UTC)

<p>We also <a href="https://github.com/Radiomics/SlicerRadiomics/pull/44">committed the fix</a> to hopefully resolve the build issue for the Radiomics extension on mac. We will see tomorrow if that worked!</p>

---
