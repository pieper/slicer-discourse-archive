# Change setting to "harden regularization transform"

**Topic ID**: 33241
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/change-setting-to-harden-regularization-transform/33241

---

## Post #1 by @Gaelle_Leroux (2023-12-05 21:13 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a> !</p>
<p>I’m developing a module to automatically apply the matrix to volume files. In the new version of Slicer we can change the “Acquisition geometry regularization” to “harden regularization transform”. Is there a way to change this parameter from my python code before saving my files with slicer.utils.saveNode  ?</p>
<p>Thank you very much !</p>

---

## Post #2 by @jcfr (2023-12-05 21:34 UTC)

<p>To harden transforms while saving, simply consider calling <del><code>slicer.util.saveNode</code></del> <code>slicer.util.exportNode</code> passing <code>world=True</code>.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file</a></p>

---

## Post #3 by @Gaelle_Leroux (2023-12-06 15:24 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, I tried to use what you suggested but I ran into a problem.<br>
My line to save my file look like this : <code>slicer.util.saveNode(my_model,"output/path/to/my/file.nii.gz",world=True)</code>. When I’m trying to run it in slicer 5.6.0 I have this error :<code>saveNode() got an unexpected keyword argument 'world'</code></p>
<p>Can you help me ?</p>

---

## Post #4 by @lassoan (2023-12-06 18:07 UTC)

<p><code>saveNode</code> function does not have a <code>world</code> argument. This function always saves the node as is, without hardening its parent transform on it.</p>
<p>You can use the <code>exportNode</code> function, which has an optional <code>world</code> argument - as shown in the example that <a class="mention" href="/u/jcfr">@jcfr</a> linked above.</p>

---

## Post #5 by @Gaelle_Leroux (2023-12-07 14:17 UTC)

<p>I get it, it’s working. Thank you !</p>

---
