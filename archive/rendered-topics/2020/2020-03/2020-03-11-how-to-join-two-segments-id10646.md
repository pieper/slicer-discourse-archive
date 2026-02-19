---
topic_id: 10646
title: "How To Join Two Segments"
date: 2020-03-11
url: https://discourse.slicer.org/t/10646
---

# How to join two segments?

**Topic ID**: 10646
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/how-to-join-two-segments/10646

---

## Post #1 by @Lucia_Munoz (2020-03-11 16:19 UTC)

<p>Hello! Im trying to model a total knee replacement and i can´t join the tibia with the tibial tray to see if they match. Is it possible to do? <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=9" title=":upside_down_face:" class="emoji" alt=":upside_down_face:"><br>
perating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-03-11 16:28 UTC)

<p>What do you mean by joining? If you want to evaluate how well they fit then most likely you don’t want to merge them into a single segment but do something like measuring distance between the surfaces.</p>

---

## Post #3 by @Lucia_Munoz (2020-03-12 02:54 UTC)

<p>And how can i measure the distance? i have been using the ruler but the surface of the bones aren´t easy to measure with the it. Is there any other tool i can use?</p>

---

## Post #4 by @manjula (2020-03-12 10:07 UTC)

<p>There are extensions like model to model distance which you can and also visualise with them with shape population viewer.</p>
<p>Also you have Fiducials to Model Distance extension recently developed by <a class="mention" href="/u/juicy">@Juicy</a></p>
<p>Also you can do the distance with markups only.</p>
<p>Alos you can use,</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>

---

## Post #5 by @Lucia_Munoz (2020-03-12 21:25 UTC)

<p>Thanks!! this is very helpful!</p>

---
