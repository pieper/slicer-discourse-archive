# Using external QML for Slicer custom application?

**Topic ID**: 5325
**Date**: 2019-01-10
**URL**: https://discourse.slicer.org/t/using-external-qml-for-slicer-custom-application/5325

---

## Post #1 by @jdx-john (2019-01-10 14:14 UTC)

<p>We’re redesigning the GUI on our Slicer custom application and some designers I spoke to have Qt experience and proposed to supply QML scripts. I am not a Qt dev so I’m unclear if this is compatible with the way we use Qt in Slicer, the versions used, etc - it sounds like it could save some boring coding if so.</p>
<p>Anyone know more or even done this themselves? I was also asked how Qt interacts with Python since some of the Qt tools emit C++ code too, but we do pretty much all development in Python.</p>

---

## Post #2 by @jcfr (2019-01-10 14:33 UTC)

<p>Based on our prior experience, if the whole application is written in QML, the challenge was the integration with VTK viewers (it is related to sharing of OpenGL context). Note that, this comment is based on experiments done a while back and it may be worth revisiting.</p>
<p>Now, if specific components are written in QML, this shouldn’t be an issue.</p>

---

## Post #3 by @lassoan (2019-01-10 18:21 UTC)

<p>You can also use Qt Designer - creating complex GUI widgets without coding. See discussion in this thread: <a href="https://discourse.slicer.org/t/workflow-that-brings-together-a-few-modules-as-tabs-in-a-unifying-parent-module/5314/15" class="inline-onebox">Workflow that brings together a few modules as tabs in a unifying parent module.</a></p>

---

## Post #4 by @jdx-john (2019-01-10 18:34 UTC)

<p>Thanks guys. <a class="mention" href="/u/lassoan">@lassoan</a> knows our project intimately but more generally, if someone did design and had QML scripts, how would we benefit from that in Python without having to write all the code - is that what Qt Designer does or are they separate ways to do something similar? I’ve not used either but both Qt-familiar designers I spoke to today were telling me how great QML is <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2019-01-10 19:41 UTC)

<p>Qt Quick Designer does the same thing as Qt Designer, but the first generates QML (web &amp; mobile app look&amp;feel by default) while the second generates UI files (traditional desktop look&amp;feel by default). Both designers allow specifying properties and making connections between GUI elements (in QML you can even use JavaScript), so some GUI behavior can be defined at that level - probably this is the reason why designers like them (especially QML, which feels very familiar for web designers). There is no difference in how much code you need to write to implement the application logic.</p>

---

## Post #6 by @jdx-john (2019-01-11 11:37 UTC)

<p>Is it pyqt used in Slicer?</p>

---

## Post #7 by @jamesobutler (2019-01-11 13:54 UTC)

<p>I believe it is actually PythonQt (<a href="http://pythonqt.sourceforge.net" rel="nofollow noopener">http://pythonqt.sourceforge.net</a>). It is similar to PyQt.</p>

---

## Post #8 by @lassoan (2019-01-11 14:53 UTC)

<p><a href="https://github.com/commontk/PythonQt" rel="nofollow noopener">PythonQt</a> and pyqt do the same thing (allow Qt to be used from Python), but in Slicer, we chose to use PythonQt, as it comes with a non-restrictive license that allows commercial use for free. Pyqt with non-restrictive license costs $550 per developer.</p>
<p>PythonQt has a number of advantages: it automatically generates code, so the library is much smaller and easier to maintain; applications are not implemented by extending Python but instead native applications embed Python (which allows much cleaner message processing and threading), etc. Unfortunately, its developers do not advertise this library at all, so it is not widely known.</p>

---

## Post #9 by @pieper (2019-01-11 16:27 UTC)

<p>In addition to wheat Andras says, I’ll just also mention that there is also PySide, which is like PyQt but without the restrictive licensing.  It did not exist at the time we decided on PythonQt.  Overall PythonQt has worked very well for us, but I also note that PySide is now <a href="https://doc.qt.io/qtforpython/index.html" rel="nofollow noopener">Qt for Python</a> and is an official part of the Qt ecosystem so we’ll keep an eye on that in case there’s a motivation to change in the future.</p>

---

## Post #10 by @lassoan (2019-01-11 16:49 UTC)

<p>It would be better to use mainstream libraries, but for me it looked like that similarly to PyQt, PySide takes over the application (Python is the executable) and does not allow an application to embed Python. With embedding Python, we have full control over message processing and threading in our application and Python remains an optional component.</p>
<p>It is hard to tell if it is worth giving up this full control. If current trends continue and Python becomes the standard computing environment for most researchers then we may give in: make Python a required dependency, switch to PySide, and convert all Slicer components to Python packages and build/distribute Slicer via anaconda.</p>

---

## Post #12 by @burnhamd (2019-08-15 17:35 UTC)

<p>Opening this back up.  I am interested in making a touch screen interface with 3D slicer.  The widgets are great for desktop with mouse, but leave something to be desired when it comes to touch screen interfaces.</p>
<p>I see that PythonQt supports QtQml and QtQuick submodules, but these do not seem to be included in Slicer.  Are there plans to add them, or has anyone done this already on another branch?</p>

---

## Post #13 by @lassoan (2019-08-15 18:15 UTC)

<p>We usually implement touch-friendly interfaces using classic widgets with appropriate style sheets.</p>
<p>It would be nice if you could try to build Slicer with Qml and Quick enabled in PythonQt and see how things work. If you find that it works very well then we can consider enabling them by default.</p>

---

## Post #14 by @burnhamd (2019-12-04 15:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I have tried building slicer with QtQuick turned on in pythonqt.  However, I am still not seeing any of the qml/qt quick objects in the python interpreter.</p>
<p>I turned them on by enabling  PYTHONQT_WRAP_QTALL through passing it into the suberbuild cmake generation.</p>
<p>I see in the cmake gui that it appears to be enabled after configuration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/419869f6492c7ffe30887dbc86d0e11d0a8da545.png" data-download-href="/uploads/short-url/9mhA0V2GaeyUThfO5HH2xyrkT9H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/419869f6492c7ffe30887dbc86d0e11d0a8da545.png" alt="image" data-base62-sha1="9mhA0V2GaeyUThfO5HH2xyrkT9H" width="690" height="376" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1067×582 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a better way to make sure it is actually being enabled and built with this option?</p>
<p>EDIT:<br>
Im pretty sure it isnt actually enabled correctly in the superbuild.  If I do an autocomplete for<br>
PythonQt.  I see Qt, QtCore, QtGUI, QtNetwork and QtUiTools</p>

---

## Post #15 by @lassoan (2019-12-04 16:00 UTC)

<p>PythonQt is now on GitHub: <a href="https://github.com/MeVisLab/pythonqt">https://github.com/MeVisLab/pythonqt</a>. I would recommend to post a question in their issue tracker about this.</p>

---

## Post #16 by @burnhamd (2020-01-02 15:48 UTC)

<p>Ok.  I got it to build with QML support, but unfortunately I am not able to get any QML to display.  I get a blank white box for everything that I try.  Will keep looking into it.</p>

---
