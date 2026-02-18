# Importing a Volume in VTK (.vtk) format

**Topic ID**: 11104
**Date**: 2020-04-13
**URL**: https://discourse.slicer.org/t/importing-a-volume-in-vtk-vtk-format/11104

---

## Post #1 by @kalpathi (2020-04-13 17:55 UTC)

<p>I have a volume in vtk format (structured points) and am trying to import it into Slicer. I was expecting to see the 3 slice views show up with the data none so far…</p>
<p>Any pointers would be appreciated. Thanks.</p>
<p>Should it be in binary format? I do remember vaguely reading something about that some place…</p>
<p>Here is the header fo the data file:</p>
<p>vtk output</p>
<pre><code class="lang-auto">ASCII

DATASET STRUCTURED_POINTS

DIMENSIONS 400 280 131

SPACING 1 1 1

ORIGIN 0 0 0

POINT_DATA 14672000

SCALARS scalars double

LOOKUP_TABLE default

65 17 0 24 31 27 19 57 61 

31 37 40 59 29 60 67 95 54 

63 80 103 0 55 44 91 25
</code></pre>

---

## Post #2 by @lassoan (2020-04-13 17:58 UTC)

<p>Legacy .vtk file format can store various data types (images, surface meshes, unstructured grids, etc.). You need to specify in Add data dialog’s description section how you want to interpret the data. If it is an image volume then choose “Volume”.</p>

---

## Post #3 by @kalpathi (2020-04-20 00:01 UTC)

<p>Thanks a whole bunch… that helped!</p>
<pre><code>  -- krs</code></pre>

---
