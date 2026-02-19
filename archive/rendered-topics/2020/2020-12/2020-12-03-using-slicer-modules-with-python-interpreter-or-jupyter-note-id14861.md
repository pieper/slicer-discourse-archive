---
topic_id: 14861
title: "Using Slicer Modules With Python Interpreter Or Jupyter Note"
date: 2020-12-03
url: https://discourse.slicer.org/t/14861
---

# Using Slicer modules with Python interpreter or Jupyter Notebook (Help!)

**Topic ID**: 14861
**Date**: 2020-12-03
**URL**: https://discourse.slicer.org/t/using-slicer-modules-with-python-interpreter-or-jupyter-notebook-help/14861

---

## Post #1 by @perecanals (2020-12-03 11:26 UTC)

<p>Hi,</p>
<p>I am trying to automize Slicer functions that I regularly do manually using Python scripts and I have been facing some problems that have been slowing me down quite a bit. I have been reading through the forums and documentation but I cannot seem to find a proper way to consistently understand how to use the functions embedded in the different modules that Slicer offers. I am no expert in Python, but right now I am only able to successfully use Slicer modules with Python scripts if I happen to come across some use case example that resembles what I am trying to accomplish.</p>
<p>My question is, could someone perhaps give me some insight on their experience as to how would you find your way through using a specific module? Or maybe link some useful documentation to this regard? Maybe what I am asking is a bit too general and it heavily depends on the module itself, but I am really stuck and a bit overwhelmed by documentation at the moment.</p>
<p>If it helps to put a specific (simple) scenario, I am trying to use the surface toolbox module to invert normals from the surface I generate with the segmentation, so that when I extract the .obj or .stl file, normals are facing outwards (shouldn’t that be default?). After that I would like to use VMTK to auto-detect endpoints and extract centerlines, but I have not looked into this last part just yet.</p>
<p>Thank you,</p>

---

## Post #2 by @pieper (2020-12-03 15:50 UTC)

<p>Agreed, figuring out the mapping between UI features and implementation can be tricky.  One thing I commonly use is <code>git grep</code> for to find a feature.  Sometimes this means finding the text of a label in a .ui or cxx file and then finding the corresponding widget name, and then figuring out what signals it fires and what slots are connected to them.  Other times it means reading through a script to figure out the logic.  Basically is means getting comfortable with the source code and architecture of the system (and while that is a bit of work, it should be valuable when trying to automate things).</p>

---

## Post #3 by @lassoan (2020-12-03 15:59 UTC)

<p>For Python scripted modules, you can see what exact Python calls are made and either replicate those in your module or call the methods of that scripted module. The latter is preferred, especially if it is more than a couple of lines of code, but sometimes modules don’t expose reusable components nicely in their logic interface - in this case you may contact the author and ask for improving the API.</p>
<p>For Slicer core modules, implemented in C++, you can follow the approach described here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="inline-onebox">Python FAQ — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="perecanals" data-post="1" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>I am trying to use the surface toolbox module to invert normals from the surface I generate with the segmentation</p>
</blockquote>
</aside>
<p>Computing the normals is just 2-3 lines of Python code, so I would just call that directly. Inverting the normals should not be necessary. Maybe you applied a transform that turned the mesh inside out?</p>
<aside class="quote no-group" data-username="perecanals" data-post="1" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>After that I would like to use VMTK to auto-detect endpoints and extract centerlines, but I have not looked into this last part just yet.</p>
</blockquote>
</aside>
<p>VMTK centerline extraction module is Python scripted module, so you can apply the techniques I described above. If you have trouble using the centerline extraction module logic (without the GUI) then submit an issue to the <a href="https://github.com/vmtk/SlicerExtension-VMTK">repository</a>.</p>

---

## Post #4 by @muratmaga (2020-12-03 18:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For Slicer core modules, implemented in C++, you can follow the approach described here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features </a></p>
</blockquote>
</aside>
<p>I discussed this <a class="mention" href="/u/pieper">@pieper</a> and while this is fine for full-time developers, it is a very tedious process for someone who occasionally needs to script a basic function in Slicer. In R there is an excellent search function apropos which would return functions containing the string, from which one can directly get the help for (see below an example for SimpleITK. Fyi this all command line, no IDE is involved). I think something along these lines this would be great to implement for Slicer and help scientist who need to bring a few lines of code together without having to go through the source code manually (at least not at the beginning).</p>
<pre><code>&gt; library(SimpleITK)
&gt; apropos("smooth")
 [1] "KalmanSmooth"
 [2] "ksmooth"
 [3] "loess.smooth"
 [4] "panel.smooth"
 [5] "scatter.smooth"
 [6] "smooth"
 [7] "smooth.spline"
 [8] "smoothEnds"
 [9] "SmoothingRecursiveGaussian"
[10] "SmoothingRecursiveGaussianImageFilter"
[11] "smoothScatter"
[12] "tsSmooth"
&gt; ?SmoothingRecursiveGaussianImageFilter
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f59667a5ad61a01befe3ab48623d78f8269116b.png" data-download-href="/uploads/short-url/iaAb2icyOH8DFnBoQJTBv8yQt0T.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f59667a5ad61a01befe3ab48623d78f8269116b_2_354x375.png" alt="image" data-base62-sha1="iaAb2icyOH8DFnBoQJTBv8yQt0T" width="354" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f59667a5ad61a01befe3ab48623d78f8269116b_2_354x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f59667a5ad61a01befe3ab48623d78f8269116b_2_531x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f59667a5ad61a01befe3ab48623d78f8269116b_2_708x750.png 2x" data-dominant-color="B2B4B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1814×1915 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @perecanals (2020-12-03 18:20 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thank you for the tips! I guess this is more or less what I was fearing a bit, but wanted to make the post before deep diving further in source code, just in case I am missing something obvious. Gonna to try the <code>git grep</code> tip, thanks!</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For Python scripted modules, you can see what exact Python calls are made and either replicate those in your module or call the methods of that scripted module. The latter is preferred, especially if it is more than a couple of lines of code, but sometimes modules don’t expose reusable components nicely in their logic interface - in this case you may contact the author and ask for improving the API.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Okay, so from what you say, automating functions from CLI and loadable modules will generally be trickier than scripted modules, which should be more straight forward, is that correct?</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="3" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For Slicer core modules, implemented in C++, you can follow the approach described here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="inline-onebox" rel="noopener nofollow ugc">Python FAQ — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p>Thanks! Will take a good look to this.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Inverting the normals should not be necessary. Maybe you applied a transform that turned the mesh inside out?</p>
</blockquote>
</aside>
<p>I do not think I have applied any transformation, I just applied thresholding (min=1, max=1) to a binary nifty and exported the segmentation as an STL or OBJ. Same happens when I do it manually. Should I do it differently?</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="14861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you have trouble using the centerline extraction module logic (without the GUI) then submit an issue to the <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">repository</a>.</p>
</blockquote>
</aside>
<p>Okay, will probably do at some point, thank you very much!</p>

---

## Post #6 by @lassoan (2020-12-04 02:46 UTC)

<p>Apropos seems like a nice indexer for documentation of already installed Python-accessible packages but it would not help users in finding out how to access a specific features from Python to automate a workflow.</p>
<p>The problem is that scripting <em>applications</em> are much harder to learn that scripting <em>libraries</em>, because libraries typically do not have states and you build your data model yourself. To be able to script applications, you need to get to know how the application works internally, which is a lot of learning. Good documentation, macro recording, etc. can help, but most of the time you end up just googling for a problem and copy-pasting, modifying, combining scripts that you find on forums, blogs, or StackOverflow. This is not specific to Slicer, but the same for all applications that expose a large part of its API. See for example all MS Office applications and these <a href="https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office#all-of-my-office-applications-example-code">examples</a> to get an idea that just how complicated is to script even the simplest actions. You may be an expert Excel user, but there is no chance you could figure out what 4-5 lines to write to script an action because you need to be very familiar with the application’s data model and functions that operate on them. Macros that Excel records can be somewhat useful, but the recorded actions are rarely reusable directly, instead they may just give some useful hints or make lead you to a dead end.</p>
<p>So, while we can clearly improve many things, scripting an application will be always hard. However, it still takes less effort to learn an application platform than redeveloping an application from scratch.</p>

---
