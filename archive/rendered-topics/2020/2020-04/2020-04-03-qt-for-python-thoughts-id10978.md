# Qt for Python - Thoughts?

**Topic ID**: 10978
**Date**: 2020-04-03
**URL**: https://discourse.slicer.org/t/qt-for-python-thoughts/10978

---

## Post #1 by @jamesobutler (2020-04-03 14:57 UTC)

<p>Does anyone have opinions about <a href="https://www.qt.io/qt-for-python" rel="nofollow noopener">Qt for Python</a> for the Qt python bindings?  I received a promotional email about it recently and briefly looked into it. It would I guess replace <a href="https://github.com/MeVisLab/pythonqt" rel="nofollow noopener">PythonQt</a>.</p>
<p>Some background is available at <a href="https://wiki.qt.io/Qt_for_Python:" rel="nofollow noopener">https://wiki.qt.io/Qt_for_Python:</a></p>
<ul>
<li>Properly supported by the Qt Company</li>
<li>The name of the project is  <strong>Qt for Python</strong>  and the name of the module is  <strong>PySide2</strong> .</li>
<li>The module was released mid June 2018 as a Technical Preview (supporting Qt 5.11), and it was officially released without the Technical Preview tag, in December 2018 for Qt 5.12.</li>
</ul>
<p>Licensing: <strong>Qt for Python</strong>  is available under LGPLv3 <a href="https://doc.qt.io/qtforpython/licenses.html" rel="nofollow noopener">https://doc.qt.io/qtforpython/licenses.html</a></p>
<p><a href="https://doc.qt.io/qtforpython/gettingstarted.html" rel="nofollow noopener">Qt for Python Getting Started</a> with platform specific details and about building from source if not wanting to use Pyside 2 wheels from pypi (<a href="https://pypi.org/project/PySide2/#history" rel="nofollow noopener">https://pypi.org/project/PySide2/#history</a>).</p>

---

## Post #2 by @lassoan (2020-04-03 15:50 UTC)

<p>It is always better to use mainstream libraries (people are more familiar with it, easier to find help, less likely to die off, etc.) and “Qt for Python” is a clear winner. In the long term we would like to be able to distribute Slicer components as individually loadable Python packages (starting with vtkAddon, MRML, etc.) and using “Qt for Python” for GUI would be aligned with this goal.</p>
<p>My concerns are the followings:</p>
<ol>
<li>In “Qt for Python” examples the application is always Python.exe, and the QApplication object is always created in Python and executed in Python:</li>
</ol>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/tonytony2020/Qt-Python-Binding-Examples/blob/485150bfaf732c883833377750c2d3752be00f6b/markup/markdown_editor.py#L78-L82" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/tonytony2020/Qt-Python-Binding-Examples/blob/485150bfaf732c883833377750c2d3752be00f6b/markup/markdown_editor.py#L78-L82" target="_blank">tonytony2020/Qt-Python-Binding-Examples/blob/485150bfaf732c883833377750c2d3752be00f6b/markup/markdown_editor.py#L78-L82</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="78" style="counter-reset: li-counter 77 ;">
<li>if __name__ == "__main__":</li>
<li>    app = QtGui.QApplication(sys.argv)</li>
<li>    foo = Foo()</li>
<li>    foo.show()</li>
<li>    sys.exit(app.exec_())</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It would be great if somebody could try if Qt for Python can be used in an application that embeds Python (not in Python.exe), so that we can keep complete ownership of how the application is created/destroyed, how threads and message queue is handled, etc.</p>
<ol start="2">
<li>
<p>Qt version. We would lose control of what Qt version is used and how Qt is built.</p>
</li>
<li>
<p>Porting the Python/Qt infrastructure and all Python scripts to “Qt for Python” would be a very significant effort.</p>
</li>
</ol>

---

## Post #3 by @jcfr (2020-04-03 16:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10978">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In the long term we would like to be able to distribute Slicer components as individually loadable Python packages (starting with vtkAddon, MRML, etc.) and using “Qt for Python” for GUI would be aligned with this goal.</p>
</blockquote>
</aside>
<p>Step by step we will get there. This will also streamline continuous integration.</p>

---

## Post #4 by @pieper (2020-04-03 16:09 UTC)

<p>Yes, I’ve been keeping an eye on this too, and certainly there are a lot of advantages in using the mainstream libraries.  There are good reasons why we have the current system, but they are always worth revisiting if/when circumstances evolve.</p>
<p>To Andras’s points:</p>
<ol>
<li>
<p>There’s no reason we couldn’t create a QSlicerApplication from python.</p>
</li>
<li>
<p>We could still choose to build and distribute any specific versions we wanted, but aiming for compatibility with the standard installations would have a lot of benefit.</p>
</li>
<li>
<p>Yes, lots of work!  But most would be pretty routine and would result in a cleaner and more maintainable system.</p>
</li>
</ol>

---

## Post #5 by @jcfr (2020-04-03 16:24 UTC)

<p>It may also be worth investigating:</p>
<ul>
<li>support for wrapping your own classes</li>
<li>integration with VTK objects (e.g slot or wrapped function accepting vtk objects)</li>
</ul>

---
