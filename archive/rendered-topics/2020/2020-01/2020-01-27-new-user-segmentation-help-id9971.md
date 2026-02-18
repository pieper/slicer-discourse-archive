# New user segmentation help

**Topic ID**: 9971
**Date**: 2020-01-27
**URL**: https://discourse.slicer.org/t/new-user-segmentation-help/9971

---

## Post #1 by @bobkallal (2020-01-27 17:55 UTC)

<p>Hi,</p>
<p>I’m a new user, trying to transition to using Slicer from Avizo. I have micro-CT scans of spiders, and I’m interested in segmenting the dense, sclerotized parts from the soft tissue as well as segmenting muscles. I have watched several tutorial videos and followed along from written tutorials, but I’m still struggling to get functionality akin of Avizo, but I suspect it is my inexperience. Any aid you can give, or videos you can point me to, would be great. Also, I’m using a Windows 10 machine with an Intel Xeon 3.3GHz processor, 128 GB RAM, and Invidia Quadro P4000 GPU.</p>
<ol>
<li>
<p>Are these specs sufficient? I find the program struggles and crashes frequently.</p>
</li>
<li>
<p>I am working primarily with the paint tool, but there are two tools from Avizo that I think should be here but I’m not finding yet and don’t see in a tutorial. The first is moving large areas, highlighted through all layers, between segments. For instance, I want to grab all the layers with legs and move them from a thresholded layers to another layer. How do I do that?</p>
</li>
</ol>
<p>I see the Scissors tool, but I do not understand how it works. If I have two layers (seg1 and seg2), and I circle an area with Editable Area: Everywhere and Modify Other Segments: Modify All, nothing happens. Paint seems to work more as expected (in seg2, if I highlight an area of seg2, with Editable Area: Inside seg1 and Modify Other Segments: Overwrite visible, it <em>does</em> move to seg2. But surely there is a way to move structures in many layers between segments?</p>
<ol start="3">
<li>Interpolation / Fill Between Slice. I have a feeling this is me not understanding the details of how Slicer is doing this process. In Avizo, I would highlight two or three areas of, for instance, a leg or duct or stretch of carapace, and interpolation would follow between those structures to highlight them without going through and segmenting each layer. Here, if I highlight two regions of a leg in seg2 (where seg1 is ‘the rest’ of the material), and Apply, nothing happens. I fear I am missing something obvious here as lacking this function will make this program difficult to continue to use.</li>
</ol>
<p>Thank you for your advice,<br>
Bob</p>

---

## Post #2 by @JanWitowski (2020-01-27 18:27 UTC)

<p>Hey <a class="mention" href="/u/bobkallal">@bobkallal</a>,<br>
Regarding specs it comes up pretty often and I’m sure you can find some threads on Discourse. There is <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/HardwareConfiguration" rel="noopener nofollow ugc">official recommended hardware list</a>. Take a look at this thread about handling micro CT / high res data:</p><aside class="quote quote-modified" data-post="1" data-topic="2469">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/working-with-large-datasets/2469">Working with large datasets</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, I have the luck of having some really nice high-res / microCT scans to work with. They are around the 1-2GB mark as original .dcms &amp; if loaded into fijiJ show up as 16bit individual images. I can get the sizes down of course by 

cropping the area of interest
then resizing each images x/y to 256x256
saving as an 8bit JPG

But this still leaves me often with a 70MB file(if saved as nifti) or folder of imags 
<a href="https://youtu.be/z_R7zyILIPw" rel="noopener nofollow ugc">I’m loading these across the web</a> so it would be good to get them down even furthe…
  </blockquote>
</aside>

<ol start="2">
<li></li>
</ol>
<blockquote>
<p>For instance, I want to grab all the layers with legs and move them from a thresholded layers to another layer.</p>
</blockquote>
<p>I’m not sure if I understood you correctly, but you can copy the mask/layer contents to another layer with Logical operators effect. There you can add &amp; perform other logical operations on layers.</p>
<blockquote>
<p>If I have two layers (seg1 and seg2), and I circle an area with Editable Area: Everywhere and Modify Other Segments: Modify All, nothing happens.</p>
</blockquote>
<p>What kind of operation are you trying to perform with scissors? (Erase, Fill)</p>
<p>If you have your segmentation on one layer (seg1) and want to copy part of seg1 to another layer (seg2), you can use either Scissors or Paint brush. Simple approach would be to: activate second layer seg2, choose Paint tool, select Editable area: Inside seg1. You can keep “Allow overlap” in Modify other segments option.</p>
<p>Similarly with Scissors: if you have segmentation on layer seg1 and want to copy a selected part of it: create new layer seg2 and activate it, select Scissors tool, use Fill inside operation, select Editable area: Inside seg1.</p>
<blockquote>
<p>Here, if I highlight two regions of a leg in seg2 (where seg1 is ‘the rest’ of the material), and Apply, nothing happens.</p>
</blockquote>
<p>Fill between slices works so that it will interpolate your segmentation between slices. Eg. if you have segmentation on seg1 slice <span class="hashtag-raw">#1</span> and seg1 slice <span class="hashtag-raw">#10</span>, it should fill in the between (seg1).</p>
<p>You might find instructions details important too:</p>
<blockquote>
<p>Instructions:</p>
<ul>
<li>Create complete segmentation on selected slices using any editor effect. Segmentation will only expanded if a slice is segmented but none of the direct neighbors are segmented, therefore do not use sphere brush with Paint effect and always leave at least one empty slice between segmented slices.</li>
<li>All visible segments will be interpolated, not just the selected segment.</li>
<li>The complete segmentation will be created by interpolating segmentations in empty slices.</li>
</ul>
<p>Masking settings are ignored. If segments overlap, segment higher in the segments table will have priority. The effect uses <a href="http://insight-journal.org/browse/publication/977" rel="noopener nofollow ugc">morphological contour interpolation method</a>.</p>
</blockquote>

---

## Post #3 by @bobkallal (2020-01-29 21:57 UTC)

<p>Dear Jan,</p>
<p>Thank you for your reply. I’m happy someone replied as I’m struggling a bit here myself.</p>
<p>When I bring a stacked image tif file into Slicer, it appears to be 50-200 MB. Is this considered a lot? They have been downsampled by 50% and cropped. If I have 128 GB RAM, surely that should be enough to handle it? As I am painting layer by layer into the segments, it takes about 30 seconds for the new color to appear, and eventually it crashes. If 10x RAM than data size is recommended, this seems to be satisfied. What am I missing?</p>
<p>The Logical Operators Effect was helpful - that was one of the things I needed.</p>
<p>I also think I understand scissors better.</p>
<p>I’m still struggling a bit with Fill Between Slices / interpolation. I have a segment1 and segment2, and segment2 has a mostly complete structure with a few holes in it. I make segment1 invisible, and initialize the interpolation on segment2 with Editable Area = segment1, and Modify Other Segments = Overwrite visible. My understanding that this should more or less connect areas of segment2 where they may be touching in invisible segment1 - does that seem coherent? Of course this takes a long time to calculate, but it doesn’t seem like it ends up doing very much interpolation. For instance, I have two slices about</p>
<p>Also, when something is “Erased,” does this mean its voxels are removed from all segments?</p>
<p>Thank you for your support. I am very interested in learning to use this program and I have many dozen segmentations to carry out!</p>

---

## Post #4 by @lassoan (2020-01-29 22:11 UTC)

<aside class="quote no-group" data-username="bobkallal" data-post="3" data-topic="9971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/838e76/48.png" class="avatar"> bobkallal:</div>
<blockquote>
<p>When I bring a stacked image tif file into Slicer, it appears to be 50-200 MB. Is this considered a lot? They have been downsampled by 50% and cropped. If I have 128 GB RAM, surely that should be enough to handle it? As I am painting layer by layer into the segments, it takes about 30 seconds for the new color to appear, and eventually it crashes. If 10x RAM than data size is recommended, this seems to be satisfied. What am I missing?</p>
</blockquote>
</aside>
<p>What is the volume size (shown in Volumes module → Volume Information section)?<br>
What Slicer version do you use?<br>
How much memory does Slicer use (you can see it in Windows Task manager)?</p>
<p>If you import from TIFF, make sure you convert to single-component (scalar) volume using “Vector to scalar volume” module.</p>
<aside class="quote no-group" data-username="bobkallal" data-post="3" data-topic="9971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/838e76/48.png" class="avatar"> bobkallal:</div>
<blockquote>
<p>I’m still struggling a bit with Fill Between Slices / interpolation. I have a segment1 and segment2, and segment2 has a mostly complete structure with a few holes in it. I make segment1 invisible, and initialize the interpolation on segment2 with Editable Area = segment1, and Modify Other Segments = Overwrite visible.</p>
</blockquote>
</aside>
<p>In general, if you want to interpolate segment2 then do not set segment1 as editable area, as it would restrict adding interpolated regions to segment2. Instead, you can leave editable area “Everywhere”.</p>
<aside class="quote no-group" data-username="bobkallal" data-post="3" data-topic="9971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/838e76/48.png" class="avatar"> bobkallal:</div>
<blockquote>
<p>Also, when something is “Erased,” does this mean its voxels are removed from all segments?</p>
</blockquote>
</aside>
<p>The data is always what you see. If you erase from all segments (e.g., by enabling “Erase all segments” in “Erase” effect) then you will see that data is erased from all segments. If you just erase from one segment then only that single segment is changed. When you paint somewhere and “Modify other segments” is set to “Overwrite all” or “Overwrite visible” then the painted region will be erased from other segments.</p>

---

## Post #5 by @muratmaga (2020-01-30 15:42 UTC)

<p>Dear <a class="mention" href="/u/bobkallal">@bobkallal</a>. Welcome to the Slicer world.</p>
<p>Please answer <a class="mention" href="/u/lassoan">@lassoan</a>’'s questions (about volume size and dimensions etc), and perhaps provide a few screenshots what you want to accomplish and what’s failing in Slicer. Also what version of Slicer are you using (stable or preview)?</p>

---

## Post #6 by @bobkallal (2020-02-27 18:44 UTC)

<p>Thank you for your replies. I apologize for the tardiness of this message.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<ol>
<li>I am attaching an image of what I see under Volume Information. The dimensions are 327x350x705 - is that what you are asking for? The tiff file in this case is 77 MB.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8323b5043ea4c8298f620803991dd3e7c455e2cf.png" data-download-href="/uploads/short-url/iI7390c2vqgMxmuDXDSundFgOjZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8323b5043ea4c8298f620803991dd3e7c455e2cf.png" alt="image" data-base62-sha1="iI7390c2vqgMxmuDXDSundFgOjZ" width="588" height="500" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">883×750 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>I’m using verison 4.11.0</li>
<li>Slicer is using 458.1 MB</li>
<li>I was not aware of this module. When I bring it up, I cannot select anything under ‘Input Vector Volume,’ with 'Output Scalar Volume" being the input tiff. What do you recommend?</li>
</ol>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
I’m using preview release 4.11.0. What I would like to do is segment out sclerites and muscles from scans of spiders, akin to what you can see in this paper: <a href="https://onlinelibrary.wiley.com/doi/full/10.1002/jmor.20939" rel="noopener nofollow ugc">https://onlinelibrary.wiley.com/doi/full/10.1002/jmor.20939</a></p>

---

## Post #7 by @muratmaga (2020-02-27 19:42 UTC)

<p>Your dataset is not big. You have plenty of RAM, so sluggishness and crashes should not come from lack of resources… Would it possible for you to share your dataset? I wonder if the issue is somehow the small voxel size?</p>
<p>As for segmentation lingo and terminology, perhaps you can take a look at our tutorial about how copying segments work, what it means to overwriting, or overlapping segments, segments to labelmap representation etc:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/45026482?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab03_Slicer_3_Segmentation" target="_blank" rel="nofollow noopener">SlicerMorph/W_2020</a></h3>

<p>Contents for the Winter 2020 SlicerMorph workshop. Contribute to SlicerMorph/W_2020 development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I find  trying with the simple cases and toy data until I understand the specifics of the functions is the best route in learning a new software. Then I switch to my own dataset…</p>

---

## Post #8 by @bobkallal (2020-02-27 20:04 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thank you. I also suspected I wasn’t having an issue with memory but I didn’t know another issue to investigate. Many of my samples are small. My voxel size is 0.000144999 mm, but I downsample by 50% in FIJI so I multiply by two, resulting in 0.0028 mm, which I think is correct. I’ll try to go back to the tutorials. I’m happy to share the dataset all the same, if there is a preferred way to do so.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I realized I forgot to reply about interpolation. Here’s my issue there - I have the green part of the spider, with blue rings which are the outside a roughly cylindrical structure. I want to interpolate the green area between them to segment out the blue cylinder.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4ff6b46a4da05ab79976ec79dc9d90f7272e0c69.jpeg" data-download-href="/uploads/short-url/bpohwv0TUQpOZ2XKtyTuKv2OT9L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff6b46a4da05ab79976ec79dc9d90f7272e0c69_2_690x374.jpeg" alt="image" data-base62-sha1="bpohwv0TUQpOZ2XKtyTuKv2OT9L" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff6b46a4da05ab79976ec79dc9d90f7272e0c69_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff6b46a4da05ab79976ec79dc9d90f7272e0c69_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4ff6b46a4da05ab79976ec79dc9d90f7272e0c69.jpeg 2x" data-dominant-color="678174"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1235×670 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I make the green invisible, then select “Editable Area: Everywhere” and “Modify Other Segments: Overwrite All,” and this works. But I’m confused why choosing “Editable Area: green” would not work. Changing to “overwrite visible” also works. I think I must experiment more.</p>

---

## Post #9 by @muratmaga (2020-02-27 20:52 UTC)

<p>I would suggest saving your tiff stack as a NRRD and posting somewhere on a cloud file share service and putting the link here…</p>
<p>By the way, with your computer specs, you shouldn’t encounter a problem with the  full resolution  dataset.</p>

---

## Post #10 by @bobkallal (2020-03-02 21:37 UTC)

<p>Thank you, I will try without reducing the data.</p>
<p>I have a new problem that I suspect is something simple. I want to open my project from last week (pictured above). Last time, saving the data produced the following files: a slicer scene file (mrml), a scene image file (png), an acsv file, and a vp file. I also produced an nrrd file from the stack in FIJI.</p>
<p>I’m attempting to follow the data loading tutorial by Csaba Pinter. If I drop the nrrd file into Slicer, only one of the views shows the stacked images; the other two are not shown correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c01ff070d377309f1a53749f0f05b64ea2362dc4.jpeg" data-download-href="/uploads/short-url/rpC6qYKrQC9nOYXV1IGPkB3Kfc0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c01ff070d377309f1a53749f0f05b64ea2362dc4_2_690x428.jpeg" alt="image" data-base62-sha1="rpC6qYKrQC9nOYXV1IGPkB3Kfc0" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c01ff070d377309f1a53749f0f05b64ea2362dc4_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c01ff070d377309f1a53749f0f05b64ea2362dc4_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c01ff070d377309f1a53749f0f05b64ea2362dc4_2_1380x856.jpeg 2x" data-dominant-color="60617A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2782×1728 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In part 2, you can drop an mrml scene file directly into Slicer. As I produced one last week, I try that - the segmented 3D visualization and one of three stacked images appears:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddf8e2071b57fff06c8ccb9f33ee2f9526085955.jpeg" data-download-href="/uploads/short-url/vFEKvE4matnhLT4H39kZ8dCtnM1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddf8e2071b57fff06c8ccb9f33ee2f9526085955_2_690x393.jpeg" alt="image" data-base62-sha1="vFEKvE4matnhLT4H39kZ8dCtnM1" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddf8e2071b57fff06c8ccb9f33ee2f9526085955_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddf8e2071b57fff06c8ccb9f33ee2f9526085955_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddf8e2071b57fff06c8ccb9f33ee2f9526085955_2_1380x786.jpeg 2x" data-dominant-color="525261"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2754×1570 660 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What am I missing here? I’m sorry if this should be obvious.</p>

---

## Post #11 by @muratmaga (2020-03-02 22:05 UTC)

<p>Your Z voxel spacing is incorrect. Go to <code>volumes</code> module and correct the value and make sure to save your NRRD. Also hit the little square icon in slice views to reset the field of view after correcting the spacing.</p>
<p>Do try the ImageStacks function that you get with installing the SlicerMorph extension with the latest preview. It can be a viable alternative to Fiji.</p>

---
