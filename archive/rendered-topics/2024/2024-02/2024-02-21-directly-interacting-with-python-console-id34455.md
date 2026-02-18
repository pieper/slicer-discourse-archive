# Directly interacting with python console

**Topic ID**: 34455
**Date**: 2024-02-21
**URL**: https://discourse.slicer.org/t/directly-interacting-with-python-console/34455

---

## Post #1 by @muratmaga (2024-02-21 18:30 UTC)

<p>Is there a way to send python scripts from a text editor or an IDE directly to Slicer’s python? Copy and paste occasionally fails or creates weird issues (I am on remote connection). I am not a big fan of jupyter notebooks either.</p>

---

## Post #2 by @pieper (2024-02-21 19:06 UTC)

<p>I thought about various ways but in the end I like copy-paste the best.  With current slicer it doesn’t become part of the command history and it stops after the first error so I haven’t had any trouble.  What trouble do you have?</p>
<p>Sometimes I also put a comment like this at the top of the a file and then I have the exec line in my python history so I can just hit up arrow until I get to it and hit return to re-execute the file.</p>
<pre><code class="lang-auto">"""
filePath = "/Users/pieper/slicer/latest/OBJFileReader/textureImport_test.py"
exec(open(filePath).read())
"""
</code></pre>
<p>It would be possible to make something more integrated to an editor, like programming it to post the python code to the WebServer’s exec endpoint or by writing a snippet to a special file that Slicer could monitor with a QFileSystemWatcher, but in the end none of that seemed better than copy-paste for my use cases.</p>
<p>What I have been tempted to do is add a way to search the Slicer python console history to re-execute lines or previously pasted blocks.  It would be especially nice if this persisted across runs.  Since the data we need is in the log files this wouldn’t be hard to implement but I’ve never gotten around to it.</p>

---

## Post #3 by @muratmaga (2024-02-21 19:18 UTC)

<p>I have first have to login into a citrix server and then launch turbovnc to connect to our lab server interactively. Occasionally copy and paste functionality gets confused about what is being copied and pasted (local to remote, remote to remote, remote to local, local to local), and to get things back in order I have to restart both sessions.</p>
<p>in Rstudio there is an option to highlight a piece of code and direct it to the active terminal window (you can have as many terminal windows you like). I was hoping there might be a way to start Slicer from command line such that text sent to that terminal find its way to the Slicer’s python environment. So something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53cbf6cbcce5daf0087c76e80709dba409a13805.jpeg" data-download-href="/uploads/short-url/bXiCv8qIJzhcvR99bDwXnLesZMh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cbf6cbcce5daf0087c76e80709dba409a13805_2_643x500.jpeg" alt="image" data-base62-sha1="bXiCv8qIJzhcvR99bDwXnLesZMh" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cbf6cbcce5daf0087c76e80709dba409a13805_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cbf6cbcce5daf0087c76e80709dba409a13805_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53cbf6cbcce5daf0087c76e80709dba409a13805_2_1286x1000.jpeg 2x" data-dominant-color="5F6268"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1491 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-02-21 20:05 UTC)

<p>Jupyter notebook can be misused many ways, but it is the ideal tool for replacing copy-pasting of code snippets. It is much easier than carefully selecting text in an editor.</p>
<p>If you want to <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#python-console">run Python scripts from files</a> then you can use the <kbd>Ctrl-G</kbd> shortcut in Slicer. First time you use it you select a Python script to run. Next time you don’t need to select a file, just press hit <kbd>Ctrl-G</kbd> and then <kbd><code>Enter</code></kbd> (as the previously selected path is used by default).</p>

---

## Post #5 by @pieper (2024-02-21 20:24 UTC)

<p>I guess everyone can develop what works best for them and maybe we can add more hooks in Slicer to make things easier.  I find copy-paste to be such a universally supported and useful feature that I’ve never felt the need to develop anything further.  For example I’m frequently testing the same code on mac/windows/linux and it would be a waste of time if I needed to manually configure each editor.  Instead I just use vi (gvim typically) where it’s easy to use the keyboard to select blocks of code and then paste them to Slicer.</p>
<p>That said, if you are working on a module, then the Reload and Reload and Test buttons can be very valuable.</p>

---

## Post #6 by @muratmaga (2024-02-21 23:46 UTC)

<p>I know mine is a corner case, but sometimes the copy/paste buffer gets confused very quickly and I have to reset sessions every few minutes.</p>
<p>When I am working locally copy/paste is just fine, and yes the ability to reload the modules is also great. That’s what I was sort of wondering for python scripts. Is there any open-source, simple programming editor that can actually be incorporated to Slicer as an extension to facilitate that?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> is there a way to have jupiter notebooks to save things as at least mostly pyton + markdown, as opposed to JSON? JSON just makes interacting with the code on github much more difficult.</p>

---

## Post #7 by @lassoan (2024-02-22 04:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="34455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>is there a way to have jupiter notebooks to save things as at least mostly pyton + markdown, as opposed to JSON? JSON just makes interacting with the code on github much more difficult.</p>
</blockquote>
</aside>
<p>Even though jupyter notebook (.pynb) file content is in json, most editors, including GitHub’s online editor allows viewing and <em>editing</em> the actual formatted content. Example online viewers and editors:</p>
<ul>
<li><a href="https://github.com/Slicer/SlicerNotebooks/blob/master/01_Data_loading_and_display.ipynb">Github online in-place viewer</a></li>
<li><a href="https://github.dev/Slicer/SlicerNotebooks/blob/master/01_Data_loading_and_display.ipynb">Github online in-place editor</a></li>
<li><a href="https://nbviewer.org/github/Slicer/SlicerNotebooks/blob/master/01_Data_loading_and_display.ipynb">nbviewer for very fast viewing of large notebooks</a></li>
</ul>
<p>Interestingly, a new notebook variant, <a href="https://discourse.slicer.org/t/new-python-notebook-library/33758">marimo</a>, uses Python code instead of json as source format. However, I’m not sure if it can run code inside the Python environment in the running Slicer process.</p>

---

## Post #8 by @pieper (2024-02-22 16:50 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="34455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is there any open-source, simple programming editor that can actually be incorporated to Slicer as an extension to facilitate that?</p>
</blockquote>
</aside>
<p>I’m not sure about “simple” but at least you can run vim in Slicer with this wasm compiled version:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; ww = slicer.qSlicerWebWidget()
&gt;&gt;&gt; ww.url = "https://rhysd.github.io/vim.wasm"
&gt;&gt;&gt; ww.show()
</code></pre>
<p>I didn’t spend much time on it, but I’m sure it’s possible to add hooks to move code in and out of Slicer using the javascript interface from python.</p>
<p>This seems to work as well, and may be simpler:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; ww.url = "https://ace.c9.io/build/kitchen-sink.html"
</code></pre>

---

## Post #9 by @muratmaga (2024-02-22 22:17 UTC)

<p>THis is interesting, I will give it a try.</p>
<p>Meanwhile, what I was thinking is that we already have a Texts module in Slicer. Would it be possible it to support code highlighting and indentations and have route the code the python console?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801.png" data-download-href="/uploads/short-url/dTzDn9bUfr6LUmDQBaLrHOHRxa9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801_2_434x499.png" alt="image" data-base62-sha1="dTzDn9bUfr6LUmDQBaLrHOHRxa9" width="434" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801_2_434x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801_2_651x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61648005019eb55b29d8e686ce0bf1c091c23801_2_868x998.png 2x" data-dominant-color="DEDDEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1734×1996 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2024-02-22 22:32 UTC)

<p>Yes, that could work too.  Interesting that this approach would save code snippets along with the scene, and that could be useful for sharing work, something like what people do with notebooks.</p>

---

## Post #11 by @muratmaga (2024-02-22 22:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="34455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Interesting that this approach would save code snippets along with the scene, and that could be useful for sharing work</p>
</blockquote>
</aside>
<p>+1<br>
I think this would be great actually. Having the code baked into the scene would be even more useful than having in an external notebook (particularly for small projects).</p>

---

## Post #12 by @muratmaga (2024-02-24 00:41 UTC)

<p>Turned into a feature request for votes: <a href="https://discourse.slicer.org/t/support-python-text-highlighting-in-text-module/34511/1" class="inline-onebox">Support python text highlighting in Text module</a></p>

---
