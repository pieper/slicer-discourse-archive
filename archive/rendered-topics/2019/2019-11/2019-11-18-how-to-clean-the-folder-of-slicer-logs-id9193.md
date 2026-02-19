---
topic_id: 9193
title: "How To Clean The Folder Of Slicer Logs"
date: 2019-11-18
url: https://discourse.slicer.org/t/9193
---

# How to clean the folder of Slicer_Logs?

**Topic ID**: 9193
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/how-to-clean-the-folder-of-slicer-logs/9193

---

## Post #1 by @aiden.zhu (2019-11-18 15:07 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2019<br>
Expected behavior: Keep Slicer_Logs folder as small as possible<br>
Actual behavior: it is swelling after each usage</p>
<p>Hi All expertise in Slicer:<br>
I happened to see my C: drive space shrunk and then figure it out that users\Documents\Slicer_Logs folder having lots of history of my slicer usage.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f61a811c803289e7c62de29bc94c10829ea6f0d.png" data-download-href="/uploads/short-url/bkeWNfPPL0droS8vMGx6KDTgz81.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f61a811c803289e7c62de29bc94c10829ea6f0d.png" alt="image" data-base62-sha1="bkeWNfPPL0droS8vMGx6KDTgz81" width="401" height="500" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">478×595 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So how to keep it as small as possible? Is there any python/CLI functions so that I may clean it before or after each time usage?</p>
<p>Thanks a lot, Aiden</p>

---

## Post #2 by @jamesobutler (2019-11-18 15:37 UTC)

<p>I’m not familiar with this “Slicer_Logs” directory within Documents.  Did you go into Settings-&gt;Modules and change “Temporary Directory” from the default location of %LocalAppData%/Temp/Slicer ? This is where Slicer logs are typically found and are usually fairly small in size.</p>
<p>Did you change Settings-&gt;Cache which also has a default location of %LocalAppData%/Temp/Slicer/RemoteIO to be in “Slicer_Logs” and then increase the max cache size really large as well? Log files wouldn’t result in such a large file usage, but some cache location could grow large if you set the limit to something really high.</p>
<p>Or by chance have you been writing custom code or using a third party Slicer extension that is using this “Slicer_Logs” location?</p>

---

## Post #3 by @aiden.zhu (2019-11-18 15:43 UTC)

<p>Thanks a lot for your quick reply, James.</p>
<p>I guess I did not use a third party slicer extension associated with Slicer_Logs (or, LOL, I do not know it at all).</p>
<p>Yes, I did set up the “Temporary directory” as “C:/Users/Aiden.Zhu/documents/Slicer_Logs”.  But it seems I did not really set up a large Cache, here is my settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/363dc52a15540fc9346a27e9dc4da5e5b4fe8d66.png" data-download-href="/uploads/short-url/7JQ7M02qN6CSYlSMhh7moLNQ0V8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/363dc52a15540fc9346a27e9dc4da5e5b4fe8d66.png" alt="image" data-base62-sha1="7JQ7M02qN6CSYlSMhh7moLNQ0V8" width="690" height="348" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">786×397 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So is there any command I may use to clean cache?<br>
Thanks again.<br>
Aiden</p>

---

## Post #4 by @lassoan (2019-11-18 16:06 UTC)

<p>Only the last 10 log files are kept by default (you can change the value in your Slicer-NNN.ini file in LogFiles section “NumberOfFilesToKeep” value), but usually the files are small, so it should not be an issue.</p>
<p>Maybe you have enabled “Developer mode”. In developer mode, CLI module input and output files are not deleted after execution to make debugging easier. You can disable developer mode if this causes an issue for you.</p>

---

## Post #5 by @aiden.zhu (2019-11-18 16:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>   <a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
Thanks  a lot.<br>
Yeah, I guess it’s just due to my “Developer Mode” on. Then all right for me, I just need pay attention to it to make sure of that I have enough space in C-drive.</p>
<p>Best, Aiden</p>

---

## Post #6 by @Victor_Wayne (2025-10-31 05:33 UTC)

<p>Can I know where the log files go in linux systems?<br>
Can I also get some resources to implement logging in my extension?<br>
How can I inspect core slicer’s logging system?</p>

---

## Post #7 by @lassoan (2025-10-31 14:48 UTC)

<aside class="quote no-group" data-username="Victor_Wayne" data-post="6" data-topic="9193" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>Can I know where the log files go in linux systems?</p>
</blockquote>
</aside>
<p>Current application log:</p>
<pre><code>slicer.app.errorLogModel().filePath
</code></pre>
<p>Recent log file paths:</p>
<pre><code>slicer.app.recentLogFiles()
</code></pre>
<aside class="quote no-group" data-username="Victor_Wayne" data-post="6" data-topic="9193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>Can I also get some resources to implement logging in my extension?</p>
</blockquote>
</aside>
<p>You can use standard Python, VTK, ITK, Qt, console logging - they are all captured in the application log.</p>
<aside class="quote no-group" data-username="Victor_Wayne" data-post="6" data-topic="9193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>How can I inspect core slicer’s logging system?</p>
</blockquote>
</aside>
<p>You can access all the logs, connect event handlers, etc. through the <a href="https://github.com/commontk/CTK/blob/master/Libs/Core/ctkErrorLogAbstractModel.h"><code>slicer.app.errorLogModel()</code> object</a>.</p>

---

## Post #8 by @Victor_Wayne (2025-11-03 08:35 UTC)

<p>Ok I get it.</p>
<p>How can I set the number of files that is kept in the log folder? I want to keep all the log files.<br>
If I can’t keep all the log files, what is the maximum number of files I can keep? I don’t want to be limited to only ten. (it seems only 10 files get stored according to the experiment I did.) If I can keep the number of files that can be kept in the log folder, How can I set the number of files to keep programmatically? should I put it in the .slicerrc.py file?</p>
<p>Thanks in advance.</p>

---

## Post #9 by @cpinter (2025-11-03 09:26 UTC)

<p>This number is stored in the application settings. I didn’t find it in the GUI, but you can open the <code>Slicer.ini</code> file and change the number for the <code>NumberOfFilesToKeep</code> entry. I don’t think there is a maximum.</p>

---

## Post #10 by @Victor_Wayne (2025-11-10 04:57 UTC)

<p>How can I keep all the log files? the log files goes inside the tmp directory and if I just reboot my or shut down and boot it the next day the whole directory is gone. how can I prevent this? Is there any way to change the cmake files so that the logs goes in the folder where the slicer executable lives? I changed the number of files to keep to 10,000 I need all the log files.</p>

---

## Post #11 by @muratmaga (2025-11-10 05:10 UTC)

<aside class="quote no-group" data-username="Victor_Wayne" data-post="10" data-topic="9193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>How can I keep all the log files?</p>
</blockquote>
</aside>
<p>Why do you need to keep all the log files? How many Slicer sessions are you starting and ending a day? If you explain your use case, we might be able to give more pointed advise.</p>
<p>If you are on Linux you might simply add a cronjob to rsync the files to a permanent location (say every 5 minutes).</p>

---

## Post #12 by @Victor_Wayne (2025-11-10 06:22 UTC)

<p>We need to collect all the details from our custom built slicer such as which functionality the user is using the most;  how are they navigating through our modified custom built slicer; what series of operation that led to the crash if at all there is one and how much time user spends working on our components and much more. We also don’t want to make such that their tmp is constantly sending us their log files. We should be able to ssh into their machine and look around the log files if there is a problem. This is our use case. We at least need 1000 log files in a path where it doesn’t get automatically cleaned.</p>

---

## Post #13 by @muratmaga (2025-11-10 06:55 UTC)

<aside class="quote no-group" data-username="Victor_Wayne" data-post="12" data-topic="9193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>custom built slicer</p>
</blockquote>
</aside>
<p>If you have a custom built slicer, I am pretty sure you can control where the files are written?</p>
<p>I do not know where they are in the source code, but a quick github repo search for logfile keyword, returned results both of to your inquiries (e.g., how many log files to keep, as well as their location).  It looks like it is</p>
<p><a href="https://github.com/Slicer/Slicer/blob/071e13bf55808ae4a65d06940a60ddbcf231b9cf/Base/QTGUI/qSlicerApplication.cxx#L996" rel="noopener nofollow ugc">Base/QTGUI/qSlicerApplication.cxx</a> you want to modify</p>
<p><code>https://github.com/search?q=repo%3ASlicer%2FSlicer+logfile&amp;type=code</code></p>

---

## Post #14 by @Victor_Wayne (2025-11-10 08:36 UTC)

<p>Is there any way to change the path using the .ini files where all the configuration goes? I don’t want to modify the core slicer’s code.</p>

---

## Post #15 by @pieper (2025-11-10 12:36 UTC)

<p>You may want to have a look at the <a href="https://github.com/Slicer/SlicerTelemetry">SlicerTelemetry</a> extension to get more specific info about what features are being used and how often.  Be sure to get user consent before collecting this data.</p>
<aside class="quote no-group" data-username="Victor_Wayne" data-post="14" data-topic="9193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar"> Victor_Wayne:</div>
<blockquote>
<p>I don’t want to modify the core slicer’s code.</p>
</blockquote>
</aside>
<p>While it wouldn’t be as clean, you could add custom python code to copy the log file somewhere either with a timer or at application exit (or both).</p>

---
