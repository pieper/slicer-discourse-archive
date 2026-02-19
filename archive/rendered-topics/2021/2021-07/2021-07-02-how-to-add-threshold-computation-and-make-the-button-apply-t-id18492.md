---
topic_id: 18492
title: "How To Add Threshold Computation And Make The Button Apply T"
date: 2021-07-02
url: https://discourse.slicer.org/t/18492
---

# How to add threshold computation and make the button apply to work

**Topic ID**: 18492
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/how-to-add-threshold-computation-and-make-the-button-apply-to-work/18492

---

## Post #1 by @rafael.cristo (2021-07-02 19:46 UTC)

<p>Hi, everyone.</p>
<p>I am trying to implement a python code to create a module in 3d slicer, howevery I don’t know how to activate the button apply. Basically I have an input volume that will be 1 or 0 comparing with a threshold value, however I don’t know how to make the button apply works.</p>
<h1><a name="p-62543-h-1" class="anchor" href="#p-62543-h-1" aria-label="Heading link"></a></h1>
<pre><code>    # Apply Button
    #
    self.apply_button = qt.QPushButton("Apply")
    self.apply_button.toolTip = "Run the algorithm."
    self.apply_button.enabled = False
    parameters_form_layout.addRow(self.apply_button)
</code></pre>
<p>It is considered a widget. How can I make it works!?</p>
<p>Best,<br>
Rafael Cristo</p>

---

## Post #2 by @pieper (2021-07-07 16:46 UTC)

<p>Hi -</p>
<p>You need to connect the button to a callback slot.  You can read through the developer tutorials for all the details.</p>

---
