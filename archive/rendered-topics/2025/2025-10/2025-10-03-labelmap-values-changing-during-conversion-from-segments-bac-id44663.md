---
topic_id: 44663
title: "Labelmap Values Changing During Conversion From Segments Bac"
date: 2025-10-03
url: https://discourse.slicer.org/t/44663
---

# Labelmap values changing during conversion from segments back to labels

**Topic ID**: 44663
**Date**: 2025-10-03
**URL**: https://discourse.slicer.org/t/labelmap-values-changing-during-conversion-from-segments-back-to-labels/44663

---

## Post #1 by @sulli419 (2025-10-03 19:12 UTC)

<p>Hi,</p>
<p>In my workflow I am importing an 8 bit greyscale volume/mask where each pixel corresponds to a subregion.  Some of the pixel values are rather high (e.g. ,227), and there are gaps between the classes (some intermediate pixel values do not have a class); e.g., 60, 61, then jump to 200.  In my workflow I convert these to segments, smoothen, and then I want to export a new greyscale volume that preserves the orginal pixel values I imported (e.g., 227 still 227).  I noticed that when the segments get converted back to a volume (both when I try to export the segments, or convert them to a labelmap within slicer), the 227 value become ~70(ish).  Other high pixels change there values.  Is each original value forced to count sequentially up.  So say if my classes were 1,2,3,10; does slicer always make this 1,2,3,4 when it converts from the segments back to volume?</p>
<p>I noticed the exported volume is always 16 bit.  Does this have anything to do with it?</p>

---

## Post #2 by @mikebind (2025-10-03 19:58 UTC)

<p>Might the segments overlap after smoothing?  If so, the output segments may not be able to be fully represented in a single labelmap.</p>
<p>If they don’t overlap, then you can just get each segment as a binary labelmap and then use that as a binary mask to apply the label number you want to each segment.  That should all be pretty straightforward to accomplish with python and numpy.  (If the segments do overlap, you would need to decide how to handle conflicts where the same voxel is claimed by more than one segment</p>

---

## Post #3 by @sulli419 (2025-10-04 19:36 UTC)

<p>Thanks for the pointers Mike.  So it sounds like there is no way to preserve the pixel identities (with gaps/jumps between pixel values) when I convert from segments back to labelmaps?  Can you confirm that it just rebuilds the pixels from the list, starting at the top as 1, and counting up 1 pixel per group.  I think this is how it’s behaving but it would help to be certain, so I can relabel in python as you suggest.  I am managing 75 labels, so my process is prone to error.</p>
<p>Maybe a whole different problem: but at some point I want to convert back to 8 bit, and suspect there will be low-depth rounding errors that merge the pixel classes.  Can I create an 8 bit labelmap file?</p>
<p>Still, does anyone know of a way within slicer to convert from segments to labelmaps and preserve the gaps in assigned pixel values?</p>
<p>I feel like this discussion is related:</p><aside class="quote quote-modified" data-post="1" data-topic="26468">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/export-segmentation-as-labeled-labelmap/26468">Export Segmentation as Labeled LabelMap</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi everyone! 
I´m trying to export a segmentation with some segments labed as: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461.png" data-download-href="/uploads/short-url/3h0VaNRThqq9bZXG6rTVJKjw5tn.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
And I exported: 
<a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403.png" data-download-href="/uploads/short-url/h3ZXjOSISYuxPirRxW5yCiknf8f.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
If I close scene and try to import again this file as a segmentation: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2.png" data-download-href="/uploads/short-url/2GmR8IK1xWx3bPiv0xZ9AH2bo5Q.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
Original label is not preserved… 
I have some other NonSlicerMade labelmaps and if I import them: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c1eabb770d4364d22b81b6f75e2b08c003ab4dd.png" data-download-href="/uploads/short-url/hI0UVnuSYztvnMiDVD0JSdyBk4Z.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
So I undertand that: 

Slicer always add string “Segment_” to labelmap labels
Slicer save labelmaps always without original label (just as a ColorTable second file)

Is there any way to change t…
  </blockquote>
</aside>


---

## Post #4 by @muratmaga (2025-10-04 21:21 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="3" data-topic="44663">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>Still, does anyone know of a way within slicer to convert from segments to labelmaps and preserve the gaps in assigned pixel values?</p>
</blockquote>
</aside>
<p>If you want to have non-continuous labelmap values (e.g., 1, 2, 4, 10, 50), you need to define a color table ( <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv" class="inline-onebox" rel="noopener nofollow ugc">Colors — 3D Slicer documentation</a> ) to tell Slicer what index each segment going to get, and then specify that while you are exporting the segmentation to labelmap. Otherwise Slicer while export them in the order they are in the segmentation table, starting from 1.</p>

---

## Post #5 by @sulli419 (2025-10-08 19:22 UTC)

<p>I needed some time to finally get around to trying this… and it absolutely worked.  Thank you!</p>

---
