---
topic_id: 11045
title: "Whats The Risk Of Changing Representation"
date: 2020-04-08
url: https://discourse.slicer.org/t/11045
---

# What's the risk of changing representation

**Topic ID**: 11045
**Date**: 2020-04-08
**URL**: https://discourse.slicer.org/t/whats-the-risk-of-changing-representation/11045

---

## Post #1 by @codecrazer (2020-04-08 15:28 UTC)

<p>What’s the risk of changing representation?<br>
Due to I need to use pyradiomics, I need to change Dicom to NRRD, so I need to use binary labelmap, however, every time I click make master, a warning screen pop up, and tell me there is risk of losing important information!</p>
<p>What kind of  important information may be lose? Does lose the data affect pyradiomics feature computing? Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-04-08 21:29 UTC)

<p>Do you import segmentation from RT structure sets?</p>

---

## Post #3 by @codecrazer (2020-04-08 22:38 UTC)

<p>Yes, so I need to change representation to get RTstruct NRRD file</p>

---

## Post #4 by @lassoan (2020-04-08 23:53 UTC)

<p>In RT structure sets, each structure is defined by a set of parallel contours. NRRD file is a binary labelmap representation. Conversion is always lossy because the straight contour lines are sampled at a finite resolution (the labelmap’s resolution).</p>
<p>By default, the conversion happens at the chosen master volume’s resolution, which is usually sufficient, as the segmentation was originally created from that image. You can visually verify that the converted segment contains all the clinically relevant details.</p>

---

## Post #5 by @codecrazer (2020-04-09 00:44 UTC)

<p>I am newbie in CV. I am still confused! If the resolution of Dicom and NRRD doesn’t change, why we need to sample ? Thanks for your help!</p>

---

## Post #6 by @lassoan (2020-04-09 01:56 UTC)

<p>Contour point positions in RT structure sets have practically infinite resolution (coordinate values are stored as 64-bit floating point values), while images always have a specific resolution. When you convert from contours to images you need to decide what image resolution to use.</p>
<p>Using the original input image’s resolution should work well in all cases except rare cases of very small or very thin structures. If your structures are like that then you may decide to oversample the original image when creating the labelmap representation (Segmentations module / Representations section / Binary labelmap -&gt; Update, in the displayed dialog, choose conversion path and adjust “Oversampling factor”).</p>

---

## Post #7 by @codecrazer (2020-04-16 14:23 UTC)

<p>I try to do as you say, adjust “Oversampling factor”, but there are two options when I click, also there is a value called “Estimated relative cost”, what is that? Thanks for your help!</p>

---

## Post #8 by @cpinter (2020-04-16 14:35 UTC)

<p>It is a ballpark number for how long the conversion takes. It is considered when the mechanism chooses a conversion path between two representations automatically.</p>

---

## Post #9 by @codecrazer (2020-04-16 14:56 UTC)

<p>Do these two methods give different results? If the result is similar, why do we need two methods, thanks for your help!</p>

---

## Post #10 by @lassoan (2020-04-16 15:06 UTC)

<p>You can develop and register any number of conversion algorithms between any representations. As a result, you end up with multiple ways of getting from one representation to the other. Usually a direct conversion step is better, but you are free to choose and compare the various available options and use the one that works best for you.</p>

---

## Post #11 by @codecrazer (2020-04-17 01:26 UTC)

<p>So if I only click make master, the result will be direct tranformation? If I want different pathway, then I should click update; or only clicking make master will choose the least cost way in the update panel? Which one is correct?</p>

---

## Post #12 by @lassoan (2020-04-17 04:30 UTC)

<p>By default the conversion with the shortest total path is used. If you want to apply a non-default conversion path then you need to click update, chose a different conversion path, and click “Convert”. Note that manual override is not remembered, so if you convert again automatically (e.g., you remove a representation and create it again with default settings) then it will use the default path.</p>

---

## Post #13 by @codecrazer (2020-04-17 11:38 UTC)

<p>Are the RTstruct file stored as vector graph? If the RTstruct file is a vector graph, when I transform it into bitmap, it is lossy. Is it right?</p>

---

## Post #14 by @cpinter (2020-04-17 12:18 UTC)

<p>RTStruct is stored in a series of 2D contours, described by a set of points for each contour. It is a legacy representation, that is very hard to create well for complex structures, and hard to convert to more manageable formats. See the first image on this page. It shows just the RTSS conversions.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a></p>

---

## Post #15 by @lassoan (2020-04-17 15:09 UTC)

<aside class="quote no-group" data-username="codecrazer" data-post="13" data-topic="11045" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/codecrazer/48/6479_2.png" class="avatar"> codecrazer:</div>
<blockquote>
<p>Are the RTstruct file stored as vector graph? If the RTstruct file is a vector graph, when I transform it into bitmap, it is lossy. Is it right?</p>
</blockquote>
</aside>
<p>Probably you don’t realize how hard it is to do this correctly. For example, when a slice intersection has a hole (this happens even when the segment does not have an internal cavity, but simply has a concavity) then it is saved into a single contour using “keyhole” technique. You need to detect and reverse-engineer keyholes when you rasterize the contour. End-capping of contours is not trivial either (you don’t want to abruptly end a segment at the first and at the last contour’s position). To reduce information loss, you often need to oversample the contour, but it means that you need to robustly and smoothly interpolate contours. Robust contour interpolation is hard because RT structure sets normally don’t contain connectivity information (which contours of neighbor slices are connected to each other), so you need to detect connections, branching, and terminations. These are <em>all</em> solved quite well in SlicerRT’s converter - tested on many data sets, by many users, over several years.</p>
<p>So, your options are something like these:</p>
<ul>
<li>A. use a naive contour rasterization algorithm: you can only use native resolution (no oversampling, so you may lose lots of information, which can be very significant for small or thin structures) and you must manually review and potentially correct all conversion errors (due to keyholes etc.)</li>
<li>B. Use SlicerRT’s converter</li>
<li>C. Get rid of contours and only use labelmap representation for segmentation (this is the safest and most efficient, unfortunately not always feasible, if you must interface with radiotherapy software that can only work with contours)</li>
</ul>

---
