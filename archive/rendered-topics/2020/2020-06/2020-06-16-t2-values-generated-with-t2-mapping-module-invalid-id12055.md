# T2-values generated with T2-mapping module invalid?

**Topic ID**: 12055
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/t2-values-generated-with-t2-mapping-module-invalid/12055

---

## Post #1 by @KatS (2020-06-16 12:29 UTC)

<p>Dear Slicer community,<br>
I came across a problem when using the T2 mapping extension for mouse brain data acquired on a 9.4T Bruker scanner (MSME sequence with 30 echo times).<br>
I loaded Bruker DICOM files via the MultiVolumeImporter PlugIn as “30 frames MultiVolume by EchoTime” and used this as input in the T2 mapping-Module. I generated a T2-map with thresholds of 0.1 for R^2 and 300 for T2. The output looks reasonable.<br>
I then wanted to extract the actual T2-values for different anatomical regions. I used Segment editor for segmentation and Segment statistics. The values displayed in the table however seem to be incorrect and do not match the values expected from the literature or derived from Bruker’s Paravision analysis tool: mean values for different structures (i.e. cortex and CSF) are roughly the same and higher than they should be.<br>
Has anyone experience with this? Is there anything I need to do in a different way? I assume it has something to do with how the map is calculated, but am not sure about that.<br>
Thanks a lot for your help in advance!!!</p>

---

## Post #2 by @lassoan (2020-06-16 13:23 UTC)

<p>Bruker scanners are well known to produce inconsistent and incorrect DICOM outputs (you can read about frustration of Bruker users <a href="https://github.com/neurolabusc/Bru2Nii/">here</a>). Most probably you need to fix <code>MultiVolume.FrameLabels</code> values in Data module “MRML node information” section.</p>

---

## Post #3 by @KatS (2020-06-16 14:43 UTC)

<p>Thanks for the fast reply! Yes, I’m aware of the issues with Bruker DICOMS unfortunately.<br>
I checked MultiVolume.FrameLabels values and these were the echo times in ascending order, which I think is correct. Or should it be something different?<br>
Additionally, when looking at the imported images in MultiVolume Explorer, they appear to be fine.<br>
Could there be a problem when Bruker files are used for the calculation of the T2 map in the T2-mapping extension?</p>

---

## Post #4 by @lassoan (2020-06-16 17:20 UTC)

<p>This is a Python-scripted module, so you can inspect and modify the code very easily.</p>
<p>The source code is available here: <a href="https://github.com/gattia/Slicer-T2mapping/blob/master/T2mapping/T2mapping.py#L223-L298">https://github.com/gattia/Slicer-T2mapping/blob/master/T2mapping/T2mapping.py#L223-L298</a>. The computation part is quite short and has lots of comments, and high-level overview is also given in the <a href="https://github.com/gattia/Slicer-T2mapping">module documentation</a>, so you should be able to tell if the computation is correct.</p>
<p>If you enable developer mode in Slicer application settings and restart the application then “Edit” button will appear in the modue, which you can use to open the source code in a text editor. After making changes, you just need to click “Reload” button.</p>

---

## Post #5 by @KatS (2020-06-22 15:00 UTC)

<p>Thanks for the reply! I was able to figure out how the computation is done, but I’m afraid that it might not be working well for my data.<br>
Is there a way to display a plot with the fit or an error map?</p>
<p>Hitting the “Edit” button in developer mode does not open the code in a text editor. Is there anything else apart from enabling developer mode and restart Slicer to use this function?</p>

---

## Post #6 by @lassoan (2020-06-23 21:58 UTC)

<aside class="quote no-group" data-username="KatS" data-post="5" data-topic="12055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/a8b319/48.png" class="avatar"> KatS:</div>
<blockquote>
<p>Hitting the “Edit” button in developer mode does not open the code in a text editor</p>
</blockquote>
</aside>
<p>Make sure .py fine extension is associated with a text editor. But you don’t need to use this convenience feature, you can open the module’s .py file manually (you can find its location in the application log).</p>
<aside class="quote no-group" data-username="KatS" data-post="5" data-topic="12055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/a8b319/48.png" class="avatar"> KatS:</div>
<blockquote>
<p>Is there a way to display a plot with the fit or an error map?</p>
</blockquote>
</aside>
<p>I don’t think the module offers this, but you can create plots yourself. See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plotting" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>.</p>
<p>Would you like to plot intensity values at specific positions?</p>

---

## Post #7 by @gattia (2021-09-01 04:00 UTC)

<p><a class="mention" href="/u/kats">@KatS</a> Im the developer of that module and just came across this post. Did you figure out the problem? It could be that for some reason your data wasn’t playing nicely with the linear fit method (log transform the data and then fit a linear equation). I’d be interested in helping out to make sure this works for others.</p>

---
