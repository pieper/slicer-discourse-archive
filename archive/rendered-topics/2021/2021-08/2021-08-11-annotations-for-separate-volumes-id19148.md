---
topic_id: 19148
title: "Annotations For Separate Volumes"
date: 2021-08-11
url: https://discourse.slicer.org/t/19148
---

# Annotations for separate volumes

**Topic ID**: 19148
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/annotations-for-separate-volumes/19148

---

## Post #1 by @caesarsalad (2021-08-11 02:45 UTC)

<p>Hello,</p>
<p>I have loaded multiple master volumes as shown:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5b90f6a51573d063c5df4b930d31a02fc70f071.png" data-download-href="/uploads/short-url/z3Lt8sSs7ESS2W8eHsEw8aL1A53.png?dl=1" title="Screen Shot 2021-08-11 at 11.44.04 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b90f6a51573d063c5df4b930d31a02fc70f071_2_690x144.png" alt="Screen Shot 2021-08-11 at 11.44.04 AM" data-base62-sha1="z3Lt8sSs7ESS2W8eHsEw8aL1A53" width="690" height="144" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b90f6a51573d063c5df4b930d31a02fc70f071_2_690x144.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b90f6a51573d063c5df4b930d31a02fc70f071_2_1035x216.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5b90f6a51573d063c5df4b930d31a02fc70f071.png 2x" data-dominant-color="CED8CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-11 at 11.44.04 AM</span><span class="informations">1058×222 84.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I wish to annotate each volume separately, ex) annotate a slice from volume 1 but have it stay in that volume and not affect volume 2. Is there a way to do this, or do the annotations apply for all volumes by default?</p>
<p>For example, this segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34da5397c95ea665cf9f27e63efc93937aefbb68.jpeg" data-download-href="/uploads/short-url/7xyADrFhJuRvyYG9VGl5dNkBTsc.jpeg?dl=1" title="Screen Shot 2021-08-11 at 11.45.32 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34da5397c95ea665cf9f27e63efc93937aefbb68.jpeg" alt="Screen Shot 2021-08-11 at 11.45.32 AM" data-base62-sha1="7xyADrFhJuRvyYG9VGl5dNkBTsc" width="631" height="500" data-dominant-color="673D37"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-11 at 11.45.32 AM</span><span class="informations">972×770 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>appears when I switch volumes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9f87d034721c6a0fa561c746416cc1121c589ba.jpeg" data-download-href="/uploads/short-url/ofD4JiuRTCWYFyDzWMwKWbO2cGK.jpeg?dl=1" title="Screen Shot 2021-08-11 at 11.46.00 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9f87d034721c6a0fa561c746416cc1121c589ba.jpeg" alt="Screen Shot 2021-08-11 at 11.46.00 AM" data-base62-sha1="ofD4JiuRTCWYFyDzWMwKWbO2cGK" width="690" height="472" data-dominant-color="6E3C2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-11 at 11.46.00 AM</span><span class="informations">1046×716 81.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your help.</p>

---

## Post #2 by @muratmaga (2021-08-11 04:14 UTC)

<p>You can create a new segmentation node for your second volume. Segmentations in that will be independent of the first volume.</p>
<p>However, visibility for all segmentation nodes are enabled by default, simply switching to a new one will not hide the previous one (if there are already segments with content in it).<br>
You can control this through the Data module (click the eye icon next to the segmentation node you want to hide and it will hide all segments within that node).</p>

---

## Post #3 by @caesarsalad (2021-08-11 04:37 UTC)

<p>Hi,</p>
<p>Thank you for your reply.</p>
<p>I see what you mean, I appreciate the insight. However, from my understanding, when I try saving the files the segmentations are combined into a single nrrd file. Is it possible to have each segmentation module saved with each corresponding module?</p>

---

## Post #4 by @muratmaga (2021-08-11 04:44 UTC)

<p>Only the segments within a segmentation node will be saved in the file. If you have two segmentation nodes (one for each volume), you will save two files.</p>

---
