---
topic_id: 35362
title: "How To Add A Clickable Button On The Main Window"
date: 2024-04-08
url: https://discourse.slicer.org/t/35362
---

# How to add a clickable button on the main window

**Topic ID**: 35362
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/how-to-add-a-clickable-button-on-the-main-window/35362

---

## Post #1 by @nicola-dallosto (2024-04-08 18:01 UTC)

<p>I uploaded a python script in the .slicerrc.py file in order to open the Segment Editor when 3D Slicer starts up. Then the image to annotate is opened. I want to insert a button that the user has to click once he has finished with the annotation and when the button is clicked the segmentation is exported and another image is opened.<br>
Is there a simple way to implement this idea in python?</p>

---

## Post #2 by @cpinter (2024-04-09 12:43 UTC)

<p>Probably the best would be to create a new module, which contains segment editor as well as the rest of the GUI you need. Segment Editor is a completely reusable widget (and the module only contains that one widget), so you can add it easily to the module using Qt Designer (just as the rest of the buttons etc.).</p>
<p>You can also move the slicerrc code into the module, in the <code>enter</code> function for example (which is executed when the user switches to the module, which you can trigger from slicerrc, but in this case it would just have that one line).</p>
<p>You can find information about creating a new extension here (it is easiest to package a new module into an extension):<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html</a></p>
<p>I strongly suggest doing this tutorial if you haven’t created a Slicer module yet:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">
  <header class="source">

      <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx</a></h4>


  This file is binary. <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
