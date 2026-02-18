# qMRMLSliceWidget has no attribute named 'imageData'

**Topic ID**: 10851
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/qmrmlslicewidget-has-no-attribute-named-imagedata/10851

---

## Post #1 by @aaron.b.tanenbaum (2020-03-26 15:39 UTC)

<p>I am using Slicer version 4.3.1 on ubuntu 16.04. I am getting the error<br>
qMRMLSliceWidget has no attribute named ‘imageData’</p>
<p>Does any know why this is happening?</p>

---

## Post #2 by @lassoan (2020-03-26 15:40 UTC)

<p>Please use latest stable or latest preview release and let us know if you find any problems.</p>

---

## Post #3 by @aaron.b.tanenbaum (2020-03-26 20:42 UTC)

<p>I installed the newer version. I get the same error plus more errors.</p>

---

## Post #4 by @lassoan (2020-03-26 21:11 UTC)

<p><a href="http://apidocs.slicer.org/master/classqMRMLSliceWidget.html#a9d165dee031dfbb2105108871173482b">qMRMLSliceWidget</a> has <code>imageDataConnection</code> method instead.</p>

---
