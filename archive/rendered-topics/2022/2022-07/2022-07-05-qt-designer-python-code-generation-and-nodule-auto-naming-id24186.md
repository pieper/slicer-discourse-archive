# QT designer python code generation, and nodule auto-naming

**Topic ID**: 24186
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/qt-designer-python-code-generation-and-nodule-auto-naming/24186

---

## Post #1 by @Kevin.Kn (2022-07-05 16:14 UTC)

<p>I have been messing around with creating my own extensions, and was wondering if it was possible at all for code to be generated from the Qt Designer in a python environment.</p>
<p>I see this <a href="https://discourse.slicer.org/t/qt-designer-doesnt-work-for-python-code-preview/14342">previous post</a> and that the designer without the generator reduces module size by a significant amount.</p>
<p>My use case is that I have 2 widgets for placing markups included in my extension, and would like for the nodes for each of the individual widgets to be named either ‘nodule’ or ‘background’ so that I can read these values into other code I have written. The only way I can think to do that is by getting access to the node</p>
<p>As of right now, I have added these widgets to the UI, connected their signals to the MRMLscene, but this leaves me with needing to create, and then rename the respective nodes for nodule/background points of interest.</p>
<p>Thank you for any help or suggestions!</p>
<p>just for reference,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b41fff31f674f77281c748a74f8dacf4561ba849.png" alt="image" data-base62-sha1="pHsuQSTUbMxe1jmPizk1RNl1mBj" width="405" height="353"></p>
<p>BG and nod were test markups I manually created/named after updating the UI to make sure they were linked properly to the MRMLscene update.</p>

---

## Post #2 by @Sam_Horvath (2022-07-05 17:11 UTC)

<p>For the node naming, the qMRMLNodeComboBox has the attribute ‘baseName’ that controls the default name that the node is created with.</p>

---

## Post #3 by @Kevin.Kn (2022-07-05 20:54 UTC)

<p>Thank you, I will take a look at it when I’m back in office tomorrow. Being able to nodes that will help greatly from a user standpoint.</p>
<p>I did end up finding a method to generate a python script file from the QT .ui file through some youtube tutorials, and I can post the link/steps to that here. The end result isn’t as pretty as the Extension Wizard example that you start off with, but its workable.</p>

---

## Post #4 by @lassoan (2022-07-06 00:48 UTC)

<aside class="quote no-group" data-username="Kevin.Kn" data-post="3" data-topic="24186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kevin.Kn:</div>
<blockquote>
<p>I did end up finding a method to generate a python script file from the QT .ui file through some youtube tutorials,</p>
</blockquote>
</aside>
<p>Python code generation from .ui file is unnecessary. I don’t know what problems PySide is trying to solve with this clunky code generation stuff, but for all the use cases that I’ve encountered so far, code generation is simply not needed.</p>
<p>Slicer uses PythonQt for Python wrapping, which has many advantages compared to PySide (the Python wrapping that the Qt Company provides), but there are slight differences. PythonQt is not widely known, so most examples that you find on the web are for PySide and not directly applicable to PythonQt.</p>

---

## Post #5 by @Kevin.Kn (2022-07-06 15:59 UTC)

<p>I am currently looking at the basename attribute for qMRMLNodeComboBox, but have no option to edit it. Are there any special options that I need to include so that it is editable?</p>
<p>Right now if I type in any string for the baseName and hit enter, it just disappears/doesnt apply.</p>

---

## Post #6 by @lassoan (2022-07-06 18:27 UTC)

<aside class="quote no-group" data-username="Kevin.Kn" data-post="5" data-topic="24186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kevin.Kn:</div>
<blockquote>
<p>Right now if I type in any string for the baseName and hit enter, it just disappears/doesnt apply.</p>
</blockquote>
</aside>
<p>That’s fine, what you see is just a small Qt designer bug that if you edit properties of a widget that is currently not visible (for example, it is in a collapsed widget) then the focus is moved away from the property editor on any modification.</p>
<p>You can either open the collapsible button or groupbox or tab widget while you are editing widgets in it; or copy-paste text into the property editor instead of typing.</p>

---

## Post #7 by @Kevin.Kn (2022-07-06 19:09 UTC)

<blockquote>
<p>You can either open the collapsible button or groupbox or tab widget while you are editing widgets in it; or copy-paste text into the property editor instead of typing.</p>
</blockquote>
<p>Thank you,</p>
<p>I just got it to work. I just needed to link the scene to a combo button, and then I found the ‘drop down button view’ QT setting to allow me to edit the basename. I additionally had to add ‘vtkMRMLMarkupsFiducialNode’ to the combobox nodetypes, so the point list is created correctly.</p>
<p>Unfortunately, the node selection incorporated in the markups widgets dont have editable baseNames, but I am able to use two combo boxes to create nodes with the foreground/background seed names now, and then the user is able to select those in the markup placement widget.</p>
<p>This is my first time doing UI/QT development so it’s taken me a bit to understand what’s going on.</p>
<p>Thank you!</p>

---

## Post #8 by @lassoan (2022-07-07 03:02 UTC)

<aside class="quote no-group" data-username="Kevin.Kn" data-post="7" data-topic="24186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/59ef9b/48.png" class="avatar"> Kevin.Kn:</div>
<blockquote>
<p>Unfortunately, the node selection incorporated in the markups widgets dont have editable baseNames,</p>
</blockquote>
</aside>
<p>Indeed, not everything is exposed as property that can be edited in Qt Designer, so for some things you need to add a line in the <code>setup</code> method of the module widget - for example <code>self.ui.someMarkupsWidget.setNodeBaseName('something')</code></p>

---
