---
topic_id: 29312
title: "How To Configure Vr Controls Interactions In Python"
date: 2023-05-06
url: https://discourse.slicer.org/t/29312
---

# How to configure VR controls interactions in Python?

**Topic ID**: 29312
**Date**: 2023-05-06
**URL**: https://discourse.slicer.org/t/how-to-configure-vr-controls-interactions-in-python/29312

---

## Post #1 by @guillaumarie (2023-05-06 00:28 UTC)

<p>Hi,</p>
<p>I’m developing a 3DSlicer module using the virtual reality module and a Valve Index headset.<br>
I’m trying to configure my own controller interactions in order to:</p>
<ol>
<li>Deactivate all default VR controls</li>
<li>Add new customized VR controls (link the joystick movements to a transform so that a model moves accordingly // use the L/R triggers as “Previous” and “Next” buttons)</li>
</ol>
<p>The closest I’ve been is by getting the <code>vtkRenderWindowInteractor3D</code> using <code>slicer.modules.virtualreality.viewWidget().interactor()</code>. The good point is I’m able to remove event observers from this interactor so that the default VR controls don’t work anymore.<br>
But, out of 51 default event observers that I found in the <code>vtkRenderWindowInteractor3D</code>, it is enough to deactivate only 3 of them so that no command works anymore: <code>PinchEvent</code>, <code>Move3DEvent</code> and <code>Button3DEvent</code> (the 48 others observers can be removed and it doesn’t seem to change anything).<br>
This is an issue for my second goal, because as I want to allocate specific VR controls to individual events, it seems that all controls are accessible through 3 observers. Furthermore, I’d like to get data that come from events (particularly 2D vector for joysticks).</p>
<p>Then I found this code from <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/a5468fc3eb674cdbd2c724654e3e30d99f9ca360/VirtualReality/MRML/vtkVirtualRealityViewInteractorStyle.cxx#L289" rel="noopener nofollow ugc">vtkVirtualRealityViewInteractorStyle.cxx</a></p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
// Copied from vtkOpenVRInteractorStyle::SetupActions
//------------------------------------------------------------------------------
void vtkVirtualRealityViewInteractorStyle::SetupActions(vtkRenderWindowInteractor* iren)
{
  vtkOpenVRRenderWindowInteractor* oiren = vtkOpenVRRenderWindowInteractor::SafeDownCast(iren);

  if (oiren)
  {
    oiren-&gt;AddAction("/actions/vtk/in/Elevation", vtkCommand::Elevation3DEvent, true);
    oiren-&gt;AddAction("/actions/vtk/in/Movement", vtkCommand::ViewerMovement3DEvent, true);
    oiren-&gt;AddAction("/actions/vtk/in/NextCameraPose", vtkCommand::NextPose3DEvent, false);
    oiren-&gt;AddAction("/actions/vtk/in/PositionProp", vtkCommand::PositionProp3DEvent, false);
    oiren-&gt;AddAction("/actions/vtk/in/ShowMenu", vtkCommand::Menu3DEvent, false);
    oiren-&gt;AddAction("/actions/vtk/in/StartElevation", vtkCommand::Elevation3DEvent, false);
    oiren-&gt;AddAction("/actions/vtk/in/StartMovement", vtkCommand::ViewerMovement3DEvent, false);
    oiren-&gt;AddAction("/actions/vtk/in/TriggerAction", vtkCommand::Select3DEvent, false);
  }
}
</code></pre>
<p>But the interactor I use is from the <code>vtkRenderWindowInteractor3D</code> class, which doesn’t have these lines. So I got access to the interactorStyle <code>vtkVirtualRealityViewInteractorStyle</code> using interactor<code>.GetInteractorStyle()</code> but this “<em>object has no attribute ‘SetupActions’</em>”.<br>
Plus, the above <code>vtkCommand</code> are not understood neither by the interactor nor by the interactorStyle.</p>
<p>How should I do? If I’m not on the right track at all, what is the right way to change controls? Can I do this in Python? If not, what are the alternatives?</p>
<p>Sorry if it’s not clear but it’s also not in my mind, I hope I provided enough informations.<br>
Thanks you very much,</p>
<p>[Slicer 4.11.20210226 - Python 3.7]<br>
PS: I’m using an old 3DSlicer version because VR controllers didn’t work in the latest version last time I checked (2023-03-03).</p>

---

## Post #2 by @rbumm (2023-05-07 14:44 UTC)

<p>The 3D Slicer Virtual Reality extension is still not working in Slicer 5.3.0-2023-04-27.</p>
<p>Symptoms on Windows 11, Oculus Quest2 headset, <a href="https://gitlab.kitware.com/vtk/vtk/-/tree/master/Rendering/OpenVR">JSON files copied</a>:</p>
<p>Connecting the headset via SteamVR works, and rendering starts.<br>
You can fly the object around by pressing the right joystick and moving the right controller to a different axis.<br>
Trying to “grab” the object with the grab keys of both controllers - for rotating it etc. - immediately erases the object from the screen<br>
<img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji only-emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @cpinter (2023-05-11 10:50 UTC)

<p>Grabbing <em>objects</em> using the two controllers was never a feature of SlicerVR. The two-handed gesture controlled the camera. This is the last part that still does not work. Grabbing and moving objects as before (with one controller) works for me.</p>

---

## Post #4 by @guillaumarie (2023-05-13 23:37 UTC)

<p>Thanks for your answer!<br>
I finally stayed on Slicer 4.11.20210226 but used <a href="https://github.com/BOLL7708/OpenVR2Key" rel="noopener nofollow ugc">OpenVR2Key</a> to map VR controllers inputs to keyboard inputs. Then, I used <a href="https://doc.qt.io/qt-6/qshortcut.html" rel="noopener nofollow ugc">QShortcut</a> objects to listen to keyboard events and to callback my own functions (moving a needle according to one joystick and spinning a head model according to the other one).<br>
If it works in Slicer 5.3.0-2023-04-27 (I don’t see why it wouldn’t), it should be possible to recreate all default SlicerVR controls this way (a bit of work <img src="https://emoji.discourse-cdn.com/twitter/grimacing.png?v=12" title=":grimacing:" class="emoji" alt=":grimacing:" loading="lazy" width="20" height="20">)</p>

---

## Post #5 by @lucsdjango (2023-11-02 12:17 UTC)

<p>Thanks for the info!<br>
I am also hoping to be able to create my own mapping of controller buttons to actions.<br>
Is the workaround described above best way to acheive this?<br>
Any code snippet you could share with me would be greatly appriciated!</p>

---

## Post #6 by @lassoan (2023-11-02 13:21 UTC)

<p>The interaction in virtual reality in Slicer is being reworked right now to use as much as possible from VTK, yet keep the flexibility and access to many more features in Slicer. Maybe <a class="mention" href="/u/jcfr">@jcfr</a> can offer more information on timelines and what exactly will be available in the near future.</p>

---
