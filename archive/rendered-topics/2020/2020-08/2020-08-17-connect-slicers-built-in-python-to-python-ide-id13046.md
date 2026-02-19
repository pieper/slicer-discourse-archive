---
topic_id: 13046
title: "Connect Slicers Built In Python To Python Ide"
date: 2020-08-17
url: https://discourse.slicer.org/t/13046
---

# Connect Slicer's built-in Python to Python IDE

**Topic ID**: 13046
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/connect-slicers-built-in-python-to-python-ide/13046

---

## Post #1 by @kleingeo (2020-08-17 16:53 UTC)

<p>I am trying to play around with a bunch of packages with Slicer, some of which are called through the command line/terminal. To make my life easier, I’m trying to connect the build-in python interpreter with Slicer to the IDE I use (PyCharm). I connected the the IDE to the <code>PythonSlicer.exe</code> file. However, when running anything I am getting this error.</p>
<pre><code class="lang-python">ModuleNotFoundError: No module named 'PythonQt'
</code></pre>
<p>Is there something I am missing?</p>
<p>The reason I am not using the normal remote debugger is that the file I am working with is run through cmd/terminal.</p>

---

## Post #2 by @ROSENty (2021-12-02 12:18 UTC)

<p>I get the same error, is anybody can help me? <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"></p>

---

## Post #3 by @lassoan (2021-12-02 18:38 UTC)

<p>You need to connect to a running application instance to access PythonQt and any objects that the Slicer application instantiates.</p>
<p>You can find instructions for connecting your IDE to Slicer <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/overview.html#python-debugging">here</a>.</p>
<p>To experiment with Python scripting in Slicer’s Python environment you can also <a href="https://github.com/Slicer/SlicerJupyter#slicerjupyter">use Slicer as a Jupyter notebook kernel</a>.</p>

---

## Post #4 by @ROSENty (2021-12-03 02:37 UTC)

<p>Thanks for your reply! <img src="https://emoji.discourse-cdn.com/twitter/yum.png?v=10" title=":yum:" class="emoji" alt=":yum:"><br>
I just want to execute python script on terminal, but I used the '…/Slicer-4.11.20210226-linux-amd64/bin/PythonSlicer  xx.py ', which is wrong. When I use ‘…/Slicer-4.11.20210226-linux-amd64 --python-script xx.py’,  I get the correct result.</p>

---

## Post #5 by @ROSENty (2021-12-03 02:53 UTC)

<p>sorry, the correct way is '…/Slicer-4.11.20210226-linux-amd64/Slicer --python-script xx.py’</p>

---

## Post #6 by @ROSENty (2021-12-16 09:51 UTC)

<p>dear Lasso, I got another problem: when I execute python script on terminal on ubuntu, which works. But when I use SSH to connect ubuntu on another PC(windows) , and execute the same python script on terminal with same code</p>
<pre><code class="lang-auto">…/Slicer-4.11.20210226-linux-amd64 --python-script xx.py --no-main-window
</code></pre>
<p>, I got</p>
<pre><code class="lang-auto">qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>please help me, thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=10" title=":sob:" class="emoji" alt=":sob:"></p>

---

## Post #7 by @lassoan (2021-12-16 17:58 UTC)

<p>You need a frame buffer to run Slicer. If you search for topics in the forum about running Slicer on a headless machine then you will find more details (as far as I remember xdummy and xvfb-run may help).</p>

---

## Post #8 by @ROSENty (2021-12-17 13:27 UTC)

<p>emmm, to be honest, I did what you said above, maybe I’m a newbie, I don’t get the correct way to solve this problem.<br>
Actually my problem is same as this</p><aside class="quote quote-modified" data-post="1" data-topic="21096">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e480ec/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/converting-dicom-to-nrrd-on-docker-via-a-python-script/21096">Converting DICOM to NRRD on Docker via a Python script</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hello, I would like to start off thanking all of you for the great work with 3D Slicer. It is truly a phenomenal piece of software! The issue we are having requires some description, so I will split this question into two main sections. 

<a name="h-1-setup-1" class="anchor" href="#h-1-setup-1"></a>1) Setup
I am working on a containerized application to perform some processing of DICOM images, and part of the pipeline involves first converting the DICOM files into an .nrrd file. Performing the conversion must be done via the 3D Slicer interface for a very…
  </blockquote>
</aside>
<p>
But I want to convert RTStruct file to .vtp file, so I got the same error <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=15" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=15" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=15" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2021-12-17 15:23 UTC)

<p>Running a Python script on docker or using a virtual frame buffer should work fine. Let’s continue the discussion in that other topic.</p>

---

## Post #10 by @ROSENty (2021-12-17 15:29 UTC)

<p>Thanks for your reply!!! You can reply me in</p><aside class="quote" data-post="5" data-topic="21096">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/converting-dicom-to-nrrd-on-docker-via-a-python-script/21096/5">Converting DICOM to NRRD on Docker via a Python script</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There’s a batch struct conversion script in SlicerRT that could be run in docker using a similar formula.  Be aware that RTStruct can be a tricky format due to variable vendor compliance issues, but SlicerRT is generally good at handling most cases.
  </blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">for all of you,cause I can’t image you developers could answer my question directly</p>

---
