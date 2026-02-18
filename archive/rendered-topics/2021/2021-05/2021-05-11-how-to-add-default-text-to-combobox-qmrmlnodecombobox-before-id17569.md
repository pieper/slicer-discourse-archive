# How to add default text to combobox(qMRMLNodeComboBox) before opening any customize model.

**Topic ID**: 17569
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/how-to-add-default-text-to-combobox-qmrmlnodecombobox-before-opening-any-customize-model/17569

---

## Post #1 by @Mahesh_Timmanagoudar (2021-05-11 13:34 UTC)

<p>we have customised model. The GUI is written in XML code. Depending on XML tag qSlicerCLIModuleWidgetPrivate class function is called and dynamically combo box is created. We wanted to add some default text to combo box object. qMRMLNodeComboBox class has setBaseName function. We are able to call the function. But unable to add existing labels as default text.  We wanted to add default text label as “Create new Model”. Please refer attached image.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00aecc3210e337020d9d4759d35b6b5c2355a53d.png" alt="DefaultText" data-base62-sha1="62v8vIANoYWf05NtrDDwNRs7X7" width="658" height="130"></p>

---

## Post #2 by @cpinter (2021-05-11 15:41 UTC)

<p>qMRMLNodeComboBox has a regular QComboBox, which does not support default text. This feature is only implemented in <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkComboBox.h#L47">ctkComboBox</a>.</p>

---

## Post #3 by @Mahesh_Timmanagoudar (2021-05-12 12:13 UTC)

<p>Is it possible to use <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkComboBox.h#L47" rel="noopener nofollow ugc">ctkComboBox</a>  in qMRMLNodeComboBox  class?</p>

---

## Post #4 by @jamesobutler (2021-05-12 12:24 UTC)

<p>If you use default text of “Create new Model”, won’t that be confusing because it will be separate from the selection in the qMRMLNodeComboBox that is called “Create new Model”?</p>
<p>Can you describe more of your use case? Are you actually just trying to default select the action so that it will create a new model whenever you use your module?</p>

---
