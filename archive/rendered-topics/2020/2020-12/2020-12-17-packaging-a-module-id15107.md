---
topic_id: 15107
title: "Packaging A Module"
date: 2020-12-17
url: https://discourse.slicer.org/t/15107
---

# Packaging a module

**Topic ID**: 15107
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/packaging-a-module/15107

---

## Post #1 by @jrl (2020-12-17 08:03 UTC)

<p>This is more of a clarification question. If I created a module and wanted to pass that on to somebody, do I just “create installer package”? It’s unclear to me how to package the code for another person.</p>

---

## Post #2 by @lassoan (2020-12-19 06:37 UTC)

<p>If you build Slicer then you can build an extension package (zip file) that users can install from file using the extensions manager in Slicer.</p>
<p>If you don’t want to build Slicer then the user needs to add your module folder to additional module paths in menu: Application settings / Modules.</p>

---
