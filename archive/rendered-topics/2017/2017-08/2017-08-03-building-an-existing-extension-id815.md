# Building an existing extension

**Topic ID**: 815
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/building-an-existing-extension/815

---

## Post #1 by @crossmanith (2017-08-03 15:34 UTC)

<pre><code class="lang-auto">Operating system  : Linux 4.4.25-040425-generic (Ubuntu 16.04.2 LTS)
Slicer version    : Slicer-4.7.0-2017-07-10-linux-amd64
Expected behavior : -
Actual behavior   : -
</code></pre>
<p><code>DTIProcess</code> is available as extension for Slicer but the Extension Manager can’t find it.</p>
<p>Probably because it is a very recent version of Slicer.</p>
<p>I’ve cloned <code>DTIProcess</code> from github but don’t have an idea how to build it as an extension. Any hints how to proceed?</p>
<p>Regards,<br>
Christina Roßmanith</p>
<p>Dept. of Neurology<br>
University Medicine Mannheim<br>
University of Heidelberg</p>

---

## Post #2 by @pieper (2017-08-03 18:33 UTC)

<p>Hi  -</p>
<p>It looks like there’s a build error on the linux version of DTIProcess at the moment:</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1074584" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1074584</a></p>
<p>but windows and mac appear to be working.</p>
<p>If you don’t hear more on this forum you could contact the authors listed here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DTIProcess" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DTIProcess</a></p>
<p>To answer your original question, you can do what is described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a></p>
<p>It requires also building Slicer on your machine (and the build error from the extension factory will need to be fixed)</p>

---

## Post #3 by @crossmanith (2017-08-04 09:40 UTC)

<p>I’ve built DTIProcess locally but had to add the line “set( CMAKE_CXX_STANDARD_REQUIRED ON )” to SuperBuild.cmake of DTIProcess to make the " CXX_STANDARD is set to invalid value ‘’ errors disappear. I’ve emailed Francois already. Maybe they modify the DTIProcess SuperBuild.cmake - if the fix is feasible. Is there a way to influence building DTIProcess from the Slicer build process and to add this option there, too?</p>

---

## Post #4 by @pieper (2017-08-04 13:02 UTC)

<p>Glad you got it working - I’m not sure if this is something specific to DTIProcess or something that might apply to all extensions.  My guess is that your change should be applied in the DTIProcess code.</p>

---
