---
topic_id: 24317
title: "Python Code To Place Fiducial Markers Into Slicer"
date: 2022-07-14
url: https://discourse.slicer.org/t/24317
---

# Python code to place fiducial markers into slicer

**Topic ID**: 24317
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/python-code-to-place-fiducial-markers-into-slicer/24317

---

## Post #1 by @mxtt (2022-07-14 15:51 UTC)

<p>I am trying to place fiducial markers down, but not with the widget or GUI. I am wondering how I can do this in my python code. I have a text file with a list of coordinates, and I want to place the markers at those coordinates. Any help would be appreciated. Thanks.</p>

---

## Post #2 by @mangotee (2022-07-14 16:17 UTC)

<p>Here’s one way to do it: Read your text file into a Nx3 numpy array (here: <code>arr</code>), then create or get the desired fiducial node (here: <code>nfids</code>, class: <code>slicer.vtkMRMLMarkupsFiducialNode</code>). With these two, you can use the following function to place fiducials into that node (with or without names):</p>
<pre><code class="lang-python">def fiducialListFromArray(nfids, arr, listFidNames=None):
    nrfids = arr.shape[0]
    if listFidNames is None:
        listFidNames = ['%s-%d'%(nfids.GetName(),i+1) for i in range(nrfids)]
    for i in range(nrfids):
        nfids.AddFiducial(arr[i,0], arr[i,1], arr[i,2], listFidNames[i])
    return nfids
</code></pre>

---

## Post #3 by @mxtt (2022-07-14 16:28 UTC)

<pre><code class="lang-python">slicer.modules.markups.logic().AddFiducial(x, y, z)
</code></pre>
<p>I think this will work right?</p>

---

## Post #4 by @jcfr (2022-07-15 16:49 UTC)

<p><a class="mention" href="/u/mxtt">@mxtt</a>  Reading the <code>Markups</code> section of the “Script Repository” should help you move forward:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups</a></p>
<blockquote>
<p>place fiducial markers down, but not with the widget or GUI. […] do this in my python code</p>
</blockquote>
<p>More specifically, the entry <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically">Adding control points Programmatically</a></p>

---
