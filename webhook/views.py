import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Webhook


@csrf_exempt
def webhook_payment(request):
    # Check authorization header before continue

    if request.method == "POST":
        # Get the data from the request and save to Webhook model
        json_data = json.loads(request.body)

        # Create a new webhook
        webhook = Webhook.objects.create(
            webhook_type="payments",
            event_type="payment_completed",
            resource_type="MyResource",
            event_data=json_data
        )

        # Return a json response with code ok and the event data if needed
        return JsonResponse(
            {"code": 200, "message": "Webhook recived", "data": webhook.event_data}
        )
    else:
        return JsonResponse(
            {"code": 400, "message": "Bad request"}
        )
