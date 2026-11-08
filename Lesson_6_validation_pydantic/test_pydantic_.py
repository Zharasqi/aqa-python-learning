# import pytest
# from pydantic import BaseModel, ValidationError
#
# class BookingResponse(BaseModel):
#     bookingid: int
#     totalprice: int
#     depositpaid: bool
#
# def test_booking_valid():
#     raw_data = {"bookingid": 777, "totalprice": 1430, "depositpaid": False}
#     booking = BookingResponse.model_validate(raw_data)
#     assert booking.bookingid == 777
#     assert booking.depositpaid is False
#
# def test_booking_invalid():
#     bad_data = {"bookingid": "not_a_number", "totalprice": 1430, "depositpaid": False}
#     with pytest.raises(ValidationError) as exp_info:
#         BookingResponse.model_validate(bad_data)
#     assert exp_info.value.errors()[0]["loc"] == ("bookingid",)
#
