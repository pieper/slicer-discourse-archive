---
topic_id: 12054
title: "Question On Using Decimated Model In Vmtk Plugin"
date: 2020-06-16
url: https://discourse.slicer.org/t/12054
---

# Question on using decimated model in VMTK plugin

**Topic ID**: 12054
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/question-on-using-decimated-model-in-vmtk-plugin/12054

---

## Post #1 by @Deepa (2020-06-16 11:55 UTC)

<p>Hello Everyone,</p>
<p>I’ve decimated a model (Reduction: 0.7). The decimated model is used for Computing centerlines. After I hit Preview, the following is displayed in Python interactor</p>
<p><code>Mesh subdivision failed. Skip subdivision step.</code></p>
<p>Could someone explain what this error means? Is it ok do proceed with computing centerlines after the above-mentioned error pops up?</p>

---

## Post #2 by @lassoan (2020-06-16 13:04 UTC)

<p>By default, triangles of the mesh are subdivided to make network extraction more robust. However, mesh subdivision may fail for non-manifold meshes.</p>
<p>If your mesh resolution is already high enough (this is the case most of the time) then skipping mesh subdivision is not a problem. However, the failure indicates that the mesh has errors, which may impact network extraction, therefore you may consider smoothing the segmentation using median method (before model exporting the segmentation to model).</p>

---

## Post #3 by @Deepa (2020-06-16 13:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>smoothing the segmentation using median method</p>
</blockquote>
</aside>
<p>Thank you.<br>
I couldn’t locate the module that offers smoothing using median method. Can I simply use Segment Editor  and set <code>Smoothing Factor</code> to 1?</p>

---

## Post #4 by @lassoan (2020-06-16 13:39 UTC)

<p>Median smoothing method is available in Segment Editor’s Smoothing effect.</p>

---

## Post #5 by @Deepa (2020-06-16 13:56 UTC)

<p>Thank you. Can I use the default value of 3.00 mm for Kernel size?</p>

---

## Post #6 by @Deepa (2020-06-16 14:49 UTC)

<p><span class="mention">@lasson</span></p>
<p>I’ve used Median Smoothing to smooth the segment using default value of 3.00 mm for Kernel size . The <a href="https://github.com/DeepaMahm/misc/blob/master/Segmentation3_smoothed.seg.nrrd" rel="nofollow noopener">smoothed segment</a><br>
was decimated (0.9 reduction) was converted to <a href="https://github.com/DeepaMahm/misc/blob/master/segment3_model.vtk" rel="nofollow noopener">model</a>. The <a href="https://github.com/DeepaMahm/misc/blob/master/segment3_deci_0.9.vtk" rel="nofollow noopener">decimated model</a> is now used  for Computing Centerlines.</p>
<p>Unfortunately, I get the same error (<code>Mesh subdivision failed. Skip subdivision step.</code>) for 0.9 reduction. This error doesn’t occur for 0.7 reduction now. But since the memory usage is high while computing centerlines, I want to decimate it &gt;0.9.</p>
<p>Could you please have a look at the model files shared in the links provided above?</p>

---

## Post #7 by @Deepa (2020-06-17 01:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>If you had a chance to look at the files, I’d like to know if the same error appears and I would also like to ask for suggestions on how to resolve to this error.<br>
Thanks a lot for all your support</p>

---

## Post #8 by @Deepa (2020-06-17 17:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Reducing above 0.9 doesn’t work most of the time. I am really stuck here, unfortunately.</p>
<pre><code>Mesh subdivision failed. Skip subdivision step.
Input model preparation failed. It probably has surface errors.</code></pre>

---

## Post #9 by @lassoan (2020-06-17 17:32 UTC)

<p>There are several decimation methods available. Some of them work perfectly with your data set. I’m tuning things a bit and then describe which one to use and how.</p>

---

## Post #10 by @Deepa (2020-06-17 17:33 UTC)

<p>Thanks a ton <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=9" title=":upside_down_face:" class="emoji" alt=":upside_down_face:"></p>

---

## Post #11 by @Deepa (2020-06-19 03:32 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
May I know when I will be able to use this feature?</p>

---

## Post #12 by @lassoan (2020-06-19 16:47 UTC)

<p>It is available in today’s Slicer Preview Release:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12117">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">New module: Extract Centerline (in SlicerVMTK extension)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a completely new module that makes vessel (or airway or any other tree structure) centerline extraction much faster, flexible, and robust. It can quickly extract a network, determine branch endpoints automatically, allows editing of endpoints, computing centerlines, branches, and quantitative metrics (radius, curvature, torsion, etc). The new “Extract Centerline” module is available in SlicerVMTK extension for latest Slicer-4.11 release (it replaces the old “Centerline Computation” modu…
  </blockquote>
</aside>


---

## Post #13 by @Deepa (2020-06-20 11:51 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks a lot, I really like the new module especially the relocation of endpoints for positioning on the Voronoi model, autodetect, and deletion of endpoints. In the Windows version, I could view both centerline and Voronoi model after hitting <code>Apply</code>. I am not able to view the Voronoi model in Linux version though.</p>
<p>Could you please explain a bit about how  <code>Decimation Aggressiveness</code> woks?</p>
<p>I’d also like to know if the documentation of <code>Extract Centerlines</code> module is already available.</p>

---

## Post #14 by @lassoan (2020-06-20 20:55 UTC)

<p>Parameters are explained in tool tips that appear when you hover over with the mouse and leave there for a few seconds.</p>

---

## Post #15 by @Deepa (2020-06-21 03:30 UTC)

<p>Thank you.</p>
<aside class="quote no-group" data-username="Deepa" data-post="13" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I am not able to view the Voronoi model in Linux version though</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f151ad45441e4a712ea9510f24c63a7bf7cb05a.png" data-download-href="/uploads/short-url/29qnursbb9oIIDwGG2VeTMcQBN8.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f151ad45441e4a712ea9510f24c63a7bf7cb05a_2_345x223.png" alt="Untitled" data-base62-sha1="29qnursbb9oIIDwGG2VeTMcQBN8" width="345" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f151ad45441e4a712ea9510f24c63a7bf7cb05a_2_345x223.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f151ad45441e4a712ea9510f24c63a7bf7cb05a_2_517x334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f151ad45441e4a712ea9510f24c63a7bf7cb05a_2_690x446.png 2x" data-dominant-color="CED5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">917×594 84.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please look into this?</p>

---

## Post #16 by @Deepa (2020-06-21 03:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="12054" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Parameters are explained in tool tips that appear when you hover over with the mouse and leave there for a few seconds.</p>
</blockquote>
</aside>
<p>Thank you. I’m trying to understand the relation between <code>Target point count</code> and <code>Decimation aggressiveness</code>. From what I understand from the explanations provided in the tool tip, <code>Target point count</code> does the function of <code>Reduction</code> (a ratio, varied between 0-1; similarly what’s the range of <code>Decimation aggressiveness</code>) previously available in the <code>centerline computation</code> module i.e reduce the number of points on the surface.  But I don’t clearly understand how <code>Decimation aggressiveness</code></p>
<blockquote>
<p>Lower values preserve mesh integrity better but it may not be possible to reduce number of points to desired level</p>
</blockquote>
<p>is related to  <code>Target point count</code>. For instance, I thought if I vary one (e.g. <code>Target point count</code>) the other parameter (<code>Decimation Aggressivess</code>) will vary as a function of the former. But this doesn’t happen.</p>
<p>Could you please explain this a bit?</p>

---

## Post #17 by @muratmaga (2020-06-21 04:00 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="13" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I am not able to view the Voronoi model in Linux version though</p>
</blockquote>
</aside>
<p>You need to experiment a bit more to investigate the issue. For example, if you take the scene from the Linux, can you visualize the missing voronoi diagram on your windows? If that’s the case it might be related to your Linux graphics settings.</p>

---

## Post #18 by @Deepa (2020-06-21 04:29 UTC)

<p>Thank you. The problem is after using <code>Extract Centerlines</code>, in addition to the Voronoi model, I am not able to view the segmentation volume too (this can be seen in the snapshot posted above- the eye icon next to segmentation node is open ). The segmentation volume is visible after loading the file though, prior to centerline computation. The volume disappears after hitting Apply in <code>Extract Centerlines</code>. So I think the problem may not be due to the Linux graphics settings.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Could you please look into this?</p>

---

## Post #19 by @lassoan (2020-06-21 14:09 UTC)

<p>Please add a new topic to discuss this models/volume not appearing issue. Try to reproduce it without VMTK, just by loading models and adjusting transparency settings and enabling/disabling depth peeling in the 3D view.</p>

---

## Post #20 by @Deepa (2020-06-21 16:23 UTC)

<p>Thanks a lot for your response. Sure , my question on <code>Decimatin aggressivenes</code> remains here and I have navigated the other question to  <a href="https://discourse.slicer.org/t/problem-in-viewing-segmentation-volume-and-voronoi-model/12144">new thread</a></p>

---

## Post #21 by @lassoan (2020-06-21 16:50 UTC)

<p>Aggressiveness controls how much simplification is allowed. If aggressiveness value is too low then you may not be able to reach the point count target. If aggressiveness value is too high then you may have errors in the generated mesh.</p>

---

## Post #22 by @Deepa (2020-06-22 02:56 UTC)

<p>Thank you. May I know what’s the range in which this parameter can be varied? Or is it recommended to use the default?</p>

---

## Post #23 by @lassoan (2020-06-22 04:00 UTC)

<p>Any positive “aggressiveness” value is valid, but on the models I’ve tested on values in 3.5 to 4.5 range worked best.</p>
<p>I have added detailed “Extract centerline” module documentation here: <a href="https://github.com/vmtk/SlicerExtension-VMTK#extract-centerline">https://github.com/vmtk/SlicerExtension-VMTK#extract-centerline</a></p>

---

## Post #24 by @Deepa (2020-06-22 16:27 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I would like to know if you had a chance to test the centerline computation on the model file that I had shared to understand how much memory would be required and the duration that it takes.</p>
<p>I’d also like to know if multi-thread centerline extraction can be executed.</p>

---

## Post #25 by @lassoan (2020-06-23 02:23 UTC)

<p>Yes, it works well.</p>
<p>Starting from your original model (525k points, 1051k cells), with default settings, endpoint auto-detection is done under 15 seconds and with these endpoints centerlines are detected in less than  1 minute. Memory usage does not go above 1GB.</p>
<p>Branch extraction (computation of centerline curve or quantification results) seems to be sensitive to presence of unreachable endpoints: computation can take a really long time and lots of memory (maybe it never completes?). For example, I had to stop one execution after about half an hour computation and 10GB memory usage. After deleting all the unreachable endpoints, computation was completed within a couple of minutes (and peak memory usage was not more than 1.2GB).</p>

---

## Post #26 by @Deepa (2020-06-23 02:43 UTC)

<p>Thanks a lot for sharing the link to documentation.</p>
<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Branch extraction (computation of centerline curve or quantification results) seems to be sensitive to presence of unreachable endpoints: computation can take a really long time and lots of memory (maybe it never completes?).</p>
</blockquote>
</aside>
<p>Yes, it never completes. I have been facing memory issues in the past while trying to obtain the quantification results and the centerline detection worked absolutely fine. I now switched to a server with 35GB of free memory and the process is still running for more than 12 hours. So I was wondering why it’s taking so long and why does it consuming so much memory</p>
<p>Could you please let me know how to find out the unreachable endpoints ?  Should I have a look at the Voronoi model and find out the endpoints that don’t lie on the Voronoi model? If you could add a snapshot of the <code>unreachable endpoints</code> that you are referring to, that will be really helpful.</p>
<p>I also have a suggestion, I think it would be helpful for the users if Slicer can throw a warning before<br>
the <code>computation of centerline curve or quantification results</code> task is initiated when unreachable endpoints are present in the model.</p>

---

## Post #27 by @lassoan (2020-06-23 03:27 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="26" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Could you please let me know how to find out the unreachable endpoints ?</p>
</blockquote>
</aside>
<p>Look for the straight line segments, as <a href="https://youtu.be/yi07mjr3JeU?t=257">shown in the tutorial video</a>. For each unreachable point, you can decide to move it to the Voronoi model surface or (if they are actually not connected to the rest of the tree) delete it.</p>
<aside class="quote no-group" data-username="Deepa" data-post="26" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I also have a suggestion, I think it would be helpful for the users if Slicer can throw a warning before<br>
the <code>computation of centerline curve or quantification results</code> task is initiated when unreachable endpoints are present in the model.</p>
</blockquote>
</aside>
<p>Yes, of course, it would be great to detect these points automatically. Could you give it a try to implement it? Centerline extraction is just a Python script, so you can make changes very easily. You just need to do some detective work to figure how these points can be detected: search on google in VMTK mailing list archives, ask on the mailing list, or maybe review and figure out something from VMTK source code.</p>

---

## Post #28 by @Deepa (2020-06-23 04:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Look for the straight line segments, as <a href="https://youtu.be/yi07mjr3JeU?t=257" rel="noopener nofollow ugc">shown in the tutorial video</a>. For each unreachable point, you can decide to move it to the Voronoi model surface or (if they are actually not connected to the rest of the tree) delete it.</p>
</blockquote>
</aside>
<p>I had noticed this in the tutorial and removed 1 line before I initiated the run. I had a relook at the model and figured out there was another straight line that I missed. Finally after removing both, the quantification of results completed in less than 2 minutes. Never imagined the presence of these lines could cause a lot of trouble. Thanks a lot !</p>
<p>However, I also noticed that the centerlines aren’t detected for some branches in the model that I have shared before.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ecc378cbe6a91d1115f10d1daa7ce49c63cea42.png" data-download-href="/uploads/short-url/fOa3o19CZCy9WYSOwixsZo93LMK.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecc378cbe6a91d1115f10d1daa7ce49c63cea42_2_345x209.png" alt="Untitled" data-base62-sha1="fOa3o19CZCy9WYSOwixsZo93LMK" width="345" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecc378cbe6a91d1115f10d1daa7ce49c63cea42_2_345x209.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecc378cbe6a91d1115f10d1daa7ce49c63cea42_2_517x313.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecc378cbe6a91d1115f10d1daa7ce49c63cea42_2_690x418.png 2x" data-dominant-color="7C8F9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1020×619 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please let me know  if it’s possible to do some manual intervention to enable the centerline computation of these vessel segments too?</p>
<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, of course, it would be great to detect these points automatically. Could you give it a try to implement it?</p>
</blockquote>
</aside>
<p>Sure, I will discuss this issue on VMTK mailing list and keep you posted here.</p>
<p>Thanks a lot for your tremendous support!</p>

---

## Post #29 by @lassoan (2020-06-23 19:01 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="28" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Could you please let me know if it’s possible to do some manual intervention to enable the centerline computation of these vessel segments too?</p>
</blockquote>
</aside>
<p>Path search between endpoints fail if no path is found, i.e., the route would need to go through very thin or non-existing segmented regions. You need to improve the segmentation’s quality (increase image resolution, smooth it more carefully) and/or tune surface smoothing. You can try disabling surface smoothing completely to ensure that branches are not thinned at all.</p>
<aside class="quote no-group" data-username="Deepa" data-post="28" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>However, I also noticed that the centerlines aren’t detected for some branches in the model that I have shared before.</p>
</blockquote>
</aside>
<p>If a branch is clearly visible in the segmentation (branch is not thin and its tip is not pointy) but the branch is not in the preprocessed model then you can increase the <code>Target point count</code> or decrease <code>Decimation aggressiveness</code>.</p>

---

## Post #30 by @Deepa (2020-06-25 06:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you. I’m trying out the about-mentioned suggestion on improving the segmentation quality.</p>
<p>But from what I understand, only tree-like structure is returned and the loops /cycles aren’t detected.</p>
<p>EDIT:<br>
It is indeed true. Please check the following excerpt from [<a href="https://groups.google.com/forum/?utm_medium=email&amp;utm_source=footer#!searchin/vmtk-users/loops%7Csort:date/vmtk-users/QGLCi6fs78U/HI6GbBnvp2AJ" rel="noopener nofollow ugc">vmtk mailing list</a>], written by Luca</p>
<blockquote>
<p>Indeed the centerlines filter doesn’t catch loops, which is usually ok for arterial trees, but it can be limiting in other situations such as yours.The reason is that the algorithm searches for some sort of shortest path from the inlet to the outlet, thus is will only choose one of the two arms of the loop.<br>
There are a couple of things you can do:</p>
<ol>
<li>
<p>This is a hack:<br>
a) generate one centerline and save it to a file<br>
b) use vmtksurfaceclipper to make a cut in the branch in which the centerline  was generated<br>
c) run vmtkcenterlines again; it will extract the other branch (since the former is not continuous due to the cut); save it to another file<br>
d) use vmtksurfaceappend to have the two centerlines in one dataset, if you need this</p>
</li>
<li>
<p>use vmtknetworkextractor; make sure the surface has at least one opening and run the script; this algorithm is less accurate in tracing the centerline, although it might be enough for your needs; however, it handles loops correclty</p>
</li>
</ol>
</blockquote>

---

## Post #31 by @Deepa (2020-06-25 10:58 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I’ve testes the above. Networkmodel, I belive is obtained using VMTK’s networkextraction, captures the loops -blue lines appropriately.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f81a7fc59d55b4ce42324c543f234573668e6dc4.png" data-download-href="/uploads/short-url/zoPbzRWsvnPNfsJbQfIZICscpKs.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a7fc59d55b4ce42324c543f234573668e6dc4_2_269x250.png" alt="Untitled" data-base62-sha1="zoPbzRWsvnPNfsJbQfIZICscpKs" width="269" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a7fc59d55b4ce42324c543f234573668e6dc4_2_269x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a7fc59d55b4ce42324c543f234573668e6dc4_2_403x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a7fc59d55b4ce42324c543f234573668e6dc4_2_538x500.png 2x" data-dominant-color="7B9399"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">600×557 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It will be really helpful if the <code>quantifications results</code> are made available for the network model in addition to the centerline model. I hope this will be easy and the network polydata can be used as input instead of centerline polydata in <code> createCurveTreeFromCenterline</code> function definition available <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/5f6352986ac511772cd53ad2edb11801da054232/ExtractCenterline/ExtractCenterline.py#L543" rel="noopener nofollow ugc">here</a>.</p>
<p>Could you please let me know this will be made available?</p>

---

## Post #32 by @lassoan (2020-06-25 12:45 UTC)

<p>I would be happy to add this to a Slice module if you can provide me to a Python script that computes it. Could you give it a try? If you are not sure if it is possible then ask it on the VMTK mailing list.</p>

---

## Post #33 by @Deepa (2020-06-25 14:55 UTC)

<p>Could you please have a look at the relevant python script that I have <a href="https://github.com/DeepaMahm/misc/blob/master/network_extraction.py" rel="noopener nofollow ugc">shared on my GitHub account</a> ?</p>
<p>The <a href="https://github.com/DeepaMahm/misc/blob/master/vesseltree.stl" rel="noopener nofollow ugc">input file</a> for running the above script is in stl format.</p>
<p>I worked on this a month back before I got started with Slicer.<br>
I am stuck here – computing the centerlines length / branch length in the network . Some suggestions were offered in <a href="https://mail.google.com/mail/u/0/?tab=rm&amp;ogbl#search/evan/FMfcgxwHMsVGfTPNDjDdffjtNQnSKbkC" rel="noopener nofollow ugc">this discussion</a> on VMTK mailing list.</p>
<blockquote>
<p>You can use vmtkCenterlineAttributes on any centerline object (e,g, the output of vmtkNetworkExtractor).  It will create an array called “Abscissas”.  The Abscissas is the length along each cell/branch.  So the length of the branch will be the abscissas value at the last endpoint of the branch.  See the VMTK tutorial “Geometric Analysis” for more information.</p>
</blockquote>
<p>But I couldn’t find <code>Abscissas</code>  array and got stuck here. Please have a look at the discussion in the above-mentioned thread.</p>
<p>If you could offer advice on how to improve this further I will be super happy to continue from here.</p>

---

## Post #34 by @Deepa (2020-06-26 06:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Could you please have a look at this <a href="https://github.com/DeepaMahm/misc/blob/master/netwrok_extraction2.py" rel="nofollow noopener">updated script</a>?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Updated a nicer version again in the above link <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #35 by @Deepa (2020-06-26 07:14 UTC)

<p>I’d like to ask for suggestions on using the network model generated form slicer as an input instead of the stl input file that’s currently used.</p>
<p>The problem is, currently the networkExtraction algorithm doesn’t work on the stl files that I export from <a href="https://github.com/DeepaMahm/misc/blob/master/Segmentation3_smoothed.seg.nrrd" rel="nofollow noopener">the segment generated</a> in Slicer.</p>

---

## Post #36 by @Deepa (2020-06-26 16:20 UTC)

<p>Please find the corresponding stl file of the large model, for which networkextraction failed in vmtk, available <a href="https://github.com/DeepaMahm/misc/blob/master/segment3.zip" rel="nofollow noopener">here</a></p>

---

## Post #37 by @lassoan (2020-06-27 00:08 UTC)

<p>Network extraction works perfectly using Extract Centerline module for this model (segment3.stl, 264702 points, 529596 cells). Both with preprocessing and without it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7261c3cc86c84a4c6a083b6937a40bfa374d454.png" data-download-href="/uploads/short-url/q8d1JMoBqkyUNKpbbiLRTXTIkcI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7261c3cc86c84a4c6a083b6937a40bfa374d454_2_690x479.png" alt="image" data-base62-sha1="q8d1JMoBqkyUNKpbbiLRTXTIkcI" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7261c3cc86c84a4c6a083b6937a40bfa374d454_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7261c3cc86c84a4c6a083b6937a40bfa374d454_2_1035x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7261c3cc86c84a4c6a083b6937a40bfa374d454.png 2x" data-dominant-color="8788B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1149×798 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve enabled metric computation (radius, curvature, torsion, Frenet-Serret frame, length, and tortuosity) for network extraction result (will be availble in tomorrow’s Slicer Preview Release):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09dd643f8b3ede41d252d602afce6aa080e44aed.png" data-download-href="/uploads/short-url/1pgCQpwsZGIGrgSxcFpOYbkIAIR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09dd643f8b3ede41d252d602afce6aa080e44aed_2_690x420.png" alt="image" data-base62-sha1="1pgCQpwsZGIGrgSxcFpOYbkIAIR" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09dd643f8b3ede41d252d602afce6aa080e44aed_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09dd643f8b3ede41d252d602afce6aa080e44aed_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09dd643f8b3ede41d252d602afce6aa080e44aed_2_1380x840.png 2x" data-dominant-color="C4C7DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 678 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #38 by @Deepa (2020-06-27 01:39 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>. I look forward to use it</p>
<p>Slicer and this forum is simply amazing!</p>

---

## Post #39 by @Deepa (2020-06-27 02:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="37" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve enabled metric computation (radius, curvature, torsion, Frenet-Serret frame, length, and tortuosity) for network extraction result</p>
</blockquote>
</aside>
<p>In addition to these could you please enable startposition and endposition for this network model as well in the quantification results table?</p>

---

## Post #40 by @lassoan (2020-06-27 06:25 UTC)

<p>Adding a quantification table for network extraction would not be hard, but for this to make sense one step is missing: you would need to split curves at branching points:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745af915020505840724c2b53f28461503d21306.png" data-download-href="/uploads/short-url/gBkij2xaLezWzCLf2jvcHUN4ubQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745af915020505840724c2b53f28461503d21306_2_690x405.png" alt="image" data-base62-sha1="gBkij2xaLezWzCLf2jvcHUN4ubQ" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745af915020505840724c2b53f28461503d21306_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/745af915020505840724c2b53f28461503d21306_2_1035x607.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745af915020505840724c2b53f28461503d21306.png 2x" data-dominant-color="6D8BA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×615 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please try to figure this out by playing with the code in Extract Centerline module and/or asking on VMTK mailing list.</p>

---

## Post #41 by @Deepa (2020-06-27 07:06 UTC)

<p>If my understanding is right, in the network model, a segment is the vessel that lies between two junctions or a junction and a free end. So I am not sure why the curves have to be split. Could you please explain why curves have to be split and the downside of not splitting?</p>

---

## Post #42 by @lassoan (2020-06-27 13:54 UTC)

<p>The fact is that in network extraction result, curve segments are not split at branching points. If it is a problem for you (I would guess it is), then you need to split them. VMTK has lots of great tools, so maybe the solution is to simply apply a processing filter.</p>

---

## Post #43 by @Deepa (2020-06-27 14:41 UTC)

<p>When you say,</p>
<aside class="quote no-group" data-username="lassoan" data-post="42" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The fact is that in network extraction result, curve segments are not split at branching points</p>
</blockquote>
</aside>
<p>could you please let me know if you mean curves split like the following?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4f7776296691c756855d6512e52cab1e3364b5e.png" data-download-href="/uploads/short-url/yX4HdfrGLLxAH79v1rl8OzNVhQq.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4f7776296691c756855d6512e52cab1e3364b5e_2_269x250.png" alt="Untitled" data-base62-sha1="yX4HdfrGLLxAH79v1rl8OzNVhQq" width="269" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4f7776296691c756855d6512e52cab1e3364b5e_2_269x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4f7776296691c756855d6512e52cab1e3364b5e_2_403x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4f7776296691c756855d6512e52cab1e3364b5e_2_538x500.png 2x" data-dominant-color="799197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">600×557 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="42" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>maybe the solution is to simply apply a processing filter.</p>
</blockquote>
</aside>
<p>Sorry for the naive question, may I know how the processing filter will be useful here?</p>

---

## Post #44 by @lassoan (2020-06-27 14:54 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="43" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>could you please let me know if you mean curves split like the following?</p>
</blockquote>
</aside>
<p>I mean what I wrote in the picture above "… curve would need to be split here.</p>
<p>Difference between network and branch extraction is a different story. Network can have loops, while I think branch extraction always produces a tree.</p>
<aside class="quote no-group" data-username="Deepa" data-post="43" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>may I know how the processing filter will be useful here</p>
</blockquote>
</aside>
<p>From VMTK documentation, tutorials, source code, and mailing list.</p>

---

## Post #45 by @Deepa (2020-06-27 15:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="44" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I mean what I wrote in the picture above "… curve would need to be split here.</p>
</blockquote>
</aside>
<p>Thanks, I think now I understand what you are pointing to. I got a little confused, sorry.<br>
Could you please explain a bit on how the coloring has been done?</p>

---

## Post #46 by @lassoan (2020-06-27 15:31 UTC)

<p>You can choose which point/cell data array to use for coloring in Models module Scalars section.</p>

---

## Post #47 by @Deepa (2020-06-27 15:57 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>In summary, from what I understand, I think the size of celldata array is not  equal to the number of segments (a segment is the vessel that lies between two junctions or a junction and a free end) in the network. And this is the question that I have raised in vmtk mailing list.</p>
<p>For small model, I could visually check for the number of segments and size of cell array. Both were equal.</p>
<p>I could check the celldata array’s size for the large model but I am not sure how to get the number of segments.</p>

---

## Post #48 by @lassoan (2020-06-27 19:33 UTC)

<p>I’ve checked and tou are right, cells are indeed segments between branching points. So, I can add a quantification result table for them very easily.</p>

---

## Post #49 by @lassoan (2020-06-27 23:53 UTC)

<p>I’ve implemented curve node export and properties computation for extracted networks. It’ll be available in tomorrow’s Slicer Preview Release.</p>

---

## Post #50 by @Deepa (2020-06-28 03:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="48" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve checked and tou are right, cells are indeed segments between branching points</p>
</blockquote>
</aside>
<p>Glad to know that .  I hope the coloring would also work fine now using cell data.</p>
<p>Thanks a lot for your wonderful support.</p>

---

## Post #51 by @lassoan (2020-07-08 04:43 UTC)

<p>A post was merged into an existing topic: <a href="/t/issues-running-latest-preview-on-macos-windows-10/12424/3">Issues running latest preview on macOS/Windows 10</a></p>

---

## Post #52 by @Alice (2020-08-20 02:20 UTC)

<p>I utilized module “VMTK” to compute the centerline of lung airways, which need a long time to run.In addition,the result is not good.The airway tree is out of order and the centerlines line incorrectly.</p>
<p>And I installed other versions,like 4.11.0(2020-06-24) which doesn’t have the function “Centerline Compute”, 4.11.0(2020-05-14) which doesn’t have the option “Curve tree root” and can’t create the airway tree,those versions all can’t draw the tree.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d6d8b380361ecdf36a1448d5a9dca9d7c852cf0.png" data-download-href="/uploads/short-url/hTAnA7JHQTFTwuXY5FbX2quFhT2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d6d8b380361ecdf36a1448d5a9dca9d7c852cf0_2_690x388.png" alt="image" data-base62-sha1="hTAnA7JHQTFTwuXY5FbX2quFhT2" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d6d8b380361ecdf36a1448d5a9dca9d7c852cf0_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d6d8b380361ecdf36a1448d5a9dca9d7c852cf0_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d6d8b380361ecdf36a1448d5a9dca9d7c852cf0_2_1380x776.png 2x" data-dominant-color="BABBDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #53 by @lassoan (2020-08-20 02:23 UTC)

<p>In recent Slicer-4.11 version we hugely improved the module and renamed to “Extract centerline” to make it more consistent with module naming conventions. It has built-in automatic decimation to make centerline extraction 10x-100x faster without impacting accuracy, can work directly with segmentation input, export curves, compute statistics, etc.</p>

---

## Post #54 by @Alice (2020-08-20 03:38 UTC)

<p>I just installed the version 4.11.0(2020-08-18),but it doesn’t have the module “centerline compute”, so how can I get the centerline?</p>

---

## Post #55 by @lassoan (2020-08-20 03:38 UTC)

<p>In recent Slicer-4.11 version we hugely improved the module and renamed to “Extract centerline” to make it more consistent with module naming conventions.</p>

---

## Post #56 by @Alice (2020-08-20 07:58 UTC)

<p>Sorry，I am new here.I clicked the “Apply”,but it seemed that nothing has happened.I can’t find the centerline in the module “Data”,and the “Table_1” is empty,as well as “PlotSeries_1”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e814aa13b30289171adff30ddc78fe164cf0f9ba.jpeg" data-download-href="/uploads/short-url/x752S7CuRYlQX9RNEe00hldeiuK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e814aa13b30289171adff30ddc78fe164cf0f9ba_2_690x388.jpeg" alt="image" data-base62-sha1="x752S7CuRYlQX9RNEe00hldeiuK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e814aa13b30289171adff30ddc78fe164cf0f9ba_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e814aa13b30289171adff30ddc78fe164cf0f9ba_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e814aa13b30289171adff30ddc78fe164cf0f9ba_2_1380x776.jpeg 2x" data-dominant-color="CCCBCD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #57 by @Alice (2020-08-20 08:07 UTC)

<p>And what confused me is that the input of the module “centerline metrics” is “centerline”,but my purpose is to compute the centerline,which is really strange.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3056d7b62993ddbfeb27f32cbb7908a4e4a0f680.png" data-download-href="/uploads/short-url/6TCYDBfQatz3aNv0BiSF4MRb5cc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3056d7b62993ddbfeb27f32cbb7908a4e4a0f680.png" alt="image" data-base62-sha1="6TCYDBfQatz3aNv0BiSF4MRb5cc" width="654" height="500" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×505 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #58 by @cpinter (2020-08-20 08:54 UTC)

<p>From your screenshot is seems possible to me that you created an empty model node called Model_1 and did the processing on that. If so, then it’s no surprise that the output is empty. Choose “Airway Label” instead.</p>

---

## Post #59 by @chir.set (2020-08-20 09:10 UTC)

<aside class="quote no-group" data-username="Alice" data-post="57" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/779978/48.png" class="avatar"> Alice:</div>
<blockquote>
<p>my purpose is to compute the centerline</p>
</blockquote>
</aside>
<p>Use ‘Extract centerline’ to compute a centerline.</p>
<p>‘Centerline metrics’ is meant to plot the diameter distribution around an existing centerline.</p>

---

## Post #60 by @Alice (2020-08-20 10:27 UTC)

<p>Thank you! I have ran the ‘Extract centerline’ following the video on Youtube.But there is nothing in the result ‘Centerline curve’ .<br>
Do you know why?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3826cbdf2042810adf9457632265595074f668a4.png" data-download-href="/uploads/short-url/80JRgJshOzIvqg2Wu9RdQKxMJzC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3826cbdf2042810adf9457632265595074f668a4_2_690x318.png" alt="image" data-base62-sha1="80JRgJshOzIvqg2Wu9RdQKxMJzC" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3826cbdf2042810adf9457632265595074f668a4_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3826cbdf2042810adf9457632265595074f668a4_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3826cbdf2042810adf9457632265595074f668a4.png 2x" data-dominant-color="C1C4DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1363×629 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #61 by @chir.set (2020-08-20 11:17 UTC)

<p>You’d be better off by manually placing the endpoints; avoid the furthest extreme points; and results are more predictable if you avoid extracting bifurcated centerlines.</p>

---

## Post #62 by @Alice (2020-08-20 11:59 UTC)

<p>Thank you! I have solved it,and I have a new question which is that I want to save the ‘centerline curve’ and the ‘Centerline quantification’,so how to achieve that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e1ef2b4b72b48dbc0eb9701adb1a88f04dbbf2a.png" data-download-href="/uploads/short-url/4isD3TZIzIpyZDG6qQYxjIVa64q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e1ef2b4b72b48dbc0eb9701adb1a88f04dbbf2a_2_690x388.png" alt="image" data-base62-sha1="4isD3TZIzIpyZDG6qQYxjIVa64q" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e1ef2b4b72b48dbc0eb9701adb1a88f04dbbf2a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e1ef2b4b72b48dbc0eb9701adb1a88f04dbbf2a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e1ef2b4b72b48dbc0eb9701adb1a88f04dbbf2a_2_1380x776.png 2x" data-dominant-color="D0D1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×900 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #63 by @chir.set (2020-08-20 12:21 UTC)

<aside class="quote no-group" data-username="Alice" data-post="62" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/779978/48.png" class="avatar"> Alice:</div>
<blockquote>
<p>I want to save</p>
</blockquote>
</aside>
<p>Doesn’t File/Save offer to save anything ?</p>

---

## Post #64 by @Alice (2020-08-20 12:31 UTC)

<p>Oh,you are right!  I’m already confused by the software.Thank you very much!</p>

---

## Post #65 by @lassoan (2020-08-20 13:52 UTC)

<aside class="quote no-group" data-username="Alice" data-post="64" data-topic="12054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/779978/48.png" class="avatar"> Alice:</div>
<blockquote>
<p>I’m already confused by the software.</p>
</blockquote>
</aside>
<p>That’s why we are here to help. Let us know if you have any suggestions for making the software simpler or more intuitive.</p>

---
