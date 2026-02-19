---
topic_id: 20970
title: "Clipping 2D Slices In An Arbitary Shape"
date: 2021-12-08
url: https://discourse.slicer.org/t/20970
---

# Clipping 2D slices in an arbitary shape

**Topic ID**: 20970
**Date**: 2021-12-08
**URL**: https://discourse.slicer.org/t/clipping-2d-slices-in-an-arbitary-shape/20970

---

## Post #1 by @Hitesh_Ganjoo (2021-12-08 18:31 UTC)

<p>Hi,</p>
<p>I want to display a part of the slice data(in any slice view) based on an existing geometric constraint or specifically the 2D projection of a surface model(attaching a sample image). Instead of showing all the voxels in a plane(axial, sagittal, coronal or an oblique plane), I just wish to show the intersection. Is there an existing way to do this through any existing module or extension? If not, any pointers would really help…<br>
Thanks in advance!<br>
Hitesh<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e701bb0fa38bb34e3ad4dffebb5dd187ddae80.jpeg" data-download-href="/uploads/short-url/zeco1hZsd2hmly6uPHksFYT2JI4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e701bb0fa38bb34e3ad4dffebb5dd187ddae80_2_690x410.jpeg" alt="image" data-base62-sha1="zeco1hZsd2hmly6uPHksFYT2JI4" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e701bb0fa38bb34e3ad4dffebb5dd187ddae80_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e701bb0fa38bb34e3ad4dffebb5dd187ddae80_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e701bb0fa38bb34e3ad4dffebb5dd187ddae80_2_1380x820.jpeg 2x" data-dominant-color="222222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1477×879 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mikebind (2021-12-08 22:55 UTC)

<p>If you have a threshold set on the background volume in a slice view, the foreground and label layers are only shown where the background volume is within the threshold bounds. So, I think the easiest way to achieve the effect you want is to</p>
<ol>
<li>convert your model to a labelmap (by importing it into a segmentation and exporting to a labelmap (use Segmentations module, or see example code for this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">here</a>). Then</li>
<li>set this labelmap as the background volume in your slice views, and apply a lower threshold of 0.5 (to exclude background voxels) using the Volumes module. Then,</li>
<li>set whatever volume you wanted masked as the foreground volume in the slice views and</li>
<li>shift the foreground/background blend slider to show only the foreground.</li>
</ol>
<p>If you have any trouble implementing this, just post what step you are stuck on and I can provide some more details.</p>

---

## Post #3 by @Hitesh_Ganjoo (2021-12-09 19:13 UTC)

<p>Thanks! I understand this and was able to quickly achieve this… However, while trying this I realized it would be better for my current need to do have an annotation achieve this using a markup(e,g. a closed curve) and achieve the same effect…<br>
Is there a way to generate similar lablemap for background layer from a markup? Also, I want to have this markup more like an extension of a 3d model(e.g. ultrasound probe) and move with it(mimicking the ultrasound plane).<br>
Is there a better way to do this other than use observing transforms on a 3d model and apply these to a “child”?<br>
Lastly, can I have more than 2 forground layers over a lablemap( e.g. in this case have a MRI and a registered Ultrasound volume over the background labelmap). So far as I understand there is one background and one foreground layer…</p>
<p>Thanks for your help.</p>

---

## Post #4 by @mikebind (2021-12-10 18:49 UTC)

<p>Take a look at the “Mask Scalar Volume” module.  This would allow you to create masked versions of the MRI and ultrasound and use one as the background volume and one as the foreground volume. This should work OK to achieve the desired effect.  If update time is not a major issue, I’m not sure there is much advantage to trying to convert the slice through your 3D model to a markups curve to then try to create a labelmap from that.  It seems like you might as well just create 3D labelmap from the model and let Slicer handle the slice display from that.</p>
<p>However, I wonder if you are asking about reducing to 2D in hopes of speeding up the display updates. If you are hoping to do this in real time, I expect this approach will be far too slow for you. If that’s the case, then you need a more sophisticated solution.  I might suggest taking a look at <a href="http://www.slicerigt.org/wp/">Slicer IGT</a>, which is used, for example, for tracking surgical instruments relative to registered images in real time.</p>

---

## Post #5 by @Hitesh_Ganjoo (2021-12-12 18:24 UTC)

<p>Thanks for your reply and suggestions!</p>
<p>While the filtering plugins on scalar volume like “Mask Scalar Volume” module are good options to generate the desired effect, I think it will not help me much to create real time slice updates, like you said.</p>
<p>I am trying to build a small “torchlight” like effect, where a 3d model(of a US probe) can be used to move in real time and its “projection or beam” can light up specific voxels on a slice and only those should be visible in that slice. So far, I have been able to build real time tracking of an external sensor through which I am able to generate a specific slice data(of registered MR and US).</p>
<p>So, I just need to add the “torchlight” like effect so that it mimics and tries to simulate an ultrasound probe at that position and only the voxels in the area of the beam are visible. I hope am able to explain what I want to achieve. I have played a bit with IGT before, but I am not sure if IGT can help here?</p>
<p>Please let me know if you have further ideas/suggestions. Thanks!</p>

---

## Post #6 by @mikebind (2021-12-13 16:54 UTC)

<p>Unfortunately, I haven’t even experimented with any real-time updating in Slicer, so I don’t think I can be much further help.  <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/cpinter">@cpinter</a>, might you be able to give some guidance or point <a class="mention" href="/u/hitesh_ganjoo">@Hitesh_Ganjoo</a> towards someone else who could?</p>

---

## Post #7 by @mau_igna_06 (2021-12-13 17:11 UTC)

<p>I think this is possible because Slicer slices the scalarVolume of a CT to show it to the user on the sliceView. So you just need to add your torchlike effect (that sounds like a threshold operation to me).<br>
Probably you need to create a single slice scalarVolume which is updated when a new transform from the tracker arrives. I think for the update of the scalarVolume’s imageData you would need your original MRI and the transform used in combination with a vtkThreshold filter (for slicing and the torchEffect). Or something like this.</p>
<p>I hope this gives some ideas to test out.</p>
<p>It would be great if you could share a code sample if you get it working</p>

---

## Post #8 by @lassoan (2021-12-13 20:19 UTC)

<p>If you use a convex probe then the ultrasound image is already fan shaped (0 outside the beam), so you can achieve a “flashlight effect” quite easily by using thresholding and adjusting the blending mode:</p>
<ul>
<li>If you want to blank out the MRI completely: you can use the US image as background, MRI as foreground, and adjust the US volume’s display threshold in Volumes module.</li>
<li>If you want to add the US as an overlay on the MRI: you can use the MRI as background, US as foreground, and set the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view’s blending mode</a> to “Add”.</li>
<li>If you want to display the fan-shape US image in 3D views: adjust display threshold in the Volumes module and choose to show that slice view in 3D.</li>
</ul>
<p>If thresholding does not work for you (e.g., because you have lots of 0 voxels in the image and you want to show a solid beam) then you can apply a mask very quickly using a VTK filter (vtkImageMask or stencil filters) or numpy (using numpy array indexing and lookup). It should not add more than a few millisecond delay to the image display. This requires some minimal Python coding (setting up the mask filter and input image observer is probably 5-10 lines of code; the callback function that updates the mask is probably 3-4 lines of code).</p>

---

## Post #9 by @Hitesh_Ganjoo (2021-12-17 18:10 UTC)

<p>Thank you for the help and ideas. I was able to acheive this by doing the following:-</p>
<ul>
<li>
<p>Created a dummy 3d model to mimic the beam/fan like shape. Thereafter, I created the segmentation node and binary labelmap from the 3d model.</p>
</li>
<li>
<p>Then I set the labelmap as the background layer, while setting the registered(MR and US) in the foreground layer. So its pretty much like thresholding but I was concerned about the 2D slice update speed, since I receive hand poses through an external sensor and I update the slices(orientation and position) based on the hand position. I used a little bit of reference from how the reformat widget slices using a slice normal and position and was able to achieve this at a reasonably fast update of 2D slices</p>
</li>
</ul>
<p>Thanks…</p>

---
