# Problems with a microtomography and growing from seeds

**Topic ID**: 43681
**Date**: 2025-07-10
**URL**: https://discourse.slicer.org/t/problems-with-a-microtomography-and-growing-from-seeds/43681

---

## Post #1 by @JaredAmudeo (2025-07-10 19:33 UTC)

<p>Hello! I need a little help understanding the ideal hardware for this feature to work quickly, or fast enough. On my personal computer, I haven’t had any “issues” with files requiring more RAM than I have, and when I do, it takes longer, which is normal since it exceeds my current memory.<br>
I’m currently segmenting fossils still within sediment. This corresponds to a stack of TIF images obtained from a microtomograph with the following specifications: KV 195, uA 128, and 0.15 mm pixel size.<br>
The problem is that for each bone I want to segment using this feature, and after cropping it so my computer can handle it, it takes more than 30 minutes, reaching up to 45 minutes. I tried on another Windows PC with 128GB of RAM and a Mac with 192GB, so memory was no longer a limitation. However, I got very similar results to those on my PC; in short, it was still taking a long time.</p>
<p>Is there a way to speed up the process without using more RAM in this case or without cropping the volume again? I’ve seen that when I segment using this tool, sometimes the segment used as a background remains well-defined and occupies a small, well-defined portion, but other times it occupies the entire tomography despite having a clear and well-defined outline. Could that have something to do with it? I’ve also disabled the 3D view to load faster, but I don’t see any improvement. Or is there a possibility and possible improvement by involving the GPU in some way?</p>
<p>Thank you very much in advance.</p>
<p>Here are the specifications of the PCs I have access to to work with this dataset:<br>
The current .nrrd file is 2.7 GB.<br>
Own: Windows 11, 32 GB DDR5 5600 MHz RAM, Intel i5-14600kf, and RTX 4070ti Super.<br>
Lab 1: Lenovo ThinkStation, Windows 11, 128 GB DDR4 2400 MHz RAM, Intel Xeron Silver 4208, and RTX A5000.<br>
Lab 2: Mac Studio, macOS Sequoia 15.3.2, 195 GB LPDRR5 RAM, Apple M2 Ultra.</p>

---

## Post #2 by @muratmaga (2025-07-10 20:14 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="1" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>I’m currently segmenting fossils still within sediment. This corresponds to a stack of TIF images obtained from a microtomograph with the following specifications: KV 195, uA 128, and 0.15 mm pixel size.</p>
</blockquote>
</aside>
<p>How big are your microCT scans? Pixel size doesn’t tell us anything about the size of the data?</p>
<aside class="quote no-group" data-username="JaredAmudeo" data-post="1" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>I’m currently segmenting fossils still within sediment.</p>
</blockquote>
</aside>
<p>This is a challenging segmentation because there is probably an intensity gradation from your fossils to the sediment around it. But hard to tell without looking at your data.</p>
<aside class="quote no-group" data-username="JaredAmudeo" data-post="1" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>Is there a way to speed up the process without using more RAM in this case or without cropping the volume again?</p>
</blockquote>
</aside>
<p>If your volume is big, and the structures you are trying to segment are not continuous across the volume, then the biggest imrpovement you can do is to create subvolumes that only contain what you want to segment (for example if you are goal is to segment hand bones, do not have the thorax in the field of view). Because everything in Slicer in physical space, you can then move/copy segments to one segmentation.</p>
<p>Also give SlicerNNinteractive extension a try. It works really well as replacement for grow from the seeds (just make sure you downsample the data to match your GPU).</p>

---

## Post #3 by @JaredAmudeo (2025-07-10 20:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>How big are your microCT scans? Pixel size doesn’t tell us anything about the size of the data?</p>
</blockquote>
</aside>
<p>It is 2.7 gb of size</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If your volume is big, and the structures you are trying to segment are not continuous across the volume, then the biggest imrpovement you can do is to create subvolumes that only contain what you want to segment (for example if you are goal is to segment hand bones, do not have the thorax in the field of view). Because everything in Slicer in physical space, you can then move/copy segments to one segmentation.</p>
</blockquote>
</aside>
<p>I’ve thought about doing the subvolumes, although it’s a bit tedious. I don’t know if it will be viable because the bones are scattered throughout the rock matrix. The animal is complete but disarticulated, and it would be a good idea for me to segment and export all the models in position so I can then rework them in Blender.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also give SlicerNNinteractive extension a try. It works really well as replacement for grow from the seeds (just make sure you downsample the data to match your GPU).</p>
</blockquote>
</aside>
<p>This is the first time I’m reading about this extension. How does it work? My GPU has 16GB of VRAM. Would I have to lower the resolution, for example, to make it fit as you say?<br>
I’m thinking about using the Slicemorph module, importing the image stack at half the resolution instead of full, and re-cropping it to fit the threshold. I don’t know how much information I’d lose by lowering the detail.<br>
Isn’t there a way to involve the GPU in the “normal” process of how Grown from Seeds works?</p>

---

## Post #4 by @JaredAmudeo (2025-07-10 21:33 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This is a challenging segmentation because there is probably an intensity gradation from your fossils to the sediment around it. But hard to tell without looking at your data.</p>
</blockquote>
</aside>
<p>I managed to reduce it to a couple of seconds, but by halving the quality, the result isn’t working. I lose a lot of detail, and the pieces are even millimetric. I tried installing the extension you mentioned, but none of it loads. I don’t know what’s going on. I’m using version 5.7.0.</p>

---

## Post #5 by @muratmaga (2025-07-10 22:46 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="4" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>’m using version 5.7.0.</p>
</blockquote>
</aside>
<p>NNinteractive is only available for slicer’s preview version from last couple months. Try with the latest preview.</p>

---

## Post #6 by @JaredAmudeo (2025-07-11 04:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>NNinteractive is only available for slicer’s preview version from last couple months. Try with the latest preview.</p>
</blockquote>
</aside>
<p>After following the server installation guide, I’m getting errors trying to run it. Do you know how to fix this?<br>
“Failed to connect to server ‘<a href="http://localhost:1527" rel="noopener nofollow ugc">http://localhost:1527</a>’. Please make sure the server is running and check the server URL in the ‘Configuration’ tab.”</p>
<p>The first command line executes successfully: “powershell -ExecutionPolicy ByPass -c “irm -useb <a href="https://pixi.sh/install.ps1" rel="noopener nofollow ugc">https://pixi.sh/install.ps1</a> | iex””</p>
<p>The second line gives me an error in this section:</p>
<p>PS C:\Users\jared&gt; cd /d %localappdata%<br>
Set-Location: No location parameter found that accepts the argument ‘%localappdata%’.<br>
Line: 1 Character: 1</p>
<ul>
<li>cd /d %localappdata%</li>
<li>
<pre><code class="lang-auto"></code></pre>
</li>
<li>CategoryInfo: InvalidArgument: (<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> [Set-Location], ParameterBindingException</li>
<li>FullyQualifiedErrorId: PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand</li>
</ul>
<p>and therefore when starting the server I get this error:<br>
PS C:\Users\jared&gt; cd /d %localappdata%\nninteractive-server.pixi\envs\default\Scripts<br>
Set-Location: No position parameter found that accepts the argument<br>
‘%localappdata%\nninteractive-server.pixi\envs\default\Scripts’.<br>
On line: 1 Character: 1</p>
<ul>
<li>cd /d %localappdata%\nninteractive-server.pixi\envs\default\Scripts</li>
<li>
<pre><code class="lang-auto"></code></pre>
</li>
<li>CategoryInfo: InvalidArgument: (<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> [Set-Location], ParameterBindingException</li>
<li>FullyQualifiedErrorId: PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand</li>
</ul>
<p>PS C:\Users\jared&gt; pip install nninteractive-slicer-server<br>
pip: The term ‘pip’ is not recognized as the name of a cmdlet, function, script file, or executable program.<br>
Check if you entered the name correctly, or if you included a path, verify that the path is correct and try again.<br>
On Line: 1 Char: 1</p>
<ul>
<li>pip install nninteractive-slicer-server</li>
<li>
<pre><code class="lang-auto"></code></pre>
</li>
<li>CategoryInfo: ObjectNotFound: (pip:String) <span class="chcklst-box fa fa-square-o fa-fw"></span>, CommandNotFoundException</li>
<li>FullyQualifiedErrorId: CommandNotFoundException</li>
</ul>
<p>PS C:\Users\jared&gt; nninteractive-slicer-server --host 0.0.0.0 --port 1527</p>

---

## Post #7 by @muratmaga (2025-07-11 04:41 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="6" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>PS C:\Users\jared&gt; cd /d %localappdata%<br>
Set-Location: No location parameter found that accepts the argument ‘%localappdata%’.<br>
Line: 1 Character: 1</p>
</blockquote>
</aside>
<p>Nowadays I don’t use windows as much, but if I were to guess you were running this inside the powershell instead of the terminal windows (command console) as instructed. I have not tried using this on windows.</p>
<p>You can also try on MorphoCloud (<a href="https://instances.morpho.cloud">https://instances.morpho.cloud</a>) far more straightforward to set it up.</p>

---

## Post #8 by @JaredAmudeo (2025-07-11 06:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Nowadays I don’t use windows as much, but if I were to guess you were running this inside the powershell instead of the terminal windows (command console) as instructed. I have not tried using this on windows.</p>
</blockquote>
</aside>
<p>Aaah! I found the error, you were absolutely right. Thank you so much. I misinterpreted it, there were some interpretation issues when translating, haha. I only have one question, and it seems it doesn’t support CUDA. Is there any way to fix this?</p>

---

## Post #9 by @muratmaga (2025-07-11 06:26 UTC)

<p>It uses cuda? if it is not working,</p>
<p>it may not be bringing in right combination of torch and cuda libraries, or you might have some issues with your Nvidia driver? again I find getting deep-learning tools working correctly on windows quite difficult, I suggest you try the MorphoCloud or use a Linux machine locally if you can.</p>

---

## Post #10 by @JaredAmudeo (2025-07-11 06:41 UTC)

<p>It uses the CPU, but I want it to use the GPU.</p>
<p>Everything’s up to date. I have CUDA 12.9, so maybe the combination of CUDA and Torch isn’t right. I don’t understand how this actually works; it’s new to me, but I’ll have to figure it out somehow to see if I can improve the segmentation speed.</p>

---

## Post #11 by @muratmaga (2025-07-11 15:42 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="10" data-topic="43681">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>It uses the CPU, but I want it to use the GPU.</p>
</blockquote>
</aside>
<p>Again I do not know about windows environment that much. This tells me the server installation is not detecting the GPU for one reason or the other.</p>

---

## Post #12 by @JaredAmudeo (2025-07-12 21:35 UTC)

<p>Well, after trial and error, I managed to make it compatible with CUDA and have it detect the GPU. However, NNInteractive Slicer doesn’t have CUDA compatibility on Pixi, and it’s not viable with a CPU. Thanks anyway.</p>

---

## Post #13 by @muratmaga (2025-07-12 22:35 UTC)

<p>I am pretty sure quite a few people are using the nninteractive with cuda and gpu on windows. Not sure if they are doing it via docker or pixi.<br>
Hopefully one of them can chime i .</p>

---

## Post #14 by @pieper (2025-07-12 23:08 UTC)

<p>We use nnInteractive on windows.  It was just a regular pip install as documented on the github page.  It might have been pixi or venv, I don’t recall but I also don’t think it matters.</p>

---

## Post #15 by @JaredAmudeo (2025-07-13 23:15 UTC)

<p>Update<br>
There’s something about microtomography that makes it take so long. I tested how long Grown from Seeds took with another image stack weighing approximately 9GB at full resolution, and it took less than two minutes.</p>

---

## Post #16 by @muratmaga (2025-07-14 02:56 UTC)

<p>There should be nothing “special” about microCT data. However, if you can share your data, and the seeds you are trying to grow from, I can take a look…</p>

---
