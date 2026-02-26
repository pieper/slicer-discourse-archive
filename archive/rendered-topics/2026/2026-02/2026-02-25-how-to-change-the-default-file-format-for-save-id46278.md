---
topic_id: 46278
title: "How To Change The Default File Format For Save"
date: 2026-02-25
url: https://discourse.slicer.org/t/46278
---

# How to change the default file format for save

**Topic ID**: 46278
**Date**: 2026-02-25
**URL**: https://discourse.slicer.org/t/how-to-change-the-default-file-format-for-save/46278

---

## Post #1 by @Victor_Wayne (2026-02-25 06:31 UTC)

<p>Hello,</p>
<p>When we click on the save button the default file format for saving a scene is .mrml. Is there any way I can change it to .mrb? Is there a way to edit the config file so that the save data dialog opens with .mrb file format to save?</p>
<p>I am willing to edit the qSlicerSaveDataDialog.cxx file and maintain it, if it is like one or two line edit. If that is the only case please tell me how to do it. Or should I subclass the save data dialog and make my own save widget? If so please instruct me on how to do it.</p>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @cpinter (2026-02-25 14:12 UTC)

<p>I was curious as well so did a brief chat with GitHub Copilot. Here is the relevant part of the results, maybe it helps:</p>
<p>… but <strong>not as a simple “default extension setting” in the Save dialog UI</strong>—to <em>force</em> a default (your option <strong>B</strong>) you typically need either:</p>
<ol>
<li>a <strong>small core change</strong> in Slicer (recommended if you control the build), or</li>
<li>a <strong>scripted override of the scene save dialog</strong> (works without rebuilding, but it replaces the standard dialog behavior).</li>
</ol>
<p>Below is what the current Slicer code is doing and where you’d change it.</p>
<hr>
<h2><a name="p-132277-h-1-mrml-vs-mrb-default-in-the-save-dialog-save-scene-and-unsaved-data-1" class="anchor" href="#p-132277-h-1-mrml-vs-mrb-default-in-the-save-dialog-save-scene-and-unsaved-data-1" aria-label="Heading link"></a>1) MRML vs MRB default in the Save dialog (“Save scene and unsaved data”)</h2>
<p>That dialog is implemented here:</p>
<pre data-code-name="Base/QTGUI/qSlicerSaveDataDialog.cxx" data-code-wrap="cpp"><code class="lang-cpp">void qSlicerSaveDataDialogPrivate::saveSceneAsDataBundle()
{
  int sceneRow = this-&gt;findSceneRow();
  QComboBox* box = qobject_cast&lt;QComboBox*&gt;(this-&gt;FileWidget-&gt;cellWidget(sceneRow, FileFormatColumn));
  int mrbIndex = box-&gt;findText("mrb", Qt::MatchContains);
  int mrmlIndex = box-&gt;findText("mrml", Qt::MatchContains);
  // Toggle between scene data bundle entry and mrml entry
  if (mrbIndex != -1)
  {
    if (box-&gt;currentIndex() != mrbIndex)
    {
      box-&gt;setCurrentIndex(mrbIndex);
    }
    else
    {
      if (mrmlIndex != -1)
      {
        box-&gt;setCurrentIndex(mrmlIndex);
      }
    }
  }
}
</code></pre>
<p>Key point: <strong>MRB is currently a “toggle button” behavior</strong>, not a persisted “default”. So “force MRB always” is not exposed as a preference; you’d need to change logic so that on dialog initialization/population it <em>sets</em> the scene’s file format combobox to MRB and (optionally) disables toggling back.</p>
<h3><a name="p-132277-what-to-change-core-approach-2" class="anchor" href="#p-132277-what-to-change-core-approach-2" aria-label="Heading link"></a>What to change (core approach)</h3>
<p>You’d look for where the scene row is populated (e.g., <code>populateScene()</code> / <code>populateItems()</code> in the same file) and make it do something like:</p>
<ul>
<li>find the scene row combobox</li>
<li>set it to the <code>mrb</code> entry unconditionally</li>
<li>optionally call the logic that hides other rows when MRB is selected (since MRB implies bundling; Slicer already has code that hides non-scene rows when saving as MRB)</li>
</ul>
<p>There is already code that hides other rows when saving as MRB:</p>
<pre data-code-name="Base/QTGUI/qSlicerSaveDataDialog.cxx" data-code-wrap="cpp"><code class="lang-cpp">// When scene is saved as .mrb then item selection state,
// file format, and options may be ignored. To indicate
// this clearly to the users, we only show the scene in the table
// and hide all the other storable nodes.
</code></pre>
<p>So the feature is conceptually supported; it’s just not “force MRB by default”.</p>
<h3><a name="p-132277-alternative-no-rebuild-override-the-scene-save-dialog-3" class="anchor" href="#p-132277-alternative-no-rebuild-override-the-scene-save-dialog-3" aria-label="Heading link"></a>Alternative (no rebuild): override the scene save dialog</h3>
<p>Slicer supports overriding the default scene save dialog from a scripted module. This is documented here:</p>
<pre data-code-name="Docs/developer_guide/script_repository/gui.md" data-code-wrap="markdown"><code class="lang-markdown">### Override default scene save dialog

Place this class in the scripted module file to override

```python
class MyModuleFileDialog ():
  ...
  def execDialog(self):
    # Implement custom scene save operation here.
    ...
```
</code></pre>
<p>With that approach you could implement “Save always writes an .mrb” (for example by calling <code>slicer.util.saveScene("something.mrb")</code>)—but it replaces the normal dialog, so it’s a heavier UX change.</p>

---
