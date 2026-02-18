# Make clipping to be separate module

**Topic ID**: 44266
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/make-clipping-to-be-separate-module/44266

---

## Post #1 by @mohammed_alshakhas (2025-08-29 17:38 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/chir.set">@chir.set</a>  i posted earlier about clipping to be separate module or be much more accessible  . its an amazing feature that’s so hard to use . since i accidently discovered it i use it all the time . toggling on and off from segmentation menu is time consuming</p>
<p>please consider this .</p>

---

## Post #2 by @lassoan (2025-08-29 17:46 UTC)

<p>Adding a separate module would mean that you need to switch away from the current module (Models, Segmentations, Volume rendering, etc.). It would make the feature a bit less accessible (you would need to do several clicks instead of just scroll down in the module GUI).</p>
<p>Could you describe how you use clipping and how do you think it could be made simpler?</p>

---

## Post #3 by @mohammed_alshakhas (2025-08-29 18:23 UTC)

<p>thank you for reply .</p>
<p>i do lots of surgery planning measurement in slicer , despite having the best software for planning . i still find slicer the most accurate and versatile .</p>
<p>when meausreing , i like to split mandibles into halves . allow much better visulaizarion .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71d6d1a5b1eb597979004added59592c78a45314.jpeg" data-download-href="/uploads/short-url/gf4cuYcXEE6XnUsqPOdxurOpg3y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71d6d1a5b1eb597979004added59592c78a45314_2_690x267.jpeg" alt="image" data-base62-sha1="gf4cuYcXEE6XnUsqPOdxurOpg3y" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71d6d1a5b1eb597979004added59592c78a45314_2_690x267.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71d6d1a5b1eb597979004added59592c78a45314_2_1035x400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71d6d1a5b1eb597979004added59592c78a45314_2_1380x534.jpeg 2x" data-dominant-color="ECEBE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×738 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96384fc78d25867b7857289d2e87dcb096d3079.jpeg" data-download-href="/uploads/short-url/qs1yc53NApaivCFbtELeXRmZ4V3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96384fc78d25867b7857289d2e87dcb096d3079_2_690x358.jpeg" alt="image" data-base62-sha1="qs1yc53NApaivCFbtELeXRmZ4V3" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96384fc78d25867b7857289d2e87dcb096d3079_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96384fc78d25867b7857289d2e87dcb096d3079_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b96384fc78d25867b7857289d2e87dcb096d3079_2_1380x716.jpeg 2x" data-dominant-color="C9C7C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×994 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i also clip to see condyles in 3d clipped in mid fossa which is great view for clinical correlations .</p>
<p>i can see many uses for it  in the future cases</p>
<p>it doesn’t have to be a module , it cant be toggled on and off at least from slice view or 3d view  similar to slice interaction tab . or from drop menu in the slice .</p>
<p>another way is to make it like to markup tool . once tab is pressed a tool bar is shown . toggling and slice selection is accessible .</p>
<p>i think it  deserve its place in the drop menu or right click for toggling it on and off.</p>
<p>i still think making it a module on its own is great to configure it quickly  and full interaction .</p>

---

## Post #4 by @lassoan (2025-08-29 18:46 UTC)

<p>Would a <code>Clipping</code> menu item in the Subject Hierarchy tree’s visibility menu help?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef9fa460ccdddaf54499460833e1e6ad34577a38.png" data-download-href="/uploads/short-url/ybO97jmk8IpExyArofk7KOUtwyA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef9fa460ccdddaf54499460833e1e6ad34577a38_2_690x243.png" alt="image" data-base62-sha1="ybO97jmk8IpExyArofk7KOUtwyA" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef9fa460ccdddaf54499460833e1e6ad34577a38_2_690x243.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef9fa460ccdddaf54499460833e1e6ad34577a38_2_1035x364.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef9fa460ccdddaf54499460833e1e6ad34577a38_2_1380x486.png 2x" data-dominant-color="D3D8DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1668×589 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, you may find that adding a direct keyboard shortcut that toggles all clipping on/off works better. To get that, you can copy-paste this code snippet into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">def toggleClipping():
    if hasattr(slicer, 'clippedDisplayNodes'):
        # Restore clipped state of nodes
        for displayNode in slicer.clippedDisplayNodes:
            displayNode.ClippingOn()
        del slicer.clippedDisplayNodes
    else:
        # Save clipped state of nodes and then disable clipping
        slicer.clippedDisplayNodes = []
        displayNodes = slicer.util.getNodesByClass("vtkMRMLDisplayNode")
        for displayNode in displayNodes:
            if displayNode.GetClipping():
                slicer.clippedDisplayNodes.append(displayNode)
                displayNode.ClippingOff()

shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Ctrl+R"))
shortcut.connect("activated()", toggleClipping)
</code></pre>
<p>After this you can use Ctrl-R to toggle all clipping in the scene. You can add this code snippet to your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup file</a> to make the keyboard shortcut persistent.</p>

---

## Post #5 by @mohammed_alshakhas (2025-09-09 13:41 UTC)

<p>Clipping in in hierarchy would need good enough</p>

---
