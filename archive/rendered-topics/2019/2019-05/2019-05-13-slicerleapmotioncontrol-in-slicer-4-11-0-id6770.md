---
topic_id: 6770
title: "Slicerleapmotioncontrol In Slicer 4 11 0"
date: 2019-05-13
url: https://discourse.slicer.org/t/6770
---

# SlicerLeapMotionControl in Slicer 4.11.0

**Topic ID**: 6770
**Date**: 2019-05-13
**URL**: https://discourse.slicer.org/t/slicerleapmotioncontrol-in-slicer-4-11-0/6770

---

## Post #1 by @JaceYang (2019-05-13 05:51 UTC)

<p>Operating system:windows10<br>
Slicer version:4.11.0<br>
Expected behavior: **<a href="https://github.com/lassoan/SlicerLeapMotionControl" rel="noopener nofollow ugc">SlicerLeapMotionControl</a>**can work<br>
Actual behavior:SlicerLeapMotionControl cannot work</p>
<p>I add the src directory to the additional module paths,but there are some errors in python.<br>
What can I do to make the SlicerLeapMotionControl work in Slicer4.11? It can work in Slicer4.8.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4253973738222606c18da7640cfa7a9935f5e0.png" data-download-href="/uploads/short-url/fSf6ouJXH8Zf3BaDFI5xJYmB1L2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4253973738222606c18da7640cfa7a9935f5e0_2_690x448.png" alt="image" data-base62-sha1="fSf6ouJXH8Zf3BaDFI5xJYmB1L2" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4253973738222606c18da7640cfa7a9935f5e0_2_690x448.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4253973738222606c18da7640cfa7a9935f5e0_2_1035x672.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4253973738222606c18da7640cfa7a9935f5e0_2_1380x896.png 2x" data-dominant-color="999898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1675×1088 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2019-05-13 06:06 UTC)

<p>Thanks for reporting the problem.</p>
<p>Since Slicer was recently updated to use with Python 3 (see [1] for more details), extensions and more general any example of code also need to be updated to support python 3 and it seems the <code>SlicerLeapMotionControl</code> scripts still need to be updated to support it.</p>
<p>[1] <a href="https://discourse.slicer.org/t/updating-slicer-to-work-with-python-3/4662" class="inline-onebox">Updating slicer to work with python 3</a></p>

---

## Post #3 by @jcfr (2019-05-13 06:09 UTC)

<p>For reference, migration guide explaining how to update code to work with Python 3 is available at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Slicer_5.0:_Python2_to_Python3" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Slicer_5.0:_Python2_to_Python3</a></p>
<p>I will update the code following the migration guide, it would be great if you could test the changes once this is done.</p>

---

## Post #4 by @jcfr (2019-05-13 06:19 UTC)

<p>Here  is a PR that should fix the issue reported in your initial screenshot: <a href="https://github.com/lassoan/SlicerLeapMotionControl/pull/1" rel="nofollow noopener">https://github.com/lassoan/SlicerLeapMotionControl/pull/1</a></p>
<p>That said, there are most likely other problem to address. Could you try the updated code available in the Pull request linked above and report the other errors ?</p>

---

## Post #5 by @JaceYang (2019-05-13 06:23 UTC)

<p>Wow,it’s a pleasure to do the test work.<img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"><br>
Is it after midnight in America or Canada? <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20"> You replied so soon at this time.<br>
I will try your suggestions in the future hours.</p>

---

## Post #6 by @JaceYang (2019-05-13 06:54 UTC)

<p>Em,I switch to the code you just push but there are still errors.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0569c5c63c1785b221f5d604e5dc73e2992e0cf9.png" data-download-href="/uploads/short-url/LT0fpkIrirRRrqxPZEgqOMG1ND.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0569c5c63c1785b221f5d604e5dc73e2992e0cf9_2_690x345.png" alt="image" data-base62-sha1="LT0fpkIrirRRrqxPZEgqOMG1ND" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0569c5c63c1785b221f5d604e5dc73e2992e0cf9_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0569c5c63c1785b221f5d604e5dc73e2992e0cf9_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0569c5c63c1785b221f5d604e5dc73e2992e0cf9_2_1380x690.png 2x" data-dominant-color="1A1A1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1837×920 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2019-05-13 11:46 UTC)

<p>Probably you need to download the LeapMotion Python SDK, and replace SDK files in the extension’s folder with their Python3 version.</p>

---

## Post #8 by @jcfr (2019-05-13 13:00 UTC)

<aside class="quote no-group" data-username="JaceYang" data-post="6" data-topic="6770">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>I switch to the code you just push but there are still errors.</p>
</blockquote>
</aside>
<p>It also looks like you are still using the old version of the file. Line  is expected to be different.<br>
See <a href="https://github.com/lassoan/SlicerLeapMotionControl/pull/1/commits/8034a17836ee23c42e867e576a3d3d5e42c97436" class="inline-onebox">Add python3 support by jcfr · Pull Request #1 · lassoan/SlicerLeapMotionControl · GitHub</a></p>

---

## Post #9 by @JaceYang (2019-05-14 01:38 UTC)

<p>I modify the SlicerLeapModule.py according to your code.It now has different errors.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4357d43609992af31b533590e24f3bade091b552.png" data-download-href="/uploads/short-url/9BKa7fyY5V6uyQJRBwxW6yiSGwW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4357d43609992af31b533590e24f3bade091b552_2_690x213.png" alt="image" data-base62-sha1="9BKa7fyY5V6uyQJRBwxW6yiSGwW" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4357d43609992af31b533590e24f3bade091b552_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4357d43609992af31b533590e24f3bade091b552_2_1035x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4357d43609992af31b533590e24f3bade091b552_2_1380x426.png 2x" data-dominant-color="8E8E8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2465×762 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jcfr (2019-05-14 04:29 UTC)

<p>The next step would be to obtain the leap motion  SDK for python 3.x.</p>
<p>Reading  <a href="https://developer.leapmotion.com/releases">https://developer.leapmotion.com/releases</a>, it seems they have been removed from the latest SDK (Leap Motion Orion 4.0.0):</p>
<blockquote>
<p>Removed Leap.dll, all associated language bindings (LeapPython, LeapJava, Objective-C) and samples Leap Motion Orion 4.0.0</p>
</blockquote>
<p>Now, reading the “Setting up a project” section found in the v3.2 of the documentation, we can find information about the python bindings:</p>
<ul>
<li><a href="https://developer-archive.leapmotion.com/documentation/python/index.html">https://developer-archive.leapmotion.com/documentation/python/index.html</a></li>
<li><a href="https://developer-archive.leapmotion.com/documentation/python/devguide/Project_Setup.html">https://developer-archive.leapmotion.com/documentation/python/devguide/Project_Setup.html</a></li>
</ul>
<blockquote>
<p>The LeapPython library included in the Leap Motion SDK supports only Python 2.7. However, the SDK also includes the SWIG interface file used to generate the LeapPython source code, so advanced users can generate and compile their own version of LeapPython. For instructions, refer to <a href="https://support.leapmotion.com/entries/39433657-Generating-a-Python-3-3-0-Wrapper-with-SWIG-2-0-9">Generating a Python 3.3.0 Wrapper with SWIG 2.0.9</a> in our support knowledge base.</p>
</blockquote>
<p>If you download the v3.2 of the SDK and try to follow instruction from  <a href="https://support.leapmotion.com/hc/en-us/articles/223784048">https://support.leapmotion.com/hc/en-us/articles/223784048</a> , you should be able to address the remaining issues.</p>
<p>Also look like there are readily available code to make the python 3 binding for linux … see <a href="https://github.com/BlackLight/leap-sdk-python3" class="inline-onebox">GitHub - BlackLight/leap-sdk-python3: Leap Motion SDK - Python 3 module builder</a> but i couldn’t find a similar project.</p>
<p>Note that it may exist, i just didn’t spend too much time searching …</p>

---

## Post #11 by @JaceYang (2019-05-15 05:49 UTC)

<p>I compile and generate LeapPython.dll(x86) file successfully by following this<br>
<a href="https://support.leapmotion.com/hc/en-us/articles/223784048" class="onebox" target="_blank" rel="noopener nofollow ugc">https://support.leapmotion.com/hc/en-us/articles/223784048</a><br>
But there are still errors.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94ddb28c6ea17172fe2357f4a3a96f9e0958778c.png" data-download-href="/uploads/short-url/leVEjuWoyi6qgqd8EBckM34Wcu8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94ddb28c6ea17172fe2357f4a3a96f9e0958778c.png" alt="image" data-base62-sha1="leVEjuWoyi6qgqd8EBckM34Wcu8" width="690" height="365" data-dominant-color="1C1C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1667×884 47.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And when I build LeapPython.dll(x64) with Leap.lib(x64),link error occur.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/532c02fe4c03533fdb67a7a67c26a63d54167e80.png" data-download-href="/uploads/short-url/bRLVkplW1Vw2oDcqZEDygPGldrG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/532c02fe4c03533fdb67a7a67c26a63d54167e80_2_542x500.png" alt="image" data-base62-sha1="bRLVkplW1Vw2oDcqZEDygPGldrG" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/532c02fe4c03533fdb67a7a67c26a63d54167e80_2_542x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/532c02fe4c03533fdb67a7a67c26a63d54167e80_2_813x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/532c02fe4c03533fdb67a7a67c26a63d54167e80_2_1084x1000.png 2x" data-dominant-color="E5E6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1346×1241 55.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2019-05-15 12:19 UTC)

<p>You can probably fix the link errors by using the 64-bit LeapMotion library files.</p>

---

## Post #13 by @mikecsu (2019-05-16 05:58 UTC)

<p>Hi ,<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> i did the same thing that <a class="mention" href="/u/jaceyang">@JaceYang</a> did , i build LeapPython.dll with Leap.lib(x64),   it can  successfully generate LeapPython.dll, so i change it to leapPython.pyd and put it into the demo1 folder to replace the old one,and then add it to 3D Slicer, but those errors have not changed comparing to the unmodified source code( original source code) and they are the same errors that Jace Yang has got.</p>

---

## Post #14 by @mikecsu (2019-05-27 08:30 UTC)

<p>Hi,everyone <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a>@JaceYang. I recently found that there is no way for me to develop a leap motion python Module on slicer 4.11.0(python 3.6.7) with leap motion V3.2(only support Python2.7).  I tried <strong>Generating a Python 3.3.0 Wrapper with SWIG 2.0.9,</strong> but errors remains. and then i try to Generating a Python 3.6.7 Wrapper with SWIG 2.0.9, it failed at the beginning to produce a LeapPython.dll. So i would like to know if you guys can give me some advice？  If there is no solution for this issue, i may change to develop a c++ module. Thanks in advance.</p>

---

## Post #15 by @timeanddoctor (2020-01-31 11:06 UTC)

<p>Hi, Mikecsu, Did you deal with this problem now? I donnot know can I perform the leap motion in the last version slicer now?</p>

---

## Post #16 by @timeanddoctor (2020-01-31 13:04 UTC)

<pre><code>Traceback (most recent call last):
  File "C:/slicerpy/leapmotion/SlicerLeapModule.py", line 20, in __init__
    logic = SlicerLeapModuleLogic()
  File "C:/slicerpy/leapmotion/SlicerLeapModule.py", line 164, in __init__
    self.LeapController = Leap.Controller()
AttributeError: module 'Leap' has no attribute 'Controller'
</code></pre>
<p>I don’t think there is a mistake:<br>
`class SlicerLeapModuleLogic(object):</p>
<pre><code>      def __init__(self):
        import Leap
        self.LeapController = Leap.Controller()
        self.enableAutoCreateTransforms = False    
        self.onFrame()'
  `
</code></pre>
<p>the ‘Leap.py’ file contain the class:Controller() , but the slicer(4.11) cannot import it, any problem?</p>

---

## Post #17 by @Eserval (2022-08-15 16:22 UTC)

<p>Hello everyone,</p>
<p>Do we actually have a functionality of leap motion on slicer?</p>
<p>Best</p>

---
