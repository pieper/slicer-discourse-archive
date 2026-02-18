# IOError: [Errno 13] Permission denied: 'Values.txt'

**Topic ID**: 1577
**Date**: 2017-12-02
**URL**: https://discourse.slicer.org/t/ioerror-errno-13-permission-denied-values-txt/1577

---

## Post #1 by @happyle (2017-12-02 17:54 UTC)

<p>Operating system:win 7<br>
Slicer version:3Dslicer 4.9.0-2017-11-01 r26541<br>
hello all</p>
<p>as seen in the screenshot,i was trying to save an array,then it came out an erro,but I can’t find out what I am doing wrong! the code was copied from here <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>Thanks in advance!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0897ba845e90311f09f0a23fef146a20502b268.jpeg" alt="bug" data-base62-sha1="pbIADd9rp6NacUYdigTDkyN0iQU" width="597" height="417"></p>

---

## Post #2 by @ihnorton (2017-12-02 18:38 UTC)

<p>You are probably trying to write in a read-only program directory. Try specifying an absolute path (<code>C:\path\to\somewhere\values.txt</code>) instead.</p>

---

## Post #3 by @happyle (2017-12-03 07:53 UTC)

<p>I think it’s still a little difficult for me to specify an absolute path:disappointed_relieved:<br>
how about print it out?how to do?<br>
seem not good enough:neutral_face:<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad604a128c9fe77f92321ea404bdfb3302f68e41.jpeg" alt="不过" data-base62-sha1="oJKTSP6oZ7O93EvxsE2FfTqt4NX" width="575" height="213"></p>

---

## Post #4 by @happyle (2017-12-03 08:49 UTC)

<p>GOD!I try it out   <img src="https://emoji.discourse-cdn.com/twitter/heart_eyes.png?v=12" title=":heart_eyes:" class="emoji" alt=":heart_eyes:" loading="lazy" width="20" height="20"> thank you!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc42a2f9d18c16f40d1aef84ec9f45d61961b3d9.jpeg" alt="bug2" data-base62-sha1="zZB5Dh5HqWtJit9KuKSMGbZnSEp" width="589" height="304"></p>

---

## Post #5 by @lassoan (2017-12-03 12:49 UTC)

<p>I would recommend you to complete Python and numpy tutorials, but to answer your question specifically, this should work:</p>
<pre><code>import numpy as np
values=np.array([1,2,3,7,4,3])
fullPath=slicer.app.defaultScenePath+"/values.txt"
np.savetxt(fullPath,values)
print(fullPath)
</code></pre>
<p>Of course, it is much more efficient to visualize 3D arrays as images (by slicing, volume rendering, segmenting, etc). If you hover over any position in the image, you can see the coordinate and grayscale value in the data probe widget in the bottom-left corner.</p>

---

## Post #6 by @happyle (2017-12-05 05:50 UTC)

<p>yes,you are right!that what thay say"书到用时方恨少" <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"></p>

---
