---
topic_id: 18165
title: "Creating An Automatic Us Vessel Segmentation Algorithm Using"
date: 2021-06-16
url: https://discourse.slicer.org/t/18165
---

# Creating an automatic US vessel segmentation algorithm using the Python interactor 

**Topic ID**: 18165
**Date**: 2021-06-16
**URL**: https://discourse.slicer.org/t/creating-an-automatic-us-vessel-segmentation-algorithm-using-the-python-interactor/18165

---

## Post #1 by @J.vd.Zee (2021-06-16 12:34 UTC)

<p>Hi all!</p>
<p>I would like to develop an automatic vessel segmentation algorithm in Python code based on the abdominal aorta.</p>
<p>Currently, I am stuck in the trial-and-error procedure since I really would like to avoid any manual operator interventions such as pointing seeds manually.</p>
<p>I tried the VTKVesselEnhancement module but didn’t succeed. Moreover, I couldn’t find the perfect filter operation.</p>
<p>Is anyone familiar with any gradient filter in which I could find the vessel in some pixels and perform some morphological or seed growing with these pixels as a starting point?</p>
<p>Your help is appreciated!</p>

---

## Post #2 by @lassoan (2021-06-17 02:06 UTC)

<p>Ultrasound image quality can be quite bad, with lots of noise and artifacts. In general, you cannot expect that any common image processing filter (even vessel enhancement filter) will be readily usable to detect features on ultrasound images. Do you work with a single 2D image, a sequence of 2D images, or 3D ultrasound volume? Can you post a few example images so that we have an idea about what kind of images do you have?</p>

---

## Post #3 by @J.vd.Zee (2021-06-17 14:59 UTC)

<p>Thanks for your reply! Really appreciated.<br>
The data that is collected intraoperatively, is comparable to the attached image. The major problem in Slicer for automatic segmentation is to find a morphological operation that is capable of detecting a single vessel shaped structure. I tried some simple conventional operations in the following order: thresholding → Gaussian filtering → Median filtering. This result in sort of binary image.</p>
<p>The data we collected is both 2D and 3D reconstructed US volume. Currently, I’m working on the 2D US images alone.<br>
Source of image: <a href="https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/uog.15942" rel="noopener nofollow ugc">https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/uog.15942</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1659aa0a27d40a66707064554675af6517d94d10.png" alt="Slicer_forum_1" data-base62-sha1="3bIBLbCGJF2m5ZmMg8QXIFx67vO" width="577" height="385"></p>

---

## Post #4 by @lassoan (2021-06-17 15:51 UTC)

<p>You cannot extract these vessels using basic image filtering, but seems like an easy task for deep learning. You “just” need to segment a few thousand slices and train a network.</p>
<p>During the <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/">upcoming Slicer Project Week #35</a> we’ll work with MONAI, NVidia, and PerkLab engineers and researchers (<a class="mention" href="/u/diazandr3s">@diazandr3s</a> <a class="mention" href="/u/sachidanandalle">@SachidanandAlle</a> <a class="mention" href="/u/ungi">@ungi</a> <a class="mention" href="/u/rebeccahisey">@RebeccaHisey</a>) to make it easier to segment ultrasound image sequences (both with and without position tracking) with <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a>, which will be very useful for streamlining this initial manual segmentation and test the performance the network as you go. You are welcome to join this work during the project week or catch up after the project week and see what you can use from what we develop.</p>

---

## Post #5 by @ungi (2021-06-17 19:57 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> says, there are a couple of examples using deep learning and U-Net showing that this problem can be solved. I think about 8-10 scans with about a hundred manually annotated images from each scan could be enough to achieve good accuracy. But of course the more the better. It could be done in a few days since all software pieces to do this is already available and they work in 3D Slicer. I’m happy to help if you decide to do it either at the project week or another time.</p>

---

## Post #6 by @diazandr3s (2021-06-18 10:23 UTC)

<p>Happy to help with creating the MONAILabel App for this use case.</p>

---

## Post #7 by @J.vd.Zee (2021-06-18 14:12 UTC)

<p>Hi <a class="mention" href="/u/ungi">@ungi</a>! thanks again for your reply.</p>
<p>That sounds interesting! I have US-series of six acquisitions that include about 300 images each. Would that be enough for building a deep learning? We might need to involve some augmented data to enlarge the available data set. Do you have a link to a tutorial or related work, so I can check the feasibility?<br>
The project week would be bit too late to be honest. Therefore, your help is really welcome.</p>

---

## Post #8 by @ungi (2021-06-18 17:42 UTC)

<p>Are your ultrasound scans recorded as Slicer sequences? If not, first we need to find a way to import them into Slicer. Could you check what file format are they saved in? And how are files organized?</p>

---

## Post #9 by @J.vd.Zee (2021-06-21 07:48 UTC)

<p>All the files are saved both in .mhf and the corresponding .zraw formats.<br>
I already succeeded to import the files into Slicer with:<br>
[success_I, masterVolumeNode_I] = slicer.util.loadVolume(‘C:/Users … .mhd’,returnNode=True)</p>

---

## Post #10 by @ungi (2021-06-21 19:08 UTC)

<p>That way, your images are loaded as a single 3D volume. But you have a time-series of 2D images, so the third dimension should be interpreted as time, right? If you can share a sample scan file pair (e.g. paste a Dropbox link in this conversation), we could see if there is an option to treat the third dimension as time. If not, it should be simple to convert your 3D volume to a sequence of 2D images.<br>
FYI, Slicer has a modified version of the mhd file format, called sequence metafile. Those can be loaded directly as sequences using this command: slicer.util.loadNodeFromFile(fullpath, ‘Sequence Metafile’)<br>
But probably your modules are sequence metafiles (yet).</p>

---

## Post #11 by @Marijn_H (2021-08-09 08:47 UTC)

<p>Hi all!</p>
<p>I am working with J.vd.Zee on this project and we have collected some more US data in the past few months. Now we have recorded the data directly in Slicer using the sequence module. So we have 2D US images, which are transformed to the correct position using the tracking system information in time. I think I have enough data to train a neural network, as a first feasibility test, and I would really appreciate your help with this!</p>
<p>Do you have a tutorial or manual (maybe from the project week) on how to do this using the software pieces that are already available in Slicer? Thanks a lot for your help!</p>

---

## Post #12 by @whu (2022-10-19 02:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="18165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>few thousand slices and train a network</p>
</blockquote>
</aside>
<p>Hi, did you finish the US vessel segmentation latter ?   I  met the same request .  Please share some solutions.  Thanks.</p>
<p>The US images are extracted from the MP4 video through the US device.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48360610a042d12f84249d85158be4e39629f3e7.jpeg" alt="5" data-base62-sha1="aiO7DbraTfGEIHKu3s2iaekoMkf" width="240" height="416"></p>

---
