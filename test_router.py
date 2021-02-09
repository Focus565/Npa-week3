import pytest
import router
def test_init():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    assert r1.brand == 'Cisco', "test failed"
    assert r1.model == 'IOSv', "test failed"
    assert r1.hostname == 'R1', "test failed"

    r2 = router.Router('Cisco', '3745', 'R2')
    assert r2.brand == 'Cisco', "test failed"
    assert r2.model == '3745', "test failed"
    assert r2.hostname == 'R2', "test failed"

    r3 = router.Router('Juniper', 'Mx5', 'R3')
    assert r3.brand == 'Juniper', "test failed"
    assert r3.model == 'Mx5', "test failed"
    assert r3.hostname == 'R3', "test failed"
def test_add_inf():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    assert r1.add_inf('Gigabit 0/1') == True, "test failed"
    assert r1.add_inf('Gigabit 0/2') == True, "test failed"
    assert r1.add_inf('Gigabit 0/3') == True, "test failed"
    assert r1.add_inf('Gigabit 0/1') == False, "test failed"

    r2 = router.Router('Cisco', '3745', 'R2')
    assert r2.add_inf('Gigabit 0/1') == True, "test failed"


def test_remove_inf():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r1.add_inf('Gigabit 0/3')
    assert r1.remove_inf('Gigabit 0/1') == True, "test failed"
    assert r1.remove_inf('Gigabit 0/1') == False, "test failed"

def test_show_inf():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r1.add_inf('Gigabit 0/3')
    r2 = router.Router('Cisco', '3745', 'R2')
    r2.add_inf('Gigabit 0/1')
    r3 = router.Router('Juniper', 'Mx5', 'R3')

    assert r1.show_infs() == "Show interface of R1\nR1 has 3 interfaces\nGigabit 0/1\nGigabit 0/2\nGigabit 0/3\n"
    assert r2.show_infs() == "Show interface of R2\nR2 has 1 interfaces\nGigabit 0/1\n"
    assert r3.show_infs() == "Show interface of R3\nR3 has 0 interfaces\n"

def test_connect():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r1.add_inf('Gigabit 0/3')
    r2 = router.Router('Cisco', '3745', 'R2')
    r2.add_inf('Gigabit 0/1')
    r2.add_inf('Gigabit 0/2')
    r3 = router.Router('Juniper', 'Mx5', 'R3')
    r3.add_inf('Gigabit 0/1')

    assert r1.connect('Gigabit 0/1', r2, 'Gigabit 0/2') == True, "test failed"
    assert r1.connect('Gigabit 0/2', r3, 'Gigabit 0/1') == True, "test failed"
    assert r1.connect('Gigabit 0/3', r3, 'Gigabit 0/1') == False, "test failed"
    assert r3.connect('Gigabit 0/2', r1, 'Gigabit 0/3') == False, "test failed"
    assert r2.connect('Gigabit 0/2', r3, 'Gigabit 0/2') == False, "test failed"

def test_show_cdp():
    r1 = router.Router('Cisco', 'IOSv', 'R1')
    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r1.add_inf('Gigabit 0/3')
    r2 = router.Router('Cisco', '3745', 'R2')
    r2.add_inf('Gigabit 0/1')
    r2.add_inf('Gigabit 0/2')
    r3 = router.Router('Juniper', 'Mx5', 'R3')
    r3.add_inf('Gigabit 0/1')

    r1.connect('Gigabit 0/1', r2, 'Gigabit 0/2')
    r1.connect('Gigabit 0/2', r3, 'Gigabit 0/1')
    r1.connect('Gigabit 0/3', r3, 'Gigabit 0/1')
    r3.connect('Gigabit 0/2', r1, 'Gigabit 0/3')
    r2.connect('Gigabit 0/2', r3, 'Gigabit 0/2')

    assert r1.show_cdp() == "R1 interface Gigabit 0/1 connect to R2 on interface Gigabit 0/2\nR1 interface Gigabit 0/2 connect to R3 on interface Gigabit 0/1\n", "test failed"
    assert r2.show_cdp() == "R2 interface Gigabit 0/2 connect to R1 on interface Gigabit 0/1\n", "test failed"
    assert r3.show_cdp() == "R3 interface Gigabit 0/1 connect to R1 on interface Gigabit 0/2\n", "test failed"