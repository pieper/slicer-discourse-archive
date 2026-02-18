# DICOM export failed - UID tags

**Topic ID**: 22317
**Date**: 2022-03-04
**URL**: https://discourse.slicer.org/t/dicom-export-failed-uid-tags/22317

---

## Post #1 by @koeglfryderyk (2022-03-04 17:43 UTC)

<p>I tried exporting a volume to a DICOM series with only the ‘StudyInstanceUID’ tag specified.</p>
<p>This threw the following error:</p>
<blockquote>
<p>If any of UIDs (studyInstanceUID, seriesInstanceUID, and frameOfReferenceInstanceUID) are specified then all of them must be specified.</p>
</blockquote>
<p>So I specified all three tags in the following way:</p>
<pre><code class="lang-auto">exp.setTag('StudyInstanceUID', study_instance_uid)
exp.setTag('SeriesInstanceUID', series_instance_uid)
exp.setTag('FrameOfReferenceUID', frame_of_reference_uid)
</code></pre>
<p>But the export still failed and it gave the same error.</p>
<p>I tried it with several different volumes and the error didn’t change.</p>
<p>Slicer version 4.11.20210226, revision 29738, built 2021-02-28, macOS</p>

---

## Post #2 by @mikebind (2022-03-04 19:09 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="22317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>frameOfReferenceInstanceUID</p>
</blockquote>
</aside>
<p>does not match</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="22317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p><code>exp.setTag('FrameOfReferenceUID', frame_of_reference_uid)</code></p>
</blockquote>
</aside>
<p>Perhaps that is your problem? (The difference is the code is missing “Instance” in the tag name)</p>

---

## Post #3 by @koeglfryderyk (2022-03-04 19:41 UTC)

<p>That worked…!</p>
<p>However, I had another problem with this error message:<br>
the first letter of each of the keywords is lower-case, however, the first letter has to be upper-case. (e.g. in the error message it says ‘studyInstanceUID’ and it should be ‘StudyInstanceUID’</p>
<p>Would it be possible to change the content of this error message? I would make a pull request, however I couldn’t find this anywhere on GitHub.</p>
<p>Also, why doesn’t setTag() throw an error when a wrong tag is used?</p>

---

## Post #4 by @mikebind (2022-03-04 21:21 UTC)

<p>The error message is from <a href="https://github.com/Slicer/Slicer/blob/54884b5c11e9834c3a784bcfbadffdeeaa19ce7e/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx#L358" class="inline-onebox">Slicer/CreateDICOMSeries.cxx at 54884b5c11e9834c3a784bcfbadffdeeaa19ce7e · Slicer/Slicer · GitHub</a></p>
<p>It looks like the underlying export machinery is likely ITK.  Perhaps both cases for the first character of a tag name are accepted? You could test that to see if it is the case.  If not, then the error message should definitely be corrected.</p>
<p>I suspect (but don’t know) that <code>setTag()</code> does not throw an error for a new tag because you could use it to create a new custom tag.</p>

---

## Post #5 by @koeglfryderyk (2022-03-04 23:43 UTC)

<p>that was the problem - it was case sensitive, so the keywords mentioned in the error didn’t work. Now that you showed me where the error is, I’ll make a pull request</p>
<p>I’m not sure about the custom tag - at least when I set a custom tag like this <code>exportable[0].setTag('MyCustomTestTag', 'tag_value')</code> I cannot find this tag anywhere in the DICOM header when I load it for example with pydicom</p>

---
