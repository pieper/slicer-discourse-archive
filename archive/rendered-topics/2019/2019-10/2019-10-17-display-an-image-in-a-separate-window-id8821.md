# Display an image in a separate window

**Topic ID**: 8821
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/display-an-image-in-a-separate-window/8821

---

## Post #1 by @giovform (2019-10-17 19:34 UTC)

<p>Hello. I am trying to display a grayscale OpenCV image in separate window, but no success so far. The code I am executing is as follows and causes Slicer to crash:</p>
<pre><code>    height, width = image.shape
    qImg = qt.QImage(np.asarray(image), width, height, qt.QImage.Format_Grayscale8)
    pixmap = qt.QPixmap.fromImage(qImg)
    myLabel = qt.QLabel()
    myLabel.setPixmap(pixmap)
    myLabel.show()
</code></pre>
<p>Before this, I was successfully displaying the image using OpenCV imshow() method, but it also caused Slicer to crash when I tried to interact with it while maintaining the OpenCV window open.</p>
<p>Any suggestions? I am using Slicer 4.11.0-2019-09-01 r28473.</p>

---

## Post #2 by @lassoan (2019-10-17 20:39 UTC)

<p>You can show a proper image viewer outside the view layout as shown here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout</a></p>
<p>If you want to convert a numpy array to QImage then I would recommend to use qimage2ndarray package:</p>
<pre><code class="lang-auto">try:
    import qimage2ndarray
except ImportError:
    pip_install('qimage2ndarray')
    import qimage2ndarray

import numpy as np
image = np.fromfunction(lambda i, j: i + j, (100, 100), dtype='uint8')
qImg = qimage2ndarray.array2qimage(image, normalize=True)
pixmap = qt.QPixmap.fromImage(qImg)
myLabel = qt.QLabel()
myLabel.setPixmap(pixmap)
myLabel.show()
</code></pre>

---
