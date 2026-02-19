---
topic_id: 14265
title: "Unit Tests For Command Line And Loadable Modules"
date: 2020-10-27
url: https://discourse.slicer.org/t/14265
---

# Unit tests for command line and loadable modules

**Topic ID**: 14265
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/unit-tests-for-command-line-and-loadable-modules/14265

---

## Post #1 by @Mik (2020-10-27 08:06 UTC)

<p>Couple of questions about testing:</p>
<ol>
<li>Are there any unit tests recommendations for command line interface and loadable modules?</li>
<li>How to use Slicer test data (md5 checksum file), if command line module needs CT data as an input value?</li>
</ol>
<p>For example CLI module:</p>
<ol>
<li>Input data: CT volume and several parameters;</li>
<li>Output data: a scalar volume and several temporary files.</li>
</ol>
<p>Test checks that temporary files are created during data processing and the output scalar volume has proper dimension and size in bytes.</p>

---
