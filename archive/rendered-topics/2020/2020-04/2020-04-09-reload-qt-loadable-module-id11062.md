---
topic_id: 11062
title: "Reload Qt Loadable Module"
date: 2020-04-09
url: https://discourse.slicer.org/t/11062
---

# Reload Qt Loadable Module

**Topic ID**: 11062
**Date**: 2020-04-09
**URL**: https://discourse.slicer.org/t/reload-qt-loadable-module/11062

---

## Post #1 by @xlucox (2020-04-09 20:53 UTC)

<p>Hi everyone !!!</p>
<p>I’m adding some functionalities to the MultiVolumeExplorer Module. I wonder if there is any easy way to reload this module from Slicer. Always when I edit the code of the module I have to restart slicer to reload this module.</p>
<p>Thank you very much.</p>
<p>Kind regards.</p>

---

## Post #2 by @pieper (2020-04-09 21:50 UTC)

<p>No, you can’t reload the C++ based modules unfortunately.</p>
<p>Often it’s a good idea to put infrastructure in the C++ code, like filters or other algorithms, test it in isolation (small test programs) and then develop your module in Pythong.</p>

---

## Post #3 by @xlucox (2020-04-09 23:29 UTC)

<p>Ok,</p>
<p>Thank you very much.</p>

---

## Post #4 by @lassoan (2020-04-10 02:00 UTC)

<p>Important: Sequences will be merged into Slicer core in a couple of days (see progress <a href="https://github.com/Slicer/Slicer/pull/4810">here</a>) and MultiVolume explorer will be replaced by Sequences infrastructure (which support 4D sequences of any nodes - transforms, markups, models, etc. - and not just volumes). MultiVolume modules will be probably kept around for a year or so, but no further developments will be done and at some point the modules will be moved out to an unsupported extension.</p>
<p>Therefore, I would not recommend to make any changes or improvements to MultiVolumeExplorer now. What improvements would you like to implement?</p>

---

## Post #5 by @xlucox (2020-04-10 16:30 UTC)

<p>I just changed some little things.</p>
<p>For example: Instead of show the current frame number in the frame slider, it shows the current frame label. I also added a new button to fit the data plotted in the chart when I make a ROI.</p>

---

## Post #6 by @lassoan (2020-04-10 16:44 UTC)

<p>In Sequences you can already switch between showing index number or value (advanced section of browser).</p>
<p>Computing plot from a ROI is not available yet - it would be great if you could contribute it (just wait a few days until Sequences are merged into Slicer core). I would add a separate module for this (probably the current quick plotting feature will be moved out from Sequences/SequenceBrowser module to a separate module, too).</p>

---
