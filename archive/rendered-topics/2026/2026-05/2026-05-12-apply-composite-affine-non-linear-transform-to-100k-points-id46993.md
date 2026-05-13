---
topic_id: 46993
title: "Apply Composite Affine Non Linear Transform To 100K Points"
date: 2026-05-12
url: https://discourse.slicer.org/t/46993
---

# Apply composite affine + non-linear transform to 100k points

**Topic ID**: 46993
**Date**: 2026-05-12
**URL**: https://discourse.slicer.org/t/apply-composite-affine-non-linear-transform-to-100k-points/46993

---

## Post #1 by @sulli419 (2026-05-12 18:06 UTC)

<p>Hi,<br>
I have a large ~10GB .h5 transform that I created within Slicer (affine+non-linear displacement field) by registering two volumes.  I also have a spreadsheet that lists the XYZ coordinates of up to 100,000 points.  Is there a simple way in slicer to apply my transform, to warp and create a new spreadsheet of points, and visualize this.  My goals is to stay in slicer so as not to get confused by different origin definitions and keep the gui visualizations.</p>
<p>On a related topic, is there a preferred way to graphically display this many points.  The typical point list method seems like it’s ideal for no more than 100 or so.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2026-05-12 18:09 UTC)

<p>I don’t know how you plan to visualize 100K points but one way to do this is to create 3D point cloud where each your points is a vertex and then apply and harden your transform, and then extract the new coordinates of vertices.</p>

---

## Post #3 by @sulli419 (2026-05-12 18:18 UTC)

<p>This sounds on the right track. Thanks. I don’t have much experience in this realm, so if you can point to how to draw them and warp them it’d be appreciated.  Would this be using some of Model tools?  This is one part of slicer I haven’t dabbled in much.</p>

---

## Post #4 by @muratmaga (2026-05-12 18:23 UTC)

<p>Just give this prompt to any LLM (chatGPT, claude or copilot)</p>
<p>“I have 100K points that I would like to convert to a point cloud such coordinate each of point is a vertex and write the output in PLY format. I will apply a non-linear transformation to this model in 3D slicer and need to extract the coordinates of each vertex after the transform is applied. Write python script that I can execute in 3D Slicer”</p>
<p>or something along those lines. That’s nowadays the fastest approach to get what you want to do.</p>
<p>Otherwise you can browse throught the script repository for example</p>

---

## Post #5 by @muratmaga (2026-05-12 18:25 UTC)

<p>Although I would highly advise to test this with a smaller transform and a subset of points until you know that it is working correctly.</p>

---

## Post #6 by @sulli419 (2026-05-12 18:39 UTC)

<p>Yes, starting small is good.   I can also visualize the points against a volume make sure the new points are in the correct location.</p>
<p>I was exploring the LLM path in parallel.  It’s still good to get grounded by wet-brains occasionally too… but at the current rate, in a couple of months that might not be necessary. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
