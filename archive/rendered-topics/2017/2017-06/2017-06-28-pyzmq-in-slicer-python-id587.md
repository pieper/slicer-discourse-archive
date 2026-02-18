# Pyzmq in slicer python

**Topic ID**: 587
**Date**: 2017-06-28
**URL**: https://discourse.slicer.org/t/pyzmq-in-slicer-python/587

---

## Post #1 by @Filipe_Trocado_Ferre (2017-06-28 13:03 UTC)

<p>Operating system: Ubuntu 16<br>
Slicer version: 4.7<br>
Expected behavior:<br>
Actual behavior: Can’t Import pyzmq</p>
<p>Is there any way one could import pyzmq into slicer python module ? I want to process 3d scans in my python modules that I can’t install in slicer. At least communication support should be able to do.</p>

---

## Post #2 by @lassoan (2017-06-28 13:07 UTC)

<p>Slicer can receive surfaces, volumes, transforms, etc. in real-time through <a href="http://www.openigtlink.org">OpenIGTLink protocol</a>. There are a couple of Python implementations of OpenIGTLink (I haven’t tried them, it would be great if you could try them and report back), so it would be probably much simpler to use that protocol instead. You can set up connections in OpenIGTLinkIF module.</p>

---

## Post #3 by @Filipe_Trocado_Ferre (2017-06-28 14:33 UTC)

<p>At first sight, None of these (<a href="https://github.com/Danielhiversen/pyIGTLink" rel="nofollow noopener">https://github.com/Danielhiversen/pyIGTLink</a> ; <a href="https://github.com/nenetto/OpenIGTLink/tree/master/Notebooks" rel="nofollow noopener">https://github.com/nenetto/OpenIGTLink/tree/master/Notebooks</a>) implement image sending and receiving using igtlink protocol.</p>

---

## Post #4 by @ihnorton (2017-06-28 14:48 UTC)

<p>The first one has an <a href="https://github.com/Danielhiversen/pyIGTLink/blob/07cf0759f6a1901c008c945a6336c355c43f45f6/pyIGTLink/pyIGTLink.py#L483-L501">example</a> of sending a numpy array as an image message.</p>
<p>For zmq, recent Slicer nightly versions include pip, and should be able to download a pre-compiled (wheel) version. In the slicer python prompt: <code>import pip; pip.main(['install', 'PyZMQ'])</code></p>
<p>That said, Andras’ suggestion is still better because:</p>
<ul>
<li>you need to very careful with the event loop among python, slicer, qt, etc. and this work has already been done for OpenIGTLink</li>
<li>I’m not sure what the Slicer + wheel (pypi) compatibility level is across platforms. I believe there is/was at least one weird shared library compatibility issue on linux for pyradiomics.</li>
</ul>

---

## Post #5 by @Filipe_Trocado_Ferre (2017-06-28 15:03 UTC)

<p>You’re right. I think i’ll have to mesh both implementation to achieve both send/receive images.<br>
Thank you both!</p>

---

## Post #6 by @lassoan (2017-06-28 15:05 UTC)

<p>You cannot get precompiled binary python packages on Windows (Slicer uses Python 2.7 and VS2013).</p>
<p>It would be great if you could test these Python OpenIGTLink implementations. If you find a nice, promising one then we would be happy to help with fixing issues or extending it to additional message types, etc.</p>

---

## Post #7 by @ihnorton (2017-06-28 15:16 UTC)

<p>Be aware that the second implementation is <a href="https://en.wikipedia.org/wiki/GNU_General_Public_License">GPL licensed</a>, so you need to abide by the GPL provisions. Practically: any derived code must also be provided under GPL (there are many in-depth discussions on the internet of the implications).</p>

---

## Post #8 by @lassoan (2017-06-28 15:31 UTC)

<p>Thanks for checking. I can only afford to spend time with code that we can use without restrictions, so it would be important to choose something based on BSD, MIT or similar license.</p>

---
