# How to add another module (Reformat) into a module that I have created?

**Topic ID**: 38077
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/how-to-add-another-module-reformat-into-a-module-that-i-have-created/38077

---

## Post #1 by @Saladi (2024-08-28 12:26 UTC)

<p>Hi community,<br>
I am trying to develop a new module from my research work, in that “Reformat” module is essential. I want to have some features (offset, rotation, etc) into my existing module. I am developing in Python but “Reformat” is in C/C++. Is there any way I can access some features from “Reformat” without coding the entire function?</p>

---

## Post #2 by @Llujoo (2024-09-05 09:26 UTC)

<p>So you want to run c++ code in python, right?<br>
I haven’t used it myself but I’ve heard <strong>pybind11</strong> is pretty useful.</p>

---

## Post #3 by @Saladi (2024-09-07 11:32 UTC)

<p>Oh cool! I’ll check it out once.<br>
Thanks</p>

---

## Post #4 by @cpinter (2024-09-07 19:30 UTC)

<p>I don’t recommend using libraries and mechanisms that are not already part of Slicer. You’ll need to change basic Slicer cmake and other files, and will end up with something that is very hard to maintain, or you will spend a year or more making it part of Slicer.</p>
<p>The best way would be to create a reusable widget from the part of the module that you want to use from Python and add that widget like any other. There are many examples, e.g. <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Segmentations/Widgets/Resources/UI">here</a>.</p>

---
