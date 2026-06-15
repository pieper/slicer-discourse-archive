---
topic_id: 47334
title: "slicer.modules.SegmentEditorWidget does not exists anymore"
date: 2026-06-14
url: https://discourse.slicer.org/t/47334
last_bumped: 2026-06-14T18:29:30.634Z
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
