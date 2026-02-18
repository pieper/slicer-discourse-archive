# Ubuntu 18.04,Slicer 4.10.2, build error

**Topic ID**: 11888
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/ubuntu-18-04-slicer-4-10-2-build-error/11888

---

## Post #1 by @leemoncn (2020-06-06 04:27 UTC)

<p>On unbuntu 18.04, i build Slicer 4.10.2 from source code, it shows error:</p>
<p>‘/home/biso/Slicer-SuperBuild-Release/python-install/bin/PythonSlicer’ ‘setup.py’ ‘install’</p>
<p>error: Failed to obtain launcher executable name !</p>

---

## Post #2 by @jcfr (2020-06-06 04:55 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>For reference, the problem has been discussed in the this post <a href="https://discourse.slicer.org/t/error-failed-to-obtain-launcher-executable-name/10913" class="inline-onebox">error: Failed to obtain launcher executable name !</a></p>
<p>While the problem has been addressed in recent version of Slicer, a workaround is also discussed in <a href="https://github.com/Slicer/Slicer/issues/4787#issuecomment-606220350">https://github.com/Slicer/Slicer/issues/4787#issuecomment-606220350</a></p>
<p>Now, is there a specific reason you are trying to build version 4.10.2 from source ? If not, I suggest you build the latest version.</p>

---

## Post #3 by @leemoncn (2020-06-06 05:24 UTC)

<p>I have made a lot of change in 4.10.2. It’s  difficult to upgrade to a higher version.<br>
If I want to compile successfully Slicer 4.10.2, Which version is more recommended? Is Ubuntu16.04 can compile it?</p>

---

## Post #4 by @lassoan (2020-06-06 05:39 UTC)

<p>If you send a pull request with your changes to the Slicer-4.10 branch then we’ll check if we can port them for you to Slicer-4.11. In general, the best is to minimize Slicer core patches, but instead do all customizations using the CustomSlicer template and extensions. These Slicer core updates much easier. You can usually even keep your code compatible with both the stable and latest Slicer for a good while.</p>
<p>Slicer-4.11 (soon to be released as Slicer 5) is so much better than Slicer-4.10 that you really need to find a way to upgrade. If you run into any specific issues that the migration guide does not answer then let us know.</p>

---
