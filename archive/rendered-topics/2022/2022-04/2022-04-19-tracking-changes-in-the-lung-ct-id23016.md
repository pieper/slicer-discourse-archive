---
topic_id: 23016
title: "Tracking Changes In The Lung Ct"
date: 2022-04-19
url: https://discourse.slicer.org/t/23016
---

# Tracking changes in the lung CT

**Topic ID**: 23016
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/tracking-changes-in-the-lung-ct/23016

---

## Post #1 by @ylcnkzy (2022-04-19 08:52 UTC)

<p>Dear all,</p>
<p>I am currently working on lung CT to evaluate the changes in lung tissue and tumor size. I have CT scans at 8 different time points such as Planning CT, Therapy Control CT, and Follow-up CTs.</p>
<p>I want to use planning CT as the base data (the first data point) and visualize the changes over time. I have seen many tools (such as ANTs for image registration) and some plugins in 3D Slicer, however; I am not sure which one I need to use.</p>
<p>The thing in my mind is simply that;<br>
Image registration by labeling anatomic points in two CTs and then extracting the changes in lung tissue (this can be done in a manual/autonomous or semi/autonomous fashion). Then. visualize the changes as a heat map (such as Jacobian Map )and extract the statistics</p>
<p>I have seen ChangeTracker, SlicerMorph, and SlicerElastix in the extension manager. However, I am unsure which one may fit my problem better, and which pipeline.</p>
<p>Kind Regards</p>

---

## Post #2 by @pieper (2022-04-19 15:34 UTC)

<p>It sounds like you have found relevant prior work.  I’m not sure there’s an existing pipeline that covers your exact use case, but putting together the steps you described should work.  You can either develop a manual workflow procedure or you could automate some steps with python scripts and/or build a custom module to make the work easier.</p>

---

## Post #3 by @dave3d (2022-04-19 15:41 UTC)

<p>I would be interested in whatever work flow you come up with, since I am working on a similar project.  I’ve just started playing with ANTs to register a couple time steps of my lung CT data sets.  And I would also like to visualize the changes in the images.</p>

---

## Post #4 by @ylcnkzy (2022-04-20 12:02 UTC)

<p>Hi <a class="mention" href="/u/dave3d">@dave3d</a>, I will let you know If I come up with any solution.</p>

---
