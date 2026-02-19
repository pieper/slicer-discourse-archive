---
topic_id: 36147
title: "Colormap Loading Issue After Scene Save"
date: 2024-05-14
url: https://discourse.slicer.org/t/36147
---

# Colormap loading issue after scene save

**Topic ID**: 36147
**Date**: 2024-05-14
**URL**: https://discourse.slicer.org/t/colormap-loading-issue-after-scene-save/36147

---

## Post #1 by @connorh (2024-05-14 15:20 UTC)

<p>I’m creating custom colormaps for a tool I’ve developed. If I create a continuous colormap I can save the scene, close, reload, and the colormap works as expect.</p>
<p>When I create discrete colormaps, it works initially, but when the scene is saved, closed, and reopened the colormap has no data.</p>
<p>I’m creating the discrete colormap by this function:</p>
<pre><code class="lang-auto">def CreateCustomColormap():
    """
      more on discrete colormap nodes https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-color-table-node
    """
    title = "Test Colormap"
    colorNode = slicer.mrmlScene.GetFirstNodeByName("TestColormap")
    if colorNode is None:
        colorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLColorTableNode")
        colorNode.SetTypeToUser()
        colorNode.HideFromEditorsOff()
        slicer.mrmlScene.AddNode(colorNode)
        colorNode.UnRegister(None)  # to prevent memory leaks

        colorNode.SetName(slicer.mrmlScene.GenerateUniqueName("TestColormap"))
        

        colorNode.SetNumberOfColors(3)
        colorNode.SetNamesInitialised(True)
        scalars_to_colours = [(0, [210, 210, 210]), (1, [255, 255, 25]), (2, [255, 0, 0])]
        for (label, colour) in scalars_to_colours:
            colorNode.SetColor(label, "", colour[0] / 255, colour[1] / 255, colour[2] / 255)

    return colorNode.GetID()
</code></pre>
<p>I’ve tried this in the latest preview version of Slicer and in 5.6.1.</p>
<p>When initially created:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b52ef51560c4a9cd962bae3e6904d087e268a399.png" data-download-href="/uploads/short-url/pQP1IXCT0m0bm1sdjsFV3ReJI7v.png?dl=1" title="DataIsThereColormap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b52ef51560c4a9cd962bae3e6904d087e268a399_2_382x374.png" alt="DataIsThereColormap" data-base62-sha1="pQP1IXCT0m0bm1sdjsFV3ReJI7v" width="382" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b52ef51560c4a9cd962bae3e6904d087e268a399_2_382x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b52ef51560c4a9cd962bae3e6904d087e268a399_2_573x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b52ef51560c4a9cd962bae3e6904d087e268a399_2_764x748.png 2x" data-dominant-color="2E2E2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DataIsThereColormap</span><span class="informations">864×846 17.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After scene save/close/reopen.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d93e2b35793e50beeb8e2507ad8ee56ac02dc4d2.png" data-download-href="/uploads/short-url/uZOO2tbmTQCA8eIJRYoU0ASzfQS.png?dl=1" title="LostInfoColormap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93e2b35793e50beeb8e2507ad8ee56ac02dc4d2_2_348x500.png" alt="LostInfoColormap" data-base62-sha1="uZOO2tbmTQCA8eIJRYoU0ASzfQS" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93e2b35793e50beeb8e2507ad8ee56ac02dc4d2_2_348x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93e2b35793e50beeb8e2507ad8ee56ac02dc4d2_2_522x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d93e2b35793e50beeb8e2507ad8ee56ac02dc4d2_2_696x1000.png 2x" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LostInfoColormap</span><span class="informations">855×1226 17.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for any pointers!</p>

---
