---
topic_id: 11941
title: "Can Not Find Modules In Slicer"
date: 2020-06-09
url: https://discourse.slicer.org/t/11941
---

# Can not find modules in Slicer

**Topic ID**: 11941
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/can-not-find-modules-in-slicer/11941

---

## Post #1 by @doc-xie (2020-06-09 02:41 UTC)

<p>Hi everyone,<br>
I remember there is a module named Creatmodels in Slicer which can create a cube or a ball and the size can be set manually. But it can not be found in Slicer recently. Is there any other module can perform the task now?<br>
Best wishes,<br>
Xie</p>

---

## Post #2 by @muratmaga (2020-06-09 04:03 UTC)

<p>It is in the SlicerIGT extension.</p>

---

## Post #3 by @doc-xie (2020-06-09 07:06 UTC)

<p>Hi muratmaga,<br>
What in SlicerIGT is Markups to model, fiducials should be set for model make. I want create a cube or a ball with diameter setting.<br>
Best wishes,<br>
Xie</p>

---

## Post #4 by @pieper (2020-06-09 12:58 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a> -</p>
<p>I know it’s not as convenient as a gui module, but you get a lot of powerful options if you use python for a task like that.  There are lots of classes like <code>vtkConeSource</code>, <code>vtkPlaneSoure</code> and others expose many useful controls that would get overwhelming in a gui.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node</a></p>

---

## Post #5 by @lassoan (2020-06-09 13:08 UTC)

<p>“Create models” module show up in IGT category in the module list after you install SlicerIGT extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e13ff1700a31bc9d56492b4d3900baff50e447.png" data-download-href="/uploads/short-url/pO8xu9UWxBxGf7OKLl39Oo9bdVd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4e13ff1700a31bc9d56492b4d3900baff50e447_2_565x499.png" alt="image" data-base62-sha1="pO8xu9UWxBxGf7OKLl39Oo9bdVd" width="565" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4e13ff1700a31bc9d56492b4d3900baff50e447_2_565x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4e13ff1700a31bc9d56492b4d3900baff50e447_2_847x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4e13ff1700a31bc9d56492b4d3900baff50e447_2_1130x998.png 2x" data-dominant-color="E5E7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×1201 79.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @doc-xie (2020-06-10 01:55 UTC)

<p>Hi Lassoan,<br>
SlicerIGT had been installed in 3D Slicer(4.10.0), but “Create models” do not show up in the list. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e71d0bcf837fb8abf459d838d21e8d0e8f1639e6.png" data-download-href="/uploads/short-url/wYwwEKOEM1PnXLRC92Zq3OP3nF4.png?dl=1" title="Screen Shot 2020-06-10 at 9.50.27 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e71d0bcf837fb8abf459d838d21e8d0e8f1639e6_2_690x368.png" alt="Screen Shot 2020-06-10 at 9.50.27 AM" data-base62-sha1="wYwwEKOEM1PnXLRC92Zq3OP3nF4" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e71d0bcf837fb8abf459d838d21e8d0e8f1639e6_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e71d0bcf837fb8abf459d838d21e8d0e8f1639e6_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e71d0bcf837fb8abf459d838d21e8d0e8f1639e6_2_1380x736.png 2x" data-dominant-color="EEF4EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-06-10 at 9.50.27 AM</span><span class="informations">1404×750 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is it the reason about the version of Slicer?<br>
Best wishes,<br>
Xie</p>

---

## Post #7 by @lassoan (2020-06-10 01:59 UTC)

<p>Only latest Slicer Stable Release (4.10.2) and latest Slicer Preview Release (4.11.x) are supported. CreateModels module should be available for both.</p>

---

## Post #8 by @doc-xie (2020-06-10 02:05 UTC)

<p>Hi Steve,<br>
Thank you very much. I will try the code you advice.<br>
Best wishes,<br>
Xie</p>

---

## Post #9 by @KatS (2020-08-19 08:51 UTC)

<p>Dear all,</p>
<p>I have a similar problem: after installing the SlicerIGT Extension on Slicer 4.10.2 r28257, I only have the Fiducial-Module Registration, Model Registration and Viewpoint modules available.<br>
All other modules are not displayed, but I would like to use them. It wasn’t a problem when installing SlicerIGT on Slicer 4.10.1 version recently. Are the other modules not available for 4.10.2?</p>

---

## Post #10 by @lassoan (2020-08-19 12:06 UTC)

<p>Does everything work fine in latest Slicer Preview Release?</p>

---
