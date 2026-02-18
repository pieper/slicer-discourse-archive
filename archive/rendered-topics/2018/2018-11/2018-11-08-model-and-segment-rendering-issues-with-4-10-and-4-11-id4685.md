# Model and Segment rendering issues with 4.10 (and 4.11)

**Topic ID**: 4685
**Date**: 2018-11-08
**URL**: https://discourse.slicer.org/t/model-and-segment-rendering-issues-with-4-10-and-4-11/4685

---

## Post #1 by @dominicrushforth (2018-11-08 17:15 UTC)

<p>I have been using the isodose module to make isodose models.  It worked in 4.8 but with 4.10 the 2D isolines do not display correctly - they do not change properly as I scroll through the slices - the lines do not change shape the just start to disappear as on the red and yellow windows…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3487137f3bb680520eb3350811f4e1dc1b26f42.png" data-download-href="/uploads/short-url/wqDAK1vFX0uWpDecviHhvWdKPS2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3487137f3bb680520eb3350811f4e1dc1b26f42_2_625x500.png" alt="image" data-base62-sha1="wqDAK1vFX0uWpDecviHhvWdKPS2" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3487137f3bb680520eb3350811f4e1dc1b26f42_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3487137f3bb680520eb3350811f4e1dc1b26f42_2_937x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3487137f3bb680520eb3350811f4e1dc1b26f42_2_1250x1000.png 2x" data-dominant-color="85888A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×1024 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>… If I change the size of the windows (e.g. by moving the program to a different monitor) they detatch from the images and do not align at all…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5886491e5a7de56c869a21f265d07f9baa1a112.png" data-download-href="/uploads/short-url/usZV8pbiyBLbsUcHV5kzHQmfo8q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5886491e5a7de56c869a21f265d07f9baa1a112_2_690x402.png" alt="image" data-base62-sha1="usZV8pbiyBLbsUcHV5kzHQmfo8q" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5886491e5a7de56c869a21f265d07f9baa1a112_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5886491e5a7de56c869a21f265d07f9baa1a112_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5886491e5a7de56c869a21f265d07f9baa1a112_2_1380x804.png 2x" data-dominant-color="696B70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1852×1080 472 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have also had issues with the volume segment editor module. Even using a simple tool such as paint it does not render properly with all kinds of odd lines…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8bb85e9e68cf0fb1e80801d2c6afe5638a14146.png" data-download-href="/uploads/short-url/qmdCuWgqdWLbZfzkcZyWkmZ0N1Q.png?dl=1" title="ERROR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8bb85e9e68cf0fb1e80801d2c6afe5638a14146_2_690x402.png" alt="ERROR" data-base62-sha1="qmdCuWgqdWLbZfzkcZyWkmZ0N1Q" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8bb85e9e68cf0fb1e80801d2c6afe5638a14146_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8bb85e9e68cf0fb1e80801d2c6afe5638a14146_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8bb85e9e68cf0fb1e80801d2c6afe5638a14146_2_1380x804.png 2x" data-dominant-color="686970"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ERROR</span><span class="informations">1852×1080 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>…and if I persevere the program freezes or crashes.</p>
<p>I have tried the latest nightly, I have tried unistalling and reinstalling without any additional modules etc - and I have also tried using the experimental rendering method. Nothing seems to make any difference.</p>
<p>Does anyone know what is going on?</p>

---

## Post #2 by @dominicrushforth (2018-11-09 12:14 UTC)

<p>So it seems it was not slicer that was at fault at all…</p>
<p>I downloaded and installed the latest graphics drivers for my card and now everything is working as expected.</p>
<p>Sorry for any inconvenience.</p>

---

## Post #3 by @cpinter (2018-11-09 14:11 UTC)

<p>Great news, thanks for reporting and also for following up!</p>
<p>So now both Segment Editor and Isodose work properly?</p>

---

## Post #4 by @dominicrushforth (2018-11-13 12:42 UTC)

<p>Yes the the isodoses and segmentations are now working perfectly. The only thing I’ve not managed to fix is a widget I made to render a surface volume at precise dose levels using a slider.</p>
<p>First, in set up I create a volume display node</p>
<pre><code>  # Display node for 3D volumes
  volRenLogic = slicer.modules.volumerendering.logic()
  volumeDisplayNode = volRenLogic.CreateVolumeRenderingDisplayNode()
  slicer.mrmlScene.AddNode(volumeDisplayNode)
  volumeDisplayNode.UnRegister(volRenLogic)
  self.threeDVolumeDisplayNode = volumeDisplayNode
</code></pre>
<p>Later, after calculating my doses,  I set the parameters for the 3D display updating the display node whenever the foreNode changed</p>
<pre><code>  # and volume render the dose
  volRenLogic = slicer.modules.volumerendering.logic()
  volRenLogic.UpdateDisplayNodeFromVolumeNode(self.threeDVolumeDisplayNode, foreNode)
  # sets the window parameters for the 3D volume where the volume is rendered
  layoutManager = slicer.app.layoutManager()
  threeDWidget = layoutManager.threeDWidget(0)
  controller = threeDWidget.threeDController()
  threeDView = threeDWidget.threeDView()
  controller.set3DAxisVisible(False)
  controller.set3DAxisLabelVisible(False)
  controller.setOrientationMarkerType(2)
  controller.setOrthographicModeEnabled(True)
  controller.spinView(True)
  threeDView.lookFromViewAxis(ctk.ctkAxesWidget.Anterior)
  threeDView.resetCamera(False, True, True)
  threeDView.resetFocalPoint()
</code></pre>
<p>I then changed the threshold of the volume using a slider bar / dose selector…</p>
<p>def onChangeThresholdSliderWidget(self, value):<br>
propNode = self.threeDVolumeDisplayNode.GetVolumePropertyNode()<br>
volumeProp = propNode.GetVolumeProperty()<br>
volRenLogic = slicer.modules.volumerendering.logic()<br>
max = self.volumeThresholdSliderWidget.maximum<br>
volRenLogic.SetThresholdToVolumeProp([0,max],[value,max], volumeProp, False, True)</p>
<p>this all worked beautifully in 4.8 but not in 4.10. I’m not really sure what’s going on – I can get a (I’m not sure if it’s the same) volume display node to appear if I go to volume rendering and choose the node it was created from, but my slider no longer affects it. If I play with it too much the whole thing crashes.<br>
I’m sure this is to do with differences in how volume rendering is now handled and I suspect that I should be doing something simpler - but I’m struggling to figure exactly what it is I need to change. Perhaps there is some documentation that I’ve missed that someone could point me towards?</p>

---

## Post #5 by @cpinter (2018-11-13 14:40 UTC)

<p>Volume rendering changed quite a bit internally after 4.8.1. There have been discussions about this, they will probably help. Such as this:</p><aside class="quote quote-modified" data-post="2" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063/2">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Oliver, 
There have been some improvements since 4.8.1 that makes it easier for us to do this. So if you use the latest nightly, then this is what you can do: 
Easier setup of volume rendering (no need to create the display node and update it from the logic): 
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

This is not very clean, because it uses widgets from the volume rendering module, but you can apply a shift li…
  </blockquote>
</aside>


---
