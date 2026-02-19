---
topic_id: 18067
title: "Help With Rendering Labelmap"
date: 2021-06-10
url: https://discourse.slicer.org/t/18067
---

# Help with rendering labelmap

**Topic ID**: 18067
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/help-with-rendering-labelmap/18067

---

## Post #1 by @sannpeterson (2021-06-10 19:05 UTC)

<p>When I load a labeled segmentation, the colors on the rendered volume shows up differently from the original. What am I doing wrong?</p>

---

## Post #2 by @lassoan (2021-06-10 23:04 UTC)

<p>Labelmap volumes do not store segment names or colors. You need to select a color table that defines name and color for each label value.</p>
<p>What is your complete workflow? Do you have a color table for your labelmap volume?</p>

---

## Post #3 by @sannpeterson (2021-06-11 18:33 UTC)

<p>Thank you! I figured it out based on what you said.</p>

---

## Post #4 by @sannpeterson (2021-06-11 18:35 UTC)

<p>Is there a way to permanently add a color table to the built-in list and/or set it as the default? Or do I have to upload the ctbl file each time I load a labelmap?</p>

---

## Post #5 by @lassoan (2021-06-11 18:49 UTC)

<p>You only need to load a color table into the Slicer scene once, when you import the labelmap into segmentation. Then you can just use segmentation, which takes care of maintaining all the segment names and colors, even if you split and merge segments or move them around across different segmentations, even if segments overlap. None of these can be done using static color tables.</p>
<p>You can access all the segmentation labels and metadata stored in a segmentation .nrrd file from Python using <a href="https://github.com/lassoan/slicerio">slicerio</a> in any Python environment. We participate in development efforts for creating modern file formats biomedical imaging (<a href="https://ngff.openmicroscopy.org/latest/">OME-Zarr</a>) and will provide converters to/from this file format in Slicer in the near future. So, it should not be necessary to go back to static color tables ever again.</p>

---
