# Add Drag and drop import to slicelet?

**Topic ID**: 9382
**Date**: 2019-12-04
**URL**: https://discourse.slicer.org/t/add-drag-and-drop-import-to-slicelet/9382

---

## Post #1 by @Amine (2019-12-04 12:40 UTC)

<p>Hi, is there any way to implement the drag and drop function to a slicelet (qt widget without the main window) as it is with the the main window (hopefully other than rewriting it from scratch ) thanks</p>

---

## Post #2 by @pieper (2019-12-04 14:43 UTC)

<p>Last time I checked you could only implement the drop behavior in C++ by overriding the <code>dropEvent</code> method, but maybe somebody can find a way to do it in Python.</p>
<p><a href="https://doc.qt.io/qt-5/dnd.html" class="onebox" target="_blank">https://doc.qt.io/qt-5/dnd.html</a></p>

---

## Post #3 by @lassoan (2019-12-04 15:15 UTC)

<aside class="quote no-group" data-username="Amine" data-post="1" data-topic="9382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>drag and drop function to a slicelet</p>
</blockquote>
</aside>
<p>We do not recommend to implement slicelets without main window for many reasons. Slicer now has built-in scripts to strip down the default main window from Python (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">here</a>). For more control, you can create a <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">custom application</a> in C++ (based on a default main window that you can customize any way you need).</p>

---

## Post #4 by @jamesobutler (2020-01-19 18:28 UTC)

<p>I came across this thread as I was experimenting adding a custom drop action for a custom app using only python.  With the code below I was able to redefine the drop action to execute what I put in <code>dropEvent</code> when I dropped a file path instead of the Slicer default of opening the Add Data Dialog.</p>
<pre><code class="lang-python">class MyClass(qt.QWidget):
    def eventFilter(self, object, event):
        """
        Custom event filter for Slicer Main Window.

        Inputs: Object (QObject), Event (QEvent)
        """
        if event.type() == qt.QEvent.DragEnter:
            self.dragEnterEvent(event)
            return True
        if event.type() == qt.QEvent.Drop:
            self.dropEvent(event)
            return True
        return False
    def dragEnterEvent(self, event):
        """
        Actions to do when a drag enter event occurs in the Main Window.

        Read up on https://doc.qt.io/qt-5.12/dnd.html#dropping
        Input: Event (QEvent)
        """
        if event.mimeData().hasUrls:
            event.acceptProposedAction()  # allows drop event to proceed
        else:
            event.ignore()
    def dropEvent(self, event):
        """
        Actions to do when an item is dropped onto the Main Window.

        Read up on https://doc.qt.io/qt-5.12/dnd.html#dropping
        Input: Event (QEvent)
        """
        print("Custom drop code goes here")

my_class = MyClass()
slicer.util.mainWindow().installEventFilter(my_class)
</code></pre>

---

## Post #5 by @Amine (2020-01-20 12:56 UTC)

<p>Thanks for your answer, i did use almost the same process without merging the filters in slicer main window and instead did an override of the qt.QWidget class methods and used it as the main slicelet window.<br>
Instead of <code>eventFilter</code> i had:</p>
<blockquote>
<pre><code>class MyClass(qt.QWidget):
    def __init__(self, type, parent=None):
        super(MyClass, self).__init__(parent)
        self.setAcceptDrops(True)
</code></pre>
</blockquote>
<p>The following functions are the same,</p>
<p>Your approach is great to change the main slicer window drag and drop actions, thank you for pointing it out!</p>

---
