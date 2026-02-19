---
topic_id: 33873
title: "How To Develop 3D Slicer On A Website"
date: 2024-01-19
url: https://discourse.slicer.org/t/33873
---

# How to develop 3D slicer on a website

**Topic ID**: 33873
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/how-to-develop-3d-slicer-on-a-website/33873

---

## Post #1 by @bodenstandig (2024-01-19 15:03 UTC)

<p>Hello to all members of the Slicer community! I am an undergraduate student majoring in computer science, currently working on my graduation project. For my final project, I aim to transplant the 3D image browsing functionality from 3D slicer to a website and employ my own designed deep learning algorithm to segment tumors within the images. This is my first time undertaking such a project, and despite exploring resources in the 3Dslicer community such as webserver and slicerio, I have not come across suitable introductory tutorials, leaving me feeling quite perplexed.</p>
<p>I would like to seek advice from the community. Are there any recommended projects related to this? How should I get started? Your assistance would be greatly appreciated!</p>

---

## Post #2 by @muratmaga (2024-01-19 16:04 UTC)

<p>3D slicer is a complex desktop application. You cannot take pieces of it and make it work as a web application. What you can do is:</p>
<ol>
<li>You can run full Slicer inside a web browser through a number of technologies like docker or remote virtual machines.</li>
<li>If you only want the image browsing functionality, there are open-source web-based technologies that already offer that. You can use one of them, for the Glance app. <a href="https://kitware.github.io/glance/doc/index.html">What is Glance? | Glance (kitware.github.io)</a>. That you can deploy as a web application (since it is designed as one) and from functionality perspective is very similar looking to 3D Slicer.</li>
</ol>
<p>As for machine learning, there are a number of tools and technologies such as MONAI framework, MONAILabel, TotalSegmentator and others that are already available for Slicer. Searching the forum, you should find lots of pointers and discussions about them.</p>

---

## Post #3 by @bodenstandig (2024-01-22 02:52 UTC)

<p>Thanks very much for your kindly reply! I will give it a try!</p>

---
