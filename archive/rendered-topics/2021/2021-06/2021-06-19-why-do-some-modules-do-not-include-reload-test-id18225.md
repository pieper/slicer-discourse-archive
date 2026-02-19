---
topic_id: 18225
title: "Why Do Some Modules Do Not Include Reload Test"
date: 2021-06-19
url: https://discourse.slicer.org/t/18225
---

# Why do some modules do not include Reload&Test ？

**Topic ID**: 18225
**Date**: 2021-06-19
**URL**: https://discourse.slicer.org/t/why-do-some-modules-do-not-include-reload-test/18225

---

## Post #1 by @slicer365 (2021-06-19 05:23 UTC)

<p>Why some modules do not include Reload&amp;Test,</p>
<p>as is shown in this picture.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd93510df9c5bd2d032beaf2fb08fff9e29d8db.png" alt="捕获" data-base62-sha1="96PrAZJk3WlnwREPpGRoHbqgIQj" width="458" height="293"></p>

---

## Post #2 by @lassoan (2021-06-19 12:37 UTC)

<p>Only Pytho on scripted modules can be dynamically reloaded while Slicer is running. Crop volumes module (and most Slicer core modules) is implemented in C++.</p>

---
