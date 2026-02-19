---
topic_id: 29945
title: "How To Connect Node List To Qmrml Treeview"
date: 2023-06-09
url: https://discourse.slicer.org/t/29945
---

# How to connect node list to qmrml Treeview ?

**Topic ID**: 29945
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/how-to-connect-node-list-to-qmrml-treeview/29945

---

## Post #1 by @bongo_kat (2023-06-09 15:42 UTC)

<p>Hello,</p>
<p>I’m new to 3d Slicer and I’m trying to create a module for calibrating my files. I have python scripts that temporally and spatially calibrate my files.<br>
I want to import my files through slicer’s Data module and I would like to be able to view and select it through treeview widget like the image below.</p>
<p>My goal is to be able to execute my python script calibration on one or more selected files.<br>
But first, how can I list my nodes on the Treeview ? Is it through the modules python script?<br>
Can someone please give an example or pointers to this direction?</p>
<p>I’m hoping with your help I will understand how module development works. Thank you very much for your time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/861a3f5aaa38afdf277ffa8ba3b69d2ed951f901.png" data-download-href="/uploads/short-url/j8kdoj0OWwsL0B361oEfIQEYuAN.png?dl=1" title="thumbnail_image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861a3f5aaa38afdf277ffa8ba3b69d2ed951f901_2_690x350.png" alt="thumbnail_image" data-base62-sha1="j8kdoj0OWwsL0B361oEfIQEYuAN" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861a3f5aaa38afdf277ffa8ba3b69d2ed951f901_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861a3f5aaa38afdf277ffa8ba3b69d2ed951f901_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861a3f5aaa38afdf277ffa8ba3b69d2ed951f901_2_1380x700.png 2x" data-dominant-color="2C2C2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_image</span><span class="informations">1494×758 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-16 14:46 UTC)

<p>There are a number of widgets for selecting nodes, such as <code>qMRMLNodeComboBox</code> or <code>qMRMLSubjectHierarchyTreeView</code>. Ther <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab Slicer programming tutorial</a> may be a good start.</p>

---
