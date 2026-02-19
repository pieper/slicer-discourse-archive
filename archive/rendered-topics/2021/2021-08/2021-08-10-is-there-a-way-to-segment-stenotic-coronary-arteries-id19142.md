---
topic_id: 19142
title: "Is There A Way To Segment Stenotic Coronary Arteries"
date: 2021-08-10
url: https://discourse.slicer.org/t/19142
---

# Is there a way to segment stenotic coronary arteries?

**Topic ID**: 19142
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-segment-stenotic-coronary-arteries/19142

---

## Post #1 by @Mattia_Chiesa (2021-08-10 13:57 UTC)

<p>Dear all,<br>
I’d like to automatically segment the three main coronaries (LCA (LDA+LCX) and RCA) feeding DICOM of <strong>stenotic patients</strong> into 3D slicer.<br>
I followed these 2 VMTK tutorials:  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=yi07mjr3JeU</a> and <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=yi07mjr3JeU</a>.<br>
However, coronaries are often broken into 2 or more parts because of stenosis. What I have always got are partial segmentations (i.e., only the first segment from aorta to stenosis).<br>
What should I do?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-08-10 20:59 UTC)

<p>This topic on coronary segmentation should help:</p>
<aside class="quote quote-modified" data-post="4" data-topic="17998">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extract-the-coronary-and-aorta/17998/4">Extract the coronary and aorta</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    With 6GB of physical RAM I’m surprised that you can load a volume of 512x512x545 voxels at all. I would recommend minimum of 16GB RAM, an Intel Core i7 CPU, and a computer not more than 3 years old. 
Since you will only create a few models, it should be no problem to invest a lot of time in the segmentation process. As you also want high accuracy, it is probably better to not use curves (which would only give you vessel centerline curves and not diameters), but simply set an editable threshold r…
  </blockquote>
</aside>

<p>Let us know if you still have questions.</p>

---

## Post #3 by @Mattia_Chiesa (2021-08-11 11:44 UTC)

<p>Many thanks Andras for your kind and quick reply. I saw that video tutorial on coronary segmentation, but this is a completely manual segmentation. I was wondering whether there is a way to do the same stuff  automatically, even in presence of stenosis (i.e., “tube interruptions”). For instance, a tool which estimates the connection between two ‘MarkUp points’ (the starting and the end point of stenosis), based on the color gradient over frames.</p>

---

## Post #4 by @lassoan (2021-08-11 13:44 UTC)

<p>Optimal choice of method depends on many factors. Most importantly, quality of your images and number of cases.</p>
<p>For a research study with a few hundred cases it may not worth developing a robust automatic tool, and you would need to manually segment a few hundred cases independently, manually, anyway to serve as gold standard for validation and/or training. If you need to develop something for routine clinical use then you probably need to invest into a fully automated method.</p>
<p>If image quality is good (high resolution, good contrast), cases are not challenging overall (not much stenosis, total occlusion, calcifications or metal artifacts), or you know very specifically what and where you want to measure (instead of aiming for “perfect” segmentation of all the coronaries) accurately then automation may be easier to implement.</p>
<p>I did not look thoroughly into what VMTK tools can be used for automating this. I know that there are some semi-automatic tools for extracting a single coronary branch, but did not have much luck using them (maybe the image quality was not sufficiently good or I did not use the tools correctly). <a class="mention" href="/u/lantiga">@lantiga</a> can you comment on this? What VMTK tools you would recommend for this and how robust and accurate they are?</p>

---
