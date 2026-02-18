# My QActions hangs the Slicer application

**Topic ID**: 12152
**Date**: 2020-06-22
**URL**: https://discourse.slicer.org/t/my-qactions-hangs-the-slicer-application/12152

---

## Post #1 by @joachim (2020-06-22 11:21 UTC)

<p>I’m creating 2 layouts for manual segmentation. And I’m trying to create <em>QtAction</em> s to trigger these layouts (<em>slicerrc.py</em>-file can be found <a href="https://github.com/karamellpelle/SlicerRC/blob/965e571a12f9eab596626046a851095579c9c17e/slicerrc.py" rel="noopener nofollow ugc">here</a>):</p>
<pre><code class="lang-auto"># XML definitions (definitions omitted)
LAYOUTXML_MANUALSEGMENTATION_3D = "..."
LAYOUTXML_MANUALSEGMENATION = "..."
# out-of-the-blue values
LAYOUTID_MANUALSEGMENTATION_3D = 440
LAYOUTID_MANUALSEGMENTATION    = 442


# switch layout
def setLayout(idx):
    slicer.app.layoutManager().setLayout( idx )


# global variables to access our layout actions
actionSegmentation3D = None
actionSegmentation   = None


# callback for action
def triggerLayoutManualSegmentation():
    # set layout
    setLayout( LAYOUTID_MANUALSEGMENTATION )

# callback for action
def triggerLayoutManualSegmentation3D():
    # set layout
    setLayout( LAYOUTID_MANUALSEGMENTATION_3D )

# callback for shortcut
def toggleLayoutManualSegmentation():
    lm = slicer.app.layoutManager()
    if lm.layout == LAYOUTID_MANUALSEGMENTATION_3D:
        actionSegmentation.triggered()
    else: 
        actionSegmentation3D.triggered()


# create our custom layouts, add actions in layout menu, create shortcut
def createCustomLayouts():
    # create layouts
    slicer.app.layoutManager().layoutLogic().GetLayoutNode().AddLayoutDescription( LAYOUTID_MANUALSEGMENTATION_3D, LAYOUTXML_MANUALSEGMENTATION_3D )
    slicer.app.layoutManager().layoutLogic().GetLayoutNode().AddLayoutDescription( LAYOUTID_MANUALSEGMENTATION, LAYOUTXML_MANUALSEGMENTATION )
    # create menu entries
    global actionSegmentation3D
    global actionSegmentation
    actionSegmentation3D = mainWindow().findChild('QMenu', 'LayoutMenu').addAction( "Segmentation+3D" ) # TODO: create Icon: #.setIcon(qt.QIcon(':Icons/Go.png'))
    actionSegmentation3D.setToolTip("Manual Segmentation")
    actionSegmentation3D.connect('triggered()', lambda: triggerLayoutManualSegmentation3D() )
    actionSegmentation = mainWindow().findChild('QMenu', 'LayoutMenu').addAction( "Segmentation" ) # TODO: create Icon: #.setIcon(qt.QIcon(':Icons/Go.png'))
    actionSegmentation.setToolTip("Manual Segmentation, fullscreen")
    actionSegmentation.connect('triggered()', lambda: triggerLayoutManualSegmentation() )
    # create toggle shortcut
    shortcutToggleSeg = qt.QShortcut( mainWindow() )
    shortcutToggleSeg.setKey( qt.QKeySequence('g') )
    shortcutToggleSeg.connect( 'activated()', lambda: toggleLayoutManualSegmentation() )
    # set custom layout right now. this makes sure volumes are loaded into our custom Slice Views
    #actionSegmentation3D.triggered() # TODO: enable when slicerrc.py works

createCustomLayouts()
</code></pre>
<p>However, I can’t get this working. And if I do <code>actionSegmentation3D.triggered()</code> and then <code>actionSegmentation.triggered()</code> in the Python console, Slicer hangs and stops working. What am I doing wrong? I don’t know Python, so help would be appreciated.</p>

---

## Post #2 by @lassoan (2020-06-22 15:39 UTC)

<p>The problem is that you missed the <code>layoutSwitchAction.setData(layoutId)</code> call. The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">example code in the script repository</a> was misleading because you don’t actually need to do anything else (no need to connect a custom function to the trigger). I’ve updated the example now.</p>

---

## Post #3 by @joachim (2020-06-23 16:44 UTC)

<p>Thank you, it worked!</p>
<p>I see you made <a href="https://github.com/Slicer/Slicer/blob/21fa3d053e3eba4a18c50d7ba59a9495e3f266a9/Base/QTApp/qSlicerMainWindow.cxx#L1529" rel="nofollow noopener">a fix for this</a>. I guess you can remove the “find” code in <code>void qSlicerMainWindow::onLayoutActionTriggered(QAction* action)</code> since the <code>QAction</code> is contained in <em>LayoutMenu</em> according to <a href="https://doc.qt.io/qt-5/qmenu.html#triggered" rel="nofollow noopener"><code>QMenu</code> documentation</a>.</p>
<p>Also, connecting the submenus <a href="https://github.com/Slicer/Slicer/blob/21fa3d053e3eba4a18c50d7ba59a9495e3f266a9/Base/QTApp/qSlicerMainWindow.cxx#L403" rel="nofollow noopener"><code>menuConventionalQuantitative</code></a> etc. to this slot can be removed since the parent menu (<em>LayoutMenu</em>) will handle the children. And in fact should be removed since it will set the layout twice. If I read the documentation right.</p>
<p>The example in Wiki has to be changed since a <code>QAction</code> not part of <em>LayoutMenu</em> (i.e. <em>viewToolBar</em>) will not be able to switch layout. I suggest to only use LayoutMenu. This will also reflect the current layout by showing the corresponding icon/text in <em>LayoutMenu</em>:</p>
<pre><code class="lang-auto"># Add button to LayoutMenu
menu = mainWindow().findChild('QMenu', 'LayoutMenu')
action = menu.addAction('Custom layout') 
action.setData(layoutId) # 'layoutId' defines the number for your layout
action.setIcon(qt.QIcon(':Icons/Go.png'))
action.setToolTip('Switch to my custom layout')
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2020-06-23 18:37 UTC)

<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="12152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>I guess you can remove the “find” code in <code>void</code></p>
</blockquote>
</aside>
<p>Yes, it is just an extra check. Unfortunately, it is not described in code comments or commit comments why it was added. We can remove it when we make significant changes to that part of the code anyway (e.g., when implementing custom “favorite views”).</p>
<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="12152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Also, connecting the submenus <a href="https://github.com/Slicer/Slicer/blob/21fa3d053e3eba4a18c50d7ba59a9495e3f266a9/Base/QTApp/qSlicerMainWindow.cxx#L403"> <code>menuConventionalQuantitative</code> </a> etc. to this slot can be removed</p>
</blockquote>
</aside>
<p>Thank you for the suggestion, we have already removed these. The pull request has not been merged yet, as it was part of a larger effort that requires some more work (<a href="https://github.com/Slicer/Slicer/pull/4904">https://github.com/Slicer/Slicer/pull/4904</a>).</p>
<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="12152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>The example in Wiki has to be changed since a <code>QAction</code> not part of <em>LayoutMenu</em> (i.e. <em>viewToolBar</em> ) will not be able to switch layout</p>
</blockquote>
</aside>
<p>The example is for “You can use this code snippet to add a button to the layout selector toolbar” and the corresponding code is correct. We could add example to show how to define QActions in general, but I don’t think it is necessary.</p>

---
