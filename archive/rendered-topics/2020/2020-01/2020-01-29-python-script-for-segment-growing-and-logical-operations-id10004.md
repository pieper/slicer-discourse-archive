# Python Script for segment growing and Logical operations

**Topic ID**: 10004
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/python-script-for-segment-growing-and-logical-operations/10004

---

## Post #1 by @manjula (2020-01-29 17:51 UTC)

<p>Hi all,</p>
<p>I want to write a python code to grow a segment margin. (need to overlap and also grow in to a specified intensity only)</p>
<p>Then i want to subtract the newly grown segment from the original.</p>
<p>How do i do that ?</p>
<p>I tried to look for simpleITK  documentation at</p>
<p><a href="https://itk.org/SimpleITKDoxygen120/html/index.html" rel="nofollow noopener">https://itk.org/SimpleITKDoxygen120/html/index.html</a> but it is not working.</p>
<p>It would be great if some</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-01-29 17:56 UTC)

<p>These examples should help you getting started: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @manjula (2020-01-29 17:58 UTC)

<p>Thank you Prof Lasso,</p>
<p>I looked at them also but i could not find how to grow and subtract segments.</p>
<p>Is there any documentation for simpleITK like a handbook available ?</p>
<p>i looked at <a href="https://itk.org/SimpleITKDoxygen120/html/index.html" rel="nofollow noopener">https://itk.org/SimpleITKDoxygen120/html/index.html</a>  but the link is not working.</p>

---

## Post #4 by @lassoan (2020-01-29 18:31 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10004">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I looked at them also but i could not find how to grow and subtract segments.</p>
</blockquote>
</aside>
<p>There are no examples for using all the effects, but you can start from those examples and just change the effect name and input parameters if you want to use different effects.</p>
<p>You can post questions about SimpleITK to the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---

## Post #5 by @manjula (2020-01-29 18:32 UTC)

<p>Thank Prof Lasso. I will try to work with this information.</p>

---

## Post #6 by @Juicy (2020-01-29 22:43 UTC)

<p>I have a question slightly related to this. I am referring to the code in <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">this link</a>.</p>
<p>To set the active effect and change some parameters this following code is used:</p>
<pre><code># Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","35")
effect.setParameter("MaximumThreshold","695")
effect.self().onApply()
</code></pre>
<p>I see the setParameter() method takes a string input (to select the parameter) and a value input (to define the value of that parameter). Is there any documentation anywhere that lists what the names of all the parameters are for a given active effect? I have been just trying to guess what the parameters are called but not having much luck.</p>

---

## Post #7 by @Juicy (2020-01-29 23:09 UTC)

<p>I think I answered my own question.</p>
<p>Found this link: <a href="https://discourse.slicer.org/t/scissors-segment-editor-effects-from-a-script/8348/2">https://discourse.slicer.org/t/scissors-segment-editor-effects-from-a-script/8348/2?u=juicy</a></p>
<p>I found the slicer segment editor effect code in the Slicer core code <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects" rel="nofollow noopener">here</a></p>
<p>I should be able to find the parameter names which I need by sifting through the code.</p>

---

## Post #8 by @lassoan (2020-01-29 23:36 UTC)

<p>It would be nice to extract the parameter names from the code and present it in a developer documentation page instead of requiring developers to mine it from the source code.</p>
<p>However, for this we would need much tighter integration between source code and documentation. Currently they are stored in two separate systems (svn and wiki), but soon both will be managed in git. When the transition completes, in a few weeks or worst case months, we can start working on improving the developer documentation with such details.</p>

---

## Post #9 by @manjula (2020-01-30 07:50 UTC)

<p>Thank you <a class="mention" href="/u/juicy">@Juicy</a> and <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>This has been super helpful for me as i try to work on the code. What i was trying to ask for was what <a class="mention" href="/u/juicy">@Juicy</a> asked even though i failed to put it in that way, instead of having to come back here and asking is there any documentation related to 3DSlicer  python interactor    that gives functions/methods and what inputs they take etc…   so we can easily go through and write the code…I find good documents on C++ but i don’t know it.</p>

---

## Post #11 by @lassoan (2020-01-30 15:17 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">PerkLab Scripting and module development tutorial</a> contains links to API documentation sites and example of how to use Python <code>help</code> command to get Python-style manual for a specific command or class in the console.</p>
<p>I see how argument type information specified in C++ may look alien to Python developers, but it is just a small syntax difference that can be “translated” by a number of simple rules. I give a few examples here how a mapping could look like and if you find it useful then let me know and I’ll consider creating a more comprehensive documentation page:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>C++</th>
<th>Python</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>nullptr</td>
<td>None</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Q(some-class-name)*</td>
<td>qt.Q(some-class-name)</td>
<td>QWidget*</td>
<td>qt.QWidget</td>
<td></td>
</tr>
<tr>
<td>Qt::(some-type)</td>
<td>qt.Qt.(some-type)</td>
<td>Qt::WindowFlags</td>
<td>qt.Qt.WindowFlags</td>
<td></td>
</tr>
<tr>
<td>qMRML(some-class-name)*</td>
<td>slicer.qMRML(some-class-name)</td>
<td>qMRMLTableWidget*</td>
<td>slicer.qMRMLTableWidget</td>
<td></td>
</tr>
</tbody>
</table>
</div><p>Syntax differences:</p>
<ul>
<li>type before the method name specifies what type of data the method returns; <code>void</code> means that the method does not return any data</li>
<li>const before an argument type means that the called method will not change that input argument</li>
</ul>

---
