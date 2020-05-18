from rdmapper.rdmapper import initialize_smarts

class TestClass:

    def test_initialize_smarts(self):
        trg = "[#6]-[#8]"
        ans = "[#6:1]-[#8:2]"
        res, num = initialize_smarts(trg, 1)
        assert ans == res
        assert num == 3
        trg = "[#6]-[#7]-[#6](-[#6])=[#8]"
        ans = "[#6:1]-[#7:2]-[#6:3](-[#6:4])=[#8:5]"
        res, num = initialize_smarts(trg, 1)
        assert ans == res
        assert num == 6
        trg = "[#9]-[#6]1(-[#9])-[#6]-[#6]-[#6]-[#6]-[#6]-1"
        ans = "[#9:1]-[#6:2]1(-[#9:3])-[#6:4]-[#6:5]-[#6:6]-[#6:7]-[#6:8]-1"
        res, num = initialize_smarts(trg, 1)
        assert ans == res
        assert num == 9
        trg = "[#8]=[#6]1-[#6]-[#6]-[#6]-[#6]-[#6]-1"
        ans = "[#8:9]=[#6:10]1-[#6:11]-[#6:12]-[#6:13]-[#6:14]-[#6:15]-1"
        res, _ = initialize_smarts(trg, num)
        assert ans == res