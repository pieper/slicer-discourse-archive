---
topic_id: 31756
title: "How To Load The Image Streaming From Opencv To 2D View"
date: 2023-09-17
url: https://discourse.slicer.org/t/31756
---

# How to load the image streaming from opencv to 2D view

**Topic ID**: 31756
**Date**: 2023-09-17
**URL**: https://discourse.slicer.org/t/how-to-load-the-image-streaming-from-opencv-to-2d-view/31756

---

## Post #1 by @slicer365 (2023-09-17 07:27 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57bebfddc575d8c148f917178b7f163799c6a069.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57bebfddc575d8c148f917178b7f163799c6a069.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57bebfddc575d8c148f917178b7f163799c6a069.mp4</a>
    </video>
  </div><p></p>
<p>I write a script based on opencv pacakge to capture  the video streaming.</p>
<p>As is shown, now I want to show the image on the red slice view ,what should I do?</p>
<p>I know Plus can help,but that is not what I want on  my project.</p>
<pre><code class="lang-auto">def onCamera(self):
        with slicer.util.tryWithErrorDisplay("Failed to compute results.", waitCursor=True):
    
          if self.ui.camButton.text =="Start":
            self.ui.camButton.text = "Stop"
            self.timer.connect('timeout()', self.ImageShow)
            self.timer.start()
            self.cap = cv2.VideoCapture(0)
          
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
            
          else:
            self.ui.camButton.text = "Start"
            self.timer.stop()
            self.cap.release()
def ImageShow(self):
        try:
          if self.cap.isOpened() != 1:
           
            return
        
          ret, img = self.cap.read()
          cv2.imwrite('temp.jpg', img, [cv2.IMWRITE_PNG_BILEVEL, 0])
          Pic = qt.QPixmap('temp.jpg')
          self.ui.imageBox.setPixmap(Pic)
          self.ui.imageBox.setScaledContents(True) 
          
        except Exception as e:
          print('%s' % e)
          
</code></pre>

---

## Post #2 by @lassoan (2023-09-17 15:42 UTC)

<p>If you can capture the image into a numpy array then you can use that array to update a volume node. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">script repository</a>.</p>
<p>However, in general, I would recommend to acquire images, tracking data, and other sensor data in a separate process and stream it into Slicer using <a href="https://plustoolkit.github.io/">Plus toolkit</a>. This provides more flexibility in what devices you can use and where the data is acuired; and makes the application more responsive (as image acquisition does not block the main thread of the GUI application).</p>

---

## Post #3 by @slicer365 (2023-09-17 17:04 UTC)

<p>Thank you Mr Lasso!</p>
<p>I find this function:<br>
slicer.util.loadVolume(“temp.jpg”, {“singleFile”: False})</p>
<p>And I get the same result with slicer.util.addVolumeFromArray(img)</p>

---

## Post #4 by @lassoan (2023-09-17 18:53 UTC)

<p>The safest is to allocate an image of the required size and scalar type, then get it as a numpy array, and then copy the pixels from the numpy array that OpenCV provides.</p>
<p>It would be cleaner and would probably have perceivably better performance if you acquired the images in a separate process and streamed into Slicer using OpenIGTLink. If you don’t want to develop any code then you can use the Plus Toolkit. If you want to develop this yourself then you can write a short Python script that acquires the image using OpenCV and sends it using <a href="https://pypi.org/project/pyigtl/" class="inline-onebox">pyigtl · PyPI</a>.</p>

---
