
from app.main import sort_results, paginate

def test_sort_results_asc():
    data = [{"name": "B"}, {"name": "A"}]
    sorted_data = sort_results(data, "name")
    assert sorted_data[0]["name"] == "A"

def test_sort_results_desc():
    data = [{"name": "A"}, {"name": "B"}]
    sorted_data = sort_results(data, "-name")
    assert sorted_data[0]["name"] == "B"

def test_paginate():
    data = list(range(20))
    page = paginate(data, page=2, page_size=5)
    assert page == [5,6,7,8,9]
