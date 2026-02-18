# SlicerRT Batch Conversation Memory issue

**Topic ID**: 13026
**Date**: 2020-08-16
**URL**: https://discourse.slicer.org/t/slicerrt-batch-conversation-memory-issue/13026

---

## Post #1 by @kleingeo (2020-08-16 17:26 UTC)

<p>I am trying to use the batch conversion tool with SlicerRT and I’ve been getting memory issues. I am trying to use it to convert label maps from a Struct file and an accompanying CT scan. Is there any reason why I would be getting this type of issue and how much computation memory is required? I am running it on a PC with 32 GB of RAM, so not an insignificant amount.</p>

---

## Post #2 by @lassoan (2020-08-16 17:31 UTC)

<p>If you set a large oversampling value, extents are large, or you have many segments then memory usage can be excessive.</p>
<p>Try latest Slicer Preview Release, as it contains many memory optimizations.</p>
<p>If you still have issues then attach the application log (menu: Help / Report a bug) obtained with latest Slicer Preview Release.</p>

---

## Post #3 by @kleingeo (2020-08-16 17:42 UTC)

<p>I’m using one of the lastest nightly previews to do it (maybe just a week ago). I’m not sure what the issue is, or if it is a slicer bug, a bug with the extension, or if this behaviour is expected.</p>

---

## Post #4 by @lassoan (2020-08-16 18:20 UTC)

<p>Attach the application log (menu: Help / Report a bug) of a session where you run out of memory. It may help us to answer what causing the issue and how to resolve it.</p>

---

## Post #5 by @kleingeo (2020-08-16 18:26 UTC)

<p>I have the log, what is the best way to share it (its too large to copy-and-paste)?</p>

---

## Post #6 by @lassoan (2020-08-16 18:30 UTC)

<p>You can use <a href="https://gist.github.com/">https://gist.github.com/</a> or any cloud storage provider (Dropbox, OneDrive, Google drive, etc) and post the link here.</p>

---

## Post #7 by @kleingeo (2020-08-16 18:31 UTC)

<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/kleingeo/eaa06ae63d525c00be7f7e2e0841fcd2" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/kleingeo/eaa06ae63d525c00be7f7e2e0841fcd2" target="_blank" rel="nofollow noopener">https://gist.github.com/kleingeo/eaa06ae63d525c00be7f7e2e0841fcd2</a></h4>
<h5>slicerRT_batch_conversion_error_log</h5>
<pre><code class="">[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Session start time .......: 2020-08-16 14:13:38
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Slicer version ...........: 4.11.0-2020-08-15 (revision 29281 / 0525461) win-amd64 - installed release
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Memory ...................: 32679 MB physical, 37543 MB virtual
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 7 3800X 8-Core Processor             , 16 cores, 16 logical processors
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 16.08.2020 14:13:38 [] (unknown:0) - Application path .........: D:/NA-MIC/Slicer 4.11.0-2020-08-15/bin</code></pre>
This file has been truncated. <a href="https://gist.github.com/kleingeo/eaa06ae63d525c00be7f7e2e0841fcd2" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @lassoan (2020-08-16 19:07 UTC)

<p>Thank you, these logs are already useful, but it is hard to tell for sure what’s wrong. Can you share the structure set files (of anonymized or phantom data sets)?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do any of the errors shown in the log look familiar to you?</p>

---

## Post #9 by @Sunderlandkyl (2020-08-16 21:15 UTC)

<p>No, it’s not an error that I’ve seen before.</p>

---

## Post #10 by @cpinter (2020-08-17 12:14 UTC)

<p>Is this something that occurs with any data you want to convert or one specific dataset?</p>

---

## Post #11 by @kleingeo (2020-08-17 14:39 UTC)

<p>Here is a link to the file. Sorry for the delay, I just had to make sure the file was properly deidentified.</p>
<p><a href="https://utoronto-my.sharepoint.com/:u:/g/personal/geoff_klein_mail_utoronto_ca/Eeb1--vk2S1GpMu4sOfO-ekBL94v_pzPEkTaft12_W2p-w?e=Qj41Ob" class="onebox" target="_blank" rel="nofollow noopener">https://utoronto-my.sharepoint.com/:u:/g/personal/geoff_klein_mail_utoronto_ca/Eeb1--vk2S1GpMu4sOfO-ekBL94v_pzPEkTaft12_W2p-w?e=Qj41Ob</a></p>

---

## Post #12 by @kleingeo (2020-08-17 14:47 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="13026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>his something that occurs with any data you</p>
</blockquote>
</aside>
<p>I’ve only been trying right now with a specific dataset, I haven’t tried with others. That being said, there shouldn’t be anything specifically different with this dataset compared to others I have.</p>

---

## Post #13 by @Sunderlandkyl (2020-08-17 15:20 UTC)

<p>What is the resolution of the accompanying CT scan?</p>

---

## Post #14 by @kleingeo (2020-08-17 15:48 UTC)

<p>The CT scan is a 512 x 512 x 296 volume with voxel spacing 1.171 x 1.171 x 1 mm^3</p>

---

## Post #15 by @cpinter (2020-08-17 15:59 UTC)

<aside class="quote no-group" data-username="kleingeo" data-post="14" data-topic="13026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>512 x 512 x 296</p>
</blockquote>
</aside>
<p>That is quite standard, it shouldn’t be a problem.</p>
<aside class="quote no-group" data-username="kleingeo" data-post="12" data-topic="13026">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>there shouldn’t be anything specifically different with this dataset compared to others I have</p>
</blockquote>
</aside>
<p>I wouldn’t be so sure. Maybe there is somethig going on with one of the contours that confuses our conversion algorithm and makes it allocate way too much memory.</p>
<p>Thanks for the data! I think the only way to see it is to try it ourselves. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you have some time checking it out? You know way more about the contour conversion algorithm specifically, so if my hunch is right then you’re in a better position to find out the root of the problem. Please let me know if you don’t, and then I’ll give it a go when I can.</p>

---

## Post #16 by @kleingeo (2020-08-17 16:01 UTC)

<p>I know in the Struct file there are a lot of contours. However, there are only a few that I am actually interested in. Is there a way in the batch conversion tool to specify which labels I am actually interested in?</p>

---

## Post #17 by @Sunderlandkyl (2020-08-17 16:05 UTC)

<p>Yes, I can take a look at it.</p>
<p>I’ve already looked at the contour to surface conversion in Slicer, and some of the structures were not converted correctly.<br>
I think this is causing some additional issues in the closed surface to binary labelmap conversion, but I’ll debug and find out.</p>

---

## Post #18 by @Sunderlandkyl (2020-08-18 15:06 UTC)

<p>The following structures: TS+2mmring, TS+4mmring, outer tissue ring, and bowel max20 are all not triangulated correctly from the contours, however that doesn’t seem to be the issue.</p>
<p>2 things seem to be happening:</p>
<ul>
<li>The memory usage when collapsing the binary labelmaps to a single layer is very high</li>
<li>After collapsing the labelmaps, the closed surface to binary labelmap conversion is run again.</li>
</ul>
<p>I’m working on a fix.</p>

---

## Post #19 by @Sunderlandkyl (2020-08-18 19:00 UTC)

<p>This should be fixed in tomorrows preview release (<a href="https://github.com/SlicerRt/SlicerRT/commit/c4fe6c54c0b3269ba24a46f7d72967d5d132c976" rel="nofollow noopener">c4fe6c5</a>).<br>
The reference geometry wasn’t being applied to the segmentation.</p>

---
