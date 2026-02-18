# Ipywidgets and SlicerJupyter

**Topic ID**: 11913
**Date**: 2020-06-07
**URL**: https://discourse.slicer.org/t/ipywidgets-and-slicerjupyter/11913

---

## Post #1 by @Vinny (2020-06-07 13:58 UTC)

<p>Hi,</p>
<p>I downloaded the tutorial sets for SlicerJupyter and noticed that the interactive widgets were not showing up.  I had to enable them using:</p>
<p>jupyter nbextension enable --py widgetsnbextension</p>
<p>I want to make sure that I did not miss something in the installation instructions using Option 2 (note that I did not run the additional commands for Jupyter lab): <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" rel="nofollow noopener">https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup</a></p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2020-06-07 14:44 UTC)

<p>Thanks for reporting this. Some places I saw instructions for enabling notebook extensions, but I also saw comments about these steps not being necessary. I’ve found that things worked for me without them, but probably it’s safer to execute them, even if they are not always necessary. I’ve updated the instructions, please send a pull request if you think further changes are needed. Thank you.</p>

---

## Post #3 by @just_zzzzzz (2023-08-03 03:36 UTC)

<p>I’m encountering the same problem. This happens when run the “01_Data_loading_and_display.ipynb” - " Dynamic views". I’m using windows and slicer 5.2.2. I did “jupyter nbextension enable --py widgetsnbextension” in my anaconda base env and didn’t solve the problem. Where shall I do “jupyter nbextension enable --py widgetsnbextension”? I need more help on making the interactive widgets work. Thanks!</p>

---
