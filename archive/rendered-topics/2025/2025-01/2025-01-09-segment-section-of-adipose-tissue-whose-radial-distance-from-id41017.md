---
topic_id: 41017
title: "Segment Section Of Adipose Tissue Whose Radial Distance From"
date: 2025-01-09
url: https://discourse.slicer.org/t/41017
---

# Segment section of adipose tissue whose radial distance from the blood vessel wall is equal to the diameter of the blood vessel.

**Topic ID**: 41017
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/segment-section-of-adipose-tissue-whose-radial-distance-from-the-blood-vessel-wall-is-equal-to-the-diameter-of-the-blood-vessel/41017

---

## Post #1 by @seraphina (2025-01-09 16:53 UTC)

<p>I would like to obtain a segment of adipose tissue whose radial distance from the blood vessel wall is equal to the diameter of the blood vessel, and this segment can change along with the variation of the blood vessel diameter. Then, I need to measure its CT value. So, what should I do?</p>
<p>Currently, I have used the “paint” tool to outline the target blood vessel (assuming the diameter of the blood vessel is 9 mm). Then, I applied the “hollow” function to expand it by 1 mm and 9 mm respectively. After that, I used “logical operators” to subtract (subtracting 1 mm is to avoid the artifacts caused by contrast agents). In the remaining range of 8 mm, I set the threshold for adipose tissue, and finally used the “segment statistics” function to calculate the average CT value.</p>
<p>However, there are still two problems:</p>
<ol>
<li>
<p>After applying the “hollow” function, it doesn’t simply expand along the planar edge of the selected blood vessel. Instead, it seems to expand in all directions with this layer as the center. If I only want to expand on the plane of the selected blood vessel section, what should I do? (Currently, the solution I adopted is to manually erase the parts outside the scope.)</p>
</li>
<li>
<p>If a segment of blood vessel with a certain length is selected and the thickness of the entire blood vessel varies, and I want the expansion distance to change with the diameter of the blood vessel, what should I do?</p>
</li>
</ol>

---

## Post #2 by @pieper (2025-01-09 17:50 UTC)

<p>What you describe sounds reasonable if you are willing to write a somewhat detailed script, which would be worth it if you want to do this semi-automatically on a lot of data.  If you want to do this manually I’d suggest just doing the calculation at a few representative spots along the vessel and paint the desired segments manually with the size and shape you need.</p>

---

## Post #3 by @seraphina (2025-01-11 06:17 UTC)

<p>hi，How can I measure the diameter of my blood vessels more accurately?</p>

---

## Post #4 by @chir.set (2025-01-11 08:30 UTC)

<aside class="quote no-group" data-username="seraphina" data-post="3" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seraphina/48/79059_2.png" class="avatar"> seraphina:</div>
<blockquote>
<p>measure the diameter</p>
</blockquote>
</aside>
<p>You may:</p>
<ul>
<li>install SlicerVMTK extension</li>
<li>generate a centerline of the blood vessel using the ‘Extract centerline’ module</li>
<li>process the surface and centerline in the ‘Cross-section analysis’ module.</li>
</ul>

---

## Post #5 by @seraphina (2025-01-13 13:24 UTC)

<p>1.VMTK ⭢ Extract Centerline,What are the meanings of Centerline model and Centerline curve?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81ce0d4db1044baa8de5f9b36545cb9c036d96b8.jpeg" data-download-href="/uploads/short-url/iwj3AUN2CfCvbaY3at7C52IR9Py.jpeg?dl=1" title="Pasted Graphic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ce0d4db1044baa8de5f9b36545cb9c036d96b8_2_690x315.jpeg" alt="Pasted Graphic" data-base62-sha1="iwj3AUN2CfCvbaY3at7C52IR9Py" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ce0d4db1044baa8de5f9b36545cb9c036d96b8_2_690x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ce0d4db1044baa8de5f9b36545cb9c036d96b8_2_1035x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ce0d4db1044baa8de5f9b36545cb9c036d96b8_2_1380x630.jpeg 2x" data-dominant-color="A5A3A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pasted Graphic</span><span class="informations">1920×879 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2.In the cross section analysis, may I ask what are the different meanings and results of selecting Centerline Source between Centerline model and Centerline curve, and what is the difference between the Diameter (MIS) and (CE) tables obtained after applying the table, and which one is more accurate？<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bb0e76b6a07de6c7dfbe404837a309f60734ac5.jpeg" data-download-href="/uploads/short-url/1Fqgz9COFFO2u0jKXnJQHBm4yfX.jpeg?dl=1" title="Pasted Graphic 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb0e76b6a07de6c7dfbe404837a309f60734ac5_2_690x364.jpeg" alt="Pasted Graphic 1" data-base62-sha1="1Fqgz9COFFO2u0jKXnJQHBm4yfX" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb0e76b6a07de6c7dfbe404837a309f60734ac5_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb0e76b6a07de6c7dfbe404837a309f60734ac5_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb0e76b6a07de6c7dfbe404837a309f60734ac5_2_1380x728.jpeg 2x" data-dominant-color="AAA7A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pasted Graphic 1</span><span class="informations">1920×1015 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @SANTIAGO_PENDON_MING (2025-01-13 14:11 UTC)

<p>MIS and CE diameter are quite different ways to extract the radius.</p>
<p>MIS uses minimal inscribed sphere method to extract radius ( In my experience, this method struggles with very tortouse geometries)</p>
<p>CE diameter uses the cross section diameter estimated using the perpendicular planes from the nodes (and some more, due to internal interpolations the code made…)  of your centerline. Again, in my experience, this usually struggles in bifurcations and zones where your centerline is not providing great perpendicular planes.</p>

---

## Post #7 by @chir.set (2025-01-13 16:58 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="6" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>in bifurcations</p>
</blockquote>
</aside>
<p>Since <a class="mention" href="/u/seraphina">@seraphina</a> has already excluded the external carotid artery, the measurements are reliable. Nevertheless, extreme tortuosity is a problematic case, but this is not the case here.</p>

---

## Post #8 by @seraphina (2025-01-14 04:55 UTC)

<p>Thank you very much for your answer. Can I understand that CE diameter is better compared to others.Because I excluded the external carotid artery.I can use the measured CE diameter for further research.</p>

---

## Post #9 by @seraphina (2025-01-14 04:57 UTC)

<p>Thank you very much for your answer. Can I assume that apart from the bifurcation region, the measurement results of CE diameter are better.</p>

---

## Post #10 by @chir.set (2025-01-14 07:56 UTC)

<aside class="quote no-group" data-username="seraphina" data-post="9" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seraphina/48/79059_2.png" class="avatar"> seraphina:</div>
<blockquote>
<p>better</p>
</blockquote>
</aside>
<p>‘Better’ is not the right term. Your research goals determine which one suits best. The CE diameter conveys a functional meaning. The MIS diameter carries a geometric information.</p>

---

## Post #11 by @seraphina (2025-01-20 12:02 UTC)

<p>Thank you very much for your answer, but I don’t quite understand the actual nature. My research goal is to obtain tissues whose radial distance from the blood vessel wall is equal to the diameter of the blood vessel. My current ability is not able to change each layer accordingly, so I intend to choose the minimum value measured. May I ask which one should I choose just to get the most true blood vessel diameter?</p>

---

## Post #12 by @chir.set (2025-01-20 12:55 UTC)

<aside class="quote no-group" data-username="seraphina" data-post="11" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seraphina/48/79059_2.png" class="avatar"> seraphina:</div>
<blockquote>
<p>obtain tissues whose radial distance from the blood vessel wall is equal to the diameter of the blood vessel</p>
</blockquote>
</aside>
<p>You should be able to approximate this pending approval of a pull request. There will be a few more steps to do.</p>

---

## Post #13 by @chir.set (2025-01-20 12:56 UTC)

<aside class="quote no-group" data-username="seraphina" data-post="11" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seraphina/48/79059_2.png" class="avatar"> seraphina:</div>
<blockquote>
<p>true blood vessel diameter</p>
</blockquote>
</aside>
<p>Please define ‘true blood vessel diameter’ in the image below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc0efc21ca1c985c18324c3a5940e385faf595b.png" data-download-href="/uploads/short-url/Auv7pQQkFEjrLz6hDyri1uoazph.png?dl=1" title="aorta_00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc0efc21ca1c985c18324c3a5940e385faf595b_2_469x500.png" alt="aorta_00" data-base62-sha1="Auv7pQQkFEjrLz6hDyri1uoazph" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffc0efc21ca1c985c18324c3a5940e385faf595b_2_469x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc0efc21ca1c985c18324c3a5940e385faf595b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffc0efc21ca1c985c18324c3a5940e385faf595b.png 2x" data-dominant-color="4A4A4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aorta_00</span><span class="informations">576×614 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @seraphina (2025-01-23 02:08 UTC)

<p>Perhaps my expression is not precise enough, theoretically what I need is the closest blood vessel diameter to reality. However, in fact, even if blood vessels are displayed perfectly in enhanced images, manual delineation may still have subjective bias because the smallest unit of delineation is a pixel point, which cannot completely fit the edge of the blood vessel. So now I use Local threshold, changing the minimum threshold range to 200, to identify blood vessels with contrast agents, and then use scissors to remove those outside the region of interest to avoid subjective bias. Based on this outlined range, I want to obtain the closest blood vessel diameter to reality.</p>

---

## Post #15 by @seraphina (2025-01-23 07:24 UTC)

<p>But this has a new problem, can not include the thickened blood vessel wall, what should I do. <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #16 by @chir.set (2025-01-23 08:39 UTC)

<aside class="quote no-group" data-username="seraphina" data-post="14" data-topic="41017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seraphina/48/79059_2.png" class="avatar"> seraphina:</div>
<blockquote>
<p>reality</p>
</blockquote>
</aside>
<p>The only way would be to open the patient and measure! You will always work with best estimates, either with manual measurements or with algorithms.</p>
<p>You could provide an MRB file with your anonymized data, and your segmentation results. Go through the documentation of the segment editor first. Check the SlicerVMTK extension also.</p>

---
