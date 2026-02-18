# How to create a drop down list with multiple options

**Topic ID**: 17357
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/how-to-create-a-drop-down-list-with-multiple-options/17357

---

## Post #1 by @akshay_pillai (2021-04-27 15:29 UTC)

<p>How do I create a drop-down list with multiple options and each option onclick performs a different function? I am trying to do this in python for a module.</p>

---

## Post #2 by @cpinter (2021-04-28 11:09 UTC)

<p>This is hardly a Slicer question, but my suggestion would be to use a QMenu and populate it with QActions. If you search in the Slicer source code you will find plenty of examples.</p>

---

## Post #3 by @akshay_pillai (2021-04-30 14:05 UTC)

<p>Sorry. I understand the irrelevance.</p>
<p>I have been trying to create this drop-down list to add a certain functionality to my module, specifically just have 2 to 3 options to perform addition or subtraction of segments. I have created the drop-down list using qt and created a UI for a combo box. But I don’t understand how to add a onclick function to the options in the drop-down list. If anyone has implemented anything similar please let me know. Thank you.</p>

---

## Post #4 by @jamesobutler (2021-04-30 14:09 UTC)

<p>I would suggest to review the QComboBox documentation as it relates to Signals. <a href="https://doc.qt.io/qt-5/qcombobox.html#signals" class="inline-onebox" rel="noopener nofollow ugc">QComboBox Class | Qt Widgets 5.15.3</a></p>
<p>The <code>currentIndexChanged</code> or even the <code>activated</code> signal would allow you to link to a selection changed or selected event respectively.</p>

---

## Post #5 by @cpinter (2021-04-30 15:07 UTC)

<p>Although it is possible to use a combobox like this, let me give my 2 cents in that using a combobox to directly run functions is not a good design choice. Such widgets are used to make selections, so it would be legit if you had an Apply button below the combobox that gets the current selection and runs the proper function. Or as an alternative you can use a menu, or a series of buttons or tool buttons.</p>

---
