# Extracting a subnetwork from 3D volume

**Topic ID**: 11570
**Date**: 2020-05-16
**URL**: https://discourse.slicer.org/t/extracting-a-subnetwork-from-3d-volume/11570

---

## Post #1 by @Deepa (2020-05-16 03:21 UTC)

<p>Hi there,</p>
<p>This is a follow up to my previous post <a href="https://discourse.slicer.org/t/3d-reconstruction-from-2d-slices/9784/10">here</a></p>
<p>I’m trying to reconstruct a 3D volume from the 2D images provided in <a href="https://www.nature.com/articles/s41598-019-49055-7" rel="noopener nofollow ugc">this</a> study (<a href="https://springernature.figshare.com/articles/Images_of_mouse_popliteal_lymph_node_vascular_structure_derived_using_phase-contrast_synchrotron_micro-computed_tomography_CT_/8289869" rel="noopener nofollow ugc">image source</a>).<br>
Post reconstruction, I’d like to filter only blood vessels that range from 1-10 micrometers.<br>
Side note: The input data for reconstructing a 3D volume is available in tiff format.</p>
<p>Following the instructions given in the above-mentioned link, I could obtain the following 3D volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/737cf97c8a1f01901e55188e39f0411d23b6662e.png" alt="image" data-base62-sha1="gtEFhxHDjAWsgPY23SIdB7v78my" width="345" height="223"> .</p>
<p>Next,<br>
I’d like to generate a skeleton like the following (sample skeleton image below) from the 3D volume.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd9526906dfdd70e0a9da95c79b079d131c80987.png" alt="Untitled" data-base62-sha1="tkFqYYtn2ElJpZg3f9jDhIuiL0X" width="201" height="214"></p>
<p>Next, I’d like to compute the centerline distance and maximal inscribed sphere radius (MISR) associated with each segment. By segment, I refer to the line between two branching points/ branching point and a terminal point. Previously, I have had some experience to use VMTK for obtaining centerline distance and MISR for simple skeletons like the one shown in the skeleton displayed above.<br>
The polyData could be nicely processed further into numpy array with node numbers, edge numbers and the corresponding centerlines distances and MISR’s of each edge(/segment/branch) .  So I 'd like to us the output obtained (subnetwork) from SLicer in VMTK to obtain centerline distance and MISR.</p>
<p>In the end, I am looking for a connected network(/skeleton), which I call as a <code>subnetwork,</code> with around 25 segments.</p>
<p>Here,  I’d like to ask for suggestions on how to extract the network.</p>
<ol>
<li>Should I convert the 3D volume into a skeleton and then apply the constraints to extract the subnetwork.</li>
<li>Or, Is it easier to extract a subvolume from the 3D volume and later skeletonize the subvolume ?</li>
</ol>
<p>The <a href="https://discourse.slicer.org/t/3d-reconstruction-from-2d-slices/9784/10">following suggestion</a> has been offered in the previous post</p>
<blockquote>
<p>If the goal is to just extract vessels of a diameter range then it is very easy to do. If you have a segment that only contains vessels then you can use the Margin effect to shrink diameter of all vessels (this will make all vessels that have smaller diameters than the erosion disappear completely) then use the same effect to grow them back to the original diameter. This results in vessel tree that contains vessels that have diameters over the margin size (or twice the margin size - you need to check the details). To remove large-diameter vessels, you first find them using the same method, then use Logical operators effect to remove them from the image.</p>
</blockquote>
<p>But I’m afraid I don’t clearly understand how to do the above after obtaining the 3D volume.</p>
<p>I’d like to request for help to do the above.</p>
<p>P.S: I’d also like to know if it’s possible to do the above programmatically. The size of the dataset is large (6GB). So I’ve been trying to work on a server by launching the GUI in X terminal. Unfortunately, it’s getting really tough, the graphics freeze and it closes when there are interruptions due to work from home:( . Doing this programmatically will allow me to use <code>screen</code>.</p>

---

## Post #2 by @muratmaga (2020-05-16 04:12 UTC)

<p>I can’t comment for skeletinization and VMTK, but what <a class="mention" href="/u/lassoan">@lassoan</a> suggested above should result in something like this:<br>
Top Original Volume (LN1 dataset)<br>
Bottom segmentation threshold followed by margin effect (shrink/dilate operation) that left 10voxel or larger diameter vessels:<br>
(I couldn’t find the actual voxel sizes in the data repository, so its voxel units).</p>
<p>Does this help?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f68f61f59461f27d3ed6cbc5ea1d727bc4791cba.jpeg" alt="image" data-base62-sha1="zbaEwCOuqPLVv30zAgElS6iWvfc" width="357" height="291"></p>

---

## Post #3 by @Deepa (2020-05-16 05:03 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Thank you very much for the response. I had a chance to use the <code>local thickness plugin</code> in Fiji and the output obtained was similar to the second image displayed with disconnected fragments. Is there a way to remove all the disconnected fragments and retain only the segments that are connected?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Bottom segmentation threshold followed by margin effect (shrink/dilate operation) that left 10voxel or larger diameter vessels</p>
</blockquote>
</aside>
<p>If my understanding is right, the above has retained the large diameter vessels and removed the small diameter vessels. Shall we retain the small ones and remove the large ones?</p>
<p>Thanks a ton for your time and kind attention.</p>

---

## Post #4 by @muratmaga (2020-05-16 05:18 UTC)

<p>You mean like this? If so, please follow the <a class="mention" href="/u/lassoan">@lassoan</a>’s instructions above (Basically segment larger diameter ones as a separate segment (red), then subtract it from the original segment (green)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af54e03e70d1174fba768e96d8e230986a2aebe.jpeg" alt="image" data-base62-sha1="m6P5NcL2EU792FuUYYwYax59kcu" width="530" height="392"></p>

---

## Post #5 by @Deepa (2020-05-16 05:51 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Thank you!</p>
<p>Yes, absolutely! After we subtract red from green, can we remove the disconnected fragments;<br>
extract a subvolume (I am not sure how this can be done. For instance, VMTK offers branch clipper)<br>
and save the resulting volume in vtp or stl format?</p>
<p>Thanks again for the valuable suggestions.</p>

---

## Post #6 by @lassoan (2020-05-16 18:57 UTC)

<p>You can remove disconnected fragments using Islands effect; and clip branches using Scissors effect. You can save results to mesh files using <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Export to files</a>.</p>

---

## Post #7 by @Deepa (2020-05-17 07:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot. I’m looking for ways to do the above tasks programmatically (in Python) and I’d a chance to go through this information provided here</p><aside class="quote quote-modified" data-post="1" data-topic="11569">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569">Run Slicer in your web browser - as a Jupyter notebook or as a full application</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    It has been possible to use Slicer from Jupyter notebooks but the most recent Slicer Preview Release takes this to a whole new level. 
<a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master" rel="noopener nofollow ugc">Click here to try a few example interactive notebooks now</a> - or see a short video demonstrating the new features: 

  <a href="https://www.youtube.com/watch?v=oZ3_cRXX2QM" target="_blank" rel="noopener nofollow ugc">
    [Medical image processing in your web browser using Jupyter notebooks and 3D Slicer]
  </a>


Highlights: 

Improved interactive use

You can now use IPython widgets (sliders, buttons, etc.) to control Slicer or adjust processing and visualization…
  </blockquote>
</aside>

<p>This is for Jupyter notebooks, I would like to have the above workflow in a script and run it in a server.</p>
<p>The input will be the tiff images and the output will be the stl file. I am not sure how the clipping can be<br>
done programmatically, so I wish to exclude that step for now.</p>
<p>Any help on how to set up the above workflow in Python will be of great help!</p>
<p>Thanks a lot</p>

---

## Post #8 by @lassoan (2020-05-17 15:40 UTC)

<p>Jupyter notebook is just one way of rendering an web page that your users can interact with. It is nice because you can use the exact same technology for prototyping as for final deployment. You can display a notebook in read-only mode but still with active widgets using <a href="https://github.com/voila-dashboards/voila">Voila</a>. If you are comfortable with using Javascript, it should be quite easy to put together a html page with a data upload section, an iframe to display Slicer’s 3D view for interactive preview/editing, and a download button.</p>
<p>Using binder has the advantage that it is free and it takes care of starting a new Slicer docker container for each user session. However, in the worst case, startup time can be up to 1-2 minutes. So, for optimal user experience you probably want to set up your own hosting using google/amazon/microsoft cloud services.</p>

---

## Post #9 by @Deepa (2020-05-17 16:11 UTC)

<p><span class="mention">@lasson</span> Thank you. But, unfortunately I don’t have any experience in working with Javascript.<br>
Can we use Slicer in PyCharm? In my case, I don’t want to visualize the graphics for this dataset. Can I simply run the commands that are executed in the GUI through command line in Python?</p>
<p>Thank you very much for your time and kind attention</p>

---

## Post #10 by @Deepa (2020-05-17 16:16 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Could you please let me know the commands/Plugins that have been used to obtain red and green regions? And which plugin can be used to subtract red from green?</p>
<p>Thanks a lot</p>

---

## Post #11 by @lassoan (2020-05-17 16:37 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="9" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>Can we use Slicer in PyCharm?</p>
</blockquote>
</aside>
<p>Yes. You can either use it with SlicerDebuggingTools extension, or you can use it via Jupyter notebook interface.</p>
<p>You can edit/run Slicer using notebook or debugging interface in Visual Studio Code, too (I just tried this yesterday and it worked well).</p>

---

## Post #12 by @muratmaga (2020-05-17 22:47 UTC)

<p>I only used Segment Editor following <a class="mention" href="/u/lassoan">@lassoan</a> suggestions</p>
<ol>
<li>Add blank segment and Threshold</li>
<li>Create a blank segment, copy from segment_1 (logical operations)</li>
<li>Shrink and dilate segment_2 to retain large segments (margin operations)</li>
<li>subtract segment_2 from Segment_1 using logical operations.</li>
</ol>

---

## Post #13 by @Deepa (2020-05-18 06:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Add blank segment and Threshold</p>
</blockquote>
</aside>
<p>Could you please let me know the threshold?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Create a blank segment, copy from segment_1 (logical operations)</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Shrink and dilate segment_2 to retain large segments (margin operations)</p>
</blockquote>
</aside>
<p>Could you please let me know the margin size that was used in this step?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55464ba110afcadd3711c7ec68ee07c53f8c83e.png" data-download-href="/uploads/short-url/s9ESb2TKFbL02ma1eWhRzyTPb54.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c55464ba110afcadd3711c7ec68ee07c53f8c83e_2_300x500.png" alt="Untitled" data-base62-sha1="s9ESb2TKFbL02ma1eWhRzyTPb54" width="300" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c55464ba110afcadd3711c7ec68ee07c53f8c83e_2_300x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c55464ba110afcadd3711c7ec68ee07c53f8c83e_2_450x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c55464ba110afcadd3711c7ec68ee07c53f8c83e_2_600x1000.png 2x" data-dominant-color="808086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1929×3209 701 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @muratmaga (2020-05-18 15:48 UTC)

<p>Dataset I downloaded from your link was binary (it was all 0s and 255s), meaning that any non-zero threshold value will give you the same segmentation. I think I put in something like 1</p>
<p>For margin, I entered 10, that was only to pick up something that will clear to small diameters. You should explore your datasets more carefully. Particularly you need to find the real voxel spacing.</p>

---

## Post #15 by @Deepa (2020-05-19 03:46 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Thank you.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Particularly you need to find the real voxel spacing.</p>
</blockquote>
</aside>
<p>“the voxel size in this study (pixel size of 0.81 µm)” This has been mentioned in the paper associated with the dataset.</p>
<p>I’d like to know if we can use this (0.81 µm) to subtract green from red and obtain the vessels in the range 0-10 µm thickness as a result.</p>
<p>Kindly excuse me for the naive questions.</p>

---

## Post #16 by @muratmaga (2020-05-19 15:07 UTC)

<p>Yes, you should first set the voxel spacing for your volume. There are few things to be careful though. Default spacing units in slicer is mms. So 0.81 micron would be 0.00081mm. There are some down sides of working with such small numbers. So you should either:</p>
<p>(1) increase the precision of length unit from the default 3 to 8 or something.<br>
(2) change the default length unit to micron.</p>
<p>Both of these can be set under <strong>Edit-&gt;Application Settings -&gt;Units</strong>. (Enable the advance option for 2).</p>
<p>You need to do these before you import your data.</p>
<p>If you are using <code>ImageStacks</code> from SlicerMorph to import this data, select the entire sequence of images you would like to work with, then enter the spacing information (either in mms, or micron, dependning on your preference above) and then choose ‘Downsample’ (since you seem to be running out of memory).</p>
<p>The resultant volume will be reduced by 2 in each axis, and then the voxel spacing will be adjusted accordingly (1.62microns).</p>
<p>When you specify the margin size during dilate/shrink operation, you can choose 10 micron as the size (if that’s what you want to remove)  for the second segment. This operation will remove anything less than 10micron in diameter (I think, as <a class="mention" href="/u/lassoan">@lassoan</a> indicated you need to check this for yourself, and experiment). So this segment will contain only the vessels that are larger than specified size.</p>
<p>To retain only the small diameter ones, subtract this from the first segment which has the all the vessels, and the remaining ones should be the vessels you want to isolate…</p>

---

## Post #17 by @Deepa (2020-05-20 11:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Yes, you should first set the voxel spacing for your volume. There are few things to be careful though. Default spacing units in slicer is mms. So 0.81 micron would be 0.00081mm. There are some down sides of working with such small numbers. So you should either:</p>
<p>(1) increase the precision of length unit from the default 3 to 8 or something.<br>
(2) change the default length unit to micron.</p>
<p>Both of these can be set under <strong>Edit-&gt;Application Settings -&gt;Units</strong> . (Enable the advance option for 2).</p>
</blockquote>
</aside>
<p>I change the settings using advanced option.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If you are using <code>ImageStacks</code> from SlicerMorph to import this data, select the entire sequence of images you would like to work with, then enter the spacing information (either in mms, or micron, dependning on your preference above) and then choose ‘Downsample’ (since you seem to be running out of memory).</p>
</blockquote>
</aside>
<p>I couldn’t install/find the SlicerMorph extension, so I continued with the usual procedure to load the data. File &gt; Add Data.</p>
<p>After the data is loaded, I am not able to see the image slices in the RYG panels on the right. It shows the image is out of frame.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380c1018590e082a5f57ddfac8e9c5c561d32297.png" data-download-href="/uploads/short-url/7ZOA8M6GHAK1VgVcbIXh2kZEph5.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/380c1018590e082a5f57ddfac8e9c5c561d32297_2_383x500.png" alt="Untitled" data-base62-sha1="7ZOA8M6GHAK1VgVcbIXh2kZEph5" width="383" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/380c1018590e082a5f57ddfac8e9c5c561d32297_2_383x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/380c1018590e082a5f57ddfac8e9c5c561d32297_2_574x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/380c1018590e082a5f57ddfac8e9c5c561d32297_2_766x1000.png 2x" data-dominant-color="DEDEDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">2628×3428 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure why this occurs.</p>

---

## Post #18 by @muratmaga (2020-05-20 15:47 UTC)

<p>SlicerMorph is only available for preview versions (4.11). You must be using the stable (4.10.2). In general switching to the preview, you will have other benefits (as in improved and added functionality)</p>

---

## Post #19 by @Deepa (2020-05-21 09:03 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I installed preview version 4.11. Unfortunately, volume rendering wasn’t successful.</p>
<blockquote>
<p>/Slicer-4.11.0-2020-05-19-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0143ca9d02a7e23a4e81438dd2fccfc5e47396d7.png" data-download-href="/uploads/short-url/bbIDG9CPpVqGqWdWde7l9CcKmH.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0143ca9d02a7e23a4e81438dd2fccfc5e47396d7_2_492x499.png" alt="Untitled" data-base62-sha1="bbIDG9CPpVqGqWdWde7l9CcKmH" width="492" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0143ca9d02a7e23a4e81438dd2fccfc5e47396d7_2_492x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0143ca9d02a7e23a4e81438dd2fccfc5e47396d7_2_738x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0143ca9d02a7e23a4e81438dd2fccfc5e47396d7_2_984x998.png 2x" data-dominant-color="87878C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1921×1949 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, I couldn’t see the slices on the right panel after loading the files using ImageStacks.</p>
<p>Could you please let me know if the issues reported above are due to the following error?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb8d5483bf5982b161009da661d5c2478da2f850.png" data-download-href="/uploads/short-url/xBN0fh68nOGSR7QZWGaec4IBdcs.png?dl=1" title="untitled1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb8d5483bf5982b161009da661d5c2478da2f850.png" alt="untitled1" data-base62-sha1="xBN0fh68nOGSR7QZWGaec4IBdcs" width="613" height="500" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">untitled1</span><span class="informations">1035×843 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am accessing Slicer installed on linux server through Mobaxterm. I am facing same problem with the stable version too. Please let me know if I should open a new thread for this issue.</p>
<p>I don’t encounter the same issue while using Slicer on my laptop with Windows OS. Suggestions on how to resolve the display issue while running Slicer on a remote server will be of great help.</p>

---

## Post #20 by @Deepa (2020-05-21 17:02 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Meanwhile, I could use the segment editor to do the following in my laptop</p>
<ol>
<li>Segment 1: Threshold range: 63 - 255 (default)</li>
<li>Segment  2: Segment 1 has been copied in segment 2. Next, margin tab was used to shrink and grow (10um).</li>
<li>Segment 3: Segment 1 was copied using logical operator. Again, using margin operator I tried to subtract 2 from 3.</li>
</ol>
<p>Next, to  retain only segment 3 (i.e vessel less than 10 um) , I tried to remove both segment 1 and segment 2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e335d210e888a1046995570da14753a14dc48779.png" data-download-href="/uploads/short-url/wpZH8MlLoiuIQSWCAlNCABfVxCV.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e335d210e888a1046995570da14753a14dc48779_2_345x194.png" alt="Untitled" data-base62-sha1="wpZH8MlLoiuIQSWCAlNCABfVxCV" width="345" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e335d210e888a1046995570da14753a14dc48779_2_345x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e335d210e888a1046995570da14753a14dc48779_2_517x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e335d210e888a1046995570da14753a14dc48779_2_690x388.png 2x" data-dominant-color="6A696C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1920×1080 574 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But , I still find the vessels greater than 10 um (grey colored) in the volume. I would like  to know<br>
how to retain only brown colored ( &lt; 10 um vessels) in the volume.</p>
<p>Thank you very much<br>
Deepa</p>

---

## Post #21 by @Deepa (2020-05-21 17:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can remove disconnected fragments using Islands effect</p>
</blockquote>
</aside>
<p>I would like to know if it is right to select <code>keep largest island</code> to retain only the connected component and remove fragments.</p>

---

## Post #23 by @muratmaga (2020-05-21 17:23 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="19" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I am accessing Slicer installed on linux server through Mobaxterm. I am facing same problem with the stable version too. Please let me know if I should open a new thread for this issue.</p>
</blockquote>
</aside>
<p>This issue is due to OpenGL support in Mobaxterm. I am not sure what the fix it. In our lab we use VNC + virtualGL to run Slicer in a remote Linux server.</p>
<aside class="quote no-group" data-username="Deepa" data-post="21" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I would like to know if it is right to select <code>keep largest island</code> to retain only the connected component and remove fragments.</p>
</blockquote>
</aside>
<p>If want to create a new volume that only contains voxels represented by the brown segment, you can use the <code>MaskVolume</code> which will create a new volume.</p>

---

## Post #24 by @Deepa (2020-05-22 17:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can remove disconnected fragments using Islands effect</p>
</blockquote>
</aside>
<p>May I know how long it would take to remove the disconnected fragments using Island effect.</p>
<p>I am running island effect on a volume that resulted after using shrink and grow operations.<br>
It’s running on my local machine for 4 hours and it’s not complete yet.</p>
<p>Thanks a lot for the support<br>
Deepa</p>

---

## Post #25 by @lassoan (2020-05-22 18:10 UTC)

<p>Usually it takes a few seconds, maybe it can take 1-2 minutes for a huge image. Did you reduce the default minimum island size? Can you upload your scene .mrb file somewhere and post the link here?</p>

---

## Post #26 by @Deepa (2020-05-23 02:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Did you reduce the default minimum island size?</p>
</blockquote>
</aside>
<p>I didn’t reduce the default minimum island. I selected <code>island effect</code> , <code>keep largest island</code> and hit enter.</p>
<p>After I forcefully terminated the run, the following error message was shown. I think there was a memory leak.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27088003c25b32db8a5f310b49123cb68dcdeddb.png" alt="image" data-base62-sha1="5ziPCEzuM9v0oMafnqPYUgmSm3p" width="512" height="212"></p>
<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you upload your scene .mrb file somewhere and post the link here?</p>
</blockquote>
</aside>
<p>Sure, I will repeat the steps and share the scene if I encounter the same problem again.<br>
Thanks a lot for the support.</p>

---

## Post #27 by @Deepa (2020-06-03 10:45 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
This time I carried out all the steps on a server and I could get it working</p>

---

## Post #28 by @Deepa (2020-06-03 11:22 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>When you specify the margin size during dilate/shrink operation, you can choose 10 micron as the size (if that’s what you want to remove) for the second segment. This operation will remove anything less than 10micron in diameter</p>
</blockquote>
</aside>
<p>Could you offer some advice on how to set the margin size for filtering vessel diameters &gt; 5 micron and &lt; 10 micron?<br>
Previously I have used 10 micron in <code>Margin</code> settings for both shrink and grow to filter vessels less than 10 microns.</p>
<p>Thank you very much for your time and attention</p>

---

## Post #29 by @Deepa (2020-06-03 17:09 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>After using Islands for retaining the largest connected island , I could observe the resulting segment has holes on the surface.</p>
<p>I would like to know why these holes are present on the surface and how to obtain a surface without holes. In the end I would like to retain the surfaces that don’t have holes. The reason is, I intend to find the centerline lengths and I am afraid that computation of centerline lengths will be erroneous when holes area present.</p>
<p>Suggestions on how to retain surfaces without holes will be really helpful</p>

---

## Post #30 by @lassoan (2020-06-03 17:25 UTC)

<p>Can you post a few screenshots that shows what kind of holes you see?</p>
<p>You may avoid holes if you disable surface smoothing (in drop-down menu of “Show 3D” button).</p>

---

## Post #31 by @Deepa (2020-06-04 03:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Please find the snapshot below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e305270eb34ba3f8275f12140ec74c6ebbe1b47.png" data-download-href="/uploads/short-url/b9GLSfMJZ74YQrFqFDTdQuVEg3Z.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e305270eb34ba3f8275f12140ec74c6ebbe1b47_2_379x500.png" alt="Untitled" data-base62-sha1="b9GLSfMJZ74YQrFqFDTdQuVEg3Z" width="379" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e305270eb34ba3f8275f12140ec74c6ebbe1b47_2_379x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e305270eb34ba3f8275f12140ec74c6ebbe1b47.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e305270eb34ba3f8275f12140ec74c6ebbe1b47.png 2x" data-dominant-color="7A7A83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">540×712 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="11570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may avoid holes if you disable surface smoothing (in drop-down menu of “Show 3D” button).</p>
</blockquote>
</aside>
<p>Sure, I will try this</p>

---
