---
topic_id: 36192
title: "A Simple Circle With A Given Radius"
date: 2024-05-16
url: https://discourse.slicer.org/t/36192
---

# A simple circle with a given radius

**Topic ID**: 36192
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/a-simple-circle-with-a-given-radius/36192

---

## Post #1 by @Valeriya (2024-05-16 05:25 UTC)

<p>Hi!</p>
<p>My issue is the following. I need to be able to create a circle (2D) of a specific radius and place it over a certain region of my MRI image. Ideally I should be able to move this circle with my mouse after creation, but it is also okay if instead I have to pre-define where its center is.<br>
Is ther any way to do this in slicer? Or if not, is it possible to create a circle in another software and import it into Slicer, but importantly - still being able to place it where I need it to be?</p>
<p>Thank you!</p>

---

## Post #2 by @chir.set (2024-05-16 08:23 UTC)

<p>You can do that with the Shape::Ring object in ‘Projection’ mode, it’s available in the ‘ExtraMarkups’ extension. A ‘Radius’ line is forcibly drawn altogether. If you want to set a determined radius, a few lines of Python code will do that.</p>

---
