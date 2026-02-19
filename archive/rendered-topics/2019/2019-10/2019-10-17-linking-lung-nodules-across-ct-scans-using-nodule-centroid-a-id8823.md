---
topic_id: 8823
title: "Linking Lung Nodules Across Ct Scans Using Nodule Centroid A"
date: 2019-10-17
url: https://discourse.slicer.org/t/8823
---

# Linking lung nodules across CT scans using nodule centroid anatomical coordinates

**Topic ID**: 8823
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/linking-lung-nodules-across-ct-scans-using-nodule-centroid-anatomical-coordinates/8823

---

## Post #1 by @matt-warkentin (2019-10-17 21:36 UTC)

<p>Hi,</p>
<p>Here is the setup for my question: I have lung CT scans from multiple time points for multiple patients. Our team’s radiologist is using <code>Slicer</code> to perform semi-automated contouring of lung nodules. In addition, he is saving/recording the <code>[xyz]</code> coordinates of the nodule centroid in anatomical space. Each nodule identified in the CT scans has an ID number. Unfortunately, the nodule IDs are not consistent across scans. The IDs are assigned in order the nodule was observed, and so lesion <code>#1</code> on one scan might be lesion <code>#2</code> on another scan, even if they are the same lesion.</p>
<p>So, of course we can have the radiologist manually review scans to determine which lesions IDs are actually the same lesions across scans. But this is prohibitively slow to do. I thought I should be able to use the nodule centroid anatomical coordinates to link lesions across scans. So we looked at the data for two scans for two lesions we know are the same, and yet the anatomical <code>[xyz]</code> differed substantially. We realized the origins differ, and these numbers are relative to the origin.</p>
<p>So I extracted the image origin coordinates from DICOM header using <code>Slicer</code>, and then calculated the nodules “distance from origin” using the origin and centroid coordinates. For example:</p>
<p><strong>First scan:</strong> centroid<code> [126.3, -38.5, -166.7]</code>; image origin <code>[185.2, 180.0, -347.7]</code><br>
<strong>Second scan:</strong> centroid <code>[121.4, 103.2, -215.9]</code>; image origin <code>[180.6, 316.6, -382.2]</code></p>
<p>Subtracting the nodule coordinate from the origin coordinate, we get the “distance from origin”:<br>
<strong>First scan:</strong> <code>[58.9, 218.5, -181.0]</code><br>
<strong>Second scan:</strong> <code>[59.2, 213.5, -166.3]</code></p>
<p>These numbers are fairly close, which suggested to me I was on the right track. I would expect these numbers to be identical ONLY if the fiducial for the centroid was placed in the EXACT same physical location across scans, right? Does anyone have any thoughts on whether this approach could be used to “link” nodules from different scans?</p>

---

## Post #2 by @pieper (2019-10-17 21:59 UTC)

<p>Did you have a look at registration options?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Registration/RegistrationLibrary</a></p>
<p>It can be tough to line up cases exactly, but should be possible to reasonable results for your use case.  Have a look at the pet/ct longitudinal example.</p>

---

## Post #3 by @matt-warkentin (2019-10-17 22:18 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thanks for the response. I did momentarily think about registration, but to be honest, I wasn’t sure if registration would be helpful retroactively. The (perhaps) problem is that we already have the centroid coordinates for thousands of nodules, and we know that most of the nodules appearing on follow-up scans are present on previous scans, without a concrete way of linking them. I am trying to think of the most robust and least manual way of using any/all available information to connect nodules across scans.</p>
<p>Would after-the-fact registration help in this respect?</p>

---

## Post #4 by @muratmaga (2019-10-17 22:40 UTC)

<p>Registration is probably the most automated option. You can register the follow up scans of your patient to their initial scan, convert your centroids into a multi-label labelmap, and apply the resultant transformation from your registraiton to those binary maps. This will bring everything into patient’s initial scans coordinate system. There you can do quite a bit of stuff (intersection, finding the closest point, changing ids etc).</p>

---

## Post #5 by @matt-warkentin (2019-10-17 22:47 UTC)

<p>This does sound like a promising option. I am definitely going to look into this approach further.</p>
<p>Do you have any resources you could point me towards to learn more about how to actually achieve all of this in <code>Slicer</code> in a non-GUI manner?</p>

---

## Post #6 by @muratmaga (2019-10-17 23:11 UTC)

<p>I am sure there is with some python code, others might give you better pointers. I usually do this in R with ANTsR.</p>

---

## Post #7 by @lassoan (2019-10-17 23:41 UTC)

<p>Origin is usually chosen by the imaging tech based on the scout scans. If your imaging protocol specifies where to place the origin then you can expect that anatomical coordinates (LPS) to be fairly consistent. If they don’t pay attention to the origin placement but the size and position of the anatomical region is consistent between the scans then subtracting the centroid would probably somewhat consistent, too (within a couple of centimeters).</p>
<p>This is a relatively easy image registration task (same imaging modality, same imaging protocol, same patient, same patient orientation), so any registration toolkit should work well. Slicer provides graphical user interface for Elastix and BRAINSFit. I would expect that Elastix will work well with the default parameter settings, BRAINSFit probably requires some parameter tuning.</p>

---

## Post #8 by @matt-warkentin (2019-10-17 23:51 UTC)

<p>Thanks for the insight. I will look into <code>Elastix</code> to learn more about it. Can image registration with <code>Elastix</code> be codified (i.e. automated) for hundreds to thousands of registrations? Or is the <code>Slicer</code> GUI the only approach?</p>
<p>As a follow-up, I get the logic behind registering two CTs in order to align them anatomically, but how exactly does this registration translate into me being able to take existing sets of nodule centroid coordinates and aligning <em><strong>them</strong></em> anatomically. I think I am conceptually missing the connection.</p>

---

## Post #9 by @matt-warkentin (2019-10-17 23:52 UTC)

<p>Thanks for bringing this package to my attention. I am very comfortable using <code>R</code>, so I am happy to find out a package may exist to solve this problem.</p>

---

## Post #10 by @muratmaga (2019-10-18 00:02 UTC)

<p>I thought your challenge is not aligning, but making sure the labels of nodules are consistent across scans? I would probably try something along the lines where you take the centroid (a point), convert them into small spheres (may be 5mm depends on the size of the nodules, I guess). So from the registered scans, anyone that intersects a sphere with the first scan, you relabel the others.</p>
<p>So if nodule2 from scan2 and nodule4 from scan 3 intersect with nodule10 from original scan, you relabel the others as nodule10, or make some sort of a table matrix of correspondences.</p>
<p>Or you can calculate distances of new centroid coordinates from aligned scans to the reference scan, and pick the label of the one that it is closest to…</p>
<p>Isn’t that’s what you are trying to solve? If not, apologies I got your question completely wrong…</p>

---

## Post #11 by @matt-warkentin (2019-10-18 14:39 UTC)

<p>No, I think you are understanding my issues rather well from my limited description. Indeed, we have a dataset whereby we have nodules that are identified at baseline and  their ID is assigned starting at 1 and incremented by 1 for each subsequent finding. The same ID’ing and incrementing strategy is using for the second and third follow ups, but without consideration for previous scans. We <em><strong>do</strong></em> have a variable in our data that indicates whether a nodule on follow-up scans was pre-existing on the previous scan(s), however, since the ID assignment is based on whatever nodule the radiologist identified first, second, third, etc., the IDs are not consistent across scans, even for the same nodule.</p>
<p>So your suggestion to create a sphere around the nodules (perhaps with the size of the sphere dependent on the nodule size), and then look for intersection of spheres to determine if they are the same nodules could indeed work. But this approach would similarly require registration, or am I misinterpreting?</p>
<blockquote>
<p>Or you can calculate distances of new centroid coordinates from aligned scans to the reference scan, and pick the label of the one that it is closest to…</p>
</blockquote>
<p>Yes, I guess this was sorta my initial line of thinking. If the follow-up CTs were registered to the baseline scan, and we compared new nodule coordinates to the baseline nodule coordinates, we could do some sort of fuzzy matching to assign baseline labels to follow-up nodules.</p>

---

## Post #12 by @lassoan (2019-10-18 15:41 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="11" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>we could do some sort of fuzzy matching to assign baseline labels to follow-up nodules</p>
</blockquote>
</aside>
<p>This fuzzy matching and alignment of points is implemented in SlicerIGT extension’s Fiducial registration wizard module. You need to provide the input as two markup fiducial lists (one point at each centroid), which can be implemented in a couple of lines of Python code (but for initial testing you can do it manually). If you enable point matching option in Fiducial registration wizard then number and order of input points do not need to match: the module performs an exhaustive search for the best match and gives you the transform between the two point sets. After you apply this alignment transform, the point coordinates should be quite close, so it should be easy to do the relabeling.</p>

---

## Post #13 by @matt-warkentin (2019-10-18 16:05 UTC)

<p>Thanks again for the great suggestion, <a class="mention" href="/u/lassoan">@lassoan</a>. This sounds like it could be a  good solution to my problem. I will test drive this option and report back with my experiences.</p>

---

## Post #14 by @matt-warkentin (2019-10-18 16:41 UTC)

<p>So I have added the <code>SlicerIGT</code> extension and tried to play around with the <code>Fiducial Registration Wizard</code>, but I am unclear on a few things.</p>
<ol>
<li>
<p>I am getting a status/warning that <code>Status: 'From' fiducial list has too few fiducials (minimum 3 required).</code> I am unclear why this restriction is in place.</p>
</li>
<li>
<p>I am unclear how this module could possibly spatially align two fiducials/coordinates without knowing the geometry of the CT scans from which they were derived. I have all of the CT scans in <code>DICOM</code> and <code>NRRD</code> format, shouldn’t I be using this information somewhere to help with the fiducial alignment?</p>
</li>
</ol>
<p>For all of the work we have been doing in <code>Slicer</code>, we have been saving the fiducial file (<code>.fcsv)</code> for the centroids, so I have those data handy. Anyway, for a test case, I have selected the fiducials for a nodule I <strong>know</strong> is the same nodule on two different scans. The fiducial on baseline scan is <code>[126.3, -38.5, -166.7]</code>, and for the 1-year follow-up scan is <code>[121.4, 103.2, -215.9]</code>. As you mentioned before, same imaging modality, protocol, patient, orientation, but it just so happens that for this specific case they are using different vendors (GE vs. Siemens, if that matters). How would it be possible to determine if these fiducials are spatially aligned without considering image geometry? Or am I misinterpreting how the <code>Fiducial Registration Wizard</code> works?</p>
<p>Sorry for my confusion, I really appreciate everyone’s help.</p>

---

## Post #15 by @lassoan (2019-10-18 17:37 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="14" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>How would it be possible to determine if these fiducials are spatially aligned without considering image geometry?</p>
</blockquote>
</aside>
<p>If you have at least 3 points (that are not arranged in a symmetric pattern) then only one transform exists that aligns them. Fiducial registration wizard displays a warning if multiple similarly good alignments exist due to symmetry in the point pattern.</p>

---

## Post #16 by @matt-warkentin (2019-10-21 14:03 UTC)

<p>Upon second thought, this method doesn’t appear to be able to solve my problem, correct? I only have a single point for each nodule (i.e. the centroid). Is image registration the only viable approach?</p>

---

## Post #17 by @lassoan (2019-10-22 12:59 UTC)

<p>Yes, if completely different nodules may be found on different images (e.g., one found on each image and they are not the same) then your only choice is to register the images. If they are close enough to each other you could assume that they are the same.</p>

---

## Post #18 by @matt-warkentin (2019-10-22 14:26 UTC)

<p>Thanks for confirming.</p>
<p>I have just ran the image registration using the <code>Elastix</code> extension in <code>Slicer</code>. It was very user-friendly. I set the baseline CT as the <code>fixed volume</code>, and the 1-year follow-up CT as the <code>moving volume</code>; I used the <code>generic (all)</code> preset (please let me know if you think another preset might be preferred for lung CTs).</p>
<p>I see that it produced two outputs, <code>Volume.nrrd</code> which I presume is the follow-up CT registered to the baseline geometry, and <code>Transform.h5</code> which I’m guessing describes the transformation for resgitering the moving volume to the fixed volume. Am I now able to apply that transformation to the nodule coordinates? Any suggestions on how to do this next step?</p>
<p>For all the nodules in both scans for this patient, I have the nodule centroid coordinates saved in <code>.fcsv</code> files, and I also have binary segmentation masks in <code>.nrrd</code> files.</p>

---

## Post #19 by @lassoan (2019-10-22 14:40 UTC)

<p>You can apply the computed transform to the point position in the coordinate system of the other image.</p>

---

## Post #20 by @matt-warkentin (2019-10-22 14:52 UTC)

<p>Does <code>Slicer</code> offer this functionality? I am not sure how to do this. Sorry for the helplessness, this is all fairly new to me.</p>
<p>Not to further complicate things, but when I was writing out my last comment, it struck me that it might be better to transform the binary masks than the centroid coordinates, do you agree? Thinking back to <a class="mention" href="/u/muratmaga">@muratmaga</a>’s suggestion to form spheres around the centroid and check for intersection, couldn’t the binary mask be viewed as a (deformed) sphere around the centroid?</p>
<p>Would it be more reliable to see how much voxel intersection there is between the original mask and the transformed mask, rather than fuzzy matching the transformed centroid coordinate?</p>

---

## Post #21 by @muratmaga (2019-10-22 20:16 UTC)

<p>This is a longer explanation of what Andras already said.</p>
<p>Download MRBrainTumor1 and 2 from sample data. Create a Fiducial (markup) on the edge of the left ventricle of the Tumor2. Note point is not on the edge of the ventricle in Tumor1 dataset.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca3170b3cefc6fdee255ddba331b08e661a8f48a.png" alt="image" data-base62-sha1="sQGncFE0vAOI7xhQXHJbBrIuJnk" width="227" height="172"></p>
<p>Switch to General Registration(Brains) module. Set Tumor1 as fixed, Tumor2 as moving. Choose  all registration options including bspline. Expand <strong>Expert Only Parameters</strong> and create an Output Transform. This helps you concatenate the linear and non-linear portions of the transformation into a single transform that you can apply to markups and volumes.</p>
<p>When you execute this flow, Tumor2 will be put under the Output Transform but not the point. If you add the F to the output transform you can now see it lining up on the edge of the ventricle for both Tumor1 and Tumor2.</p>
<p>I am sure you can do all this with Elastix as well, I am not very familiar with it.</p>

---

## Post #22 by @lassoan (2019-10-22 20:46 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="20" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>Would it be more reliable to see how much voxel intersection there is between the original mask and the transformed mask, rather than fuzzy matching the transformed centroid coordinate?</p>
</blockquote>
</aside>
<p>You can transform volumes, markup fiducial points, segmentations, models, etc. the same way, using Transforms module (see documentation and/or demo video at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" class="inline-onebox">Documentation/Nightly/Modules/Transforms - Slicer Wiki</a>) or using Data module (double-click on the transform column in the row of the node that you would like to transform).</p>
<p>Once you have the aligned segmentations, you can use “Segment editor” module’s “Logical operators” effect to compute intersection of each segment pairs and then use “Segment statistics” module to get the volumes of the intersecting regions. This is of course very tedious to do manually (using the GUI), so if you confirmed that everything works well then it is worth writing a short Python script to automate it. There are many code snippets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">script repository</a> that you can combine/modify to get what you need.</p>

---

## Post #23 by @matt-warkentin (2019-10-23 15:04 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a>. This is very helpful.</p>
<p>I think I am very close to getting my test example to work using the GUI. I am stuck on getting the intersection of the transformed binary mask and the baseline/fixed mask. I used the <code>Elastix</code> extension to get the transformation of the follow-up scan to the baseline geometry. Then I applied the transformation to the binary mask in the <code>Data</code> module as you described. Upon visual inspection, I can now see the two masks are closely aligned.</p>
<p>Using the <code>Segment Editor</code> I then <code>Create new Segmentation</code>. Then using the <code>Master volume:</code> option I <code>Add</code> both of the masks. I then selected <code>Logical operators</code> and the <code>intersect</code> operation. In the upper box I selected one mask, and in the lower box (<code>Intersect with segmet:</code>) I selected the second mask and hit apply. However, nothing seems to happen, and <code>Segment Statistics</code> produces an empty table for the resulting segmentation. Am I using the logical operators wrong? It feels like it.</p>

---

## Post #24 by @lassoan (2019-10-23 17:33 UTC)

<p>You need to <em>harden the transform</em> on the segmentation to apply the transform permanently (even if you copy/move segments to another segmentation).</p>
<p>When you apply intersection operation do you see that the non-overlapping part of the segment disappears?</p>

---

## Post #25 by @matt-warkentin (2019-10-23 20:45 UTC)

<p>So I was eventually able to get it working. I had to harden the transform, as you mentioned. The other issue was that I was loading in the binary label maps (<code>.nrrd</code> files) as volumes (and selecting the <code>LabelMap</code> option). Once I changed the <code>Description</code> to <code>Segmentation</code>, I was able to intersect the two nodules and use the <code>Segment Statistics</code> module to generate volume statistics.</p>
<p>I don’t think I’m entirely clear on whether I should load binary label maps as <code>Volumes</code> with the <code>LabelMap</code> or whether they should be loaded as <code>Segmentations</code>.</p>
<p>The overlap fraction (<code>intersection volume / min(nodule1_volume, nodule2_volume) * 100</code>) was rather low (~8%). This, of course, could be the result of two segmentation masks that do not overlap much, but could some of this be attributable to poor CT registration?</p>

---

## Post #26 by @lassoan (2019-10-23 22:08 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="25" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>I was eventually able to get it working</p>
</blockquote>
</aside>
<p>Awesome.</p>
<aside class="quote no-group" data-username="matt-warkentin" data-post="25" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>whether I should load binary label maps as <code>Volumes</code> with the <code>LabelMap</code> or whether they should be loaded as <code>Segmentations</code> .</p>
</blockquote>
</aside>
<p>If you use Segment Editor module to process these images then it makes sense to load them as segmentation nodes directly.</p>
<aside class="quote no-group" data-username="matt-warkentin" data-post="25" data-topic="8823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>could be the result of two segmentation masks that do not overlap much, but could some of this be attributable to poor CT registration?</p>
</blockquote>
</aside>
<p>You can fade between the registered CT volumes to verify how well they are aligned.</p>
<p>If you find that overlap volume is not a sensitive enough metric then you can also compute average distance from each segment. To do this, export one segment to a labelmap and use Simple Filters module to generate distance map image. Then use Seent statistics module with the distance map as input scalar volume to get average distance. You may also use Segment Comparison module to compute overlap and diatance between segments.</p>

---

## Post #27 by @matt-warkentin (2019-10-24 19:34 UTC)

<p>So I think I was able to follow your instructions to compute the average distance metric.</p>
<ol>
<li>
<p>I imported one binary label map as a label map; and imported one binary label map as a segmentation node (I hardened the transform to this segmentation).</p>
</li>
<li>
<p>I used the <code>Simple Filters</code> module and chose the filter <code>ApproximateSignedDistanceMapImageFilter</code> and selected the label map as the input volume. I created a new output volume for this distance map.</p>
</li>
<li>
<p>I then used the <code>Segment Statistics</code> module with the segmentation node as the <code>Segmentation</code>, and the distance map as the <code>Scalar volume</code>. I was able to produce a table with several statistics including a <code>Mean</code> of 1.74.</p>
</li>
</ol>
<p>I am not entirely sure on how to interpret this number in absolute terms, but I have to think smaller numbers indicate shorter distances, and vice versa.</p>
<ol start="4">
<li>Lastly, I went back a re-imported the first binary label map as a segmentation node directly. I then used the <code>Segment Comparison</code> module to compare the nodes. I obtained some Hausdorff distance metrics (<code>Max: 3.6, Min: 1.9, 95% 3.1</code>) and Dice similarity metrics (e.g. <code>Coef: 0.067, Ref center: (126,-38,-167), Compare center: (127,-35,-167), Ref volume: 0.06, Compare volume: 0.05</code>).</li>
</ol>
<p>I suppose I could use any number of metrics to make a determination on whether they are the “same” nodule.</p>
<p>Sorry for the long write-up. I am partly documenting my steps for my own sake, but also in case this is useful for anyone who stumbles upon this thread in the future.</p>

---
