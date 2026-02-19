---
topic_id: 43447
title: "Segment Middle Inner Ear"
date: 2025-06-21
url: https://discourse.slicer.org/t/43447
---

# Segment middle & inner ear

**Topic ID**: 43447
**Date**: 2025-06-21
**URL**: https://discourse.slicer.org/t/segment-middle-inner-ear/43447

---

## Post #1 by @Nadine_Nabil (2025-06-21 15:13 UTC)

<p>Hi everyone,<br>
I’m trying to segment the middle and inner ear in high anatomical detail using 3D Slicer. I need to extract small structures like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png" data-download-href="/uploads/short-url/jn3xvXAaonFLOfA89VdQ7RlHlUW.png?dl=1" title="Screenshot 2025-06-21 180648" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c489e35345fd8ea701529a180281974ee81636_2_541x500.png" alt="Screenshot 2025-06-21 180648" data-base62-sha1="jn3xvXAaonFLOfA89VdQ7RlHlUW" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c489e35345fd8ea701529a180281974ee81636_2_541x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c489e35345fd8ea701529a180281974ee81636.png 2x" data-dominant-color="C49079"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-21 180648</span><span class="informations">765×707 567 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any advice or workflows for segmenting these fine structures?<br>
Should I do it all manually, or is there a better way?</p>
<p>Appreciate any tips or resources!</p>
<p>Thanks,<br>
Nadine</p>

---

## Post #2 by @pieper (2025-06-21 16:53 UTC)

<p>Do you mean from this image or from a CT?  Assuming you mean CT, a lot depends on the resolution of the scan, but thresholding and scissors would be a place to start, but you could also try nnInteractive.</p>

---

## Post #3 by @Nadine_Nabil (2025-06-21 17:00 UTC)

<p>Thank you for your reply!</p>
<p>I’m still quite new to Slicer. I’ve only worked on a 3D model of the sinus and nasal cavity, so I’m not yet familiar with all the available tools.</p>
<p>So far, I usually rely on thresholding, then do most of the refinement manually using Paint and Erase.</p>
<p>For this ear project, I’ll be working with CT data (not the endoscopic image), and I should be able to get high-resolution scans, but I’m not sure if there’s a specific tool that could make segmenting the tiny detailed parts (like the ones I highlighted in the pervious image ) easier — or if manual work is the only option.</p>

---

## Post #4 by @pieper (2025-06-21 17:04 UTC)

<p>There are lots of tutorials and videos so you can get an idea what worked for other people, but in the end you’ll need to experiment a bit.  If you post data publicly along with your experiments other people may get inspired to give it a try and give you more concrete feedback.</p>

---

## Post #5 by @Nadine_Nabil (2025-06-21 17:17 UTC)

<p>Thank you so much, Steve — I really appreciate your time and advice!</p>
<p>I understand that experimenting is key, and I’ll definitely do that.<br>
I just wanted to get a rough idea of how challenging this type of model might be, so I could estimate how much time it would take before diving in.</p>
<p>This project is a step up for me — so far, I’ve only worked on a 3D model of the sinus and nasal cavity — so I’m still learning and trying to plan accordingly.</p>
<p>Thanks again for your support!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbb7d22f6213061d422a5eb32a09ccc64391fde2.jpeg" data-download-href="/uploads/short-url/zUNG9hHy0IkeLuTdqIzEAPulbbQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb7d22f6213061d422a5eb32a09ccc64391fde2_2_690x366.jpeg" alt="image" data-base62-sha1="zUNG9hHy0IkeLuTdqIzEAPulbbQ" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb7d22f6213061d422a5eb32a09ccc64391fde2_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb7d22f6213061d422a5eb32a09ccc64391fde2_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb7d22f6213061d422a5eb32a09ccc64391fde2_2_1380x732.jpeg 2x" data-dominant-color="9EA6BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1018 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the first model I have made. I don’t know where my true level is.</p>

---
