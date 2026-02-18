# New extension: ScriptEditor - a simple programming editor

**Topic ID**: 37806
**Date**: 2024-08-09
**URL**: https://discourse.slicer.org/t/new-extension-scripteditor-a-simple-programming-editor/37806

---

## Post #1 by @muratmaga (2024-08-09 21:26 UTC)

<p>ScriptEditor (formely named SlicerEditor) provides open-source Monaco programming editor as an extension. It is available for <strong>preview</strong> builds of 3D Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69d1fe59695bdefeaf8244dcfc2436556568c654.jpeg" data-download-href="/uploads/short-url/f682HeViNCVWn0rm2Kh6IS13LTe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d1fe59695bdefeaf8244dcfc2436556568c654_2_690x448.jpeg" alt="image" data-base62-sha1="f682HeViNCVWn0rm2Kh6IS13LTe" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d1fe59695bdefeaf8244dcfc2436556568c654_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d1fe59695bdefeaf8244dcfc2436556568c654_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d1fe59695bdefeaf8244dcfc2436556568c654_2_1380x896.jpeg 2x" data-dominant-color="77777A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1247 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It allows auto complete, text highlighting and saving of the python scripts as text nodes into the scene. To execute a code, highlight in the editor, hit copy and then manually paste it into the python console. More information is available at <a href="https://github.com/SlicerMorph/SlicerScriptEditor" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerScriptEditor: a simple programming editor for Slicer based on monaco</a></p>
<p>We are looking for usability suggestions and improvement.</p>
<p>ScriptEditor was prototyped during the <a href="https://projectweek.na-mic.org/PW41_2024_MIT/Projects/SimpleEditorForPythonScripting/" rel="noopener nofollow ugc">41st Project Week</a> by <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/oothomas">@oothomas</a> and <a class="mention" href="/u/smrolfe">@smrolfe</a>.</p>
<p>ScriptEditor is created and made available by funding from National Science Foundation (MorphoCloud: DBI/2301405; Imageomics Institute: OAC/2118240)</p>

---

## Post #2 by @keri (2024-08-09 21:31 UTC)

<p>Looks nice and useful!<br>
Thank you!</p>

---

## Post #3 by @JASON (2024-08-09 21:55 UTC)

<p>This is a very cool idea! <img src="https://emoji.discourse-cdn.com/twitter/sunglasses.png?v=12" title=":sunglasses:" class="emoji" alt=":sunglasses:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2024-08-10 13:04 UTC)

<p>Thank you for the contribution, I’ll give this a try!</p>
<p>To avoid user confusion, we need to improve the extension name:</p>
<ul>
<li>We already have “Segment Editor”, we’ll have a “Model Editor”, and probably other similar module and extension names will come up, so it would be inappropriate for an extension to claim to be The Slicer Editor. It has to be more specific.</li>
<li>We are also trying to reduce the number of extensions that use “Slicer” as name prefix, because it is harder to find extensions if most of them are called SlicerXyz. For example it can be quite annoying when you are trying to find an extension but you don’t remember the exact name and you need to browse two alphabetically ordered lists (the extension names wirh and without the Slicer prefix).</li>
</ul>
<p>For example, ScriptEditor or PythonEditor extension names would work well.</p>

---

## Post #5 by @muratmaga (2024-08-11 01:05 UTC)

<p>yes, we have gone through some thoughts about the extension idea. There is nothing into the tool that makes it specific to Python (and in fact we do want to use it for R integration as well), so perhaps <strong>Script Editor</strong> or <strong>Code Editor</strong>  although I am not sure it is a much of an improvement over <strong>Slicer Editor</strong>, it suffers from the same things.</p>
<p>On that note, I also do not like extensions being prefixed with Slicer. However, it think this is stemming from the extension submission reqiurements checklist, which requires the repo to be name prefixed with Slicer. <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md#todo-list-for-submitting-a-new-extension" rel="noopener nofollow ugc">2nd item here</a></p>
<p>Obviously it is not mandatory to have the repo name reflect the actual extension name. But it is natural to do so. if my extension is Editor, then I wouldn’t want the repo to be SlicerEditor. And if I am going to call the repo SlicerEditor, I would rather not get confused where to use Editor and where to use SlicerEditor (in Cmake files etc) and simply call everything SlicerEditor too…</p>
<p>If we want more unique names, I think we should change that requirement.</p>

---

## Post #6 by @lassoan (2024-08-11 06:17 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="37806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>requires the repo to be name prefixed with Slicer. <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md#todo-list-for-submitting-a-new-extension">2nd item here</a></p>
</blockquote>
</aside>
<p>The recommendation is: <code>Repository name is Slicer+ExtensionName</code>. In this case: extension name is ScriptEditor, repository name is SlicerScriptEditor. I’ll clarify this further in the extension checklist.</p>

---

## Post #7 by @finetjul (2024-08-12 06:27 UTC)

<p>Great extension, thanks.</p>
<p>Here are some thoughts:</p>
<ul>
<li>add a button to execute the code directly from the extension (and with a CTRL+ENTER shortcut) to avoid copy/paste that requires the mouse.</li>
<li>have the extension better integrated from the Python console: e.g. add a button in the console that opens the ScriptEditor extension panel (for discoverability). Or make as much as possible useful features (e.g. auto-completion) from the ScriptEditor extension available within the Python console</li>
</ul>

---

## Post #8 by @muratmaga (2024-08-12 06:45 UTC)

<p>Thank you for the feed back.</p>
<aside class="quote no-group" data-username="finetjul" data-post="7" data-topic="37806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/finetjul/48/146_2.png" class="avatar"> finetjul:</div>
<blockquote>
<p>add a button to execute the code directly from the extension (and with a CTRL+ENTER shortcut) to avoid copy/paste that requires the mouse.</p>
</blockquote>
</aside>
<p>This is also what I want, but there is currently a usability issue. We tried directly sending the code (both via a run button and/or a shortcut). The issue is code is executed silently, and unless it produces a visual output (e.g., loading a data), or generates error, there is nothing in the python window. It is not even in the history buffer. This is a very confusing behavior, particularly for the people new to scripting/programming.</p>
<p>By making it an explicit action, our goal is to avoid this confusion. I know it is not convenient, so I would like to know what alternative there might be to have the executed code show up in the python console history buffer.</p>

---

## Post #9 by @finetjul (2024-08-12 06:53 UTC)

<blockquote>
<p>We tried directly sending the code</p>
</blockquote>
<p>I guess that means the python console API should be improved… sorry I do not know much about it. Maybe <a class="mention" href="/u/jcfr">@jcfr</a>  does.<br>
Alternatively, you can “simulate” a user copy/paste with Qt. Maybe there are ways to creating synthetic QEvents that reproduce a copy/paste by a user…</p>

---

## Post #10 by @pieper (2024-08-12 11:58 UTC)

<p>Those are great suggestions <a class="mention" href="/u/finetjul">@finetjul</a> - agreed we should fix the issues rather than remove the features.</p>
<p>Also since this is based on the same core editor of VS code, there are lots of other features we could explore.</p>

---

## Post #11 by @Matteboo (2024-08-12 12:36 UTC)

<p>Thanks you, that will be very usefull<br>
I think that another usefull extension to help beginner script in Slicer would be to have an easy way for a user to get the line of code executed  when clicking a button/doing an action.<br>
I read that such an extension is technically difficult but it would be very usefull for newcomers</p>

---

## Post #12 by @jamesobutler (2024-08-12 14:03 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="11" data-topic="37806">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>I think that another usefull extension to help beginner script in Slicer would be to have an easy way for a user to get the line of code executed when clicking a button/doing an action.</p>
</blockquote>
</aside>
<p>This is specifically like what <a href="https://www.stata.com/" rel="noopener nofollow ugc">stata</a> does with its command history? Is that the specific feature in another application that you wish Slicer had as well? Or is there a feature from a different application?</p>

---

## Post #13 by @evaherbst (2024-08-12 16:51 UTC)

<p>Looks great, looking forward to trying it!</p>

---

## Post #14 by @Matteboo (2024-08-13 15:52 UTC)

<p>I’m not familiar with stata so I don’t know. The thing I was thinking about is COMSOL that allow you to save your model as MATLAB code. That way if there’s something that you don’t know how to code you can just do it in the GUI, save it as matlab code and copy paste the code.<br>
As someone who got into slicer scripting recently, that’s the feature I wish for the most. It would have been especially helpfull when I was just starting.</p>
<p>For a concrete example:<br>
Last time I was loading a and generating picture of liver segmentation. I wanted to change the contrast of the CT to be the abdomen default value. This action takes only a few clicks but I struggled to find the corresponding line of code : <em>slicer.modules.volumes.logic().ApplyVolumeDisplayPreset(VolumeDisplayNode, “CT_ABDOMEN”)</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acb868e17200f8d6e35f0484bbd099509499100f.jpeg" data-download-href="/uploads/short-url/oDXdGY9GVfqRpUdbyqhaHcdcxbN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acb868e17200f8d6e35f0484bbd099509499100f_2_254x250.jpeg" alt="image" data-base62-sha1="oDXdGY9GVfqRpUdbyqhaHcdcxbN" width="254" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acb868e17200f8d6e35f0484bbd099509499100f_2_254x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acb868e17200f8d6e35f0484bbd099509499100f_2_381x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acb868e17200f8d6e35f0484bbd099509499100f_2_508x500.jpeg 2x" data-dominant-color="5B5D61"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">810×796 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @pieper (2024-08-13 18:00 UTC)

<p>The method described here works pretty well for me.  It would be nice if it could be simplified but I don’t think there’s any completely automatic solution.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---

## Post #16 by @chz31 (2024-08-16 01:43 UTC)

<p>Looks amazing! Looking forward to try it.</p>

---

## Post #17 by @muratmaga (2024-10-02 03:24 UTC)

<p>Slightly revised version of this extension is now on the catalogue. The name was changed to ScriptEditor to avoid confusion with Segment Editor.</p>

---
