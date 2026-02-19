---
topic_id: 13439
title: "Import Mesh Into Slicer Heart Device Simulator"
date: 2020-09-11
url: https://discourse.slicer.org/t/13439
---

# Import mesh into Slicer Heart device simulator

**Topic ID**: 13439
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/import-mesh-into-slicer-heart-device-simulator/13439

---

## Post #1 by @gabccamargo (2020-09-11 14:21 UTC)

<p>I use Slicer Heart to simulate transcatheter cardiac device implants. The custom device feature is great but limited. Is it possible to import a new mesh into Slicer Heart to be used as a new device? The deform feature and displacement mapping would work?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2020-09-11 14:23 UTC)

<p>You can add any device and deformation and displacement mapping works on your custom devices, too. In fact, we have created models for many other devices that will be publicly released when corresponding studies get published.</p>

---

## Post #3 by @gabccamargo (2020-09-11 19:53 UTC)

<p>Thanks for you fast response! Does slicer have an extension for importing meshes? Tried to import an stl file which worked ok, but I do not know how to create the handles and transforms for it and neither move them into Device Simulator… If advanced skills are necessary I might just have to wait for the new models…<br>
Thanks again!</p>

---

## Post #4 by @lassoan (2020-09-12 01:42 UTC)

<p>Complexity depends on the device and the kind of modeling you want to do.<br>
What kind of devices are you interested in?</p>

---

## Post #5 by @gabccamargo (2020-09-12 22:13 UTC)

<p>I am trying to simulate left atrial appendage closure with different devices (Amulet, Watchman, Watchman flex and LAmbre). Attempted to simulate the Amulet using two custom devices at the same time (image)  but deforming didn’t work for both…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1cf5e830fa240b819e71a61b1447af29a04d5d3.png" data-download-href="/uploads/short-url/wdBItfj2AuyFMa9SfBCCgPsALAv.png?dl=1" title="Captura de Tela 2020-09-12 às 19.06.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cf5e830fa240b819e71a61b1447af29a04d5d3_2_652x500.png" alt="Captura de Tela 2020-09-12 às 19.06.40" data-base62-sha1="wdBItfj2AuyFMa9SfBCCgPsALAv" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cf5e830fa240b819e71a61b1447af29a04d5d3_2_652x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cf5e830fa240b819e71a61b1447af29a04d5d3_2_978x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1cf5e830fa240b819e71a61b1447af29a04d5d3.png 2x" data-dominant-color="53526C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2020-09-12 às 19.06.40</span><span class="informations">1243×953 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-09-12 23:27 UTC)

<p>There are already a couple of devices that are similar to these devices, for example:</p>
<p>Amulet:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64e7360b3fb8edde3722d746da416d492f50bda5.jpeg" data-download-href="/uploads/short-url/eoD76nffvmlHBU7kBEYHYOu2NIF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64e7360b3fb8edde3722d746da416d492f50bda5_2_200x200.jpeg" alt="image" data-base62-sha1="eoD76nffvmlHBU7kBEYHYOu2NIF" width="200" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64e7360b3fb8edde3722d746da416d492f50bda5_2_200x200.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64e7360b3fb8edde3722d746da416d492f50bda5_2_300x300.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64e7360b3fb8edde3722d746da416d492f50bda5_2_400x400.jpeg 2x" data-dominant-color="C3C3D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2100×2100 1.4 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Duct occluder device in SlicerHeart’s Cardiac Device Simulator module is quite similar shape, and you can adjust dimensions using the sliders.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61999cbfdd6d64a2a2d51016d1645bd67491782c.jpeg" data-download-href="/uploads/short-url/dVpqvd2H7lDjgvyLvoxnMhz0Owk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61999cbfdd6d64a2a2d51016d1645bd67491782c_2_690x421.jpeg" alt="image" data-base62-sha1="dVpqvd2H7lDjgvyLvoxnMhz0Owk" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61999cbfdd6d64a2a2d51016d1645bd67491782c_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61999cbfdd6d64a2a2d51016d1645bd67491782c_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61999cbfdd6d64a2a2d51016d1645bd67491782c_2_1380x842.jpeg 2x" data-dominant-color="696867"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1379 531 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to adjust the range of the sliders or modify the shape of the device then you just need to change a few lines in <code>AsdVsdDevices/devices.py</code> file and restart Slicer.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/28ba86f8535508c926b2c2e23962af93b4bb1f30/AsdVsdDeviceSimulator/AsdVsdDevices/devices.py#L100-L142">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/28ba86f8535508c926b2c2e23962af93b4bb1f30/AsdVsdDeviceSimulator/AsdVsdDevices/devices.py#L100-L142" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/28ba86f8535508c926b2c2e23962af93b4bb1f30/AsdVsdDeviceSimulator/AsdVsdDevices/devices.py#L100-L142" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/28ba86f8535508c926b2c2e23962af93b4bb1f30/AsdVsdDeviceSimulator/AsdVsdDevices/devices.py#L100-L142</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="100" style="counter-reset: li-counter 99 ;">
          <li>class DuctOccluder(CardiacDeviceBase):</li>
          <li>
          </li>
<li>  NAME = "Duct Occluder"</li>
          <li>  ID = "DuctOccluder"</li>
          <li>  RESOURCES_PATH = os.path.join(os.path.dirname(__file__), "..",  "Resources")</li>
          <li>
          </li>
<li>  @classmethod</li>
          <li>  def getParameters(cls):</li>
          <li>    return {</li>
          <li>      'aortaDiameterMm': cls._genParameters("Aorta diameter", "Device diameter at descending aorta", 8, "mm", 5, 12, 1, 0),</li>
          <li>      'pulmonaryArteryDiameterMm': cls._genParameters("PA diameter", "Device diameter at pulmonary artery", 6, "mm", 4, 10, 1, 0),</li>
          <li>      'diameterMm': cls._genParameters("Retention skirt diameter", "Diameter of the retention skirt", 12, "mm", 9, 18, 1, 0),</li>
          <li>      'lengthMm': cls._genParameters("Device length", "Device length", 7, "mm", 5, 8, 1, 0)</li>
          <li>    }</li>
          <li>
          </li>
<li>  @classmethod</li>
          <li>  def getInternalParameters(cls):</li>
          <li>    return {'interpolationSmoothness': -0.70}</li>
          <li>
          </li>
<li>  @staticmethod</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/28ba86f8535508c926b2c2e23962af93b4bb1f30/AsdVsdDeviceSimulator/AsdVsdDevices/devices.py#L100-L142" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can find the location of this file in the Module finder (hit Ctrl+F or click the search icon on the toobar), type <code>ASD</code>, and you’ll see location at the bottom of the right panel.</p>

---

## Post #7 by @gabccamargo (2020-09-17 20:39 UTC)

<p>That was exactly what I was doing for the Amulet but with the custom device. A lot easier now with the increased thresholds for the PDA. Thanks!<br>
The shape generator file is also accessible? I was considering tweaking some device to get a more conical shape…</p>

---

## Post #8 by @gabccamargo (2020-09-17 21:11 UTC)

<p>Actually, I managed to simulate all devices using the Harmony TCPV without dimension constraints (Watchman attempt - image). If I could set each as new presets would be great for future use. Can it be done by editing some of the files?<br>
Thank you again for all the help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60698ecc5e870737d0d310e414609f1a13ac6e2e.png" data-download-href="/uploads/short-url/dKTZBR836jX2NLdEypJwahY8iRM.png?dl=1" title="Captura de Tela 2020-09-17 às 18.08.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60698ecc5e870737d0d310e414609f1a13ac6e2e_2_628x500.png" alt="Captura de Tela 2020-09-17 às 18.08.23" data-base62-sha1="dKTZBR836jX2NLdEypJwahY8iRM" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60698ecc5e870737d0d310e414609f1a13ac6e2e_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60698ecc5e870737d0d310e414609f1a13ac6e2e_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60698ecc5e870737d0d310e414609f1a13ac6e2e.png 2x" data-dominant-color="55526B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2020-09-17 às 18.08.23</span><span class="informations">1200×955 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2020-09-17 21:23 UTC)

<p>Yes, all presets are stored as csv files in the module’s directory. Shapes are generated using Python script, so you can define arbitrary shapes with minimal effort.</p>

---
