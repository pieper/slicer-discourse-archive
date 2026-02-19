---
topic_id: 23546
title: "Upgrading Endoscopy Extension With Camera Interpolation"
date: 2022-05-23
url: https://discourse.slicer.org/t/23546
---

# Upgrading Endoscopy extension with camera interpolation

**Topic ID**: 23546
**Date**: 2022-05-23
**URL**: https://discourse.slicer.org/t/upgrading-endoscopy-extension-with-camera-interpolation/23546

---

## Post #1 by @jadh4v (2022-05-23 18:43 UTC)

<p>In our work towards developing a camera flythrough visualization for a Slicer based custom application <a href="https://github.com/KitwareMedical/vpaw" rel="noopener nofollow ugc"> VPAW</a>, we are considering keyframe interpolation of camera poses for creating a flythrough.</p>
<p>We considered multiple existing options as discussed in issue <a href="https://github.com/KitwareMedical/vpaw/issues/9" rel="noopener nofollow ugc">KitwareMedical/vpaw#9</a>, to converge on two extensions that consist most of the functionalities that we require.</p>
<p><em>Endoscopy</em> is the obvious choice as it provides a camera flythrough over a user-defined curve. However, it doesn’t provide camera pose interpolation over this curve and only follows the curve tangentially.</p>
<h3><a name="p-78428-proposed-plan-1" class="anchor" href="#p-78428-proposed-plan-1" aria-label="Heading link"></a>Proposed plan</h3>
<p>We are thinking of upgrading the Slicer build-in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html" rel="noopener nofollow ugc">Endoscopy</a> module to allow defining camera poses over the curve and interpolation using these “keyframes”.</p>
<p>There is an existing C++ extension, <a href="https://github.com/KitwareMedical/Slicer-CameraPath" rel="noopener nofollow ugc">CameraPath</a>, that contains some of these functions that can either be imported and re-used in <em>Endoscopy</em> or re-implement in it. We would like your opinion on the same.</p>
<p><strong>Question:</strong> Would it make sense to promote <em>CameraPath</em> as a core Slicer module and then import the logic to upgrade <em>Endoscopy</em>? Or Simply re-implement the functions in <em>Endoscopy</em> itself?</p>
<p>In some sense <em>Endoscopy</em> is a special case of <em>CameraPath</em>. <em>CameraPath</em> will define a fixed flythrough path and interpolated camera poses along it, while <em>Endoscopy</em> utilizes such a path / camera interpolation for a more interactive navigation and visualization of data.</p>

---

## Post #2 by @pieper (2022-05-23 19:13 UTC)

<p>Glad you are able to work on this <a class="mention" href="/u/jadh4v">@jadh4v</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>To me it would make sense to add some pure-VTK camera interpolation functionality, perhaps just one class based on <a href="https://vtk.org/doc/nightly/html/classvtkQuaternionInterpolator.html#details"><code>vtkQuaternionInterpolator</code></a> with some extra code to handle changes in field of view and maybe other parameters.  This could go in vtkAddon if it’s C++ or in Endoscopy logic if it could be done in python (I’d think it could).</p>
<p>Then in the Endoscopy module I think it would be pretty straightforward to allow the user to camera keyframes along the path and then they could be interpolated during the flythrough.  The exact UI would take a bit of thought, but if we constrain the options it should be usable and not too confusing for the user.</p>
<p>It would also make sense for the Endoscopy module to export to a Sequence, like the Animator does, so that it could be recorded by the ScreenCapture logic.</p>

---

## Post #3 by @hherhold (2022-05-23 19:39 UTC)

<p>I’m not familiar with the CameraPath module, and my recent attempts with Endoscopy haven’t gone well, but a few thoughts on what would make this sort of thing useful. I think at a minimum, the Camera position, Camera look point, and Camera orientation (up vector) should be key-framable. Currently (I believe) endoscopy assumes the camera looks down the path, which is not always optimal.</p>
<p>I think a real issue here could be feature creep. It’s very easy to say “well, VG Studio does this or Drishti does that”, which is nice, but I find if I truly need full animation capabilities, I just use Blender. There should be a “sweet spot” of features that will satisfy a large Slicer audience without being onerous or requiring lots of feature additions.</p>
<p>My 2 cents…</p>

---

## Post #4 by @hherhold (2022-05-23 19:40 UTC)

<p>Sorry - should have added that yes, I know a number of people (myself included) who would be VERY interested in any work on this!</p>

---

## Post #5 by @jadh4v (2022-05-24 14:15 UTC)

<p>Thanks for the reply. Using <code>vtkAddon</code> to create the interpolation functionality of camera pose sounds good to me.</p>
<p><strong>To flesh-out the UI part a bit more:</strong></p>
<ol>
<li>
<p>We could use the 3D view camera state itself as a way to insert keyframes. Initially we were considering having a <a href="https://github.com/KitwareMedical/Slicer/commit/9af308920309ec8cef890b98078574ef36de3737" rel="noopener nofollow ugc">flight mode</a> for the 3D view to assist in flying around and placing keyframes, but since we can define the path curve first, it is probably not needed. The user can just fly along the path and stop and insert keyframes wherever necessary.</p>
</li>
<li>
<p>Regarding markup / display of keyframes we can simply use a camera mesh model to indicate the position of the interested keyframes along the path, unless there are any existing suitable markups/glyphs for this purpose.</p>
</li>
<li>
<p>Along with camera pos and fov, would it make sense to also interpolate volume property, etc for better local control of visualization?</p>
</li>
<li>
<p>Should we provide lighting fixed on the camera that moves with it?</p>
</li>
</ol>

---

## Post #6 by @pieper (2022-05-24 14:20 UTC)

<aside class="quote no-group" data-username="jadh4v" data-post="5" data-topic="23546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jadh4v/48/65504_2.png" class="avatar"> jadh4v:</div>
<blockquote>
<p>Along with camera pos and fov, would it make sense to also interpolate volume property, etc for better local control of visualization?</p>
</blockquote>
</aside>
<p>The Animator module <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L277-L434">has some code for this</a> and it would be nice to either reuse or generalize this feature.  Currently it requires that the transfer functions have the same number of control points at the keyframes.</p>
<aside class="quote no-group" data-username="jadh4v" data-post="5" data-topic="23546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jadh4v/48/65504_2.png" class="avatar"> jadh4v:</div>
<blockquote>
<p>Should we provide lighting fixed on the camera that moves with it?</p>
</blockquote>
</aside>
<p>Yes, I would think so - a headlight makes sense for an endoscopy simulation.</p>

---

## Post #7 by @jadh4v (2022-05-24 16:29 UTC)

<p>Thanks, that is great to hear. I do appreciate the point of feature creep. While this started as a way to satisfy our requirements of the custom app, the endoscopy extension also feels a little lacking in its current state. As you mentioned, it only flies tangentially to the path. So we are also thinking from the point of view of justification of the name “Endoscopy” for the extension and what are the minimum set of features that are essential to it to be useful.</p>

---
