---
topic_id: 33744
title: "Import 3D Images From Philips Affinity 70"
date: 2024-01-12
url: https://discourse.slicer.org/t/33744
---

# Import 3D images from Philips Affinity 70

**Topic ID**: 33744
**Date**: 2024-01-12
**URL**: https://discourse.slicer.org/t/import-3d-images-from-philips-affinity-70/33744

---

## Post #1 by @emanuel_ozcoidi (2024-01-12 01:31 UTC)

<p>Translated by Google Translate:</p>
<blockquote>
<p>Help, please! When following the recommended sequence for loading 3D ultrasounds into slicer, I get the following banner “Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?” with the detail of 1: US [50] [Image sequence]: Image spacing may need to be calibrated for accurate size measurements. How can I fix this error? Could it be the problem that I’m exporting the files from the Philips Affinity 70 and not from the QLAB? BEST REGARDS!</p>
</blockquote>
<p>Original text in Spanish:</p>
<blockquote>
<p>ayuda, por favor! al seguir la secuencia recomendada para cargar ecografias 3D en slicer, me aparece el siguiente cartel “Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?” con el detalle de 1: US [50] [Image sequence]: Image spacing may need to be calibrated for accurate size measurements. Como puedo solucionar dicho error? puede ser el problema que estoy exportando los archivos desde el Philips Affinity 70 y no desde el QLAB? SALUDOS!</p>
</blockquote>

---

## Post #2 by @lassoan (2024-01-12 01:32 UTC)

<p>If you want to load 3D/4D ultrasound images from Philips systems then you need to export them from QLab as Cartesian image as described <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#import-philips-4d-cardiac-images">here</a>.</p>

---
