---
topic_id: 9670
title: "Thickness Of The Model"
date: 2019-12-31
url: https://discourse.slicer.org/t/9670
---

# Thickness of the model

**Topic ID**: 9670
**Date**: 2019-12-31
**URL**: https://discourse.slicer.org/t/thickness-of-the-model/9670

---

## Post #1 by @Tekk_ya (2019-12-31 11:16 UTC)

<p>Hi,</p>
<p>I am using the hallow module to create a hallow model, with the desired width. However, when I check the model’s thickness in meshmixer it seems like the thickness is roughly half of the desired width. Would you please suggest a way to measure the thickness of the generated hallow model in the Slicer and also compare the results in any other 3D software to make sure that the generated model has the same thickness?</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2019-12-31 14:05 UTC)

<p>Thanks for reporting this. This was an issue in Slicer-4.10 and it was fixed in some time ago in Slicer-4.11.</p>

---

## Post #3 by @Tekk_ya (2020-01-14 10:25 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply. I imported my segmentation in Slicer 4.11, however when I try to grow the margin of the segmentation with the desired thickness, it has almost the same thickness as previous(almost half of the desire value). Is the problem fixed both for hallow and the the margin modules?</p>
<p>Bests,</p>

---

## Post #4 by @lassoan (2020-01-14 21:56 UTC)

<p>Margin size in “Margin” effect still refers to overall margin (the structure will be wider by the margin size in total, so width is increased by half the margin size on all sides). I agree that it is confusion and it should work the same way as hollow effect.</p>
<p>We have a <a href="https://github.com/Slicer/Slicer/pull/1274">pending pull request</a> by <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> that hugely improves speed of these effects for large values - we’ll change interpretation of the margin size when that gets integrated.</p>

---

## Post #5 by @lassoan (2020-02-11 15:02 UTC)

<p>Fast margin computation will be available in Slicer Preview Release from tomorrow (rev28764 or later).</p>

---

## Post #6 by @manjula (2020-02-12 20:53 UTC)

<p>Thank you so much for this improvement to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and Prof <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>It works perfectly !!!</p>
<p>Just for the information,<br>
What was actually changed ?</p>
<p>What is the algorithm/science behind this ? If you have a publication please link it.</p>
<p>I read somewhere along the way that something was changing from marching cubes to flying edge algorithm ? was this something like that ?</p>

---

## Post #7 by @Sunderlandkyl (2020-02-12 21:15 UTC)

<p>Margin computation was previously computed using kernel based erosion and dilation (<a href="https://vtk.org/doc/nightly/html/classvtkImageDilateErode3D.html" rel="nofollow noopener">vtkImageDilateErode3D</a>).</p>
<p>We updated the margin and hollow effects to calculate and threshold a distance map using ITK (<a href="https://itk.org/Doxygen/html/classitk_1_1SignedMaurerDistanceMapImageFilter.html" rel="nofollow noopener">itk::SignedMaurerDistanceMapImageFilter</a>, <a href="http://hdl.handle.net/1926/171" rel="nofollow noopener">Insight Journal paper</a>).</p>

---
