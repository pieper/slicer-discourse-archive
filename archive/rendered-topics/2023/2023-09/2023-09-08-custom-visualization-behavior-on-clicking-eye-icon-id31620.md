---
topic_id: 31620
title: "Custom Visualization Behavior On Clicking Eye Icon"
date: 2023-09-08
url: https://discourse.slicer.org/t/31620
---

# Custom visualization behavior on clicking "eye" icon

**Topic ID**: 31620
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/custom-visualization-behavior-on-clicking-eye-icon/31620

---

## Post #1 by @pfrwilson (2023-09-08 17:35 UTC)

<p>Hi Community,</p>
<p>My use case involves loading and visualizing tracked ultrasound sequences. I have been using the volume reslice driver to set up visualization, and have implemented a function which successfully sets up this visualization. So far I have been controlling it by using a node combo box and the “nodeActivated” signal.</p>
<p>An even better solution would be to customize the behavior of clicking the “eye” icon in the subject hierarchy view widget in my module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8918e78f2c44817b3d13606276b44234da7f82a6.png" data-download-href="/uploads/short-url/jyOLOkqGCJy2ykY0rjiLQVPzCHI.png?dl=1" title="Screenshot 2023-09-08 at 1.35.16 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8918e78f2c44817b3d13606276b44234da7f82a6_2_646x500.png" alt="Screenshot 2023-09-08 at 1.35.16 PM" data-base62-sha1="jyOLOkqGCJy2ykY0rjiLQVPzCHI" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8918e78f2c44817b3d13606276b44234da7f82a6_2_646x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8918e78f2c44817b3d13606276b44234da7f82a6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8918e78f2c44817b3d13606276b44234da7f82a6.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-08 at 1.35.16 PM</span><span class="informations">954×738 95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea how to approach this? Is a signal or event emmitted somewhere when this eye icon is clicked?</p>
<p>Paul</p>

---

## Post #2 by @ebrahim (2023-09-08 18:04 UTC)

<p>I don’t know if there’s a signal/event or how this would be customized if possible, but in case it can help <a href="https://github.com/Slicer/Slicer/blob/6fc6a2abe964263f7cdef4c57fd1675a561256f4/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.cxx#L1471-L1475" rel="noopener nofollow ugc">here is the code that gets executed when you left-click the eye.</a></p>

---

## Post #3 by @lassoan (2023-09-08 21:13 UTC)

<p>The behavior of the eye icon is designed to be customizable. All you need to do is to create a subject hierarchy plugin, make that plugin return higher value in <code>canOwnSubjectHierarchyItem</code> method and specify any behavior you need in the <code>visibilityIcon</code> method. See a complete example <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveAnnulusAnalysis/HeartValveLib/HeartValvesSubjectHierarchyPlugin.py">here</a>.</p>

---
