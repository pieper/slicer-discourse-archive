# Importing PLY with Color

**Topic ID**: 5500
**Date**: 2019-01-24
**URL**: https://discourse.slicer.org/t/importing-ply-with-color/5500

---

## Post #1 by @Nicholas.jacobson (2019-01-24 21:12 UTC)

<p>Hi All,<br>
I am importing a PLY file with color from 4d flow. It imports well but is missing the color. This color is coming through in other software so I know there is information in the file. Any advice for activating color importing a PLY?</p>
<p>nick</p>

---

## Post #2 by @lassoan (2019-01-24 21:16 UTC)

<p>You can use Models module Scalars section to choose which point or cell data to use for coloring and how. See information here: <a href="https://discourse.slicer.org/t/ply-file-colors-not-displayed/4206/6?u=lassoan" class="inline-onebox">PLY file colors not displayed</a></p>
<p>There are various ways to store colors and scalars in a PLY file, so if your format is not supported then send us a sample and we’ll have a look.</p>

---

## Post #3 by @Nicholas.jacobson (2019-01-24 21:19 UTC)

<p>Ah that works! Thanks.</p>

---

## Post #4 by @Nicholas.jacobson (2019-02-22 03:47 UTC)

<p>Can these ply imports be converted into a volume rendering for bitmap printing?</p>

---

## Post #5 by @lassoan (2019-03-13 14:22 UTC)

<p>It could be possible to implement a slicing algorithm for models, similarly how we slice images. However, computing colored filling based on surface point colors would not be trivial. An alternative approach could be to convert the model to an image and then colorize it using nearby points.</p>
<p>As far as I know, most color 3D printers usually take a colored mesh as input, so I’m not sure if you need bitmap printing for such models.</p>

---
