---
topic_id: 24969
title: "How To Make Modification Of Home Module Work In Custom Appli"
date: 2022-08-29
url: https://discourse.slicer.org/t/24969
---

# How to make modification of Home module work in Custom Application?

**Topic ID**: 24969
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/how-to-make-modification-of-home-module-work-in-custom-application/24969

---

## Post #1 by @nnzzll (2022-08-29 05:53 UTC)

<p>I’m developing a custom application of Slicer and successfully build the project.<br>
The application is switched to the “Home” module by default and I’d like to make some modification in the “Home” module.<br>
However, whatever change I had made in the <code>Home.py</code> file it just doesn’t work.<br>
For example , I added a simple line</p>
<pre><code class="lang-auto">print("HomeWidget init!")
</code></pre>
<p>to the <code>__init__</code> method of <code>HomeWidget</code> and rebuild this project. When the program starts up this function just won’t be called.</p>
<p>How to solve this problem?</p>

---

## Post #2 by @cpinter (2022-09-02 09:51 UTC)

<p>A very basic suggestion, but may be the case if I understand your problem correctly. You may be trying to change the source code and expect that the change to be reflected in the build. If so, you may need to do either of the following</p>
<ol>
<li>Run the build</li>
<li>Edit the deployed source files in <code>[SuperbuildPath]/Slicer-build/lib/[AppName]-5.0/qt-scripted-modules</code>. But then remember to copy those back to source otherwise you’ll lose the changes when you run a build</li>
<li>Edit the source code in the working copy and have a script copy the <code>.py</code> files to the binary folder (see just above). This is what I do when I only edit Python files</li>
</ol>

---

## Post #3 by @Sam_Horvath (2022-09-02 14:24 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="24969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Run the build</p>
</blockquote>
</aside>
<p>An additional method/option for ‘run the build’: you can use cmake/ninja/make/etc to run just the targets that copy over the .py files, ex:</p>
<pre><code class="lang-auto">cd /path/to/Slicer-build
cmake --build . --target CopySlicerPythonScriptFiles
cmake --build . --target CopySlicerPythonResourceFiles
</code></pre>

---
