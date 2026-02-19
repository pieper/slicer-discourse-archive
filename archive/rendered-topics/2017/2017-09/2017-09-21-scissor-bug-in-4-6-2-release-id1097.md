---
topic_id: 1097
title: "Scissor Bug In 4 6 2 Release"
date: 2017-09-21
url: https://discourse.slicer.org/t/1097
---

# Scissor bug in 4.6.2 release

**Topic ID**: 1097
**Date**: 2017-09-21
**URL**: https://discourse.slicer.org/t/scissor-bug-in-4-6-2-release/1097

---

## Post #1 by @LESAUNIER_Thibault (2017-09-21 15:16 UTC)

<p>Hello,</p>
<p>I’m working with 3D Slicer and i want to cut some part of my 3D Volume. We can do this using Segment Editor and Scissor like in the video : <a href="https://www.youtube.com/watch?v=m4zTj8i4tCA" rel="nofollow noopener">https://www.youtube.com/watch?v=m4zTj8i4tCA</a></p>
<p>But on my pc, it doesn’t work.</p>
<p>An idea ?</p>
<p>Thanks</p>

---

## Post #2 by @ihnorton (2017-09-21 15:16 UTC)

<p>Please use the nightly download.</p>

---

## Post #3 by @LESAUNIER_Thibault (2017-09-22 07:10 UTC)

<p>I did, but nothing change.</p>

---

## Post #4 by @lassoan (2017-09-22 13:33 UTC)

<p>Can you send us a screen capture of what you tried to do? Or describe in detail, what button you clicked, where you drew contours, what you expected to happen, and what happened instead?</p>

---

## Post #5 by @LESAUNIER_Thibault (2017-09-22 14:13 UTC)

<p>I try to erase a part of my Volume like in this example.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c2e10ee16a96881702584d35ba62581b03c9ba3.png" data-download-href="/uploads/short-url/41i43qn4mft5Y407gB7k1Vfro8r.png?dl=1" title="Sans titre" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c2e10ee16a96881702584d35ba62581b03c9ba3_2_690x245.png" alt="Sans titre" data-base62-sha1="41i43qn4mft5Y407gB7k1Vfro8r" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c2e10ee16a96881702584d35ba62581b03c9ba3_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c2e10ee16a96881702584d35ba62581b03c9ba3_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c2e10ee16a96881702584d35ba62581b03c9ba3_2_1380x490.png 2x" data-dominant-color="B5B6D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sans titre</span><span class="informations">1693×603 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2017-09-22 14:57 UTC)

<p>Your screenshot is not from a recent nightly. Please download and install the <em>nightly</em> (yellow buttons on the bottom) from here:<br>
<a href="http://download.slicer.org/" class="onebox" target="_blank">http://download.slicer.org/</a></p>

---

## Post #7 by @LESAUNIER_Thibault (2017-09-22 15:04 UTC)

<p>I tried with the nightly version, it doesn’t work too</p>

---

## Post #8 by @lassoan (2017-09-22 17:01 UTC)

<p>In the video that you linked, the bones were not volume rendered, but they were segmented structures.</p>
<div class="lazyYT" data-youtube-id="m4zTj8i4tCA" data-youtube-title='New "scissors" editing tool in 3D Slicer for 3D cropping' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Scissors erase from segmentations. If you want to erase from your input volume then install SegmentEditorExtraEffects extension and use the “Mask volume” effect, as shown here:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #9 by @LESAUNIER_Thibault (2017-09-25 09:22 UTC)

<p>Hi !</p>
<p>Thansk you, i understand the fact that i have to create a 3D segment before Scissor it. It works perfectly.<br>
I used a threshold to create the segment and use scissor to cut parts i don’t want.</p>
<p>Tks, Bye !</p>

---
