---
topic_id: 5064
title: "Input Segments In New Module"
date: 2018-12-12
url: https://discourse.slicer.org/t/5064
---

# Input segments in new module

**Topic ID**: 5064
**Date**: 2018-12-12
**URL**: https://discourse.slicer.org/t/input-segments-in-new-module/5064

---

## Post #1 by @ThomPote (2018-12-12 23:10 UTC)

<p>Hi,</p>
<p>I’m trying to create a new module.</p>
<p>I can select differents nodes like Volume and Segmentation node as input.</p>
<p>But how can I select my different segments in Segmentation as input before running the analyse with apply button ?</p>
<p>Thanks for all</p>

---

## Post #2 by @cpinter (2018-12-12 23:15 UTC)

<p>Is your module C++ or Python?</p>

---

## Post #3 by @ThomPote (2018-12-12 23:38 UTC)

<p>Only in Python for the moment</p>
<p>Thanks</p>

---

## Post #4 by @cpinter (2018-12-12 23:49 UTC)

<p>We don’t have a widget for that just yet. But we have examples. Please follow this variable through this code and you can easily replicate it:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L81" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L81" target="_blank" rel="nofollow noopener">SlicerRt/SegmentRegistration/blob/master/SegmentRegistration/SegmentRegistration.py#L81</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="71" style="counter-reset: li-counter 70 ;">
<li>self.fixedSegmentationNodeCombobox = slicer.qMRMLNodeComboBox()</li>
<li>self.fixedSegmentationNodeCombobox.nodeTypes = ( ("vtkMRMLSegmentationNode"), "" )</li>
<li>self.fixedSegmentationNodeCombobox.noneEnabled = False</li>
<li>self.fixedSegmentationNodeCombobox.setMRMLScene( slicer.mrmlScene )</li>
<li>self.fixedSegmentationNodeCombobox.setToolTip( "Select fixed segmentation" )</li>
<li>self.fixedSegmentationNodeCombobox.name = "fixedSegmentationNodeCombobox"</li>
<li>self.registrationCollapsibleButtonLayout.addRow('Fixed segmentation: ', self.fixedSegmentationNodeCombobox)</li>
<li>self.fixedSegmentationNodeCombobox.connect('currentNodeChanged(vtkMRMLNode*)', self.onFixedSegmentationNodeSelectionChanged)</li>
<li>
</li>
<li># Fixed segment name combobox</li>
<li class="selected">self.fixedSegmentNameCombobox = qt.QComboBox()</li>
<li>self.registrationCollapsibleButtonLayout.addRow('Fixed segment: ', self.fixedSegmentNameCombobox)</li>
<li>self.fixedSegmentNameCombobox.connect('currentIndexChanged(QString)', self.onFixedSegmentSelectionChanged)</li>
<li>self.fixedSegmentNameCombobox.enabled = False</li>
<li>
</li>
<li># Moving volume node combobox</li>
<li>self.movingVolumeNodeCombobox = slicer.qMRMLNodeComboBox()</li>
<li>self.movingVolumeNodeCombobox.nodeTypes = ( ("vtkMRMLScalarVolumeNode"), "" )</li>
<li>self.movingVolumeNodeCombobox.showChildNodeTypes = False</li>
<li>self.movingVolumeNodeCombobox.noneEnabled = False</li>
<li>self.movingVolumeNodeCombobox.setMRMLScene( slicer.mrmlScene )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @lassoan (2018-12-13 00:24 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> you’ve implemented a segment selector widget - <em>qMRMLSegmentSelectorWidget</em> - which includes a segmentation node selector and a segment selector combobox:</p>
<pre><code class="lang-auto">sw=slicer.qMRMLSegmentSelectorWidget()
sw.setMRMLScene(slicer.mrmlScene)
sw.setCurrentNode(getNode('Segmentation'))
sw.show()
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba560a18125760647b06393241c1cf7b94633576.png" alt="image" data-base62-sha1="qAp9bpW2TqgjaJXQ4JaxLEmQrVY" width="514" height="275"></p>
<p>For selecting multiple segments, you can use <em>qMRMLSegmentsTableView</em> (you need to add a segmentation node selector separately):</p>
<pre><code class="lang-auto">st=slicer.qMRMLSegmentsTableView()
st.setMRMLScene(slicer.mrmlScene)
st.setSegmentationNode(getNode('Segmentation'))
st.show()
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc695ae62274f06633dfe155eab6691e91b49b36.png" alt="image" data-base62-sha1="vrQLtmHg4vB0ymUOhpK3ED3bApw" width="632" height="194"></p>

---

## Post #6 by @cpinter (2018-12-13 02:42 UTC)

<p>Wow you’re right <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Not sure why I still have the old way in those python modules. Thanks for remembering better what I did than myself <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @Saima (2021-09-12 01:55 UTC)

<p>Hi Andras,<br>
How can I get the selected segment using the selectorwidgot using python script.</p>
<p>I get the segmentationNode but how can I get the selected segment from the qmrmlsegmentselectorwidget</p>
<p>regards,</p>
<p>Saima Safdar</p>

---

## Post #8 by @lassoan (2021-09-12 02:10 UTC)

<p>Have you tried to use the <a href="https://apidocs.slicer.org/master/classqMRMLSegmentsTableView.html#a0c20e258ba22fcd494a96829e0ddb146">selectedSegmentIDs</a> method?</p>

---

## Post #9 by @Saima (2021-09-12 04:24 UTC)

<p>no I cannot use it with segmentationNode.</p>
<p>Do you have any example where the qMRMLsegmentselectorwidget is used.</p>
<p>Thankyou for sharing</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #10 by @Saima (2021-09-12 04:49 UTC)

<p>Hi Andras,<br>
Thank you for the feedback. I found how to connect the widget in scripted module.</p>
<p>Reagrds,<br>
Saima Safdar</p>

---

## Post #11 by @lassoan (2021-09-12 11:44 UTC)

<aside class="quote no-group" data-username="Saima" data-post="10" data-topic="5064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Thank you for the feedback. I found how to connect the widget in scripted module.</p>
</blockquote>
</aside>
<p>If you find out anything non-obvious then please share it here so that others who run into this can find the solution (and we may also use the information to improve the documentation).</p>

---

## Post #12 by @Saima (2021-09-13 04:12 UTC)

<p>Yes I will share on github and provide link here.</p>

---

## Post #13 by @RafaelPalomar (2024-09-19 06:31 UTC)

<p>Hello. I’m looking for a more compact widget for selecting multiple segments and I found this post. I was wondering if there is a more recent approach for segments selection that can easily be integrated in other modules. Thanks.</p>

---

## Post #14 by @lassoan (2024-09-19 11:34 UTC)

<p>If you need to select multiple segments then I would recommend the qMRMLSegmentsTableView. This widget has filter&amp;search capabilities that are essential if you need to work with a segmentation that contains many segments (common with automatic segmentation tools).</p>
<p>Alternatively, you can use the qMRMLSegmentSelectorWidget to select a segment and an “add” button to add it to a list, and “remove” button for each added segment to remove them. This may take up a bit less space, but it is more work to implement.</p>
<p>You can also do without any segment selection and say that you work with all visible segments; or all flagged segments (you can set status of a segment in the segment list by right-clicking and choosing “Show filter bar”).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df7ccdb9bccf260b9cea5fd4b08ea2612fb2cb2e.png" data-download-href="/uploads/short-url/vT3RIwPRAPYcNPoatNQOjfZj1NQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ccdb9bccf260b9cea5fd4b08ea2612fb2cb2e_2_690x313.png" alt="image" data-base62-sha1="vT3RIwPRAPYcNPoatNQOjfZj1NQ" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ccdb9bccf260b9cea5fd4b08ea2612fb2cb2e_2_690x313.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df7ccdb9bccf260b9cea5fd4b08ea2612fb2cb2e_2_1035x469.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df7ccdb9bccf260b9cea5fd4b08ea2612fb2cb2e.png 2x" data-dominant-color="383D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1178×535 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
