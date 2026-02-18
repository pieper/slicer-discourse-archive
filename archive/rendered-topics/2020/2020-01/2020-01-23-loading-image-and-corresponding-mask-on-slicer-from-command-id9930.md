# Loading image and corresponding mask on Slicer from command line

**Topic ID**: 9930
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/loading-image-and-corresponding-mask-on-slicer-from-command-line/9930

---

## Post #1 by @tbillah (2020-01-23 21:58 UTC)

<p>Hi there,</p>
<p>Is there a command like:</p>
<blockquote>
<p>Slicer T1.nii.gz LabelMap=Mask.nii.gz</p>
</blockquote>
<p>using which I can load an image and its mask (as LabelMap) directly from the command line?</p>
<p>Basically, I want to replicate the following GUI loading from the command line:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f4c3006533c53c64d85aa904c53cf0825defd7a.png" data-download-href="/uploads/short-url/6KpFGg3Eh6QqAkc1iAe75xF9Qw2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f4c3006533c53c64d85aa904c53cf0825defd7a_2_690x305.png" alt="image" data-base62-sha1="6KpFGg3Eh6QqAkc1iAe75xF9Qw2" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f4c3006533c53c64d85aa904c53cf0825defd7a_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f4c3006533c53c64d85aa904c53cf0825defd7a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f4c3006533c53c64d85aa904c53cf0825defd7a.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×439 25.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note that:</p>
<blockquote>
<p>Slicer T1.nii.gz Mask.nii.gz</p>
</blockquote>
<p>will load two images as two foreground volumes which don’t serve the purpose I am interested in.</p>

---

## Post #2 by @lassoan (2020-01-24 01:13 UTC)

<p>Deafult loader is used when you simply pass the file name.</p>
<p>You can use .label.nii.gz extension instead of just .nii.gz as a hint to get your volume loaded as labelmap (or .seg.nrrd to make it load as a segmentation).</p>
<p>If renaming the file is impossible then you can force reading as volume+labelmap by calling <code>Slicer.exe --python-code "slicer.util.loadVolume('/tmp/series/T1.nii.gz'); slicer.util.loadLabelVolume('/tmp/series/Mask.nii.gz')"</code> or as volume+segmentation by by calling <code>Slicer.exe --python-code "slicer.util.loadVolume('/tmp/series/T1.nii.gz'); seg=slicer.util.loadSegmentation('/tmp/series/Mask.nii.gz'); seg.CreateClosedSurfaceRepresentation()"</code>.</p>
<p>Segmentation has many advantages over simple labelmaps, for example, it is rendered in slice views a bit nicer (it shows a stronger outline and more transparent filling) it can be easily displayed in 3D view, you can sort&amp;filter segments, associate with standard terminologies, etc.</p>

---

## Post #3 by @tbillah (2020-01-24 14:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, the following does not load as you expected:</p>
<blockquote>
<p>Slicer T1.nii.gz Mask.label.nii.gz</p>
</blockquote>
<p>Rather, it still loads them as two separate foreground volumes.</p>
<p>FYI, my Slicer is:<br>
<code>Slicer-4.10.2-linux-amd64/Slicer</code></p>
<p>Are we missing something here?</p>

---

## Post #4 by @lassoan (2020-01-24 14:48 UTC)

<p>That’s right, <code>Slicer something.seg.nrrd</code> is loaded properly as segmentation but <code>something.label.nrrd</code> is still loaded as scalar volume (if you drag-and-drop something.label.nrrd then by default it is loaded as labelmap, but not when passing as command-line argument).</p>
<p>I’ll add .label.nii.gz and .label.nrrd as recognized composite file extensions to Slicer Preview Release, but until then you can use <code>--python-code</code> argument to force loading any volume as labelmap (regardless of filename extension).</p>

---

## Post #5 by @tbillah (2020-01-24 15:03 UTC)

<p>Thanks. I confirm that the following works:</p>
<pre><code class="lang-auto">Slicer --python-code "slicer.util.loadVolume('T1.nii.gz');slicer.util.loadLabelVolume('Mask.nii.gz');
slicer.util.getNode('vtkMRMLSliceNodeRed').SetUseLabelOutline(1);
slicer.util.getNode('vtkMRMLSliceNodeYellow').SetUseLabelOutline(1);
slicer.util.getNode('vtkMRMLSliceNodeGreen').SetUseLabelOutline(1)"
</code></pre>
<p>By the way, can you give any shortcut for the last three lines? As you know, they produce the following view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3d9f7bdd0075dd091492b293b5cada30ef82a66.jpeg" data-download-href="/uploads/short-url/nnuOVvBrpldEvajmbunWy6SVaVo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3d9f7bdd0075dd091492b293b5cada30ef82a66_2_331x500.jpeg" alt="image" data-base62-sha1="nnuOVvBrpldEvajmbunWy6SVaVo" width="331" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3d9f7bdd0075dd091492b293b5cada30ef82a66_2_331x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3d9f7bdd0075dd091492b293b5cada30ef82a66_2_496x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3d9f7bdd0075dd091492b293b5cada30ef82a66_2_662x1000.jpeg 2x" data-dominant-color="848490"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">858×1295 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2020-01-24 15:16 UTC)

<p>You can show a volume in slice views by calling <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L322-L332"><code>slicer.util.setSliceViewerLayers</code></a>.</p>

---

## Post #7 by @tbillah (2020-01-24 15:22 UTC)

<p>With this option, there is no control for “toggle between showing label map volume with regions filled or outlined.”</p>

---

## Post #8 by @lassoan (2020-01-24 15:31 UTC)

<p>You can change labelmap display node properties to set region outline/filling, but I would recommend to load labelmap volumes as segmentation instead (due to the advantages described above).</p>

---

## Post #9 by @tbillah (2020-01-24 16:11 UTC)

<blockquote>
<p>You can change labelmap display node properties to set region outline/filling</p>
</blockquote>
<p>I am sure this is a good idea. But can you be more specific about how to do that?</p>

---

## Post #10 by @lassoan (2020-01-24 16:43 UTC)

<p>Sorry, outline/filling is not defined in labelmap display node but in <a href="http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html#a86599c00bb51107b577133825ce67a6f">vtkMRMLSliceNode</a>.</p>

---

## Post #11 by @tbillah (2020-01-24 16:50 UTC)

<p>Yup, coming back to what I noted in first place. Use three lines like this:</p>
<pre><code class="lang-auto">slicer.util.getNode('vtkMRMLSliceNodeRed').SetUseLabelOutline(1);
</code></pre>
<p>So, no shortcut for setting the property for all views all together.</p>

---

## Post #12 by @lassoan (2020-01-24 17:34 UTC)

<p>It would be easy to add outline/fill as an option to setSliceViewerLayers (pull requests are welcome), which would simplify the startup script. You can also add utility function like <code>slicer.show('somevolume.nrrd','somelabel.nrrd')</code> to your <code>.slicerrc.py</code> file or in an extension.</p>
<p>However, labelmap volumes are becoming more and more used just as legacy infrastructure, so I would recommend to load them as segmentation (<code>slicer.util.loadSegmentation('somelabel.nrrd')</code>).</p>

---

## Post #13 by @oguzcanbekar (2023-01-10 07:34 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> I really appreciate for your effort!</p>
<p>Related to this command I would like to ask something…</p>
<p>As you mention I am able to run my image and corresponding a segmentation file from terminal but I would like to ask How can I run same image with 2 diiferent corresponding segmentation files? Is it possible?</p>
<p>Thank you very much again.!</p>

---
