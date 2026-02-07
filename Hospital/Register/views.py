
from django.shortcuts import render
from .models import Patient, Doctor, Slot, Bookings
from django.http import JsonResponse
from .models import Slot, Bookings

def Index(request):
    doctors = Doctor.objects.all()
    slots = Slot.objects.all()
    return render(request, "index.html", {"doctors": doctors, "slots": slots})

def Home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        date = request.POST.get("date")
        concerns = request.POST.get("concerns")
        phone_number = request.POST.get("phone")
        doctor_name = request.POST.get("doctor")
        print(doctor_name)
        slot_name = request.POST.get("slot")     
        doctor = Doctor.objects.get(Id=doctor_name)
        print(doctor)     
        slot = Slot.objects.get(Start_time=slot_name)
        patient = Patient.objects.filter(Phone_Number=phone_number).first()      
        if not patient:

                patient_full=Patient.objects.create(
                    Name=name,
                    Age=age,
                    gender=gender,
                    Concerns=concerns,
                    Phone_Number=phone_number
                )          
                Bookings.objects.create(
                        Patient_Id=patient_full,
                        Doctor_Id=doctor,
                        Slot_Id=slot,
                        Date =date
                    )
        else:
             Bookings.objects.create(
                        Patient_Id=patient,
                        Doctor_Id=doctor,
                        Slot_Id=slot,
                        Date =date
                    )
        
    return render(request, "success.html", {"name": name,"age":age,"date":date ,"concerns": concerns,"doctor_name":doctor.Name,"time":slot_name})

def get_available_slots(request):
    doctor_id = request.GET.get("doctor_id")
    date = request.GET.get("date")
    
    try:
        booked_slot_ids = Bookings.objects.filter(
        Doctor_Id=doctor_id,
        Date=date
        ).values_list("Slot_Id_id", flat=True)  

        booked_slots = Slot.objects.filter(Slot_Id__in=booked_slot_ids) 

        available_slots = Slot.objects.exclude(Slot_Id__in=booked_slot_ids) 

        slots_data = [
        {
            "id": slot.Slot_Id,
            "start": slot.Start_time.strftime("%H:%M"),
            "end": slot.End_time.strftime("%H:%M")
        }
        for slot in available_slots
    ]   
        booked_data = [
        {
            "id": slot.Slot_Id,
            "start": slot.Start_time.strftime("%H:%M"),
            "end": slot.End_time.strftime("%H:%M")
        }
        for slot in booked_slots
    ]   
        return JsonResponse({
        "slots": slots_data,
        "book": booked_data
        })

    except Exception as e:
 
        print("Error in get_available_slots:", e)
        return JsonResponse({"slots": [], "error": str(e)}, status=500)
