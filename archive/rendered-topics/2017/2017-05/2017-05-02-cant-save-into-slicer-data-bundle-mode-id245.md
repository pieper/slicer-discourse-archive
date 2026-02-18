# Can't save into "Slicer Data Bundle" mode

**Topic ID**: 245
**Date**: 2017-05-02
**URL**: https://discourse.slicer.org/t/cant-save-into-slicer-data-bundle-mode/245

---

## Post #1 by @finetjul (2017-05-02 14:50 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.6.2 and nightly<br>
Expected behavior: Should be able to save scene into “Slicer Data Bundle”<br>
Actual behavior: Fails to save with error message: “Selected directory contains -2 files or directories. Please choose an empty directory.”</p>
<p>Some problems:<br>
<a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L284" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L284</a>   → <br>
On windows, there is no . and … folders:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L294" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L294</a> → <br>
breaks are missing</p>
<p>Bonus: In the file name column, “.*” is enforced and wrongly suffixed onto the name.</p>

---

## Post #2 by @pieper (2017-05-02 15:34 UTC)

<p>I can’t replicate this.</p>
<p>Tried Windows 10, Slicer 4.6.2:</p>
<ul>
<li>start fresh slicer</li>
<li>download MRHead</li>
<li>save data bundle</li>
<li>close scene</li>
<li>reload scene</li>
</ul>
<p>No error messages or abnormal behavior.</p>

---

## Post #3 by @finetjul (2017-05-02 15:42 UTC)

<p>Thanks for trying it out.</p>
<p>Do you choose “Slicer Data Bundle” and not “Medical Reality Bundle”?<br>
Do you save into an empty folder ?</p>

---

## Post #4 by @lassoan (2017-05-02 16:09 UTC)

<p>Medical Reality Bundle (.mrb) works well for me.<br>
If I select the “Slicer Data Bundle (*)” option then I have the same issue.</p>
<p>Should we just remove the Slicer Data Bundle option?</p>

---

## Post #5 by @pieper (2017-05-02 16:19 UTC)

<p>Ah, no, I was using .mrb Medical Reality Bundle, the default.  Right, if I<br>
pick Slicer Data Bundle I see the same errors you reported.</p>
<p>Hate to ask, but why does this second mode even exist?</p>

---

## Post #6 by @jcfr (2017-05-02 19:29 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Great question. Look like the functionality was first added in <a href="https://github.com/Slicer/Slicer/commit/479f8c249">https://github.com/Slicer/Slicer/commit/479f8c249</a></p>

---

## Post #7 by @pieper (2017-05-03 00:25 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> yes, the save to MRB code is something I added.</p>
<p>But the code Julien pointed to is something he committed [1] and it really doesn’t look like my code…</p>
<p>I’m not even sure what use case qSclicerSceneWriter::writeToDirectory is<br>
meant to support. The related issue it closes doesn’t really explain [2].</p>
<p>Anyway if that code path doesn’t work right and none of us use it we should<br>
simplify things by retiring it.</p>
<p>[1]<br>
<a href="https://github.com/Slicer/Slicer/blame/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L284" class="onebox" target="_blank">https://github.com/Slicer/Slicer/blame/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L284</a></p>
<p>[2] <a href="http://na-mic.org/Bug/view.php?id=2097">http://na-mic.org/Bug/view.php?id=2097</a></p>

---

## Post #8 by @lassoan (2017-05-03 01:08 UTC)

<p>qSlicerSceneWriter::writeToDirectory is mostly redundant:</p>
<ul>
<li>If user saves the scene using the Save data dialog then saving as mrml or mrb should cover all use cases.</li>
<li>For single-click save operation for slicelets/custom applications we typically use applicationLogic.SaveSceneToSlicerDataBundleDirectory (it saves everything to a directory without creating a scene view and without zipping the results; <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/Guidelet/GuideletLib/Guidelet.py#L363-L381">see for example here</a>).</li>
</ul>
<p>As the method is not really needed, does not work correctly, and it would be difficult to make it robust and efficient (handle non-empty directory, overwriting files with the same name, etc), I think it would be a good idea to remove it (and the corresponding file format) from qSlicerSceneWriter.</p>

---

## Post #9 by @finetjul (2017-05-03 06:30 UTC)

<p>I’m fine if such option is removed. No problem.</p>

---
