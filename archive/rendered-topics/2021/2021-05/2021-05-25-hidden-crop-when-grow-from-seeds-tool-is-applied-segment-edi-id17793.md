---
topic_id: 17793
title: "Hidden Crop When Grow From Seeds Tool Is Applied Segment Edi"
date: 2021-05-25
url: https://discourse.slicer.org/t/17793
---

# Hidden crop when GROW from seeds tool is applied (Segment Editor Module)

**Topic ID**: 17793
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/hidden-crop-when-grow-from-seeds-tool-is-applied-segment-editor-module/17793

---

## Post #1 by @ond12 (2021-05-25 15:26 UTC)

<p>Hello 3DSlicer forum ,</p>
<p>I have encountered a weird behavior with the tool “Grow From Seed” in the Segment Editor module :</p>
<p>Sometimes when I apply Grow from Seeds , after having painted inside a segment (choosing “inside segment” and “overwrite visible” as parameters), my previous segment (in which I have painted) isn’t fully completed.<br>
Like the "Grow from seed " tool only take into account a small region and not my entire segment mask.  For information, the mask (i.e. the bone on which I apply my Grow from seeds), is the tibia completely colored initially.<br>
Also, normally by coloring my tibia completely on more images I won’t have this error, but I would like to know if it is possible to color automatically the whole mask.</p>
<p>Therefore the “Grow from seed” Result stop abrulty at a line.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee317361bea27c8c7bafd7fa2a16c0df2ac5c58.jpeg" data-download-href="/uploads/short-url/y5ib0eXMsuEO1MTA2daFz1hUqqQ.jpeg?dl=1" title="GFS_CROPED.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee317361bea27c8c7bafd7fa2a16c0df2ac5c58_2_504x499.jpeg" alt="GFS_CROPED.PNG" data-base62-sha1="y5ib0eXMsuEO1MTA2daFz1hUqqQ" width="504" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee317361bea27c8c7bafd7fa2a16c0df2ac5c58_2_504x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee317361bea27c8c7bafd7fa2a16c0df2ac5c58.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee317361bea27c8c7bafd7fa2a16c0df2ac5c58.jpeg 2x" data-dominant-color="403D48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GFS_CROPED.PNG</span><span class="informations">713×706 74.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Another same example but here we can clearly see the left bottom left and rigth boudaries of the blur grow from seed result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5627cb577e6448111c0089a98b8fc91a9ff3fa.png" data-download-href="/uploads/short-url/6bn7ldj8qGlAXqmBVTZnR7VSh3Y.png?dl=1" title="cropGFS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5627cb577e6448111c0089a98b8fc91a9ff3fa_2_388x500.png" alt="cropGFS" data-base62-sha1="6bn7ldj8qGlAXqmBVTZnR7VSh3Y" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5627cb577e6448111c0089a98b8fc91a9ff3fa_2_388x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5627cb577e6448111c0089a98b8fc91a9ff3fa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5627cb577e6448111c0089a98b8fc91a9ff3fa.png 2x" data-dominant-color="3C3C4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cropGFS</span><span class="informations">557×716 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know why ? Is there a solution for this problem ? ( If necessary I not afraid of scripting something )</p>

---

## Post #2 by @lassoan (2021-05-26 04:23 UTC)

<p>Region growing is performed around the area designated by the seeds, expanded with about a 20% margin on all sides. All you need to do to expand the segmentation further in any direction is to paint a small additional seed close to the boundary.</p>

---

## Post #3 by @ond12 (2021-05-26 07:00 UTC)

<p>hello Lassoan ,</p>
<p>Thanks for you help, so I need to do some manual paint for this tool to work.<br>
Is there a way to tweak the code or script something to automate this task ?</p>
<p>Remove the region limitation or increase the margin maybe ?</p>

---

## Post #4 by @lassoan (2021-05-26 17:42 UTC)

<p>Grow from seeds requires a at least one small seed region for each segment. For easy segmentation tasks you can generate these seeds fully automatically or use other tools (e.g., Thresholding and Islands / Split islands to segments). If you describe what you would like to achieve on what kind of images then we can give more specific advice.</p>

---

## Post #5 by @ond12 (2021-05-28 07:57 UTC)

<p>Hello Lassoan,</p>
<p>Thank you for your time and your help. I think I misspoke indeed my goal is not really to do the segmentation of this image ( it was just an example to illustrate an issue in the grow from seed tool that I want to correct) .</p>
<p>I’m currently develloping a Python module extension that use the grow from seed tool.</p>
<p>I want to know how it’s possible to remove this Roi limitation in the GFS tool by code and set the work region for a whole segmentation mask ?</p>
<p>Is there a solution for this problem , Should I go c++ or still possible in python in which files ?</p>
<p>Best regards<br>
Thank you</p>

---

## Post #6 by @lassoan (2021-05-28 19:48 UTC)

<p>You can modify <code>extentGrowthRatio</code> to add a larger margin around the seeds. If you specify a very large value then it will always include the entire volume. For example, if you use the Segment editor module:</p>
<pre data-code-wrap="python"><code class="lang-python">gfs = slicer.modules.SegmentEditorWidget.editor.effectByName('Grow from seeds').self()
gfs.extentGrowthRatio = 10000
</code></pre>
<p>You may also try Local threshold effect, which takes care of the extent (it uses whatever large extent is needed), allows setting the threshold range in the same tool (you draw a small region to specify the threshold range, then you get the complete segmentation with a single Ctrl-click):</p>
<aside class="quote quote-modified" data-post="1" data-topic="9233">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">New Segment Editor effect: Local threshold</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Local threshold, a new semi-automatic segmentation method, has been added to the Segment Editor. It is available in both the 4.11.0 and 4.10.2 releases through the SegmentEditorExtraEffects extension. This effect adds connected voxels to segments that are within a specified threshold, and attempts to prevent leaks into other structures through small connecting regions. The result is similar to that of the “Level trace” effect in that it delineates a region within a certain threshold value, howev…
  </blockquote>
</aside>


---
