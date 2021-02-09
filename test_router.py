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