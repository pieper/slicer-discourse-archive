# Reading inputs and writing outputs in CLI module

**Topic ID**: 268
**Date**: 2017-05-04
**URL**: https://discourse.slicer.org/t/reading-inputs-and-writing-outputs-in-cli-module/268

---

## Post #1 by @f.cnunez (2017-05-04 20:18 UTC)

<p>Hi all,</p>
<p>I am doing a CLI module in which I am trying to pass the <code>.stl</code> chosen in a file browser, created with the <code>.xml</code> file.</p>
<p>In the <code>.cxx</code> file, I read the file chosen and the data is converted to polydata and then it’s added to a new <code>vtkMRMLModelNode</code>.</p>
<p>When I try to add the model to the current scene to see it in the 3D view, it doesn’t work. I would appreciate if anyone can help me. The code that I am using is the following:</p>
<pre><code class="lang-cpp">  std::string inputFilename = file1;
  
  vtkNew &lt; vtkMRMLScene&gt; Scene;

  vtkSmartPointer&lt; vtkSTLReader&gt; reader = vtkSmartPointer&lt; vtkSTLReader&gt;::New();
  reader-&gt;SetFileName(inputFilename.c_str());
  reader-&gt;Update();
  vtkPolyData* polyData = reader-&gt;GetOutput();

  vtkNew&lt; vtkMRMLModelNode&gt; modelNode;
  modelNode-&gt;SetAndObservePolyData(polyData);
  Scene-&gt;AddNode(modelNode.GetPointer());
  Scene-&gt;Import();
</code></pre>
<p>Thanks.</p>

---

## Post #2 by @cpinter (2017-05-04 20:24 UTC)

<p>You’ll need to create a display node as well if you want it to be shown.</p>
<p>Something like<br>
<code>modelNode-&gt;CreateDefaultDisplayNodes();</code></p>

---

## Post #3 by @lassoan (2017-05-04 23:19 UTC)

<p>You create a new scene in your CLI and put the node into that, but that scene is not related to the scene that the Slicer application uses.</p>
<p>If you generate one or a few models then specify them as output data, as it is done in the <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/GrayscaleModelMaker">Grayscale model maker module</a>.</p>
<p>If you generate many models (or you don’t know in advance how many models you’ll have in the output), then export it into a mini-scene as it is done in the <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/ModelMaker">ModelMaker module</a>.</p>

---

## Post #4 by @f.cnunez (2017-05-08 11:10 UTC)

<p>Hi Andras,</p>
<p>I’m trying to do it like the grayscale model maker but I can’t pass the polydata information of the .stl model file to the output node created with the output geometry. Also, the output geometry is created when I apply the CLI but it isn’t displayed at the scene and I don’t have a cursor to work with the output geometry model node created by default to pass the information to it. How can I pass the polydata of the model to the output geometry?</p>
<p>Thanks.</p>

---

## Post #5 by @lassoan (2017-05-08 12:49 UTC)

<aside class="quote no-group" data-username="f.cnunez" data-post="4" data-topic="268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/cc9497/48.png" class="avatar"> f.cnunez:</div>
<blockquote>
<p>I can’t pass the polydata information of the .stl model file to the output node created with the output geometry</p>
</blockquote>
</aside>
<p>What do you do? What do you expect to happen? What happens actually? Copy-paste the application log here (Help/Report a bug).</p>

---

## Post #6 by @f.cnunez (2017-05-08 20:08 UTC)

<p>I want to pass a .stl file choosing it in a file browser in the cli module, and put it in the scene for modifying its position with a transformation.I have two parameters in my xml file for doing it. I expect to add the path of the .stl file in the first parameter, create a new output geometry in the second and then, when I apply the module, have the .stl model chosen in my 3D view. Actually, when I press apply, the module return: “Status: Completed with errors” and the vtkmodelnode created with the output geometry label appears in the data module, but without any polydata and it can’t be visualized.</p>
<p>The parameters of the xml file are:</p>
<pre><code>&lt; file fileExtensions=".stl"&gt;
  &lt; longflag&gt;InputVolume&lt; /longflag&gt;
  &lt; description&gt;&lt; ![CDATA[fichero de entrada con el modelo de la camara]]&gt;&lt; /description&gt;
  &lt; label&gt;Camera model file&lt; /label&gt;
  &lt; channel&gt;input&lt; /channel&gt;
&lt; /file&gt;

 &lt;geometry type="model" reference="InputVolume"&gt;
  &lt;name&gt;OutputGeometry&lt;/name&gt;
  &lt;label&gt;Output Geometry&lt;/label&gt;
  &lt;channel&gt;output&lt;/channel&gt;
  &lt;index&gt;1&lt;/index&gt;
  &lt;description&gt;&lt;![CDATA[Output that contains geometry model.]]&gt;&lt;/description&gt;
 &lt;/geometry&gt;
</code></pre>
<p>and the code in the .cxx file is:</p>
<pre><code>int main(int argc, char * argv[])
{
  PARSE_ARGS;

  // vtk and helper variables
  vtkITKArchetypeImageSeriesReader* reader = NULL;
  vtkImageData *                    image;
  vtkXMLPolyDataWriter *            writer = NULL;

  // check for the input file
  // - strings that start with slicer: are shared memory references, so they won't exist.
  //   The memory address starts with 0x in linux but not on Windows
  if( InputVolume.find(std::string("slicer:") ) != 0 )
    {
    // check for the input file
    FILE * infile;
    infile = fopen(InputVolume.c_str(), "r");
    if( infile == NULL )
      {
      std::cerr &lt;&lt; "ERROR: cannot open input volume file " &lt;&lt; InputVolume &lt;&lt; endl;
      return EXIT_FAILURE;
      }
    fclose(infile);
    }

  // Read the file
  reader = vtkITKArchetypeImageSeriesScalarReader::New();
  reader-&gt;SetArchetype(InputVolume.c_str() );
  reader-&gt;SetOutputScalarTypeToNative();
  reader-&gt;SetDesiredCoordinateOrientationToNative();
  reader-&gt;SetUseNativeOriginOn();
  reader-&gt;Update();

  std::cout &lt;&lt; "Done reading the file " &lt;&lt; InputVolume &lt;&lt; endl;

  vtkImageChangeInformation *ici = vtkImageChangeInformation::New();
  ici-&gt;SetInputConnection(reader-&gt;GetOutputPort() );
  ici-&gt;SetOutputSpacing( 1, 1, 1 );
  ici-&gt;SetOutputOrigin( 0, 0, 0 );
  ici-&gt;Update();

  ici-&gt;Update();
  image = ici-&gt;GetOutput();

  writer = vtkXMLPolyDataWriter::New();
  writer-&gt;SetInputConnection(reader-&gt;GetOutputPort() );
  writer-&gt;SetFileName(OutputGeometry.c_str() );

  writer-&gt;Write();

// Cleanup
  if( reader )
    {
    reader-&gt;Delete();
    }
  if( ici )
    {
    ici-&gt;Delete();
    }
  if( transformIJKtoRAS )
    {
    transformIJKtoRAS-&gt;Delete();
    }
  if( mcubes )
    {
    mcubes-&gt;Delete();
    }
  if( decimator )
    {
    decimator-&gt;Delete();
    }
  if( reverser )
    {
    reverser-&gt;Delete();
    }
  if( smootherSinc )
    {
    smootherSinc-&gt;Delete();
    }
  if( transformer )
    {
    transformer-&gt;Delete();
    }
  if( normals )
    {
    normals-&gt;Delete();
    }
  if( stripper )
    {
    stripper-&gt;Delete();
    }
  if( writer )
    {
    writer-&gt;Delete();
    }
  return EXIT_SUCCESS;
}</code></pre>

---

## Post #7 by @lassoan (2017-05-09 03:46 UTC)

<p>Do you have volume input/output or is that only a mistake in the xml file (InputVolume) and in the cxx file (vtkITKArchetypeImageSeriesReader)?</p>
<p>Instead of <code>file</code> tag, use <code>geometry</code> for models (surface mesh) or <code>image</code> for volumes. If you use <code>file</code> then it means that the input is read from file (not from the scene) / result will be written to file (not loaded into the scene).</p>
<p>If you need to transform a mesh then it’s better to leave it to Slicer, as it can apply the transform to any loaded data types (volumes, models, markups, other transforms) dynamically. For that, have a <code>transform</code> output element. You can apply a transform by drag-and-dropping your model under the transform in the Data module (or in the Transforms module: select your transform node at the top, then use the <code>Apply transform</code> section to apply it to a node).</p>
<p>There are many registration methods already available in Slicer between images, models, points, etc. Have you checked if there is a similar module that does what you need? You could get started much more easily by modifying, improving an existing module.</p>

---

## Post #8 by @f.cnunez (2017-05-09 11:25 UTC)

<p>What I want to do in my module is to have an input model and an input transform. Choose them and, when I apply, see the transformed model in the scene, but I don’t find any module that makes it. After, I want to pass a transform from other software (ORBSLAM2) to move my model in real time.</p>

---

## Post #9 by @lassoan (2017-05-09 13:01 UTC)

<p>It’s very good to know what you actually want to achieve.</p>
<p>CLI modules are not ideal for real-time processing, as there is some overhead with writing/reading parameters and running the CLI module.</p>
<p>You could implement camera-based tracking in a loadable module more efficiently, because it has direct access to all objects in the application. However, we implement real-time imaging and tracking applications in Slicer using an external process that performs all the data acquisition from hardware and pre-processing (computing transforms, etc) and communicates with Slicer using <a href="http://www.openigtlink.org">OpenIGTLink protocol</a>.</p>
<p>You can either implement the separate application from scratch and link the very simple and small OpenIGTLink library to be able to send transforms to Slicer in real-time. Or, you can use an existing generic application, such as <a href="http://www.plustoolkit.org">Plus toolkit</a>, which can already connect to a wide range of cameras, other imaging and tracking devices, inertial measurement units, and other sensors, compute and combine transforms, calibrate and fuse data streams and send them to Slicer through OpenIGTLink. If you have transforms updating in real-time in Slicer then you can use the <a href="http://slicerigt.org/">SlicerIGT extension</a> to implement a complete surgical navigation or guidance system, without any additional programming (there are several <a href="http://www.slicerigt.org/wp/user-tutorial/">tutorials</a> on the SlicerIGT website that describe how to do this, with step-by-step instructions).</p>
<p>Probably the simplest way to get a complete RGBD-camera based guidance system is to add a new device class to the Plus toolkit that connects to a camera directly or uses output of a Plus camera device and computes transforms (see for example how our <a href="https://github.com/PlusToolkit/PlusLib/tree/master/src/PlusDataCollection/IntelRealSense">IntelRealSense based tracking device</a> works in Plus). Plus can take care of sending those transforms to Slicer, and SlicerIGT takes care of calibrating and visualizing tools and surfaces. This summer we’ll add better support in Plus for Intel RealSense RGBD cameras and will implement marker tracking (using OpenCV and probably ArUco). In the future, we will be interested in from surface-based tracking, so we would be happy to help you and see what you can get from ORB SLAM2.</p>
<p>Feel free to ask any Plus related questions on the Plus website and any Slicer or SlicerIGT related questions on this forum.</p>

---
