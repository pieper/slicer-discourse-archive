# Resample overlaid volume

**Topic ID**: 3671
**Date**: 2018-08-06
**URL**: https://discourse.slicer.org/t/resample-overlaid-volume/3671

---

## Post #1 by @Laura (2018-08-06 14:33 UTC)

<p>Good afternoon,</p>
<p>Imagine I have two volumes of images in 3D. Each one has its own “image spacing” and its own “image dimensions”.<br>
However, I would like to overlay them in order to see if the organ on the first volume (let say the background) can fit with the organ on the second volume (let say the foreground).<br>
On my python script, I load the first volume in “.nii” and display it then, I load the second one and display it.<br>
Finally, I write that to overlay them together :</p>
<pre><code>lm = slicer.app.layoutManager()
for sliceViewName in lm.sliceViewNames():
  sliceWidget = lm.sliceWidget(sliceViewName)
  view = lm.sliceWidget(sliceViewName).sliceView()
  sliceNode = view.mrmlSliceNode()
  sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
  compositeNode = sliceLogic.GetSliceCompositeNode()
				# Setup background volume
  compositeNode.SetBackgroundVolumeID(self.VolumeNode1.GetID())
				# Setup foreground volume
  compositeNode.SetForegroundVolumeID(self.VolumeNode2.GetID())
				# Changer l'opacite
  compositeNode.SetForegroundOpacity(0.7)
</code></pre>
<p>I have tried the “Resample Scalar Volume” with an interpolation of nearestNeighbor and the spacing (the smallest one of the two volumes) but I can’t find how to visualize the two volumes overlaid (the one with no modification and the new second one) and write it in Python (I can’t find the python code on github for the module “Resample Scalar Volume”). Moreover, I need to change the “image dimensions” of the one that is resampled but I don’t know how to do that…</p>
<p>Does anyone have an idea on how can I do all of that ?<br>
Thanks a lot in advance<br>
Laura</p>

---

## Post #2 by @lassoan (2018-08-06 22:25 UTC)

<p>Slicer displays volumes correctly in their physical location (defined by image origin, spacing, and axis directions). It is not necessary to manually resample them.</p>
<p>Does everything work well when you set the foreground/background volume using the graphical user interface?<br>
Are the foreground and background volumes spatially registered to each other?</p>

---

## Post #3 by @Laura (2018-08-07 06:32 UTC)

<p>Good morning,<br>
When I display one by one, the visualisation is ok, I can see all the slices in all plans<br>
However, when I try to overlay the two, it isn’t well overlaid as you can see :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a359718e546838839f625b710314497ce081e77b.png" data-download-href="/uploads/short-url/nj3suX7iEw0RcvorTGAP5z3iZar.png?dl=1" title="superposition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a359718e546838839f625b710314497ce081e77b.png" alt="superposition" data-base62-sha1="nj3suX7iEw0RcvorTGAP5z3iZar" width="265" height="500" data-dominant-color="21211F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">superposition</span><span class="informations">320×602 2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So I would like either being able to move one image from another to fit them correctly either resample them with the same dimensions and same spacing<br>
What can I do ?<br>
Thanks a lot<br>
Laura</p>

---

## Post #4 by @lassoan (2018-08-07 07:44 UTC)

<p>You don’t need to worry about resampling or dimensions, since Slicer can correctly overlay images with arbitrary non-matching geometry. However, you have to make sure the images are spatially registered to each other in physical space.</p>
<p>How these images are created?<br>
Would you expect them to be spatially aligned (registered) in physical space?</p>

---

## Post #5 by @Laura (2018-08-07 07:55 UTC)

<p>Thanks to answer me !<br>
At the very beginning, I have :</p>
<ul>
<li>volume n°1 initial that is segmented by different treatments and that saved in ‘.nii’ so the format of the segmented image is the same as the initial one</li>
<li>volume n°2 initial (which has dimensions and spacing different from the volume n°1) is segmented with others treatments and saved in ‘.nii’ so the format of the segmented volume n°2 is the same as the initial one</li>
</ul>
<p>I would expect to overlay the two segmentations let’s say an organ overlaid with a cavity for instance. So, i would like that the white parts of each volume (ie the segmented areas) be overlaid to see if it can fit together.<br>
So, that’s why I think that I have to do something special because it is impossible to overlay two volumes that have different dimensions and spacing, isn’t it ?<br>
I don’t know if it is more clear…<br>
Thanks !</p>

---

## Post #6 by @lassoan (2018-08-07 10:47 UTC)

<aside class="quote no-group" data-username="Laura" data-post="5" data-topic="3671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>I think that I have to do something special</p>
</blockquote>
</aside>
<p>Yes, you need to spatially register the anatomical images. Result of registration is a transform that you can use to align segmentations. I would recommend to use SlicerElastix extension for registration, as it usually works well with default settings.</p>

---

## Post #7 by @Laura (2018-08-07 11:00 UTC)

<p>Oh thanks ! I have tried and I think that I am on the right way but is it normal to get that kind of image as output volume ? :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05cdff4aa25ffe76ad5939d3a054908273ae64af.png" data-download-href="/uploads/short-url/PlJwZ7ylIdEK9YGpnQvmsaWC3d.png?dl=1" title="elastic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05cdff4aa25ffe76ad5939d3a054908273ae64af_2_690x360.png" alt="elastic" data-base62-sha1="PlJwZ7ylIdEK9YGpnQvmsaWC3d" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05cdff4aa25ffe76ad5939d3a054908273ae64af_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05cdff4aa25ffe76ad5939d3a054908273ae64af_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05cdff4aa25ffe76ad5939d3a054908273ae64af_2_1380x720.png 2x" data-dominant-color="363743"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">elastic</span><span class="informations">1680×877 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It seems really strange when I change the slice I look<br>
A little more question : is it possible to create a little window pop-up with this module General Registration Elastix in my python script ?<br>
Thanks a lot for your help !</p>

---

## Post #8 by @Laura (2018-08-07 11:27 UTC)

<p>I forgot to precise that the two volumes are not from the same patient, it is two different patients…</p>

---

## Post #9 by @lassoan (2018-08-07 14:18 UTC)

<p>As long as images contain approximately the same anatomical region, registration of different patients should be successful.</p>

---
