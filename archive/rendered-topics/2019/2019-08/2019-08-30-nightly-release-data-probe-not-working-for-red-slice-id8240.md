# Nightly Release - Data Probe not working for Red Slice

**Topic ID**: 8240
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/nightly-release-data-probe-not-working-for-red-slice/8240

---

## Post #1 by @Greydon_Gilmore (2019-08-30 16:47 UTC)

<p>Hi all,</p>
<p>I haven’t found a solution so I’m asking here. I can’t seem to activate the data probe instance for the Red Slice. It is working for Yellow and Green. The widget appears empty when hovering over the Red slice.</p>
<p>Is there a way to activate the data probe for Red? Preferably in code.</p>
<p>Thanks!<br>
Greydon</p>

---

## Post #2 by @Sam_Horvath (2019-08-30 16:55 UTC)

<p>What platform are you on?  In, today’s windows package the data probe appears to be working correctly for all three slice viewers.</p>
<p>Did you encounter this this while trying some type of customization (you mention code)?  Some more details about what you are trying to do would be helpful.</p>
<p>Sam</p>

---

## Post #3 by @Greydon_Gilmore (2019-08-30 20:30 UTC)

<p>On Windows 10 and have 3D Slicer version 4.11.0-2019-08-13.</p>
<p>I am scripting a module, which runs the following lines of code to reset the slice views when the module loads:</p>
<pre><code class="lang-auto">applicationLogic = slicer.app.applicationLogic()
interactionNode = applicationLogic.GetInteractionNode()
interactionNode.Reset(None)
		
layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(3)
		
interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()
interactorStyle.SetActionEnabled(interactorStyle.BrowseSlice, True)

slicer.util.resetSliceViews()
</code></pre>
<p>I’m wondering if these lines are causing the issue?</p>
<p>Greydon</p>

---

## Post #4 by @Sam_Horvath (2019-08-30 21:28 UTC)

<p>These lines are the issue.  You are changing the state of the red slice interactor, which is why it is the only one broken.</p>
<p><code>interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()</code></p>
<p><code>interactorStyle.SetActionEnabled(interactorStyle.BrowseSlice, True)</code></p>
<p>The default state can be obtained by instead using:</p>
<p><code>interactorStyle.SetActionEnabled(interactorStyle.AllActionsMask, True)</code></p>
<p>However, I am not sure why you are changing the slice interactor to reset the slices.  You can just exclude the two lines relating to the interactorStyle entirely, and it should work as intended.</p>

---

## Post #5 by @Greydon_Gilmore (2019-08-30 21:46 UTC)

<p>Thank you for the reply, that will help!</p>
<p>The module I am developing has a neurosurgical application. Surgeons will be using it to plan research cases. There is a step that requires detection of a stereotactic frame from a CT scan. The frame contains fiducial markings that are best seen on the axial slice. I use a search algorithm to find these fiducials through the entire z-plane. The surgeon has to scroll through the z-plane to confirm that the fiducials were accurately detected by my algorithm. So to make this easier, in the module script, I use this:</p>
<pre><code class="lang-auto">applicationLogic = slicer.app.applicationLogic()
selectionNode = applicationLogic.GetSelectionNode()
selectionNode.SetReferenceActiveVolumeID(self.frameFidVolume.GetID())
applicationLogic.PropagateVolumeSelection(0)
applicationLogic.FitSliceToAll()
		
interactionNode = applicationLogic.GetInteractionNode()
interactionNode.Reset(None)
			
layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(6)
			
layoutManager = slicer.app.layoutManager()
			layoutManager.sliceWidget('Red').mrmlSliceNode().RotateToVolumePlane(self.frameFidVolume)
</code></pre>
<p>Which gives this display…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d5b99fc465d964290599f950515cd9e4bec0d72.jpeg" data-download-href="/uploads/short-url/kavzSlsYLpEDCvZmBDhqwbziaJA.jpeg?dl=1" title="example_frame" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5b99fc465d964290599f950515cd9e4bec0d72_2_690x414.jpeg" alt="example_frame" data-base62-sha1="kavzSlsYLpEDCvZmBDhqwbziaJA" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5b99fc465d964290599f950515cd9e4bec0d72_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d5b99fc465d964290599f950515cd9e4bec0d72_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d5b99fc465d964290599f950515cd9e4bec0d72.jpeg 2x" data-dominant-color="444242"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example_frame</span><span class="informations">1357×815 92.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If 3D Slicer is closed I wanted to ensure the slice views are reset upon opening the module again.</p>
<p>Greydon</p>

---

## Post #6 by @lassoan (2019-08-30 23:21 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="5" data-topic="8240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>The module I am developing has a neurosurgical application</p>
</blockquote>
</aside>
<p>Sounds great. Slicer has been used for neurosurgical planning quite extensively since its inception, so it should be well suited for your project.</p>
<p>There is an <a href="https://github.com/SlicerProstate/SlicerZFrameRegistration">automatic stereoractic frame registration extension</a> available, if you need an other implementation for comparison.</p>
<p>You can also use Slicer for surgical navigation, using Medtronic or BrainLab systems or a wide range of standalone optical or electromagnetic trackers. Intra operative ultrasound, surface scanning, etc. are also available. See <a href="http://www.slicerigt.org">www.slicerigt.org</a> for details.</p>
<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="5" data-topic="8240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>If 3D Slicer is closed I wanted to ensure the slice views are reset upon opening the module again.</p>
</blockquote>
</aside>
<p>All views are automatically reset when you close the scene, so there is no need for any additional node modifications.</p>

---
