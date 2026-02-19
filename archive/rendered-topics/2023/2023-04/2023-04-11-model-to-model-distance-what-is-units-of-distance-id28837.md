---
topic_id: 28837
title: "Model To Model Distance What Is Units Of Distance"
date: 2023-04-11
url: https://discourse.slicer.org/t/28837
---

# Model-to-Model Distance - What is units of distance?

**Topic ID**: 28837
**Date**: 2023-04-11
**URL**: https://discourse.slicer.org/t/model-to-model-distance-what-is-units-of-distance/28837

---

## Post #1 by @KAMONCHAT_APIVANICHK (2023-04-11 11:00 UTC)

<p>I try to use ‘Model-to-Model Distance’ for measuring the distance between two model. The output showed the color map, so I wonder what is units, maybe mm. or others.</p>
<p>And positive values mean? negative values mean?</p>

---

## Post #2 by @lassoan (2023-04-11 19:05 UTC)

<p>By default it is millimeter.</p>
<p>The unit is the current length unit that was set in the application settings in menu: Edit / Application settings / Units → Show Advanced Options. You need to scale the length values by <code>Coefficient</code> value to get it in the unit specified by the <code>Suffix</code> (Coefficient=1, Suffix=mm means the current length unit is millimeters).</p>
<p>If you work with medical images then there is no reason to consider using any other unit than millimeter. But as always, you need to test your data processing workflow on some known data (e.g., measure some known distance using a markup line).</p>

---

## Post #3 by @KAMONCHAT_APIVANICHK (2023-08-19 15:31 UTC)

<p>Thank you for your answer. By now, I get a problem about the meaning of value. I set the predicted model as source model and the ground truth model as target model, I thought that the negative value means the predicted model is inside the ground truth model. But I got the same result when I switched them (the predicted model as target model and the ground truth model as source model)</p>
<p>I am very confuse. What is wrong?</p>

---

## Post #4 by @Mohammed_Abdul_Majee (2023-08-22 06:10 UTC)

<p>I am sorry but how did you create the colour map with the output file? Opening the ShapePopulationViewer and loading the output ? I try doing so but it takes a very long time to load. Shall I wait?</p>

---

## Post #5 by @KAMONCHAT_APIVANICHK (2023-08-24 07:31 UTC)

<p>I got the VTK output and then I open with the ShapePopulationViewe by choosing the VTK model and click ‘load’</p>

---
