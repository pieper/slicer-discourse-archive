# Switching between different volume display

**Topic ID**: 24860
**Date**: 2022-08-22
**URL**: https://discourse.slicer.org/t/switching-between-different-volume-display/24860

---

## Post #1 by @AMK (2022-08-22 11:02 UTC)

<p>Hi,</p>
<p>I have imported a Dicom file containing various volumes of pelvic and ankle of different slice thicknesses. The view window always shows the last volume imported. I can switch between different volumes by going to the ‘Data’ Module. But I am trying to implement this functionality in python. Could anyone suggest how should I proceed?</p>

---

## Post #2 by @pieper (2022-08-22 15:40 UTC)

<p>In general we suggest this method:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>For this feature you can look for the <code>PropagateVolumeSelection</code> method.</p>

---

## Post #3 by @AMK (2022-08-24 12:32 UTC)

<p>Thanks Steve for your answer. The link has proven really helpful.</p>
<p>I was able to solve using the following code. Maybe it might be helpful to someone else also.</p>
<pre><code>def displaySelectVolume(self, a):
    layoutManager = slicer.app.layoutManager()
    for sliceViewName in layoutManager.sliceViewNames():
        view = layoutManager.sliceWidget(sliceViewName).sliceView()
        sliceNode = view.mrmlSliceNode()
        sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
        compositeNode = sliceLogic.GetSliceCompositeNode()
        compositeNode.SetBackgroundVolumeID(str(a))
</code></pre>
<p>Here ‘a’ is the Mrml Node ID</p>

---
