# Output directory button widget and drop-down list widget for an extension

**Topic ID**: 8144
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/output-directory-button-widget-and-drop-down-list-widget-for-an-extension/8144

---

## Post #1 by @AurelienCD (2019-08-23 07:37 UTC)

<p>Hi everyone,</p>
<p>I am working on an 3dslicer extension.</p>
<p>The aim of this extension is to automatically analyse dosimetric films for quality control in a radiotherapy center.</p>
<p>The code in python is ok and the extension works well.</p>
<p>To finish the extension i would just need two things to add in the Widget’s class:</p>
<ol>
<li>add an output directory button where the result of the analyse would be put</li>
<li>add a drop-down list where the user could choose the radiotherapy machine used for the quality control.</li>
</ol>
<p>and of course put these two informations in two variables.</p>
<p>I tried to find in internet the code for these buttons but I didn’t find something easy for a beginner like me.</p>
<p>Anyone could help me for this ?</p>
<p>Many thanks,<img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>
<p>All the best,</p>
<p>AurelienCD</p>
<p>I am using Slicer 4.10.2</p>

---

## Post #2 by @lassoan (2019-08-23 16:53 UTC)

<p>You can use <code>ctk.ctkPathLineEdit()</code> for directory selection and a regular <code>qt.QComboBox()</code> for choosing a name from a list. I would recommend to complete this Slicer programming tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #3 by @AurelienCD (2019-08-26 08:05 UTC)

<p>Thank you very much for your help, that is what I needed. I will look at the tutorial more deeply.</p>

---

## Post #4 by @Saima (2020-03-10 03:40 UTC)

<p>Hi Andras,<br>
Any information regarding how to use qt designer. where can i find information for developing slicer modules. I currently don’t know how to make combo box for uploading files. I know how to use the design for qmrml modules but I don’t understand how to use the simple modules like uploading file or using a text box to get a number input etc. could you please help.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #5 by @lassoan (2020-03-10 03:56 UTC)

<aside class="quote no-group" data-username="Saima" data-post="4" data-topic="8144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Any information regarding how to use qt designer. where can i find information for developing slicer modules.</p>
</blockquote>
</aside>
<p>Qt designer manual is available <a href="https://doc.qt.io/qt-5/qtdesigner-manual.html">here</a>.</p>
<p>In addition to standard Qt widgets, you can use CTK widgets (see <a href="http://www.commontk.org/index.php/Documentation/ImageGallery">gallery</a>, with links to API documentation) and special widgets added in Slicer core and modules (see <a href="https://apidocs.slicer.org/master/classes.html">Slicer API documentation</a>).</p>

---
