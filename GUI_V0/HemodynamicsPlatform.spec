# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['HemodynamicsPlatform.py'],
             pathex=['F:\pyinstaller\Hedys\Hedys\GUI_V0'
             ],
             binaries=[("../Base/QSSFil/Ubuntu.qss","BaseResource"),
	  	   ("../Base/example/CFD_file_37.vtu","BaseResource"),
		   ("./ui/main.ui","ui"),
           ("./ui/BatchCoronaryFSI.ui","ui"),
           ("./ui/BatchPreProcessing.ui","ui"),
           ("./ui/BloodPressureAndHeartRate.ui","ui"),
           ("./ui/CenterlineExtraction.ui","ui"),
           ("./ui/CenterLineGeneration.ui","ui"),
           ("./ui/CenterlineXsec.ui","ui"),
           ("./ui/ConvertDatatype.ui","ui"),
           ("./ui/CPR_MPRGeneration.ui","ui"),
           ("./ui/DateOutput.ui","ui"),
           ("./ui/end_page.ui","ui"),
           ("./ui/face_and_boundaryconditions.ui","ui"),
           ("./ui/FAI_Image_Display.ui","ui"),
           ("./ui/FFRCalculation.ui","ui"),
           ("./ui/FilterMask.ui","ui"),
           ("./ui/Generate_InputFile.ui","ui"),
           ("./ui/LumenCorrect.ui","ui"),
           ("./ui/MaskCoordinate.ui","ui"),
           ("./ui/MaskDilation.ui","ui"),
           ("./ui/MaskShrinking.ui","ui"),
           ("./ui/Mesh.ui","ui"),
           ("./ui/MeshCut.ui","ui"),
           ("./ui/MeshFillGap.ui","ui"),
           ("./ui/MurraysLaw.ui","ui"),
           ("./ui/NodeMatching.ui","ui"),
           ("./ui/OneClickCFD.ui","ui"),
           ("./ui/OneClicked.ui","ui"),
           ("./ui/PeriluminalSegmentation.ui","ui"),
           ("./ui/Plot3DView.ui","ui"),
           ("./ui/PostProcessing.ui","ui"),
           ("./ui/PostProcessing_YC.ui","ui"),
           ("./ui/PostProcessingRadialDisplay.ui","ui"),
           ("./ui/PreProcessing.ui","ui"),
           ("./ui/ResultsMapping.ui","ui"),
           ("./ui/Savevtu.ui","ui"),
           ("./ui/SegmentationExtension.ui","ui"),
           ("./ui/SegmentationInformationExtraction.ui","ui"),
           ("./ui/Solver.ui","ui"),
           ("./ui/StackSegmentation.ui","ui"),
           ("./ui/StackSTL.ui","ui"),
           ("./ui/STLGeneration.ui","ui"),
           ("./ui/StraightCPRPointStats.ui","ui"),
           ("./ui/TissueElemAssign.ui","ui"),
           ("./ui/TissueSegmentationSmooth.ui","ui"),
           ("./ui/UpdateCenterlineJson.ui","ui"),
           ("./ui/VisualizationParaview.ui","ui"),
           ("./ui/VisualizationPyVista.ui","ui"),
           ("./ui/VTUDataExtraction.ui","ui"),
           ("./ui/XsetionOriVolume.ui","ui")
],
             datas=[],
             hiddenimports=["PySide2.QtXml",
             "QT_GUI",
             "vtkmodules",
             "vtkmodules.all",
             "vtkmodules.qt.QVTKRenderWindowInteractor",
             "vtkmodules.util",
             "vtkmodules.util.numpy_support",
             "vtkmodules.numpy_interface",
             "vtkmodules.numpy_interface.dataset_adapter",
             "sklearn.neighbors._partition_nodes"
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Hedys',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon="F:\pyinstaller\Hedys\HemodynamicsPlatform.ico" )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Hedys')