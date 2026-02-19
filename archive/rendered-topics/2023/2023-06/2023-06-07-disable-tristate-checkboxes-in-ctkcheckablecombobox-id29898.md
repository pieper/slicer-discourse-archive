---
topic_id: 29898
title: "Disable Tristate Checkboxes In Ctkcheckablecombobox"
date: 2023-06-07
url: https://discourse.slicer.org/t/29898
---

# Disable tristate checkboxes in ctkCheckableComboBox

**Topic ID**: 29898
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/disable-tristate-checkboxes-in-ctkcheckablecombobox/29898

---

## Post #1 by @abertelsen (2023-06-07 13:26 UTC)

<p>Hello everybody!</p>
<p>A quick question: is there a way to disable the tristate behaviour in ctkCheckableComboBox? For my application, the usual checked or unchecked states are more appropriate.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8e76dddedeeffb8fb6352f6fe9d34c2a3bded11.png" alt="image" data-base62-sha1="zvUfkUGmQBiSgobLXqaXZwK01e9" width="448" height="326"></p>
<p>I forgot to mention that I am using Python, for a scripted module (in Slicer 5.2.2).</p>
<p>Any help is welcome!</p>
<p>Thanks,<br>
Álvaro</p>

---

## Post #2 by @jamesobutler (2023-06-07 14:19 UTC)

<p>Below code shows that the ctkCheckableComboBox by default does not have tristate when using from the GUI.</p>
<pre><code class="lang-python">checkable_combobox = ctk.ctkCheckableComboBox()
checkable_combobox.addItems(["L1", "L2", "L3"])
checkable_combobox.show()
# Manually check the "L3" checkbox and observe that there are only 2 states (Checked/Unchecked support)
</code></pre>
<p>However below is where I think you are likely misusing the API and making the checkboxes go into the PartiallyChecked state.</p>
<pre><code class="lang-python">checked_items = checkable_combobox.checkedIndexes()
single_checked_item = checked_items[0]
# https://doc.qt.io/qt-5/qcheckbox.html#setCheckState
# https://doc.qt.io/qt-5/qt.html#CheckState-enum (0 for Unchecked, 1 for PartiallyChecked, 2 for Checked)
# Note that Check State takes in a CheckState and not a boolean
# Different from a QCheckBox which has SetChecked which does take a boolean
checkable_combobox.setCheckState(single_checked_item, True) # This is not setting to the "Checked" state, but rather the "PartiallyChecked" state because True == 1
</code></pre>

---
