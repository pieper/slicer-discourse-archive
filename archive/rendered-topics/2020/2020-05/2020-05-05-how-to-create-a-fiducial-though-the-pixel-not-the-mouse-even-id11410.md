---
topic_id: 11410
title: "How To Create A Fiducial Though The Pixel Not The Mouse Even"
date: 2020-05-05
url: https://discourse.slicer.org/t/11410
---

# How to create a fiducial though the pixel not the mouse event

**Topic ID**: 11410
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/how-to-create-a-fiducial-though-the-pixel-not-the-mouse-event/11410

---

## Post #1 by @timeanddoctor (2020-05-05 01:23 UTC)

<p>I went creat fiducial in the 3d view just give the x,y coordinate, and I found some information maybe help for me. But I don’t know how to use it.</p>
<pre><code class="lang-auto">virtual int vtkSlicerMarkupsWidget::AddNodeOnWidget ( const int *displayPos* [2] ) virtual
</code></pre>
<p>Given a specific X, Y pixel location, add a new node on the widget at this location.</p>

---

## Post #2 by @lassoan (2020-05-05 03:59 UTC)

<p>This operation is called point picking. Model displayable manager has a point picker that you can use:</p>
<pre><code class="lang-python">displayPosition = [100,120]

# Get model displayable manager
modelDisplayableManager = None
threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
managers = vtk.vtkCollection()
threeDViewWidget.getDisplayableManagers(managers)
for i in range(managers.GetNumberOfItems()):
  obj = managers.GetItemAsObject(i)
  if obj.IsA('vtkMRMLModelDisplayableManager'):
    modelDisplayableManager = obj
    break

# Use model displayable manager's point picker
pickedPosition = []
if modelDisplayableManager.Pick(displayPosition[0], displayPosition[1]):
    rasPositionArray = vtk.vtkDoubleArray()
    rasPositionArray.SetVoidArray(modelDisplayableManager.GetPickedRAS(),3,1)
    rasPosition = [rasPositionArray.GetValue(i) for i in range(3)]

print(rasPosition)
</code></pre>

---

## Post #3 by @lassoan (2023-06-16 19:14 UTC)

<p>In current Slicer version, the code snippet is much simpler -  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-3d-coordinates-from-2d-display-coordinates">see in the script repository</a>.</p>

---
