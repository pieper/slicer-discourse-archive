# Link a transform's visibility to transformed volume visibility

**Topic ID**: 45604
**Date**: 2025-12-25
**URL**: https://discourse.slicer.org/t/link-a-transforms-visibility-to-transformed-volume-visibility/45604

---

## Post #1 by @shai-ikko (2025-12-25 14:57 UTC)

<p>Hi,</p>
<p>In my application, I want to load a volume, and give the user controls to spin it around. So when I load the volume, I also create a Transform, make the volume observe it, and then call <code>transformNode.GetDisplayNode().SetEditorVisibility(True)</code>. This puts very handy controls for rotations and translations (shifts in space) in all slice views and the 3D views, and yay! As long as I’m considering only this volume, all is peachy.</p>
<p>But if I now try to repeat the process, and load another volume the same way, the first transform is still visible for editing – although it does not even affect the shown volume. Now there are double controls; you can’t tell visually which is the “current” one, you can only fix this by non-obvious manipulations.</p>
<p>For very simple use, I guess I could listen for changes in the Selection Node, but when the use becomes more involved (comparisons, or putting one volume in background and one in foreground) that becomes useless.</p>
<p>Is there a (preferably easy) way I’m missing, to say “show this Transform only with observing volumes”?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2025-12-26 14:42 UTC)

<p>I don’t see having anything built-in for that, since a transform could be applied to several things, some visible and some not.  I think you need a custom piece of logic that sets the desired transform interaction and volume visibility as a mode you configure when the data is loaded or when you want to go back to that state.  I.e. you have a list of volumes you are operating on and when the user selects one you make it and the corresponding transform visible and make the others invisibile.</p>

---

## Post #3 by @lassoan (2025-12-27 02:42 UTC)

<p>I agree, short-term a few-line custom script is the best solution.</p>
<p>In the next few months we plan to finish implementation of <a href="https://github.com/Slicer/Slicer/issues/6159"><em>node focus</em></a> feature, which provides the functionality that you described and much more. It will be possible to configure display of additional elements (such as transform handles) so that they are shown when the node gets <em>hard focus</em> (e.g., the user clicks on it).</p>

---

## Post #4 by @shai-ikko (2025-12-29 08:39 UTC)

<p>Thank  you both, I’ll implement something now but will keep tabs on node focus for the future.</p>

---

## Post #5 by @shai-ikko (2025-12-31 15:58 UTC)

<p>FWIW, this turned out harder than I thought – probably because I am not actually writing an independent application, but just an extension, which I want to “play nice” with the rest of Slicer.</p>
<p>What I did (I may share later, not sure I can) is,</p>
<p>Per transform that I want handled this way:</p>
<ul>
<li>Keep an observer on each SliceCompositeNode, to note when the volumes change</li>
<li>Keeping an observer on node addition/removal in the scene, to note when <code>SliceCompositeNode</code>s are added or removed</li>
<li>Manage the ViewNode ids on the transform’s DisplayNode</li>
<li>Also listen for changes in the transform’s DisplayNode that don’t originate from the volume changes in the Composite nodes – so that if a user hides it, it stays hidden.</li>
</ul>
<p>This now mostly works.</p>

---

## Post #6 by @pieper (2025-12-31 16:19 UTC)

<p>Yes, thanks for sharing that experience.  I agree it’s hard to do this “bottom up” since visibility is a complex concept (a volume can be visible in some views and hidden in others, and they can come can do at any time).  That’s why I was suggesting a “top down” approach, where you pick a volume, and then ensure that it is visible in the views you want ant that only the corresponding transform controls are enabled.  Not sure what works best with your workflow.</p>

---
