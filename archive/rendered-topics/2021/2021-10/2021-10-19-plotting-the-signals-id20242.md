# Plotting the signals

**Topic ID**: 20242
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/plotting-the-signals/20242

---

## Post #1 by @wpgao (2021-10-19 15:11 UTC)

<p>Hi Guys,</p>
<p>Is it possible to plot the signals in Slicer? I had collected the signal with different length at different times. I  want to show these signals in one PlotView. I’m not sure whether PlotView support ‘subplot’ like in matplotlib. Or is there any other advices?<br>
Thanks a lot!</p>

---

## Post #2 by @PaoloZaffino (2021-10-19 15:16 UTC)

<p>I did something like this in the extension “SlicerArduinoController”.</p>
<p>You can give a look at this class:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py#L40">
  <header class="source">

      <a href="https://github.com/pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py#L40" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py#L40" target="_blank" rel="noopener nofollow ugc">pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py#L40</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="30" style="counter-reset: li-counter 29 ;">
          <li>    #EXAMPLE TO PRINT THE RECEIVED VALUE:</li>
          <li>    print("FIRED! %s" % (self.ArduinoNode.GetParameter("Data")))</li>
          <li>
          </li>
<li>  def sendDataToArduino(self, message):</li>
          <li>    messageSent = slicer.modules.arduinoconnect.widgetRepresentation().self().logic.sendMessage(message)</li>
          <li>
          </li>
<li>#</li>
          <li>#ArduinoPlotter</li>
          <li>#</li>
          <li>
          </li>
<li class="selected">class ArduinoPlotter():</li>
          <li>  def __init__(self, numberOfSamples):</li>
          <li>
          </li>
<li>    self.active = True</li>
          <li>
          </li>
<li>    self.ArduinoNode = slicer.mrmlScene.GetFirstNodeByName("arduinoNode")</li>
          <li>    sceneModifiedObserverTag = self.ArduinoNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.addPointToPlot)</li>
          <li>
          </li>
<li>    # Add data into table vtk</li>
          <li>    self.tableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")</li>
          <li>    self.tableNode.SetName("Arduino plotting table")</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Basically I receive the data on the serial port and then I plot the samples.</p>
<p>HTH</p>
<p>Paolo</p>

---

## Post #3 by @wpgao (2021-10-19 15:49 UTC)

<aside class="quote no-group" data-username="PaoloZaffino" data-post="2" data-topic="20242">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p>t and then I plot the samples.</p>
</blockquote>
</aside>
<p>Hi Paolo,</p>
<p>It’s a nice work! I wonder whether the plotview can show the signals from different channels. In your work, the signal from one channel can be plotted in the plotview. However, if there are signals from different channels, how to show these signals and respectively in one plotview?<br>
Thanks!</p>
<p>Wenpeng</p>

---

## Post #4 by @PaoloZaffino (2021-10-19 20:12 UTC)

<p>I think it is sufficient to have a table with a column for each channel you want to plot (in my case was just a channel).</p>
<p>The plot is linked to a table, so if you edit the table the plot will be updated accordingly.</p>

---

## Post #5 by @wpgao (2021-10-20 04:43 UTC)

<p>Agree. In my case, the signal from different channels should be shown separately, otherwise they will overlap. So I had to add an offset to the amplitude of different signal. The result is shown in <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c080d0d0432f093c5a9d7b235a14ad8d8735e54f.png" data-download-href="/uploads/short-url/rsXEXvL05sANRU4BUmiyiaVE62H.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c080d0d0432f093c5a9d7b235a14ad8d8735e54f_2_690x451.png" alt="screenshot" data-base62-sha1="rsXEXvL05sANRU4BUmiyiaVE62H" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c080d0d0432f093c5a9d7b235a14ad8d8735e54f_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c080d0d0432f093c5a9d7b235a14ad8d8735e54f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c080d0d0432f093c5a9d7b235a14ad8d8735e54f.png 2x" data-dominant-color="E0E2D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">698×457 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. I hope that the signal from each channel can be shown in one plotchart. However, plotview can only show one plotchart at the same time?<br>
So is there any other advices?<br>
Thanks!</p>

---

## Post #6 by @lassoan (2021-10-20 05:44 UTC)

<p>One plot view can only show one chart at a time but you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">show any number of plot views in a custom view layout</a>. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#hide-view-controller-bars">hide the controller bars</a> to keep all the plots close together.</p>

---

## Post #7 by @wpgao (2021-10-20 06:26 UTC)

<p>So the layout should be created dynamically, because the number of channels is unknown until the signal files are loaded. Therefore, the number of plot views is a parameter to create the customized layout, which is difficult to realize in this way (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>).</p>

---

## Post #8 by @lassoan (2021-10-20 06:31 UTC)

<p>No problem at all, you can change the layout anytime based on the number of channels you want to display. All you need is to generate the text description based on the number of channels, then update it in the layout node by calling <code>SetLayoutDescription</code> method.</p>

---

## Post #9 by @wpgao (2021-10-21 03:27 UTC)

<p>Hi Lassoan,</p>
<p>Slicer crashed, when I try to show the signal from different channel separately.<br>
Here is the code:</p>
<pre><code class="lang-auto">for channel in range(num):
        tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","Table{}".format(channel))
        table=tableNode.GetTable()
        table.Initialize()

        arrX=vtk.vtkFloatArray()
        arrX.SetName("Time(ms)")
        table.AddColumn(arrX)

        arrY=vtk.vtkFloatArray()
        name="{0} mm".format(self.logic.Data[channel].dist)
        arrY.SetName(name)
        table.AddColumn(arrY)

        table.SetNumberOfRows(maxNumOfPoints)

        for j in range(maxNumOfPoints):
            table.SetValue(j,0,j)
            if j&lt;self.logic.Data[channel].rawSignal.shape[0]:
                table.SetValue(j,1,self.logic.Data[channel].rawSignal[j])
            else:
                table.SetValue(j,1,0)

        table.Modified()

        name="{0} mm".format(self.logic.Data[channel].dist)
        plotSeriesNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode","Signal@{0}".format(name))
        plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
        plotSeriesNode.SetXColumnName("Time(ms)")
        plotSeriesNode.SetYColumnName(name)
        plotSeriesNode.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeLine)
        plotSeriesNode.SetUniqueColor()

        plotChartNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode","Chart@{0}".format(name))
        plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())
        plotChartNode.SetXAxisTitle('Time(ms)')
        plotChartNode.SetYAxisTitle('Voltage(uV)')
        plotChartNode.SetYAxisRangeAuto(True)
        plotChartNode.SetXAxisRangeAuto(True)

        plotWidget=self.layoutManager.plotWidget(channel)
        plotViewNode=plotWidget.mrmlPlotViewNode()
        plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
</code></pre>

---

## Post #10 by @lassoan (2021-10-21 03:34 UTC)

<p>Could you please provide an example that I can run as is?</p>
<p>Specify <code>num</code>, replace <code>self.logic.Data[channel].rawSignal[j]</code> with some hardcoded or random values, etc.</p>

---

## Post #11 by @wpgao (2021-10-21 05:22 UTC)

<p>Here are two functions implementation( PlotSignal and SetLayout)<br>
Slicer version: 4.11.20200930 r29402<br>
OS: unbuntu: 16.04</p>
<pre><code class="lang-auto">def PlotSignal(self):
 
    import math
    num=10
    self.SetLayout(num)

    maxNumOfPoints=100

    self.layoutManager=slicer.app.layoutManager()
    if self.layoutManager.plotViewCount!=num:
        print("Plot view number({}) is not equal to signal channel number({})".format(self.layoutManager.plotViewCount,num))
        return

    for channel in range(num):
        tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","Table{}".format(channel))
        table=tableNode.GetTable()
        table.Initialize()

        arrX=vtk.vtkFloatArray()
        arrX.SetName("Time(ms)")
        table.AddColumn(arrX)

        arrY=vtk.vtkFloatArray()
        name="{0} mm".format(channel)
        arrY.SetName(name)
        table.AddColumn(arrY)

        table.SetNumberOfRows(maxNumOfPoints)

        for j in range(maxNumOfPoints):
            print(j)
            table.SetValue(j,0,j)
            table.SetValue(j,1,math.sin(j))

        table.Modified()

        #Create two plot series nodes
        name="{0} mm".format(channel)
        plotSeriesNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode","Signal@{0}".format(name))
        plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
        plotSeriesNode.SetXColumnName("Time(ms)")
        plotSeriesNode.SetYColumnName(name)
        plotSeriesNode.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeLine)
        plotSeriesNode.SetUniqueColor()

        plotChartNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode","Chart@{0}".format(name))
        plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())
        plotChartNode.SetXAxisTitle('Time(ms)')
        plotChartNode.SetYAxisTitle('Voltage(uV)')
        plotChartNode.SetYAxisRangeAuto(True)
        plotChartNode.SetXAxisRangeAuto(True)

        plotWidget=self.layoutManager.plotWidget(channel)
        plotViewNode=plotWidget.mrmlPlotViewNode()
        plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
</code></pre>
<pre><code class="lang-auto">def SetLayout(self,nChannels):
    if self.setLayout is False:
        customLayout=(
        "&lt;layout type=\"horizontal\" split=\"true\"&gt;" 
            "&lt;item&gt;"
                "&lt;layout type=\"vertical\" split=\"true\"&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Axis&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Sagittal&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;Y&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#EDD54C&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                "&lt;/layout&gt;"
            "&lt;/item&gt;"
            "&lt;item&gt;"
                "&lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"
                    "&lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"
                "&lt;/view&gt;"
            "&lt;/item&gt;"
            "&lt;item&gt;"
                "&lt;layout type=\"vertical\" split=\"true\"&gt;")
        
        for i in range(nChannels):
            customLayout+='&lt;item&gt;&lt;view class="vtkMRMLPlotViewNode" singletontag="SignalView'+'-{}"'.format(i)+'&gt;'
            customLayout+='&lt;property name="viewlabel" action="default"&gt;'+'P{}'.format(i+1)+'&lt;/property&gt;'
            customLayout+='&lt;/view&gt;&lt;/item&gt;'

        customLayout+='&lt;/layout&gt;&lt;/item&gt;&lt;/layout&gt;'

        '''
        customLayout=(
        "&lt;layout type=\"horizontal\" split=\"true\"&gt;" 
            "&lt;item&gt;"
                "&lt;layout type=\"vertical\" split=\"true\"&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Axis&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Sagittal&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;Y&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#EDD54C&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                    "&lt;item&gt;"
                        "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;"
                            "&lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;"
                            "&lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;"
                            "&lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;"
                        "&lt;/view&gt;"
                    "&lt;/item&gt;"
                "&lt;/layout&gt;"
            "&lt;/item&gt;"
            "&lt;item&gt;"
                "&lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"
                    "&lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"
                "&lt;/view&gt;"
            "&lt;/item&gt;"
            "&lt;item&gt;"
                "&lt;layout type=\"horizontal\" split=\"true\"&gt;"
                    "&lt;view class=\"vtkMRMLPlotViewNode\" singletontag=\"MERView\"&gt;"
                        "&lt;property name=\"viewlabel\" action=\"default\"&gt;2&lt;/property&gt;"
                    "&lt;/view&gt;"
                "&lt;/layout&gt;"
            "&lt;/item&gt;"            
        "&lt;/layout&gt;")
        '''

        customLayoutId=501
        layoutManager=slicer.app.layoutManager()
        if not layoutManager.layoutLogic().GetLayoutNode().SetLayoutDescription(customLayoutId,customLayout):
            layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId,customLayout)
        layoutManager.setLayout(customLayoutId)

        for i in range(nChannels):
            layoutManager.plotWidget(i).plotController().setVisible(False)
</code></pre>

---

## Post #12 by @lassoan (2021-10-21 15:30 UTC)

<p>I could not reproduce any crash with the scripts above, so maybe the issue is how you fill the tables with real data. I’ve made a couple of fixes and improvement (fix order of views, fit plot to the view, adjust labeling, etc.) and this is the result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39.png" data-download-href="/uploads/short-url/boK3tawewWs5PBIRvUb4n4FZetj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39_2_690x420.png" alt="image" data-base62-sha1="boK3tawewWs5PBIRvUb4n4FZetj" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39_2_1380x840.png 2x" data-dominant-color="C7C7CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 421 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The updated code:</p>
<pre><code class="lang-python">def SetLayout(nChannels):
    customLayout=(
    "&lt;layout type=\"horizontal\" split=\"true\"&gt;" 
        "&lt;item&gt;"
            "&lt;layout type=\"vertical\" split=\"true\"&gt;"
                "&lt;item&gt;"
                    "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Red\"&gt;"
                        "&lt;property name=\"orientation\" action=\"default\"&gt;Axis&lt;/property&gt;"
                        "&lt;property name=\"viewlabel\" action=\"default\"&gt;R&lt;/property&gt;"
                        "&lt;property name=\"viewcolor\" action=\"default\"&gt;#F34A33&lt;/property&gt;"
                    "&lt;/view&gt;"
                "&lt;/item&gt;"
                "&lt;item&gt;"
                    "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Yellow\"&gt;"
                        "&lt;property name=\"orientation\" action=\"default\"&gt;Sagittal&lt;/property&gt;"
                        "&lt;property name=\"viewlabel\" action=\"default\"&gt;Y&lt;/property&gt;"
                        "&lt;property name=\"viewcolor\" action=\"default\"&gt;#EDD54C&lt;/property&gt;"
                    "&lt;/view&gt;"
                "&lt;/item&gt;"
                "&lt;item&gt;"
                    "&lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;"
                        "&lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;"
                        "&lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;"
                        "&lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;"
                    "&lt;/view&gt;"
                "&lt;/item&gt;"
            "&lt;/layout&gt;"
        "&lt;/item&gt;"
        "&lt;item&gt;"
            "&lt;view class=\"vtkMRMLViewNode\" singletontag=\"1\"&gt;"
                "&lt;property name=\"viewlabel\" action=\"default\"&gt;1&lt;/property&gt;"
            "&lt;/view&gt;"
        "&lt;/item&gt;"
        "&lt;item&gt;"
            "&lt;layout type=\"vertical\"&gt;")
    for i in range(nChannels):
        customLayout+='&lt;item&gt;&lt;view class="vtkMRMLPlotViewNode" singletontag="SignalView'+'-{}"'.format(i)+'&gt;'
        customLayout+='&lt;property name="viewlabel" action="default"&gt;'+'P{}'.format(i+1)+'&lt;/property&gt;'
        customLayout+='&lt;/view&gt;&lt;/item&gt;'
    customLayout+='&lt;/layout&gt;&lt;/item&gt;&lt;/layout&gt;'
    slicer.customLayout = customLayout
    customLayoutId=501
    layoutManager=slicer.app.layoutManager()
    if not layoutManager.layoutLogic().GetLayoutNode().SetLayoutDescription(customLayoutId,customLayout):
        layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId,customLayout)
    layoutManager.setLayout(customLayoutId)
    for i in range(nChannels):
        layoutManager.plotWidget(i).plotController().setVisible(False)

def PlotSignal():
    import math
    num=10
    SetLayout(num)
    maxNumOfPoints=100
    layoutManager=slicer.app.layoutManager()
    if layoutManager.plotViewCount!=num:
        print("Plot view number({}) is not equal to signal channel number({})".format(layoutManager.plotViewCount,num))
        return
    for channel in range(num):
        tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode","Table{}".format(channel))
        table=tableNode.GetTable()
        table.Initialize()
        arrX=vtk.vtkFloatArray()
        arrX.SetName("Time(ms)")
        table.AddColumn(arrX)
        arrY=vtk.vtkFloatArray()
        name="{0} mm".format(channel)
        arrY.SetName(name)
        table.AddColumn(arrY)
        table.SetNumberOfRows(maxNumOfPoints)
        for j in range(maxNumOfPoints):
            table.SetValue(j,0,j)
            table.SetValue(j,1,math.sin(j))
        table.Modified()
        #Create two plot series nodes
        name="{0} mm".format(channel)
        plotSeriesNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode","Signal@{0}".format(name))
        plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
        plotSeriesNode.SetXColumnName("Time(ms)")
        plotSeriesNode.SetYColumnName(name)
        plotSeriesNode.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeLine)
        plotSeriesNode.SetUniqueColor()
        plotChartNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode","Chart@{0}".format(name))
        plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())
        plotChartNode.SetXAxisTitle('') # 'Time(ms)'
        plotChartNode.SetYAxisTitle(f'uV @{name}')
        plotChartNode.SetAxisTitleFontSize(9)
        plotChartNode.SetAxisLabelFontSize(9)
        plotChartNode.SetYAxisRangeAuto(True)
        plotChartNode.SetXAxisRangeAuto(True)
        plotChartNode.SetLegendVisibility(False)
        plotViewNode=slicer.mrmlScene.GetSingletonNode(f'SignalView-{channel}','vtkMRMLPlotViewNode')
        plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
    for i in range(layoutManager.plotViewCount):
        layoutManager.plotWidget(i).plotView().fitToContent()

PlotSignal()
</code></pre>

---

## Post #13 by @wpgao (2021-10-22 14:37 UTC)

<p>Agree, I will check the data filled in the table.</p>
<p>Thanks so much!</p>

---

## Post #14 by @wpgao (2021-11-23 06:57 UTC)

<p>Hi Lasso,</p>
<p>The reason why the application crashed is that after setting the layout, the layout containing the plot views was collapsed in default. Then, I specified “splitSize” in “item” when defining the customLayout and the layout containing the plot views were shown and then the signal can be plotted successfully.</p>

---
