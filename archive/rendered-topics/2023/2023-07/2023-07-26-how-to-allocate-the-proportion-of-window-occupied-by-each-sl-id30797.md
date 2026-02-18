# How to allocate the proportion of window occupied by each slicewidget?

**Topic ID**: 30797
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/how-to-allocate-the-proportion-of-window-occupied-by-each-slicewidget/30797

---

## Post #1 by @jay1987 (2023-07-26 09:17 UTC)

<p>i use the code below to custom 3d slicer layout</p>
<pre><code class="lang-auto">def custom_layout(self):
    customLayout = """
      &lt;layout type="vertical" split="true"&gt;
          &lt;item splitSize="150"&gt;
            &lt;layout type="horizontal"&gt;
            &lt;item&gt;
              &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
              &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
              &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
              &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
              &lt;/view&gt;
            &lt;/item&gt;
            &lt;item&gt;
              &lt;view class="vtkMRMLViewNode" singletontag="1"&gt;
              &lt;property name="viewlabel" action="default"&gt;1&lt;/property&gt;
              &lt;/view&gt;
            &lt;/item&gt;
            &lt;/layout&gt;
          &lt;/item&gt;
          &lt;item splitSize="150"&gt;
            &lt;layout type="horizontal" split="true"&gt;
            &lt;item splitSize="130"&gt;
              &lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;
                &lt;property name="orientation" action="default"&gt;Coronal&lt;/property&gt;
                &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
                &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;
              &lt;/view&gt;
            &lt;/item&gt;
            &lt;item splitSize="20"&gt;
              &lt;view class="vtkMRMLSliceNode" singletontag="Green2"&gt;
                &lt;property name="orientation" action="default"&gt;Coronal&lt;/property&gt;
                &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
                &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;
              &lt;/view&gt;
            &lt;/item&gt;
            &lt;/layout&gt;
          &lt;/item&gt;
      &lt;/layout&gt;
    """
    customLayoutId=503
    layoutManager = slicer.app.layoutManager()
    layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)
    layoutManager.setLayout(customLayoutId)
</code></pre>
<p>i want to make the proportion is 13:2<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd0f61bc3560a9c90563faf7b02576e3805c96af.png" alt="image" data-base62-sha1="vxAtwO5Z18pcffj5C3teNNb5AyX" width="633" height="205"></p>
<p>but the actual result is below,the proportion is more like 2:1,how to make the proportion to 13:2 then?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d16ac027d50da7a281927edc6a15bc74350e6d1.png" data-download-href="/uploads/short-url/8IpHoYMREs77F2OUxshx06D6KgV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d16ac027d50da7a281927edc6a15bc74350e6d1_2_690x448.png" alt="image" data-base62-sha1="8IpHoYMREs77F2OUxshx06D6KgV" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d16ac027d50da7a281927edc6a15bc74350e6d1_2_690x448.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d16ac027d50da7a281927edc6a15bc74350e6d1_2_1035x672.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d16ac027d50da7a281927edc6a15bc74350e6d1_2_1380x896.png 2x" data-dominant-color="2A2A29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1414×919 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @icedream (2023-07-28 01:44 UTC)

<p>i use splitsize 500 by 500,it works fine!</p>

---

## Post #3 by @jay1987 (2023-07-28 05:23 UTC)

<p>If the ratio is close to 1, the result is correct, but if the ratio is less than 0.5, the result is inaccurate</p>

---

## Post #4 by @icedream (2023-07-30 08:18 UTC)

<p>yes,the result is inaccurate</p>

---

## Post #5 by @lassoan (2023-07-31 01:46 UTC)

<p>Everything works as it is supposed to, the issue is just layout sizing is an extremely complex topic. Layout is computed by Qt, taking into account hundreds of constraints (minimum/maximum sizes and stretch factors and size policies for every widget) that may be somewhat contradicting.</p>
<p><code>splitSize</code> calls <code>setSizes</code> method of <a href="https://doc.qt.io/qt-6/qsplitter.html">QSplitter</a>. The sizes are absolute (defined in device-independent pixels). If you specify a smaller size than the minimum size (dictated by the slice view controller - the slider, buttons, labels above the image) then the <code>splitSize</code> has no effect. If you specify a larger size than the size than available in the view layout then Qt will try to respect the specified sizes as much as possible. If it is impossible to respect all the constraints then Qt will allocate the avaialable space according to the requested sizes: sections with larger <code>splitSize</code> will be allocated larger area. Therefore, to set a ratio of 1:2 between two widgets, you can set their sizes to 10000:20000.</p>
<p>Note that minimum widget sizes will still be respected. So, if you request size of 10000 and 50000 then the size ratio may not be 1:5 if that would make the first section smaller than the minimum size. Instead, the first section’s size will be set to the minimum size and the other section will get the remaining space.</p>

---

## Post #6 by @jay1987 (2023-07-31 01:51 UTC)

<p>thank you lassoan, This answer is very professional !</p>

---

## Post #7 by @jay1987 (2023-07-31 03:44 UTC)

<p>hide the controller bar of all slice widget , it can be adjust into a right size ratio,thank you lassoan for sugggestion!!</p>

---
