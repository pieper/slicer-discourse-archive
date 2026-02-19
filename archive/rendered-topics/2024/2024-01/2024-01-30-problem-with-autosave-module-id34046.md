---
topic_id: 34046
title: "Problem With Autosave Module"
date: 2024-01-30
url: https://discourse.slicer.org/t/34046
---

# Problem with AutoSave module

**Topic ID**: 34046
**Date**: 2024-01-30
**URL**: https://discourse.slicer.org/t/problem-with-autosave-module/34046

---

## Post #1 by @MJamal (2024-01-30 13:22 UTC)

<p>Hello,</p>
<p>How can I prevent the Slicer main window from becoming unresponsive when using the autosave feature? I’ve observed significant lag in the main window after enabling autosave. Is it running on the same thread as Slicer?</p>
<p>Few suggestions on autosave:</p>
<ol>
<li>Since CLI modules run on a separate process, and I came across a <a href="https://github.com/jcfr/Slicer/commit/2cdd5c9da49e692a463af0d80efa6b6d20ad5099" rel="noopener nofollow ugc">commit</a> mentioning running at least two CLI modules parallely, So can we run autosave as a CLI on a separate thread to prevent the main window from getting stuck?</li>
<li>Alternatively, can we utilize the ParallelProcessing module to run autosave in a separate process? (I’m concerned about whether this handles synchronization between scene saving.)</li>
</ol>
<p>Lastly, is there a way to integrate QtConcurrent into Slicer? I attempted to add it, but it didn’t work at all.</p>

---

## Post #2 by @cpinter (2024-01-30 18:19 UTC)

<ol>
<li><a href="https://github.com/PerkLab/SlicerSandbox/tree/master/AutoSave">AutoSave</a> is a Python module so it cannot make use of the methods applicable to CLI.</li>
<li>If you use ParallelProcessing you do not have access to the Slicer MRML scene, only data you may have saved yourself before starting the process. Since it is the saving itself that takes time, and causes the lag, it is not something that can be outsourced to a parallel thread. Note that I say this with my limited knowledge about both modules.</li>
</ol>
<p>Maybe you can limit autosaving to the MRML node types you are interested in autosaving? Or limit the types of events that trigger it?</p>

---

## Post #3 by @MJamal (2024-01-31 04:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Maybe you can limit autosaving to the MRML node types you are interested in autosaving? Or limit the types of events that trigger it?</p>
</blockquote>
</aside>
<p>For my use case, I would like to save the entire scene as a bundle. Incremental saving would also be acceptable if it is applicable in the slicer.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><a href="https://github.com/PerkLab/SlicerSandbox/tree/master/AutoSave" rel="noopener nofollow ugc">AutoSave </a> is a Python module so it cannot make use of the methods applicable to CLI.</p>
</blockquote>
</aside>
<p>How about re-implementing it as a C++ CLI or Loadable module? Is it a viable option?</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If you use ParallelProcessing you do not have access to the Slicer MRML scene</p>
</blockquote>
</aside>
<p>Additionally, what are your thoughts on using shared memory for data saving?</p>

---

## Post #4 by @muratmaga (2024-01-31 04:30 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="3" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>I would like to save the entire scene as a bundle</p>
</blockquote>
</aside>
<p>I think a lot of the slowness is caused by the single threaded compression of the bundle, particularly if the data is large or there are many volumes in the scene. I wonder if it is possible to create the bundle without compression.</p>

---

## Post #5 by @pieper (2024-01-31 08:04 UTC)

<p>It looks like the current AutoSave only saves as MRB, so it’s always saving the bulk data (and compressing it) without regard for the modified status.  Someone could look into saving incremental .mrml files to avoid this overhead for cases where the bulk data isn’t actually changing and can be restored if there’s a crash.</p>

---

## Post #6 by @MJamal (2024-01-31 11:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>a lot of the slowness is caused by the single threaded compression of the bundle, particularly if the data is large or there are many volumes in the scene</p>
</blockquote>
</aside>
<p>I experimented with it, and I found that scene saving is taking place on the same thread as the slicer. That’s probably the reason for freezing.</p>

---

## Post #7 by @MJamal (2024-01-31 11:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="34046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Someone could look into saving incremental .mrml files to avoid this overhead for cases where the bulk data isn’t actually changing and can be restored if there’s a crash.</p>
</blockquote>
</aside>
<p>That can probably be achieved if there is a way to determine whether a scene has been updated and also retrieve its state, including the source of the update. This would allow us to save incremental updates from the last modified state to the current state.</p>

---

## Post #8 by @pieper (2024-01-31 12:45 UTC)

<p>The <code>ModifiedSinceRead</code> property should be reliable.  It’s used in the Save dialog to determine which nodes need to be enabled for saving by default.</p>

---
