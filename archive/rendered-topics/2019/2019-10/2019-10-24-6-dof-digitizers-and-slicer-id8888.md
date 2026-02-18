# 6 DOF digitizers and Slicer

**Topic ID**: 8888
**Date**: 2019-10-24
**URL**: https://discourse.slicer.org/t/6-dof-digitizers-and-slicer/8888

---

## Post #1 by @muratmaga (2019-10-24 04:03 UTC)

<p>In the early days of 3D morphometrics, people used 3D digitizers like this (<a href="https://www.aniwaa.com/product/3d-scanners/microscribe-g2x/" rel="nofollow noopener">https://www.aniwaa.com/product/3d-scanners/microscribe-g2x/</a>) to collect 3D coordinates of landmarks directly from museum specimens. While things have shifted to surface or volumetric scanning, there is still some niche use cases where a digitizer may come in handy, if particularly we can collect data directly in Slicer.</p>
<p>I thought this might make an interesting student project, does anyone have any pointers about where to start? Can we use something like this in Slicer, and record points as fiducials (<a href="https://www.3dsystems.com/haptics-devices/touch/specifications" rel="nofollow noopener">https://www.3dsystems.com/haptics-devices/touch/specifications</a>)?</p>

---

## Post #2 by @lassoan (2019-10-24 13:58 UTC)

<p>Slicer can connect to such devices via <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">OpenIGTLink</a>.</p>
<p>We implemented OpenIGTLink interface to many position trackers, surface scanners, and imaging devices in <a>Plus toolkit</a>, but we did not encounter any applications that required mechanical 3D digitizers. As you said, 3D scanners are better solution for most use cases. The remaining few applications can be addressed by optical and electromagnetic trackers, which are less expensive and, more convenient to use, and similarly accurate.</p>
<p>I think the only remaining class of 3D digitizers that is still relevant today, is those that provide force feedback. These are used as haptic interface in robotics and simulation applications and since they are essentially small backdrivable robots, they are supported in robotics toolkits. For example, if you want to connect such a device to 3D Slicer then you can use <a href="https://github.com/jhu-cisst/cisst-saw" rel="nofollow noopener">CISST SAW</a> toolkit, which supports Novint Falcon, Sensable Phantom, MicroScribe, and a number of other sensors and robots and can stream real-time position information via OpenIGTLink.</p>

---

## Post #3 by @JBeninca (2023-10-28 11:44 UTC)

<p>Dear Andras:</p>
<p>i am using a MicroScriber to get anatomical data to be correlationated with some medical images.<br>
do you have an example to see how de MicroScriber pass the data to 3DSlicer?<br>
which is the IGTL module or the python script to do the work?<br>
Thanks</p>

---

## Post #4 by @lassoan (2023-10-28 12:53 UTC)

<p>We haven’t added support for mechanical digitizers in the PLUS toolkit, as most people now use optical trackers or surface scanners instead.</p>
<p>For example, you can get an Optitrack Duo optical tracker for $3000 and then you would not be constrained by mechanical links.</p>
<p>Are you using the Microscribe clinically?</p>

---

## Post #5 by @lassoan (2023-10-28 16:00 UTC)

<p>The Slicer side is easy, you just need to install thr OpenIGTLink extension and use OpenIGTLink IF module to set up the connection.</p>
<p>You need to build CISST for MicroScribe on your operating system. The CISST team at Johns Hopkins may be able to help if you run into trouble.</p>
<p>Overall, it is probably overall lower cost for you (if you consider your time as cost) to buy an Optitrack Duo for $3000. That is ready to use with PLUS toolkit on Windows. The user experience is also way better with an optical tracker, as you don’t need to struggle with mechanical joints and it is much easier to maintain sterility. Mechanical digitizers are not used clinically for patient registration for these reasons.</p>

---

## Post #6 by @muratmaga (2023-10-28 18:00 UTC)

<p><a class="mention" href="/u/jbeninca">@JBeninca</a></p>
<p>We tried the optitrack this summer, and it actually works quite well. It does take a few steps to set it up, and I find the motive software (digitizer’s own software that stream data to Slicer), a bit weird to setup.</p>
<p>A HS intern has written this brief tutorial, if it is of use to you. There are more involved tutorials in SlicerIGTLink by perklab</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/deringur/OpticalTrackingSystem#readme">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/deringur/OpticalTrackingSystem#readme" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/bd588bae20c0ddfdcd609cffebd3bab27b9c2dd76bd082a91f9925d557321c2d/deringur/OpticalTrackingSystem" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/deringur/OpticalTrackingSystem#readme" target="_blank" rel="noopener">GitHub - deringur/OpticalTrackingSystem</a></h3>

  <p>Contribute to deringur/OpticalTrackingSystem development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @JBeninca (2023-10-30 11:47 UTC)

<p>Hello Andras.<br>
We are using both an optical tracker (home-made with apriltags, stereo cam) and a Miscroscriber. You are right about your considerations on sterilization and the fact that the Scriber is IN the operating field but i do prefer the mechanical one.<br>
I was asking to use the MicroScriber with OpenIGTLink, if there is a simple connection with it.</p>

---
