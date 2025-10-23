# to verify everything is working fine

import pytest
import allure


@allure.title("Sample Testcase")
@allure.description("Test Sample description")
def test_sample_testcase():
    assert True == True
