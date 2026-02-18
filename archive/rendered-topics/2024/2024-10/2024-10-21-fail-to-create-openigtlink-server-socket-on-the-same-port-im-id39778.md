# Fail to create OpenIGTLink server socket on the same port immediately after another server has just stopped

**Topic ID**: 39778
**Date**: 2024-10-21
**URL**: https://discourse.slicer.org/t/fail-to-create-openigtlink-server-socket-on-the-same-port-immediately-after-another-server-has-just-stopped/39778

---

## Post #1 by @Filippo_Parronchi (2024-10-21 16:34 UTC)

<p>Hello! I am establishing a connection between 3Dslicer (installed on my server) and Unity to render my volumes on an AR headset using the Open IGTLink communication protocol. My Python script is executed on the server via a service. The connection works correctly, and once I start my Python module through the service, I am able to correctly receive my volumes.</p>
<p>However, after receiving the first volume, I am unable to receive more immediately afterward because I get the error “Fail to create server socket!” (visible in Cmd). At that point, to make the module work, I have to stop the service running my Python script via cmd, wait for a variable amount of time in the order of ten seconds, and then restart the service with my module, which can then successfully establish the socket connection again.</p>
<p>The problem seems to be that there is a latency time and an inability to establish a connection once the previous one has ended. I do not need to interrupt the connection every time; I just need to ensure that each time I output a volume to a connectionNode and it is sent, it is then removed from the outputs so that I can send more.<br>
How can I keep my socket connection always open and working?<br>
Could you help me with my code?</p>
<p>Thanks</p>
<pre><code class="lang-auto">import sys
from multiprocessing.connection import Connection
import slicer
import os
from qt import QTimer

class SlicerListener:
    @staticmethod
    def CreateConnectionNode():
        connectionNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLIGTLConnectorNode", "connectionNode")
        connectionResult = connectionNode.SetTypeServer(18944)
        if connectionResult != 1:
            raise ValueError("Errore nella creazione del nodo di connessione.")

        return connectionNode

    @staticmethod
    def FormatFilePath(connectionNode):
        filePathNode = connectionNode.GetIncomingMRMLNode(0)
        if filePathNode.GetClassName() != "vtkMRMLTextNode":
            raise ValueError("Errore: il nodo ricevuto non è di tipo vtkMRMLTextNode.")
        filePath = filePathNode.GetText()
        windowsFilePath = filePath.replace('\\', '/')
        rawWindowsFilePath = r"{}".format(windowsFilePath)
        print(f"Percorso formattato: {rawWindowsFilePath}")
        #rawWindowsFilePath = r"C:\Users\Sara\Desktop\P9\F_A.001.DCM"
        return rawWindowsFilePath

    @staticmethod
    def LoadVolume(filePath):
        [success, volumeNode] = slicer.util.loadVolume(filePath, returnNode=True)
        if not success:
            raise ValueError(f"Errore nel caricamento del volume dal file: {filePath}")
        print(f"Volume caricato correttamente da: {filePath}")
        return volumeNode

    @staticmethod
    def LoadDatasetFromConnection(connectionNode):
        try:
            filePath = SlicerListener.FormatFilePath(connectionNode)
            volumeNode = SlicerListener.LoadVolume(filePath)
            return volumeNode
        except Exception as e:
            print(f"Errore Loading Dataset: {str(e)}")
            return None

    @staticmethod
    def CheckIncomingNodes(connectionNode, timer):
        if connectionNode.GetNumberOfIncomingMRMLNodes() &gt; 0:
            timer.stop()  # Ferma il timer una volta che il nodo è arrivato
            print("Nodo ricevuto, caricamento del volume...")

            # Carica il volume e continua il flusso principale
            volumeNode = SlicerListener.LoadDatasetFromConnection(connectionNode)
            #volumeRenderer = VolumeRenderer(volumeNode)
            #volumeRenderingDisplayNode = volumeRenderer.setupVolumeRendering()

            if volumeNode:
                slicerSender = SlicerSender(connectionNode, volumeNode)
                slicerSender.sendVolume()
            else:
                print("Errore nel caricamento del volume.")
        else:
            print("In attesa di nodi in arrivo...")

class SlicerSender:
    def __init__(self, connectionNode, volumeNode):
        self.connectionNode = connectionNode
        self.volumeNode = volumeNode

    def sendVolume(self):
        if not self.connectionNode:
            raise ValueError("Nessun nodo di connessione disponibile.")

        if not self.volumeNode:
            raise ValueError("Nessun nodo volume disponibile per l'invio.")

        success = self.connectionNode.RegisterOutgoingMRMLNode(self.volumeNode)

        if success:
            self.volumeNode.SetAttribute("OpenIGTLinkIF.pushOnConnect", "true")
            self.connectionNode.PushNode(self.volumeNode)
            self.connectionNode.UnregisterOutgoingMRMLNode(self.volumeNode)
            slicer.mrmlScene.RemoveNode(self.volumeNode)
            self.connectionNode.Stop()
            
            slicer.util.delayDisplay("Restarting connection node...", 60000)
            StartListeningWithConnectionNode(self.connectionNode)
        else:
            print(f"Errore nell'invio del volume '{self.volumeNode.GetName()}'.")

def StartListeningWithConnectionNode(connectionNode: 'vtkMRMLIGTLConnectorNode'):
    connectionNode.Start()
    timer = QTimer()
    timer.timeout.connect(lambda:SlicerListener.CheckIncomingNodes(connectionNode,timer))
    timer.start(3000)

def main():
    connectionNode = SlicerListener.CreateConnectionNode()
    StartListeningWithConnectionNode(connectionNode)

if __name__ == "__main__":
    main()
</code></pre>

---

## Post #2 by @lassoan (2024-10-21 20:16 UTC)

<p>It may take a while for the operating system to allow a port to be used again after a listening server is stopped. I would recommend to keep the socket server open.</p>

---
