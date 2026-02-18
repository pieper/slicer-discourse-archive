# How to retrieve modeltomodel values by coordinates?

**Topic ID**: 23431
**Date**: 2022-05-14
**URL**: https://discourse.slicer.org/t/how-to-retrieve-modeltomodel-values-by-coordinates/23431

---

## Post #1 by @K_Tilman (2022-05-14 19:36 UTC)

<p>Hey there!</p>
<p>Currently I am using the ModelToModelDistance module on two models, which outputs a third model which I have been analyzing using the ShapePopulationView module.</p>
<p>This colormap is somewhat useful in itself but I would like to look at the specific values that the model contains. I have used the function arrayFromModelPointData() to retrieve the distances however this gives me no indication to which points on the model these distances belong.</p>
<p>Is there maybe a way to click on the model to then retrieve the distances of the colormap for that specific point? I tried doing it using markups but I am not sure how to map the control point to a point on the node (retrieved using getNode) of the color map.</p>

---

## Post #2 by @lassoan (2022-05-14 21:28 UTC)

<p>You can get the ID of the closest point to a coordinate using VTK locator classes. See a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-scalar-values-at-surface-of-a-model">complete example in the script repository</a>.</p>

---

## Post #3 by @K_Tilman (2022-05-25 08:43 UTC)

<p>Thank you for your answer!<br>
I managed to write a script to extract the data from the model to model distance extensions by placing markup nodes on the model. I still can’t manage to figure out how to place markup nodes on the colormap in ShapePopulationViewer. Can you help me with that? Thank you!</p>

---

## Post #4 by @lassoan (2022-05-25 17:30 UTC)

<p>I don’t think ShapePopulationViewer supports any kind of markups. Instead, I would recommend to enable coloring by scalars using Models module → Scalars section.</p>

---
