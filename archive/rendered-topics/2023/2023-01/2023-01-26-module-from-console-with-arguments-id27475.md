---
topic_id: 27475
title: "Module From Console With Arguments"
date: 2023-01-26
url: https://discourse.slicer.org/t/27475
---

# Module from console with arguments

**Topic ID**: 27475
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/module-from-console-with-arguments/27475

---

## Post #1 by @lucas_sd (2023-01-26 09:27 UTC)

<p>Hi everybody,</p>
<p>I run a specific module using the terminal like this: <code>Slicer.exe --python-code selectModule('MyModule')</code>.</p>
<p>Now, the code of the module take arguments (-t), and I try to run the module just adding: <code>Slicer.exe --python-code selectModule('MyModule') -t 44</code></p>
<p>But it doenst work, the argument is not taken (‘NoneType’), so its possible to run a module with arguments in this way? and which is the correct syntax?</p>
<p>Thanks a lot,<br>
Lucas.</p>

---

## Post #2 by @lassoan (2023-01-26 23:44 UTC)

<p>Is it a scripted CLI module or a scripted Loadable module?</p>

---

## Post #3 by @lucas_sd (2023-01-27 09:25 UTC)

<p>Hi Andras,</p>
<p>Its just a scripted loadable module.</p>
<p>Thanks+</p>

---

## Post #4 by @lassoan (2023-01-28 17:52 UTC)

<p>You can then simply list all the commands you want to launch at startup, separated by semicolons. If you want to submit many commands or you would like to avoid messing with proper quotation marks and indentation then you can specify a Python script filename to launch at startup.</p>
<p>If you want to interact with the application after it is started (load more data, remove data, etc) then you can use Slicer’s REST API.</p>
<p>There is a Python package -  <a href="https://pypi.org/project/slicerio">slicerio</a> - that you can pip install very easily into any Python environment that allows you to start Slicer, load data, view data, export data, etc. using a few simple Python function calls. If you find that some features are missing then feel free to add them and submit pull requests.</p>

---

## Post #5 by @lucas_sd (2023-01-30 09:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="27475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>separated by semicolons</p>
</blockquote>
</aside>
<p>Hi Andras, I tried like this, but it didnt work:</p>
<pre><code class="lang-auto">Slicer.exe --python-code selectModule('MyModule'); -t 20
</code></pre>
<p>In this case “t” is an argument which modify a specific action of the module. The use the semicolons is correct in this case?</p>
<p>Thanks+</p>

---

## Post #6 by @lassoan (2023-01-30 16:42 UTC)

<p>You can use <code>--python-code</code> to specify all parameters and actions by multiple Python commands, separated by semicolons, quoted if contains spaces. For example:</p>
<pre><code class="lang-auto">Slicer.exe --python-code "selectModule('SampleData'); getModuleGui('SampleData').setCategoryVisible('BuiltIn', False)"
</code></pre>
<p>Alternatively, you can use <code>--python-script</code> to specify a launcher script and set each additional parameter as a separate command-line argument. You can parse the arguments using Python argparse as usual. For example:</p>
<pre><code class="lang-auto">Slicer.exe --python-script path/to/BatchStructureSetConversion.py --input-folder input/folder/path --output-folder output/folder/path
</code></pre>
<p>You can find a complete example of a script that is launched like this <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/_readme.txt">here</a>.</p>

---
