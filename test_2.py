import pytest
from task2 import check_post_id



def test_step1(real_post_id, autorization):
    assert real_post_id in check_post_id(autorization)

def test_step2(new_description, create_newpost):
    assert new_description in create_newpost


if __name__ == "__main__":
    pytest.main(["-vv"])