# Not locating a file - Called by an scripted module

**Topic ID**: 5070
**Date**: 2018-12-13
**URL**: https://discourse.slicer.org/t/not-locating-a-file-called-by-an-scripted-module/5070

---

## Post #1 by @jadam1995 (2018-12-13 17:12 UTC)

<p>Operating system: Windows (6.1.7601)<br>
Slicer version: 4.10.0<br>
Expected behavior: Load in python package to slicer, package is loaded, use package in scripted module to access and load an external audio data file.<br>
Actual behavior: Load in python package to slicer, package is loaded, script loaded module cannot locate external file.</p>
<p>Hello,</p>
<p>I am trying to implement a specific sound feedback in Slicer to play a specific audio file in response to an observed change in a node. I am attempting to use the python module <em>pydub</em>. I have imported this into slicer using the following:</p>
<p>import pip<br>
pip.main(‘install’, ‘pydub’)</p>
<p>The module is loaded into Slicer, but when I attempt to use this module to access an external .wav file</p>
<p>out_audio = AudioSegment.from_wav("/tmp/file.wav")</p>
<p>it fails to recognize the file (Windows Error 2, the file or directory does not exist. is this an issue with Slicer being able to open a file called by an external command? If anyone has an insight into why I may be getting this issue I would greatly appreciate your input.</p>

---

## Post #2 by @lassoan (2018-12-13 17:33 UTC)

<p>The <code>/tmp/file.wav</code> is not a full path on Windows. Verify the path and make sure to include drive name: <code>C:/tmp/file.wav</code>.</p>
<p>You can also replay sound using Qt or for more flexibility use a sound synthesizer (by using/customizing <a href="https://github.com/SlicerIGT/SlicerSoundControl" rel="nofollow noopener">SoundControl</a> extension).</p>

---

## Post #3 by @jadam1995 (2018-12-13 19:00 UTC)

<p>The  <code>/tmp/file.wav</code>  was a typo, I was using the path with the full drive name:<code>C:/tmp/file.wav</code>.</p>
<p>In regards to customizing the SoundControl extension, I had previously tried to work with this extension but was getting an error (<a href="https://discourse.slicer.org/t/breach-warning-open-sound-control-test-with-pure-data-errors/5045" class="inline-onebox">Breach warning, Open Sound Control, test with Pure Data errors</a>) which i belive is related to purr-data.</p>
<p>Also, the use of Qt in python would require some form of C++ wrapping would it not? I know that the PyQT provides binding for Qt but I am not sure if I would be able to use this within Slicer.</p>

---

## Post #4 by @lassoan (2018-12-13 21:40 UTC)

<p>All Qt classes (with a few exceptions) are Python-wrapped and heavily used in all scripted modules in Slicer.</p>

---

## Post #5 by @jamesobutler (2018-12-13 23:14 UTC)

<p>Yes, Qt already have python-wrapping in Slicer using PythonQt. You can see in the OpenSoundControl python module <a href="https://github.com/SlicerIGT/SlicerSoundControl/blob/master/OpenSoundControl/OpenSoundControl.py#L3" rel="nofollow noopener">here</a> where the python wrapped qt package is imported.</p>
<p>I would suggest to keep debugging that issue with the subprocess call within the OpenSoundControl extension code. I wouldn’t be surprised if the config file path is in an incorrect format. Maybe you have quotes around the path when there shouldn’t be? I haven’t tried anything myself, but giving you some ideas to try.</p>

---

## Post #6 by @jadam1995 (2018-12-14 19:45 UTC)

<p>Hi,</p>
<p>Thanks for the suggestions! I appreciate your support. The error I am getting is actually when I just use the built in Open Sound Control module under Modules&gt;IGT&gt;Open Sound Control. When i go under the PureData Server input section and add the PureData configuration for the OscSimpleTest and then it gives the error I discussed. I have tried several different iterations or ways of expressing the path for the OscSimpleTest.pd file and none seem to work I still get the same Error 87.</p>
<p>Additionally, I ran the OscSimpleTest just within Purr-Data, it is producing sound but outputting these errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7accc2ed7f72a784262a1d62a4eb23bb5e802b92.png" data-download-href="/uploads/short-url/hwkWWG7MxcjzQ7ALl5F793icnxo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7accc2ed7f72a784262a1d62a4eb23bb5e802b92_2_361x500.png" alt="image" data-base62-sha1="hwkWWG7MxcjzQ7ALl5F793icnxo" width="361" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7accc2ed7f72a784262a1d62a4eb23bb5e802b92_2_361x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7accc2ed7f72a784262a1d62a4eb23bb5e802b92.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7accc2ed7f72a784262a1d62a4eb23bb5e802b92.png 2x" data-dominant-color="F1EEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">508×703 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Not sure if this is contributing to the problem.</p>

---

## Post #7 by @lassoan (2018-12-16 02:02 UTC)

<aside class="quote no-group" data-username="jadam1995" data-post="6" data-topic="5070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f0a364/48.png" class="avatar"> jadam1995:</div>
<blockquote>
<p>Additionally, I ran the OscSimpleTest just within Purr-Data, it is producing sound but outputting these errors</p>
</blockquote>
</aside>
<p>I’ve just tried this and it works well. Make sure you download full pd version (including plugins) as described in instructions: <a href="https://github.com/SlicerIGT/SlicerSoundControl/blob/master/README.md" class="inline-onebox">SlicerSoundControl/README.md at master · SlicerIGT/SlicerSoundControl · GitHub</a></p>

---
