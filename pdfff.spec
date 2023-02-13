# -*- mode: python -*-

block_cipher = None


a = Analysis(['_main_.py.py'],
             pathex=['.'],
             datas=[ ('pdfff\config.yml', 'pdfff'),
                     ('forms\J155 - Undertaking and Acceptance of Masters Directions.pdf', '.'),
                     ('forms\J190 - Acceptance of Trust as Executor.pdf', '.'),
                     ('forms\J192 - Next of Kin Affidavit.pdf', '.'),
                     ('forms\J243 - Estate Inventory.pdf', '.'),
                     ('forms\J294 - Death Notice.pdf', '.'),
                     ('forms\Marital Status Declaration.pdf', '.'),
                     ('forms\Nomination to Act as Executor or Masters Representative.pdf', '.'),
                     ('forms\Reporting Affidavit.pdf', '.'),
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
