# -*- mode: python -*-

block_cipher = None

a = Analysis(['pdfff/__main__.py'],
             pathex=['.'],
             datas=[ ('config.yml', '.'),
                     ('forms/J155 - Undertaking and Acceptance of Masters Directions.pdf', 'forms'),
                     ('forms/J190 - Acceptance of Trust as Executor.pdf', 'forms'),
                     ('forms/J192 - Next of Kin Affidavit.pdf', 'forms'),
                     ('forms/J243 - Estate Inventory.pdf', 'forms'),
                     ('forms/J294 - Death Notice.pdf', 'forms'),
                     ('forms/Marital Status Declaration.pdf', 'forms'),
                     ('forms/Nomination to Act as Executor or Masters Representative.pdf', 'forms'),
                     ('forms/Reporting Affidavit.pdf', 'forms'),
                     ('README.md', '.'),
                     ('LICENSE', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='pdfff',
          icon='',
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
               name='pdfff')
