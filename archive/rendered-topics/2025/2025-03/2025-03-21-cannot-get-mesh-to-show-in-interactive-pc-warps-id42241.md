# Cannot get mesh to show in interactive PC warps

**Topic ID**: 42241
**Date**: 2025-03-21
**URL**: https://discourse.slicer.org/t/cannot-get-mesh-to-show-in-interactive-pc-warps/42241

---

## Post #1 by @christyhipsley (2025-03-21 02:34 UTC)

<p>Hi all,<br>
I’m fairly new to Slicer so forgive me if I’m missing something obvious. I loaded a previous GPA/PCA from geomorph into SlicerMorph, and everything looks fine. I can view the PC scatter plots, lollipop plots, and make an interactive visualisation shape change along the PC axes using the generated PC warped Landmarks. But when I specify a reference model and LM set for that model under Setup Interactive Visualization - 3D model visualization, and press Apply, it only loads the landmarks into both 3D windows, and they cannot be warped. In other words, it is not creating the PCA Warped Volume that links the PC warped landmarks to this model and landmark set. Am i missing a step? When I follow the GPA tutorial with the Mouse Skull Landmarks  and load the Mouse Skull Reference Model dataset from the Sample Data, everything works fine. The only differences I can see is that my mesh is a binary ply file and my landmark data is fcsv in CoordinateSystem = LPS, while the sample data 3D model is a vtk file and their landmark data is fcsv in CoordinateSystem = RAS. Otherwise I have not changed the order or number of landmarks, which were themselves created in Slicer using ALPACA.</p>
<p>Thanks for any help and I am happy to send the data if anyone wants to try!</p>
<p>Christy</p>

---

## Post #2 by @muratmaga (2025-03-21 03:54 UTC)

<p><a class="mention" href="/u/christyhipsley">@christyhipsley</a> Without the data this would be hard to replicate. If you can share your datasets, it would be easier to debug. We have introduced a few changes to the GPA module’s visualization functionality to report potential issues with landmark mismatch (as opposed to silently failing). Since you are not seeing any errors, makes me wonder if you are using the latest version of the SlicerMorph.</p>
<p>At this point, you should be running Slicer 5.8.1 (that’s the latest stable, 5.8.0 is not receiving the updates anymore) and you can either uninstall/reinstall SlicerMorph, or use the update functionality.</p>
<p>Meanwhile, I would load also the reference model and landmark set into a clean Slicer, and make sure that they do line up (i.e., landmarks are on the model they are supposed to represent).</p>

---
