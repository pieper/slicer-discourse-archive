# Create a paint brush

**Topic ID**: 27652
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/create-a-paint-brush/27652

---

## Post #1 by @devD (2023-02-06 10:11 UTC)

<p>Hi,</p>
<p>I am making an extension. I want to add one button to it which creates a paint brush with optional diameter (such as the one that exists in Segment Editor), the only thing it should return is the area in pixels in which the user has right clicked with the brush. How should this be done?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2023-02-08 20:55 UTC)

<p>One option is to add a segment editor widget to your module and activate the paint effect. You don’t need to show the widget, just create the object and use it. You can set up masking options (paint inside certain regions or intensity range) and then you can get area of the painted region using Segment Statistics module.</p>
<p>Alternatively, you can just use a markup and model to specify a circular region (something like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this</a>) and then compute what you need from the click position and the input image/segmentation using numpy.</p>

---
