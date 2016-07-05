# -*- mode: python -*-
def addMyDatas():
    import os
    extraDatas = []
    for file in os.listdir('src\\fgmk\\data'):
        extraDatas.append(('data\\'+file, 'src\\fgmk\\data\\' + file, 'DATA'))
    return extraDatas

block_cipher = None


a = Analysis(['fgmk'],
             pathex=['C:\\Python34\\fgmk','C:\\Python34\\fgmk\\src','C:\\Python34\\fgmk\\src\\fgmk'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


a.datas += addMyDatas()

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='fgmk',
          debug=False,
          strip=False,
          upx=True,
          console=False )

