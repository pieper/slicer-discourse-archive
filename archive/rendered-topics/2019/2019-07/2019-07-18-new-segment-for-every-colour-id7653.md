# New segment for every colour

**Topic ID**: 7653
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/new-segment-for-every-colour/7653

---

## Post #1 by @the3dslicerdude (2019-07-18 11:56 UTC)

<p>Hi there</p>
<p>I have a 16bit raw image stack of a segmentation ‘so it doesn’t have a crazy amount of colors in the image itself’. Is there a way in slicer to generate a segment for every existing color in the image using the segment editor? Hopefully slicer can handle a fairly large number of segments. Sorry if it sounds confusing</p>
<p>Any help would be appreciated</p>

---

## Post #2 by @lassoan (2019-07-18 12:51 UTC)

<p>It sounds like you have a labelmap volume (you have discrete values in the volume, each value corresponds to a certain structure). You can follow these instructions to load this image and import to segmentation:</p>
<aside class="quote" data-post="2" data-topic="4954">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-nrrd-file-into-stl-file/4954/2">Save .nrrd file into STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If your nrrd is binary (i.e. contains a segmentation) then you can load it as a labelmap (click Show Options in the load window and check LabelMap option). Then go to Data module, right-click the labelmap, select Convert labelmap to segmentation node. Then go to the Segmentations module, select the segmentation, go to the very bottom to the Export to files section, then select your options and click Export.
  </blockquote>
</aside>


---

## Post #3 by @the3dslicerdude (2019-07-18 13:00 UTC)

<p>Thank you so much for the quick reply, I won’t be able to try this until tomorrow. Just one question in regards to your answer, will I be able to re-sample while using the method in the other thread</p>

---

## Post #4 by @lassoan (2019-07-18 13:20 UTC)

<p>Yes, you can crop and resample labelmap volumes the same way as scalar volumes, just make sure to use <em>nearest neighbor</em> interpolator if you want to preserve original voxel values at the boundaries.</p>

---

## Post #5 by @the3dslicerdude (2019-07-19 03:17 UTC)

<p>After trying this method with about 1/8th of the dataset, which is a 700mb nrrd file. It did work but took a very long time to compute and with the labels it uses about 98percent of my 16gigs of ram. I will try some other software packages but I feel like they will also be too resource heavy</p>

---

## Post #6 by @lassoan (2019-07-19 03:24 UTC)

<p>Currently, you can can probably edit up to about 30-50 segments at a time and move out other segments to another segmentation or labelmap. We are improving the segment editor to better support some neurosegmentation workflows which may involve a few hundred segments.</p>
<p>What kind of data do you work with? How many segments do you have? What is the volume size?</p>

---

## Post #7 by @the3dslicerdude (2019-07-19 03:30 UTC)

<p>It is a micro-ct of a mammal and has I estimate it will have north of 200 segments if I was to load in the full dataset. Unfortunately I am interested in preserving as much detail as possible so reducing the quality isn’t really an option. Looking forward to future updates to the segment editor.</p>

---

## Post #8 by @lassoan (2019-07-19 03:30 UTC)

<p>What is the volume size?</p>

---

## Post #9 by @the3dslicerdude (2019-07-19 13:57 UTC)

<p>Sorry I am not sure how to check that. However today I did try to do the same with the 1/8th data set using both Itk-snap and Mimics. I wasn’t able to find where to import a labelmap for mimics ‘it probably doesn’t have this functionality’, but with itk-snap I just clicked open segmentation and opened the nrrd and it imported and created the hundred or so masks within a few seconds, and also had almost no effect on the memory usage (to compare, slicer took about 5 minutes to generate the segments and used 98percent ram once they were imported). Itk also had a really nice export all segments into single vtk scene which didn’t create a file size too large. However the downside with Itk-snap is the mesh it created was not as nice and had holes that were larger than the ones in slicer. Since I am interested in mesh quality, I am leaning more towards slicer, however memory usage and calculation speed is an issue with lots of labels</p>

---

## Post #10 by @cpinter (2019-07-19 14:14 UTC)

<aside class="quote no-group" data-username="the3dslicerdude" data-post="9" data-topic="7653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/839c29/48.png" class="avatar"> the3dslicerdude:</div>
<blockquote>
<p>Sorry I am not sure how to check that</p>
</blockquote>
</aside>
<p>If you keep your mouse cursor above the CT in the Data module, the tooltip will contain the image size. You can also check these (and more) details in the Volumes module.</p>
<aside class="quote no-group" data-username="the3dslicerdude" data-post="9" data-topic="7653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/839c29/48.png" class="avatar"> the3dslicerdude:</div>
<blockquote>
<p>itk-snap I just clicked open segmentation and opened the nrrd and it imported and created the hundred or so masks within a few seconds</p>
</blockquote>
</aside>
<p>ITK-SNAP uses the legacy labelmap volume concept, whereas Slicer uses the more advanced PolySeg segmentations concept that allows overlapping segments, automatic conversions, etc. (see <a href="http://perk.cs.queensu.ca/contents/polymorph-segmentation-representation-medical-image-computing">this paper</a>).</p>

---

## Post #11 by @lassoan (2019-07-19 15:23 UTC)

<p>Yes, segment editor is much more capable than ITK-snap but currently it uses an separate labelmap for each segment, which may require significantly more memory, especially when you have many segments.</p>
<p>We’ll make editing of hundreds of segments more efficient within a couple of months (allow sharing memory between segments, add filtering/searching in the segment list, etc.). Until then, you can edit up to 30-50 segments at a time and merge them into a single labelmap at the end (or upgrade your computer, mainly by add a lot of RAM).</p>

---

## Post #12 by @tee (2022-09-30 14:13 UTC)

<p>Sorry to revive this much later, but I hope someone can help: I am having a stack of png-images with 5 different colors in them. I’d like to segment this by color, mainly select the white background and remove it to 3D render the rest.</p>
<p>But when I try to load the image stack as a label map, I just get an error: “Error: Loading slices/slice_000.png -  load failed.”</p>
<p>Any hints on how to do this? Sorry, but absolute newbie with Slicer3D here.</p>

---

## Post #13 by @lassoan (2022-09-30 14:33 UTC)

<p>Do you have 5 discrete colors in your images (e.g., you painted those using some drawing tools) or you have 5 somewhat similar (not exactly the same) colors (e.g., from scanning images)?</p>

---

## Post #14 by @tee (2022-09-30 16:28 UTC)

<p>They are exact identical: results from a simulation and then assigned 5 specific RGB values. One is white (255,255,255) and should disappear, the rest should be visible segments.</p>

---

## Post #15 by @lassoan (2022-09-30 19:41 UTC)

<p>OK, it means that your data is actually a labelmap volume, not a color image. Therefore, it is better to save it as a scalar (single-channel) image. Use 0 for background and 1, 2, 3, 4, 5 for the segments. You can save it as png, but it would be much better to save the entire array as a single file, in nrrd format. You can find nrrd file writer for all programming languages, but if you are not sure which one to use then let us know.</p>
<p>You can load the nrrd file directly as segmentation, by choosing “Segmentation” in the “Description” column in the “Add data” window. You can make the file open as segmentation by default if you use <code>.seg.nrrd</code> as file extension.</p>

---

## Post #16 by @tee (2022-10-02 11:28 UTC)

<p>Thanks for the explanation. Unfortunately the PNGs are the data I need to work with. Sounds like I need to transform them to that <code>nrrd</code> format first before I can visualize them.</p>

---
