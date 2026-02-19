---
topic_id: 3517
title: "Slicer Crashes When Applying A Rigid Transform To A Structur"
date: 2018-07-18
url: https://discourse.slicer.org/t/3517
---

# Slicer crashes when applying a rigid transform to a structure set

**Topic ID**: 3517
**Date**: 2018-07-18
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-applying-a-rigid-transform-to-a-structure-set/3517

---

## Post #1 by @Lowey (2018-07-18 22:42 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior: To be able to apply a rigid 6DOF transform to a structure set, and then apply a DVF from a non-rigid registration to the same structure set<br>
Actual behavior: After using the ‘registration’ module to create a rigid transform between two CT images I try to apply that transform to a RT structure set in the ‘transform’ module. However, Slicer just crashes (Not responding indefinitely)</p>
<p>Any help would be greatly appreciated<br>
Thanks!</p>

---

## Post #2 by @Lowey (2018-07-18 22:57 UTC)

<p>Note that the crash occurs when ‘hardening’ the transform</p>

---

## Post #3 by @Fernando (2018-07-19 20:01 UTC)

<aside class="quote no-group" data-username="Lowey" data-post="1" data-topic="3517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e36b37/48.png" class="avatar"> Lowey:</div>
<blockquote>
<p>Slicer version: 4.8.1</p>
</blockquote>
</aside>
<p>Can you try the nightly version instead?</p>

---

## Post #4 by @brandus1 (2023-04-28 14:19 UTC)

<p>Happens to me also on Slicer 5.2.2. Both on MacOs and on Ubuntu. Happens only with some stl files I import</p>

---

## Post #5 by @lassoan (2023-05-02 19:07 UTC)

<p>Csak you provide data set and instructions to reproduce?</p>

---
