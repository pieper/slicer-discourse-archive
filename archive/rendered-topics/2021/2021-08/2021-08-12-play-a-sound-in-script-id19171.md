# Play a sound in script

**Topic ID**: 19171
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/play-a-sound-in-script/19171

---

## Post #1 by @atracsys-sbt (2021-08-12 15:45 UTC)

<p>Hi,<br>
From <a href="https://discourse.slicer.org/t/sound-feedback-navigation/690/2">this discussion</a>, I’ve gathered that it is possible to play a sound in Slicer, based on QSound. As I’m writing a scripted module, I would like to be able to play a beep in certain circumstances. However, I could not find the correct qt python command to do so.<br>
Thank you for any help,<br>
S.</p>

---

## Post #2 by @lassoan (2021-08-12 17:26 UTC)

<p>It seems that QSound is not wrapped by PythonQt, so you can either ask for it from PythonQt developers or add a small Qt or VTK class to your module (or some other existing module) that exposes methods that you need in Python.</p>
<p>What do you need the sound for?</p>
<p>Do you need sound feedback to indicate that an optically tracked tool gets out of view/gets in the view again? That is already implemented in Watchdog module in SlicerIGT extension. You can further enhance it, if it does not yet do things exactly the way you want. You could also add an API there to play in-view/out-of-view sound directly by a method call, instead of determining tool state by observing a transform node that is being updated by tracking data stream.</p>
<p>Do you need sound to convey more complex information, such as tracked tool distance, position, direction? That is implemented in <a href="https://github.com/SlicerIGT/SlicerSoundControl">SoundControl extension</a>.</p>

---

## Post #3 by @atracsys-sbt (2021-08-13 13:16 UTC)

<p>Thanks for your response Andras.<br>
While using an optically tracked pointer on a phantom with many divots, I would like to emit a short beep when a divot has been acquired for long enough.<br>
Since I don’t expect the PythonQt developers to place the QSound integration as an absolute priority, I will probably go the small qt class route first. Is there an example somewhere on how to perform such binding ?</p>

---

## Post #4 by @lassoan (2021-08-13 13:22 UTC)

<p>There is nothing special about this, you just create a class as usual and add methods that manipulate objects that are stored in the class. If you need a specific example, you can have a look at <code>qSlicerWebWidget</code>, which provides interface for the non-wrapped <code>QWebEngineView</code> class.</p>

---

## Post #5 by @atracsys-sbt (2021-08-16 13:19 UTC)

<p>After looking into the PythonQt source, it seems that QSound is in fact included in the wrapper. Is there a reason why it is not accessible in Slicer or am I mistaken ?</p>

---

## Post #6 by @lassoan (2021-08-16 14:30 UTC)

<p>Where did you find references to QSound?</p>

---

## Post #7 by @atracsys-sbt (2021-08-16 15:25 UTC)

<p>So I cloned PythonQt from their repo <a href="https://github.com/MeVisLab/pythonqt" rel="noopener nofollow ugc">here</a>, and looked for “QSound” in all files and found a lot of hits, notably:</p>
<pre><code class="lang-auto">Search "qsound" (695 hits in 25 files of 708 searched)
  D:\dev-ext\src\pythonqt\generated_cpp_50\com_trolltech_qt_gui\com_trolltech_qt_gui7.cpp (29 hits)
	Line 6517: PythonQtShell_QSound::~PythonQtShell_QSound() {
	Line 6517: PythonQtShell_QSound::~PythonQtShell_QSound() {
	Line 6521: void PythonQtShell_QSound::childEvent(QChildEvent*  arg__1)
	Line 6538:   QSound::childEvent(arg__1);
	Line 6540: void PythonQtShell_QSound::customEvent(QEvent*  arg__1)
	Line 6557:   QSound::customEvent(arg__1);
	Line 6559: bool  PythonQtShell_QSound::event(QEvent*  arg__1)
	Line 6587:   return QSound::event(arg__1);
	Line 6589: bool  PythonQtShell_QSound::eventFilter(QObject*  arg__1, QEvent*  arg__2)
	Line 6617:   return QSound::eventFilter(arg__1, arg__2);
	Line 6619: void PythonQtShell_QSound::timerEvent(QTimerEvent*  arg__1)
	Line 6636:   QSound::timerEvent(arg__1);
	Line 6638: QSound* PythonQtWrapper_QSound::new_QSound(const QString&amp;  filename, QObject*  parent)
	Line 6638: QSound* PythonQtWrapper_QSound::new_QSound(const QString&amp;  filename, QObject*  parent)
	Line 6638: QSound* PythonQtWrapper_QSound::new_QSound(const QString&amp;  filename, QObject*  parent)
	Line 6640: return new PythonQtShell_QSound(filename, parent); }
	Line 6642: QString  PythonQtWrapper_QSound::fileName(QSound* theWrappedObject) const
	Line 6642: QString  PythonQtWrapper_QSound::fileName(QSound* theWrappedObject) const
	Line 6647: bool  PythonQtWrapper_QSound::isFinished(QSound* theWrappedObject) const
	Line 6647: bool  PythonQtWrapper_QSound::isFinished(QSound* theWrappedObject) const
	Line 6652: int  PythonQtWrapper_QSound::loops(QSound* theWrappedObject) const
	Line 6652: int  PythonQtWrapper_QSound::loops(QSound* theWrappedObject) const
	Line 6657: int  PythonQtWrapper_QSound::loopsRemaining(QSound* theWrappedObject) const
	Line 6657: int  PythonQtWrapper_QSound::loopsRemaining(QSound* theWrappedObject) const
	Line 6662: void PythonQtWrapper_QSound::static_QSound_play(const QString&amp;  filename)
	Line 6662: void PythonQtWrapper_QSound::static_QSound_play(const QString&amp;  filename)
	Line 6664:   (QSound::play(filename));
	Line 6667: void PythonQtWrapper_QSound::setLoops(QSound* theWrappedObject, int  arg__1)
	Line 6667: void PythonQtWrapper_QSound::setLoops(QSound* theWrappedObject, int  arg__1)
  D:\dev-ext\src\pythonqt\generated_cpp_50\com_trolltech_qt_gui\com_trolltech_qt_gui7.h (18 hits)
	Line 55: #include &lt;qsound.h&gt;
	Line 869: class PythonQtShell_QSound : public QSound
	Line 869: class PythonQtShell_QSound : public QSound
	Line 872:     PythonQtShell_QSound(const QString&amp;  filename, QObject*  parent = 0):QSound(filename, parent),_wrapper(NULL) {};
	Line 872:     PythonQtShell_QSound(const QString&amp;  filename, QObject*  parent = 0):QSound(filename, parent),_wrapper(NULL) {};
	Line 874:    ~PythonQtShell_QSound();
	Line 885: class PythonQtWrapper_QSound : public QObject
	Line 890:   Infinite = QSound::Infinite};
	Line 892: QSound* new_QSound(const QString&amp;  filename, QObject*  parent = 0);
	Line 892: QSound* new_QSound(const QString&amp;  filename, QObject*  parent = 0);
	Line 893: void delete_QSound(QSound* obj) { delete obj; } 
	Line 893: void delete_QSound(QSound* obj) { delete obj; } 
	Line 894:    QString  fileName(QSound* theWrappedObject) const;
	Line 895:    bool  isFinished(QSound* theWrappedObject) const;
	Line 896:    int  loops(QSound* theWrappedObject) const;
	Line 897:    int  loopsRemaining(QSound* theWrappedObject) const;
	Line 898:    void static_QSound_play(const QString&amp;  filename);
	Line 899:    void setLoops(QSound* theWrappedObject, int  arg__1);
</code></pre>

---

## Post #8 by @lassoan (2021-08-16 20:04 UTC)

<p>OK, it seems that PythonQt indeed already supports the Multimedia component. Multimedia component is enabled at Slicer level, too. So, multimedia Qt component is most likely not Python-wrapped because of multimedia component configuration is missing at some places or wrapping is disabled (or not enabled by default) in CTK. You can search for names of other Qt components that are available in Python, such as <code>network</code> and <code>uitools</code> and make sure whenever they are mentioned, <code>multimedia</code> component is mentioned, too. Then redo a complete CTK build and hopefully it’ll all work. If it works well on your computer then send a pull request to commontk/CTK so that we can get your changes into official Slicer builds, too.</p>

---

## Post #9 by @atracsys-sbt (2021-08-17 15:19 UTC)

<p>So I tried to force the inclusion of QtMultimedia in PythonQt through CTK inside the Slicer build. After some tweaking, I successfully included it in the build, but I ended up with some errors of missing header files. These headers were part of QtMultimediaWidgets, another component, which I can’t successfully include like QtMultimedia.</p>
<p>Separately, I cloned CTK from its official repo (so completely separate from Slicer) and tried to build with QtMultimedia. Indeed it is not available in the cmake config, even with PythonQt enabled and despite having seemingly all the multimedia wrapper implemented (as shown in <a href="https://discourse.slicer.org/t/play-a-sound-in-script/19171/7">my previous post</a>). So I could try to tweak it similarly to what I did in Slicer’s CTK, but I’ll likely end up stuck with the same problem of missing headers.</p>
<p>In the end, I posted a <a href="https://github.com/commontk/CTK/issues/990" rel="noopener nofollow ugc">ticket</a> in the CTK github describing the issue, so I hope the devs will consider it.</p>

---

## Post #10 by @lassoan (2021-08-17 15:43 UTC)

<p>QtMultimedia and QtMultimediaWidgets are two distinct Qt modules, but PythonQt may bundle the two so that if you enable multimedia wrapping then it wraps both QtMultimedia and QtMultimediaWidgets. THe build errors maybe due to QtMultimediaWidgets Qt module not installed when you have installed Qt.</p>

---

## Post #11 by @lassoan (2021-08-18 01:21 UTC)

<aside class="quote no-group" data-username="atracsys-sbt" data-post="9" data-topic="19171">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atracsys-sbt/48/11434_2.png" class="avatar"> atracsys-sbt:</div>
<blockquote>
<p>posted a <a href="https://github.com/commontk/CTK/issues/990">ticket </a> in the CTK github describing the issue, so I hope the devs will consider it.</p>
</blockquote>
</aside>
<p>CTK development is driven mainly by needs of 3D Slicer and MITK, by the developers of these groups. So, it is unlikely that such a specific need will pull in anybody else.</p>
<p>Please test if adding the multimedia widget Qt module solves the build issue, because we cannot start the review/integration process until a working solution is found (we will not have time in the near future to work on a solution ourselves because there are much higher priority tasks and there are alternative solutions for this issue).</p>

---

## Post #12 by @atracsys-sbt (2021-08-18 07:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="19171">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>THe build errors maybe due to QtMultimediaWidgets Qt module not installed when you have installed Qt.</p>
</blockquote>
</aside>
<p>I checked inside my Qt folder and it seems QtMultimediaWidgets is installed, all the missing headers are there.<br>
Also, I had already tried to include the multimedia widgets component to the build as I did for the multimedia component but that didn’t work. I will try again though, maybe I missed something.</p>

---

## Post #13 by @atracsys-sbt (2021-08-18 07:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="19171">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please test if adding the multimedia widget Qt module solves the build issue, because we cannot start the review/integration process until a working solution is found (we will not have time in the near future to work on a solution ourselves because there are much higher priority tasks and there are alternative solutions for this issue).</p>
</blockquote>
</aside>
<p>I understand. I will try to get it working so more.</p>

---

## Post #14 by @atracsys-sbt (2021-08-18 12:37 UTC)

<p>So, I’ve finally been able to successfully build CTK with the right components. Porting these modifications to the CTK included in Slicer, I was able to play sound !<br>
Now, I need to find out how to make these changes from the config files of CTK and I’ll do a pull request.</p>

---

## Post #15 by @atracsys-sbt (2021-08-18 16:29 UTC)

<p>So I have figured out the modifications necessary. I already created a pull request for the fix for PythonQt and will do the one for CTK tomorrow.</p>

---
