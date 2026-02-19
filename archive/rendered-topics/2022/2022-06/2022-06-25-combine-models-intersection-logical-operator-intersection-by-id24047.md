---
topic_id: 24047
title: "Combine Models Intersection Logical Operator Intersection By"
date: 2022-06-25
url: https://discourse.slicer.org/t/24047
---

# Combine models intersection / logical operator intersection by script

**Topic ID**: 24047
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/combine-models-intersection-logical-operator-intersection-by-script/24047

---

## Post #1 by @gfurnari (2022-06-25 17:06 UTC)

<p>Hi everyone,<br>
does anybody know how to run intersection between two models (using combine models module) or two segments (using logical operators in segment editor) by python script??</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @mau_igna_06 (2022-06-25 21:23 UTC)

<p>There is the CombineModels module in the Sandbox extension that will allow you to do that. Check the test to see how it’s done by code</p>

---

## Post #3 by @gfurnari (2022-06-26 08:18 UTC)

<p>Thank you very much <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>.<br>
I tried to implment the code but i have a little problem: the output model is empty. I used getNode() to get my input models, is that right or should i use something else?<br>
thank you again for your help</p>

---

## Post #4 by @mau_igna_06 (2022-06-26 14:29 UTC)

<p>You can search “booleanoperation” on yhe BoneReconstructionPlanner extension to see how ot is done in that extension</p>

---
