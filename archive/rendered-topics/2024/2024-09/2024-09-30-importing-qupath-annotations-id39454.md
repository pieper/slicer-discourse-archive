---
topic_id: 39454
title: "Importing Qupath Annotations"
date: 2024-09-30
url: https://discourse.slicer.org/t/39454
---

# Importing QuPath annotations

**Topic ID**: 39454
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/importing-qupath-annotations/39454

---

## Post #1 by @NatasjaD (2024-09-30 11:46 UTC)

<p>Hi I am segmenting and annotating the different nuclei of the human amygdala on brightfield sections in QuPath and I would like to import these annotations into 3D Slicer. The common file format used for export of QuPath annotations is GeoJSON. Is this possible to import in 3D Slicer?</p>

---

## Post #2 by @pieper (2024-09-30 13:27 UTC)

<p>I don’t think there’s an existing parser for GeoJSON but it should be easy to write a python script for it, maybe with <a href="https://pypi.org/project/geojson/">this package</a>.  If you try and run into questions you could post an example file and image and someone can probably help you out (e.g. include a screenshot of what it looks like in QuPath, the json, and an image file).</p>

---
