---
topic_id: 34612
title: "Flipimagefilter In Itk Simple Filters Broken"
date: 2024-02-29
url: https://discourse.slicer.org/t/34612
---

# FlipImageFilter (in ITK Simple filters) broken?

**Topic ID**: 34612
**Date**: 2024-02-29
**URL**: https://discourse.slicer.org/t/flipimagefilter-in-itk-simple-filters-broken/34612

---

## Post #1 by @shai-ikko (2024-02-29 10:26 UTC)

<p>Hi,</p>
<p>I have a volume which I want to flip along one of the axes, and I was very happy to find the FlipImageFilter in the list of Simple Filters. However, when I apply the filter, I don’t get the expected results.</p>
<p>The end result looks like nothing happened; If I’m lucky and observant enough, sometimes I can see the displayed volume flip and then flip back. When I examine the original vs. the filtered image, I can see that the content of the volume was indeed flipped – as can be evidenced by the relationship between space coordinates and grid coordinates – but the directions matrix is also changed (relevant value negated), and the total result is that the represented volume is exactly identical to the original.</p>
<p>Is this the intended effect?</p>
<p>Slicer 5.4.0 on Linux.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1be1851009f63a8641fb2c78d011d2655a558baf.png" alt="image" data-base62-sha1="3YE448PYW2LD90U8Fg0YwQQOIwf" width="529" height="156"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d336132869531549964ece4cc085c2012e5934.png" alt="image" data-base62-sha1="pENZ52LkUqJkVxGSe0bE9TiUfGc" width="491" height="160"></p>

---

## Post #2 by @pieper (2024-02-29 14:18 UTC)

<p>Flipping the image contents changes their memory layout but not the physical location.  You can use a transform to change the physical location of the pixels (e.g. negate a column to flip).</p>

---

## Post #3 by @shai-ikko (2024-02-29 15:32 UTC)

<p>Yes, that’s what I described – but it’s a bit surprising after looking at things like <a href="https://examples.itk.org/src/filtering/imagegrid/flipanimageoverspecifiedaxes/documentation" rel="noopener nofollow ugc">https://examples.itk.org/src/filtering/imagegrid/flipanimageoverspecifiedaxes/documentation</a></p>

---

## Post #4 by @pieper (2024-02-29 15:37 UTC)

<p>Probably the ITK example code doesn’t take into account the index to physical mapping.  ITK originally didn’t include orientation in the images so some of the code and examples don’t include it.</p>

---
