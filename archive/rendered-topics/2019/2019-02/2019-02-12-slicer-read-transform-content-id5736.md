---
topic_id: 5736
title: "Slicer Read Transform Content"
date: 2019-02-12
url: https://discourse.slicer.org/t/5736
---

# Slicer Read Transform Content

**Topic ID**: 5736
**Date**: 2019-02-12
**URL**: https://discourse.slicer.org/t/slicer-read-transform-content/5736

---

## Post #1 by @zhenyu1995 (2019-02-12 06:12 UTC)

<p>Hello,</p>
<p>I am now writing a Slicer scripted module and I need to read only a certain element from a specified transform node. For example, I have transform node named “Transform1” and I just need to read the value of element of 3rd column from each row. How can this be done using python coding?</p>
<p>Thanks!</p>

---

## Post #2 by @zhenyu1995 (2019-02-12 07:12 UTC)

<p>Sorry, there was a typo, I just want to read the values of 4th column from each transform. I have 8 (4x4) transform</p>

---

## Post #3 by @pieper (2019-02-12 13:14 UTC)

<p>You can access the matrix and call GetElement like in this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_transform_is_modified" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_transform_is_modified</a></p>

---
