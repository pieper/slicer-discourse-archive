---
topic_id: 7293
title: "Display Dicom Data Just Received By Websocket Connection"
date: 2019-06-24
url: https://discourse.slicer.org/t/7293
---

# Display Dicom data just received by websocket connection

**Topic ID**: 7293
**Date**: 2019-06-24
**URL**: https://discourse.slicer.org/t/display-dicom-data-just-received-by-websocket-connection/7293

---

## Post #1 by @rbahegne (2019-06-24 15:30 UTC)

<p>Hello, I’m rather new to Slicer. I just developed a loadable module in C++ that connect to a MRI using websocket and receive dicom image data. Now i just need to display those dicoms.</p>
<p>So correct me if i’m wrong, i need to :</p>
<p>-Create a Node (not sure which kind), fill it with some dicom data (for now i’ve QbyteArrays)</p>
<p>-Add the node to the MRML scene</p>
<p>-That it ?</p>
<p>Thank you for any hints and answers.</p>

---

## Post #2 by @lassoan (2019-06-25 12:06 UTC)

<p>You need to create a vtkMRMLScalarVolumeNode as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" rel="nofollow noopener">here</a>. I’m not sure how to set the pixel data in vtkImageData from a QByteArray but <a class="mention" href="/u/pieper">@pieper</a> did something similar in the past so maybe he can help.</p>
<p>A much simpler approach is to write the byte array to a file, create a text header file (e.g., a <a href="https://discourse.slicer.org/t/load-vol-file-into-3d-slicer-from-morita-machine/4815/5">NRRD image file header</a>) and read the header file into Slicer using <code>slicer.util.loadVolume("path/to/something.nhdr")</code>.</p>

---

## Post #3 by @pieper (2019-06-25 22:54 UTC)

<p>Here’s something similar.  It takes the contents of a nrrd as the body of an http POST and converts it into a volume node.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L748-L830" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L748-L830" target="_blank" rel="nofollow noopener">pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L748-L830</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="748" style="counter-reset: li-counter 747 ;">
<li>def postNRRD(self, volumeID, requestBody):</li>
<li>  """Convert a binary blob of nrrd data into a node in the scene.</li>
<li>  Overwrite volumeID if it exists, otherwise create new"""</li>
<li>
</li>
<li>  if requestBody[:4] != b"NRRD":</li>
<li>    self.logMessage('Cannot load non-nrrd file (magic is %s)' % requestBody[:4])</li>
<li>    return</li>
<li>
</li>
<li>  fields = {}</li>
<li>  endOfHeader = requestBody.find(b'\n\n') #TODO: could be \r\n</li>
<li>  header = requestBody[:endOfHeader]</li>
<li>  self.logMessage(header)</li>
<li>  for line in header.split(b'\n'):</li>
<li>    colonIndex = line.find(b':')</li>
<li>    if line[0] != '#' and colonIndex != -1:</li>
<li>      key = line[:colonIndex]</li>
<li>      value = line[colonIndex+2:]</li>
<li>      fields[key] = value</li>
<li>
</li>
<li>  if fields[b'type'] != b'short':</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py#L748-L830" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @rbahegne (2019-06-26 12:51 UTC)

<p>Thank you for your answer, i used dcmtk to get the pixel data from the dicom and copied it in the vtkImageData. I don’t know the use of DisplayNodes but i get “vtkMRMLScalarVolumeNode::CreateDefaultDisplayNodes failed: scene is invalid” when i try to create one.</p>
<p>But the major problem is that slicer crash when i try to add a new Node to the scene. So it may be related to fact that the scene is invalid but i don’t know why it is that way, it is the only time interact with the scene.</p>
<p>I work on Ubuntu using QtCreator<br>
Here is part of my code :</p>
<pre><code class="lang-auto">vtkNew&lt;vtkMRMLScalarVolumeNode&gt; dicomNode;
 
vtkSmartPointer&lt;vtkImageData&gt; imageData =  vkSmartPointer&lt;vtkImageData&gt;::New();
imageData-&gt;SetOrigin(0.0,0.0,0.0);
imageData-&gt;SetSpacing(2.34375,2.34375,2.34375);
imageData-&gt;SetDimensions(583,583,1);
imageData-&gt;AllocateScalars(VTK_TYPE_UINT16,1);
if( dcmImage != nullptr )
          {
              if( dcmImage-&gt;getStatus() == EIS_Normal )
              {
                  
                 if( dcmImage-&gt;getOutputData(16) != nullptr )
                  {
                      // we copy the data in the dcmtk buffer to the vtkImageData one
                      memcpy((unsigned short *)imageData-&gt;GetScalarPointer(), (unsigned short *)dcmImage-&gt;getOutputData(16), dcmImage-&gt;getOutputDataSize() );
                      dcmImage-&gt;deleteOutputData();
                      imageData-&gt;Modified();                      
                  }
          }
  }
  dicomNode-&gt;CreateDefaultDisplayNodes();
  dicomNode-&gt;SetAndObserveImageData(imageData);
  this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLScalarVolumeNode", "dicomNode");
</code></pre>
<p>ImageData setting are hardcoded for know and are extracted from my dicom image test (DCM_PixelSpacing and DCM_WindowWidth) .</p>
<p>Any idea why i can’t add this node ?</p>

---

## Post #5 by @rbahegne (2019-06-26 13:46 UTC)

<p>I tried following the example to create an empty volume, but i got the same crash :</p>
<pre><code class="lang-auto">    vtkNew&lt;vtkMRMLScalarVolumeNode&gt; dicomNodeTest;
    vtkSmartPointer&lt;vtkImageData&gt; imageDataTest = vtkSmartPointer&lt;vtkImageData&gt;::New();
    imageDataTest-&gt;SetDimensions(512,512,512);
    imageDataTest-&gt;AllocateScalars(VTK_UNSIGNED_CHAR,1);

    vtkSmartPointer&lt;vtkImageThreshold&gt; imageThreshold = vtkSmartPointer&lt;vtkImageThreshold&gt;::New();
    imageThreshold-&gt;SetInputData(imageDataTest);
    imageThreshold-&gt;SetInValue(0);
    imageThreshold-&gt;SetOutValue(0);
    imageThreshold-&gt;Update();
    this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLScalarVolumeNode", "dicomNodeTest");
    dicomNodeTest-&gt;SetOrigin(0,0,0);
    dicomNodeTest-&gt;SetSpacing(1,1,1);
    dicomNodeTest-&gt;SetIToRASDirection(1,0,0);
    dicomNodeTest-&gt;SetJToRASDirection(0,1,0);
    dicomNodeTest-&gt;SetKToRASDirection(0,0,1);
    dicomNodeTest-&gt;SetAndObserveImageData(imageThreshold-&gt;GetOutput());
    dicomNodeTest-&gt;CreateDefaultDisplayNodes();
    dicomNodeTest-&gt;CreateDefaultStorageNode();
</code></pre>
<p>So I guess then that problem is not about the image data. I create this module using the extension wizard, and this code part is in the logic part derivated from vtkSlicerModuleLogic.</p>

---

## Post #6 by @pieper (2019-06-26 14:17 UTC)

<p>Are you running in a debugger so you can see where the crash happens?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions</a></p>

---

## Post #7 by @rbahegne (2019-06-26 15:10 UTC)

<p>So i attached gdb and here what i got :</p>
<blockquote>
<p>[New Thread 0x7f654bc10700 (LWP 11920)]<br>
[New Thread 0x7f654b40f700 (LWP 11921)]<br>
[New Thread 0x7f654ac0e700 (LWP 11925)]<br>
[New Thread 0x7f654a40d700 (LWP 11926)]<br>
[New Thread 0x7f6549c0c700 (LWP 11927)]<br>
[New Thread 0x7f654940b700 (LWP 11928)]<br>
[New Thread 0x7f6548c0a700 (LWP 11929)]<br>
[Thread 0x7f654a40d700 (LWP 11926) exited]<br>
[Thread 0x7f654ac0e700 (LWP 11925) exited]<br>
[Thread 0x7f6549c0c700 (LWP 11927) exited]<br>
[Thread 0x7f654940b700 (LWP 11928) exited]<br>
[Thread 0x7f6548c0a700 (LWP 11929) exited]</p>
<p>Thread 12 “SlicerApp-real” received signal SIGSEGV, Segmentation fault.<br>
[Switching to Thread 0x7f654b40f700 (LWP 11921)]<br>
0x00007f665d3f264d in std::vector&lt;vtkMRMLNode*, std::allocator&lt;vtkMRMLNode*&gt; &gt;::size (this=0x178)<br>
at /usr/include/c++/7/bits/stl_vector.h:671<br>
671	      { return size_type(this-&gt;_M_impl._M_finish - this-&gt;_M_impl._M_start); }</p>
</blockquote>

---

## Post #8 by @pieper (2019-06-26 15:32 UTC)

<p>Hard to tell just from that, but if you single step through and check the stack trace you should be able to track which statement leads to the crash.</p>

---

## Post #9 by @rbahegne (2019-06-26 15:46 UTC)

<p>Here the end of the backTrace, seems that CreateNodeByClass try to allocate the node and somehow fail.</p>
<blockquote>
<p><span class="hashtag-raw">#0</span>  0x00007fc42a29464d in std::vector&lt;vtkMRMLNode*, std::allocator&lt;vtkMRMLNode*&gt; &gt;::size() const (this=0x178)<br>
at /usr/include/c++/7/bits/stl_vector.h:671<br>
<span class="hashtag-raw">#1</span>  0x00007fc41a717965 in vtkMRMLScene::CreateNodeByClass(char const*) (this=0x0, className=0x7fc30c2bb9b0 “vtkMRMLScalarVolumeNode”)<br>
at /home/raphaelbahegne/Dev/Slicer/Libs/MRML/Core/vtkMRMLScene.cxx:449<br>
<span class="hashtag-raw">#2</span>  0x00007fc41a71cf2e in vtkMRMLScene::AddNewNodeByClass(std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt;, std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt;) (this=0x0, className=“vtkMRMLScalarVolumeNode”, nodeBaseName=“dicomNodeTest”) at /home/raphaelbahegne/Dev/Slicer/Libs/MRML/Core/vtkMRMLScene.cxx:1275</p>
</blockquote>

---

## Post #10 by @rbahegne (2019-06-27 10:01 UTC)

<p>Well i tried this :</p>
<blockquote>
<p>vtkMRMLScene* scene = this-&gt;GetMRMLScene();<br>
if (!scene)<br>
{<br>
vtkErrorMacro(“RegisterNodes: Invalid MRML scene”);<br>
return false;<br>
}</p>
</blockquote>
<p>It’s quite simple in fact, it’s not adding node that crash. It’s just that the scene is null. But i don’t know why it is null.</p>

---

## Post #11 by @pieper (2019-06-27 11:15 UTC)

<p>Sounds like you are making progress.  Now that you have the debugger set up you can single step through one of the other loadable modules and see how it uses the scene and see why it’s different in your module.</p>

---

## Post #12 by @rbahegne (2019-06-27 13:35 UTC)

<p>Slicer can hold several mrml scene ? I was under the impression that there was only one scene and the link between modules and the scene was kinda automatic, am I wrong ?</p>

---

## Post #13 by @rbahegne (2019-06-28 15:53 UTC)

<p>OK mrml scene was not connected to the logic, i though automatic generation of the module had taken care of this but i was mistaken.</p>
<p>I fix this architecture problem and now i face a new one : I create the node with the correct imageData and then i get :</p>
<blockquote>
<p>HasItemAttribute: Failed to find subject hierarchy item by ID 94424278946520</p>
</blockquote>
<p>The node is created but when i try to look a it i get</p>
<blockquote>
<p>Input port 0 of algorithm vtkImageMapToWindowLevelColors(0x55914d195a70) has 0 connections but is not optional.</p>
<p>Input port 0 of algorithm vtkImageThreshold(0x55914d19d860) has 0 connections but is not optional.</p>
</blockquote>
<p>Any ideas ?</p>

---

## Post #14 by @lassoan (2019-06-28 16:01 UTC)

<p>There should be no need for low-level manipulation of scene, viewers, logic, etc. Creating  a volume node, setting the received vtkImageData into it, adding the volume node to the scene, and creating default display nodes should be enough.</p>

---

## Post #15 by @rbahegne (2019-07-01 07:46 UTC)

<p>Ok, well somehow the setup of the mrml scene is broken, when i try to CreateDefaultDisplayNodes i get :</p>
<blockquote>
<p>vtkMRMLScalarVolumeNode::CreateDefaultDisplayNodes failed: scene is invalid</p>
</blockquote>

---

## Post #16 by @lassoan (2019-07-01 12:44 UTC)

<p>You need to add volume node to MRML scene before calling <code>CreateDefaultDIsplayNodes()</code>.</p>

---

## Post #17 by @rbahegne (2019-07-01 12:44 UTC)

<p>Well it seems that the node just like the logic can’t find the scene by himself so i needed to do a</p>
<blockquote>
<p>dicomNode-&gt;SetScene(this-&gt;GetMRMLScene());<br>
this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, “dicomNode”);</p>
</blockquote>
<p>To be able to create a DisplayNode</p>
<p>BUT my journey is not finished yet because the created node is filled with just one black slice in I, J and K. First i thought my data were broken, then i tried to load dicoms the regular way and i got the same. Then i thought my module messed up something so i tried with a slicer 4.10.2 version freshly downloaded and i got the same with every dicom series i tried. I cross checked on a collegue computer and it worked on his machine (windows).</p>
<p>Here is my config :<br>
Ubuntu 18.04.2 LTS<br>
-Memory: 7,6 Gio<br>
-Proc : Intel® Core™ i5-8500 CPU @ 3.00GHz × 6<br>
-GPu : Intel® UHD Graphics 630 (Coffeelake 3x8 GT2)<br>
-GNOME : 3.28.2</p>
<ul>
<li>64-bit</li>
</ul>
<p>Do my setup miss something, is there a specific on Ubuntu ?</p>

---

## Post #18 by @lassoan (2019-07-01 12:52 UTC)

<p><code>node-&gt;SetScene(scene)</code> is an undocumented internal helper method. To add a node to a scene, use <code>scene-&gt;AddNode(node)</code> instead.</p>
<p>Do you see any error in the application log?<br>
Can you load sample data sets using Sample Data module?</p>

---

## Post #19 by @rbahegne (2019-07-01 13:07 UTC)

<p>Well i may miss something but if  i use scene-&gt;AddNode(node), then when I do node-&gt;GetDisplayNode, the function check this-&gt;GetScene and do not find a scene and throw the vtkMRMLScalarVolumeNode::CreateDefaultDisplayNodes failed: scene is invalid.</p>
<p>Sample data are working, seems to be only dicom not loading.</p>

---

## Post #20 by @lassoan (2019-07-01 13:17 UTC)

<p>After <code>scene-&gt;AddNode(node)</code> you need to call <code>node-&gt;CreateDefaultDisplayNodes()</code> to create display nodes. After that, <code>node-&gt;GetDisplayNode()</code> will return valid node.</p>

---

## Post #21 by @rbahegne (2019-07-01 13:23 UTC)

<p><code>node-&gt;CreateDefaultDisplayNodes()</code> does return “vtkMRMLScalarVolumeNode::CreateDefaultDisplayNodes failed: scene is invalid” as well if I don’t do a set scene.</p>
<p>But the maybe it’s connected to my issue about loading dicom. With a regular 4.10.2 slicer i’m not able to load a dicom series. It result in one black slice. Sample nrrd are working.</p>

---

## Post #22 by @rbahegne (2019-07-01 15:03 UTC)

<p>I can load a Dicom serie using the add Data function. But i can’t load it using the DCM database , i see the series in the database, i can check metadata, but i cant examine them (button does nothing) and i can’t load them either.</p>

---

## Post #23 by @pieper (2019-07-01 18:30 UTC)

<p>Are there errors in the log?</p>

---

## Post #24 by @rbahegne (2019-07-02 08:20 UTC)

<p>No, here is a log when i add a Dicom to DB and tried to examine it and load it :</p>
<blockquote>
<p>Session start time …: 2019-07-02 10:14:13</p>
<p>Slicer version …: 4.11.0-2019-05-21 (revision a3fce80) linux-amd64 - not installed release</p>
<p>Operating system …: Linux / 4.15.0-54-generic / <span class="hashtag-raw">#58-Ubuntu</span> SMP Mon Jun 24 10:55:24 UTC 2019 - 64-bit</p>
<p>Memory …: 7772 MB physical, 976 MB virtual</p>
<p>CPU …: GenuineIntel Intel(R) Core™ i5-8500 CPU @ 3.00GHz, 6 cores, 6 logical processors</p>
<p>VTK configuration …: OpenGL2 rendering, Sequential threading</p>
<p>Developer mode enabled …: yes</p>
<p>Prefer executable CLI …: yes</p>
<p>Additional module paths …: /home/raphaelbahegne/Dev/Repo/SiStream-Debug-Build/lib/Slicer-4.11/qt-scripted-modules, /home/raphaelbahegne/Dev/Repo/SiStream-Debug-Build/lib/Slicer-4.11/qt-loadable-modules, /home/raphaelbahegne/Dev/Repo/SiStream-Debug-Build/lib/Slicer-4.11/cli-modules</p>
<p>Scripted subject hierarchy plugin registered: Annotations</p>
<p>Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>Switch to module: “Welcome”</p>
<p>Switch to module: “DICOM”</p>
<p>TagCacheDatabase adding table</p>
<p>New patient inserted: 1</p>
<p>New patient inserted as : 1</p>
<p>Need to insert new study: “1.3.12.2.1107.5.2.18.42563.30000019012809010957000000004”</p>
<p>Study Added</p>
<p>Need to insert new series: “1.3.12.2.1107.5.2.18.42563.2019012916550569633133260.0.0.0”</p>
<p>Series Added</p>
<p>“DICOM indexer has successfully processed 30 files [0.46s]”</p>
<p>Imported a DICOM directory, checking for extensions</p>
<p>Imported a DICOM directory, checking for extensions</p>
</blockquote>

---

## Post #25 by @rbahegne (2019-07-02 08:54 UTC)

<p>A “restore default” in application setting solved my problem. I don’t know what caused thoses troubles.</p>
<p>I’m back to creating nodes.</p>

---

## Post #26 by @rbahegne (2019-07-04 08:16 UTC)

<p>Ok, i fixed my problem here part of my code if someone want to do same <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code>long int  val_long, width, height;
for (int sliceNum=0; sliceNum&lt;dcmImageList.count(); sliceNum++)
{
    DcmDataset *dataSet = dcmImageList[sliceNum].getDataset();
    if(  dataSet != nullptr )
    {
        vtkNew&lt;vtkMRMLScalarVolumeNode&gt; dicomNode;
        dataSet-&gt;findAndGetLongInt(DCM_Columns,val_long);
        width = val_long;
        dataSet-&gt;findAndGetLongInt(DCM_Rows,val_long);
        height = val_long;

        if (sliceNum==0) {
            imageData-&gt;SetDimensions(width, height, dcmImageList.count());
            imageData-&gt;AllocateScalars(VTK_UNSIGNED_SHORT,1);
        }

        const unsigned short *dicom_buf;
        dataSet-&gt;findAndGetUint16Array(DCM_PixelData, dicom_buf);

        E_TransferSyntax xfer = dataSet-&gt;getOriginalXfer();
        dataSet-&gt;chooseRepresentation(xfer, nullptr);
        DicomImage *di = new DicomImage(dataSet, xfer, 0);

        memcpy(imageData-&gt;GetScalarPointer(0,0,sliceNum), di-&gt;getOutputData(16), di-&gt;getOutputDataSize());
        imageData-&gt;Modified();
    }
    else
    {
        std::cout &lt;&lt; "-------------------empty image--------------------------------" &lt;&lt; std::endl;
    }
}
imageData-&gt;SetOrigin(0,0,0);

this-&gt;GetMRMLScene()-&gt;AddNode(dicomNode);
//this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLScalarVolumeNode", "dicomNode");
dicomNode-&gt;SetAndObserveImageData(imageData);
dicomNode-&gt;SetOrigin(197,192,-83);
dicomNode-&gt;SetSpacing(1.25,1.25,3.00);
dicomNode-&gt;SetIToRASDirection(-1,0,0);
dicomNode-&gt;SetJToRASDirection(0,-1,0);
dicomNode-&gt;SetKToRASDirection(0,0,1);
dicomNode-&gt;CreateDefaultDisplayNodes();
dicomNode-&gt;CreateDefaultStorageNode();
dicomNode-&gt;UpdateScene(this-&gt;GetMRMLScene()); 
</code></pre>
<p>(Some dicom infos are hardcoded at the moment)</p>
<p>Few observations :</p>
<ul>
<li>if i use AddNewNodeByClass instead of AddNode it throw “scene invalid” and it does not work</li>
<li>CreateDisplayDefaultNodes throw a warning :</li>
</ul>
<blockquote>
<p>Warning: In /home/raphaelbahegne/Dev/Slicer/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx, line 718<br>
vtkSubjectHierarchyItem (0x562fd3c5c650): FindChildByID: Item cache does not contain requested ID 140486651064064<br>
HasItemAttribute: Failed to find subject hierarchy item by ID 140486651064064</p>
</blockquote>
<p>But the image is displayed properly.</p>

---

## Post #27 by @lassoan (2019-07-04 13:05 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="26" data-topic="7293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>if i use AddNewNodeByClass instead of AddNode it throw “scene invalid” and it does not work</p>
</blockquote>
</aside>
<p><code>this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLScalarVolumeNode", "dicomNode")</code> creates a new node by the name “dicomnode”. The new node has nothing to do with the other node that you created previously. That previously created node is not added to the scene, that’s why you got the error that the scene was invalid.</p>
<p>You can use to use <code>scene-&gt;AddNewNodeByClass(...)</code> instead of <code>vtkNew&lt;...&gt; node; scene-&gt;AddNode(node)</code>. AddNewNodeByClass is simpler (just one method calls instead of two) and it creates the new node with default properties stored in the scene (for volume nodes there is not much to customize but for display or storage nodes the user may have set some non-default values).</p>
<aside class="quote no-group" data-username="rbahegne" data-post="26" data-topic="7293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>CreateDisplayDefaultNodes throw a warning</p>
</blockquote>
</aside>
<p>Most likely this warning is a false alarm. Do you use latest master version of Slicer?</p>

---

## Post #28 by @rbahegne (2019-07-04 13:27 UTC)

<p>It got the src and built slicer just 2 month ago, so it’s 4.11.0</p>
<p>Thanks a lot it becomes clearer, and clearer.</p>

---

## Post #29 by @rbahegne (2019-07-05 08:28 UTC)

<p>Ok i used  <code>AddNewNodeByClass</code> but it gives me a vtkMrmlNode not a Scalar volume one.</p>
<p>So it did a cast :</p>
<blockquote>
<p>vtkMRMLScalarVolumeNode <em>dicomNode = (vtkMRMLScalarVolumeNode</em>)scene-&gt;AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, “dicomNode”);</p>
</blockquote>
<p>But it seem a little bit brutal, is there a cleaner way ?</p>

---

## Post #30 by @lassoan (2019-07-05 12:23 UTC)

<p>You can use vtkMRMLScalarVolumeNode::SafeDownCast to retrieve a more specific pointer.</p>

---
