---
topic_id: 9141
title: "How To Open Nifti Gz Gz Files"
date: 2019-11-14
url: https://discourse.slicer.org/t/9141
---

# How to open NIFTI-GZ (.gz) files?

**Topic ID**: 9141
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/how-to-open-nifti-gz-gz-files/9141

---

## Post #1 by @NoobForSlicer (2019-11-14 07:51 UTC)

<p>The exact name of the image is: IMAGE01.rgb.gz</p>
<p>I found a lot about nii.gz, but what the hell is .rgb.gz?</p>
<p>Hmm…</p>

---

## Post #2 by @lassoan (2019-11-14 14:36 UTC)

<p>I haven’t seen such images yet. If you know that they are nifti images then try renaming them to .nii.gz and see if you can load them. If that fails then unzip them and have a look at it using an editor if the header looks familiar. If not then you can use RawImageGuess extension on the unzipped file to guess image parameters and load the file.</p>

---

## Post #3 by @NoobForSlicer (2019-11-14 15:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>nifti images then try renaming them to .nii.gz and see if you can load them. If that fails then unzip them and have a look at it using an editor if the header looks familiar. If not then you can use RawIm</p>
</blockquote>
</aside>
<p>from my understanding, .gz is a compression by gunzip or gzip?<br>
What would be the difference between gunzip and gzip?</p>
<p>Or .gz in this case means something else?</p>
<p>I managed to unzip them with Win rar… I have no clue what it unzipped, maybe that is now  where i made the mistake…</p>
<p>When I “unzip them” I am left with an .rgb file extension.</p>
<p>.rgb file is some old format used in the 90s <a href="https://en.wikipedia.org/wiki/Silicon_Graphics_Image" class="inline-onebox" rel="noopener nofollow ugc">Silicon Graphics Image - Wikipedia</a><br>
by company Silicon Graphics and that company apparently went bankrupt after cold war ended since they ran out out government contracts.</p>
<p>Now I tried opening .rgb with a whole lot of software, non of them worked. They all say “cant read header, wrong file type”</p>
<p>so I dont know now where the mistake happened…</p>
<ol>
<li>what does .gz mean</li>
<li>did it properly get extracted or it was some fault extraction by win rar</li>
<li>is the problem with opening the .rgb simply problem of not having software to open it… I found the ones in the internet that said they can open it.</li>
</ol>

---

## Post #4 by @lassoan (2019-11-14 15:20 UTC)

<p>gz means compressed with gzip. Most probably winrar unzipped it correctly. If it is a scalar image (with a single component) then you should be able to load it using RawImageGuess module. If it is RGB, as the name suggests, then RawImageGuess would need to be tuned a bit to accept RGB voxels, too. There is similar raw image import feature in ImageJ (it supports RGB images, but not live image preview, so it is a bit harder to guess the right image dimensions).</p>
<p>Where the image comes from? Can you share a sample?</p>

---

## Post #5 by @NoobForSlicer (2019-11-14 15:26 UTC)

<p>I’ll have to ask for a permission to share…I’ll do so tomorrow early morning…</p>
<p>But this isn’t a 3d image… this is a 2D image so those would be pixels, rather than voxels.</p>
<p>I wonder if there is some proper way to open the file and see what header in it says.</p>
<p>I am downloading ImageJ</p>

---

## Post #6 by @NoobForSlicer (2019-11-14 15:27 UTC)

<p>that’s the trouble picking up some governmental research from cold war era… no computers, no compatible software, weird file formats hahaha</p>

---

## Post #7 by @lassoan (2019-11-14 15:35 UTC)

<p>2D image should be no problem, as it is just a single-slice 3D volume.</p>

---

## Post #8 by @NoobForSlicer (2019-11-14 15:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc16e92a75828d89a3e3669dad92c711cc900c7c.jpeg" data-download-href="/uploads/short-url/qPUQJLzWK43h45Btjj7yU0fNTpG.jpeg?dl=1" title="bunch%20of%20nothing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc16e92a75828d89a3e3669dad92c711cc900c7c_2_524x500.jpeg" alt="bunch%20of%20nothing" data-base62-sha1="qPUQJLzWK43h45Btjj7yU0fNTpG" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc16e92a75828d89a3e3669dad92c711cc900c7c_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc16e92a75828d89a3e3669dad92c711cc900c7c_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc16e92a75828d89a3e3669dad92c711cc900c7c_2_1048x1000.jpeg 2x" data-dominant-color="EEEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bunch%20of%20nothing</span><span class="informations">1930×1840 612 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>HEre I tried to read it through some anayzer and it just gave me a bunch of random letters.</p>

---

## Post #9 by @NoobForSlicer (2019-11-14 15:46 UTC)

<p>Also yes .RGB files are indeed rgb type and there is possibility of .RGBA which basically adds alpha to the format.</p>
<p>but the one I have is definitely without alpha</p>

---

## Post #10 by @NoobForSlicer (2019-11-14 23:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>an load them. If that fails then unzip them and have a look at it using an editor if the header looks fami</p>
</blockquote>
</aside>
<p>can you please tell me how can i look at the header using the “editor” as you’ve previously said… I assume in the header we can see how it looks like</p>

---

## Post #11 by @NoobForSlicer (2019-11-14 23:47 UTC)

<p>Here I was given the same file type but not related to confidential research.</p>
<p>So we can exmine it: <a href="https://drive.google.com/open?id=1YfZWbj2MpUwDVt_Kt8q_83Z-PK-LEAwf" rel="nofollow noopener">https://drive.google.com/open?id=1YfZWbj2MpUwDVt_Kt8q_83Z-PK-LEAwf</a></p>
<p>Interestingly SGI not only had those files but they had computer machines which run those files and as name implies Silicone Graphics was a company that worked with graphics. So hard to believe technology gets so old and obsolete so quickly.</p>
<p>Here is a wider description of what the file format looks like:<br>
<a href="http://paulbourke.net/dataformats/sgirgb/sgiversion.html" class="onebox" target="_blank" rel="nofollow noopener">http://paulbourke.net/dataformats/sgirgb/sgiversion.html</a><br>
Written by a creator of the file format. He also gives a lot of functions how to decompress the file, whatever that means. He basically gives like 5-6  functions but I have no clue in which program he wrote those and how to utilize those anyway. I am a noob</p>

---

## Post #12 by @NoobForSlicer (2019-11-14 23:57 UTC)

<p><a href="http://paulbourke.net/dataformats/sgirgb/" class="onebox" target="_blank" rel="nofollow noopener">http://paulbourke.net/dataformats/sgirgb/</a><br>
I have found here how header should look like</p>
<p>Also I have found this:<br>
A straightforward C library that reads SGI RGB files: <a href="http://paulbourke.net/dataformats/sgirgb/readrgb.h" rel="nofollow noopener">readrgb.h</a> and <a href="http://paulbourke.net/dataformats/sgirgb/readrgb.c" rel="nofollow noopener">readrgb.c</a> and turns them into a 4 byte RGB and alpha channel.</p>
<p>hmm</p>

---

## Post #13 by @lassoan (2019-11-15 00:51 UTC)

<p>The SGI file at the download link is very different (compressed and does not have the same range of values) from the one you showed <a href="https://discourse.slicer.org/t/how-to-open-nifti-gz-gz-files/9141/8">above</a> (which looks like uncompressed pixel buffer). Probably .rgb just means that it is an RGB color file and has nothing to do with SGI.</p>
<p>To load the file, you can either follow the recommendations that I gave above or share a single example file.</p>

---

## Post #14 by @NoobForSlicer (2019-11-15 10:40 UTC)

<p>Just talked to my professor and he laughed at me…<br>
He said the files “may be shared” for such reasons it is nothing confidential nor so strict, it’s just we don’t have a permission to share in a way redistribute data publicly for other reasons.</p>
<p>Sorry for my initial misunderstanding Lassoan. I am just too careful not to break some rules, since I know he made us sight that we won’t “redistribute” bla bla bla… But clearly he didn’t mean something silly like this.</p>
<p>But I just tried what you said and it worked… it’s raw RGB data and not .RGB format from silicone graphics. I IMPRTED (not opened) the file as RAW image in imageJ program and chose resolution because I read the description file about resolution and I just chose randomly 24bi 32 bit 8 bit until it looked okay.</p>
<p>Amazing Lassoan… Sorry I made it harder for you to help me because I didn’t know what the actual data policy of my university is like.</p>
<p>Either way you saved my life at least 3-4 times so far.</p>
<p>So to conclude…<br>
.gz can be exported easily with win rar<br>
.rgb must not be a file with header that Paul has developed for Silicone Graphics but INSTEAD raw RGB data. This data can be opened with imageJ IF you know the resolution and how many bits the image should be 24 bit or 8 bit or 32 bit.</p>
<p>Hope that helps anyone who reads this thread in the future.</p>
<p>So here as promised I post the file</p>

---
