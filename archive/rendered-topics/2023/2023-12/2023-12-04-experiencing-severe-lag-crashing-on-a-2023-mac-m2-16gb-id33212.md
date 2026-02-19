---
topic_id: 33212
title: "Experiencing Severe Lag Crashing On A 2023 Mac M2 16Gb"
date: 2023-12-04
url: https://discourse.slicer.org/t/33212
---

# Experiencing severe lag/crashing on a 2023 Mac M2 16GB

**Topic ID**: 33212
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/experiencing-severe-lag-crashing-on-a-2023-mac-m2-16gb/33212

---

## Post #1 by @yevyevchungy (2023-12-04 23:02 UTC)

<p>Hello, I am a new user of 3D Slicer and I am experiencing long wait times (8 min+) and crashing with the program on my 2023 Mac M2 16 GB, which based off what I have seen and read seems uncommon. I am wondering if anyone has any insight as to why I am having this problem/can provide any tips?</p>
<p>I am working with CT data (DICOM) and it takes ~8+ min just to load DICOM data that is already in my DICOM database. Once this data does load, I have noticed that some buttons/tools take an extremely long time to load/will simply cause an error, forcing me to quit the program. For example, if I load my DICOM data and then try to click on “Segment Editor” it will load endlessly/crash. However I noticed that if I click on “Segment Editor” before I load my DICOM data, I do not run into this problem? When I try to proceed with segmentation to select my source volume to enable editing, the program always crashes, and I have been stuck on this step for a couple days now. Does anyone have any idea as to why this may be happening?</p>

---

## Post #2 by @pieper (2023-12-04 23:07 UTC)

<p>Hmm, yes, that is unusual.  I don’t do a lot of heavy processing on it, but when i test with a 8GB M2 mac book air things seem normal and I don’t get crashes.  We have seen a few odd cases in the past when they first came out but mostly the M macs work pretty well lately.</p>

---

## Post #3 by @hherhold (2023-12-05 12:05 UTC)

<p>How big is your dataset? Are you running anything else that might be using a lot of RAM?</p>

---

## Post #4 by @yevyevchungy (2023-12-05 14:34 UTC)

<p>My datasets range from 6-9 GB in size with series counts of approximately 1200-1300. I am suspecting its an issue regarding RAM because once I click certain buttons or try to access certain functions and the software is loading/frozen for long enough, I get a popup that says “Your system has run out of application memory” and that I must force quit Slicer.</p>
<p>Can someone confirm that this is a RAM problem? Would the problem be resolved by getting a computer with more RAM or are there any other ways to resolve the issue? My only concern is that a coworker working on the same project, with the same 16GB M2 MacBook Pro was able to successfully use segmentation on these data sets (albeit they did also complain about lengthy wait times).</p>

---

## Post #5 by @muratmaga (2023-12-05 16:48 UTC)

<aside class="quote no-group" data-username="yevyevchungy" data-post="1" data-topic="33212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a8b319/48.png" class="avatar"> yevyevchungy:</div>
<blockquote>
<p>I am working with CT data (DICOM) and it takes ~8+ min just to load DICOM data that is already in my DICOM database. Once this data does load, I have noticed that some buttons/tools take an extremely long time to load/will simply cause an error, forcing me to quit the program.</p>
</blockquote>
</aside>
<p>First thing to consider whether that’s a cloud sync folder (google drive, dropbox, onedrive etc). We have seen strange slowness of data loading (particularly if the file themselves are pointers to actual data on the cloud, as opposed to being local. That means everything is downloaded from the cloud).</p>
<p>Once the import is completed, please report the volume dimension and data type (can be found under Volumes module).</p>
<p>Segmentation can use large amounts of RAM (8-10 times more than your volume size) transiently depending on the algorithm, but it shouldn’t take too long to initialize a new segmentation object. You don’t have a lot of memory, so make sure you are not running other memory intensive applications on your computer simulatenously (as memory is shared resource) and you don’t have anything else in your Slicer scene.</p>
<p>Barring our unusual data issues, yes, your simplest way forward is doing this on a computer with larger RAM. I suggest 64GB or more…</p>

---

## Post #6 by @lassoan (2023-12-05 20:45 UTC)

<aside class="quote no-group" data-username="yevyevchungy" data-post="4" data-topic="33212">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a8b319/48.png" class="avatar"> yevyevchungy:</div>
<blockquote>
<p>My datasets range from 6-9 GB in size</p>
</blockquote>
</aside>
<p>As <a class="mention" href="/u/muratmaga">@muratmaga</a> indicated, most processing algorithms require temporary buffers that may be several times larger than the input data set. Additional modified copies of the input data set may be needed for visualization. If you create a segmentation that requires storage that may require similar amount of memory as the input volume size, and if your segments may overlap then you may need a separate buffer for each segment. Therefore, to avoid performance degradation or running out of memory (which inevitably leads to crashes), I would recommend to <strong>use a computer that has 10x more RAM than the size of the data set you load</strong>. In this case, I would recommend to use a computer with 60-90GB RAM.</p>
<p><strong>If that is not feasible then you can reduce the size of your data set</strong> by 1-2 magnitudes by cropping it to the relevant region of interest and reduce its resolution. You can do both of these in <em>Crop volume</em> module. For example, if the size of the region of interest is 1/3 of your full image size then you can reduce memory need by a factor of 27x by cropping to that region; if half resolution is sufficient to see all relevant details then you can further reduce the memory need by 8x. These combined provide a 216x reduction of memory need. So, instead of 90GB RAM, you would just need 0.5GB RAM.</p>

---
