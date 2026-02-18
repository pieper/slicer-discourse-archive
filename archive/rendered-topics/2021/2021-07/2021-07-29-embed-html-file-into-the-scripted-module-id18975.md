# Embed html file into the scripted module

**Topic ID**: 18975
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/embed-html-file-into-the-scripted-module/18975

---

## Post #1 by @Hualin (2021-07-29 16:54 UTC)

<p>Operating system: Ubuntu18.04<br>
Slicer version: 4.13.0-2021-07-21 r3042 / 2a223c0</p>
<p>Hello，<br>
I am trying to generate a scripted module with embed html. Then I use webEngineView and set the webEngineView url to my html file. Since I want html js to interact with slicer, I use websockets to allow the two to interact, but whether I use multi-process or Cli Module to run websockets server, I can’t operate view node in Slicer. So, is there any good solution to implement the interaction between the embedded HTML components and the Slicer scene?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2021-07-29 22:07 UTC)

<p>Hi -</p>
<p>No need for a websocket, you can communicate directly from python to javascript or javascript to python using the <code>qSlicerWebWidget</code>.  See the test code linked below for examples.  It’s all asynchronous and smooth.</p>
<p>Here’s an example of some demo code that mixes a web graph with the segment editor.</p><div class="youtube-onebox lazy-video-container" data-video-id="Y4MyThyeIPs" data-video-title="MultidimensionalExplorer 2020 01 24 at 2 39 37 PM" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Y4MyThyeIPs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Y4MyThyeIPs/maxresdefault.jpg" title="MultidimensionalExplorer 2020 01 24 at 2 39 37 PM" width="" height="">
  </a>
</div>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerMultiMapper">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/9a3adc7be3479d7b00570853b471485b1ec421bca080c3a0b411c5fe3f0dab52/pieper/SlicerMultiMapper" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">GitHub - pieper/SlicerMultiMapper: Tools for creating parametric maps from...</a></h3>

  <p>Tools for creating parametric maps from multidimensional MRI - GitHub - pieper/SlicerMultiMapper: Tools for creating parametric maps from multidimensional MRI</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Applications/SlicerApp/Testing/Python/WebEngine.py#L130-L225">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Applications/SlicerApp/Testing/Python/WebEngine.py#L130-L225" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Applications/SlicerApp/Testing/Python/WebEngine.py#L130-L225" target="_blank" rel="noopener">Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Applications/SlicerApp/Testing/Python/WebEngine.py#L130-L225</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="130" style="counter-reset: li-counter 129 ;">
          <li>def onEvalResult(self, js, result):</li>
          <li>  if js == "valueFromSlicer;":</li>
          <li>    self.delayDisplay("Got Slicer result back from JavaScript")</li>
          <li>    self.gotResponse = True</li>
          <li>    if result == "42":</li>
          <li>      self.gotCorrectResponse = True</li>
          <li>      self.delayDisplay("Got the expected result back from JavaScript")</li>
          <li>  else:</li>
          <li>    self.delayDisplay("Got a result back from JavaScript")</li>
          <li>    print((js, result))</li>
          <li>
          <li>
          <li>def test_WebEngine1(self):</li>
          <li>  """ Testing WebEngine</li>
          <li>  """</li>
          <li>
          <li>  self.delayDisplay("Starting the test")</li>
          <li>
          <li>
          <li>  webWidget = slicer.qSlicerWebWidget()</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Applications/SlicerApp/Testing/Python/WebEngine.py#L130-L225" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you communicate via the web widget data is passed in ascii, which is usually fast enough but if it’s not you can communicate asynchronously by integrating the sockets with the Qt event loop using tools like the QSocketNotifier, which is used in <a href="https://github.com/pieper/SlicerWeb">the SlicerWeb code</a>.</p>

---

## Post #3 by @Hualin (2021-07-30 09:44 UTC)

<p>Thanks for the reply pieper.</p>
<p>It works for me. I use <code>qSlicerWebWidget</code> and set html like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerMultiMapper/blob/master/MultiMapper/MultiMapper.py#L383">
  <header class="source">

      <a href="https://github.com/pieper/SlicerMultiMapper/blob/master/MultiMapper/MultiMapper.py#L383" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerMultiMapper/blob/master/MultiMapper/MultiMapper.py#L383" target="_blank" rel="noopener nofollow ugc">pieper/SlicerMultiMapper/blob/master/MultiMapper/MultiMapper.py#L383</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="373" style="counter-reset: li-counter 372 ;">
          <li>dataToPlot = []</li>
          <li>for index in range(len(samples['dtd_covariance_FA'])):</li>
          <li>  indexData = {}</li>
          <li>  for key in self.arrays.keys():</li>
          <li>    scalarLabel = key[len('dtd_covariance_'):]</li>
          <li>    indexData[scalarLabel] = samples[key][index]</li>
          <li>  dataToPlot.append(indexData)</li>
          <li>
          </li>
<li>dataToPlotString = json.dumps(dataToPlot)</li>
          <li>
          </li>
<li class="selected">modulePath = os.path.dirname(slicer.modules.multimapper.path)</li>
          <li>resourceFilePath = os.path.join(modulePath, "Resources", "parallel-template.html")</li>
          <li>html = open(resourceFilePath).read().replace("%%dataToPlot%%", dataToPlotString)</li>
          <li>
          </li>
<li>self.webWidget = slicer.qSlicerWebWidget()</li>
          <li>self.webWidget.size = qt.QSize(1024,512)</li>
          <li>self.webWidget.setHtml(html)</li>
          <li>self.webWidget.show()</li>
          <li>
          </li>
<li>open('/tmp/data.html', 'w').write(html)</li>
          <li>
      </li>
</ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and in html, import the <a href="https://cdn.jsdelivr.net/npm/parcoord-es@2.2.10/dist/parcoords.standalone.js" rel="noopener nofollow ugc">js</a> to enable window.slicerPython,<br>
then I can use <code>window.slicerPython.evalPython</code> and <code>self.webWidget.evalJS</code> to communicate from python to javascript and javascript to python.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #4 by @lassoan (2021-07-31 22:08 UTC)

<p>Note that you can use JavaScript widgets via <a href="https://github.com/Slicer/SlicerJupyter/">Jupyter notebooks</a>. There are tons of reusable widgets for interactive plotting and many other purposes.</p>

---

## Post #5 by @Hualin (2021-08-13 02:48 UTC)

<p>So sorry, it’s no need to import the js file <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=10" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---
