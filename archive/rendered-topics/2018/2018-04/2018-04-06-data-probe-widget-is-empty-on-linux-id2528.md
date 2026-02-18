# Data Probe widget is empty on Linux

**Topic ID**: 2528
**Date**: 2018-04-06
**URL**: https://discourse.slicer.org/t/data-probe-widget-is-empty-on-linux/2528

---

## Post #1 by @Fernando (2018-04-06 14:22 UTC)

<p>Hi all,</p>
<p>I’ve been getting this error on Linux for a while. Since Linux builds were not available for a while, I waited until a new nightly came up, but the problem is still there. The weird thing is that I also tried on stable 4.8, 4.7 and 4.6 and I’m having the same issue:</p>
<pre><code class="lang-auto">Python 2.7.13 (default, Apr  6 2018, 03:07:59) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
&gt;&gt;&gt; 
Traceback (most recent call last):
  File "/home/fernando/opt/Slicer/Nightly/lib/Slicer-4.9/qt-scripted-modules/DataProbe.py", line 66, in addView
    self.infoWidget = DataProbeInfoWidget(parent)
  File "/home/fernando/opt/Slicer/Nightly/lib/Slicer-4.9/qt-scripted-modules/DataProbe.py", line 95, in __init__
    self._createSmall()
  File "/home/fernando/opt/Slicer/Nightly/lib/Slicer-4.9/qt-scripted-modules/DataProbe.py", line 384, in _createSmall
    self.sliceAnnotations = DataProbeLib.SliceAnnotations()
  File "/home/fernando/opt/Slicer/Nightly/lib/Slicer-4.9/qt-scripted-modules/DataProbeLib/SliceViewAnnotations.py", line 91, in __init__
    self.sliceViewAnnotationsEnabled = settingsValue('DataProbe/sliceViewAnnotations.enabled', 1, converter=int)
  File "/home/fernando/opt/Slicer/Nightly/bin/Python/slicer/util.py", line 1128, in settingsValue
    return converter(settings.value(key)) if settings.contains(key) else default
ValueError: invalid literal for int() with base 10: 'false'

</code></pre>
<p>Do you know what could be happening?</p>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @lassoan (2018-04-06 16:15 UTC)

<p>It seems that your <code>Slicer.ini</code> file got corrupted. In your file<code>sliceViewAnnotations.enabled</code> value is set to <code>false</code>, while it should be <code>0</code> or <code>1</code>.</p>

---

## Post #3 by @Fernando (2018-04-10 10:08 UTC)

<p>Thanks. I just deleted all the config:</p>
<pre><code class="lang-auto">$ rm -rf ~/.config/NA-MIC
</code></pre>

---
