---
topic_id: 17132
title: "Logical Operators"
date: 2021-04-16
url: https://discourse.slicer.org/t/17132
---

# Logical operators

**Topic ID**: 17132
**Date**: 2021-04-16
**URL**: https://discourse.slicer.org/t/logical-operators/17132

---

## Post #1 by @Eileen (2021-04-16 13:26 UTC)

<p>logical operators do not work when i import self created models (created with inventor) as segmentations</p>

---

## Post #2 by @hherhold (2021-04-16 13:41 UTC)

<p>I think Logical Operators in the Segmentation module only work on segments. You need to convert your model to a segmentation node - in the Data module, right click on the model and select “Convert model to segmentation node”. Then you should be able to use logical operators.</p>

---

## Post #3 by @manjula (2021-04-16 16:31 UTC)

<p>In addtion to importing the models as segments you will need to select/create a master volume for the segment editor logical operators to work.</p>
<p>If you need only union, intersection and subtraction operations you can do that directly on models with the “combine models” module that you can install in the preview version of Slicer. (Install the sandbox extension and search for combine models module".</p>

---

## Post #4 by @hherhold (2021-04-16 16:34 UTC)

<p>Oh yeah, good point. I just downloaded CT Head and tried it to verify, so there was already a volume.</p>

---

## Post #5 by @Eileen (2021-04-19 06:38 UTC)

<p>Thanks for the replies. I converted or imported the model as segmentation. I have a Master Volume, which is always in preselection.<br>
When I convert the segmentation to a model and back to a segmentation the following message appears when using the logical operators.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aeb625228eac18aa1683c092715b45db7d4b994.png" alt="image" data-base62-sha1="8pe0553y8TCbKai9n3pcsdiku0Y" width="402" height="147"></p>

---

## Post #6 by @Eileen (2021-04-19 06:41 UTC)

<p>The problem is that I can then unfortunately only use substract, but not add, for example. And the result of subtracting does not always look as desired. Instead of a “round” hole, a dalle is created.</p>

---

## Post #7 by @chinaso1111 (2023-05-31 04:54 UTC)

<p>i try it ,and it works,<br>
thanks</p>

---
