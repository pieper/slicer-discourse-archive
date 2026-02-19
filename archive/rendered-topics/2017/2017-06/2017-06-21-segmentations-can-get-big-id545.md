---
topic_id: 545
title: "Segmentations Can Get Big"
date: 2017-06-21
url: https://discourse.slicer.org/t/545
---

# Segmentations can get big!

**Topic ID**: 545
**Date**: 2017-06-21
**URL**: https://discourse.slicer.org/t/segmentations-can-get-big/545

---

## Post #1 by @Fernando (2017-06-21 12:40 UTC)

<p>Hi all (specially <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a>),</p>
<p>I am working with a 2D segmentation. After saving it, I use Python to process the NRRD files. The size of my master volume node is 28320 x 15232, it’s a scanned histological slice with 2 µm resolution. We hace 24 segments extending pretty much all around the slice, so the size of my NRRD array is 26013 x 13644 x 24, which takes about 8 GB of RAM and I can’t use my computer anymore when I try to open the file.</p>
<p>Some possible solutions I can think of:</p>
<ol>
<li>Start using downsampled reference images</li>
<li>Downsample my segmentation (how? Exporting to a new segmentation which has a smaller reference volume? Downsampling each segment individually?)</li>
</ol>
<p>It would be nice to be able to have multiple segments in the same volume (or slice, in this case) if they don’t overlap. A typical example is a FreeSurfer segmentation. There are 192 structures that don’t overlap. A segmentation in a 142 x 140 x 177 volume uses around 650 MB, while a label map with the same information would use around 3 MB.</p>
<p>Do you have any suggestions?</p>
<p>Also, in the FreeSurfer case, if I want to see only one segment I think I have to hide the other 191 one by one. Is there a way to hide all of them at the same time?</p>
<p>Thanks,<br>
Fernando</p>

---

## Post #2 by @lassoan (2017-06-21 13:06 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>28320 x 15232, it’s a scanned histological slice with 2 µm resolution. We hace 24 segments extending pretty much all around the slice, so the size of my NRRD array is 26013 x 13644 x 24, which takes about 8 GB of RAM and I can’t use my computer anymore when I try to open the file</p>
</blockquote>
</aside>
<p>Having many segments covering the whole volume is a worst case scenario that will certainly will be slower compared to a simple labelmap. It could be possible to define groups of segments that are not allowed to overlap and store them in a labelmap, but there are many higher-priority tasks, so probably this would not be available for at least 1-2 years.</p>
<p>Is it only an issue when loading/saving the segmentation?<br>
How much RAM do you have?<br>
How much virtual memory have you configured?<br>
What operating system do you use?</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Start using downsampled reference images</p>
</blockquote>
</aside>
<p>This is the most common approach. In fact, it is always recommended to crop and/or resample your volume to a reasonable size before you start segmentation using Crop volumes module.</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Downsample my segmentation (how? Exporting to a new segmentation which has a smaller reference volume? Downsampling each segment individually?)</p>
</blockquote>
</aside>
<p>Resolution of all the segments in the segmentation node are the same, fixed value. It is determined from the master volume that is selected first or you can define it manually (using <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#aa5cdbcafbf31055339b160938accdc00">SetReferenceImageGeometryParameterFromVolumeNode</a>).</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>It would be nice to be able to have multiple segments in the same volume (or slice, in this case) if they don’t overlap.</p>
</blockquote>
</aside>
<p>Collapsing all segments into a 3D labelmap only for saving could be feasible, it would not be that much work.</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>A typical example is a FreeSurfer segmentation. There are 192 structures that don’t overlap. A segmentation in a 142 x 140 x 177 volume uses around 650 MB, while a label map with the same information would use around 3 MB.</p>
</blockquote>
</aside>
<p>If you export the segmentation to a labelmap (using Segmentations module) and save it, how big the saved file is?<br>
Is this FreeSurfer segmentation example available somewhere?<br>
Is the segmentation volume compressed?</p>
<aside class="quote no-group" data-username="Fernando" data-post="1" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>I want to see only one segment I think I have to hide the other 191 one by one. Is there a way to hide all of them at the same time?</p>
</blockquote>
</aside>
<p>Finally, an easy question! Right-click the segment in the segment list or int the Data module / Subject hierarchy tab and choose “Show only selected segments”.</p>

---

## Post #3 by @Fernando (2017-06-21 13:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It could be possible to define groups of segments that are not allowed to overlap and store them in a labelmap, but there are many higher-priority tasks, so probably this would not be available for at least 1-2 years.</p>
</blockquote>
</aside>
<p>If you’re reading this in 2019, and in case this can help, for my data I would typically divide my segments into left, right and others. That would make my segmentation use 1 GB of RAM instead of 8. 10 MB instead of 650, for the FreeSurfer segmentation.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it only an issue when loading/saving the segmentation?<br>
How much RAM do you have?<br>
How much virtual memory have you configured?<br>
What operating system do you use?</p>
</blockquote>
</aside>
<p>Developer (me):<br>
I can’t load it on Slicer, nor outside using Python (or at least it hangs for a long time).<br>
I have 16 GB of RAM.<br>
I can’t say I know what virtual memory is, sorry.<br>
Ubuntu 16.04.2 LTS</p>
<h2><a name="p-2020-user-colleague-she-says-it-takes-some-time-to-load-and-save-but-its-acceptable-32-gb-1" class="anchor" href="#p-2020-user-colleague-she-says-it-takes-some-time-to-load-and-save-but-its-acceptable-32-gb-1" aria-label="Heading link"></a>User (colleague):<br>
She says it takes some time to load and save, but it’s acceptable.<br>
32 GB</h2>
<p>Windows 7</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Resolution of all the segments in the segmentation node are the same, fixed value. It is determined from the master volume that is selected first or you can define it manually (using SetReferenceImageGeometryParameterFromVolumeNode).</p>
</blockquote>
</aside>
<p>I’ll use downsampled images as a reference from now on. My question is: how would you downsample an already existing segmentation with overlapping segments?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Collapsing all segments into a 3D labelmap only for saving could be feasible, it would not be that much work.</p>
</blockquote>
</aside>
<p>I meant internally, handled by the Segmentations logic. Maybe in 1-2 years <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you export the segmentation to a labelmap (using Segmentations module) and save it, how big the saved file is?<br>
Is this FreeSurfer segmentation example available somewhere?<br>
Is the segmentation volume compressed?</p>
</blockquote>
</aside>
<p>The Freesurfer label map uses 500 kB in disk. It’s compressed. I haven’t tried, but I guess a compressed label map would use around the same. <a href="https://www.dropbox.com/s/rkykd5upkejgv7h/freesurfer_results.zip?dl=0" rel="noopener nofollow ugc">This is the data</a>.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Finally, an easy question! Right-click the segment in the segment list or int the Data module / Subject hierarchy tab and choose “Show only selected segments”.</p>
</blockquote>
</aside>
<p>If I question is too easy to answer, I’ve probably not searched well enough! What if I want to show all of them again after that operation?</p>
<p>Thanks Andras!</p>

---

## Post #4 by @lassoan (2017-06-21 14:23 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>What if I want to show all of them again after that operation</p>
</blockquote>
</aside>
<p>In Segmentations module: select all segments in the segment list, right-click, “Show only selected segments”.</p>
<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>I can’t say I know what virtual memory is, sorry.</p>
</blockquote>
</aside>
<p>On Linux, virtual memory is referred to as “swap” - <a href="https://superuser.com/questions/48505/how-to-find-virtual-memory-size-and-cache-size-of-a-linux-system" class="inline-onebox">How to find virtual memory size and cache size of a linux system? - Super User</a></p>
<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>how would you downsample an already existing segmentation with overlapping segments?</p>
</blockquote>
</aside>
<p>Create a new segmentation with the desired resolution (set the master volume, maybe also create a segment in it) and then import all segments from the other segmentation.</p>
<p>Do you only have problem when loading/saving the segmentation?</p>

---

## Post #5 by @ihnorton (2017-06-21 16:10 UTC)

<p>For histology, the usual approach is to resample and tile at multiple zoom levels. Then you can show the whole slide overview and lazy-load only a small subset of the high resolution tiles as the user zooms in and moves around (either from separate tile files, or by mmap’ing the whole file and pulling offsets as needed). Segmentations and annotations are saved as vectors. Very similar to what map software does.</p>
<p><a class="mention" href="/u/fernando">@Fernando</a> if you haven’t looked at other software already, the keyword is “virtual slide”, and there are several tile-creation utilities and viewers around including open source, e.g. OpenSeaDragon and several in ImageJ/FIJI. I think Kitware has (or had) one too, but I don’t remember the name. In principle lazy loading and multi-level view could be done in Slicer, but it would be a fair amount of work.</p>

---

## Post #6 by @lassoan (2017-06-21 16:26 UTC)

<p>At some point I think Brad Lowekamp implemented a simple CLI module that took a ROI and a filename as an input and it returned the requested part of the image as an output. It made really easy to retrieve a certain portion of a large image. I think it used the MetaIO format, which has a nice reader that can quickly extract a small portion of a huge volume.</p>

---

## Post #7 by @fedorov (2017-06-21 17:04 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="5" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Kitware has (or had) one too</p>
</blockquote>
</aside>
<p><a href="https://digitalslidearchive.github.io/HistomicsTK/" class="onebox" target="_blank" rel="noopener">https://digitalslidearchive.github.io/HistomicsTK/</a></p>

---

## Post #8 by @Fernando (2017-06-22 10:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>On Linux, virtual memory is referred to as “swap”</p>
</blockquote>
</aside>
<pre><code>➜  ~ free
              total        used        free      shared  buff/cache   available
Mem:       16353852    10332076     1450964      475936     4570812     5110556
Swap:      16698364         440    16697924
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you only have problem when loading/saving the segmentation?</p>
</blockquote>
</aside>
<p>I can’t load it into Slicer, I can’t open it with Python’s library <code>nrrd</code>.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> that’s exactly what I’m doing: resampling and tiles. But until now, the segmentation files at the reference resolution hadn’t got so big. Of course the ideal solution would be using that virtual slide, as in <a href="https://www.hamamatsu.com/jp/en/U12388-01.html" rel="noopener nofollow ugc">NDP.view2</a>, but I haven’t looked into it yet. I’ll check the tools you, <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/fedorov">@fedorov</a> have mentioned.</p>
<p>Thank you all for your answers!</p>

---

## Post #9 by @lassoan (2017-06-22 11:54 UTC)

<p>It send that you only configured to have 16GB of virtual memory. I usually set virtual memory size 5-10x the size of the data set I’m processing.</p>

---

## Post #10 by @Fernando (2017-07-05 13:29 UTC)

<p>I added some swap but still can’t get Slicer to open the segmentation:</p>
<pre><code class="lang-auto">➜  ~ free -h 
              total        used        free      shared  buff/cache   available
Mem:            15G        6,2G        6,5G        127M        2,9G        8,9G
Swap:           65G          0B         65G
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Create a new segmentation with the desired resolution (set the master volume, maybe also create a segment in it) and then import all segments from the other segmentation.</p>
</blockquote>
</aside>
<p>This didn’t work. I create the segmentation, set my small volume as reference and copy the segments (same result if I already had a segment). The segments are high-resolution. I have to overwrite one of them so that it gets downsampled. Is there any way to do this programmatically? That might be easier. I tried <code>SetReferenceImageGeometryParameterFromVolumeNode()</code>, but that didn’t modify the segments.</p>

---

## Post #11 by @lassoan (2017-07-05 20:23 UTC)

<p>Resampling does not happen immediately when you import the labelmap (as resampling may be a lossy operation or it may take a long time to compute), but only performed when it is needed (e.g., when the segment is modified). Maybe if you use <code>Copy</code> operator of <code>Logical operators</code> effect then the result is resampled. Or you can export the segment as labelmap, use one of the Resample modules to change resolution, and import it to segmentation node. We’ll make this easier in the future (see <a href="https://issues.slicer.org/view.php?id=4308">https://issues.slicer.org/view.php?id=4308</a>).</p>

---

## Post #12 by @Fernando (2017-07-05 22:16 UTC)

<p>I’m not sure how to use the <code>Copy</code> operator for this.</p>
<p>When I tried the second approach, I got an empty label map. I’ve reported the issue: <a href="https://issues.slicer.org/view.php?id=4392" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4392</a></p>

---

## Post #13 by @Fernando (2019-10-23 16:36 UTC)

<p>This seems to have been addressed recently: <a href="https://discourse.slicer.org/t/new-feature-shared-labelmap-segmentations/8814" class="inline-onebox">New feature: Shared labelmap segmentations</a>.</p>

---

## Post #14 by @lassoan (2021-02-05 04:09 UTC)

<p>A post was split to a new topic: <a href="/t/brain-and-skull-segmentation/15859">Brain and skull segmentation</a></p>

---

## Post #15 by @lassoan (2023-03-26 04:09 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-with-spatial-resolution-different-than-the-source-volume/28582">Segmentation with spatial resolution different than the source volume</a></p>

---
