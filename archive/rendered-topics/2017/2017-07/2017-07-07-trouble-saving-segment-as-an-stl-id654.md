# Trouble saving segment as an STL

**Topic ID**: 654
**Date**: 2017-07-07
**URL**: https://discourse.slicer.org/t/trouble-saving-segment-as-an-stl/654

---

## Post #1 by @KateOxley (2017-07-07 20:15 UTC)

<p>I’m having trouble saving a segment as an STL. When I try to save, I’d expect to see a file called “Intervertebral Disc 1.vtk” that I could save as an STL, but I am not seeing that option. What am I doing wrong? Thanks for your help.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6be6388b479232189f3871c28d1b4669752f0b95.jpg" data-download-href="/uploads/short-url/fowkMQClcVenNP3T6h7Cf1xVEoZ.jpg?dl=1" title="3d Slicer Save.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6be6388b479232189f3871c28d1b4669752f0b95_2_690x441.jpg" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6be6388b479232189f3871c28d1b4669752f0b95_2_690x441.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6be6388b479232189f3871c28d1b4669752f0b95_2_1035x661.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6be6388b479232189f3871c28d1b4669752f0b95_2_1380x882.jpg 2x" data-dominant-color="8E8F92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d Slicer Save.jpg</span><span class="informations">3000×1920 843 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2017-07-07 20:38 UTC)

<p>You need to export the segment to a model node so that you can save it to STL. Easiest way is to go to Data module’s Subject hierarchy view, right-click the segmentation and select Export visible segments to models.</p>

---

## Post #3 by @KateOxley (2017-07-07 21:19 UTC)

<p>I only have the option to export to DICOM.</p>

---

## Post #4 by @lassoan (2017-07-07 21:31 UTC)

<p>Use the latest nightly version of Slicer.</p>

---

## Post #5 by @ssyip (2018-03-12 22:09 UTC)

<p>I have multiple contours (e.g. contour_1, contour_2, contour_3). I created a model and it looks fine. But 3D slicer forced me to save the contours as three separate models (model_1.stl, model_2.stl, model_3.stl). How do I save all of the models as a single stl file rather than three?</p>
<p>Thank you!</p>

---

## Post #6 by @lassoan (2018-03-13 02:54 UTC)

<p>You can use <code>Merge models</code> module for this.</p>

---

## Post #7 by @ssyip (2018-03-13 15:45 UTC)

<p>Hi Adras,</p>
<p>I have a brain and a tumor model. After merging them, it seems like the hierarchical structure is lost. That is, I can’t differentiate between the brain and tumor. Is that possible to merge them into one file, while assigning them with two different colors?</p>
<p>Thanks!!</p>

---

## Post #8 by @lassoan (2018-03-13 16:28 UTC)

<p>STL files cannot store scalar data. There are tricks that some software support, but you have to do the model merging in that software then. What would you like to do with the merged model?</p>

---

## Post #9 by @lassoan (2018-03-20 18:32 UTC)

<p>Implemented <a href="https://github.com/Slicer/Slicer/pull/919">direct STL file export from segmentation</a> - will be available in tomorrow’s nightly build. There is an option to merge all models to a single file STL and an option to save single-file .obj file, where each segment is saved with a different color.</p>

---

## Post #10 by @xszomol (2018-04-17 12:24 UTC)

<p>Hi a would like to export my swgmentations to .obj file. I am using slicer 4.9.0. When I try to export from segment editor I always get error that is shown on one of the pictures.</p>
<p>Thanks very much for help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fa6f8c7de949ec87a9a6700ee719ab5f19d4d19.png" data-download-href="/uploads/short-url/2esTDWupyUyqfORkG3rIPnd96aJ.png?dl=1" title="Sn%C3%ADmka2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa6f8c7de949ec87a9a6700ee719ab5f19d4d19_2_690x449.png" alt="Sn%C3%ADmka2" data-base62-sha1="2esTDWupyUyqfORkG3rIPnd96aJ" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa6f8c7de949ec87a9a6700ee719ab5f19d4d19_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fa6f8c7de949ec87a9a6700ee719ab5f19d4d19.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fa6f8c7de949ec87a9a6700ee719ab5f19d4d19.png 2x" data-dominant-color="DCDDE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sn%C3%ADmka2</span><span class="informations">892×581 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/812f48d2fbd71b98060cbf3f7d65d382ea595fca.png" alt="Sn%C3%ADmka" data-base62-sha1="iqOTOlZ303x82RiOjJatPUpPyRQ" width="473" height="302"></p>

---

## Post #11 by @lassoan (2018-04-17 12:46 UTC)

<p>“unable to open .obj files” error is logged when the .obj file cannot be written. Make sure the target obj files are not open in any viewer or editor application and/or choose a different destination folder.</p>

---
