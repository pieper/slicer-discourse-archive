---
topic_id: 530
title: "Get Array From Image Data"
date: 2017-06-19
url: https://discourse.slicer.org/t/530
---

# Get array from image data

**Topic ID**: 530
**Date**: 2017-06-19
**URL**: https://discourse.slicer.org/t/get-array-from-image-data/530

---

## Post #1 by @jks1995 (2017-06-19 18:10 UTC)

<p>How could i get the arrays that make up an image data object as arrays in python?</p>

---

## Post #2 by @ihnorton (2017-06-19 19:22 UTC)

<p>Please see</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>

---

## Post #3 by @jks1995 (2017-06-26 17:33 UTC)

<p>The solution I was looking for was:</p>
<code>
slicer.util.array('NodeName')
</code>

---
