---
topic_id: 14878
title: "What Does This Second Part Of The Code Mean Python"
date: 2020-12-04
url: https://discourse.slicer.org/t/14878
---

# What does this second part of the code mean? Python

**Topic ID**: 14878
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/what-does-this-second-part-of-the-code-mean-python/14878

---

## Post #1 by @NoobForSlicer (2020-12-04 05:35 UTC)

<h1>Change spacing</h1>
<pre><code>    logging.info("change spacing")
    start = time.time()
    ijkToRas = vtk.vtkMatrix4x4()
    imagenode.GetIJKToRASMatrix(ijkToRas)
    for i in range(3):
        ijkToRas.SetElement(i, i, spacing[i])
    imagenode.SetIJKToRASMatrix(ijkToRas)
    end = time.time()
    logging.info(f"change spacing in {human_time(end-start)}")
    slicer.app.processEvents()
</code></pre>
<p>This part " ijkToRas.SetElement(i, i, spacing[i])"?</p>

---

## Post #2 by @lassoan (2020-12-04 16:33 UTC)

<p>IJK to RAS transform is the mapping from voxel coordinate system (IJK) to physical space (RAS). If IJKtoRAS is a diagonal matrix then the first 3 values in the diagonal specifies the image spacing (voxel size).</p>

---
