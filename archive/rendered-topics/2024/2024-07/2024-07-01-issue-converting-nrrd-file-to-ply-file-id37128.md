# Issue converting NRRD file to PLY file

**Topic ID**: 37128
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/issue-converting-nrrd-file-to-ply-file/37128

---

## Post #1 by @mtyack (2024-07-01 19:25 UTC)

<p>Hello,</p>
<p>I am having a new issue when converting and opening saved files and hoping for some troubleshooting advice.</p>
<p>In the past, I have segmented out heads and jaws within one large file, and saved them individually from the large file as a model as a PLY file and they are able to be visualized as a smooth looking surface. Now I have recently been creating separate files by creating individual volumes for each fish head and saving them as NRRD files. I then have been segmenting out the jaws from the NRRD files and saving them as PLY files. When this is done, the PLY files looks textured with a stripped pattern.</p>
<p>Photo of how the converted NRRD to PLY looks in slicer → <a href="https://file.io/ddfdQdOHlFkT" rel="noopener nofollow ugc">https://file.io/ddfdQdOHlFkT</a></p>
<p>I was wondering if anyone had any idea what upload settings could be adjusted to fix this new issue. I have uploaded two files below, one is the technique that I was doing that yielded smooth models and the new “textured looking” models.</p>
<p>Old PLY file that appears smooth → <a href="https://file.io/rXMEdVTCM9ST" rel="noopener nofollow ugc">https://file.io/rXMEdVTCM9ST</a><br>
New PLY file that appears textured from NRRD → <a href="https://file.io/V2xMXnayjsZs" rel="noopener nofollow ugc">https://file.io/V2xMXnayjsZs</a></p>
<p>Thanks for the help!</p>

---

## Post #2 by @Dave_Matthews (2024-07-09 16:05 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Just wondering if you have any ideas about what’s happening here? I imagine it’s something simple, but we’re pretty confused!</p>
<p>Thanks!<br>
Dave</p>

---

## Post #3 by @mtyack (2024-07-09 16:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/def74cb5f5f2e6d105786752d5195ec461be01d4.jpeg" data-download-href="/uploads/short-url/vOrPNEUyMjh3m5Ftpq0KXh8kFQo.jpeg?dl=1" title="Screenshot 2024-07-01 141412" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def74cb5f5f2e6d105786752d5195ec461be01d4_2_605x500.jpeg" alt="Screenshot 2024-07-01 141412" data-base62-sha1="vOrPNEUyMjh3m5Ftpq0KXh8kFQo" width="605" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def74cb5f5f2e6d105786752d5195ec461be01d4_2_605x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def74cb5f5f2e6d105786752d5195ec461be01d4_2_907x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/def74cb5f5f2e6d105786752d5195ec461be01d4_2_1210x1000.jpeg 2x" data-dominant-color="9E9FAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-01 141412</span><span class="informations">1306×1079 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here is an image of what converted NRRD to PLY files looks like.</p>

---

## Post #4 by @muratmaga (2024-07-09 16:37 UTC)

<p>With this much information it is hard to tell what might be the issue? Did you change Slicer versions between these? If you did, and when you try to process the old data with new Slicer are you still getting these wave effects? What are the versions of Slicer you are using?</p>
<p>I am trying to understand whether that’s a workflow/data issue (that you have changed something on your end), or Slicer issue…</p>

---

## Post #5 by @lassoan (2024-07-09 18:31 UTC)

<p>You see the woodgrain pattern, because rendering of shadows is enabled (that was a feature introduced recently) and size scale is set so that the slight waves of the surface are emphasized. You can turn off shadows display or change size scale in the view controller (appears when you click the pushpin icon). You turn it off by default in Application settings / Views.</p>
<p>You can also tune steength of surface smoothing in the dropdown menu of the <code>Show 3D</code> button.</p>

---

## Post #6 by @Dave_Matthews (2024-07-09 20:31 UTC)

<p>Thanks for the help!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, I don’t think it’s a problem with the rendering in Slicer because we get similar results if we load the files into MeshLab (new method on the left, old method on the right):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbc3ee472faa84b4598ff09f6db190b3c0faa443.jpeg" data-download-href="/uploads/short-url/vm8lr9RVQ7Ae99TObh1g0hah9lh.jpeg?dl=1" title="Screenshot 2024-07-09 152114" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbc3ee472faa84b4598ff09f6db190b3c0faa443_2_690x374.jpeg" alt="Screenshot 2024-07-09 152114" data-base62-sha1="vm8lr9RVQ7Ae99TObh1g0hah9lh" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbc3ee472faa84b4598ff09f6db190b3c0faa443_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbc3ee472faa84b4598ff09f6db190b3c0faa443_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbc3ee472faa84b4598ff09f6db190b3c0faa443_2_1380x748.jpeg 2x" data-dominant-color="69668D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-09 152114</span><span class="informations">1920×1043 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One thing that I did notice in MeshLab is that the <strong>old models (normal) are solid while the new ones (bad rendering) are hollow</strong>. I don’t think we changed anything about our exporting process that would cause this, but you can see out methods in more details below.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, That’s a good point, we did change Slicer versions. The ones that come out strangely are done on 5.6.2. The old ones are from 5.2 (I’m not sure which sub-version). When I load an old file (initially imported and segmented in 5.2) into our current version of slicer (5.6.2) it looks normal. I can create new models from segments and they also look normal.</p>
<p>However, we also changed our methodology-</p>
<p>Previously we:</p>
<ul>
<li>Loaded in CT scans of 6-12 individuals through the ImageStacks module</li>
<li>Segmented individual fish and individual bones using a variety of tools (thresholding, eraser, flood fill)</li>
<li>Exported the models from the data tab (right click → Export visible segments to models).</li>
<li>Save files as .ply</li>
</ul>
<p>More recently we have been:</p>
<ul>
<li>Loading in CT scans of 6-12 individuals through the ImageStacks module</li>
<li>Create an ROI for each individual fish in the scan, surrounding that individual as closely as possible</li>
<li>Use the “Crop Volume” Module to create a new volume for each ROI (I tried changing each of these settings and nothing fixed the problem)
<ul>
<li>Fill value = 0</li>
<li>Interpolated cropping = True</li>
<li>Spacing scale = 1</li>
<li>Isotropic spacing = True</li>
<li>Interpolator = Linear</li>
</ul>
</li>
<li>Save each volume as NRRD file</li>
<li>Individually load each NRRD file, segment export exactly the same as before.</li>
<li>Note: the issue shows up specifically when we click “Export visible segments to models”. The models look totally fine when we use “Show 3D” in the Segment Editor module.</li>
</ul>
<p>So the two main differences are the version of slicer and the incorporation of the Crop Volume module into our workflow. Could either of these explain the difference in results?</p>

---

## Post #7 by @muratmaga (2024-07-09 21:25 UTC)

<p>If the 3D view from the segmentations is fine, can you try going to <code>Segmentations</code> module, scroll down to <code>Export/Import Models and Labelmaps</code> and choose to export a new model.</p>
<p>and see if it has those artifacts.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9481b8d4c238b753c743aed7b8c9ed9017f939.png" alt="image" data-base62-sha1="flHgl17rLAXbIHQSMslwEgBqyWB" width="631" height="205"></p>

---

## Post #8 by @lassoan (2024-07-09 22:59 UTC)

<p>Can you post here slice views of the old (solid) and new (hollow) segmentations?</p>
<p>What is the spacing of the <code>binary labelmap</code> representation in of the old and new segmentation? (you can see that in the data module if you expand the information section in the bottom left corner)</p>

---

## Post #9 by @Dave_Matthews (2024-07-10 15:34 UTC)

<p>I think we figured it out!</p>
<p>In 5.6.2 we’ve been using “Use surface nets (fast)” for our 3d representations of our segmentations.<br>
If I leave this option checked when I export the model (even through the “segmentations” module) then the resulting model is lower resolution and has these strange artifacts. If I turn surface nets off, then it exports perfectly normally.</p>
<p>I’m not sure if this is the expected behavior, but I did not realize that surface nets would affect the exported model and not just the “show 3D” representation.</p>

---

## Post #10 by @muratmaga (2024-07-10 16:34 UTC)

<p>This is interesting. I have been using the surfacenet option for smoothing without any noticeable difference in 3D models (compared to standard method). Are you sure you have not changed anything other than that in processing pipeline?</p>

---

## Post #11 by @Dave_Matthews (2024-07-10 18:23 UTC)

<p>I’m fairly sure that this is the issue (and not our pipeline) because I can now create good and bad models from both new and old segmentations simply by toggling this switch. So even segmentations that were done on our older version of slicer can create models with artifacts if I turn on surface nets.</p>
<p>I’m happy to post any information about our Slicer instance if that helps understand why it’s happening.</p>

---

## Post #12 by @Dave_Matthews (2024-07-10 18:56 UTC)

<p>Just to follow this up, I just tried again on a different computer using 5.7.0 and I get the exact same behavior when exporting with surface nets turned on/off.</p>

---
