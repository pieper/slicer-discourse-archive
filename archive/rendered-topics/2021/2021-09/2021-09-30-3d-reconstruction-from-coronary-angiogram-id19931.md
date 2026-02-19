---
topic_id: 19931
title: "3D Reconstruction From Coronary Angiogram"
date: 2021-09-30
url: https://discourse.slicer.org/t/19931
---

# 3D reconstruction from coronary angiogram

**Topic ID**: 19931
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/3d-reconstruction-from-coronary-angiogram/19931

---

## Post #1 by @navidvd (2021-09-30 12:43 UTC)

<p>Hi all,</p>
<p>I was wondering if I can use coronary angiogram images as an input for 3D Slicer in order to create models of the arteries. What I’ve seen so far in the tutorials, mainly CT and MRI images were used. but no coronary angiogram.<br>
Is it possible to import them into the software?<br>
Thanks<br>
Navid</p>

---

## Post #2 by @lassoan (2021-09-30 13:04 UTC)

<p>Angiograms are 2D projection images, so you can view them but they have very limited use in any 3D analysis.</p>
<p>In theory, you can reconstruct a 3D vessel tree from rotational or biplane acquisitions, but it is a hard task and such images are rarely used in cardiac procedures anyway. If you have contrasted images acquired from a few angles, then it might be possible to synchronize them and recover some 3D information, but the problem is even harder than a real biplane acquisition.</p>
<p>Can you tell a bit about the clinical program blem you want to solve? How would you use the 3D information?</p>

---

## Post #3 by @navidvd (2021-09-30 23:14 UTC)

<p>Thanks for your reply.<br>
The angiogram images that I have access to are for 5 to 6 different angles apart from each other.<br>
The reason that I choose to work with angiogram images rather than CT images is the fact that angiogram is more accessible and readily available compared to CT images. And also angiogram images give more details of the artery compared to CT in terms of its higher accuracy.</p>
<p>My aim is to 3D reconstruct coronary arteries and solve the flow inside them in order to find velocity and pressure distributions, and wall shear stress. I will use Ansys Fluent as a solver.</p>
<p>Any suggestions would be appreciated.<br>
Thanks</p>

---

## Post #4 by @lassoan (2021-09-30 23:59 UTC)

<p>Many groups have reported to implement such a system (see for example <a href="https://www.nature.com/articles/s41598-018-19440-9/">this</a>) but I’m not aware of any openly available implementation in Slicer or elsewhere. You could do some literature search and contact the authors of papers that claim they have solved this, to see if they are willing to help you reproducing their results.</p>

---

## Post #5 by @Jacktat (2022-12-22 12:38 UTC)

<p>Great paper, <a class="mention" href="/u/navidvd">@navidvd</a>, were you able to solve it or obtain a model that can extract the coronary topolgy from a 2D coronary angiogram?<br>
I want to do the same thing.<br>
Thanks,<br>
Jack</p>

---
