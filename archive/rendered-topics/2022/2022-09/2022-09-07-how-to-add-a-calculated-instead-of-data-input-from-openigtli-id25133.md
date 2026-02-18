# How to add a calculated (instead of data input from OpenIGTLInk IO) proxy node in SequenceBrowser when recording an ultrasound sequences?

**Topic ID**: 25133
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/how-to-add-a-calculated-instead-of-data-input-from-openigtlink-io-proxy-node-in-sequencebrowser-when-recording-an-ultrasound-sequences/25133

---

## Post #1 by @sunshine (2022-09-07 04:25 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first extension module to do a real-time ultrasound annotation.<br>
I am now able to write a module for offline annotation with ultrasound sequences recorded as SequenceBrowsers in module Sequences.</p>
<p>However, both widgetRepresentation() and logic() of module Sequences do not have public functions of live data retrieval that can be called in a customer extension module.</p>
<p>How can I add an annotation (PointList) sequence node into a SequenceBrowser with the Proxy-Node being a PointList that is calculated using my own code (instead of data retrieved from OpenIGTLink IO)?</p>
<p>Please let me know if this expectation is currently not possible.</p>
<p>Thank you so much in advance!</p>

---
