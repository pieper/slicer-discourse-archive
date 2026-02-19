---
topic_id: 40649
title: "Cannot Decrease The Width Of My Module"
date: 2024-12-12
url: https://discourse.slicer.org/t/40649
---

# Cannot decrease the width of my module

**Topic ID**: 40649
**Date**: 2024-12-12
**URL**: https://discourse.slicer.org/t/cannot-decrease-the-width-of-my-module/40649

---

## Post #1 by @koeglfryderyk (2024-12-12 12:46 UTC)

<p>I created a default extension with a module (it contains an input selector)</p>
<p>After I reload it, when I select a volume, I can only reduce the width of the module so that the full name of the volume is still visible.</p>
<p>Is it possible to reduce the size further?</p>
<p>Ideally, I would want a solution where when I decrease the width further, only some of the first and last letters of the name would be displayed with ellipses in the middle - like e.g. in the Volumes module</p>

---

## Post #2 by @cpinter (2024-12-12 15:38 UTC)

<p>I don’t have a clear answer for you. Just looked at the properties of the <code>qMRMLNodeComboBox</code> and there is no obvious property for this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf19eeebae735f2a0ca49c60bf530632a7d77462.png" data-download-href="/uploads/short-url/rgyL2hTfCyxBWKQjFViqZ2SmIkG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf19eeebae735f2a0ca49c60bf530632a7d77462.png" alt="image" data-base62-sha1="rgyL2hTfCyxBWKQjFViqZ2SmIkG" width="456" height="268"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">456×268 5.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are you using the same combobox type? If you look at the combobox in the Volumes module, is it set up differently in any way than yours?</p>

---

## Post #3 by @koeglfryderyk (2024-12-16 10:06 UTC)

<p>I’m using the same combobox. It seems to be setup pretty similarly. also when I make the exact same setup it still doesn’t fix the issue.</p>
<p>this is from the volumes UI</p>
<pre><code class="lang-auto">     &lt;item&gt;
      &lt;widget class="qMRMLNodeComboBox" name="ActiveVolumeNodeSelector"&gt;
       &lt;property name="nodeTypes"&gt;
        &lt;stringlist notr="true"&gt;
         &lt;string&gt;vtkMRMLVolumeNode&lt;/string&gt;
        &lt;/stringlist&gt;
       &lt;/property&gt;
       &lt;property name="addEnabled"&gt;
        &lt;bool&gt;false&lt;/bool&gt;
       &lt;/property&gt;
       &lt;property name="renameEnabled"&gt;
        &lt;bool&gt;true&lt;/bool&gt;
       &lt;/property&gt;
      &lt;/widget&gt;
     &lt;/item&gt;
</code></pre>
<p>and this is from the UI of a default module</p>
<pre><code class="lang-auto">    &lt;item row="0" column="1"&gt;
    &lt;widget class="qMRMLNodeComboBox" name="inputSelector"&gt;
    &lt;property name="toolTip"&gt;
        &lt;string&gt;Pick the input to the algorithm.&lt;/string&gt;
    &lt;/property&gt;
    &lt;property name="nodeTypes"&gt;
        &lt;stringlist notr="true"&gt;
        &lt;string&gt;vtkMRMLScalarVolumeNode&lt;/string&gt;
        &lt;/stringlist&gt;
    &lt;/property&gt;
    &lt;property name="showChildNodeTypes"&gt;
        &lt;bool&gt;false&lt;/bool&gt;
    &lt;/property&gt;
    &lt;property name="addEnabled"&gt;
        &lt;bool&gt;false&lt;/bool&gt;
    &lt;/property&gt;
    &lt;property name="removeEnabled"&gt;
        &lt;bool&gt;false&lt;/bool&gt;
    &lt;/property&gt;
    &lt;property name="SlicerParameterName" stdset="0"&gt;
        &lt;string&gt;inputVolume&lt;/string&gt;
    &lt;/property&gt;
    &lt;/widget&gt;
    &lt;/item&gt;
</code></pre>
<p>weridly, the first time I open the new module my desired behaviour works (the name of the volume shorteneing and expanding with the width of the volume), but after I click on Reload it assumes the expanded width and it cannot be reduced</p>

---

## Post #4 by @cpinter (2024-12-16 12:31 UTC)

<p>So this problem only occurs after using the Reload function?</p>
<p>In that case I wouldn’t even spend any time with this, because the users for whom you make the module will not use Reload at all.</p>

---

## Post #5 by @koeglfryderyk (2024-12-16 12:43 UTC)

<p>it occurs in two cases:</p>
<ol>
<li>when I reload</li>
<li>I have a button that will be used to change the appearance of the UI . it executes the following code - after this code is executed the problem occurs</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">    slicer.app.setStyleSheet("""
                QWidget {
                    background-color: #060f21;
                    color: white;
                }
                QMainWindow {
                    background-color: #060f21;
                }
                qSlicerLayoutManager {
                    background-color: #060f21;
                }
                """)
</code></pre>

---

## Post #6 by @cpinter (2024-12-16 12:48 UTC)

<p>I would not expect that setting a style sheet causes changes like this, so this is a bug. Unfortunately the layout logic in Qt is extremely complicated, so I see a very low chance of this being resolved unless you find a solution. However, if someone has an idea please chime in.</p>
<p>In the meantime I’d set the style sheet before first entering the module, which I imagine would solve the problem.</p>

---
