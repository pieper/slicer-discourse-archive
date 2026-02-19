---
topic_id: 32976
title: "Slicercat As Web Service"
date: 2023-11-23
url: https://discourse.slicer.org/t/32976
---

# SlicerCAT as web service

**Topic ID**: 32976
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/slicercat-as-web-service/32976

---

## Post #1 by @keri (2023-11-23 11:16 UTC)

<p>Hi,</p>
<p>I’m thinking about making a web service based on SlicerCAT.</p>
<p>That means SlicerCAT should be run as a backend and the frontend should control what is rendered in SlicerCAT and all the VTK interaction (same as we do it in Slicer like zooming, rotating etc using mouse or hotkeys).</p>
<p>Frontend should be implemented in browser. Maybe I could try using <a href="https://streamlit.io/" rel="noopener nofollow ugc">streamlit</a> for that.</p>
<p>I’ve tested Slicer Web Server. I think it is possible to add sliders, checkboxes and other GUI staff to control the scene.<br>
But I don’t know whether it is possible to keep VTK interactivity.</p>
<p>Maybe somebody has any suggestions?</p>

---

## Post #2 by @pieper (2023-11-23 13:45 UTC)

<p>Yes, the WebServer module is designed to support that architecture.</p>
<p>Since both Slicer and the web application are asynchronous you need to pay some attention to make sure, for example, that you don’t make too many requests from the web side before the Slicer side has processed the previous requests.</p>

---

## Post #3 by @keri (2023-11-23 15:02 UTC)

<p>Thank you for the hint!</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="32976">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Since both Slicer and the web application are asynchronous you need to pay some attention to make sure, for example, that you don’t make too many requests from the web side before the Slicer side has processed the previous requests.</p>
</blockquote>
</aside>
<p>Yes that is what I’m afraid of.</p>
<p>Let suppose on the front end we have VTK interactor (don’t yet how to implement it) i.e we can rotate the 3D view for example.<br>
For each small movement we will have a request I guess. May this be a problem of sending too much requests or rotating/zooming work fast enough in Slicer so there should not be such problem?</p>

---

## Post #4 by @pieper (2023-11-24 15:26 UTC)

<p>I don’t have a worked out example, but it should be possible to manage things so that new requests are compacted so the request rate is in sync with the response rate.  Such a system would need to be adaptive so that you get fast response on a local connection but gracefully degrade on remote connections.</p>
<p>Maybe you can try a simple scenario and let us know what your experience it.</p>

---

## Post #5 by @keri (2023-11-24 16:31 UTC)

<p>RIght. I should try a simple scenario first.</p>

---

## Post #6 by @keri (2024-02-09 09:45 UTC)

<p>It seems that <code>vtkWeb</code> is most suited for me as I would like to use client-server architecture for <a href="https://kitware.github.io/vtk-js/examples/RemoteView.html" rel="noopener nofollow ugc">remote view</a> without transferring the whole mesh to the client (it may be pretty big).</p>
<p>Were there any attempts to use Slicer 3D views as remote view with custom GUI on the client side (probably with <code>vtkWeb</code>)?</p>

---

## Post #7 by @pieper (2024-02-09 12:38 UTC)

<p>I haven’t tried that particular technical combination.  It would be great if you could try some experiments and let us know how it goes.</p>

---

## Post #8 by @keri (2024-02-19 12:24 UTC)

<p>I just made small experiments based on <a href="https://kitware.github.io/vtk-js/examples/RemoteView.html" rel="noopener nofollow ugc">example</a>.</p>
<p>To adjust a server I use Slicer Jupyter.<br>
In this example we will remotely render 3D scene.</p>
<p>Define a server subclass:</p>
<pre data-code-wrap="python"><code class="lang-python">r"""
    This module is a VTK Web server application.
    The following command line illustrates how to use it::

        $ vtkpython .../vtk_server.py

    Any VTK Web executable script comes with a set of standard arguments that
    can be overriden if need be::
        --host localhost
             Interface on which the HTTP server will listen.

        --port 8080
             Port number on which the HTTP server will listen.

        --content /path-to-web-content/
             Directory that you want to serve as static web content.
             By default, this variable is empty which means that we rely on another server
             to deliver the static content and the current process only focuses on the
             WebSocket connectivity of clients.

        --authKey wslink-secret
             Secret key that should be provided by the client to allow it to make any
             WebSocket communication. The client will assume if none is given that the
             server expects "wslink-secret" as the secret key.
"""

# import to process args
import sys
import os

import slicer

# import vtk modules.
import vtk
from vtk.web import protocols
from vtk.web import wslink as vtk_wslink
from wslink import server

# =============================================================================
# Create custom ServerProtocol class to handle clients requests
# =============================================================================


class _MyWebServer(vtk_wslink.ServerProtocol):

    # Application configuration
    view = None
    authKey = "wslink-secret"

    def initialize(self):
        global renderer, renderWindow, renderWindowInteractor, cone, mapper, actor

        # Bring used components
        self.registerVtkWebProtocol(protocols.vtkWebMouseHandler())
        self.registerVtkWebProtocol(protocols.vtkWebViewPort())
        self.registerVtkWebProtocol(protocols.vtkWebPublishImageDelivery(decode=False))
        self.registerVtkWebProtocol(protocols.vtkWebViewPortGeometryDelivery())

        # Update authentication key to use
        self.updateSecret(_MyWebServer.authKey)

        # tell the C++ web app to use no encoding.
        # ParaViewWebPublishImageDelivery must be set to decode=False to match.
        self.getApplication().SetImageEncoding(0)

        # Create default pipeline (Only once for all the session)
        if not _MyWebServer.view:
            # VTK Web application specific
            view = slicer.app.layoutManager().threeDWidget(0).threeDView()
            # Capture RGBA image
            renderWindow = view.renderWindow()
            _MyWebServer.view = renderWindow
            self.getApplication().GetObjectIdMap().SetActiveObject("VIEW", renderWindow)
</code></pre>
<p>start server:</p>
<pre data-code-wrap="python"><code class="lang-python">from wslink import websocket as wsl
from wslink import backends

import argparse
from dataclasses import dataclass


parser = argparse.ArgumentParser(
        description="VTK/Web Slicer 3D web-application")
# Add default arguments
server.add_arguments(parser)

# Extract arguments
args = parser.parse_args()
args.port = 1234

print(args)

server.start_webserver(options=args, protocol=_MyWebServer)
</code></pre>
<p>Go to this <a href="https://kitware.github.io/vtk-js/examples/RemoteView.html" rel="noopener nofollow ugc">page</a> or <a href="https://kitware.github.io/vtk-js/examples/RemoteView.html" rel="noopener nofollow ugc">full screen</a> and you should be able to see 3D view in web browser and be able to interact:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b590c885fea9750ceebc77b7116aca259fdecda3.jpeg" data-download-href="/uploads/short-url/pUcCnabVoOEgboChRtQ4ry5ZrOP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b590c885fea9750ceebc77b7116aca259fdecda3_2_690x349.jpeg" alt="image" data-base62-sha1="pUcCnabVoOEgboChRtQ4ry5ZrOP" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b590c885fea9750ceebc77b7116aca259fdecda3_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b590c885fea9750ceebc77b7116aca259fdecda3_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b590c885fea9750ceebc77b7116aca259fdecda3_2_1380x698.jpeg 2x" data-dominant-color="B9B0AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×971 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looks pretty promising but after some time of intercation (using different mouse keys) the rendering becomes very very slow. So further investigations needed.</p>

---
