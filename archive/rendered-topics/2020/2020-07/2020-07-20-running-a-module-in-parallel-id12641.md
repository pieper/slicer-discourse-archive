---
topic_id: 12641
title: "Running A Module In Parallel"
date: 2020-07-20
url: https://discourse.slicer.org/t/12641
---

# Running a Module in Parallel

**Topic ID**: 12641
**Date**: 2020-07-20
**URL**: https://discourse.slicer.org/t/running-a-module-in-parallel/12641

---

## Post #1 by @vertebrae (2020-07-20 14:12 UTC)

<p>Hello,</p>
<p>I am currently using a python scripted module to run my vertebra segmentation program. The program uses a for loop to segment multiple fiducial points. This process takes a long time to run and I thought that running in parallel would take a shorter time than iterating through a loop. How can I run my program in parallel using python?</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @adamrankin (2020-07-20 15:41 UTC)

<p>Your most likely route is to call into a c++ library from python.</p>
<p>Python scripted module -&gt; c++ (loadable) module with no GUI -&gt; set flag when finished processing</p>

---

## Post #3 by @pieper (2020-07-20 15:57 UTC)

<p>Another option is to start an independent PythonSlicer process and pass over the data it needs.  The SlicerProcess module does this using pickle and stdio, making it pretty efficient.  The nice thing is that you get a complete slicer python environment with all the same libraries but independent of mrml and the GUI.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerProcesses">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerProcesses" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/27bac95dd7ffa76700baa6ce3ff22f3f676488db6be74c51af2fa7c2002247c8/pieper/SlicerProcesses" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerProcesses" target="_blank" rel="noopener">GitHub - pieper/SlicerProcesses: redirect for old SlicerProcessing repo</a></h3>

  <p>redirect for old SlicerProcessing repo. Contribute to pieper/SlicerProcesses development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote" data-post="14" data-topic="10185">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/thread-for-uploading-data/10185/14">Thread for uploading data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The current SlicerProcesses code isn’t set up for progress reporting.  There could be lots of ways to do it,  Slicer CLI modules use a convention of embedding xml snippets in the output that triggers automatic progress updates in the GUI.  Another option would be to set up a connection like OpenIGTLink to pass data.  Or one could create a custom network protocol.
  </blockquote>
</aside>


---

## Post #5 by @vertebrae (2020-07-20 19:12 UTC)

<p>(post withdrawn by author, will be automatically deleted in 24 hours unless flagged)</p>

---

## Post #6 by @vertebrae (2020-07-20 23:38 UTC)

<p>Does anybody know how to do this?</p>

---

## Post #7 by @vertebrae (2020-07-21 13:20 UTC)

<p>So I have opened up a scriptedcli module and I have my function that I would like to copy on to there (the onApplybutton function from the slicer scripted module), how do I effectively transfer this code to my scriptedcli module and then run this with my scripted module?</p>

---

## Post #8 by @vertebrae (2020-07-21 13:32 UTC)

<p>(post withdrawn by author, will be automatically deleted in 24 hours unless flagged)</p>

---

## Post #9 by @vertebrae (2020-07-21 15:42 UTC)

<p>(post withdrawn by author, will be automatically deleted in 24 hours unless flagged)</p>

---

## Post #11 by @vertebrae (2020-07-22 14:03 UTC)

<p>Hello,</p>
<p>I have a local threshold segmentation code in a scripted python module which iterates through fiducial points and runs the local threshold function. Iterating through points takes a while to do and to speed it up, I would like it to run in parallel with a scripted CLI python module. I have set a list of parameters, and I have this line of code:</p>
<p>slicer.cli.runSync(slicer.modules.climodulecode, None, param, True, True)</p>
<p>I am not sure what to do in terms of adding code to the scripted cli module and how to use the parameters from there. I have looked at some examples but I am still a little unclear.</p>
<p>Thanks</p>

---

## Post #12 by @vertebrae (2020-07-22 17:08 UTC)

<p>param = {“inputVolume”: masterVolumeNode.GetID(), “MinimumThreshold”: 265, “MaximumThreshold”: 1009, “MinimumDiameterMm”: 9, “Seed”:fidList.getID()}</p>
<p>These are my parameters. Any ideas? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #13 by @lassoan (2020-07-23 01:44 UTC)

<p><code>slicer.cli.runSync</code> blocks execution until processing is complete. <code>slicer.cli.runAsync</code> blocks execution until processing is complete. <code>slicer.cli.run(..., wait_for_completion = False)</code> is not much better either, as Slicer always runs only one CLI at a time (the only advantage is that you can still use Slicer while computation is running in the background). For parallel execution, I would recommend to use <a class="mention" href="/u/pieper">@pieper</a>’s SlicerProcesses extension.</p>
<p>Another approach is to keep a single process but use multiple seeds. LocalThreshold effect uses only a single input point, but you could modify it to take all your input points at once.</p>
<p>However, before you would start trying these, the most important thing is to profile your existing implementation. You need to know what line(s) of code take most of the time and focus only on those. There are Python profilers that you can configure or you can measure approximate execution time by adding log messages.</p>

---

## Post #14 by @mau_igna_06 (2022-04-02 12:06 UTC)

<p>I would be interested on creating a CLI module (written on C++) for saving selected nodes or all scene (just what the save dialog achieves).<br>
I think this would be useful since it will allow the user to autosave by executing the callback of a timer periodically and (if I understood correctly) Slicer GUI will not freeze, further more all features (processing and visualization) of Slicer would be available as it is normally.</p>
<p>Would this idea work? Would this idea have a positive impact if it’s implemented?</p>
<p>Thank you</p>

---

## Post #15 by @pieper (2022-04-02 14:21 UTC)

<p>It it’s a CLI running as a separate process (the default) then Slicer would communicate with it via files and there would be no real time saved.  If the saving is in a separate thread there could be a problem if, for example, the data is deleted in the main thread during the save.  You could implement a threaded version that copies all the data to private memory in the thread and then does the disk IO while the main thread goes on to other tasks.  In fact, you can use multiple threads, say one for each data file and that could speed up, for example, compression.  I tried this once for reading and got about 6x performance improvement for a scene with lots of files.</p>

---

## Post #16 by @mau_igna_06 (2022-04-02 14:35 UTC)

<p>So memory cannot be shared between processes even in a read-only mode?<br>
Maybe you could flag/lock the nodes that are being read so the cannot be modified during the save.<br>
Could two Slicer instances share RAM and through it share node references so one saves the nodes on the background while the other does visualization of them on the foreground? Maybe on a virtualized enviroment that’s possible?</p>

---

## Post #17 by @pieper (2022-04-02 14:55 UTC)

<p>There’s nothing that locks memory in the scene so sharing it between processes would be unsafe in general (modules can modify the scene contents).  Copying in memory is usually a very efficient operation compared to IO so it’s probably the best way to go.  It should be easy to try some timing experiments.</p>

---

## Post #18 by @jcfr (2022-06-29 14:52 UTC)

<p><em>Documenting here comments reported during the IGT session that took place during the 37th NA-MIC project week related to <a href="https://github.com/pieper/SlicerParallelProcessing">SlicerParallelProcessing</a></em></p>
<p>from <a class="mention" href="/u/jcfr">@jcfr</a></p>
<blockquote>
<p>Why not look into doing a scripted CLI module running in the background ?</p>
<p>As well as improving the way such module can communicate feedback back to the application</p>
</blockquote>
<p>from <a class="mention" href="/u/cpinter">@cpinter</a></p>
<blockquote>
<p>Not being able to run algorithms on an actual parallel process in Python was a big limitation. Steve’s module solves this issue, but that doesn’t mean the other options are not available anymore<br>
CLI is super flexible in that you only need to specify the command-line and under the hood it van be anything, even python</p>
</blockquote>
<p>From <a class="mention" href="/u/lassoan">@lassoan</a></p>
<blockquote>
<p>The only current limitation of CLIs is that Slicer runs them on a single background thread, so if you start multiple CLIs they are all executed one after the other on that background thread. On most computers you have 8 or more cores, so allow running 5-10 CLIs in parallel could makes things faster (as demonstrated by ParallelProcessing extension).</p>
</blockquote>
<p>cc: <a class="mention" href="/u/ungi">@ungi</a></p>

---

## Post #19 by @jcfr (2022-06-29 14:53 UTC)

<blockquote>
<p>current limitation of CLIs is that Slicer runs them on a single background thread, so if you start multiple CLIs they are all executed one after the other on that background thread</p>
</blockquote>
<p>To address this, I started a topic <a href="https://github.com/jcfr/Slicer/commits/support-running-cli-in-parallel" class="inline-onebox">Commits · jcfr/Slicer · GitHub</a></p>

---

## Post #20 by @MJamal (2024-03-02 07:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="15" data-topic="12641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You could implement a threaded version that copies all the data to private memory in the thread</p>
</blockquote>
</aside>
<p>Apparently, the MRML scene cannot be directly delegated to another thread from the main thread. Therefore, I believe the main thread may still be used for this copy operation to make the scene/data available to other threads.</p>

---

## Post #21 by @lassoan (2024-03-10 22:30 UTC)

<p>Yes, while copying the inputs and final outputs from/to the scene the main thread must be blocked (or the main thread must copy the data).  Copying can be done by just replacing a few pointers, so the main thread is blocked for just microseconds.</p>

---

## Post #22 by @MJamal (2024-03-14 03:34 UTC)

<p>I’d like to know if the usage of these ‘few pointers’ is dependent on input size.</p>
<p>What I am considering is deep copying the nodes from the main thread, such as segmentation nodes, transformation nodes, color table nodes, etc., except for volume nodes which might be larger, into another thread and then performing the autosave operation. The downside to this approach is that memory overhead will increase as the size of nodes grows.</p>

---
