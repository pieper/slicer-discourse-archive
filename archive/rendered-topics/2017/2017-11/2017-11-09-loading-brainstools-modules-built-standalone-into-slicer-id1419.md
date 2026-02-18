# Loading BRAINSTools modules built standalone into Slicer

**Topic ID**: 1419
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/loading-brainstools-modules-built-standalone-into-slicer/1419

---

## Post #1 by @DTI (2017-11-09 14:33 UTC)

<pre><code class="lang-auto">Operating system : Mac OS X Version 10.12.6
Slicer version   : 4.6.2
Expected behavior: Have all BRAINSTools extensions installed in the Slicer GUI (especially GTRACT).
Actual behavior  : I downloaded the BRAINSTools from GitHub [1] to './Documents/GitHub/brains/BRAINSTools' 
                   and built it with CMake into a subfolder called 'build'. 

[1] https://github.com/BRAINSia/BRAINSTools.git
</code></pre>
<p>How can I now make the extensions appear in  Slicer GUI?</p>
<p>Thanks, Lorenz</p>

---

## Post #2 by @jcfr (2017-11-10 00:40 UTC)

<p>Hi,</p>
<p>Few remarks / questions:</p>
<p>Could you confirm that you built BRAINSTools as standalone project ?</p>
<blockquote>
<p>Slicer 4.6.2</p>
</blockquote>
<p>If you don’t have specific reason to use this version, you could use Slicer 4.8 or even download the nighty build</p>
<blockquote>
<p>make the extensions appear in Slicer GUI?</p>
</blockquote>
<p>Generally speaking, you could add the directory to the settings or use <code>--additonal-module-paths</code> command line argument. More details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Additional_module_paths" class="inline-onebox">Documentation/Nightly/SlicerApplication/ApplicationSettings - Slicer Wiki</a></p>
<p>In that particular case, to ensure  that the built CLIs load, it is recommended to build BRAINStools statically.</p>
<p>Otherwise, if BRAINSTools is statically built, the executables will try to dynamically resolve symbols against the ITK libraries bundled in Slicer which may be slightly different than the one used to build BRAINSTools.</p>

---

## Post #3 by @DTI (2017-11-10 17:35 UTC)

<p>Hi Jean</p>
<p>Thank you for your prompt response. Regarding your question: Yes, I built BRAINSTools as a standalone project.<br>
However, it’s the first time I have done that and therefore I don’t know how the result of the building process has to look in the end. What kind of files should I expect? Now I have a lot of different subfolders with the names of the different BRAINSTools modules containing files with extensions such as .xml, .cxx, .h, etc. So I’m not even sure the building process was completed correctly. Regardless of that, I downloaded as you suggested the newest nightly build version of Slicer and added my BRAINSTools folder to the paths for modules in Slicer GUI (Edit-&gt;Applications Settings-&gt;Modules). The BRAINSTools modules still don’t show up upon restart.</p>
<p>Thanks for your help!</p>
<p>Best regards, Lorenz</p>

---
