# DBS electrode reconstruction

**Topic ID**: 1872
**Date**: 2018-01-19
**URL**: https://discourse.slicer.org/t/dbs-electrode-reconstruction/1872

---

## Post #1 by @Vinny (2018-01-19 02:24 UTC)

<p>Hi,</p>
<p>I’m interested in DBS electrode reconstruction and was wondering if there was a way to do this in 3D Slicer.  I’ve used the Editor and Model Maker modules to segment out the DBS leads.  I am now trying to figure out the contact positions for each lead.  I understand that the PaCER method in Matlab is able to model the center-line for each lead and subsequently obtain a lead skeleton and derive the contact coordinates.  After seeing this discussion,  I ran the ‘Extract Skeleton’ module on one of the segmented leads using 1000 points and a 2D skeleton type; the points can be clearly seen within the leads.  I installed the SlicerVMTK module to compute the center-line but having trouble using the Input function, i.e., I cannot load anything.  A,so, if there is an easier way to do DBS electrode reconstruction in 3D Slicer, that would be great to know.  Thanks for your help.</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2018-01-19 17:45 UTC)

<p>Pierre Jannin’s group in Rennes developed a nice system for DBS planning and guidance based on Slicer and PyDBS. You can download an overview paper from <a href="https://www.researchgate.net/publication/262075665_PyDBS_an_automated_image_processing_workflow_for_deep_brain_stimulation_surgery">here</a>. Maybe <a class="mention" href="/u/mholden8">@mholden8</a> can give you more details or can help you get in contact with them.</p>
<p>If you only need DBS lead segmentation, then I think Segment Editor’s <code>Grow from seeds</code> effect could work very well. You may need to crop and resample the volume using Crop volume module (to have high, anisotropic resolution so that region growing can follow the leads more robustly). You should be able to segment multiple leads at once, specifying one small seed segment for each, and a larger seed for “other”.</p>
<aside class="quote no-group" data-username="Vinny" data-post="1" data-topic="1872">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vinny/48/7052_2.png" class="avatar"> Vinny:</div>
<blockquote>
<p>having trouble using the Input function, i.e., I cannot load anything</p>
</blockquote>
</aside>
<p>I would be happy to help with this, too, but of course I need much more accurate description of what you did, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @Vinny (2018-01-20 01:01 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for your reply.  I’ll go through the PyDBS paper and<br>
will contact <a class="mention" href="/u/mholden8">@mholden8</a> for further details on PyDBS.  I<br>
have been manually segmenting the electrodes using the Threshold Effect in<br>
the Editor Module and removing any artifact (surgical staples, etc…)<br>
prior to using the Model Maker module and saving the output in both NIFTI<br>
and VTK formats.  I’m establishing a tractography workflow and imported the<br>
white matter tracts into 3d Slicer and converted to VTK.  I’d like to be<br>
able to quantify distances between white matter tracts of interest and the<br>
electrode contacts in 3d Slicer.  So, my goal is to determine the contact<br>
coordinates on the segmented lead.</p>
<p>I was thinking that computing a center-line through the segmented lead and<br>
deriving a polynomial expression may help with determining the coordinates<br>
of the four contacts. Alternatively, I’ve used PaCER to derive the lead<br>
skeleton and the xyz contact coordinates and saved them as an excel file.<br>
I’m certain that Slicer has a method of plotting these contact coordinates<br>
onto the segmented lead.  Maybe I can start with this and see what I get.<br>
Will the Python Interactor help with this or is there an established module<br>
that I could use for plotting these coordinates onto the image?</p>
<p>Regards,</p>
<p>Vinny</p>

---

## Post #4 by @lassoan (2018-01-22 19:38 UTC)

<p>I’ve updated <code>‘Extract Skeleton</code> module to be able to export centerline points to markups fiducial list node (and improved point computation accuracy). It will be available in tomorrow’s nightly build.</p>
<p>Once you have your centerline points in markups node, then you can use <code>Markups To Model</code> module (available in MarkupsToModel extension) to create a trajectory model using spline or polygonal line fitting.</p>

---

## Post #5 by @Vinny (2018-01-22 19:54 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for the update!  I look forward to testing this out<br>
soon.</p>
<p>Regards,</p>
<p>Vinny</p>

---

## Post #6 by @Vinny (2018-01-24 02:17 UTC)

<p>Hi Andras,</p>
<p>Thanks, the trajectory model works great.  Is there a way of getting the equation of the calculated trajectory model?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51356c6f351c2fc19197ca446be1e5edfb1cd7db.png" data-download-href="/uploads/short-url/bAp8lku2RfBy6dRqjdLyuKk5Gun.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51356c6f351c2fc19197ca446be1e5edfb1cd7db_2_690x369.png" alt="image" data-base62-sha1="bAp8lku2RfBy6dRqjdLyuKk5Gun" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51356c6f351c2fc19197ca446be1e5edfb1cd7db_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51356c6f351c2fc19197ca446be1e5edfb1cd7db_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51356c6f351c2fc19197ca446be1e5edfb1cd7db_2_1380x738.png 2x" data-dominant-color="C3C4E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1028 78.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-01-24 04:23 UTC)

<p>You cannot get the trajectory model, but you can get the curve point at any resolution (by setting high value for “segments per point”). I’ve also updated the module so that when you specify 0 for radius then instead of a tube model, a simple polyline model is generated.</p>
<p>You can get points of the line in the output model as a numpy array like this:</p>
<pre><code>curveModelNode = slicer.util.getNode('MarkupsToModelModel')
points = slicer.util.arrayFromModelPoints(curveModelNode)</code></pre>

---

## Post #8 by @mholden8 (2018-01-25 13:39 UTC)

<p><a class="mention" href="/u/vinny">@Vinny</a>, I just spoke directly to Dr. Pierre Jannin about this. He says he would be happy to chat with you about using PyDBS for DBS electrode reconstruction. He asks you to contact him directly. Please find his contact info here: <a href="https://medicis.univ-rennes1.fr/members/pierre.jannin/index" rel="nofollow noopener">https://medicis.univ-rennes1.fr/members/pierre.jannin/index</a>.</p>

---

## Post #9 by @Vinny (2018-01-25 17:19 UTC)

<p><a class="mention" href="/u/mholden8">@mholden8</a>, thank you very much for speaking to Dr. Jannin about this and providing me his contact information.  <a class="mention" href="/u/lassoan">@lassoan</a>: thanks for all your help so far.</p>

---

## Post #10 by @shwetasked (2025-09-14 07:48 UTC)

<p>Hi Vinny,</p>
<p>Came across your thread from, oh 7 years ago now! I was wondering how your DBS electrode reconstruction went, were you able to do it using 3D Slicer and the PaCER toolbox? I’m embarking on a similar project myself, with the goal of making models of reconstructed DBS electrodes on a patient’s brain accessible for their viewing and understanding, and also for researchers and clinicians to be able to represent these figures accurately in their publications!</p>

---
