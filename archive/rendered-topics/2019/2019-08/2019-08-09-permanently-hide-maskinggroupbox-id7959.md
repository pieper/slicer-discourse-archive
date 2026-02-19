---
topic_id: 7959
title: "Permanently Hide Maskinggroupbox"
date: 2019-08-09
url: https://discourse.slicer.org/t/7959
---

# Permanently hide MaskingGroupBox

**Topic ID**: 7959
**Date**: 2019-08-09
**URL**: https://discourse.slicer.org/t/permanently-hide-maskinggroupbox/7959

---

## Post #1 by @EricM (2019-08-09 11:14 UTC)

<p>Hello community,</p>
<p>I am trying to simplify the segmentEditorWidget as much as possible. One feature I would like to do is hide the “MaskingGroupBox” in the “Paint” and “Draw” Effects. I have automatically set the “Modify other segments” to “Allow overlap”, and now, I would like to hide the entire MaskingGroupBox to avoid the user changing this.</p>
<p>I have tried the following:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
#various commands to set MRML scene, adding nodes, etc.
maskingGroupBox = segmentEditorWidget.findChild('ctkCollapsibleGroupBox','MaskingGroupBox')
maskingGroupBox.findChild('QComboBox','OverwriteModeComboBox').setCurrentIndex(2)
maskingGroupBox.setHidden(True)
</code></pre>
<p>However, every time I click on the “Paint” or “Draw” QToolButton, the MaskingGroupBox always reappears. I have noticed that when clicking on these buttons, the following signals are produced: Pressed, Toggled, Clicked.</p>
<p>I thus tried:</p>
<pre><code class="lang-auto">effectsGroupBox = segmentEditorWidget.findChild('QGroupBox','EffectsGroupBox')
paintButton = effectsGroupBox.findChild('QToolButton','Paint')
drawButton = effectsGroupBox.findChild('QToolButton','Draw')

def hideMaskingGroupBox():
  slicer.util.mainWindow().findChild('qSlicerModulePanel','ModulePanel').findChild('ctkCollapsibleGroupBox','MySegmentation').findChild('ctkCollapsibleGroupBox','MaskingGroupBox').hide() #this is where I keep my segmentEditorWidget module

paintButton.pressed.connect(hideMaskingGroupBox)
paintButton.toggled.connect(hideMaskingGroupBox)
paintButton.clicked.connect(hideMaskingGroupBox)

drawButton.pressed.connect(hideMaskingGroupBox)
drawButton.toggled.connect(hideMaskingGroupBox)
drawButton.clicked.connect(hideMaskingGroupBox)
</code></pre>
<p>For a brief moment, I can see the MaskingGroupBox disappear, but then it always reappears, so there must be another action after the last “clicked” signal that makes the MaskingGroupBox reappear. What makes me think this is because If I click again on the already clicked “Paint” or “Draw” box, the MaskingGroupBox disappears. However, if I switch Effects, it appears again…</p>
<p>Is there anyway to override this? Could someone let me know what action is causing the MaskingGroupBox to appear automatically?</p>
<p>Thank you for your help,<br>
Eric</p>

---

## Post #2 by @lassoan (2019-08-10 18:39 UTC)

<p>It would be hard to hack the segment editor widget from outside to prevent the masking section to reappear. Instead, you could add a “maskingOptionsVisible” property to <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx" rel="nofollow noopener">qMRMLSegmentEditorWidget</a> that would prevent the groupbox to be displayed <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L1638" rel="nofollow noopener">here</a>.</p>
<p>This would be a small change, so if you send us a pull request then we should be able to review and integrate it very quickly.</p>

---

## Post #3 by @EricM (2019-08-13 08:27 UTC)

<p>Hi Andras,<br>
Thanks for your quick reply. I will build Slicer and try to modify the source code. I will probably get around to trying this in the beginning of September. I’ll keep everyone posted.<br>
Thanks,<br>
Eric</p>

---
