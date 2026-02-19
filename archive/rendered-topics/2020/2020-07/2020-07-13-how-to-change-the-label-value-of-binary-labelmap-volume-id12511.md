---
topic_id: 12511
title: "How To Change The Label Value Of Binary Labelmap Volume"
date: 2020-07-13
url: https://discourse.slicer.org/t/12511
---

# How to change the label value of binary labelmap volume?

**Topic ID**: 12511
**Date**: 2020-07-13
**URL**: https://discourse.slicer.org/t/how-to-change-the-label-value-of-binary-labelmap-volume/12511

---

## Post #1 by @N.Arjmandi (2020-07-13 18:11 UTC)

<p>I imported CT images and radiotherapy structures (segmented organ shuch as bladder , rectum, and … ) into the 3D Slicer , then created a binary labelmap of the structures. The software assigned a label value (index) for each organ, but for a specific organ (e.g. bladder) in Different patients do not have the same label value. How can I assign the same label value to each organ in different patients?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbdf615db96e0eeaf90dd3526b8da051c688189.png" data-download-href="/uploads/short-url/8wv9YvBvLuoPhfJz39seWAZi7pv.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbdf615db96e0eeaf90dd3526b8da051c688189_2_654x500.png" alt="Capture" data-base62-sha1="8wv9YvBvLuoPhfJz39seWAZi7pv" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbdf615db96e0eeaf90dd3526b8da051c688189_2_654x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbdf615db96e0eeaf90dd3526b8da051c688189.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbdf615db96e0eeaf90dd3526b8da051c688189.png 2x" data-dominant-color="C5C4C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">703×537 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-13 18:33 UTC)

<p>If you save the segmentation as is, as a nrrd file, then you can find the label for each segment in the <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.h#L89-L102">file header</a> (in <code>SegmentN_Layer</code> and <code>SegmentN_LabelValue</code> fields).</p>
<p>If you think that this solution is not ideal for you then other approaches are available, too. What is your workflow? What software do you use to further process the segmentation? What is the overall goal of your project?</p>

---

## Post #3 by @N.Arjmandi (2020-07-13 20:16 UTC)

<p>Thank you very much!</p>
<p>I want to segment the organs using deep learning.</p>
<p>In the next step, Python software will be used.</p>
<p>I already need to create binary images for image processing. And I have to assign the same label value for each specific organ in all patients. For example, I want the bladder to get label value 2, rectum 3, for all patients.</p>
<p>I would appreciate if you mention other methods.</p>

---

## Post #4 by @lassoan (2020-07-14 06:07 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> what do you think would be a good solution? Maybe we could add an optional a color node input for segmentation labelmap export? Then the exporter could look up colors based on segment name or terminology. Some people already have a color table (which is used during import) and if the same colormap is used for export then the labelmaps would remain consistent.</p>
<p>There was also a <a href="https://discourse.slicer.org/t/segment-ids-when-imported-from-label-map/12502/2">similar question for the import side</a>. There is a solution for the import but it requires a good number of clicks and it is unlikely that users could figure it out by themselves. How do you think we could simplify? Should we add a color node selector to the qSlicerSegmentationsIOOptionsWidget for reading?</p>
<p>Maybe a common solution for both import and export would be to make it easier to create custom terminologies or improve color nodes so that they can contain standard terminologies. We could then use these to map label values to/from segment names and terminology.</p>

---

## Post #5 by @Sunderlandkyl (2020-07-14 14:11 UTC)

<p>Adding a color node option to import/export would be a good way to handle this issue.</p>
<p>I spent some time trying to come up with alternatives and couldn’t think of anything else that would handle the label values as efficiently/cleanly.</p>

---

## Post #6 by @pieper (2020-07-14 17:35 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="5" data-topic="12511">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>Adding a color node option to import/export would be a good way to handle this issue.</p>
</blockquote>
</aside>
<p>Yes, agreed.  We spent some time discussing it on this morning’s hangout and this would also help a use case I’m working on.</p>

---

## Post #7 by @N.Arjmandi (2020-07-14 19:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Finally, I  found a simple solution: first, in the segmentation module, move all the structure to the right and then sort them as desired on the left (based on the index you want the structure to take) , in next step , in the data module, create binary labelmap of structures.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bfab6648d6f089a64303ce45b0798096bf97ea5.png" data-download-href="/uploads/short-url/3Zw2wqUU13tuAgOnYSiGdgZqKzP.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bfab6648d6f089a64303ce45b0798096bf97ea5_2_690x393.png" alt="Capture" data-base62-sha1="3Zw2wqUU13tuAgOnYSiGdgZqKzP" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bfab6648d6f089a64303ce45b0798096bf97ea5_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bfab6648d6f089a64303ce45b0798096bf97ea5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bfab6648d6f089a64303ce45b0798096bf97ea5.png 2x" data-dominant-color="BBBBB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">882×503 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-07-14 19:52 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="5" data-topic="12511" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>Adding a color node option to import/export would be a good way to handle this issue.</p>
<p>I spent some time trying to come up with alternatives and couldn’t think of anything else that would handle the label values as efficiently/cleanly.</p>
</blockquote>
</aside>
<p>I’ve added an issue to keep track of this task: <a href="https://github.com/Slicer/Slicer/issues/5044" class="inline-onebox">Allow using a color node for segmentation to labelmap export · Issue #5044 · Slicer/Slicer · GitHub</a></p>

---

## Post #9 by @lassoan (2020-07-15 03:55 UTC)

<aside class="quote no-group" data-username="N.Arjmandi" data-post="3" data-topic="12511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c37758/48.png" class="avatar"> N.Arjmandi:</div>
<blockquote>
<p>I want to segment the organs using deep learning.</p>
<p>In the next step, Python software will be used.</p>
</blockquote>
</aside>
<p>I’ve added a few code snippets that should be useful: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p><code>extract_segments</code> extracts segments by name and sets their label in the output voxel array to specified values. To achieve what you described, you would need to run these few lines:</p>
<pre data-code-wrap="python"><code class="lang-python">input_filename = "/path/to/input.seg.nrrd"
output_filename = "/path/to/outpput.seg.nrrd"
segment_list = [("bladder", 2), ("rectum", 3), ("prostate", 5)]

voxels, header = nrrd.read(input_filename)
read_segmentation_info(input_filename)
output_voxels, output_header = extract_segments(voxels, header, segmentation_info, segment_list)
nrrd.write(output_filename, output_voxels, output_header)
</code></pre>

---
