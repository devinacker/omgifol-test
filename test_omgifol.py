print('Omgifol Unit Tests')

import unittest, random
import omg, omg.colormap, omg.playpal, omg.txdef

from PIL import Image, ImageChops
import pdb

class OmgifolTest(unittest.TestCase):
    def setUp(self):
        self.wad = omg.WAD('test.wad')

    #
    # colormap
    #
    def test_colormap(self):
        testcol = self.wad.data['COLORMAP']
        col = omg.colormap.Colormap()
        col.from_lump(testcol)
        lump = col.to_lump()
        
        self.assertTrue(isinstance(lump, omg.Lump))
        # compare default constructed colormap against one from test.wad
        self.assertTrue(lump.data == testcol.data)
    
    def test_colormap_build(self):
        col = omg.colormap.Colormap()
        col.build_fade()
        col.build_invuln()
    
    #
    # graphic lumps
    #
    def test_graphic_copy(self):
        testgfx = self.wad.graphics['HELP1']
        copy = testgfx.copy()
        
        self.assertTrue(copy is not testgfx)
        self.assertTrue(copy.to_raw() == testgfx.to_raw())

    def test_graphic_attr(self):
        testgfx = self.wad.graphics['HELP1']
        testgfx.offsets = (25, 50)
        self.assertTrue(testgfx.x_offset == 25)
        self.assertTrue(testgfx.y_offset == 50)
        
        self.assertTrue(testgfx.dimensions == (320, 200))

    def test_graphic_raw(self):
        testgfx = self.wad.graphics['HELP1']
        test = omg.lump.Graphic()
        raw = testgfx.to_raw()
        
        test.from_raw(raw, *testgfx.dimensions)
        self.assertTrue(test.to_raw() == raw)
    
    def test_graphic_Image(self):
        testgfx = self.wad.graphics['HELP1']
        test = omg.lump.Graphic()
        image = testgfx.to_Image()
        
        # test without remapping palette (both images already use the same default palette)
        test.from_Image(image)
        new_image = test.to_Image()
        diff = ImageChops.difference(new_image, image).getbbox()
        self.assertTrue(diff is None)
        
        # test with palette mapping
        test.from_Image(image, translate=True)
        new_image = test.to_Image()
        diff = ImageChops.difference(new_image.convert("RGB"), image.convert("RGB")).getbbox()
        self.assertTrue(diff is None)

    #
    # maps
    #
    def test_map_counts(self):
        testmap = omg.mapedit.MapEditor(self.wad.maps['MAP01'])
        self.assertTrue(len(testmap.things) == 103)
        self.assertTrue(len(testmap.linedefs) == 653)
        self.assertTrue(len(testmap.sidedefs) == 958)
        self.assertTrue(len(testmap.vertexes) == 581)
        self.assertTrue(len(testmap.segs) == 1030)
        self.assertTrue(len(testmap.ssectors) == 268)
        self.assertTrue(len(testmap.nodes) == 267)
        self.assertTrue(len(testmap.sectors) == 130)

    def test_draw_simple_sector(self):
        mapedit = omg.mapedit.MapEditor()
        verts = []
        verts.append(omg.mapedit.Vertex(x=0,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=64))
        verts.append(omg.mapedit.Vertex(x=0,y=64))
        mapedit.draw_sector(verts)
        self.assertTrue(len(mapedit.vertexes) == 4)
        self.assertTrue(len(mapedit.linedefs) == 4)
        self.assertTrue(len(mapedit.sidedefs) == 4)
        self.assertTrue(len(mapedit.sectors) == 1)
        
    def test_draw_many_sectors(self):
        for x in range(100):
            mapedit = omg.mapedit.MapEditor()
            n = random.randint(4,20)
            verts = []
            for x in range(n):
                verts.append(omg.mapedit.Vertex(x=random.randint(-30000,30000),y=random.randint(-30000,30000)))
            mapedit.draw_sector(verts)
            self.assertTrue(len(mapedit.vertexes) == n)
            self.assertTrue(len(mapedit.linedefs) == n)
            self.assertTrue(len(mapedit.sidedefs) == n)
            self.assertTrue(len(mapedit.sectors) == 1)

    #
    # playpal
    #
    def test_playpal(self):
        testpal = self.wad.data['PLAYPAL']
        pal = omg.playpal.Playpal()
        pal.from_lump(testpal)
        lump = pal.to_lump()
        
        self.assertTrue(isinstance(lump, omg.Lump))
        # compare default constructed palette against one from test.wad
        self.assertTrue(lump.data == testpal.data)
    
    def test_playpal_build(self):
        pal = omg.playpal.Playpal()
        pal.build_defaults()

    #
    # textures
    #
    def test_txdef_unpack(self):
        textures = omg.txdef.Textures(self.wad.txdefs)
        
        texture = textures['AASHITTY']
        self.assertTrue(texture.patches[0].name == 'BODIES')
        pass
    
    def test_txdef_pack(self):
        textures = omg.txdef.Textures(self.wad.txdefs)
        textures.to_lumps()
        pass

# class TestUtil(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass


# class TestWad(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass


# class TestWadio(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass

if __name__=="__main__":
    unittest.main(verbosity=2)