---
topic_id: 20285
title: "Annotation In 3D View Like Slice View"
date: 2021-10-21
url: https://discourse.slicer.org/t/20285
---

# Annotation in 3D view (like slice view)?

**Topic ID**: 20285
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/annotation-in-3d-view-like-slice-view/20285

---

## Post #1 by @hherhold (2021-10-21 13:19 UTC)

<p>Is there a way (in python is fine, doesn’t need to be a feature add) to add an annotation to the bottom left (or right, or top; any corner, really) of the 3D view? This post: <a href="https://discourse.slicer.org/t/display-text-in-a-3d-view/13018" class="inline-onebox">Display text in a 3D view</a> seems to talk about a Corner Annotation module, but it looks like that has been deprecated. Mostly looking for something like the label in the slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935924a247395fa821234230e95e3c0046f683b1.jpeg" data-download-href="/uploads/short-url/l1vaVXM4aXFuLnl9IJ71EjhiR57.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935924a247395fa821234230e95e3c0046f683b1_2_279x249.jpeg" alt="image" data-base62-sha1="l1vaVXM4aXFuLnl9IJ71EjhiR57" width="279" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935924a247395fa821234230e95e3c0046f683b1_2_279x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935924a247395fa821234230e95e3c0046f683b1_2_418x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/935924a247395fa821234230e95e3c0046f683b1_2_558x498.jpeg 2x" data-dominant-color="242424"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">680×608 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks!!!</p>

---

## Post #2 by @pieper (2021-10-21 17:59 UTC)

<p>You can probably find a way to make this work.  I’ve never tried changing them but here’s the code where they are implemented.  If you really only need this once you could just edit the code with the annotation you want and restart Slicer.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L18-L114">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L18-L114" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L18-L114" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L18-L114</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="18" style="counter-reset: li-counter 17 ;">
          <li>class SliceAnnotations(VTKObservationMixin):</li>
          <li>  """Implement the Qt window showing settings for Slice View Annotations</li>
          <li>  """</li>
          <li>  def __init__(self, layoutManager=None):</li>
          <li>    VTKObservationMixin.__init__(self)</li>
          <li>    self.hasVTKPVScalarBarActor = hasattr(slicer, 'vtkPVScalarBarActor')</li>
          <li>    if not self.hasVTKPVScalarBarActor:</li>
          <li>      logging.warning("SliceAnnotations: Disable features relying on vtkPVScalarBarActor")</li>
          <li>
          </li>
<li>    self.layoutManager = layoutManager</li>
          <li>    if self.layoutManager is None:</li>
          <li>      self.layoutManager = slicer.app.layoutManager()</li>
          <li>    self.layoutManager.connect("destroyed()", self.onLayoutManagerDestroyed)</li>
          <li>
          </li>
<li>    self.dataProbeUtil = DataProbeUtil.DataProbeUtil()</li>
          <li>
          </li>
<li>    self.dicomVolumeNode = 0</li>
          <li>
          </li>
<li>    # Cache recently used extracted DICOM values.</li>
          <li>    # Getting all necessary DICOM values from the database (tag cache)</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L18-L114" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mikebind (2021-10-21 18:20 UTC)

<p>I do this all the time to better label screenshots.  Here is the code I use which could be pasted into the logic of your own module or taken apart to use in the interactor.  As it is, it adds a text label in the upper left and upper right of all slice views and the first 3D view, though it’s probably obvious how to customize it to do any simple variation on that.</p>
<pre><code class="lang-auto">def addCornerAnnotation(self, textToAdd, textColor=(0,1,1)):
    ''' Add annotation to upper right and upper left of slice views and 3D view'''
    lm = slicer.app.layoutManager()
    sliceViewNames = lm.sliceViewNames()
    for sliceName in sliceViewNames:
      view = lm.sliceWidget(sliceName).sliceView()
      view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,textToAdd)
      view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperLeft,textToAdd)
      textProperty = view.cornerAnnotation().GetTextProperty()
      textProperty.SetColor(*textColor)
      view.forceRender()
    # Same for 3D view
    view=slicer.app.layoutManager().threeDWidget(0).threeDView()
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,textToAdd)
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperLeft,textToAdd)
    textProperty = view.cornerAnnotation().GetTextProperty()
    textProperty.SetColor(*textColor)
    view.forceRender()

  def clearCornerAnnotation(self):
    '''Removes corner annotations by placing empty strings there'''
    self.addCornerAnnotation('')
</code></pre>

---

## Post #4 by @hherhold (2021-10-21 19:04 UTC)

<p>Perfect - THANKS!!</p>
<p>-Hollister</p>

---
