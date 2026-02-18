# Are there applications about GIS based on 3D Slicer?

**Topic ID**: 31733
**Date**: 2023-09-15
**URL**: https://discourse.slicer.org/t/are-there-applications-about-gis-based-on-3d-slicer/31733

---

## Post #1 by @iwangwangwang (2023-09-15 09:28 UTC)

<p>Are there applications about GIS based on 3D SLICER?</p>
<p>Can  3D SLICER be used to develop GIS applications?</p>

---

## Post #2 by @muratmaga (2023-09-15 17:53 UTC)

<p>I am not aware of any.</p>
<p>I also don’t think Slicer is the right choice for GIS. Most GIS data is inherently 2D (lat/long).  Even if you did manage to do something, you would have to code all the functionality yourself (e.g., different types of map projections).</p>
<p>There is already a very mature open-source GIS platform called GRASS. is there a reason you are not exploring that?</p>

---

## Post #3 by @lassoan (2023-09-16 19:32 UTC)

<p>There are some geo/mining applications, but mostly analysis of drilling cores and not geography mapping.</p>
<p>VTK - the library that Slicer is based on - contains lots of GIS features, including lots of projections, dynamic forward/inverse computations, texture mapping, etc. that would be all readily usable in Slicer. Still, due to the lack of experience of the Slicer community in this field and most of the funding focusing on clinical and biomedical applications you might find you need to develop some essential features on your own (or get funding for it).</p>
<p>You might want to ask <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>, who developed SlicerAstro - an edition of 3D Slicer for astronomy applications - about his experiences in using Slicer outside its main application area.</p>

---

## Post #4 by @Davide_Punzo (2023-09-16 23:02 UTC)

<p>The view factory can be used to fully customize the 2D slice view (e.g having lat-long coordinate axis, etc…) and the controller widgets (the buttons).</p>
<p>You can have a look at the code available in the astrovolume module in SlicerAstro extension (see below for links).</p>
<p>In my astronomical use case (HI 3D data cubes), each dataset was covering little portion of the sky. So I have applied coordinate transformation (in my case celestial wcs transformations) only for the calculation of 2d axis and for the data prode (i.e getting the lat-long at the ijk coordinate)</p>
<p>However, if the data extend on large range of lat and long you would need to apply the transforms also to the data (you could create a vtkTrasformSomething, if your non-linear transformation is not implemented in vtk/Slicer).</p>
<p>This is all doable, but you need to implement this in C++ and having some knowledge of Slicer infrastructure which is not super documented.</p>
<p>See</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeLayoutSliceViewFactory.cxx">
  <header class="source">

      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeLayoutSliceViewFactory.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeLayoutSliceViewFactory.cxx" target="_blank" rel="noopener nofollow ugc">Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeLayoutSliceViewFactory.cxx</a></h4>


      <pre><code class="lang-cxx">/*==============================================================================

  Copyright (c) Kapteyn Astronomical Institute
  University of Groningen, Groningen, Netherlands. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Davide Punzo, Kapteyn Astronomical Institute,
  and was supported through the European Research Council grant nr. 291531.

==============================================================================*/

// SlicerQt includes
</code></pre>



  This file has been truncated. <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeLayoutSliceViewFactory.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L402">
  <header class="source">

      <a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L402" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L402" target="_blank" rel="noopener nofollow ugc">Punzo/SlicerAstro/blob/master/AstroVolume/qSlicerAstroVolumeModule.cxx#L402</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="392" style="counter-reset: li-counter 391 ;">
          <li>/*qMRMLLayoutSliceViewFactory* mrmlSliceViewFactory =</li>
          <li>  qobject_cast&lt;qMRMLLayoutSliceViewFactory*&gt;(</li>
          <li>  d-&gt;app-&gt;layoutManager()-&gt;mrmlViewFactory("vtkMRMLSliceNode"));*/</li>
          <li></li>
          <li>qSlicerAstroVolumeLayoutSliceViewFactory* astroSliceViewFactory =</li>
          <li>  new qSlicerAstroVolumeLayoutSliceViewFactory(d-&gt;app-&gt;layoutManager());</li>
          <li></li>
          <li>//d-&gt;app-&gt;layoutManager()-&gt;unregisterViewFactory(mrmlSliceViewFactory);</li>
          <li>// TO DO: this should be disabled, but SlicerAstro with the last Slicer version (16/02/2021)</li>
          <li>// crash if the default slice view factory is disabled</li>
          <li class="selected">d-&gt;app-&gt;layoutManager()-&gt;registerViewFactory(astroSliceViewFactory);</li>
          <li></li>
          <li>// Modify orietation in default Layouts</li>
          <li>vtkMRMLLayoutNode* layoutNode =  vtkMRMLLayoutNode::SafeDownCast(</li>
          <li>  this-&gt;mrmlScene()-&gt;GetSingletonNode("vtkMRMLLayoutNode","vtkMRMLLayoutNode"));</li>
          <li>if(!layoutNode)</li>
          <li>  {</li>
          <li>  qCritical() &lt;&lt; "qSlicerAstroVolumeModule::setup() : layoutNode not found!";</li>
          <li>  return;</li>
          <li>  }</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There were actually some issues with the factory with recent Slicer version (not sure if they are still an issue), but unfortunately I never had the time to investigate/fix it.</p>
<p>Cheers,<br>
Davide.</p>

---

## Post #5 by @iwangwangwang (2023-09-17 06:48 UTC)

<p>I see, thank you very much</p>

---
