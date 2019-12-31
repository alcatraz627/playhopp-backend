from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Customer, ForgotPass

from random import randint

def generate_code():
    # Generate a 6 digit random integer
    code = randint(1e5, 1e6)
    # If already being used, regenerate
    if ForgotPass.objects.filter(verif_code=code).count() > 0:
        code = generate_code()

    return code

@api_view(['POST'])
def check_username(request):
    if "username" not in request.data:
        return Response("Please provide a username", status=status.HTTP_400_BAD_REQUEST)

    c = Customer.objects.filter(username=request.data['username'])
    if c.count() == 0:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)

    c=c.first()

    # Check if a record for the user already exists and delete it if so
    chk = ForgotPass.objects.filter(customer=c)
    if chk.count() > 0: chk.delete()

    f = ForgotPass.objects.create(customer=c, verif_code=generate_code())
    # TODO: Send a mail

    print("Verif code generated: ", f.verif_code)
    return Response(f"An email has been sent to {c.username} with the verification code.")

@api_view(['POST'])
def verify_code(request):
    if "verif_code" not in request.data:
        return Response("Please provide a verification code", status=status.HTTP_400_BAD_REQUEST)

    verif_code = request.data['verif_code']
    f = ForgotPass.objects.filter(verif_code=verif_code)
    if f.count() == 0:
        return Response("Verification code does not match any record.", status=status.HTTP_404_NOT_FOUND)

    return Response("Email verified. Can reset password")


@api_view(['POST'])
def update_password(request):
    # Check for verif code in payload
    if "verif_code" not in request.data:
        return Response("Please provide a verification code", status=status.HTTP_400_BAD_REQUEST)

    # Check for new password in payload
    if "password" not in request.data:
        return Response("Please provide a new password", status=status.HTTP_400_BAD_REQUEST)

    verif_code = request.data['verif_code']
    password = request.data['password']

    # Check if verif code is valid
    f = ForgotPass.objects.filter(verif_code=verif_code)
    if f.count() == 0:
        return Response("Verification code invalid.", status=status.HTTP_404_NOT_FOUND)

    customer = f.first().customer
    if customer.check_password(password):
        return Response("Cannot update to the same password as before.", status=status.HTTP_400_BAD_REQUEST)

    customer.set_password(request.data['password'])
    customer.save()

    f.first().delete()

    return Response("Email verified. Can reset password")



