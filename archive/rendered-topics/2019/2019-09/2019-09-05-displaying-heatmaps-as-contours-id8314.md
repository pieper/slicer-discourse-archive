---
topic_id: 8314
title: "Displaying Heatmaps As Contours"
date: 2019-09-05
url: https://discourse.slicer.org/t/8314
---

# Displaying heatmaps as contours

**Topic ID**: 8314
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/displaying-heatmaps-as-contours/8314

---

## Post #1 by @ahmedhosny (2019-09-05 18:33 UTC)

<p>Hello -</p>
<p>I have 3 layers visualized in slicer as follows:<br>
<strong>L:</strong> a label map<br>
<strong>F:</strong> a heatmap of continousos values (think of it like an RT dosemap, but I am not using the SlicerRT extension)<br>
<strong>B:</strong> an image</p>
<p>Currently, the heatmap is on top of the image. I would like to view the two simultaneously. For now, simply reducing the opacity of the heatmap works. Ideally, viewing the heatmap as contours would provide the best viewing experience. Any ideas on how to do that within Slicer?</p>
<p>The heatmap is treated as an image not a label map when loading. If “label map” is checked, and the toggle showing “label map volume with regions outlined” is on, you get a pixelated view, which is expected since the values are continuous not discrete as in a common label map.</p>
<p>Thanks so much.</p>
<p>Here is a screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6b5bb64ba4a9e802486b2b8094e520605ae6492.jpeg" data-download-href="/uploads/short-url/nMMCnTTHAbkGJIREWqepexUPcQ2.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b5bb64ba4a9e802486b2b8094e520605ae6492_2_690x372.jpeg" alt="Screenshot" data-base62-sha1="nMMCnTTHAbkGJIREWqepexUPcQ2" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b5bb64ba4a9e802486b2b8094e520605ae6492_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b5bb64ba4a9e802486b2b8094e520605ae6492_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6b5bb64ba4a9e802486b2b8094e520605ae6492_2_1380x744.jpeg 2x" data-dominant-color="796C62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1732×936 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-09-05 18:37 UTC)

<p>This feature is implemented in SlicerRT extension’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Isodose" rel="nofollow noopener">Isodose module</a>. It can visualize iso-surfaces as surfaces in 3D and as contours in slices. You can use any volume as “dose volume”.</p>
<p>                    <a href="https://www.slicer.org/w/images/thumb/8/89/SlicerRT0.6_Isodose.png/1080px-SlicerRT0.6_Isodose.png" target="_blank" class="onebox" rel="nofollow noopener">
            <img src="https://www.slicer.org/w/images/thumb/8/89/SlicerRT0.6_Isodose.png/1080px-SlicerRT0.6_Isodose.png" width="690" height="443">
          </a>

</p>

---

## Post #3 by @ahmedhosny (2019-09-06 14:33 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>! It throws “Selected volume is not a dose”, but it seems to be a warning only.</p>

---

## Post #4 by @lassoan (2019-09-06 14:45 UTC)

<p>Yes, it should work well. To avoid the warning, set <code>DicomRtImport.DoseVolume</code> attribute of the volume to <code>1</code>.</p>

---

## Post #5 by @cpinter (2019-09-06 15:59 UTC)

<p>Yes it’s only a warning.</p>
<p>To convert the volume to dose using the UI, you can right-click your volume in the Data module (make sure it’s under a study that’s under a patient), and choose Convert to dose volume.</p>

---
