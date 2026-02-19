---
topic_id: 16963
title: "Extension Versions"
date: 2021-04-06
url: https://discourse.slicer.org/t/16963
---

# Extension versions

**Topic ID**: 16963
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/extension-versions/16963

---

## Post #1 by @LorenzE (2021-04-06 12:05 UTC)

<p>Is it possible to build a loadable extension with the newest Slicer version, i.e., 4.13, and install it in an older slicer version, i.e., 4.11?</p>

---

## Post #2 by @pieper (2021-04-06 12:49 UTC)

<p>No, as a general rule everything needs to match exactly for a loadable module to work (compiler, OS, code version…).  This is a C++ thing, not specific to Slicer.</p>

---

## Post #3 by @LorenzE (2021-04-06 15:57 UTC)

<p>Thanks for the reply. I created a .zip via cpack of a pure python based extension developed with Slicer 4.13. But I am still not able to install the .zip file in Slicer 4.11. Is there something I need to be aware of when trying to install a python extension in an older version, or should it work out of the box?</p>

---

## Post #4 by @pieper (2021-04-06 22:17 UTC)

<p>If it’s pure python it should work across versions since 4.11 and 4.13 are pretty similar, but you can look in the error log and the python console for any message to indicate something going wrong.</p>
<p>If it’s just python scripted modules you can also put them in a directory and use the Edit-&gt;Application Settings-&gt; Modules panel to add a path to that directory and they should be discovered when you start slicer.</p>

---

## Post #5 by @lassoan (2021-04-19 12:59 UTC)

<p>The Major.Minor version number is used to generate subfolder name within the zip file to prevent using incompatible packages. If you are sure that the scripts work in both Slicer-4.11 then rename all the <code>Slicer-4.13</code> folders in the zip file to <code>Slicer-4.11</code>.</p>

---
