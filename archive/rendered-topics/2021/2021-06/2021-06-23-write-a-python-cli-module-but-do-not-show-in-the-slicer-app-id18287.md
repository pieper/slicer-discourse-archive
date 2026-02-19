---
topic_id: 18287
title: "Write A Python Cli Module But Do Not Show In The Slicer App"
date: 2021-06-23
url: https://discourse.slicer.org/t/18287
---

# Write a python CLI module but do not show in the slicer app

**Topic ID**: 18287
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/write-a-python-cli-module-but-do-not-show-in-the-slicer-app/18287

---

## Post #1 by @bywbilly (2021-06-23 00:18 UTC)

<p>Hi,</p>
<p>I implemented an interactive python loadable module but it requires a heavy computation to do something with the volume.  To avoid this heavy computation stuff to block the main slicer app, (after some search) I find one solution is to create a python cli module for this heavy computation stuff and use slicer.cli.run to run it in a threads/process and add an observer to handle the callback?</p>
<p>If that’s the case, I am wondering how could I have a python cli module but do not show in the slicer app window? Basically I just want to call it from my loadble module and do not want the user to reach it through the app.</p>
<p>If there are better solutions to solve the issue, please point them out, thanks!</p>

---

## Post #2 by @pieper (2021-06-23 13:50 UTC)

<p>To give better advice, can you describe what operations are taking the time?  I.e. is it tight loops in python or do you call C++ methods (e.g. ITK or VTK)?</p>
<p>This approach could be a good general solution: <a href="https://github.com/pieper/SlicerProcesses" class="inline-onebox">GitHub - pieper/SlicerProcesses: Slicer modules for running subprocesses to operate on data in parallel</a></p>

---

## Post #3 by @bywbilly (2021-06-23 14:58 UTC)

<p>Hi Steve,</p>
<p>It is basically a deep learning model, so it is written and running purely in python.</p>

---

## Post #4 by @pieper (2021-06-23 15:09 UTC)

<p>But probably the time consuming part is in numpy or other C/C++ code.  If you have a bit computation you can release the GIL like we do in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SimpleFilters">SimpleFilters</a>.</p>
<p>We’ll be working on pytorch and monai integration next week as part of project week so we’ll be looking at various integration options and how to best handle the data and computation interactively.  You may want to join up.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW35_2021_Virtual/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW35_2021_Virtual/" target="_blank" rel="noopener">Welcome to the web page for the 35th Project Week!</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @bywbilly (2021-06-23 15:18 UTC)

<p>To be more specific, the time-consuming part is in C (CUDA).  Can you provide more information about the GIL, I cannot find it on the project page?</p>
<p>And do you have any idea about the solution I provided in the question? Wrap the time-consuming part as a CLI and run it slicer.cli.run in the background?</p>
<p>Thanks!</p>

---

## Post #6 by @pieper (2021-06-23 15:38 UTC)

<p>Regarding the original question, python is mostly single threaded but long-running calls can <a href="https://wiki.python.org/moin/GlobalInterpreterLock">release the GIL</a>, which is what we do in SimpleFilters and you could probably do for your CUDA call if the library you are using supports that.  Otherwise python threads can’t run at the same time.</p>
<p>There’s a lot of information about it <a href="https://www.na-mic.org/wiki/2013_Project_Week:Threaded_SimpleITK_Modules">here</a> and <a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2014/034633.html">here</a>.</p>

---

## Post #7 by @pieper (2021-06-23 15:49 UTC)

<p>If you are using PyTorch, and I guess by extension MONAI, then the long running tasks <a href="https://discuss.pytorch.org/t/can-pytorch-by-pass-python-gil/55498">should be releasing the GIL</a> so you can use threads like in the examples linked above.</p>

---

## Post #8 by @bywbilly (2021-06-23 16:24 UTC)

<p>I am using PyTorch but not using any MONAI stuff. Oh, so you mean GIL as the python global lock. I can run it in another process instead of thread, so GIL is not a problem.  The main problem is that the loadable module’s function will block the main slicer process and freeze the slicer app.</p>

---

## Post #9 by @lassoan (2021-06-23 16:42 UTC)

<p>Python CLI is a nice option (we’ll explore alternatives next week).</p>
<p>You can probably change visibility of a CLI module (so that it does not show up in the module finder), but I would not worry about having your CLI module visible to users. Just name it accordingly and place it in a category to make it clear for users that it is an advanced, low-level module. There are many such modules in Slicer. If you want to make your application very simple you would implement a slicelet (and the slicelet would not even have a module selector, so the CLI module would not be visible to the user at all).</p>

---

## Post #10 by @bywbilly (2021-06-24 16:49 UTC)

<p>Thanks Andras and steve,</p>
<p>I built a python CLI module and it worked perfectly for me!</p>

---
