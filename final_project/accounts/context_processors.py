from .models import MyUser, Patient

def id_request(request):
    return {
        'my_users': MyUser.objects.all(),
        'patient_users': Patient.objects.all()
    }