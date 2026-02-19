---
topic_id: 795
title: "Get Pointer To Given Element Of Markup List"
date: 2017-08-01
url: https://discourse.slicer.org/t/795
---

# Get Pointer to Given element of Markup list

**Topic ID**: 795
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/get-pointer-to-given-element-of-markup-list/795

---

## Post #1 by @gabriele.arnulfo (2017-08-01 01:36 UTC)

<p>Dear all,</p>
<p>following the use case. I have developed a segmentation algorithm that localises channel positions in single subject space for intracerebral implants. This algorithm requires as initial points the target ( head ) and cortical entry point ( tail ) of each electrode. These points should come in pairs ( both target and entry) for each electrode to be segmented. These pairs are saved in a single markup list of 2*N elements with N == number of implanted electrodes. The segmentation algorithm reconstructs the final position of each recording contact in each electrode starting from the entry/target point pairs + electrode model. The algorithm is quite robust to misplacements of the entry/target points, but sometimes ( manual error ) one of these points for some electrodes are significantly far for the expected position. At the moment, our algorithm reads the markup list and store point pairs in a vector of Electrode Objects (i.e. class that contains self.target and self.entry as members, among others). After that, the module creates a table the user can select for electrode the final model together with some other properties.Here it comes the problem I’m currently facing. While processing complex ( &gt; 10-15 electrodes ) it might happen that the user is unsatisfied by the segmentation wants to modify the position of the initial entry/target pairs. After the change, the markup list is updated but our module do not read those changes. The user can indeed reload the module, but this translate in loosing the parameters he chose. We now use the fiducial.GetNthFiducialPosition function which returns for the i-th markup the corresponding coordinate triplets. Is there a possibility to get a reference to that object instead? This will allows us to online upload the coordinate without the need of partial refactoring the logic.</p>
<p>Thanks a lot for your time</p>

---

## Post #2 by @lassoan (2017-08-01 01:43 UTC)

<p>You can use qSlicerSimpleMarkupWidget. It shows a table that is updated automatically when markups are edited and you can edit markups properties there, jump to a markup on selection, reorder markups, show/hide, change colors, activate/deactivate placement, etc. - and most importantly, you can customize its look (show/hide buttons, columns) and behavior (place single/multiple markups, get notifications when markups are changed, etc).</p>
<p>Simple example:</p>
<pre><code>w = slicer.qSlicerSimpleMarkupsWidget()
w.setMRMLScene(slicer.mrmlScene)
w.setCurrentNode(getNode('F'))
w.show()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/556c8c63d1c3fa7d6f0db99cfa9186b1ed0c249b.png" data-download-href="/uploads/short-url/cbH9edak4NZSwrOIj9vqy98DNBV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/556c8c63d1c3fa7d6f0db99cfa9186b1ed0c249b.png" alt="image" data-base62-sha1="cbH9edak4NZSwrOIj9vqy98DNBV" width="690" height="228" data-dominant-color="E9E9E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×253 9.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Documentation: <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html" class="inline-onebox">Slicer: qSlicerSimpleMarkupsWidget Class Reference</a></p>
<p>If you need a more customized look/behavior then you can use qSlicerSimpleMarkupsWidget as a template for creating your own widget.</p>

---
