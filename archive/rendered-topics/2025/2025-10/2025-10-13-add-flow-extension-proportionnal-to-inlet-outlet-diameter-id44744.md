---
topic_id: 44744
title: "Add Flow Extension Proportionnal To Inlet Outlet Diameter"
date: 2025-10-13
url: https://discourse.slicer.org/t/44744
---

# Add flow extension proportionnal to inlet/outlet diameter

**Topic ID**: 44744
**Date**: 2025-10-13
**URL**: https://discourse.slicer.org/t/add-flow-extension-proportionnal-to-inlet-outlet-diameter/44744

---

## Post #1 by @gred (2025-10-13 14:13 UTC)

<p>Dear all,</p>
<p>Is there an obvious way to add flow domain extensions using the Clip Vessel module proportional to the diameter of the inlet and outlet in question according to the centerline quantification table?</p>
<p>Best,</p>
<p>Gred</p>

---

## Post #2 by @gred (2025-10-14 13:33 UTC)

<p>My initial question was: how, from the branch clipper module, can I apply a domain extension with a different length for each inlet/outlet?</p>
<p>For example:<br>
Inlet 1 : L = 5x diameter<br>
Inlet 2 : L = 6x diameter<br>
Outlet 1: L = 3x diameter<br>
Outlet 2: L = 4x diameter<br>
…<br>
etc.</p>
<p>Since the branch clipper module applies the same extension length to all inlets and outlets, I solved the issue by using PypePad VMTK and looping the vmtkflowextensions script as many times as there were different lengths to apply.</p>
<p>I hope this helps others.</p>
<p>Best,</p>
<p>Gred</p>

---
