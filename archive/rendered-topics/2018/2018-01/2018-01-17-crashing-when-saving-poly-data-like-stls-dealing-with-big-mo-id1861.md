# Crashing when Saving Poly Data (like STLs), Dealing with Big Models

**Topic ID**: 1861
**Date**: 2018-01-17
**URL**: https://discourse.slicer.org/t/crashing-when-saving-poly-data-like-stls-dealing-with-big-models/1861

---

## Post #1 by @aiNeander (2018-01-17 03:25 UTC)

<p>Hi!</p>
<p>I’ve been struggling to get a complex model out of slicer and am looking for suggestions. The model is intentionally complex -  a didelphis skull with the nasal turbinates intact. I know this will result in a high poly model. I’ve also come to the acceptance that Slicer just can’t handle big or complex models, so I’ve been cutting it down with the intention of booleaning them together in post (fingers crossed). Still, even with cut down models, I’m having problems. I can get the model to export to a new ModelHierarchy, but as soon as I try to save the model, it crashes. Cutting down the model into smaller pieces at least allows the model to save, but then crashes immediately after.</p>
<p>Is there a way to reduce poly count in Slicer? Any other suggestions about how to get big models out of Slicer?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2018-01-17 05:16 UTC)

<p>Do you segment using Segment Editor module? Which Slicer version do you use? On what operating system? How much physical RAM do you have? How much virtual memory have you configured in your operating system?</p>
<aside class="quote no-group" data-username="aiNeander" data-post="1" data-topic="1861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>I’ve also come to the acceptance that Slicer just can’t handle big or complex models</p>
</blockquote>
</aside>
<p>Slicer, as all other software, will stop working if you run out of memory. If you cannot add more physical RAM and cannot reduce data size then increase virtual memory size (processing may get much slower but you won’t run out of memory). I would recommend to have 10x more memory space than raw data size. For example, if your input volume size is 4GB then have at least 40GB memory space available for the application; it could be 16GB physical and 30GB virtual.</p>
<aside class="quote no-group" data-username="aiNeander" data-post="1" data-topic="1861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>as soon as I try to save the model, it crashes</p>
</blockquote>
</aside>
<p>Increasing physical memory size should fix that. Or crop the volume before segmentation, using Crop volume module.</p>
<aside class="quote no-group" data-username="aiNeander" data-post="1" data-topic="1861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/48db29/48.png" class="avatar"> aiNeander:</div>
<blockquote>
<p>Is there a way to reduce poly count in Slicer?</p>
</blockquote>
</aside>
<p>To reduce polygon count, go to Segmentations module, in Representation section / Closed surface row, click Update, click Binary labelmap → Closed surface rule, set decimation factor to 0.8 (the higher the value, the more reduction will occur, but it may cause visible changes in the mesh).</p>

---

## Post #3 by @hherhold (2018-01-17 12:29 UTC)

<p>Just as a benchmark, I have a few micro-CT insect segmentations that result in models around 65 million triangles. This is on a MacBook Pro with 16 gig of ram - this is seriously straining the upper limit of my machine, but it’s doable.</p>

---

## Post #4 by @muratmaga (2018-01-17 20:50 UTC)

<p>April,</p>
<p>I have a 1024^3 voxel adult didelphis scan (with all the turbinates intact as wel) that I can convert to an polygon model in about 10 minutes on my laptop with 16GB. As <a class="mention" href="/u/lassoan">@lassoan</a> asked we need slicer version, your OS, RAM etc details to help you with your issues.</p>
<p>M</p>

---

## Post #5 by @aiNeander (2018-01-18 03:33 UTC)

<p>Hi All,</p>
<p>Thanks for your feedback.</p>
<p>lassoan,<br>
These are my specs (taken from the last Problem Report)<br>
Model: MacBookPro11,3, BootROM MBP112.0138.B18, 4 processors, Intel Core i7, 2.3 GHz, 16 GB, SMC 2.19f12<br>
Graphics: Intel Iris Pro, Intel Iris Pro, Built-In<br>
Graphics: NVIDIA GeForce GT 750M, NVIDIA GeForce GT 750M, PCIe, 2048 MB<br>
my virtual memory is 9.9G, minus reserved VM space is 8.0G<br>
I am using Slicer 4.9.0-2018-01-07, though I have a couple older versions on here too.</p>
<p>The dataset I’m using came from a micro-CT with 2024 pixel panel, though the dataset was cropped at processing so isn’t quite 2024^3. I down-sampled this dataset to 8bit jpeg and the total dataset is 323.3MB. The .nrrd volume from this stack is 921.8MB.</p>
<p>As for using Closed surface rule to decrease poly count, I can’t get that far. I have to hit “create” first, and seconds after the model is created, Slicer crashes.<br>
<em>update</em> just found that by holding the “create” button I can access the decimation factor without creating it first. I am trying it out now.</p>
<p>hherhold, 65 million triangles! I am impressed! Hopefully I can make that work too!</p>
<p>muratmaga, if it took 10 minutes, then it is possible I’m not giving it enough time. The rainbow wheel stopped spinning for me after a few minutes and I just assumed it was done, but that’s when it would crash after hitting save. Perhaps the rainbow wheel is misleading and it is not in fact done processing?</p>

---

## Post #6 by @lassoan (2018-01-18 03:51 UTC)

<p>It’s very important to clearly distinguish between application crash and hang. Crash means that the application exits, you get an error message, etc. Hang means that the application becomes temporarily non-responsive, but if it does not crash then it should eventually recover.</p>

---

## Post #7 by @aiNeander (2018-01-18 04:01 UTC)

<p>Hi lassoan,</p>
<p>It very definitely crashes, with an error report and need to reopen. In the last bit of my message, I was wondering if the crash is due to the model still being built in the background, when there is no indication that there is still a process going on. Said differently, I may have been starting a second process when the first wasn’t finished, because it seemed finished.</p>
<p>Another reason it may have crashed is that I hadn’t built the model yet and was trying to export it. I assumed it would do it all at once, though I’m not sure that is true now.</p>
<p>That being said, I think decimation is going to be a very helpful tool! I was able to build the model in about 3 minutes and successfully save and export it.</p>
<p>I’m curious if hherhold uses decimation to make his 65 million poly models work? Or what other techniques he uses to work with such large models?</p>
<p>Thanks again,<br>
April</p>

---

## Post #8 by @hherhold (2018-01-18 12:02 UTC)

<p>Hi April,</p>
<p>I do not decimate my models - yet, although I’m seriously considering something like ZBrush for post-processing and selective decimation. I’m nearly always tweaking my workflow in some way or another, as my laptop is maxed out and I can’t install more ram. When I’m working with large models, I usually do model making as the very last step, then export to PLY for use in Blender - I don’t spend a lot of time working on the actual polygon model in Slicer.</p>
<p>I also look at my models in ParaView, which does a very good job at visualizing large poly models (and can import just about anything).</p>
<p>You mentioned that you have 8G reserved for VM - are you running slicer native in MacOS or in a virtual machine like VMWare?</p>
<p>-Hollister</p>

---

## Post #9 by @muratmaga (2018-01-18 16:01 UTC)

<p>To clarify, it took 10 minutes to do the entire thing (load image stack, segment via threshold in segment editor, convert segmentation to model and then save). Perhaps about 1m (possibly less) for just saving…. You can try it yourself with the data from<br>
<a href="http://digimorph.org/specimens/Didelphis_virginiana/" rel="nofollow noopener">http://digimorph.org/specimens/Didelphis_virginiana/</a> (click CT scan link). This is an 8 bit dataset ~1024x1024x750, a bit smaller than yours. It used about 12GB of RAM during the processing.</p>
<p>Steps were:<br>
load slices (when imported, voxel sizes are wrong, but doesn’t matter for what you want to try)<br>
Segment Editor Threshold 35-255<br>
Segmentations module (scroll down to find, convert segmentation to models option)<br>
Save polydata (STL) format.</p>
<p>Your own dataset size should be within the RAM constrains of your laptop (though I did not understand the bit reserving 8GB for vm. Slicer is likely to crash via lack of RAM with this dataset if it is running under a VM provisioned with 8GB of RAM. ). Not being a mac user, I can’t comment on how, but you may want to look at the memory usage during your tasks. Slicer is so stable with any size of dataset (when provided with sufficient resources) and you are using such a core functionality, I’d say your crash is a memory related issue.</p>
<p>Again the rule of thump is to 10X more memory available to Slicer (which is not the same thing as having 10X memory installed on your computer due to usage by OS, other programs, vms etc running).</p>

---
