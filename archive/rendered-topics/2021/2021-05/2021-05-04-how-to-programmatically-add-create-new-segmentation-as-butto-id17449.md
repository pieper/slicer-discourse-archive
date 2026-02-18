# How to programmatically add create new segmentation as button?

**Topic ID**: 17449
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/how-to-programmatically-add-create-new-segmentation-as-button/17449

---

## Post #1 by @akshay_pillai (2021-05-04 16:41 UTC)

<p>I know that in segment editor the user has the ability to create a new segmentation and name the new segment using  "create new segment as … ". Is there any way I can perform that programmatically? I just want to give the user the option to input the new name of the segmentation after they click a button used for adding or subtracting segments in that subtraction. I use .setname to change the name but what would I use to give the user the option to set the name?</p>

---

## Post #2 by @lassoan (2021-05-21 18:35 UTC)

<p>You can enable <code>renameEnabled</code> flag for your MRML node selector widget to offer the user to create a new node with a specified name. You can set the default name in <code>baseName</code> property of the node selector.</p>

---
