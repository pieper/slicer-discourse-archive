---
topic_id: 24111
title: "How To Change Render Window Plane Programmingly"
date: 2022-06-30
url: https://discourse.slicer.org/t/24111
---

# How to change render window plane programmingly?

**Topic ID**: 24111
**Date**: 2022-06-30
**URL**: https://discourse.slicer.org/t/how-to-change-render-window-plane-programmingly/24111

---

## Post #1 by @user4 (2022-06-30 06:44 UTC)

<p>Hi,all.<br>
I want to change the view plane in render window using python,as marked in red box here.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9674a97cc1f045f4373fd36687ad90331ef70357.png" alt="image" data-base62-sha1="lsZzcVdmGiXiwtZHA9Pf6FGXVwb" width="672" height="170"><br>
That is to say,If I click the P-A orientation,I can get a Coronal plane of the image, I want to use few lines of code to do that.Is there any interface in Script Repository I can use?<br>
Thank you in advance for your help!</p>

---

## Post #2 by @pieper (2022-06-30 20:39 UTC)

<p>Here’s the recipe for solving this general class of problems is described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>Give that a shot and let us know if you don’t find what you need.</p>

---

## Post #3 by @user4 (2022-07-01 01:41 UTC)

<p>Thanks,pieper.<br>
I have tried,but still can not find the 3D pannel.What keywords in this case should I put in order to search on github repo?</p>

---

## Post #4 by @qiqi5210 (2022-07-01 02:56 UTC)

<p>See slicer source code <code> qMRMLThreeDViewControllerWidget.cxx</code><br>
<code>slicer.app.layoutManager().threeDWidget('View1').threeDView().lookFromAxis(ctk.ctkAxesWidget.Posterior)</code><br>
The above Python code can realize the functions you want.</p>

---

## Post #5 by @user4 (2022-07-01 07:06 UTC)

<p>Thanks,Mary.<br>
You just saved me a lot of time.</p>

---
