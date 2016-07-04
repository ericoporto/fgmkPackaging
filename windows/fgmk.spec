# -*- mode: python -*-
def addMyDatas():
    import os
    extraDatas = []
    extraDatas.append(('src\\fgmk\\icon.png', 'src\\fgmk\\icon.png', 'DATA'))
    extraDatas.append(('src\\fgmk\\paletteDefault.json', 'src\\fgmk\\paletteDefault.json', 'DATA'))
    extraDatas.append(('src\\fgmk\\basegame.tar.gz', 'src\\fgmk\\basegame.tar.gz', 'DATA'))
    extraDatas.append(('src\\fgmk\\actions\\actionsList.json', 'src\\fgmk\\actions\\actionsList.json', 'DATA'))
    extraDatas.append(('src\\fgmk\\img\\tile.png', 'src\\fgmk\\img\\tile.png', 'DATA'))

    for file in os.listdir('src\\fgmk\\coreimg'):
        extraDatas.append(('src\\fgmk\\coreimg\\'+file, 'src\\fgmk\\coreimg\\' + file, 'DATA'))
    return extraDatas


block_cipher = None


a = Analysis(['fgmk'],
             pathex=['C:\\Python34\\fgmk','C:\\Python34\\fgmk\\src','C:\\Python34\\fgmk\\src\\fgmk'],
             binaries=[],
             datas=[],
             hiddenimports=['Pillow','numpy', 'fgmk'],
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
          exclude_binaries=True,
          name='fgmk',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='fgmk')
