# Long delay after disk activity stops when loading very large data

**Topic ID**: 13452
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/long-delay-after-disk-activity-stops-when-loading-very-large-data/13452

---

## Post #1 by @jamesjcook (2020-09-11 21:08 UTC)

<p>I’m using slicer to work with very large files. After disk activity stops, there is a (surprisingly) long delay before the volume shows up in viewers.<br>
Disk time to load is a few minutes, the delay after that has been as long as 40 minutes.<br>
One cpu core is busy during this long delay time.</p>
<p>I think it is the min/max calculation, but i’m not currently in a position to verify that.</p>
<p>Is there a way to skip the min/max calc on load, or are there bare-bones programmatic ways to load which don’t do any processing?</p>

---

## Post #2 by @lassoan (2020-09-11 21:13 UTC)

<p>Min/max computation may add significant amount of time (maybe up to a few ten %) but not something like 4000%. Could you attach the header of your image file in nhdr format?</p>
<p>Slicer retrieves min/max scalar value from some file formats that supports this, this saving some loading time, but the drastic slowdown you are experiencing is probably due to some other issue.</p>

---

## Post #3 by @muratmaga (2020-09-11 21:21 UTC)

<p>Are your files compressed? I think slicer reads, and then uncompresses everything as oppose to stream. For files in the order of 10GB, these had been in dozens of minutes range for me…</p>

---

## Post #4 by @jamesjcook (2020-09-11 21:27 UTC)

<p>This was tried with and without compression. Compression is also a serious detriment in loading these, when used with a single data file this took hours to load, my memory is 7, but I didnt find my record of it. When using multiple compressed files, (one per slice) loading time was very long, but could be accomplished in one working day. I didnt time that, i started loading in the morning and it was ready at lunch time.</p>
<pre><code>type: unsigned short
dimension: 3
space: right-anterior-superior
sizes: 6263 10186 2621
space directions: (0.0018,0,0) (0,0.0018,0) (0,0,0.0040)
kinds: domain domain domain
endian: big
encoding: raw
space origin:(-5.36155006705028,	-9.68239733742919,	-4.23750168693362)
data file: big.dat</code></pre>

---

## Post #5 by @muratmaga (2020-09-11 22:13 UTC)

<p>I have noticed a delay between the end of the loading my large NRRD files (not compressed) and the appearance of  slice views, which can be a minute or two (never really timed either). I always assumed those are overheads associated with generating MRML nodes etc. But I never tested with such large dataset, my large files are 10-20GB range. Yours is almost 400GB.</p>

---

## Post #6 by @lassoan (2020-09-12 04:02 UTC)

<p>I’ve tested loading of a 6.4GB uncompressed NRRD file and only a few seconds passed after file loading finished:</p>
<ul>
<li>While cold loading of the file (after computer restarted), resource monitor showed 100MB/sec disk activity for about 64 seconds. A few seconds after disk activity went down to zero, the image appeared.</li>
<li>While warm loading the file (loading it again right after it was loaded), resource monitor did not show any activity and image appeared in 6 seconds.</li>
</ul>
<p>A few things that would be nice if you could do to diagnose what’s happening:</p>
<ol>
<li>
<p>Disk activity light is not reliable source of information. If you use a resource monitor that shows the actual disk transfer then you will know if data is actually read. Note that if you load a recently loaded file then it may be retrieved from memory instead of re-reading from disk, so you cannot blindly trust resource monitors either.</p>
</li>
<li>
<p>Your image is stored as big endian, so each value has to be byte-swapped after loading. It should not cause significant delay but it may worth a try to save the image (as it is saved as little endian) and see if loading this image is any faster.</p>
</li>
<li>
<p>You may try to instantiate a simple NRRD reader and see if it makes loading any faster:</p>
</li>
</ol>
<pre><code class="lang-python">volumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
storageNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLNRRDStorageNode")
storageNode.SetFileName("path/to/your/file.nhdr")
storageNode.ReadData(volumeNode)
setSliceViewerLayers(volumeNode)
</code></pre>

---

## Post #7 by @jamesjcook (2020-09-12 04:31 UTC)

<p>The disk activity i’m referring to is the read activity in windows server 2016 process monitoring, specifically watching the open file listing, on big.dat.</p>
<p>I have a significant processing chain problem because ImageJ saves big endian, hopefully thats only a minor contributor to my load speed.</p>
<p>Thanks for the simple reader hint, I should get a change to test that next week.</p>

---

## Post #8 by @lassoan (2020-09-12 04:48 UTC)

<p>You can also try <a href="http://www.codersnotes.com/sleepy/">VerySleepy</a> tool, which provides you function list and call stacks of methods that the application spends the most time with. For release-mode builds, without debug information, the data is not fully reliable but often gives useful hints about what the application does.</p>
<p>Instead of just watching the open file listing, use a tool that gives you real-time information about the amount of data transfer (such as Resource Monitor or Performance Monitor). You can then check if the disk activity makes sense (time x bandwidth should equal file size).</p>

---

## Post #9 by @aiden.zhu (2021-12-13 21:42 UTC)

<p>@ <a href="https://discourse.slicer.org/u/lassoan">lassoan</a><br>
I do have large data as well. I tried this way to load data, but seems the data were not read in. Need I do some command to execute or force the data read from the local disk?<br>
Thanks a lot.</p>
<p>==&gt;<br>
volumeNode=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
storageNode=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLNRRDStorageNode”)<br>
storageNode.SetFileName(“path/to/your/file.nhdr”)<br>
storageNode.ReadData(volumeNode)<br>
setSliceViewerLayers(volumeNode)</p>

---

## Post #10 by @jamesjcook (2021-12-14 16:40 UTC)

<p>When that happens to me, it is generally because I wrote my nhdr file incorrectly.<br>
You can see slicer errors in the slicer log. Errors don’t always get from the python console to the main slicer log.</p>
<p>On the bottom right corner of the slier interface there is a circle with an X in it.<br>
The circle is grey normally, if the circle is red, there has been an error.</p>
<p>Click the circle to open the log. You can do this before loading your data and “clear” the current messages to make it easier to see your errors.</p>

---

## Post #11 by @aiden.zhu (2021-12-14 19:18 UTC)

<p>Hi James,<br>
I got no problem to load data actually. But while I tried the method (with codes mentioned by <a class="mention" href="/u/lassoan">@lassoan</a> ), all shows fine but just no data does get loaded into Slicer.</p>
<p>My purpose is to check if it’s faster via <a class="mention" href="/u/lassoan">@lassoan</a>’s codes or no, since I am doing the similar things as you do with huge data. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:"></p>
<p>PS: normally I do load data using slicer.util.loadVolume, which gets me sense slow loading.</p>

---

## Post #12 by @lassoan (2021-12-14 20:09 UTC)

<p>Loading should be fast if you store the images uncompressed. For most medical images, zlib compression only provides about 50% size reduction, so likely it is not worth the increased load time.</p>

---

## Post #13 by @jamesjcook (2021-12-15 01:29 UTC)

<p>I did my testing on 4.10.2 in 2020 and this helped a great deal. It also seemed to successfully get around a big part of the single threaded process which was happening to me after load.</p>
<p>I’ve got similar code running on 20200930 and 20210226 builds. I think those were full release versions. I’ve not tested these as extensively for run time.</p>
<p>The newer builds have been better behaved with my large data.</p>
<p>When you say “it seems the data was not read in” what do you mean exactly?<br>
It loads up instantly? or you have 0 for all voxels? or it is not displayed/all black?</p>
<p>(Also thank you Andras, this snippet you gave me has been exceedingly helpful. Sorry i lost track of this thread.)</p>

---

## Post #14 by @aiden.zhu (2021-12-16 16:12 UTC)

<p>Yeah, no data shown/displayed at all after I ran that code part. And I did not see any errors coming out. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
