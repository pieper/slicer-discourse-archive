---
topic_id: 9744
title: "Using Eventfilters On Qt Objects"
date: 2020-01-09
url: https://discourse.slicer.org/t/9744
---

# Using EventFilters on qt objects

**Topic ID**: 9744
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/using-eventfilters-on-qt-objects/9744

---

## Post #1 by @Greydon_Gilmore (2020-01-09 00:53 UTC)

<p>Hi all,</p>
<p>I am attempting to ignore mouse wheel events on a qt.QDoubleSpinBox. This would be within a ScriptedLoadableModuleWidget.</p>
<p>How would I go about doing this?</p>
<pre><code class="lang-auto">def eventFilter(self, obj, event):
	if event.type() == qt.QEvent.Wheel and isinstance(obj, qt.QDoubleSpinBox):
		event.ignore()
		return True
	else:
		return False
</code></pre>
<p>Thank you,<br>
Greydon</p>

---

## Post #2 by @lassoan (2020-01-09 04:46 UTC)

<p>See a complete, working example in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py">SegmentEditorThresholdEffect.py</a> (HistogramEventFilter).</p>

---

## Post #3 by @Greydon_Gilmore (2020-01-09 16:28 UTC)

<p>For anyone looking for the answer to this question but don’t want to scroll through over 1000 lines of code:</p>
<p>You need to make a separate <code>qt.Object</code> class:</p>
<pre><code class="lang-auto">class customEventFilter(qt.QObject):
	def eventFilter(self, obj, event):
		'''
		Event filter for rerouting wheelEvents away from double spin boxes.
		'''
		if event.type() == qt.QEvent.Wheel and isinstance(obj, qt.QDoubleSpinBox):
			#this handles all the wheel events for the double spin boxes
			event.ignore()
			return True
		
		return False
</code></pre>
<p>If you’d like to ignore another type of event replace <code>qt.QEvent.Wheel</code> with the specific <a href="https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/QEvent.Type.html" rel="nofollow noopener">qt.Event</a>. If you’d like to apply this filter to a different object then replace <code>qt.QDoubleSpinBox</code> with the specific object.</p>
<p>You will then need to install this filter on the specific objects you’d like to inherit the filter:</p>
<pre><code class="lang-auto">self.customEventFilter = customEventFilter()

path = os.path.join(os.path.dirname(self.script_path), 'Resources', 'UI', 'eventFilterExample.ui')
self.ui = slicer.util.loadUI(path)

self.CrosshairCoords_X = self.ui.findChild(qt.QDoubleSpinBox, "CrosshairCoords_X")
self.CrosshairCoords_X.installEventFilter(self.customEventFilter)
</code></pre>
<p>Cheers,<br>
Greydon</p>

---
