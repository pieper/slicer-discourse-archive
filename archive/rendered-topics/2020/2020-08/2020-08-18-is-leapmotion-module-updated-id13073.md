---
topic_id: 13073
title: "Is Leapmotion Module Updated"
date: 2020-08-18
url: https://discourse.slicer.org/t/13073
---

# Is LeapMotion Module updated?

**Topic ID**: 13073
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/is-leapmotion-module-updated/13073

---

## Post #1 by @apparrilla (2020-08-18 13:57 UTC)

<p>Hi people,</p>
<p>Slicer version: Slicer 4.11.0-2020-07-04 Win</p>
<p>I´m trying to control scene view with LeapMotion device and I have some trouble.<br>
I follow installation steps from GitHub proyect (download drivers and put them inside module folder)</p>
<p>Slicer don´t show me “Gesture control / LeapMotion control module” and Python interactor send this error message:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\Users\appar\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-04\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "E:/Dicom Files 2/SlicerLeapMotionControl-master/Demo1/Leap.py", line 28, in &lt;module&gt;
    LeapPython = swig_import_helper()
  File "E:/Dicom Files 2/SlicerLeapMotionControl-master/Demo1/Leap.py", line 24, in swig_import_helper
    _mod = imp.load_module('LeapPython', fp, pathname, description)
  File "C:\Users\appar\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-04\lib\Python\Lib\imp.py", line 243, in load_module
    return load_dynamic(name, filename, file)
  File "C:\Users\appar\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-04\lib\Python\Lib\imp.py", line 343, in load_dynamic
    return _load(spec)
  File "&lt;frozen importlib._bootstrap&gt;", line 684, in _load
  File "&lt;frozen importlib._bootstrap&gt;", line 658, in _load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 571, in module_from_spec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 922, in create_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
ImportError: DLL load failed: No se puede encontrar el módulo especificado.
Traceback (most recent call last):
  File "E:/Dicom Files 2/SlicerLeapMotionControl-master/Demo1/SlicerLeapModule.py", line 20, in __init__
    logic = SlicerLeapModuleLogic()
  File "E:/Dicom Files 2/SlicerLeapMotionControl-master/Demo1/SlicerLeapModule.py", line 164, in __init__
    self.LeapController = Leap.Controller()
AttributeError: module 'Leap' has no attribute 'Controller'
</code></pre>
<p>Thanks on advance.</p>

---

## Post #2 by @lassoan (2020-08-19 05:20 UTC)

<p>Unfortunately, Leap has official Python API only for Python2 (this is what is bundled with SlicerLeapMotion extension).</p>
<p>Slicer-4.11 uses Python3, so you need to build build and wrap the LeapMotion API yourself. It is not very simple (see some attempts described <a href="https://discourse.slicer.org/t/slicerleapmotioncontrol-in-slicer-4-11-0/6770/15">here</a>), but should be possible, since Slicer uses standard Python 3.6.7, so if you can make or find anything that works with this Python version then it will work in Slicer, too.</p>

---

## Post #3 by @apparrilla (2021-01-11 09:29 UTC)

<p>Hi again <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
Searching for a way to manage Slicer scene with LeapMotion, I´ve found a Plus Toolkit config file example. It doesn´t recognice Leap controler but should be easier to fix than python wrapper for Slicer LeapMotion Module. Do you think about this way?</p>

---

## Post #4 by @lassoan (2021-01-11 19:34 UTC)

<p>I agree that using Plus to connect to LeapMotion should be a good approach, especially if you already use Plus to connect to other imaging or tracking devices. Probably all you need to do is to build Plus with LeapMotion enabled.</p>

---

## Post #5 by @apparrilla (2021-01-11 20:59 UTC)

<p>How to enable it?<br>
PLUS_USE_LEAPMOTION  in Cmake config?.. Maybe</p>

---

## Post #6 by @lassoan (2021-01-11 21:10 UTC)

<p>Exactly. Follow the build instructions here: <a href="https://github.com/PlusToolkit/PlusBuild" class="inline-onebox">GitHub - PlusToolkit/PlusBuild: CMake scripts for building Plus library, applications, and all required dependencies</a></p>

---

## Post #7 by @apparrilla (2021-01-14 22:24 UTC)

<p>I´ve some trouble building Plus with LeapMotion. Stable 2.8 branch doesn´t have Leap option so I´ve been trying with master branch:<br>
Config:<br>
VS 2017 Comm<br>
Qt 5.7<br>
Leap SDK</p>
<p>Both x86 / x64 version throw me compiling errors in VS related with x64 o Win32 issues.</p>
<p>Is there any item combination that should work? Do I need PLUSBUILD_INSTALL_ITK option? Any other option is not compatible with x64? What EXTERNAL_VTK_VERSION is the right one?</p>
<p>Thanks!</p>

---

## Post #8 by @lassoan (2021-01-15 00:10 UTC)

<p><a class="mention" href="/u/adamrankin">@adamrankin</a> Is the latest Plus supposed to support LeapMotion?</p>

---

## Post #9 by @timeanddoctor (2021-01-15 01:41 UTC)

<p>why not use a python 2.7  to broadcast the leapmotion data into slicer? And if you just went have a communicate during surgery you can use the old stable slicer to browse the DICOM$volume Renderiing.</p>

---

## Post #10 by @lassoan (2021-01-15 01:58 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="9" data-topic="13073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>why not use a python 2.7 to broadcast the leapmotion data into slicer?</p>
</blockquote>
</aside>
<p>I guess the issue with Slicer-4.10, Python2, and LeapMotion’s Python interface is that they all 3 are obsolete and unsupported. Any time you spend with them is wasted effort because even if you manage to make something work, it is very likely that you will need to abandon what you implemented and switch to current software/API versions sooner than later.</p>

---

## Post #11 by @adamrankin (2021-01-15 02:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, the leap is supported by Plus. Our students were using it last fall.</p>

---

## Post #12 by @apparrilla (2021-01-15 14:41 UTC)

<p>Ok. It´s working.<br>
Config:<br>
Win10<br>
VS 2017 Comm<br>
LeapMotion SDK  (LeapDeveloperKit_4.1.0+52211_win)<br>
QT 5.7 (qt-opensource-windows-x86-msvc2015_64-5.7.0)</p>
<p>I´ve all finger transform working. I´ll send you a video these next days.</p>

---

## Post #13 by @apparrilla (2021-01-16 03:39 UTC)

<p>Link to the video:</p><div class="youtube-onebox lazy-video-container" data-video-id="OXN7-yPlEHM" data-video-title="LeapMotion OpenIGTLinkIF" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=OXN7-yPlEHM" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/OXN7-yPlEHM/hqdefault.jpg" title="LeapMotion OpenIGTLinkIF" width="" height="">
  </a>
</div>

<p>About gesture… These upgrade should be implemented in Plus device code or throw a manage module of transforms?</p>
<p>Thanks…</p>

---

## Post #14 by @lassoan (2021-01-16 05:15 UTC)

<p>This looks great! To send gestures, you need to update the LeapMotion class in Plus toolkit. For example, you could add gesture information in custom fields (contents of custom fields appear as MRML node attributes in Slicer).</p>

---

## Post #15 by @apparrilla (2021-01-16 10:30 UTC)

<p>Does any other PlusLib Device that work in this way as example for this task? Or any documentation to follow?</p>

---

## Post #16 by @lassoan (2021-01-16 14:38 UTC)

<p>SonixVideo device adds custom fields. There should be a few more, you can search for customfield in the source code for more examples.</p>

---

## Post #17 by @apparrilla (2021-01-23 08:42 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="11" data-topic="13073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>es, the leap is supported by Plus. Our students were using it last fall.</p>
</blockquote>
</aside>
<p>Although the scene works correctly, models movement has significant delay with hands movement. Is there any parameter in Plus config file I can change to fix it?</p>
<p>Thanks!</p>

---

## Post #18 by @adamrankin (2021-01-23 13:12 UTC)

<p>Sadly the performance slow down happens in Slicer and is unavoidable without programming changes.</p>
<p>One workaround you can try is to send less transforms from Plus. Can you get away with just one fingers’ joints? Can you limit it to one hand? Maybe just the finger tip joints?</p>
<p>The slowdown comes from the quantity of transmitted joints.</p>

---

## Post #19 by @lassoan (2021-01-23 15:10 UTC)

<p>We will do some performance optimization after Slicer’s switch to VTK9 is completed (see <a href="https://github.com/Slicer/Slicer/issues/5398" class="inline-onebox">Rendering performance needs improvement · Issue #5398 · Slicer/Slicer · GitHub</a>).</p>

---
