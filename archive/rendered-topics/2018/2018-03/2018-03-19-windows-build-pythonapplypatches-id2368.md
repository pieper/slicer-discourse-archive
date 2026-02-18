# Windows Build PythonApplyPatches

**Topic ID**: 2368
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/windows-build-pythonapplypatches/2368

---

## Post #1 by @darekdev (2018-03-19 23:41 UTC)

<p>Hello everyone,</p>
<p>I want to build Slicer Nightly in Windows 10 environment(VS 2013). I follow instruction from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a> and I can’t build all python packages: cmake throw only information about error in PythonApplyPatches.cmake and nothing else.<br>
I succesfully built qt(4.8.7) and made all steps from build instructions site. Before this I had problem with patches executables but then I selected path to git binaries and now I stuck on patches. Additionaly, this is fresh Windows 10 install.</p>
<p>Darek</p>

---

## Post #2 by @ihnorton (2018-03-20 13:59 UTC)

<p>Please post the error messages.</p>
<p>(please use triple-backtick before and after so it is more readable: <code>```</code>; or post on <a href="http://gist.github.com">gist.github.com</a> and link)</p>

---

## Post #3 by @lassoan (2018-03-20 20:10 UTC)

<p>If you install git at the default install location then the build system should be able to find patch.exe. If not, then you can try to specify this CMake variable manually when you configure Slicer:</p>
<pre><code>Patch_EXECUTABLE:FILEPATH=C:/full/path/to/patch.exe</code></pre>

---

## Post #4 by @darekdev (2018-03-20 20:54 UTC)

<p>Thank you for respond.<br>
Yes, it was problem with patch.exe and git.exe (should be git.exe from cmd folder).<br>
I reinstalled git and added it in installation step to PATH. Then CMAKE read all  settings automatically.</p>
<p>Now I’m fighting with CTK:</p>
<blockquote>
<p>IOError: [Errno 2] No such file or directory: ‘E:/software/Slicer-SuperBuild-Release/CTK/Lbs/Widgets/ctkFileDialogEventTranslator.h’</p>
</blockquote>
<p>And why there is Lbs not Libs?</p>

---

## Post #5 by @lassoan (2018-03-20 21:24 UTC)

<p>Windows deletes every 8192th character from your command line, which causes the error that you see.</p>
<p>The solution is to build Slicer in a shorter directory as it makes command-line argument lists shorter.</p>
<p>I typically use C:\S4 for storing source files and build in C:\S4R or S4D. 1-2 characters longer should work, too. Anything much longer may fail to build (if you are lucky the 8192th character corrupts a non-essential value and then the build may succeed, but it is better not to bet on that).</p>

---

## Post #6 by @darekdev (2018-03-20 21:29 UTC)

<p>Ehh. Now I need to recompile all…<br>
Do you use \MP option for faster compiling? All day compiling behind me. And now again.</p>

---

## Post #7 by @lassoan (2018-03-21 03:41 UTC)

<p>I don’t use MP option, I’ve tried at some point but the improvement on my computers were not noticeable (takes a couple of hours).</p>

---

## Post #8 by @darekdev (2018-03-24 11:25 UTC)

<p>Build successfully. In summary:</p>
<ul>
<li>correctly install git and set PATHS or remember about binaries in cmd folder</li>
<li>on the beggining build path as short as possible.</li>
</ul>
<p>But I have another problem. I can’t <strong>import scipy</strong>(Successfully installed scipy-1.0.0):</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “E:\Program Files\Slicer 4.9.0-2018-03-21\lib\Python\Lib\site-packages\scipy_<em>init</em>_.py”, line 118, in <br>
from scipy._lib._ccallback import LowLevelCallable<br>
File “E:\Program Files\Slicer 4.9.0-2018-03-21\lib\Python\Lib\site-packages\scipy_lib_ccallback.py”, line 1, in <br>
from . import _ccallback_c<br>
ImportError: DLL load failed: Procedura inicjowania biblioteki do³¹czanej dynamicznie (DLL) nie powiod³a siê.</p>
</blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf8c46f2ce583f9d6c1484eb6fe8f3234cf36e4.jpeg" alt="Nowy%20obraz%20mapy%20bitowej" data-base62-sha1="jYflH5PWQ5PXXlqIIzGp8w2G7Lm" width="397" height="242"></p>
<p>I tried install intel mkl and made some research about numpy+mkl, but without success. On linux works like a charm.</p>

---

## Post #9 by @ihnorton (2018-03-24 11:55 UTC)

<p>Assuming you used pip to install: the most likely problem is that Scipy is linked against a different and incompatible CRT (C Runtime – msvcrt). The upstream Scipy for Python 2.7 is built with Visual Studio 2008. We are planning to switch to Python 3 in the future, which will allow to use packages built with Visual Studio 2015, which should be ABI compatible.</p>
<p>(also, Microsoft has updated the CRT model to eliminate – supposedly – the CRT compatibility issues starting with VS2015)</p>

---

## Post #10 by @darekdev (2018-03-24 12:10 UTC)

<p>I understand that now I can’t do anything with that problem and should work without scipy?</p>

---

## Post #11 by @lassoan (2018-03-24 13:53 UTC)

<p>You can use Slicer with conda and install any conda packages. I’ve done this in the past successfully. The only catch is that you need to build Slicer on your computer and instead of letting Slicer build its own Python, configure in CMake to use conda instead. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration">https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration</a></p>

---

## Post #12 by @jcfr (2018-03-25 02:10 UTC)

<aside class="quote no-group" data-username="darekdev" data-post="10" data-topic="2368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>with that problem and should work without scipy?</p>
</blockquote>
</aside>
<p>On Linux, you can definitively install itk, scipy, tensorflow, etc … within the Slicer environment. But if you can’t switch environment, options are currently limited.</p>

---

## Post #13 by @darekdev (2018-03-25 09:23 UTC)

<p>Thank you all for answers. I am going try with conda.<br>
I have got linux environment and I have been working 3 years with Slicer.</p>

---
