---
topic_id: 14844
title: "Write Loadable Reader Module To Import Custom Data To Slicer"
date: 2020-12-02
url: https://discourse.slicer.org/t/14844
---

# Write loadable reader module to import custom data to Slicer

**Topic ID**: 14844
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/write-loadable-reader-module-to-import-custom-data-to-slicer/14844

---

## Post #1 by @keri (2020-12-02 04:38 UTC)

<p>Hi,</p>
<p>My data is writen in hdf5 container and may be represented as <code>vtkImageData</code>.<br>
I’m trying to write module that allows me to upload this data to Slicer so it would be possible to work with this data in Slicer (I think it should become visible in <code>Data</code> module and <code>Volume</code> module).</p>
<p>Which Slicer’s module should I work with to do that? I thought it is <code>Data</code> module but I should be mistaken as I can’t see any <code>Data</code>'s method that allows me to “register” my data in Slicer scope.</p>

---

## Post #2 by @lassoan (2021-09-30 13:40 UTC)

<p>You can use the <a href="https://github.com/SlicerRt/SlicerRT/tree/master/VffFileReader">VFF file reader in SlicerRT</a> as an example.</p>

---

## Post #3 by @keri (2021-09-30 14:01 UTC)

<p>Thank you!</p>
<p>For now I’ve implemented some custom GUI API aimed at reading my data.<br>
But in the future I think I will rework them to make it more similar to Slicer native IO modules. I will come back then to that topic and see the example you gave me.</p>

---
