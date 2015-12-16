print('Omgifol Unit Tests')

import unittest, omg, random


# class TestColormap(unittest.TestCase):
#     def setUp(self):
#         pass
#         #self.col = omg.colormap.Colormap()

#     def test_to_lump(self):
#         pass
#         #lump = self.col.to_lump()
#         #self.assertTrue(lump is omg.Lump)


# class TestLump(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass

class TestMapeditReading(unittest.TestCase):
    def setUp(self):
        testwad = omg.WAD('test.wad')
        self.testmap = omg.mapedit.MapEditor(testwad.maps['MAP01'])

    def test_counts(self):
        self.assertTrue(len(self.testmap.things) == 103)
        self.assertTrue(len(self.testmap.linedefs) == 653)
        self.assertTrue(len(self.testmap.sidedefs) == 958)
        self.assertTrue(len(self.testmap.vertexes) == 581)
        self.assertTrue(len(self.testmap.segs) == 1030)
        self.assertTrue(len(self.testmap.ssectors) == 268)
        self.assertTrue(len(self.testmap.nodes) == 267)
        self.assertTrue(len(self.testmap.sectors) == 130)

class TestMapeditDrawSector(unittest.TestCase):
    def setUp(self):
        self.m = omg.mapedit.MapEditor()
        pass

    def test_draw_simple_sector(self):
        verts = []
        verts.append(omg.mapedit.Vertex(x=0,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=64))
        verts.append(omg.mapedit.Vertex(x=0,y=64))
        self.m.draw_sector(verts)
        self.assertTrue(len(self.m.vertexes) == 4)
        self.assertTrue(len(self.m.linedefs) == 4)
        self.assertTrue(len(self.m.sidedefs) == 4)
        self.assertTrue(len(self.m.sectors) == 1)
        
    def test_draw_sector_return_value(self):
        verts = []
        verts.append(omg.mapedit.Vertex(x=0,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=0))
        verts.append(omg.mapedit.Vertex(x=64,y=64))
        verts.append(omg.mapedit.Vertex(x=0,y=64))
        lines = self.m.draw_sector(verts)
        self.assertTrue(len(lines)==4)

    def test_draw_many_sectors(self):
        for x in range(100):
            self.m = omg.mapedit.MapEditor()
            n = random.randint(4,20)
            verts = []
            for x in range(n):
                verts.append(omg.mapedit.Vertex(x=random.randint(-30000,30000),y=random.randint(-30000,30000)))
            self.m.draw_sector(verts)
            self.assertTrue(len(self.m.vertexes) == n)
            self.assertTrue(len(self.m.linedefs) == n)
            self.assertTrue(len(self.m.sidedefs) == n)
            self.assertTrue(len(self.m.sectors) == 1)



# class TestPalette(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass


# class TestPlaypal(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass


# class TestTxdef(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_farts(self):
#         pass


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