# Loading JSON/XML data

**Topic ID**: 1445
**Date**: 2017-11-13
**URL**: https://discourse.slicer.org/t/loading-json-xml-data/1445

---

## Post #1 by @jdx-john (2017-11-13 14:30 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat</a> lists many image and related formats.</p>
<p>But what if I have some custom data in JSON or XML files… not a dataset, some arbitrary data needed by an extension feature or to feed into VTK functions.<br>
Is built-in loading/parsing of such files supported in Slicer?</p>

---

## Post #2 by @ihnorton (2017-11-13 14:52 UTC)

<p>for C++:</p>
<ul>
<li>JSON: both RapidJSON and jsoncpp are available (I think jsoncpp will eventually be removed, but could be wrong about that)</li>
<li>XML: MRML is an XML variant, parsed with VTK’s API over libxml2. You could probably use whichever is most convenient.</li>
</ul>
<p>for Python:</p>
<ul>
<li>
<code>import json</code>, <code>import xml</code> (although there are nicer external libraries for both)</li>
</ul>

---

## Post #3 by @jdx-john (2017-11-13 15:17 UTC)

<p>Python is most likely though I’m not a Python dev… are you saying<br>
’json’/‘xml’ are already used in Slicer or are parts of Slicer available to<br>
Python scripts? This seems an easy answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2017-11-13 16:00 UTC)

<p>Yes, both json and xml files are used extensively in Slicer.</p>

---
