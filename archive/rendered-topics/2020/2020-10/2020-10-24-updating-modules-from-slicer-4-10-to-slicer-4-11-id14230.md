# Updating modules from Slicer-4.10 to Slicer-4.11

**Topic ID**: 14230
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/updating-modules-from-slicer-4-10-to-slicer-4-11/14230

---

## Post #1 by @Greydon_Gilmore (2020-10-24 20:01 UTC)

<p>having spent some time working through our scripted modules, we failed to update slicer utility load functions to the most recent syntax. For instance, when calling <code>slicer.util.loadMarkupsFiducialList</code> the return is now a list but our script expects only the node.</p>
<p>You make a valid point, I will take the time to update our scripted modules to make it work with the latest stable.</p>

---

## Post #2 by @lassoan (2020-10-24 20:10 UTC)

<p>You may find the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer">migration guide</a> useful and documentation may help, too:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; help(slicer.util.loadMarkupsFiducialList)
Help on function loadMarkupsFiducialList in module slicer.util:

loadMarkupsFiducialList(filename, returnNode=False)
    Deprecated. Use loadMarkups function instead.

&gt;&gt;&gt; help(slicer.util.loadMarkups)
Help on function loadMarkups in module slicer.util:

loadMarkups(filename)
    Load node from file.
    
    :param filename: full path of the file to load.
    :return: loaded node (if multiple nodes are loaded then a list of nodes).
</code></pre>
<p><code>loadMarkups</code> returns the loaded node or raises an exception.</p>

---

## Post #3 by @Greydon_Gilmore (2020-10-24 20:43 UTC)

<p>fantastic resource. Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for always being so responsive <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #4 by @Greydon_Gilmore (2020-10-24 22:25 UTC)

<p>a step in one of the modules is applying a MNI transform to the volumes and models in the scene. To do this I originally ran:</p>
<pre><code class="lang-auto">volumes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
for ivol in volumes:
    ivol.SetAndObserveTransformNodeID(mniTransform.GetID())

models = slicer.util.getNodesByClass('vtkMRMLModelNode')
for imodel in models:
    imodel.SetAndObserveTransformNodeID(mniTransform.GetID())
</code></pre>
<p>however, now in the stable 4.11 release the 2D views look correct but the 3D view seems to display the volume incorrectly. Is this the correct way to apply the transform to volumes and models?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe3ebd85211f82e32a03cd5e109b520262992d23.jpeg" data-download-href="/uploads/short-url/Ah9Hh5veqbw2a2tSvccgvzOMoMz.jpeg?dl=1" title="Screenshot from 2020-10-24 17-58-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe3ebd85211f82e32a03cd5e109b520262992d23_2_690x248.jpeg" alt="Screenshot from 2020-10-24 17-58-46" data-base62-sha1="Ah9Hh5veqbw2a2tSvccgvzOMoMz" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe3ebd85211f82e32a03cd5e109b520262992d23_2_690x248.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe3ebd85211f82e32a03cd5e109b520262992d23_2_1035x372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe3ebd85211f82e32a03cd5e109b520262992d23_2_1380x496.jpeg 2x" data-dominant-color="52515B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-24 17-58-46</span><span class="informations">1668×601 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-10-24 22:27 UTC)

<p>The code snippet looks good. Can you share a scene with us that reproduces this?</p>

---

## Post #7 by @Greydon_Gilmore (2020-10-25 00:15 UTC)

<p>here is the <code>.mrb</code> file for the scene: <a href="https://drive.google.com/file/d/1Qmg8uSaWKLvbwnFhHZqlfTNYhmxP-EuR/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1Qmg8uSaWKLvbwnFhHZqlfTNYhmxP-EuR/view?usp=sharing</a></p>

---

## Post #8 by @Greydon_Gilmore (2020-10-25 00:23 UTC)

<p>I realized that without my scripted module the scene may not look like the one I took a screenshot of. I can set up the <code>.mrb</code> file so it resembles the view I would like?</p>

---

## Post #9 by @Greydon_Gilmore (2020-10-25 00:26 UTC)

<p>I think I know the problem, I have created a custom layout for the views. This is my code snippet for the views:</p>
<pre><code class="lang-auto">layout = (
			"&lt;layout type=\"horizontal\"&gt;"
			" &lt;item&gt;"
			"  &lt;settingsSidePanel&gt;&lt;/settingsSidePanel&gt;"
			" &lt;/item&gt;"
			" &lt;item&gt;"
			"  &lt;layout type=\"vertical\"&gt;"
			"   &lt;item&gt;"
			"    &lt;layout type=\"horizontal\"&gt;"
			"     &lt;item&gt;"
			"      &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;"
			"       &lt;property name=\"orientation\" action=\"default\"&gt;Axial&lt;/property&gt;"
			"       &lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;"
			"       &lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;"
			"      &lt;/view&gt;"
			"     &lt;/item&gt;"
			"     &lt;item&gt;"
			"      &lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"
			"       &lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"
			"      &lt;/view&gt;"
			"     &lt;/item&gt;"
			"    &lt;/layout&gt;"
			"   &lt;/item&gt;"
			"   &lt;item&gt;"
			"    &lt;layout type=\"horizontal\"&gt;"
			"     &lt;item&gt;"
			"      &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;"
			"       &lt;property name=\"orientation\" action=\"default\"&gt;Sagittal&lt;/property&gt;"
			"       &lt;property name=\"viewlabel\" action=\"default\"&gt;Y&lt;/property&gt;"
			"       &lt;property name=\"viewcolor\" action=\"default\"&gt;#EDD54C&lt;/property&gt;"
			"      &lt;/view&gt;"
			"     &lt;/item&gt;"
			"     &lt;item&gt;"
			"      &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;"
			"       &lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;"
			"       &lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;"
			"       &lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;"
			"      &lt;/view&gt;"
			"     &lt;/item&gt;"
			"    &lt;/layout&gt;"
			"   &lt;/item&gt;"
			"  &lt;/layout&gt;"
			" &lt;/item&gt;"
			"&lt;/layout&gt;"
			)
		layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
		layoutNode.AddLayoutDescription(yourLayoutID, layout)
</code></pre>

---

## Post #10 by @lassoan (2020-10-25 00:28 UTC)

<p>Based on what I see in the scene, it seems to be an LPS/RAS coordinate system mismatch: Slicer now assumes that surface meshes are stored on disk in LPS coordinate system if the file does not contain coordinate system information. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">this section</a> of the migration guide for details.</p>

---

## Post #11 by @Greydon_Gilmore (2020-10-25 00:36 UTC)

<p>ah okay, that would explain it. What <code>vtkMRMLModelNode</code> method would I use to determine coordinate system?</p>
<p>In my custom layout, when defining the 3D view, am I missing any setting:</p>
<pre><code class="lang-auto">"     &lt;item&gt;"
"      &lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"
"       &lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"
"      &lt;/view&gt;"
"     &lt;/item&gt;"
</code></pre>

---

## Post #12 by @Greydon_Gilmore (2020-10-25 00:39 UTC)

<p>I think I found the solution from the documentation link you sent:</p>
<blockquote>
<p>Option C: Write <code>SPACE=RAS</code> in the comment/description field in the mesh file…</p>
</blockquote>
<p>[EDIT]</p>
<p>after further reading, it’s more clear how to obtain the coordinate system of a model (using Python syntax):</p>
<pre><code class="lang-auto">node=getNode('some_model.vtk')

# Will return either LPS or RAS
coordSys = node.GetStorageNode().GetCoordinateSystemTypeAsString(node.GetStorageNode().GetCoordinateSystem())
</code></pre>
<p>Then it’s a matter of setting the coordinate system you want the model to use:</p>
<pre><code class="lang-auto"># 0 for RAS and 1 for LPS
node.GetStorageNode().SetCoordinateSystem(0)
</code></pre>

---

## Post #13 by @Greydon_Gilmore (2020-10-25 01:37 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="4" data-topic="14230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<pre><code class="lang-auto">models = slicer.util.getNodesByClass('vtkMRMLModelNode')
for imodel in models:
    imodel.SetAndObserveTransformNodeID(mniTransform.GetID())
</code></pre>
</blockquote>
</aside>
<p>I found the problem for why applying the transform to the models in the scene resulted in the spatial difference between 2D and 3D views. Using <code>slicer.util.getNodesByClass('vtkMRMLModelNode')</code> returns the models but also [‘Red Volume Slice’, ‘Green Volume Slice’, ‘Yellow Volume Slice’]. So the MNI transform was being applied to the 2D views as well as the models.</p>

---

## Post #14 by @lassoan (2020-10-25 01:43 UTC)

<p>Good catch. You can determine if a node is a slice model node by calling <code>slicer.vtkMRMLSliceLogic.IsSliceModelNode(modelNode)</code>. But of course it is much more cleaner and safer to apply transforms only to nodes that you load/create (you can never be sure what else is in the scene already).</p>

---
