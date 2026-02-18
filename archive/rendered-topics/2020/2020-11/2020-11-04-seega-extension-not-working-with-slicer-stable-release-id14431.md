# SEEGA extension not working with Slicer stable release

**Topic ID**: 14431
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/seega-extension-not-working-with-slicer-stable-release/14431

---

## Post #1 by @BushraR (2020-11-04 14:17 UTC)

<p>Hello,<br>
I am new to this community. I am using SEEGA extension with the slicer stable release 4.11. It seems that author of that extension doesn’t read this forum and I have already seen someone else reporting the error that SEEGA extension is giving errors with stable release on extension’s github repository. I am using stable release to avail Freesurfer slicer extension capabilities ( and it is not available for previous versions).<br>
Now the error I am getting with SEEGA extension (shown below) is what I have seen being reported before as well.<br>
Is there any quick fix for SEEG extension that I can do myself to be able to use it for latest slicer release. Thank you<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/Users/busria/Downloads/SEEGA-master/BrainZoneDetector/BrainZoneDetector.py”, line 52<br>
print self.lutPath</p>

---

## Post #2 by @lassoan (2020-11-04 14:35 UTC)

<p>Slicer-4.11 uses Python3, while the previous version used Python2. There are a few trivial syntax differences, which you should be able fix on your own.</p>
<p>For example, the first error that you see here is that <code>print self.lutPath</code> is not valid syntax in Python3 and you need to change it to <code>print(self.lutPath)</code> (in line 52 of “/Users/busria/Downloads/SEEGA-master/BrainZoneDetector/BrainZoneDetector.py”). If you fix this an error and restart Slicer then you’ll see the next error. If you have trouble with any specific error then let us know.</p>
<p>Once you are done, you can submit the fixes as a “pull request” to the original repository.</p>

---

## Post #3 by @BushraR (2020-11-04 14:41 UTC)

<p>Thank you so much<br>
I have fixed all the errors, teh only one I am bit confuse is this line<br>
self.electrodeList = sorted(self.electrodeList,key=lambda (x): x.name.text)<br>
I only changed it to this to make it work<br>
self.electrodeList = sorted(self.electrodeList,key=lambda x: x.name.text)</p>
<p>Is this correct?<br>
Thank you so much for the help</p>

---

## Post #4 by @lassoan (2020-11-04 18:37 UTC)

<aside class="quote no-group" data-username="BushraR" data-post="3" data-topic="14431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bushrar/48/10743_2.png" class="avatar"> BushraR:</div>
<blockquote>
<p>I only changed it to this to make it work<br>
self.electrodeList = sorted(self.electrodeList,key=lambda x: x.name.text)</p>
<p>Is this correct?</p>
</blockquote>
</aside>
<p>Yes, it is correct.<br>
.</p>

---
