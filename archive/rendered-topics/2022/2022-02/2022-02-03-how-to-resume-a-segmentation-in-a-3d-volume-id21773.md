# How to resume a segmentation in a 3D volume?

**Topic ID**: 21773
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/how-to-resume-a-segmentation-in-a-3d-volume/21773

---

## Post #1 by @pycad (2022-02-03 05:55 UTC)

<p>Hi there,<br>
I am trying to segment some 3D volumes using 3D slicer, but sometimes I can not complete the whole segmentation on the same day and I want to save then complete the segmentation after but I do not know how to save the file so that it can be opened after and how to complete the segmentation from where I ended.</p>
<p>I will really appreciate that<br>
Thank you</p>

---

## Post #2 by @ebrahim (2022-02-03 12:00 UTC)

<p>You can save and then later load your scene, using the buttons in the top right that look like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfa92090c7a4ad501edbb1c795e94b49b199e4f9.png" alt="image" data-base62-sha1="vUAPpLKb5d4ohMqvB8iiDuyQWY9" width="32" height="36"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e0fc3047483669fe38f319255bdc263ac78a81c.png" alt="image" data-base62-sha1="dq6Ep73rqU9ZvTXoHKHmIE5CE1u" width="32" height="36"></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#segmentations" rel="noopener nofollow ugc">Here’s a description of the file formats for segmentation</a></p>

---

## Post #3 by @DIV (2022-02-07 06:28 UTC)

<p>Typically when saving you get the option to save out a variety of separate files that each describe a different part of what you’ve done.<br>
Example:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269e44cd1f13ecf4f2d4a63de8adc891e760abf1.png" alt="image" data-base62-sha1="5vDes7a4cdC0CM7KLBfgJkd19u1" width="474" height="247"></p>
<p>I tend to save them all, although you might decide that it’s not worth re-saving the <code>NRRD (.nrrd)</code> file containing the original data to a new location. Obviously you should save the <code>Segmentation</code>.</p>
<p>I then typically reload <em>everything</em> via the <code>MRML Scene</code> file.  (That’s one file.)  An example is given below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2ef938f97387128fb0a136ab33b0d367c981e45.png" data-download-href="/uploads/short-url/u61yElW28L6xraSm1WcceX9FdI1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2ef938f97387128fb0a136ab33b0d367c981e45.png" alt="image" data-base62-sha1="u61yElW28L6xraSm1WcceX9FdI1" width="517" height="118" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×171 8.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
That file tells Slicer to load all of the associated files, including segmentation.</p>
<p>Optionally you could load individual aspects, rather than <em>everything</em>, by choosing one of the other files that were saved out.</p>
<p>—DIV</p>
<p>P.S.  Note that the <code>MRML Scene</code> file is different from the “scene views” that can be captured, and which tend to get saved out as separate <code>.png</code> image files.</p>

---
