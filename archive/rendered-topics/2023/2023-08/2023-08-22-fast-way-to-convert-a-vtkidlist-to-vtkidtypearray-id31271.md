---
topic_id: 31271
title: "Fast Way To Convert A Vtkidlist To Vtkidtypearray"
date: 2023-08-22
url: https://discourse.slicer.org/t/31271
---

# Fast way to convert a vtkIdList to vtkIdTypeArray

**Topic ID**: 31271
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/fast-way-to-convert-a-vtkidlist-to-vtkidtypearray/31271

---

## Post #1 by @lucsdjango (2023-08-22 03:43 UTC)

<p>Hello</p>
<p>I am working on a python scripted module and want to convert a vtkIdList (output from vtkStaticPointLocator::FindPointsWithinRadius) to a vtkIdTypeArray. What is the best way to do this?</p>
<p>So far I have only found code examples where they iterate through all items, adding them to the array, which for me runs quite slow.</p>
<p>I have not found any working examples using vtkIdList::SetArray, and cannot seem to get it working myself. Is there an quick way to access vtkIdList’s underlying array?</p>
<p>Thankful for any advice!<br>
/Jens</p>

---
