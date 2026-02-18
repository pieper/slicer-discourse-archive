# How two stream 2 different threeD views (via Web Server)?

**Topic ID**: 37119
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/how-two-stream-2-different-threed-views-via-web-server/37119

---

## Post #1 by @thymallus (2024-07-01 12:22 UTC)

<p>Hi there!</p>
<p>I want to stream 2 different 3D views over a web server for a 3D (stereo) augmented reality application in Python. It already works for one 3D view.</p>
<p>How can I do this? Is there a better/faster way than using a web server?</p>
<p>thank you!</p>

---

## Post #2 by @pieper (2024-07-01 16:35 UTC)

<p>Right now the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-threed">threeD view endpoint</a> doesn’t take a view id parameter like the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-slice">slice view one does</a>, but this would be easy to extend if you wanted to.</p>
<p>In general though the web server isn’t going to be the highest performance option so you may want to explore something like the <a href="https://link.springer.com/article/10.1007/s11548-023-02977-0">hololens remoting system</a>.</p>

---

## Post #3 by @thymallus (2024-07-03 07:36 UTC)

<p>Thank You!</p>
<p>For a first proof of concept the plan was to go with the web server.</p>
<p>The docu says: “Get screenshot of the first 3D view <strong>after applying parameters</strong>.” Does "after applaying parameters mean “the active 3D view”?</p>
<p>if yes, i changed the active threeD view and verified the change with putting the following code in the console:</p>
<pre data-code-wrap="python"><code class="lang-python">layoutManager = slicer.app.layoutManager()
targetThreeDViewIndex = 2
targetThreeDWidget = layoutManager.threeDWidget(targetThreeDViewIndex)
targetThreeDViewNode = targetThreeDWidget.mrmlViewNode()
slicer.app.applicationLogic().GetSelectionNode().SetActiveViewID(targetThreeDViewNode.GetID())

slicer.app.applicationLogic().GetSelectionNode().GetActiveViewID()
</code></pre>
<p> → But the webserver delivers always the same threeD-view.</p>
<p>Why doesn’t it work?</p>

---

## Post #4 by @jcfr (2024-07-03 21:13 UTC)

<aside class="quote no-group" data-username="thymallus" data-post="3" data-topic="37119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> thymallus:</div>
<blockquote>
<p>Why doesn’t it work?</p>
</blockquote>
</aside>
<p>I think <a class="mention" href="/u/pieper">@pieper</a> comment above explains what you are observing:</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="37119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Right now the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-threed">threeD view endpoint </a> doesn’t take a view id parameter like the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-slice">slice view one does </a>, but this would be easy to extend if you wanted to.</p>
</blockquote>
</aside>
<p>To better understand, consider reviewing the implementation of the corresponding endpoint in <a href="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1009-L1077">Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1009-L1077</a></p>
<p>corresponding to the endpoint document at <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-threed">https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#get-threed</a></p>

---

## Post #5 by @pieper (2024-07-03 23:05 UTC)

<p>Yes, <a class="mention" href="/u/jcfr">@jcfr</a> is correct.</p>
<p>Interestingly, I see now that the <code>view</code> parameter is being parsed:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1017-L1020">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1017-L1020" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1017-L1020" target="_blank" rel="noopener">Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1017-L1020</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1017" style="counter-reset: li-counter 1016 ;">
          <li>try:</li>
          <li>    view = q["view"][0].strip().lower()</li>
          <li>except KeyError:</li>
          <li>    view = "1"</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But then later it’s not being used (<code>0</code> is hard coded):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1055">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1055" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1055" target="_blank" rel="noopener">Slicer/Slicer/blob/4c1546f620424a279d6d5daa973292ee2ae32d4f/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L1055</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1045" style="counter-reset: li-counter 1044 ;">
          <li>try:</li>
          <li>    orbitX = float(q["orbitX"][0].strip())</li>
          <li>except (KeyError, ValueError):</li>
          <li>    orbitX = None</li>
          <li>try:</li>
          <li>    orbitY = float(q["orbitY"][0].strip())</li>
          <li>except (KeyError, ValueError):</li>
          <li>    orbitY = None</li>
          <li></li>
          <li>layoutManager = slicer.app.layoutManager()</li>
          <li class="selected">view = layoutManager.threeDWidget(0).threeDView()</li>
          <li>view.renderEnabled = False</li>
          <li></li>
          <li>if lookFromAxis:</li>
          <li>    axes = ["None", "r", "l", "s", "i", "a", "p"]</li>
          <li>    try:</li>
          <li>        axis = axes.index(lookFromAxis[0].lower())</li>
          <li>        view.lookFromAxis(axis)</li>
          <li>    except ValueError:</li>
          <li>        pass</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So this would be an easy fix if someone wants to give it a try.</p>
<blockquote>
<p>Does "after applaying parameters mean “the active 3D view”?</p>
</blockquote>
<p>This means that any view options specified in the url parameters, like changing the view direction are applied before the screenshot is returned.</p>

---

## Post #6 by @thymallus (2024-08-06 12:17 UTC)

<p>Hi!</p>
<p>I have started to explore the hololens remoting system. In my opinion, it is too extensive for my requirements. I also do not have a Hololens and therefore it’s cumbersome for me to understand the code.</p>
<p>In principle, I just need to broadcast 2 different threeD views from 3D Slicer to an external python programme. I’ve sketched my setup in the following image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ac3fb421857181fc60e7ae82880af23dddabdec.jpeg" data-download-href="/uploads/short-url/hw28FhU2TWBzrQjJSOOC14Mdrha.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac3fb421857181fc60e7ae82880af23dddabdec_2_521x500.jpeg" alt="grafik" data-base62-sha1="hw28FhU2TWBzrQjJSOOC14Mdrha" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac3fb421857181fc60e7ae82880af23dddabdec_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac3fb421857181fc60e7ae82880af23dddabdec_2_781x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ac3fb421857181fc60e7ae82880af23dddabdec_2_1042x1000.jpeg 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1570×1504 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you have any tips on how to do this and get better performance than with the WebServer?</p>
<p>Thank you!</p>

---

## Post #7 by @pieper (2024-08-06 19:10 UTC)

<p>I would suggest you could start with the WebServer implementation and then optimize if it’s not fast enough.  On a local machine or local network it can provide images pretty quickly, although it depends on how big they are, etc.  Usually surgical microscope’s don’t move very quickly so it could be okay and is probably the easiest just to make the small fix suggested above.  If you do need to optimize then a dedicated connection you should first determine exactly what the bottlenecks are and what performance you actually need.</p>

---

## Post #8 by @thymallus (2024-08-07 07:14 UTC)

<p>Ok, thank you for your input!</p>

---

## Post #9 by @thymallus (2024-08-07 13:38 UTC)

<p>Hi,</p>
<p>The following code shows how the ThreeD View image is loaded into the external Python programme:</p>
<pre><code class="lang-auto">import cv2
import numpy as np
import urllib

def load_from_3DSlicer(url):
    # download the image, convert it to NumPy array, and decode it to OpenCV-format
    response = urllib.request.urlopen(url)
    image = np.asarray(bytearray(response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def main():
 
    img_url = "http://localhost:2016/slicer/threeD"  
    threeDslicer_img = load_from_3DSlicer(img_url)
    cv2.imshow('3D Slicer image 3D', threeDslicer_img)
    cv2.waitKey()
    
if __name__ == '__main__':
    main()
</code></pre>
<p>Is there a much faster/better approach in general? If yes, could you pls give me a hint?</p>
<p>The whole function “load_from_3DSlicer” takes about ~2.2s on the currently used computer, whereby 2.12s are taken from the line “response = urllib.request.urlopen(url)”.</p>
<p>thank you!</p>

---

## Post #10 by @thymallus (2024-08-08 09:29 UTC)

<p>Update:</p>
<p>I tried it now with asynchronous requests, e.g:</p>
<pre><code class="lang-auto">async def fetch_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            return content 

url = "http://localhost:2016/slicer/threeD"

loop = asyncio.get_event_loop()
image = loop.run_until_complete(fetch_image(url))
image = np.asarray(bytearray(image), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow('3D Slicer img Slice', image)
cv2.waitKey()
</code></pre>
<p>Works much faster, takes ~1/4 of the computation time.</p>

---

## Post #11 by @thymallus (2024-08-08 13:04 UTC)

<p>Now I’d like to switch between the threeD views (left and right camera) by passing a parameter to the function “threeD” in the SlicerRequestHandler.py of the WebServer module.</p>
<p>How is it possible to execute the “threeD” function via the 3D slicer Python console or via an external Python console?</p>

---

## Post #12 by @pieper (2024-08-08 13:13 UTC)

<aside class="quote no-group" data-username="thymallus" data-post="11" data-topic="37119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> thymallus:</div>
<blockquote>
<p>Now I’d like to switch between the threeD views (left and right camera) by passing a parameter to the function “threeD” in the SlicerRequestHandler.py of the WebServer module.</p>
</blockquote>
</aside>
<p>You just need to implement the fix described above (change the hard-coded 0 to use the view id).</p>
<aside class="quote no-group" data-username="thymallus" data-post="11" data-topic="37119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> thymallus:</div>
<blockquote>
<p>How is it possible to execute the “threeD” function via the 3D slicer Python console or via an external Python console?</p>
</blockquote>
</aside>
<p>Not sure what you are asking here.</p>

---

## Post #13 by @thymallus (2024-08-08 13:28 UTC)

<p>Yes, but I have to pass the information about which threeD view I want to receive into the threeD function. ?</p>
<p>For example:</p>
<p>threeD(self, request, view_idx = 0) → left virtual cam<br>
threeD(self, request, view_idx = 1) → right virtual cam</p>

---

## Post #14 by @pieper (2024-08-08 13:42 UTC)

<p>You would need to encode the view id as a url parameter.</p>

---

## Post #15 by @thymallus (2025-03-06 09:47 UTC)

<p>Hi,</p>
<p>how can i make sure that the view_indices correspond to the “3d-view-number” in 3D Slicer?</p>
<p>E.g. in the following image 3D view 1 is the left cam, 3D view 3 is the right cam:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78af79610c9fa0073b3db092e379aa4c6916c2a4.jpeg" data-download-href="/uploads/short-url/hdDfnxlDwZzdWJIyZdp5IvZeZnu.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af79610c9fa0073b3db092e379aa4c6916c2a4_2_690x459.jpeg" alt="grafik" data-base62-sha1="hdDfnxlDwZzdWJIyZdp5IvZeZnu" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af79610c9fa0073b3db092e379aa4c6916c2a4_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af79610c9fa0073b3db092e379aa4c6916c2a4_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78af79610c9fa0073b3db092e379aa4c6916c2a4_2_1380x918.jpeg 2x" data-dominant-color="CBC3BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1534×1021 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve adapted the SlicerRequestHandler to get left and right images in an external python programme:</p>
<pre><code>        def threeD(self, request, view_idx):
    """
    Handle requests with path: /threeD
    Return a png for a threeD view.
    """
    #print('HERE in threeD of SlicerRequestHandler')
    #print('view_idx = ' + str(view_idx))
    #print('request = ' + str(request))
    if request.decode('utf-8') == '/threeDL':
        view_idx = 0
    if request.decode('utf-8') == '/threeDR':
        view_idx = 2
    print('view_idx AFTER IF in threeDfunction = ' + str(view_idx))
</code></pre>
<p>But the images i receive are not view 1 and view 3 but view 1 and view 2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e54f3ef0817fbe734e457d55840bf7373322e9a.jpeg" data-download-href="/uploads/short-url/dsuTmiGk0PvNU10GZsdSIX5acs2.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e54f3ef0817fbe734e457d55840bf7373322e9a_2_690x269.jpeg" alt="grafik" data-base62-sha1="dsuTmiGk0PvNU10GZsdSIX5acs2" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e54f3ef0817fbe734e457d55840bf7373322e9a_2_690x269.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e54f3ef0817fbe734e457d55840bf7373322e9a_2_1035x403.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e54f3ef0817fbe734e457d55840bf7373322e9a_2_1380x538.jpeg 2x" data-dominant-color="B2A4A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1920×751 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems to me that Slicer assigns view indices to the 3D views in a seemingly random manner—or at least, I have yet to understand the underlying logic. Additionally, the view indices of the 3D views keep changing, if Slicer is restarted.</p>
<p>How can i solve this problem?</p>
<p>Thank you and best regards,<br>
Stefan</p>

---

## Post #16 by @thymallus (2025-03-06 13:01 UTC)

<p>…and one more question:</p>
<p>I would like to change the view angle of the viewpoint module from an external Python programme, depending on the zoom of the microscope… Is this possible? if so, how?</p>

---

## Post #17 by @pieper (2025-03-06 15:28 UTC)

<p>The threeDView index probably changes when the layout changes.  You could search for the <code>viewLabel</code> instead, like <code>lm.threeDWidget(0).viewLabel</code>.</p>
<p>You can change the view angle <a href="https://github.com/Slicer/Slicer/blob/49a251067d9b645bf35c445a7be6cf4a9cf039e9/Modules/Scripted/Endoscopy/Endoscopy.py#L338-L341">like this</a>.</p>

---
