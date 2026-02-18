# Converting and Transforming Image Coordinate Frames from DICOM to PNG

**Topic ID**: 5603
**Date**: 2019-01-31
**URL**: https://discourse.slicer.org/t/converting-and-transforming-image-coordinate-frames-from-dicom-to-png/5603

---

## Post #1 by @dav (2019-01-31 22:30 UTC)

<p>I have some super high resolution DICOM image sets that take up large amounts of data (40-80gb), and they are a bit overkill for my work.  I am limited by my computer specs and am trying to label features in these sets as fast as possible.</p>
<p>Since I can’t label the entire scan all at once (computer limitations), I am doing this in sets which is a painfully slow process.  I realized that if I converted my DICOM images to jpg/png/etc and scale down my images I can label smaller resolution pictures and then transform the points back to the originals to retrieve distance data, etc.  Then if I have to go back and relabel/adjust feature point locations (hopefully won’t happen) then it will be a much quicker process.</p>
<p>The problem I’m having is that after I convert my DICOM to image data sets, I lose header info, and scaling so my labelled points are not in the same locations as in the DICOM format.  The frames are shifted quite a bit.  How do I match the coordinate frames for each of these sets?  When I imported the images I tried a number of things, saving and importing information from the DICOM files, but I’m obviously not getting the correct sets.  Does anyone know how to do this?</p>

---

## Post #2 by @muratmaga (2019-02-01 06:30 UTC)

<p>If I understand correctly you are only loading a subset of your dicom sequences at a time? If so, you can do the downsampling within Slicer. Just use the ResampleScalarVolume and specify the output spacing (in mms) you’d like. This will preserve coordinate system of the original DICOMs, and you can segment/directly measure distances/etc…</p>
<p>Alternatively, you can try to use the Fiji’s Import-&gt;Image Sequence with virtual stack option to load your entire dicom and subsample there. Though I never tried with such large datasets…</p>

---

## Post #3 by @dav (2019-02-01 17:56 UTC)

<p>This is a good idea, and would be used, except since I can’t open all sets at the same time, don’t have enough memory/available supercomputer, I might get some inaccurate labelling values if I stitch together multiple resampled sets.</p>
<p>My current solution was to scale down the resolutions by hand after converting the files to a familiar format:</p>
<ol>
<li>convert to png,</li>
<li>scale each image by 0.5 for x, y values,</li>
<li>sample every other image for equivalent scaling by z</li>
</ol>
<p>Then I can open a smaller file and label these points.  I wanted to do a self check on the original DICOM images to check if this was working correctly but I was having this transformation issue problem after just converting to png.  Even thought the png images and dicom images are the same size, I labelled the same features in both and hoped that importing the saved labels from the dicom images would label the same points on the png images.</p>
<p>Lo and behold the labels don’t match of course because there is some import setting that png doesn’t have ( header information of course) that specifies the image width and location of each image.</p>
<p>How can I transform this to match?  Can I import ‘header information’ to use with the png files? Or am I totally going the wrong route here?</p>

---

## Post #4 by @lassoan (2019-02-01 18:50 UTC)

<p>Make sure you don’t use formats that unable to maintain physical position, orientation, and spacing value. So, instead of png, use mha or nrrd format.</p>

---

## Post #5 by @muratmaga (2019-02-01 18:53 UTC)

<p>I second what Andras said. I am not sure where you are doing the DICOM-&gt;png, but that’s where the information is lost. If you use Fiji (ImageJ) with virtual stack, you can load the entire DICOM stack at once (without requiring the memory). Resample it, and save it as nrrd. It will be slow but doable.</p>

---

## Post #6 by @dav (2019-02-02 00:15 UTC)

<p>I tried to upload to ImageJ, resample and export to nrrd, but my computer was still running out of memory.  <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"> grrr, haha!   It worked for a second so thanks for the suggestion!</p>
<p>The reason I wanted to use a png, without the volume data is this:<br>
If I know the spacing from the original header data between pixels (my resolution) then I can easily reduce the sizes of each pixel via code without opening the entire series of images, and then transform any labelled points anyways.</p>
<p>I really don’t see how this won’t work if I am only concerned with positions of anatomical features (not material densities, etc.).  Is the pixel output from CT not a 1-to-1 scaling directly to the volumetric data of the CT machine (ex. each pixel is 0.05 mm apart, and each slice is 0.05 mm apart),  that is, since my dicom header information already specifies this?</p>
<p>Ultimately I’m comparing different placements of points on different animal CT scans, so after I label points, I can assign a coordinate frame based on anatomical feature (since we can’t rely on perfectly orthogonal CT scans) and transform one coordinate frame into the frame of the other, so I wouldn’t need any additional original measurement information other than the slice and pixel resolution.</p>

---

## Post #7 by @lassoan (2019-02-02 01:01 UTC)

<p>Can you load a single image slice into Slicer?</p>

---

## Post #8 by @muratmaga (2019-02-02 01:17 UTC)

<p>Are you certain you are using the ‘virtual stack’ option when importing the image sequence into Fiji?</p>
<p>Anyways, as Andras alluded, you can possibly load one DiCOM slice into Slicer, make a note of of its voxel spacing and origin values (under Volumes module), then import your resampled PNG stack into Slicer and adjust your voxel spacing manually. I don’t think the origin would be affected from the resampling.</p>

---

## Post #9 by @dav (2019-02-04 18:30 UTC)

<p>Don’t know how I was missing the virtual stack option.  Works like a charm.  Thanks for all the help!</p>

---
