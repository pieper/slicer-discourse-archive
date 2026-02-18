# How to call twoprojectionregistration module in slicer?

**Topic ID**: 9434
**Date**: 2019-12-08
**URL**: https://discourse.slicer.org/t/how-to-call-twoprojectionregistration-module-in-slicer/9434

---

## Post #1 by @James753 (2019-12-08 17:23 UTC)

<p>Hi,</p>
<p>I am developing a registration extension recently.<br>
And I am going to use a remote-module in itk which is twoprojectionregistration module.<br>
And I can not find this module in slicer library.<br>
I was wondering if there is a way to call this module from itk which I built already outside slicer.<br>
Or I need to develop a new module with twoprojectionregistration module in c++, and calling from python script in slicer.<br>
Please give me some hint or suggestion.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2019-12-09 05:20 UTC)

<p>One option is to build Slicer on your computer and one it’s done, configure ITK with Module_TwoProjectionRegistration:BOOL=ON and start the build again.</p>
<p>If you are not comfortable with C++ then you can install twoprojectionregistration as a python package (<code>pip_install('itk-twoprojectionregistration')</code>) - this requires recent Slicer Preview Release.</p>
<p>Once you confirmed that twoprojectionregistration works well then let us know and we’ll find a good way of making it available for your extension (build the ITK external module in your extension, or add this external module to Slicer core, etc.).</p>

---

## Post #3 by @James753 (2019-12-09 05:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>One option is to build Slicer on your computer and one it’s done, configure ITK with Module_TwoProjectionRegistration:BOOL=ON and start the build again.</p>
</blockquote>
</aside>
<p>Thank you for your reply.<br>
I will try it, and let you know the result.</p>

---
