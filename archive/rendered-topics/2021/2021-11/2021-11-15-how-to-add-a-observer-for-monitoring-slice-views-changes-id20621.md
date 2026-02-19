---
topic_id: 20621
title: "How To Add A Observer For Monitoring Slice Views Changes"
date: 2021-11-15
url: https://discourse.slicer.org/t/20621
---

# How to add a observer for monitoring slice views changes?

**Topic ID**: 20621
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/how-to-add-a-observer-for-monitoring-slice-views-changes/20621

---

## Post #1 by @Luke199208 (2021-11-15 07:39 UTC)

<p>system: Windows 10<br>
Slicer-version: 4.10.0<br>
Hello,<br>
I am trying to add a observer to monitor  the number of slice views changes. But the right way was not found. Which node and event should be used ?<br>
Slice views changes like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f21fc96db99a51a040d199cc5c49afe98292bb57.png" data-download-href="/uploads/short-url/yxVElKnPPP12dRfmw1jYZrzqSWP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f21fc96db99a51a040d199cc5c49afe98292bb57_2_690x336.png" alt="image" data-base62-sha1="yxVElKnPPP12dRfmw1jYZrzqSWP" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f21fc96db99a51a040d199cc5c49afe98292bb57_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f21fc96db99a51a040d199cc5c49afe98292bb57.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f21fc96db99a51a040d199cc5c49afe98292bb57.png 2x" data-dominant-color="100908"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">839×409 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
– to →   <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe0cb42143ff6b9f62779f147a1a57da8f9cd47.png" data-download-href="/uploads/short-url/tEYse0CzIIXTK2BGEJdEMCBPCbd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe0cb42143ff6b9f62779f147a1a57da8f9cd47_2_690x327.png" alt="image" data-base62-sha1="tEYse0CzIIXTK2BGEJdEMCBPCbd" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe0cb42143ff6b9f62779f147a1a57da8f9cd47_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe0cb42143ff6b9f62779f147a1a57da8f9cd47.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe0cb42143ff6b9f62779f147a1a57da8f9cd47.png 2x" data-dominant-color="050302"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">848×403 5.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to trigger my own method after the event has occurred.</p>
<p>Here is the method of  slice views changes:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
      customLayout = """
                &lt;layout type="vertical"&gt;
                &lt;item&gt;
                &lt;layout type="horizontal"&gt;
                  &lt;item splitSize="300"&gt;
                  &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
                    &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                    &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                    &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                  &lt;/view&gt;
                  &lt;/item&gt;
                  &lt;item splitSize="300"&gt;
                  &lt;view class="vtkMRMLSliceNode" singletontag="Red1"&gt;
                    &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                    &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                    &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                  &lt;/view&gt;
                  &lt;/item&gt;
                &lt;/layout&gt;
                &lt;/item&gt;
                &lt;item&gt;
                &lt;layout type="horizontal"&gt;
                  &lt;item splitSize="300"&gt;
                    &lt;view class="vtkMRMLSliceNode" singletontag="Red2"&gt;
                        &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                        &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                        &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                    &lt;/view&gt;
                  &lt;/item&gt;
                  &lt;item splitSize="300"&gt;
                    &lt;view class="vtkMRMLSliceNode" singletontag="Red3"&gt;
                        &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                        &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                        &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                    &lt;/view&gt;
                  &lt;/item&gt;
                &lt;/layout&gt;
                &lt;/item&gt;
                &lt;/layout&gt;
                """
      # Built-in layout IDs are all below 100, so you can choose any large random number
      # for your custom layout ID.
      customLayoutId = 503

      layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

      # Switch to the new custom layout
      layoutManager.setLayout(customLayoutId)
</code></pre>
<pre><code class="lang-auto">customLayout = """
                        &lt;layout type="horizontal"&gt;
                          &lt;item splitSize="500"&gt;
                          &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
                            &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                            &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                            &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                          &lt;/view&gt;
                          &lt;/item&gt;
                          &lt;item splitSize="500"&gt;
                          &lt;view class="vtkMRMLSliceNode" singletontag="Red1"&gt;
                            &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
                            &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
                            &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
                          &lt;/view&gt;
                          &lt;/item&gt;
                        &lt;/layout&gt;
                        """
      # Built-in layout IDs are all below 100, so you can choose any large random number
      # for your custom layout ID.
      customLayoutId = 502

      layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

      # Switch to the new custom layout
      layoutManager.setLayout(customLayoutId)
</code></pre>
<p>Thank you for your help!</p>

---

## Post #2 by @lassoan (2021-11-15 13:30 UTC)

<p>You can add an observer to <code>layoutManager.layoutLogic().GetLayoutNode()</code> to get notified about layout changes.</p>

---

## Post #3 by @Luke199208 (2021-11-16 02:25 UTC)

<p>Thank you so much for your support lassoan!<br>
I used the following method(<code>slicer.util.getNode("Layout").AddObserver(vtk.vtkCommand.ModifiedEvent, callbackFunc)</code>) to achieve what I want. But I don’t know if there will be other problems.</p>

---
