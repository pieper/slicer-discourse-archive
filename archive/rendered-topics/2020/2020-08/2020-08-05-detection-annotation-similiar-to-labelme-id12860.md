# Detection annotation similiar to labelme

**Topic ID**: 12860
**Date**: 2020-08-05
**URL**: https://discourse.slicer.org/t/detection-annotation-similiar-to-labelme/12860

---

## Post #1 by @ButuiHu (2020-08-05 02:16 UTC)

<p>Hi, I’m looking for an annotation tool like <a href="https://github.com/wkentaro/labelme" rel="nofollow noopener">label</a> for medical images. Is there something similar to labelme? I would like to draw a bounding box to annotate the detected tumor or structure. It would be even greater if I could make it a 3D bounding box (aka. a cube).</p>

---

## Post #2 by @lassoan (2020-08-05 02:40 UTC)

<p>There are many options.</p>
<p>If you really just want a 3D box, then you can use Annotation ROI node (select it on the toolbar and initialize it with two clicks in an axial slice):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4ddd64e130906ddbefb4e8ba541d2a5f093fd983.png" alt="image" data-base62-sha1="b6P6bGditrjFfbpcNZFxEkKnF2X" width="419" height="352"></p>
<p>It is often enough to just mark points. You can use Markups Fiducial points (you can select it from the same toolbar as ROI).</p>
<p>If you prefer a custom shape (for example, sphere) then you can follow this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>If you want some more flexibility then you can use Segment Editor module. For example, you can paint strokes corresponding to “definitely tumor” and “definitely not tumor”. Or, you can quickly create arbitrary shapes using Surface Cut effect (in SegmentEditorExtraEffects extension).</p>
<p>You can customize and automate everything using Python scripts. So, if you need to annotate thousands of images then you don’t need to make a single unnecessary click.</p>

---

## Post #3 by @ButuiHu (2020-08-06 01:25 UTC)

<p>Thanks for your quick answer. I think the Annotation ROI node is good for me. However, it seems each annotation node is exported to one file. Markups Fiducial points is also great, it’s visualized as a point, not a rectangle. It might not be intuitional.</p>

---

## Post #4 by @lassoan (2020-08-06 03:58 UTC)

<p>You can write a short Python script that exports the ROI in any format you prefer.</p>

---

## Post #5 by @ButuiHu (2020-08-10 01:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi, I also check the legacy Editor module (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Editor" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/Editor</a>), and there is a RectangleEffect which is not available in the new SegmentEditor anymore. I think it helps me with 2D bbox annotation. It would be even great if I could see a bbox when I left click and drag. I can’t modity the rectangle after it’s done.</p>

---

## Post #6 by @ButuiHu (2020-08-10 01:49 UTC)

<p>Another option, I could use SegmentEditor to draw a rough rectangle.</p>

---

## Post #7 by @lassoan (2020-08-10 02:25 UTC)

<p>An improved version of the “Rectangle” effect is available in Segment Editor module as “Scissors” effect. Scissors effect has the following advantages:</p>
<ul>
<li>supports not just rectangle but circle or free-form shape</li>
<li>can fill or erase, inside or outside the selected region</li>
<li>can be restricted to a single slice, thick slice, one side of the slice plane, or both sides</li>
<li>also works in 3D views, oblique slices</li>
<li>works with masking (you can mask cutting with an additional set of segments or intensity range)</li>
</ul>

---

## Post #8 by @ButuiHu (2020-08-10 04:23 UTC)

<p>Oh, that is what “Scissors” effect do. I thought it’s for eraring.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdaeb38f841ff7d25b8485256fc5267cdaf8486b.jpeg" data-download-href="/uploads/short-url/tlyb0fmujXggqAtdWvY9Y99WbcT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdaeb38f841ff7d25b8485256fc5267cdaf8486b_2_690x399.jpeg" alt="image" data-base62-sha1="tlyb0fmujXggqAtdWvY9Y99WbcT" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cdaeb38f841ff7d25b8485256fc5267cdaf8486b_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdaeb38f841ff7d25b8485256fc5267cdaf8486b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdaeb38f841ff7d25b8485256fc5267cdaf8486b.jpeg 2x" data-dominant-color="B5B4B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×462 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
It seems it’s not a filled rectangle. I found there is waring: Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 0.000576862 mm, tolerance threshold is 0.001 mm).<br>
I check <a href="https://discourse.slicer.org/t/question-regarding-irregular-volume-geometry-detected/8881">this post</a>. And set apply regualarization transform in the application setting, but still get this warning.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a05941649f9ce00a18afd9249dc956d4f4746c.jpeg" data-download-href="/uploads/short-url/35jztRRwbN4MVzNuswOy8LZFnPe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15a05941649f9ce00a18afd9249dc956d4f4746c_2_690x372.jpeg" alt="image" data-base62-sha1="35jztRRwbN4MVzNuswOy8LZFnPe" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/15a05941649f9ce00a18afd9249dc956d4f4746c_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a05941649f9ce00a18afd9249dc956d4f4746c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15a05941649f9ce00a18afd9249dc956d4f4746c.jpeg 2x" data-dominant-color="5B5B58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">902×487 65.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
as you could see, the image is rotated a little. Any issue with the DICOM data?<br>
PixelSpacing: 0.9375, 0.9375<br>
SliceThickness: 1<br>
ImagePositionPatient: -112.38102987944, -116.43096361169, 83.608241714<br>
ImageOrientationPatient: 0.99926579596646, 0.00441271653949, 0.03805781055539, -0.0017440497062, 0.99755447631478, -0.0698714897148</p>

---

## Post #9 by @lassoan (2020-08-10 13:20 UTC)

<p>There is no issue at all, this is all normal when view axes (that are initialized by default to be aligned with right-anterior-superior anatomical directions) are not parallel with image axes directions (they are often aligned with anatomical directions, but not always). See explanation and solutions <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation">here</a>. Probably you want to specify the rectangles in the image coordinate system and so you just need to click the warning icon next to the segmentation node selector in Segment Editor module.</p>

---
