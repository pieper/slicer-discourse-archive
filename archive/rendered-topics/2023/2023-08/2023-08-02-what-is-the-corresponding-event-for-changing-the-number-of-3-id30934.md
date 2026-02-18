# What is the corresponding event for 'changing the number of 3D widget' in python script?

**Topic ID**: 30934
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/what-is-the-corresponding-event-for-changing-the-number-of-3d-widget-in-python-script/30934

---

## Post #1 by @Nick_Jo (2023-08-02 14:26 UTC)

<p>Hello. I’ve been using the SlicerCustomAppTemplate to customize the slicer based on our needs.</p>
<p>I want to apply the customization for ‘every’ 3D widget. I found the following code from the script repository.</p>
<pre><code class="lang-auto">viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()
viewNode.SetBoxVisible(False)                             #Hide the 3d cube

controller = slicer.app.layoutManager().threeDWidget(0).threeDController()
controller.setBlackBackground()                           #Set the background color to be black
</code></pre>
<p>The problem is that this only applies to a single 3D widget. That is, if I change the layout type to ‘Dual 3D’ or ‘tripled 3D’, my customization only applies to the widget index 0.</p>
<p>So I change the above code as follows.</p>
<pre><code class="lang-auto">  num_3d_widgets = slicer.app.layoutManager().threeDViewCount
  # print(f"The number of 3d widgets is: {num_3d_widgets}")

  for i in range(num_3d_widgets):
    viewNode = slicer.app.layoutManager().threeDWidget(i).mrmlViewNode()
    viewNode.SetBoxVisible(False)                         #Hide the 3d cube

    controller = slicer.app.layoutManager().threeDWidget(0).threeDController()
    controller.setBlackBackground()                       #Set the background black
</code></pre>
<p>But this still is not perfect, because that script is applied only once when the program starts.<br>
So, if I change the layout from single 3D widget to dual 3D widget, the customization for the second 3D widget is not applied.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92bb8584df83f342fe7bcaf02c0990408a60286.png" data-download-href="/uploads/short-url/o8ymsZVfEuKKNRuF1h7iaI6Nl1s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92bb8584df83f342fe7bcaf02c0990408a60286_2_690x461.png" alt="image" data-base62-sha1="o8ymsZVfEuKKNRuF1h7iaI6Nl1s" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92bb8584df83f342fe7bcaf02c0990408a60286_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92bb8584df83f342fe7bcaf02c0990408a60286_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a92bb8584df83f342fe7bcaf02c0990408a60286_2_1380x922.png 2x" data-dominant-color="2C2C38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1423×951 14.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I write the python script so that whenver the number of 3D widgets change, the above customization automatically applies to all 3D widgets?</p>
<p>I’ve been trying to find the proper event (such as slicer.vtkMRMLScene.NewSceneEvent) for this and the proper usage of slicer.mrmlScene.AddObserver, but this is pretty difficult to me. How should I handle this?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2023-08-02 14:27 UTC)

<p>You can define any layout you want (any number of any kind of views arranged in any way you prefer). See detailed instructions and examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">script repository</a>.</p>

---
