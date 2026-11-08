from pydantic import BaseModel
from pydantic import ValidationError

class BookingResponse(BaseModel):
    bookingid: int
    totalprice: int
    depositpaid: bool

try:
    BookingResponse.model_validate({"bookingid": "abc", "totalprice": 1430, "depositpaid": False})
except ValidationError as e:
    print(e.errors())

# class BookingResponse(BaseModel):
#     bookingid: int
#     totalprice: int
#     depositpaid: bool
#
# incoming_data = {"bookingid": 777, "totalprice": 1430, "depositpaid": False}
#
# data = BookingResponse(**incoming_data)
# print(data)