---
topic_id: 18002
title: "Switching View Layouts"
date: 2021-06-07
url: https://discourse.slicer.org/t/18002
---

# Switching view layouts

**Topic ID**: 18002
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/switching-view-layouts/18002

---

## Post #1 by @Vincebisca (2021-06-07 19:28 UTC)

<p>Hello !</p>
<p>This is probably a very stupid question, but I’ve been stuck for a while now and I don’t find how to get to do what I want: I would like, through a simple GUI, to be able to switch the Layout from my views, from a standard Four-Up to a Three over Three (standards in the layout selection on the toolbar). I am sure there’s a very simple way to activate these layouts through Python but I can’t find it…</p>
<p>Thanks in advance !</p>

---

## Post #2 by @pieper (2021-06-07 19:38 UTC)

<p>See the discussion <a href="https://discourse.slicer.org/t/slicer-4-11-slice-view-widget-interactions-intersections-issue-in-slicelet/7383">here</a> for some background.  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">This code</a> shows how to make a custom layout or you can use <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLLayoutNode.h#L78-L127">one of these pre-defined codes</a>.</p>

---

## Post #3 by @Vincebisca (2021-06-07 19:44 UTC)

<p>Thank you very much, exactly what I needed !</p>

---
