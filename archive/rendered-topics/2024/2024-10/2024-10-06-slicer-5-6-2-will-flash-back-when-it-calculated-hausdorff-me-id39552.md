# Slicer 5.6.2 will flash back when it calculated Hausdorff metric and Dice metric in SegmentComparison module

**Topic ID**: 39552
**Date**: 2024-10-06
**URL**: https://discourse.slicer.org/t/slicer-5-6-2-will-flash-back-when-it-calculated-hausdorff-metric-and-dice-metric-in-segmentcomparison-module/39552

---

## Post #1 by @Alice914 (2024-10-06 08:37 UTC)

<p>Slicer will flash back when calculating Hausdorff distance metrics and dice metrics for the same layer in two different images using slicer’s radiotherapy-segmentcomparison. I tried to reduce the size of the image and run it on two different computers, but it still didn’t work. What is the reason for this? Could you give me some suggestions? Thank you</p>

---

## Post #2 by @cpinter (2024-10-07 08:17 UTC)

<p>What does it mean “flash back”? Can you please describe the exact steps you take, what you expect, and what happens instead exactly?</p>
<p>Also, what does it mean “same layer in two different images”? Are you working with 2D images?</p>

---

## Post #3 by @Alice914 (2024-10-08 08:41 UTC)

<p>1.’flash back’ means software will automatically quit suddenly when you are using.</p>
<p>2.The extact steps:</p>
<p>Load images(SliceMorph- input and output- image stack)</p>
<p>Segment images(Segment Editor- Add segment for two images)</p>
<p>Calculate Dice metric (Radiotherapy - Segment Comparison)</p>
<p>3.My goal is across ‘segment comparison’ module gains images’ Dice metric and Hausdorff. This module would give results of the calculation in software in the past, but now the software will automatically exit when ‘Compute Hausdorff distance’ is clicked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b6dd116e96183d5163e14824df63e03f00927c5.jpeg" data-download-href="/uploads/short-url/8tJs1L87eBnriUCf8c6yabXKoBf.jpeg?dl=1" title="img_v3_02f7_0834eea1-d74d-4155-a122-4f4fbd78c21g" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b6dd116e96183d5163e14824df63e03f00927c5_2_690x426.jpeg" alt="img_v3_02f7_0834eea1-d74d-4155-a122-4f4fbd78c21g" data-base62-sha1="8tJs1L87eBnriUCf8c6yabXKoBf" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b6dd116e96183d5163e14824df63e03f00927c5_2_690x426.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b6dd116e96183d5163e14824df63e03f00927c5_2_1035x639.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b6dd116e96183d5163e14824df63e03f00927c5_2_1380x852.jpeg 2x" data-dominant-color="21231F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img_v3_02f7_0834eea1-d74d-4155-a122-4f4fbd78c21g</span><span class="informations">1920×1186 96.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>4.I hope this issues that software will automatically exit when I use the function of segment comparison can be solved</p>
<p>5.Same layer looks at green line in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8cc3c421ab47abbf6cb881f8b5b30c3979cf767.jpeg" data-download-href="/uploads/short-url/zuXZ4cdzUI1YSq7u8E9ePRkK063.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8cc3c421ab47abbf6cb881f8b5b30c3979cf767_2_690x429.jpeg" alt="image" data-base62-sha1="zuXZ4cdzUI1YSq7u8E9ePRkK063" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8cc3c421ab47abbf6cb881f8b5b30c3979cf767_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8cc3c421ab47abbf6cb881f8b5b30c3979cf767_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8cc3c421ab47abbf6cb881f8b5b30c3979cf767_2_1380x858.jpeg 2x" data-dominant-color="313430"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1196 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>6.My imaging is phase contrast and fluorescence. They both consist of multiple pieces of 2d images.</p>

---

## Post #4 by @cpinter (2024-10-08 08:59 UTC)

<aside class="quote no-group" data-username="Alice914" data-post="3" data-topic="39552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alice914/48/77819_2.png" class="avatar"> Alice914:</div>
<blockquote>
<p>1.’flash back’ means software will automatically quit suddenly when you are using</p>
</blockquote>
</aside>
<p>OK thanks. It is called a crash.</p>
<p>Unfortunately it is not clear to me if you are really working with 3D images. I was asking because most tools in Slicer are not designed to run on 2D data. Could you upload this MRB scene and share it?</p>

---

## Post #5 by @cpinter (2024-10-10 11:24 UTC)

<p>Thanks for sending the scene.</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="39552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Unfortunately it is not clear to me if you are really working with 3D images. I was asking because most tools in Slicer are not designed to run on 2D data</p>
</blockquote>
</aside>
<p>It turns out this is the case. Slicer is designed to work on 3D data. I suggest doing real 3D segmentations and comparing those.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3edae62a2f72d0c71dcc25b0bb1932a05521e600.png" data-download-href="/uploads/short-url/8Y2AIKq8TwAZEUm9K2nWkbpexUI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3edae62a2f72d0c71dcc25b0bb1932a05521e600_2_690x271.png" alt="image" data-base62-sha1="8Y2AIKq8TwAZEUm9K2nWkbpexUI" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3edae62a2f72d0c71dcc25b0bb1932a05521e600_2_690x271.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3edae62a2f72d0c71dcc25b0bb1932a05521e600_2_1035x406.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3edae62a2f72d0c71dcc25b0bb1932a05521e600.png 2x" data-dominant-color="6D6E94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1373×541 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The fact that it crashes is quite bad, but if the tools are not used in a way they are intended, unexpected things may happen.</p>

---

## Post #6 by @Alice914 (2024-10-10 14:08 UTC)

<p>Thank you very much for answering my questions on your busy schedule! I would like to ask about fluorescence slicing to increase the number of picture sheets to form a 3d image, why is this not possible? Can phase contrast this kind of image be used in 3d slicer?</p>

---

## Post #7 by @cpinter (2024-10-10 15:40 UTC)

<p>I’m sorry I don’t quite understand the question, I’m not an expert in image aquisition or reconstruction. However, I have the feeling that Slicer cannot really help with acquiring better images. It can load and process images but it is a later stage. Maybe someone else will be able to help. Or if you explain it more, maybe I will understand.</p>

---

## Post #8 by @pieper (2024-10-10 16:41 UTC)

<p><a class="mention" href="/u/alice914">@Alice914</a> it sounds like you are doing microscopy analysis.  Slicer would be most helpful for confocal, light sheet, or other natively 3D acquisitions (based on my limitied experience with microscopy).  It’s not a main application, but you might checkout <a href="https://github.com/gaoyi/SlicerBigImage" class="inline-onebox">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image computing using 3D Slicer</a> to get an idea what’s possible.</p>

---

## Post #9 by @Alice914 (2024-10-11 02:34 UTC)

<p>Thank you a lot!! Maybe it is image problem. Now I get it that 2d image is not suitable in 3d slicer</p>

---

## Post #10 by @cpinter (2024-10-11 13:26 UTC)

<p>Well, some 3D algorithms may not work for simgle-slice data, like you saw with segment comparison.</p>
<p>But if you can extend the segmentation to 3D, then it will probably run. Is it important for you to have a different segment on each slice?</p>

---
