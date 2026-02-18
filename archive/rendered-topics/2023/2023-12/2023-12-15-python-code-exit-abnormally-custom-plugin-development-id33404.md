# Python code exit abnormally. custom plugin development

**Topic ID**: 33404
**Date**: 2023-12-15
**URL**: https://discourse.slicer.org/t/python-code-exit-abnormally-custom-plugin-development/33404

---

## Post #1 by @IVarha (2023-12-15 15:57 UTC)

<p>Hello I am developing a plugin for my research and encountering with a problem when I am running certain code. However error is not reproducible when I am running same code on  PythonSlicer (built in in slicer). Here I attach code and logs from correct run in slicerpython and slicer error failed<br>
slicerpython log:</p>
<blockquote>
<pre><code>    *:~$ /home/user/slic_build/python-install/bin/PythonSlicer*
    Python 3.9.10 (main, Dec 12 2023, 14:56:38)
    [GCC 11.4.0] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    &gt;&gt;&gt; from brainextractor import BrainExtractor
    &gt;&gt;&gt; import nibabel as nib
    &gt;&gt;&gt; image = nib.load("/tmp/tmp14016ra4/t1.nii.gz")
    &gt;&gt;&gt; vet = BrainExtractor(image)
    &gt;&gt;&gt; vet.run()
     vet.run()
    Running surface deformation...
    Iteration: 999
    Complete.
</code></pre>
</blockquote>
<p>SLICER RUN:</p>
<blockquote>
<p>Running surface deformation…<br>
error: [/home/user/slic_build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>

---

## Post #2 by @RafaelPalomar (2023-12-18 06:13 UTC)

<p><a class="mention" href="/u/ivarha">@IVarha</a>, did you installed any python packages within the 3D Slicer environment with <code>pip</code> (i.e., brainextractor)? Installing certain packages with <code>pip</code> may override the version of those packages provided by Slicer, sometimes producing crashes. If you have built your own Slicer, you could try to provide more information using a debugger:</p>
<p><a href="https://slicer.readthedocs.io/en/5.6/developer_guide/debugging/linuxcpp.html#c-debugging-on-gnu-linux-systems" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging on GNU/Linux systems — 3D Slicer documentation</a></p>

---

## Post #3 by @IVarha (2023-12-19 18:59 UTC)

<p>You are right I installed some other packages through pip. However as I mentioned when I use python which is used in slicer it works. Is C++ debugging my only option?(I use Wsl, therefore not sure it would be easy to install)</p>

---

## Post #4 by @RafaelPalomar (2023-12-22 06:29 UTC)

<p><a class="mention" href="/u/ivarha">@IVarha</a>, package collision is one hypothesis, to get a better picture of the error debugging is the way. I’ve never used WSL, but it seems it is possible:</p>
<aside class="quote quote-modified" data-post="1" data-topic="16022">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-can-be-built-and-runs-well-on-windows-subsystem-for-linux-wsl2/16022">Slicer can be built and runs well on Windows Subsystem for Linux (WSL2)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Some information for Windows developers who want to develop/test Slicer on Linux. On current Windows 10 versions, it is very easy to install Linux and run Linux GUI applications such as Slicer, by using Windows Subsystem for Linux (WSL2). 
Ubuntu 20.04 shows up as an app in Microsoft Store. If you install and run it you get a linux terminal. By copy-pasting 10-20 lines you can install kubuntu desktop and you can connect to it using Windows remote desktop as explained <a href="https://www.nextofwindows.com/how-to-enable-wsl2-ubuntu-gui-and-use-rdp-to-remote" rel="noopener nofollow ugc">here</a>. 
Slicer build instruct…
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2023-12-22 12:11 UTC)

<p>You can use the <a href="https://github.com/lassoan/SlicerHDBrainExtraction">HDBrainExtraction</a> extension in Slicer.</p>

---
