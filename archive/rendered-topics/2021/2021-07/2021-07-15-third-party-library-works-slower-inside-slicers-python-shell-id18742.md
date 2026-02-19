---
topic_id: 18742
title: "Third Party Library Works Slower Inside Slicers Python Shell"
date: 2021-07-15
url: https://discourse.slicer.org/t/18742
---

# Third party library works slower inside Slicer's Python shell - why? how to do performance profiling?

**Topic ID**: 18742
**Date**: 2021-07-15
**URL**: https://discourse.slicer.org/t/third-party-library-works-slower-inside-slicers-python-shell-why-how-to-do-performance-profiling/18742

---

## Post #1 by @keri (2021-07-15 00:34 UTC)

<p>Hi,</p>
<p>I’m trying to use python package <a href="https://github.com/kinverarity1/lasio" rel="noopener nofollow ugc">lasio</a>. It is geological library and its main purpose is to read textual files of format <code>.las</code></p>
<p>After installing it (<code>pip install lasio</code>) I can use it as follows:</p>
<pre><code class="lang-python">import lasio
las = lasio.read("path/to/las/file")    # I provide an example file below
</code></pre>
<p>The problem is that if I read this <code>.las</code> file (via command <code>las = lasio.read("path/to/las/file")</code>) in Slicer’s python shell then it works noticeably slower (about 5 seconds) than when I open <code>PythonSlicer.exe</code> in Windows 10 cmd and type the same command (it takes less than a second).</p>
<p>Also when I do that in Slicer’s python shell then I get warning:<br>
<code>Opening D:\D\A_Kerbel.las as ascii and treating errors with "replace"</code><br>
wich is produced by <a href="https://lasio.readthedocs.io/en/latest/_modules/lasio/reader.html#:~:text=%23%20Now%20open%20and%20return%20the%20file-like%20object" rel="noopener nofollow ugc">this source code</a> I think.<br>
I don’t get this warning if I work inside cmd in <code>PythonSlicer.exe</code></p>
<p>What may be the reason of perfomance penalty? If somebody has idea please share it. Probably it is somehow connected with <a href="https://lasio.readthedocs.io/en/latest/encodings.html" rel="noopener nofollow ugc">character encoding detection</a> but I tried to turn it off and still Slicer’s python shell works much slower. Or maybe there are many modules loaded to Slicer? Don’t know…</p>
<p>To test it you need <a href="https://drive.google.com/file/d/1ZTRs68wHi1M4rPDsgswiNXAkK_0c-Vp0/view?usp=sharing" rel="noopener nofollow ugc">relatively big .las file</a></p>
<p>P.S. I work with this library as I need it in my SlicerCAT and I can see that this problem doesn’t depend whether I use original Slicer or SlicerCAT</p>

---

## Post #2 by @lassoan (2021-07-15 04:44 UTC)

<p>Lasio runs slower in Slicer because it logs a crazy amount of messages at debug level. You can disable this by temporarily decreasing the log level by running this command:</p>
<pre><code class="lang-python">import logging
logging.getLogger().setLevel(logging.INFO)
</code></pre>
<p>After you have finished with lasio, you can restore the log level to <code>logging.DEBUG</code>.</p>
<p>I haven’t experienced this with other Python packages, so you might report this finding to lasio developers. Maybe they could use their own logger instead of using the root logger (which is set to debug level logging in Slicer).</p>
<hr>
<p>If you are curious how I’ve found out the root cause of the problem: with profiling. Profilers are invented exactly for pinpointing performance bottlenecks. I’ve used <a href="https://docs.python.org/3/library/profile.html">cProfile</a> to collect logs and visualized the results using <a href="https://github.com/nschloe/tuna">tuna</a>.</p>
<p>Collect data:</p>
<pre><code class="lang-python">import cProfile
cProfile.run("las=lasio.read(r'c:\Users\andra\Downloads\A_Kerbel.las')", "c:/tmp/las.prof")
</code></pre>
<p>Plot results:</p>
<pre><code class="lang-python">pip_install('tuna')
slicer.util._executePythonModule("tuna", ["c:/tmp/las.prof"])
</code></pre>
<p>Tuna output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90e3f56d3559d6e705f130f9c50d79d2a6c4a336.png" data-download-href="/uploads/short-url/kFL9BPhR4zuO6RguSdnL1z2wUo6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90e3f56d3559d6e705f130f9c50d79d2a6c4a336_2_690x426.png" alt="image" data-base62-sha1="kFL9BPhR4zuO6RguSdnL1z2wUo6" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90e3f56d3559d6e705f130f9c50d79d2a6c4a336_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90e3f56d3559d6e705f130f9c50d79d2a6c4a336_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90e3f56d3559d6e705f130f9c50d79d2a6c4a336_2_1380x852.png 2x" data-dominant-color="447EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1394 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After adjusting the log level, the debug message logging function disappeared from the call tree and all the time-consuming functions make sense (they are complex and/or frequent operations):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81d583739ba71663acd30c2a82dde23695b7a616.png" data-download-href="/uploads/short-url/iwz2JXGCBO1WiYK9B6lfX0QKKKG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81d583739ba71663acd30c2a82dde23695b7a616_2_690x427.png" alt="image" data-base62-sha1="iwz2JXGCBO1WiYK9B6lfX0QKKKG" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81d583739ba71663acd30c2a82dde23695b7a616_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81d583739ba71663acd30c2a82dde23695b7a616_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81d583739ba71663acd30c2a82dde23695b7a616_2_1380x854.png 2x" data-dominant-color="588DB6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1397 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @keri (2021-07-15 10:24 UTC)

<p>Thank you very much! It was my first time using profiler utility</p>
<p>I understood your idea (I didn’t know anything about <code>logging</code> before). I checked that according to <a href="https://docs.python.org/3/library/logging.html#logging-levels" rel="noopener nofollow ugc">this table</a> Slicer’s logging level (<code>logging.getLogger().level</code>) is set to 10 <code>DEBUG</code> while when working in cmd I can see that logging level is set to 30 <code>WARNING</code></p>
<p>I will report that to lasio developers, thank you</p>

---
