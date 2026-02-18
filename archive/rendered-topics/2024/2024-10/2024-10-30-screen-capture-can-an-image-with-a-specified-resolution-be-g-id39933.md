# Screen capture:Can an image with a specified resolution be generated. For example, 512 × 512.or Adjust the view to a specified resolution or size

**Topic ID**: 39933
**Date**: 2024-10-30
**URL**: https://discourse.slicer.org/t/screen-capture-can-an-image-with-a-specified-resolution-be-generated-for-example-512-x-512-or-adjust-the-view-to-a-specified-resolution-or-size/39933

---

## Post #1 by @linhuanfeng (2024-10-30 08:16 UTC)

<p>screen capture:Can an image with a specified resolution be generated. For example, 512 × 512.or Adjust the view to a specified resolution or size</p>

---

## Post #2 by @pieper (2024-10-30 14:34 UTC)

<p>If you are doing this in a script you can temporarily unparent the view and specify the resolution you want and then restore the layout afterwards, something like this:</p>
<pre><code class="lang-auto">tdv = slicer.app.layoutManager().threeDWidget(0)
tdv.setParent(None)
tdv.show()
tdv.size = qt.QSize(512,512)
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutConventionalView)
</code></pre>

---

## Post #3 by @linhuanfeng (2024-10-30 15:16 UTC)

<p>How to operate other views, such as Axial, Sagittal, or Coronal.</p>

---

## Post #4 by @pieper (2024-10-30 16:00 UTC)

<p>You can do the same, just get sliceWidgets by view id from the layoutManager.</p>
<p>Like <code>slicer.app.layoutManager().sliceWidget('Red')</code></p>

---
