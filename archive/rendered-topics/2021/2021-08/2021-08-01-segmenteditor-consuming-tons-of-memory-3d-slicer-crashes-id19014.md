# SegmentEditor consuming tons of memory & 3d slicer crashes

**Topic ID**: 19014
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/segmenteditor-consuming-tons-of-memory-3d-slicer-crashes/19014

---

## Post #1 by @Panda (2021-08-01 14:26 UTC)

<p>hello,</p>
<p>I have been working to automate some tasks for a set of CT scans which otherwise would take a long time. The code I wrote worked perfectly and in reasonable amount of time until now when I wrote a function where multiple segments (overall four colors) belonging to one category (one color) are merged together using the segment editor and logical operators. This function (if required could post it here) is now the bottleneck with the code not even finishing - I tried couple of things - but in vain - I also optimized my code where possible I thought I could - reducing time by 10-12 seconds, but still it takes a long time -and eventually 3d slicer crashes. I tried this on both - Mac (8 gigs RAM) and Windows (16 gigs RAM).</p>
<p>To figure out the bottleneck in more detail, I profiled my code and the attached snapshot shows the total time taken. I am a bit confused as to how this merging process can take so much time programmatically although when I do manually it is smooth and super fast. As can be seen from the profile report/analysis, the SegmentEditorThresholdEffect and SegmentEditorLogicalEffect are the two main functions that take most of the time. I have disabled volume rendering, display etc. but not much effect.</p>
<p>The function does this: There is a segmentation comprising of multiple RGBY segments and I have to merge them into just these four colors. So i add a new segment to my segmentation (empty) and then perform logical operations (union) on each segment of a particular color (modifier segment) and this new target segment and then remove the individual ones.</p>
<p>Can someone please share some insight as to what I could be doing wrong or some advice/tip? I can gladly share the code if required.</p>
<p>Edit 1: I added the code, should give more idea as to what I am doing. Let me know please if some info is required</p>
<p>CODE:</p>
<pre><code class="lang-auto"># segment editor part
def combine_same_colors(folder_num, bone_obj_seg_list, final_segmentation_node, final_segmentation):
	# naming and color vals
	vol_name = folder_num + 'HRimage'
	color_dict = {'blue': (0, 0, 1), 
				  'red': (1, 0, 0), 
				  'green': (0, 1, 0), 
				  'yellow': (1, 1, 0)}

# set up the segment editor widget and node
	vol_node = slicer.util.getNode(vol_name)
	seg_edit_wid = slicer.qMRMLSegmentEditorWidget()
	seg_edit_wid.setMRMLScene(slicer.mrmlScene)
	seg_edit_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
	seg_edit_wid.setMRMLSegmentEditorNode(seg_edit_node)
	seg_edit_wid.setSegmentationNode(final_segmentation_node)
	seg_edit_wid.setMasterVolumeNode(vol_node)

	seg_edit_wid.setActiveEffectByName("Logical operators")
	effect = seg_edit_wid.activeEffect()
	effect.setParameter("Operation", "UNION")
	segments_list = [i[0].get_segment() for i in bone_obj_seg_list]
	colors = ['blue', 'red', 'green', 'yellow']
# code to check if there are multiple segments belonging to same color and if yes, merge them
	def func(color):
	    	return lambda x: True if color in x else False
	for i in colors:
		check_multiple_seg = Counter(map(func(i), segments_list))[True]
		if check_multiple_seg &gt; 1:
			color_seg_list = [j for j in segments_list if i in j]

			segment_name = folder_num + 'lego' + i
			final_segmentation.AddEmptySegment(segment_name)
			final_segmentation.GetSegment(segment_name).SetColor(color_dict[i][0],
																 color_dict[i][1],
																 color_dict[i][2])

			# target_seg_id = final_segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(segment_name)
			target_seg_id = final_segmentation.GetSegmentIdBySegmentName(segment_name)
			# source_seg_id = [final_segmentation_node.GetSegmentation().GetSegmentIdBySegmentName(i) for i in color_seg_list]
			source_seg_id = [final_segmentation.GetSegmentIdBySegmentName(i) for i in color_seg_list]

			seg_edit_node.SetSelectedSegmentID(target_seg_id)

			for i in source_seg_id:
				effect.setParameter("ModifierSegmentID", i)
				effect.self().onApply()
				final_segmentation.RemoveSegment(i)

	return final_segmentation_node, final_segmentation
</code></pre>
<p>Thank you very much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/680d45a1a03835d54d8efd90d2b7f2fc9d9bbd8e.png" data-download-href="/uploads/short-url/eQu5HQ7CZXhKQH2sL0u6rFUO2Jg.png?dl=1" title="Screenshot 2021-08-01 at 3.42.50 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680d45a1a03835d54d8efd90d2b7f2fc9d9bbd8e_2_690x190.png" alt="Screenshot 2021-08-01 at 3.42.50 PM" data-base62-sha1="eQu5HQ7CZXhKQH2sL0u6rFUO2Jg" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680d45a1a03835d54d8efd90d2b7f2fc9d9bbd8e_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680d45a1a03835d54d8efd90d2b7f2fc9d9bbd8e_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/680d45a1a03835d54d8efd90d2b7f2fc9d9bbd8e_2_1380x380.png 2x" data-dominant-color="E1E1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-08-01 at 3.42.50 PM</span><span class="informations">2250×622 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Windows Errors: (I also increased the virtual memory in Win 10, but no improvement)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b1446ad883ecd8575a8c3f49cadbf8fcf82f291.png" data-download-href="/uploads/short-url/m7TrQQC0c4e4FHz1B4UbjEZTS9P.png?dl=1" title="err1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1446ad883ecd8575a8c3f49cadbf8fcf82f291_2_690x98.png" alt="err1" data-base62-sha1="m7TrQQC0c4e4FHz1B4UbjEZTS9P" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1446ad883ecd8575a8c3f49cadbf8fcf82f291_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1446ad883ecd8575a8c3f49cadbf8fcf82f291_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1446ad883ecd8575a8c3f49cadbf8fcf82f291_2_1380x196.png 2x" data-dominant-color="FEF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">err1</span><span class="informations">3250×462 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8799729179075bd3bf7230280fca48544b2822a.jpeg" data-download-href="/uploads/short-url/zs6UYQbR15wQFYCtSBgioOLxRjk.jpeg?dl=1" title="err2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8799729179075bd3bf7230280fca48544b2822a_2_690x388.jpeg" alt="err2.PNG" data-base62-sha1="zs6UYQbR15wQFYCtSBgioOLxRjk" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8799729179075bd3bf7230280fca48544b2822a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8799729179075bd3bf7230280fca48544b2822a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8799729179075bd3bf7230280fca48544b2822a_2_1380x776.jpeg 2x" data-dominant-color="BEBDC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">err2.PNG</span><span class="informations">1920×1080 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-08-01 14:35 UTC)

<p>As a hint to help you get help on this, it’s good to provide a way for others to replicate the issue easily (replicate on sample data, provide a one-line way to replicate the issue, etc).  These guidelines can help: <a href="http://sscce.org/">http://sscce.org/</a></p>

---

## Post #3 by @Panda (2021-08-01 14:40 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> hello, thanks for the reply. Right, let me refactor it so that it could be run on on other machines as well. On it!</p>
<p>Meanwhile if the above info can provide some clues, would be nice! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2021-08-01 22:07 UTC)

<p>Combining segments is a very complex operation, because it has to take into account all 3 kinds of masking methods and needs to manage multiple segmentation layers.</p>
<p>If your segments are not overlapping then it should be simpler and faster to combine the segments while they are still stored in a labelmap (in a numpy array) and import the result into a segmentation node.</p>

---

## Post #5 by @Panda (2021-08-02 04:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for the advice. I have three questions with respect to this:</p>
<ol>
<li>I am a bit uncertain as to how do you combine segments while they are in a labelmap volumes, like you mentioned. I have my ROIs as STL files which I load segmentations in 3d slicer and then export them to binary label map. And now when I have these label maps of different segmentations, how to get them together?</li>
</ol>
<p>Right, so on experimenting I found two modules that go by the name - “Add scalar volume” and “Image Label Combine”. The first one is, from what I understand for scalar volumes whereas the second one is specifically for combining labelmap volumes of same sizes. Am I correct here or is there some other piece of functionality in 3D slicer that exists and that I am missing here? The problem I get with this is - I combined labelmap volumes using the Image Label Combine module, however, in the final combined label map volume, the segmentations lose their color and they become all of one color which is not what is desired. This is surprising because in the segmentations module and in their own individual label map volumes, they still retain their color.</p>
<ol start="2">
<li>
<p>This one I just thought of as I remembered that my original ROIs are in STL format. So I exported them to models and then using the “Merge Models” module, combined them and then exported to segmentation node. It worked - what I would be glad to know that if I automate this then i hope this is not a complex operation like with segment editor where manually it worked fine but on automating, it blew up</p>
</li>
<li>
<p>After researching, I am not able to find much documentation code related to the two modules above - is it possible to do the above through Python (merge models and image label combine modules)?</p>
</li>
</ol>
<p>P.S - <a class="mention" href="/u/lassoan">@lassoan</a> Could you please guide as to how this complex procedure could be avoided and done without segment editor. I found an old post where you mentioned that segmenteditor is the way to go ahead (<a href="https://discourse.slicer.org/t/merging-two-models/931" class="inline-onebox">Merging two models</a>) but as can be seen, it might not be the best way - so if you could expand a bit on your previous suggestion - i would really appreciate it.</p>
<p>Thank you.</p>

---

## Post #6 by @lassoan (2021-08-02 05:22 UTC)

<p>Conversion from closed surface to labelmap is best done by Segmentations module.</p>
<p>Combining non-overlapping segments is internally complex (due to the reasons I described above, it also consumes more memory due to saving undo information, etc). If all you need is to change labels in a simple 3D volume then even “Image Label Combine” module is an overkill nowadays.  You can simply export the segmentation to labelmap volume and manipulate its voxels as a numpy array, using standard numpy operations. For example, if you get the voxels as a numpy array <code>a</code> then you can merge all non-zero labels (set them to 1) by calling: <code>a[a&gt;0]=1</code>.</p>

---
