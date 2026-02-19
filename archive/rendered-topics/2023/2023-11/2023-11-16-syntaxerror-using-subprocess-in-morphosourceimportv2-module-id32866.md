---
topic_id: 32866
title: "Syntaxerror Using Subprocess In Morphosourceimportv2 Module"
date: 2023-11-16
url: https://discourse.slicer.org/t/32866
---

# SyntaxError Using subprocess in MorphoSourceImportV2 Module

**Topic ID**: 32866
**Date**: 2023-11-16
**URL**: https://discourse.slicer.org/t/syntaxerror-using-subprocess-in-morphosourceimportv2-module/32866

---

## Post #1 by @othomas2 (2023-11-16 18:21 UTC)

<p>Hello Slicer Community,</p>
<p>I’m developing a module, <code>MorphoSourceImportV2</code>, for 3D Slicer to download media from MorphoSource in the background. However, I’ve encountered a <code>SyntaxError</code> when trying to use the <code>subprocess</code> module within Slicer.</p>
<p>File “/Applications/Slicer.app/Contents/bin/…/lib/Python/lib/python3.9/site.py”, line 178<br>
file=sys.stderr)<br>
^<br>
SyntaxError: invalid syntax</p>
<p>This error arises when I attempt to run a subprocess for downloading media files.</p>
<p><strong>Module Repository</strong>: The module’s code is available in my forked repository: <a href="https://github.com/oothomas/SlicerMorph/tree/master/MorphoSourceImportV2" rel="noopener nofollow ugc">MorphoSourceImportV2 on GitHub</a>.</p>
<p>I would greatly appreciate any insights or suggestions you might have on resolving this issue. If anyone has experience with using <code>subprocess</code> in Slicer or has encountered similar problems, your guidance would be invaluable.</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @muratmaga (2023-11-16 19:00 UTC)

<p>I bit more context to this question:</p>
<p>These downloads are long (multiple GBs per file), and can be multiple dataset. We do not want the Slicer UI to be non-responsive during downloads, which should happen in the background.</p>
<p>Any suggestions to do this would be appreciated.</p>

---

## Post #3 by @pieper (2023-11-16 20:04 UTC)

<p>Doing the downloads in a subprocess makes sense.  You could look at how the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMProcesses.py">DICOMProcess code handles this</a>.  Basically a <code>QProcess</code> is started as the process downloads data the main Slicer process gets signals that tell it when to read the results.  The <a href="https://github.com/pieper/SlicerParallelProcessing">ParallelProcessing</a> extension code works the same way and might be easier to read.</p>

---

## Post #4 by @othomas2 (2023-11-16 21:17 UTC)

<p>Thank you, Steve! I’ll try these approaches.</p>

---

## Post #5 by @othomas2 (2023-11-16 22:24 UTC)

<p>I’ve successfully used <code>subprocess.Popen</code> to run an external Python script (<code>download_script.py</code>) from within a Slicer module, and it’s working great for downloading data. However, I have a couple of questions regarding best practices for script placement and specifying the Python interpreter in Slicer:</p>
<ol>
<li><strong>Script Location:</strong> Currently, <code>download_script.py</code> is located in the same folder as the module file. I’ve specified its file path explicitly in the code. Is this the recommended location for such scripts, or should they be placed elsewhere? Additionally, is there a way to reference the script’s location relative to the module file, to make the module more portable?</li>
<li><strong>Python Interpreter Path:</strong> For the Python interpreter, I’ve used a hard-coded path to Slicer’s Python (<code>/Applications/Slicer.app/Contents/bin/PythonSlicer</code>). However, I’m wondering if there’s a more dynamic way to reference the interpreter, perhaps using <code>sys.executable</code> or a similar approach. This would be particularly useful for ensuring the module’s compatibility across different systems and Slicer installations.</li>
</ol>
<p>Steve, thanks again for your help! I look forward to your response. It would be helpful not only for refining my current module but also for guiding best practices for the Slicer developer community.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cfc199878944394bba32a133e6eeea95bb5c4b6.png" data-download-href="/uploads/short-url/dgA32mSxUhHYzulQBrMawQbW4Ci.png?dl=1" title="Screen Shot 2023-11-16 at 2.19.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cfc199878944394bba32a133e6eeea95bb5c4b6.png" alt="Screen Shot 2023-11-16 at 2.19.29 PM" data-base62-sha1="dgA32mSxUhHYzulQBrMawQbW4Ci" width="690" height="202" data-dominant-color="24282F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-11-16 at 2.19.29 PM</span><span class="informations">846×248 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2023-11-17 02:33 UTC)

<aside class="quote no-group" data-username="othomas2" data-post="5" data-topic="32866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/848f3c/48.png" class="avatar"> othomas2:</div>
<blockquote>
<p>Is this the recommended location for such scripts, or should they be placed elsewhere?</p>
</blockquote>
</aside>
<p>I think supplementary files for modules go under Resources/ folder of the module hierarchy.</p>
<aside class="quote no-group" data-username="othomas2" data-post="5" data-topic="32866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/848f3c/48.png" class="avatar"> othomas2:</div>
<blockquote>
<p>script’s location relative to the module file, to make the module more portable?</p>
</blockquote>
</aside>
<p><code>slicer.util.modulePath('MorphoSourceImportV2')</code><br>
returns the path of python script for your module. If you put the <code>download_script.py</code> within the Resources folder then you can paste these together to form the correct path that will be portable</p>
<aside class="quote no-group" data-username="othomas2" data-post="5" data-topic="32866">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/848f3c/48.png" class="avatar"> othomas2:</div>
<blockquote>
<p>owever, I’m wondering if there’s a more dynamic way to reference the interpreter,</p>
</blockquote>
</aside>
<p><code>os.getcwd()</code><br>
returns the path of where slicer install tree is (i.e., working directory for the python console)<br>
<code> 'C:\\Users\\amaga\\AppData\\Local\\slicer.org\\Slicer 5.4.0'</code></p>
<p>so, the path of the Python interpreter is <strong>bin/PythonSlicer</strong> under this tree.</p>
<pre><code class="lang-auto">os.path.exists("bin/PythonSlicer.exe")
True
</code></pre>

---

## Post #7 by @pieper (2023-11-17 14:06 UTC)

<p><a class="mention" href="/u/othomas2">@othomas2</a> I suggest you change from using subprocess.Popen and instead use QProcess for use within Slicer.  The reason is that QProcess integrates with the Qt event loop for the application, so that instead of relying on. timer, you can be notified of events from the process as they happen.  This is a cleaner approach and in general it is more efficient and provides a smoother user experience.</p>
<p>I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> 's suggestions about using the Resources directory and locating it relative to the module path for consistency across os platforms.  Do avoid using <code>.exe</code> as that is windows specific.</p>

---
