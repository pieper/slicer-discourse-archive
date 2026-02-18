# How to start Qt designer in Slicer environment from Ubuntu 20.04?

**Topic ID**: 13549
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/how-to-start-qt-designer-in-slicer-environment-from-ubuntu-20-04/13549

---

## Post #1 by @Fabiola (2020-09-18 15:50 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11.0-2020<br>
Expected behavior: ./Slicer-build/Slicer --designer shouldn’t start the Qt Designer?<br>
Actual behavior: it starts the Slicer application.</p>
<p>Hello Slicer community, a beginner here.<br>
Installed Qt 5.15; Qt designer 5.12.8. Built successfully the Slicer debug/release version. But unable to access the Slicer and CTK widgets because I can’t start Qt designer in Slicer environment. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
Can anyone help me please?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2020-09-18 16:12 UTC)

<p>For some reason, the convenience <code>--designer</code> application shortcut is not specified for linux. You can run designer in your install tree like this (assuming you used system Qt for building Slicer):</p>
<pre><code> ./Slicer --launch /usr/bin/designer</code></pre>

---

## Post #3 by @cpinter (2020-09-18 16:14 UTC)

<p>Is this somewhere in the documentation? If not and you tell me where, I can add it.</p>
<p>Interestingly, on Ubuntu 18.04, the --designer switch works for me.</p>

---

## Post #4 by @lassoan (2020-09-18 16:23 UTC)

<p>Until the shortcut gets fixed, a note could be added to the Linux build instructions page on readthedocs.</p>
<p>Maybe the shortcut is only created if Slicer can find Qt designer, and that may depend on how and where Qt is installed.</p>

---

## Post #5 by @cpinter (2020-09-18 16:31 UTC)

<p>I see, thanks! Well if this is something that we intend to fix, then I guess this forum topic is just as good as an entry in the documentation. Thanks Andras!</p>

---

## Post #6 by @Fabiola (2020-09-18 17:28 UTC)

<p>Thank you Andras, Csaba for the prompt solution!</p>

---
