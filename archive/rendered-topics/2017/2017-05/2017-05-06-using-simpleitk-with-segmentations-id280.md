# Using SimpleITK with Segmentations

**Topic ID**: 280
**Date**: 2017-05-06
**URL**: https://discourse.slicer.org/t/using-simpleitk-with-segmentations/280

---

## Post #1 by @cpinter (2017-05-06 15:51 UTC)

<p>Using the VTK oriented image data from ITK seems a bigger hassle than choosing another filter, but I’ll look into this one too.</p>

---

## Post #2 by @lassoan (2017-05-06 17:50 UTC)

<p>If I want to use an ITK filter I usually put a wrapper class in vtkITK. I haven’t tried with vtkOrientedImageData, but ITK supports oriented image data, so it might be doable (when we start working on adding orientation support to VTK images, this may be a good case for testing how orientation information can passed through the VTK pipeline). But we can just do what we do for all other VTK image filters (convert input to simple VTK image and then restore orientation information in the output image data of the filter).</p>

---

## Post #3 by @fedorov (2017-05-06 18:53 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="10" data-topic="266" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-radioactive-seeds-in-brachytherapy-patients-and-calculate-dose/266/10">Segment radioactive seeds in brachytherapy patients and calculate dose</a></div>
<blockquote>
<p>Using the VTK oriented image data from ITK seems a bigger hassle than choosing another filter, but I’ll look into this one too.</p>
</blockquote>
</aside>
<p>For me it’s the other way around - I always stay away from VTK when operating on oriented images, and get them into an ITK representation first. Here’s the latest place where I had to do it, in case it can help:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L363-L373">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L363-L373" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L363-L373" target="_blank" rel="noopener">AIM-Harvard/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L363-L373</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="363" style="counter-reset: li-counter 362 ;">
          <li></li>
          <li>def onCalculateAllFeaturesButton(self):</li>
          <li>  featureButtons = self.featuresButtonGroup.buttons()</li>
          <li>  for featureButton in featureButtons:</li>
          <li>    featureButton.checked = True</li>
          <li></li>
          <li>def onCalculateNoFeaturesButton(self):</li>
          <li>  featureButtons = self.featuresButtonGroup.buttons()</li>
          <li>  for featureButton in featureButtons:</li>
          <li>    featureButton.checked = False</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can next use use SimpleITK LabelShapeStatisticsImageFilter to get the centroid: <a href="https://itk.org/SimpleITKDoxygen100/html/classitk_1_1simple_1_1LabelShapeStatisticsImageFilter.html">https://itk.org/SimpleITKDoxygen100/html/classitk_1_1simple_1_1LabelShapeStatisticsImageFilter.html</a></p>

---

## Post #4 by @cpinter (2017-05-06 19:31 UTC)

<p>Thanks for the suggestions!</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Creating a node for the labelmap of one segment and adding it to the scene is an excessive workaround for such an operation. Also it goes against what we wanted to achieve with segmentation nodes (that there are no stray unconnected nodes around in the scene containing intermediate and potentially invalid data). I see how this is easy to do, and if you clean up afterwards (I hope you do), then it’s not too bad, but this is not an elegant solution either. I just looked at the function in segmentation logic, and adding the node to the scene does not seem necessary. Is it needed for SimpleITK? If not, then having a node which is not in the scene is much better.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Similarly, implementing a vtkITK wrapper is the “hassle” part I was referring to.</p>
<p>There are many solutions here, and many of them sound equally good (or rather, bad), but it’s still a hassle to use ITK filters in general. When Hongtao gets to the stage when he needs this part, I’ll try to choose the least bad solution.</p>

---

## Post #5 by @fedorov (2017-05-06 19:39 UTC)

<aside class="quote no-group quote-post-not-found" data-username="cpinter" data-post="13" data-topic="266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-radioactive-seeds-in-brachytherapy-patients-and-calculate-dose/266/13">Segment radioactive seeds in brachytherapy patients and calculate dose</a></div>
<blockquote>
<p>but it’s still a hassle to use ITK filters in general</p>
</blockquote>
</aside>
<p>It would be nice if in designing Slicer functionality, such as Segmentations, you guys appreciated the reality that developers would want to be able to use SimpleITK for the segmentations and image data. If you provided convenience functions to get SimpleITK image, all of those “dirty” workarounds would not be necessary, and developers would appreciate it (I would for sure).</p>

---

## Post #6 by @lassoan (2017-05-06 21:31 UTC)

<p>ITK is somewhat difficult to use in Slicer because ITK’s generic design and also because most Slicer classes are VTK classes. SimpleITK is great but it’s a huge additional layer and there are still some inconveniences (such as importing/exporting images, running in debug mode, etc.) but these may improve in the future.</p>
<p>We already have Segment editor effects implemented using SimpleITK, for example the <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py">watershed effect</a>.</p>

---

## Post #7 by @fedorov (2017-05-07 18:42 UTC)

<p>Andras, the way you get data into SimpleITK in the effect you linked is pretty much the same that I do in the code I shared. I am not sure I understand your argument about SimpleITK being “a huge additional layer” - it is already part of Slicer, there is no extra layer to add. I personally find SimpleITK a lot easier and more intuitive to use than VTK classes.</p>

---

## Post #8 by @cpinter (2017-05-08 01:10 UTC)

<p>I agree that it would be nice to have a more direct way to get SimpleITK images from segments.</p>
<p>If there is a way for the ReadImage function to specify a scene (which is not the Slicer scene just a temporary scene for example), or it is possible to convert a node that is not part of any scene, then it is already better than adding a node to the Slicer scene that emits lots of signals and may contain invalid data later (which are the two issues that make it dirty in my eyes). If not, then SimpleITK could facilitate easier conversion.</p>
<p>Segmentations needed to be written in VTK, because the entirety of Slicer (i.e. MRML) relies on VTK, and it is much more direct to display VTK objects, such as image data and poly data. This does make ITK or SimpleITK less powerful. They are powerful. Still it’s hard to dispute that it is not straightforward to use from the VTK-based Slicer. If there are ways to mitigate this, then let’s go for it!</p>

---

## Post #9 by @lassoan (2017-05-08 11:56 UTC)

<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="16" data-topic="266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-radioactive-seeds-in-brachytherapy-patients-and-calculate-dose/266/16">Segment radioactive seeds in brachytherapy patients and calculate dose</a></div>
<blockquote>
<p>Andras, the way you get data into SimpleITK in the effect you linked is pretty much the same that I do in the code I shared</p>
</blockquote>
</aside>
<p>Yes, this is how you can use SimpleITK in Slicer now. As Csaba pointed out above, if SimpleITK utility functions worked with private scenes then it would allow cleaner use of SimpleITK. I would add that it should be possible to refer to nodes by node ID and it would be nice to have convenience functions for non-image data I/O (transforms, models, markups, …). Most of these could be improved with not too much effort and it would worth doing it. It’s just a matter of priorities.</p>
<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="16" data-topic="266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-radioactive-seeds-in-brachytherapy-patients-and-calculate-dose/266/16">Segment radioactive seeds in brachytherapy patients and calculate dose</a></div>
<blockquote>
<p>I am not sure I understand your argument about SimpleITK being “a huge additional layer”</p>
</blockquote>
</aside>
<p>Large: I mean that binaries are large (160MB, about 2x the size of entire VTK, 4x larger than Qt) and increases Slicer build time buy about 20%. Slicer includes it by default, but projects that don’t need additional ITK filters (or use it from C++) build their custom Slicer without SimpleITK. Additional: it is an additional “simplification” layer on top of ITK (it is not a simplified version of ITK that replaces ITK with a smaller or simpler version).</p>
<p>We all agree that SimpleITK is great and it should be easy to use it for processing segmentations. While examples exist already, we should keep adding more examples, convenience functions, and improve documentation to help users in this.</p>

---

## Post #10 by @fedorov (2017-05-08 13:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer includes it by default, but projects that don’t need additional ITK filters (or use it from C++) build their custom Slicer without SimpleITK.</p>
</blockquote>
</aside>
<p>Makes sense.</p>
<p>Since we never build custom Slicer binaries for any of our applications, this has never been an issue for us.</p>

---
