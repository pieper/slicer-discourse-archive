---
topic_id: 5639
title: "Echograph For 3D Model"
date: 2019-02-05
url: https://discourse.slicer.org/t/5639
---

# Echograph for 3d model

**Topic ID**: 5639
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/echograph-for-3d-model/5639

---

## Post #1 by @jhonny422 (2019-02-05 00:17 UTC)

<p>Hi guys, What are the most known brands of ecographic equipment to obtain the 3D model? I tried with logiq s7 expert and ecube alpinion and I do not have satisfactory results, I only get 1 dcm file and I can not create 3D.</p>

---

## Post #2 by @pieper (2019-02-05 02:11 UTC)

<p>Making 3D models from ultrasound is a complex topic.  The SlicerHeart extension has some support for natively 3D probes from Philips but most ultrasound is collected as a freehand set of frames with no tracking.  Unless you have coherent 3D data Slicer won’t be much help.</p>

---

## Post #3 by @lassoan (2019-02-05 04:15 UTC)

<p>There are a number of machines that can acquire 3D volumes but usually the problem is to retrieve the images from the device (usually proprietary file format is used) - see <a href="https://github.com/SlicerHeart/SlicerHeart" rel="nofollow noopener">SlicerHeart</a> extension for a few available converters, as suggested above.</p>
<p>If the subject is not moving then you can attach a position tracker to the regular 2D probe and reconstruct a volume from the acquired slices. See <a href="http://www.slicerigt.org/wp/" rel="nofollow noopener">SlicerIGT</a> and <a href="http://www.plustoolkit.org" rel="nofollow noopener">Plus toolkit</a> volume reconstruction examples.</p>
<p>What would you like to take a 3D image of?</p>

---

## Post #4 by @jhonny422 (2019-02-06 02:50 UTC)

<p>Hello and thank you all for responding, I want to print a baby of 25 weeks, after testing with more than 20 files, the only one that worked for me is the .vol format with the HeartSlicer extension, I have to continue working on the process but I think that initially is a success, I still have to learn how to do the reconstruction and fill some holes, it would be incredible to reconstruct part of the head, at this moment it is only a mask.!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cbfe8915b3b90ea5b4aea69fab662c8c5046113.jpeg" alt="image" data-base62-sha1="46kwVOquyQD3w8U28yn7f36CpDJ" width="412" height="465"></p>

---
