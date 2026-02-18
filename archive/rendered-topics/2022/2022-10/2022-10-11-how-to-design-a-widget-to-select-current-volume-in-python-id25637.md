# How to design a widget to select current volume in Python

**Topic ID**: 25637
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/how-to-design-a-widget-to-select-current-volume-in-python/25637

---

## Post #1 by @user4 (2022-10-11 05:30 UTC)

<p>Hi,all.<br>
Here I load three volumes in Slicer as follows,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aeae5109ac424a49639abed4d417a9a3a08fa0f.png" data-download-href="/uploads/short-url/3Q7FMNU0BqeNUM9cCHSJJOTGFMH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aeae5109ac424a49639abed4d417a9a3a08fa0f_2_690x425.png" alt="image" data-base62-sha1="3Q7FMNU0BqeNUM9cCHSJJOTGFMH" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aeae5109ac424a49639abed4d417a9a3a08fa0f_2_690x425.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1aeae5109ac424a49639abed4d417a9a3a08fa0f_2_1035x637.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aeae5109ac424a49639abed4d417a9a3a08fa0f.png 2x" data-dominant-color="F2F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1089×672 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to design a python script module in which there is a widget showing all the loaded volumes.When I select a particular volume,I can get its voxels and make some changes.</p>
<p>Thanks in advance for your help!</p>

---

## Post #2 by @jay1987 (2022-10-11 06:13 UTC)

<p>这个功能很简单<br>
首先使用<br>
volumeNodes = slicer.util.getNodesByClass(“vtkMRMLScalarVolumeNode”)<br>
可以获取到所有的Volume,然后用Combox显示出来<br>
点击的时候使用<br>
slicer.util.arrayFromVolume 可以获取到每一个体素里的值</p>

---

## Post #3 by @user4 (2022-10-11 06:41 UTC)

<p>谢谢兄弟，简单明了。<br>
那如果后续我又加了一个volume，Combox怎么更新名字呢</p>
<p>十分感谢。</p>

---

## Post #4 by @jay1987 (2022-10-11 07:37 UTC)

<p>监听Scene的NodeAdded事件,比如官网上的例子</p>
<p><span class="mention">@vtk.calldata_type</span>(vtk.VTK_OBJECT)<br>
def onNodeAdded(caller, event, calldata):<br>
node = calldata<br>
if isinstance(node, slicer.vtkMRMLVolumeNode):<br>
# Call showVolumeRendering using a timer instead of calling it directly<br>
# to allow the volume loading to fully complete.<br>
qt.QTimer.singleShot(0, lambda: showVolumeRendering(node))</p>

---

## Post #5 by @user4 (2022-10-11 08:03 UTC)

<p>这例子有点抽象 <img src="https://emoji.discourse-cdn.com/twitter/crying_cat_face.png?v=12" title=":crying_cat_face:" class="emoji" alt=":crying_cat_face:" loading="lazy" width="20" height="20"><br>
比如我有个类叫 <code>class xxxWidget</code> 和 <code>class xxxLogic</code></p>
<pre><code class="lang-auto">class xxxWidget:
  def setup(self):
    self.volume_choice_box = qt.QComboBox()
    # 这里怎么监听Scene，将新的volume名字填入到???
    self.volume_choice_box.addItems(['???'])
</code></pre>

---

## Post #6 by @jay1987 (2022-10-11 08:06 UTC)

<p>您可以先了解一下Slicer的事件系统,特别是NodeAdded事件的监听,这个对你后面的Slicer编程有很大的帮助</p>

---

## Post #7 by @user4 (2022-10-11 08:12 UTC)

<p>好的，我会去官网看看例子，多谢指教。<br>
<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @cpinter (2022-10-11 18:39 UTC)

<p>It would be more inclusive if all conversation happened in English. My native language is not English either (and I’d venture that it’s true for the majority of the forum users), but we always write in English so any conversation is potentially useful to the whole community. Bottom line: please stick to English. Thanks.</p>

---
