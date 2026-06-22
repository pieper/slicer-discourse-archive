---
topic_id: 47334
title: "slicer.modules.SegmentEditorWidget does not exists anymore"
date: 2026-06-14
url: https://discourse.slicer.org/t/47334
last_bumped: 2026-06-21T22:34:36.785Z
---

# slicer.modules.SegmentEditorWidget does not exists anymore

**Topic ID**: 47334
**Date**: 2026-06-14
**URL**: https://discourse.slicer.org/t/slicer-modules-segmenteditorwidget-does-not-exists-anymore/47334

---

## Post #1 by @joachim (2026-06-14 18:29 UTC)

<p>I haven’t updated Slicer for a while, but now my <code>.slicerrc</code> does not work as usual. I have the line <code>slicer.modules.SegmentEditorWidget.editor.findChild( "QWidget", "EffectsGroupBox" )</code>, but in the newest Slicer version the <code>SegmentEditorWidget</code> is not there unless I have opened that module in Slicer window (for example by <code>slicer.utils.selectModule( "SegmentEditor" )</code>). However, opening that module creates a Segmentation node which I do not want.</p>
<p>How do I get access to the <code>SegmentEditorWidget</code>, without creating a Segmentation node?</p>
<hr>
<p>My context: I use the following code in my startup file in order to set up shortcuts which I can access with my Wacom tablet menu:</p>
<pre data-code-wrap="python"><code class="lang-python">def setupSegmentEditorShortcuts():
    # find buttons
    widget = slicer.modules.SegmentEditorWidget.editor.findChild("QWidget", "EffectsGroupBox")
    def addEffectShortcut(name, keysequence ):
        but = widget.findChild( 'QToolButton', name )
        shortcut = qt.QShortcut( mainWindow() ) # ^TODO: use SegmentEditorWidget for focused shortcut, does thtat work?
        shortcut.setKey( keysequence )
        shortcut.connect( 'activated()', lambda: but.click() )
    addEffectShortcut( "NULL", qt.QKeySequence( 'Shift+F4' ) )
    addEffectShortcut( "Paint", qt.QKeySequence( 'Shift+F5' ) )
    addEffectShortcut( "Draw", qt.QKeySequence( 'Shift+F6' ) )
    addEffectShortcut( "Erase", qt.QKeySequence( 'Shift+F7' ) )
    addEffectShortcut( "Scissors", qt.QKeySequence( 'Shift+F8' ) )
    # add shortcut for brush size
    qt.QShortcut( qt.QKeySequence( "Shift+F9"), mainWindow() ).connect( 'activated()', lambda: updateBrushSize( -1 ) )
    qt.QShortcut( qt.QKeySequence( "Shift+F10"), mainWindow() ).connect( 'activated()', lambda: updateBrushSize( 1 ) )

</code></pre>

---

## Post #2 by @cpinter (2026-06-15 09:24 UTC)

<p>You can simply create a segment editor widget for your own purposes</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>then set a <code>vtkMRMLSegmentEditorNode</code>, segmentation node, source volume node, etc. just as you would with “the” segment editor widget. If you look at the Segment Editor module code, you’ll see that it’s basically a placeholder for a segment editor widget instance, which is completely reusable.</p>

---

## Post #3 by @joachim (2026-06-21 22:34 UTC)

<p>Using <code>slicer.qMRMLSegmentEditorWidget()</code>instead of <code>slicer.modules.SegmentEditorWidget</code> did not work. However, turned out that there is another way that works: <code>slicer.util.getModuleWidget("SegmentEditor")</code></p>
<p>So now  I am able to add my shortcuts again, and hence use my Wacom tablet for efficient segmentation works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
