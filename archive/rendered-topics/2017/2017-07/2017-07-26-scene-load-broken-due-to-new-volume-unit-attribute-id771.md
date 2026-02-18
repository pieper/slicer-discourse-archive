# Scene load broken due to new volume unit attribute

**Topic ID**: 771
**Date**: 2017-07-26
**URL**: https://discourse.slicer.org/t/scene-load-broken-due-to-new-volume-unit-attribute/771

---

## Post #1 by @cpinter (2017-07-26 13:40 UTC)

<p>py_SubjectHierarchyGenericSelfTest started failing due to a failure of loading a scene. Digging into it, this error message (Error parsing XML in stream at line 38, column 151, byte index 10406: not well-formed (invalid token)) points to this line:</p>
<pre><code> &lt;Volume
  id="vtkMRMLScalarVolumeNode1" name="303: Unnamed Series" hideFromEditors="false" selectable="true" selected="false" attributes="DICOM.QuantityCode:{"CodeMeaning": "Attenuation Coefficient", "CodingSchemeDesignator": "DCM", "CodeValue": "110852"};DICOM.UnitsCode:{"CodeMeaning": "Hounsfield unit", "CodingSchemeDesignator": "UCUM", "CodeValue": "[hnsf'U]"};DICOM.instanceUIDs:1.2.826.0.1.3680043.8.274.1.1.2895132669.2819.7830930470.104 1.2.826.0.1.3680043.8.274.1.1.7405746770.5479.5810198465.165 1.2.826.0.1.3680043.8.274.1.1.3116843726.8233.3216805822.278 1.2.826.0.1.3680043.8.274.1.1.3263562271.1129.3152372828.828 1.2.826.0.1.3680043.8.274.1.1.4153098248.6996.3632241357.584 1.2.826.0.1.3680043.8.274.1.1.4770490127.9140.3834798946.219 1.2.826.0.1.3680043.8.274.1.1.6553947155.9980.4127073411.708 1.2.826.0.1.3680043.8.274.1.1.4554129680.8666.4619454551.121 1.2.826.0.1.3680043.8.274.1.1.5613951088.5396.9288000555.812 1.2.826.0.1.3680043.8.274.1.1.5710109910.8056.9834733307.864" displayNodeRef="vtkMRMLScalarVolumeDisplayNode1" references="display:vtkMRMLScalarVolumeDisplayNode1;" userTags="" ijkToRASDirections="-1   0   0 0   -1   0 0 0 1 " spacing="49 49 23" origin="248.844 248.289 -123.75" &gt;&lt;/Volume&gt;
</code></pre>
<p>Specifically the quotation mark before “CodeMeaning”. As this attribute is added when loading a volume from DICOM, I suspect that now all saved scenes are invalid that contain a DICOM volume. It would be good either to revert this commit<br>
<a href="https://github.com/Slicer/Slicer/commit/9df49830897e2d0d6e458e7390eec7807a817b41" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/9df49830897e2d0d6e458e7390eec7807a817b41</a><br>
while fixing this, or fixing this quickly.</p>

---

## Post #2 by @lassoan (2017-07-26 13:51 UTC)

<p>I’ll take care of this by this information into a member variable. We could encode the attribute to be able to store special characters, such as ", but we’ll use the unit for many things, so it’s better not to store it in just a generic metadata.</p>
<p>Scene corruption is a serious error that our development process should have captured. The pull request was open for a few days but just by looking at the code nobody noticed the error. SH test did capture the error (see <a href="http://slicer.cdash.org/testDetails.php?test=8141795&amp;build=1069200">failed test this morning</a>, it even showed the relevant error message on the dashboard “Error parsing XML in stream at line 38, column 151, byte index 10404: not well-formed (invalid token)”) and the dashboard is normally green (we don’t have any failing test), so it should not be too difficult to spot new errors.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> do you know why the tests were not executed automatically by the pull request (<a href="https://github.com/Slicer/Slicer/pull/750">https://github.com/Slicer/Slicer/pull/750</a>)?<br>
<a class="mention" href="/u/fedorov">@Fedorov</a> do you remember if you’ve run the automatic tests manually and if you saw the new test failure?</p>

---

## Post #3 by @fedorov (2017-07-26 14:03 UTC)

<p>Sorry for the trouble guys. I admit I did not run the tests manually, so it is my fault!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> will you implement the solution you mentioned, or should I revert the commit?</p>

---

## Post #4 by @jcfr (2017-07-26 14:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>this information into a member variable</p>
</blockquote>
</aside>
<p>Definitively, storing a complex document (e.g json) as a MRML attribute is a stretch.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>do you know why the tests were not executed automatically by the pull request</p>
</blockquote>
</aside>
<p>Tests are not yet run automatically, we need to finalize integration of the work of Mayeul. For now, it is only the build.</p>
<p>As soon as this is enabled, we will capture such regression beforehand.</p>

---

## Post #5 by @lassoan (2017-07-26 14:05 UTC)

<p>I revert the commit now and implement member variable storage within a few hours.</p>

---

## Post #6 by @jcfr (2017-07-26 14:07 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for tackling this.</p>
<p>On my side, I will look into adding the testing to the PR later this week</p>

---

## Post #7 by @lassoan (2017-07-26 14:10 UTC)

<p>Reverted in rev r26176.</p>

---

## Post #8 by @cpinter (2017-07-26 14:11 UTC)

<p>Thanks guys!</p>
<p>Do you think it would be worth sanitizing an attribute when setting (and restoring it when getting)? Users might add attributes with quotation marks and they might wonder what broke. Not sure if simply escaping the quotation mark would solve this, but if it does, then it’s a very simple solution.</p>

---

## Post #9 by @lassoan (2017-07-26 14:14 UTC)

<p>Yes, currently special characters in any node properties (name, description, attributes, …) can lead to invalid scenes - see <a href="https://issues.slicer.org/view.php?id=3406">https://issues.slicer.org/view.php?id=3406</a>. There is a function in MRML node already for encoding/decoding, we could probably use that in read/write XML of MRML node to fix this.</p>

---
