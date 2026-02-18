# Rendering MRI Volume using python from .nii file

**Topic ID**: 31290
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/rendering-mri-volume-using-python-from-nii-file/31290

---

## Post #1 by @Alvi_Rahman (2023-08-22 14:25 UTC)

<p>I am trying to show MRI volume of brains. Now I want to achieve sth that is shown here: <a href="https://www.youtube.com/watch?v=tXJS-ZnBP4k&amp;ab_channel=mahajanimaging" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=tXJS-ZnBP4k&amp;ab_channel=mahajanimaging</a>. It basically shows a face mesh and a variable slicer that can be adjusted to see the MRI volume in any one specific plane.</p>
<p>I have found and implemented one code that stacks the images from .nii file to produce 3D volume. The code is from here:<a href="https://gist.github.com/ofgulban/60ba53c46f6870fc30bb1b2117947600" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering of a nifti file using pyqtgraph library. · GitHub</a>.</p>
<p>I was able to crop it along the x-axis to view the internal structure which means it is possible to make the slicer function.<br>
However, I am not experienced enough.</p>
<p>I would like some guidance regarding this; mainly to learn how to accomplish this. I am a year undergrad student and I am doing this as a pet project. I would be grateful I can get guidance on how to achieve this using slicer or what algorithm to use.</p>
<p>I have also uploaded my output here as well.<br>
The code I used is as follows:</p>
<pre><code class="lang-auto">"""Test GL volume tool with MRI data."""

from pyqtgraph.Qt import QtGui, QtWidgets, QtCore
import pyqtgraph.opengl as gl
import numpy as np
from nibabel import load

FILENAME = r"X:\Braillic\NIFT to Volume\MR_Gd.nii\MR_Gd.nii"
RENDER_TYPE = "translucent"
THR_MIN = 1
THR_MAX = 2000

# =============================================================================
# Get MRI data
nii = load(FILENAME)
data = np.squeeze(nii.get_fdata())

data[data == 0] = THR_MIN
data[data &lt; THR_MIN] = THR_MIN
data[data &gt;= THR_MAX] = THR_MAX
data -= THR_MIN
data /= THR_MAX - THR_MIN

# (optional) Reorient data
data = data[:, ::-1, :]

# Prepare data for visualization
# Cropping code implemented here. Can specify how much to crop and along what axis
# Prepare data for visualization

half_x = data.shape[0] // 2
cropped_data = data[:half_x, :, :]
d2 = np.zeros(cropped_data.shape + (4,))
d2[..., 3] = cropped_data**1 * 255  # alpha
d2[..., 0] = d2[..., 3]  # red
d2[..., 1] = d2[..., 3]  # green
d2[..., 2] = d2[..., 3]  # blue

# (optional) RGB orientation lines
d2[:40, 0, 0] = [255, 0, 0, 255]
d2[0, :40, 0] = [0, 255, 0, 255]
d2[0, 0, :40] = [0, 0, 255, 255]
d2 = d2.astype(np.ubyte)

# =============================================================================
# Create qtgui
app = QtWidgets.QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 0, int(1080/2), int(1920/2))
w.setCameraPosition(distance=120, elevation=0, azimuth=0)
w.pan(0, 0, 10)
w.setWindowTitle(FILENAME)
w.show()

# glOptions are 'opaque', 'translucent' and 'additive'
v = gl.GLVolumeItem(d2, sliceDensity=6, smooth=False, glOptions=RENDER_TYPE)
v.translate(dx=-d2.shape[0]/2, dy=-d2.shape[1]/2, dz=-d2.shape[2]/3)
w.addItem(v)


# =============================================================================
def update_orbit():
    """Rotate camera orbit."""
    global counter
    counter += 1
    w.orbit(1, 0)  # degree


def stop_and_exit():
    """Stop and exit program."""
    app.quit()
    print("Finished")


# =============================================================================
if __name__ == '__main__':
    # Initiate timer
    timer1 = QtCore.QTimer()
    timer2 = QtCore.QTimer()
    counter = 0
    # Connect stuff
    timer1.timeout.connect(update_orbit)
    timer2.timeout.connect(stop_and_exit)

    # Start timer (everytime this time is up connects are excuted)
    NR_FRAMES = 360
    FRAMERATE = 1000 // 2  # ms, NOTE: keep it high to guarantee all frames  # ms, NOTE: keep it high to guarantee all frames
    timer1.start(FRAMERATE)
    timer2.start((NR_FRAMES * FRAMERATE) + 2000)

    # Start program
    QtWidgets.QApplication.instance().exec_()

</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84263d48602cf56fc760f8ea6dba77454cf7d8d6.jpeg" data-download-href="/uploads/short-url/iR2X7ENwe8MzPyQjOlsxMhgNuiG.jpeg?dl=1" title="vol1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84263d48602cf56fc760f8ea6dba77454cf7d8d6_2_690x372.jpeg" alt="vol1.PNG" data-base62-sha1="iR2X7ENwe8MzPyQjOlsxMhgNuiG" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84263d48602cf56fc760f8ea6dba77454cf7d8d6_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84263d48602cf56fc760f8ea6dba77454cf7d8d6_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84263d48602cf56fc760f8ea6dba77454cf7d8d6_2_1380x744.jpeg 2x" data-dominant-color="040404"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vol1.PNG</span><span class="informations">3779×2041 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81d557e9db203d13e1c1f19d6e3097ecda9b9613.jpeg" data-download-href="/uploads/short-url/iwyG9iYSu39E8eCZiyfd8DkMRR9.jpeg?dl=1" title="vol2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81d557e9db203d13e1c1f19d6e3097ecda9b9613_2_690x443.jpeg" alt="vol2.PNG" data-base62-sha1="iwyG9iYSu39E8eCZiyfd8DkMRR9" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81d557e9db203d13e1c1f19d6e3097ecda9b9613_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81d557e9db203d13e1c1f19d6e3097ecda9b9613_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81d557e9db203d13e1c1f19d6e3097ecda9b9613_2_1380x886.jpeg 2x" data-dominant-color="0E0E0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vol2.PNG</span><span class="informations">1566×1007 72.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2023-08-22 17:32 UTC)

<p>I got an image out of the MRHead.nrrd sample like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c728e6227740221cb4f0c298468c94466c011a09.jpeg" data-download-href="/uploads/short-url/spQDOMO5MJAyGWmBIORD2kdeoMF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c728e6227740221cb4f0c298468c94466c011a09_2_690x246.jpeg" alt="image" data-base62-sha1="spQDOMO5MJAyGWmBIORD2kdeoMF" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c728e6227740221cb4f0c298468c94466c011a09_2_690x246.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c728e6227740221cb4f0c298468c94466c011a09_2_1035x369.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c728e6227740221cb4f0c298468c94466c011a09.jpeg 2x" data-dominant-color="B6B7C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×478 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>otsu thresholding with the “foreground masking (BRAINS)” module to create a mask segmentation</li>
<li>apply mask to the volume from the segment editor, filling “-1” value in the region outside the segment</li>
<li>make the sagittal slice visible in 3D view set threshold so that -1 is not visible</li>
<li>enable volume rendering for the volume in the Volume Rendering module, and check “crop volume”</li>
<li>manually set the L-R crop range (seen in the screenshot) and the sagittal slice slider so that they roughly match</li>
</ul>
<p>Now if you want to vary the slice it is set to you have to manually match up the sagittal slice slider and the volume cropping slider, so maybe you can figure out some code to make one slider listen to the other or create a new slider that controls both at the same time.</p>

---

## Post #3 by @lassoan (2025-03-10 13:11 UTC)



---
