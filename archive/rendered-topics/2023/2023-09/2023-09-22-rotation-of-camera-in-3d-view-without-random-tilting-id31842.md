---
topic_id: 31842
title: "Rotation Of Camera In 3D View Without Random Tilting"
date: 2023-09-22
url: https://discourse.slicer.org/t/31842
---

# Rotation of camera in 3D view without random tilting

**Topic ID**: 31842
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/rotation-of-camera-in-3d-view-without-random-tilting/31842

---

## Post #1 by @moraleda (2023-09-22 10:20 UTC)

<p>Hi everyone,</p>
<p>as some of you might feel as I do that the camera in 3D view tilts when rotating, I have rewritten the code in <code>Slicer/Libs/MRML/DisplayableManger/vtkMRMLCameraWidget.cxx</code> in <code>vtkMRMLCameraWidget::ProcessRotate</code> as the following and then built my own Slicer.</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
bool vtkMRMLCameraWidget::ProcessRotate(vtkMRMLInteractionEventData* eventData)
{
  if (!this-&gt;Renderer || !eventData)
    {
    return false;
    }

  const int* eventPosition = eventData-&gt;GetDisplayPosition();
  int dx = eventPosition[0] - this-&gt;PreviousEventPosition[0];
  int dy = eventPosition[1] - this-&gt;PreviousEventPosition[1];
  if (dx == 0 &amp;&amp; dy == 0)
    {
    return true;
    }

  const int *size = this-&gt;Renderer-&gt;GetRenderWindow()-&gt;GetSize();

  double delta_elevation = -20.0 / size[1];
  double delta_azimuth = -20.0 / size[0];

  double rxf = (double)dx * delta_azimuth * this-&gt;MotionFactor;
  double ryf = (double)dy * delta_elevation * this-&gt;MotionFactor;

  vtkCamera* camera = this-&gt;GetCamera();
  if (!camera)
    {
    return false;
    }

  bool wasCameraNodeModified = this-&gt;CameraModifyStart();

  if (this-&gt;CameraTiltLocked == true)
    {
    camera-&gt;Azimuth(rxf);
    }
  else
    {
    const double* cameraPosition = camera-&gt;GetPosition();
    const double* cameraFocalPoint = camera-&gt;GetFocalPoint();
    const double* cameraViewUp = camera-&gt;GetViewUp();
    bool upside_down = cameraViewUp[2] &lt; 0;
    double upside_down_factor = upside_down ? -1.0 : 1.0;

    double P[3] = {
        cameraPosition[0] - cameraFocalPoint[0],
        cameraPosition[1] - cameraFocalPoint[1],
        cameraPosition[2] - cameraFocalPoint[2]
    };

    double H = sqrt(P[0] * P[0] + P[1] * P[1]);
    double elev = atan2(P[2], H);

    double sin_elev = sin(elev);
    double azi;
    if (abs(sin_elev) &lt; 0.8) {
      azi = atan2(P[1], P[0]);
    } else {
      if (sin_elev &lt; -0.8) {
          azi = atan2(upside_down_factor * cameraViewUp[1], upside_down_factor * cameraViewUp[0]);
      } else {
          azi = atan2(-upside_down_factor * cameraViewUp[1], -upside_down_factor * cameraViewUp[0]);
      }
    }
    double  D = sqrt(P[0] * P[0] + P[1] * P[1]  + P[2] * P[2]);
    double azi_new = azi + rxf / 60.0;
    double elev_new = elev + upside_down_factor * ryf / 60.0;
    double Hnew = D * cos(elev_new);

    double Pnew[3] = {
        Hnew * cos(azi_new),
        Hnew * sin(azi_new),
        D * sin(elev_new)
    };

    double up_z = upside_down_factor * cos(elev_new);
    double up_h = upside_down_factor * sin(elev_new);

    double up_new[3] = {
        -up_h * cos(azi_new),
        -up_h * sin(azi_new),
        up_z
    };

    double new_pos[3] = {
        cameraFocalPoint[0] + Pnew[0],
        cameraFocalPoint[1] + Pnew[1],
        cameraFocalPoint[2] + Pnew[2]
    };

    camera-&gt;SetViewUp(up_new);
    camera-&gt;SetPosition(new_pos);
    }
  camera-&gt;OrthogonalizeViewUp();
  this-&gt;CameraModifyEnd(wasCameraNodeModified, true, true);

  this-&gt;PreviousEventPosition[0] = eventPosition[0];
  this-&gt;PreviousEventPosition[1] = eventPosition[1];

  return true;
}
</code></pre>
<p>I particularly changed the code after</p>
<pre><code class="lang-auto">  if (this-&gt;CameraTiltLocked == true)
    {
    camera-&gt;Azimuth(rxf);
    }
  else
    {  # changes are made here
</code></pre>
<p>I hope you will find it usefull as well <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>The code was rewritten to C++ based on this py-file:<br>
<a href="https://github.com/RubendeBruin/DAVE/blob/d0dec40c9a2e9416f31edabfeaf1f769fb6eca51/src/DAVE/visual_helpers/vtkBlenderLikeInteractionStyle.py#L4" rel="noopener nofollow ugc">https://github.com/RubendeBruin/DAVE/blob/d0dec40c9a2e9416f31edabfeaf1f769fb6eca51/src/DAVE/visual_helpers/vtkBlenderLikeInteractionStyle.py#L4</a></p>

---

## Post #2 by @lassoan (2023-09-22 14:33 UTC)

<p>Thank you for raising this and providing an example of an additional method for constraining camera rotation in the 3D view.</p>
<p>The camera’s view-up direction may indeed unintentionally spin as the camera is rotated around. Although it is quite easy to fix it by either moving the mouse in a circle or spinning the view using Ctrl + Click-and-drag, it is even better if it can be avoided in the first place. The “Tilt lock” option was added for exactly this reason, but it may be a bit too restrictive to not let users to change the view-up direction at all.</p>
<p>Your code snippet is nice in that it allows tilting but not spinning of the view-up direction, this allows some more freedom than completely locking the view-up direction, but more controlled than letting anything rotated anywhere. However, the current impmlementation you shared has the patient IS axis hardcoded to be the view-up direction. This is great if you want the patient S direction to point upwards, but extremely annoying when you want to make some other axis to point upwards - for example to show a lateral view of the patient (as lying on the CT table). This view orientation is impossible to achieve with code you proposed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d6e909b14d467827aeacc4e3f5ae815bf3a128.jpeg" data-download-href="/uploads/short-url/p7oGsRoY6ArBeJwzndS3d0hvFC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6e909b14d467827aeacc4e3f5ae815bf3a128_2_690x405.jpeg" alt="image" data-base62-sha1="p7oGsRoY6ArBeJwzndS3d0hvFC" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6e909b14d467827aeacc4e3f5ae815bf3a128_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6e909b14d467827aeacc4e3f5ae815bf3a128_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d6e909b14d467827aeacc4e3f5ae815bf3a128_2_1380x810.jpeg 2x" data-dominant-color="8D87AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1394×820 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We cannot remove the current free motion and probably want to keep the “tilt lock” option as well, but we could add a third “Spin lock” option. It would do almost what you implemented, but instead of always keeping the patient IS axis as view-up, it would keep an arbitrarily chosen direction as view-up. The “arbitrarily chosen direction” would actually be the view-up direction at the time when “Spin lock” is activated.</p>
<p>If you can make this improvement we would be happy to add this “Spin lock” option to Slicer core.</p>

---

## Post #3 by @moraleda (2023-09-22 17:27 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>yes, you are right that my code is somewhat restricted. I had not noticed before the issue that you addressed. I will try to add the feature you said.</p>
<p>Thanks!</p>

---
