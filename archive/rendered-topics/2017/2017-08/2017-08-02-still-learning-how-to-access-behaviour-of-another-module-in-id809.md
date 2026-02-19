---
topic_id: 809
title: "Still Learning How To Access Behaviour Of Another Module In"
date: 2017-08-02
url: https://discourse.slicer.org/t/809
---

# Still learning: how to access behaviour of another module in my module

**Topic ID**: 809
**Date**: 2017-08-02
**URL**: https://discourse.slicer.org/t/still-learning-how-to-access-behaviour-of-another-module-in-my-module/809

---

## Post #1 by @mschumaker (2017-08-02 17:31 UTC)

<p>Hello, I’m still learning how to write my own modules. I would like to replicate the behaviour of the “Show DICOM Browser” button from the DICOM module in a button placed in my own module. I tried using the “Record Macro” feature to get a hint, but I didn’t find it useful. How should I proceed?<br>
Thanks.</p>

---

## Post #2 by @cpinter (2017-08-02 17:44 UTC)

<p>This python code will open the browser:</p>
<pre><code>slicer.modules.dicom.widgetRepresentation()
slicer.modules.DICOMWidget.enter()
</code></pre>
<p>You need the first line as well, because it makes sure the objects are instantiated.</p>

---

## Post #3 by @mschumaker (2017-08-02 18:57 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>slicer.modules.dicom.widgetRepresentation()<br>
slicer.modules.DICOMWidget.enter()</p>
</blockquote>
</aside>
<p>Fantastic, thank you.</p>

---
