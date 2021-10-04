from expenses import calculate_mileage, get_reimbursement_amount, \
                     get_actual_trip_cost, get_actual_mileage_rate
from pytest import approx


def test_calculate_mileage():
    assert(calculate_mileage(-5, 3000) == 0)
    assert(calculate_mileage(8000, 4000) == 0)
    assert(calculate_mileage(13500, 13505) == 5)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(0) == 0)
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(35.5) == 20.41)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(35, 2.98) == 0.0851)
    assert(get_actual_mileage_rate(0, 3.00) == 0.0)
    assert(get_actual_mileage_rate(25, 0) == 0.0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(-3, 3000, 20, 3.85) == 0)
    approx(get_actual_trip_cost(39001, 40001, 35, 3.00) == 85.71)
