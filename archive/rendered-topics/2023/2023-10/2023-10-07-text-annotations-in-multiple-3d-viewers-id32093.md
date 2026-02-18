# Text annotations in multiple 3D viewers

**Topic ID**: 32093
**Date**: 2023-10-07
**URL**: https://discourse.slicer.org/t/text-annotations-in-multiple-3d-viewers/32093

---

## Post #1 by @S_Motch_Perrine (2023-10-07 22:20 UTC)

<p>Overview of the issue: I want text data associated with scans to show as annotations in the 3D viewer or viewers in which the specific scan is being visualized. The ultimate goal is to be able to have multiple lines of text annotations to show (example: Line 1 - Disease Model; Line 2 - Mouse123; Line 3 - Age; Line 4 - Genotype) in only the specific 3D viewer(s) in which a visualization for a specific scan volume (or model) is being shown so that these labels are showing when creating animations, etc. I was testing this with the corner annotation script and realized that I could only add a line of corner annotation to the most recently opened 3D viewer.</p>
<p>Initial testing of the script:<br>
view=slicer.app.layoutManager().threeDWidget(0).threeDView()# Set text to “Something"view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,“Test text.”)# Set color to redview.cornerAnnotation().GetTextProperty().SetColor(1,0,0)# Update the viewview.forceRender()</p>
<p><span class="hashtag-raw">#At</span> some point I changed the color and can’t remember the specifics on that, but 3D Viewer 1 still shows this text. I then used the 3 3D viewers to compare some .nrrd files and did the text again… and it ended up in the lower right (assuming 3rd and most recently opened?) 3D viewer.</p>
<p>view=slicer.app.layoutManager().threeDWidget(0).threeDView()# Set text to "Something"view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,“color?”)# Set color to redview.cornerAnnotation().GetTextProperty().SetColor(29/255,243/255,22/255)# Update the viewview.forceRender()</p>
<p><span class="hashtag-raw">#For</span> whatever reason, I can only update/delete the text from viewer 3.<br>
This is what I see: <img src="https://raw.githubusercontent.com/SPerrine/DEMO/main/images/Slide2.PNG" alt="Image2" width="690" height="388"><br>
<img src="https://raw.githubusercontent.com/SPerrine/DEMO/main/images/Slide3.PNG" alt="Image2" width="690" height="388"><br>
<img src="https://raw.githubusercontent.com/SPerrine/DEMO/main/images/Slide4.PNG" alt="Image2" width="690" height="388"><br>
<span class="hashtag-raw">#I</span> can update the text for viewer 3, or delete it for viewer 3 by deleting the text within the SetText command but am unable to delete the text in viewer 1, even if I close the scene.</p>
<p>view=slicer.app.layoutManager().threeDWidget(0).threeDView()# Set text to "Something"view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,“Why is viewer 3 updating? How do I indicate a specific viewer?”)# Set color to redview.cornerAnnotation().GetTextProperty().SetColor(29/255,243/255,22/255)# Update the viewview.forceRender()<br>
<img src="https://raw.githubusercontent.com/SPerrine/DEMO/main/images/Slide6.PNG" alt="Image2" width="690" height="388"><br>
<img src="https://raw.githubusercontent.com/SPerrine/DEMO/main/images/Slide7.PNG" alt="Image2" width="690" height="388"><br>
Ultimate goal is to be able to read information from a .csv file and have annotations for specific nodes show up when they are being viewed in the 3D viewers to help identify specimens, age, genotype, etc.</p>
<p>From Andras on thread: <a href="https://discourse.slicer.org/t/corner-annotations-multiple-texts/18434">https://discourse.slicer.org/t/corner-annotations-multiple-texts/18434</a></p>
<p>Someone wanted to have a simple animation fading from text 1 to text 2.</p>
<p>You can fade out the old text and then fade in the new text (using view.cornerAnnotation().GetTextProperty().SetOpacity(…)).<br>
So: 1) How do I set text in a specific 3D viewer?<br>
2) How do I get that text to pull from a csv?</p>
<p>Thank you!</p>

---

## Post #2 by @mikebind (2023-10-08 00:29 UTC)

<p>Try something like:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
for idx in range(lm.threeDViewCount):
  view = lm.threeDWidget(idx).threeDView()
  view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight, f"I am widget number {idx}")
</code></pre>
<p>This should put an annotation on each 3D view saying what index it is. Perhaps the 3D widgets are kept in the list of threeDWidgets in reverse order of creation, so when you keep asking for the first one (index zero), you keep getting whatever the newest one is.</p>

---
