# Import and use existing code/library in a new module

**Topic ID**: 23262
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/import-and-use-existing-code-library-in-a-new-module/23262

---

## Post #1 by @llafitte007 (2022-05-03 13:42 UTC)

<p>Hi,</p>
<p>in a previous work, I made a c++ library usable from a python program (using the cython tool). It works perfectly but has to be run from the command line.</p>
<p>Now I’m trying to develop a module that would allow to launch automatically some features of this library from the Slicer interface.</p>
<p>I manage to import the python code of my library (by adding the path in sys.path) but this code imports a .so/.pyx library compiled with cython and which does not work. (I don’t know if I’m making myself understood …)</p>
<p>The console error when I start Slicer :</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/llafitte007/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "/home/llafitte007/__CODE__/primetimeire/SlicerExtensions/Primetime/NeedlesCoordinates/NeedlesCoordinates.py", line 23, in &lt;module&gt;
    from NeedlesExtraction import NeedlesExtraction, PrimetimeConfiguration, Image
  File "/home/llafitte007/__CODE__/primetimeire/NeedlesExtraction.py", line 6, in &lt;module&gt;
    from wrappers import PyIrenaUtils
  File "/home/llafitte007/__CODE__/primetimeire/wrappers/__init__.py", line 1, in &lt;module&gt;
    from .PyIrena import PyIrena, PyIrenaPatient, PyIrenaUtils
  File "/home/llafitte007/__CODE__/primetimeire/wrappers/PyIrena/__init__.py", line 8, in &lt;module&gt;
    from PyIrena import PyIrena, PyIrenaPatient, PyIrenaUtils, ptype, ConfigKey
ModuleNotFoundError: No module named 'PyIrena'
</code></pre>
<p>Someone could help me ?</p>
<p>To resume, I tried to use a .so/.pyx library imported from a file I imported in a Slicer module … <img src="https://emoji.discourse-cdn.com/twitter/face_with_raised_eyebrow.png?v=12" title=":face_with_raised_eyebrow:" class="emoji" alt=":face_with_raised_eyebrow:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @Alex_Vergara (2022-05-03 14:44 UTC)

<aside class="onebox stackexchange" data-onebox-src="https://stackoverflow.com/questions/10968309/how-to-import-python-module-from-so-file">
  <header class="source">

      <a href="https://stackoverflow.com/questions/10968309/how-to-import-python-module-from-so-file" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/463758/balki" target="_blank" rel="noopener nofollow ugc">
    <img alt="balki" src="https://www.gravatar.com/avatar/105689a9cb392f18c1d0b27ed0cf657f?s=256&amp;d=identicon&amp;r=PG&amp;f=1" class="thumbnail onebox-avatar" width="256" height="256">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/10968309/how-to-import-python-module-from-so-file" target="_blank" rel="noopener nofollow ugc">How to import python module from .so file?</a>
</h4>

<div class="tags">
  <strong>c++, python, boost-python</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/463758/balki" target="_blank" rel="noopener nofollow ugc">
    balki
  </a>
  on <a href="https://stackoverflow.com/questions/10968309/how-to-import-python-module-from-so-file" target="_blank" rel="noopener nofollow ugc">11:32AM - 10 Jun 12 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @llafitte007 (2022-05-03 15:49 UTC)

<p>I tried but it doesn’t work and I can’t show you the error… because nothing happens !</p>
<p>Slicer tries to open (loading window) then nothing : no error in the terminal, nothing !</p>
<p>I continue the investigation and I will keep you informed</p>

---

## Post #4 by @llafitte007 (2022-05-04 08:37 UTC)

<p>After several tests, it seems when Slicer started and load the library this makes it crash (absolutely no errors in console)</p>
<p>I tried manually it in base python console and it’s work<br>
I tried manually in slicer python console and it makes crash slicer without output errors.</p>
<p>Any idea what could cause slicer to crash when loading a library?</p>
<p>edit : can it be due to a different version of python between slicer (3.6) and during the build of the lib (3.8) ?</p>

---

## Post #5 by @Alex_Vergara (2022-05-04 09:50 UTC)

<aside class="quote no-group" data-username="llafitte007" data-post="4" data-topic="23262">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ba0ec/48.png" class="avatar"> llafitte007:</div>
<blockquote>
<p>edit : can it be due to a different version of python between slicer (3.6) and during the build of the lib (3.8) ?</p>
</blockquote>
</aside>
<p>This is the thing. Try using the last version of slicer with python 3.9 and please try to compile your library also in python 3.9</p>

---

## Post #6 by @llafitte007 (2022-05-05 09:25 UTC)

<p>After recompile the library with python 3.9 and use Slicer 5.1  (also with python3.9) all work fine.</p>
<p>Also, for information with python3.9 there is a clear warning message when loading a library with wrong version python.</p>

---
