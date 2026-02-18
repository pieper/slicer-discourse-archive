# Incorrect number of points in exported displacement field

**Topic ID**: 5795
**Date**: 2019-02-15
**URL**: https://discourse.slicer.org/t/incorrect-number-of-points-in-exported-displacement-field/5795

---

## Post #1 by @miniBin (2019-02-15 19:40 UTC)

<p>Action: Performed registration between two models to generate transform<br>
Expected: Number of vertices to match the number of rows in the transform txt file<br>
Result: The numbers did not match</p>
<p>I used segment registration to find a transform between two models. The protocol is described by this link: <a href="https://discourse.slicer.org/t/automatic-non-rigid-elastic-registration-between-2-stl-files/3298" class="inline-onebox">Automatic non-rigid (elastic) registration between 2 stl files</a></p>
<p>I have 11643 vertices in my model. However, my displacement field only has 220 rows of xyz data.</p>
<p>Why is this not matching up and how do I change it?</p>

---

## Post #2 by @lassoan (2019-02-15 20:34 UTC)

<p>The computed transform is independent from the models that generated them.</p>
<p>You can export the transform to a vector volume (using Transforms module) and then use “Probe volume with model” module to get displacement values assigned to each model point.</p>

---

## Post #4 by @miniBin (2019-02-15 21:43 UTC)

<p>Thank you for the fast reply.</p>
<p>I am able to complete the steps but it outputs a model. How do I convert this to a txt file with all of the displacement locations?</p>

---

## Post #5 by @lassoan (2019-02-15 22:15 UTC)

<p>All the displacement locations are stored in the model as point scalar. You can save it to standard VTK file formats and read the displacement values from that.</p>
<p>If you want to process the displacement in an external non-VTK-based software then you can access the point scalars as a numpy array and write to file in any format using a few lines of Python script. Probably you can also use a VTK filter to convert the point scalars to a vtkTable and use VTK delimited file writer to export to a csv file.</p>

---
