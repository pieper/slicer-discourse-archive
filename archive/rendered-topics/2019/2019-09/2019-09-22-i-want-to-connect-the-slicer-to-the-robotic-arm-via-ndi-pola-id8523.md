---
topic_id: 8523
title: "I Want To Connect The Slicer To The Robotic Arm Via Ndi Pola"
date: 2019-09-22
url: https://discourse.slicer.org/t/8523
---

# I want to connect the slicer to the robotic arm via NDI Polaris Vicra

**Topic ID**: 8523
**Date**: 2019-09-22
**URL**: https://discourse.slicer.org/t/i-want-to-connect-the-slicer-to-the-robotic-arm-via-ndi-polaris-vicra/8523

---

## Post #1 by @Zhao_Su (2019-09-22 02:53 UTC)

<p>But the robotic arm only supports the TCP communication protocol.  Ndi’s communication interface is API. Is there any good solution？ Thanks a lot！</p>

---

## Post #2 by @ungi (2019-09-22 18:40 UTC)

<p>Hi, check out the PLUS Toolkit. PLUS is a software that reads tracking information from NDI Polaris (and lots of other devices), and sends that information to 3D Slicer through OpenIGTLink. You may find these tutorials useful: <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">http://www.slicerigt.org/wp/user-tutorial/</a><br>
We also had a tutorial recently, specifically with a robot arm: <a href="https://github.com/rosmed/rosmed.github.io" rel="nofollow noopener">https://github.com/rosmed/rosmed.github.io</a><br>
You will need to learn how to use multiple software tools together, but what you want to do is possible.</p>

---

## Post #3 by @Zhao_Su (2019-09-26 14:37 UTC)

<p>Hi! I had already finish all of the slides, but I didn’t  know how to control a real robot. If I want control it, what should I do during the tutorial? Thanks a lot !</p>

---
