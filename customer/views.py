from django.shortcuts import render, get_object_or_404, redirect
from .models import DeliveryPerson, Feedback
from django.http import HttpResponse
from .forms import FeedbackForm  

def create_feedback(request, delivery_person_id):
    delivery_person = get_object_or_404(DeliveryPerson, id=delivery_person_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.delivery_person = delivery_person
            feedback.save()
            return HttpResponse("Feedback submitted successfully.")
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form, 'delivery_person': delivery_person})

def feedback_list(request, delivery_person_id):
    delivery_person = get_object_or_404(DeliveryPerson, id=delivery_person_id)
    feedbacks = delivery_person.feedbacks.all()
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks, 'delivery_person': delivery_person})
