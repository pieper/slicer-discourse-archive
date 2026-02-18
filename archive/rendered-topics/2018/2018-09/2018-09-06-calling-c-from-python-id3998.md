# Calling C++ from Python

**Topic ID**: 3998
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/calling-c-from-python/3998

---

## Post #1 by @Saima (2018-09-06 03:44 UTC)

<p>Hi Andras,<br>
is it possible to call external c++ customised functions using slicer python.</p>

---

## Post #2 by @ihnorton (2018-09-06 04:32 UTC)

<p>(I moved this to a new topic – please start a new topic for new questions, rather than replying to the old one)</p>

---

## Post #3 by @lassoan (2018-09-06 05:03 UTC)

<aside class="quote no-group" data-username="Saima" data-post="1" data-topic="3998">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>is it possible to call external c++ customised functions using slicer python.</p>
</blockquote>
</aside>
<p>Yes. Most of Slicer core is implemented in C++, so you usually call C++ functions from Slicer’s Python interpreter. If you implement a C++ loadable module then you can call the methods implemented in them, too.</p>

---

## Post #4 by @Saima (2018-09-06 08:32 UTC)

<p>how to call any examples available</p>

---

## Post #5 by @lassoan (2018-09-06 18:21 UTC)

<p>For example, MRML nodes are implemented in C++. You can call their methods as you would do it for any native Python class:</p>
<pre><code>node = slicer.mrmlScene.GetFirstNodeByName("Red")
print(node.GetName())</code></pre>

---

## Post #6 by @Saima (2018-09-15 09:49 UTC)

<p>Hi Andras,<br>
If I have an external implementation of an algortihm in c++ and want to call it from python. how to do that. the implementation is outside the slicer enviornment but is in c++</p>

---

## Post #7 by @lassoan (2018-09-15 13:17 UTC)

<p>The easiest is to create a CLI module in C++ and call that from Python. First (and hardest) step is to build Slicer, then follow Slicer developer tutorials.</p>

---

## Post #8 by @pieper (2018-09-16 13:43 UTC)

<p>If you already have another executable that reads and writes Slicer compatible data like nifti files, and if you want to avoid having to build slicer from source, then another option is to make a wrapper so that the other program looks like a Slicer CLI.</p>
<p>Here’s an example:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/ouyangming/DRAMMS_in_Slicer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ouyangming/DRAMMS_in_Slicer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/20e126d9412ccfab910b4b24edb9f2a1490ee3c32a69d8fdee920e5e919ab5b4/ouyangming/DRAMMS_in_Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/ouyangming/DRAMMS_in_Slicer" target="_blank" rel="noopener">GitHub - ouyangming/DRAMMS_in_Slicer: dramms integrated into slicer</a></h3>

  <p>dramms integrated into slicer. Contribute to ouyangming/DRAMMS_in_Slicer development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that if the other program uses shared libraries or python packages you may need to manipulate the environment’s path variables to make sure the program resolves correctly.</p>

---

## Post #9 by @Saima (2018-09-18 01:23 UTC)

<p>Hi Andras,<br>
Can you please post the tutorials. I build the slicer previously. when I run slicer.exe it opens up slicer but it also show me text below: what does this mean? is it not successfully build.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a11ae2db3f4646c4fcccf733626d96b0858e484.png" data-download-href="/uploads/short-url/jHpLNCbbI5XwrlOJs66mufLnDcE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a11ae2db3f4646c4fcccf733626d96b0858e484_2_690x388.png" alt="image" data-base62-sha1="jHpLNCbbI5XwrlOJs66mufLnDcE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a11ae2db3f4646c4fcccf733626d96b0858e484_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a11ae2db3f4646c4fcccf733626d96b0858e484_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a11ae2db3f4646c4fcccf733626d96b0858e484_2_1380x776.png 2x" data-dominant-color="212121"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Saima (2018-09-18 01:24 UTC)

<p>Hi Andras,<br>
Can you please refer to a good and easy to understand example for creating a CLI module in c++ and call from python.</p>

---

## Post #11 by @lassoan (2018-09-18 03:33 UTC)

<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="3998">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I build the slicer previously. when I run slicer.exe it opens up slicer but it also show me text below: what does this mean? is it not successfully build.</p>
</blockquote>
</aside>
<p>It seems that the build partially failed. I would recommend to build latest master version of Slicer (it’ll become stable within a few weeks) and following all recommendations in build instructions. For example, build might have failed because the build folder name is too long. It has to be really short, up to a few characters - for example C:\S4 for source and C:\S4D / C:\S4R for debug/release mode binary works.</p>
<aside class="quote no-group" data-username="Saima" data-post="10" data-topic="3998">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>example for creating a CLI module in c++</p>
</blockquote>
</aside>
<p>These should help:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">Slicer4_Programming_Tutorial</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_CLI_module_from_Python.3F">How to run a CLI module from Python</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Developing_and_contributing_extensions_for_3D_Slicer">Developing and contributing extensions for 3D Slicer</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Command_Line_Interface_.28CLI.29">Create CLI module</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers">Developer manual</a></li>
</ul>

---

## Post #12 by @Saima (2019-07-15 03:03 UTC)

<p>Hi peiper,<br>
I would need to know how to make a wrapper for externall c++ code. Could be please refer me to any good websites or examples.</p>
<p>Thank you</p>

---

## Post #13 by @pieper (2019-07-15 12:47 UTC)

<p>The typical way is to use something like SWIG, as done in <a href="https://github.com/InsightSoftwareConsortium/ITKModuleTemplate" rel="nofollow noopener">ITK</a>.</p>
<p>Or you could do <a href="https://docs.python.org/3/extending/extending.html" rel="nofollow noopener">something in python</a>.</p>
<p>Or as Andras points out above, pretty much any C++ code in Slicer that extends VTK or Qt gets wrapped for python automatically.</p>
<p>Hope that helps.</p>

---

## Post #14 by @Saima (2019-07-16 01:24 UTC)

<p>is boost.python ok to use instead of swig or are there any limitations.</p>

---

## Post #15 by @pieper (2019-07-16 11:48 UTC)

<p>I believe anything that works for normal python would be okay.  I’ve never tried boost.python but I suppose it would work.  Just keep in mind that if you plan to redistribute your code there can be lots of issues making sure the libraries are all packaged and (on mac) fixed up correctly.  The safest course is usually just to follow the exact pattern of something that is already maintained and known to work.</p>

---

## Post #16 by @lassoan (2019-07-16 12:21 UTC)

<aside class="quote no-group" data-username="Saima" data-post="14" data-topic="3998" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>is boost.python ok to use instead of swig or are there any limitations.</p>
</blockquote>
</aside>
<p>Is there a specific reason you would not like to implement a Slicer CLI module? You can run it in Slicer using GUI and from Python and C++, or you can even using without Slicer, just running it as a standalone executable from the command line.</p>

---

## Post #17 by @Saima (2019-07-18 01:05 UTC)

<p>Hi Andras,<br>
I could not find good documentation for CLI modules. Although there are good documentations and presentation for scripting modules but I need some good documentation for working on CLI modules. I am a just a beginner.</p>
<p>Could you please provide me with helpful documentation?</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #18 by @lassoan (2019-07-18 02:18 UTC)

<p>Would you like to implement CLI modules or run them from Python? Would you like to implement in CLI module in Python or in C++?</p>

---

## Post #19 by @Saima (2019-07-18 02:42 UTC)

<p>I have an external c++ project. I need an interface to interact through slicer python with that project without disturbing the c++ project code itself.</p>
<p>Any suggestions please?  Sorry if I confuse you with what I want to explain. Previously you told to make c++ loadable modules and then call it though slicer python.</p>
<p>then you suggested to build CLI module in c++ and call it from python. I am confused with what to follow.</p>
<p>I will be using slicer extensions as well the segment mesher and skull stipper. Along with that I need an interface to call the external c++ project.</p>

---

## Post #20 by @lassoan (2019-07-19 00:56 UTC)

<p>Implement a CLI module in C++ is probably the best way to go, as it is simpler, processing can run in the background, etc. I would only recommend implementing a loadable module instead, if you need to re-run the processing very frequently (many times per second) and so passing data to the CLI would become the bottleneck; or you need to pass many or very complex data structures that are not readily supported by the CLI interface.</p>

---
